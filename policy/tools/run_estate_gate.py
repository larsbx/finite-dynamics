#!/usr/bin/env python3
"""Fetch immutable public estate artifacts and check their digest before execution."""
import hashlib
from pathlib import Path
import subprocess
import sys
import tempfile
import tomllib
import urllib.request

# estate-governance revision -> sha256 of kernel/audit_estate_layout.py at that revision.
AUDIT_DIGESTS = {
    '0833929ed82d42cf3674a1565681625a9622827b': '7dff31575b2834b937395f3ff6f7ce2e2d1d7927b893cf8229c682ad7f3a99d2',
    '63b5605c33af726317a193c303708a37f93d7394': '2b63d6f4d399e03f860858f90fdffd3e6f26dd9844d5f0e10b6b40718467be0c',
    '5ea47dec8086eab6a1dad6fd239688d20ea89891': '412a64dea58d709aae21e5a0315b8e7e96488c310a9d999267927ba3d8146a30',
}

def run(root):
    root = Path(root).resolve()
    manifest = tomllib.loads((root / 'ESTATE.toml').read_text())
    dependency = next(d for d in manifest['dep'] if d['id'] == 'estate-governance')
    revision = dependency['rev']
    digest = AUDIT_DIGESTS[revision]
    assert dependency['pin'] == 'sha256:' + digest, 'unexpected estate pin'
    url = f'https://raw.githubusercontent.com/larsbx/estate-governance/{revision}/kernel/audit_estate_layout.py'
    with urllib.request.urlopen(url, timeout=60) as response:
        content = response.read()
    assert hashlib.sha256(content).hexdigest() == digest, 'estate artifact digest mismatch'
    with tempfile.TemporaryDirectory() as temp:
        artifact = Path(temp) / 'estate-audit.py'
        artifact.write_bytes(content)
        subprocess.run([sys.executable, str(artifact), '--root', str(root)], check=True)

if __name__ == '__main__':
    run(sys.argv[1])
