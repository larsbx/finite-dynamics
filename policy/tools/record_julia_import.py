#!/usr/bin/env python3
"""Record a successful experiment; called only after every migration gate passes."""
from pathlib import Path
import os
import subprocess

ROOT = Path(__file__).resolve().parents[2]
SOURCE = '8acb50fc2fea52077a2f3afc9c8407dc07cee799'

def record():
    for relative in ('policy/source-locks.toml', 'programs/julia-oracle/PROGRAM.toml'):
        path = ROOT / relative
        text = path.read_text()
        marker = 'commit = "' + SOURCE + '"\nauthority = "retained"\nimport_status = "not_started"'
        assert text.count(marker) == 1
        path.write_text(text.replace(marker, marker.replace('not_started', 'verified')))
    inventory = ROOT / 'policy/migration-inventory.toml'
    inventory.write_text(inventory.read_text() + '\n[history_import_experiment]\nprogram = "julia-oracle"\nstatus = "verified"\nsource_authority = "retained"\nmethod = "unsquashed_subtree"\nsource_commits = 61\nsource_files = 24\nevidence = "docs/migration/julia-oracle-history-import.md"\n')
    history = subprocess.check_output(['git', '-C', str(ROOT), 'rev-list', '--parents', '--first-parent', '--merges', 'HEAD'], text=True)
    merge = next(line.split()[0] for line in history.splitlines() if line.split()[2:] == [SOURCE])
    tree = subprocess.check_output(['git', '-C', str(ROOT), 'rev-parse', SOURCE + '^{tree}'], text=True).strip()
    version = subprocess.check_output(['julia', '--version'], text=True).strip()
    run = f'https://github.com/{os.environ["GITHUB_REPOSITORY"]}/actions/runs/{os.environ["GITHUB_RUN_ID"]}'
    (ROOT / 'docs/migration/julia-oracle-history-import.md').write_text(f'''# Julia oracle history import experiment

Source: `larsbx/julia-oracle-lab`, locked head `{SOURCE}`.
Source authority: **retained**. Claim namespace: **JO**.

## History and content

Unsquashed subtree merge: `{merge}`. The original source head is the second
parent, preserving all 61 reachable commits and their original IDs and merge topology.
Source tree: `{tree}`. All 24 source files, including the original workflows,
remain byte-for-byte and mode-for-mode identical under `programs/julia-oracle/`.
`PROGRAM.toml` is workspace metadata added alongside that original tree.
No source gate, registry entry, theorem status, or acceptance boundary was rewritten.
Release tags, hosted releases, and issues remain at the source; they were not transferred.

## Verification

[Verification run]({run}) used `{version}` and reproduced:

- Original locked checkout: pinned estate audit and `Pkg.test()`.
- Imported program: the same pinned estate audit and Julia 1.11 `Pkg.test()`.
- Consolidated workspace: pinned estate audit.
- Import guard: source ancestry, 61 commits, 24 exact Git objects and working files,
  JO namespace, retained authority, and metadata-only private boundaries.

The original estate artifact digest is
`7dff31575b2834b937395f3ff6f7ce2e2d1d7927b893cf8229c682ad7f3a99d2`;
the workspace digest is
`2b63d6f4d399e03f860858f90fdffd3e6f26dd9844d5f0e10b6b40718467be0c`.
Both public artifacts are fetched at immutable commits and verified before execution.
The root workflow `.github/workflows/julia-oracle.yml` repeats all gates on every PR
and main push with full history and read-only credentials. Imported nested workflows
are preserved historical files; they are not automatically executed by GitHub.

## Authority and next decision

`verified` records this import experiment, not an authority transfer. Julia is canonical
for registry/binding validation inside the lab and remains a non-authoritative oracle
for consuming programs. The JO namespace and both `acceptance_authority = false`
settings are preserved. Private programs are untouched. No source is archived.
Review this public experiment before selecting another program or changing authority.
Merge this PR with a merge commit: squash or rebase would discard source ancestry.
''')
    path = ROOT / 'docs/migration/source-authority-inventory.md'
    path.write_text(path.read_text() + '\n## First history-import experiment\n\nJulia oracle is imported and verified; source authority remains **retained**.\nAll 61 original commits and 24 exact files are preserved. Original-source,\nimported-program, and consolidated-workspace gates passed before this status was\nrecorded. See [the verification record](julia-oracle-history-import.md).\nThe remaining programs are still `not_started`; no private content was imported.\n')
    path = ROOT / 'README.md'
    path.write_text(path.read_text().replace('This repository currently contains migration boundaries and source locks only.', 'The first verified history import is Julia Oracle Lab under `programs/julia-oracle/`,\nwith all original commits preserved. Other programs still contain migration metadata only.') + '\nSee the [Julia oracle import verification](docs/migration/julia-oracle-history-import.md).\n')
    path = ROOT / 'ARCHITECTURE.md'
    path.write_text(path.read_text().replace('No mathematical implementation, proof record, result register, release, or issue\nauthority has moved here yet.', 'Julia oracle history and executable files have been imported and verified.\nNo mathematical implementation, proof record, result register, release, or issue\nauthority has moved here yet.'))

if __name__ == '__main__':
    record()
