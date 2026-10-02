#!/usr/bin/env python3
"""Verify the first public history import without promoting oracle authority."""
from pathlib import Path
import subprocess
import tomllib

ROOT = Path(__file__).resolve().parents[2]
SOURCE = '8acb50fc2fea52077a2f3afc9c8407dc07cee799'
PREFIX = 'programs/julia-oracle/'

def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args])

def verify():
    locks = tomllib.loads((ROOT / 'policy/source-locks.toml').read_text())
    oracle = next(p for p in locks['source'] if p['program'] == 'julia-oracle')
    assert oracle['repository'] == 'larsbx/julia-oracle-lab'
    assert oracle['commit'] == SOURCE and oracle['authority'] == 'retained'
    git('merge-base', '--is-ancestor', SOURCE, 'HEAD')
    assert int(git('rev-list', '--count', SOURCE)) == 61
    files = git('ls-tree', '-r', '-z', SOURCE).split(b'\0')
    assert len([f for f in files if f]) == 24
    for entry in filter(None, files):
        metadata, name = entry.split(b'\t', 1)
        mode, kind, sha = metadata.decode().split()
        path = name.decode()
        imported = git('ls-tree', 'HEAD', '--', PREFIX + path).decode().strip()
        assert imported.split('\t')[0] == metadata.decode(), f'import object changed: {path}'
        assert git('hash-object', str(ROOT / PREFIX / path)).decode().strip() == sha, f'working file changed: {path}'
    estate = tomllib.loads((ROOT / 'ESTATE.toml').read_text())
    program = next(p for p in estate['program'] if p['id'] == 'julia-oracle')
    assert program['claim_namespace'] == 'JO'
    assert program['canonical_language'] == 'Julia'
    assert next(l for l in estate['language'] if l['name'] == 'Julia')['acceptance_authority'] is False
    imported = tomllib.loads((ROOT / PREFIX / 'ESTATE.toml').read_text())
    assert next(l for l in imported['language'] if l['name'] == 'Julia')['acceptance_authority'] is False
    manifest = tomllib.loads((ROOT / PREFIX / 'PROGRAM.toml').read_text())
    assert manifest['source']['commit'] == SOURCE
    assert manifest['source']['authority'] == 'retained'
    # Private boundaries are still metadata-only, including the index.
    for name in ('finite-julia', 'bulb-ford'):
        assert [p.name for p in (ROOT / 'programs' / name).iterdir()] == ['PROGRAM.toml']
        assert git('ls-tree', '-r', '--name-only', 'HEAD', '--', f'programs/{name}/').decode().splitlines() == [f'programs/{name}/PROGRAM.toml']
    print('Julia import verified: 61 original commits, 24 exact files, JO namespace, retained authority, private boundaries untouched')

if __name__ == '__main__':
    verify()
