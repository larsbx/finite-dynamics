"""Negative controls for content, authority and public-disclosure import gates."""
import contextlib
import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('import_guard', ROOT / 'policy/tools/verify_julia_import.py')
guard = importlib.util.module_from_spec(spec)
spec.loader.exec_module(guard)


class ImportGuardTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.root = Path(cls.temp.name) / 'workspace'
        subprocess.run(['git', 'clone', '--quiet', '--no-hardlinks', str(ROOT), str(cls.root)], check=True)
        guard.ROOT = cls.root

    @classmethod
    def tearDownClass(cls):
        guard.ROOT = ROOT
        cls.temp.cleanup()

    @contextlib.contextmanager
    def altered(self, relative, old=None, new=None):
        path = self.root / relative
        content = path.read_bytes()
        try:
            if old is None:
                path.write_bytes(content + b'\n# corrupted import\n')
            else:
                self.assertIn(old, content.decode())
                path.write_text(content.decode().replace(old, new))
            yield
        finally:
            path.write_bytes(content)

    def test_original_import_passes(self):
        guard.verify()

    def test_corrupted_original_content_is_rejected(self):
        with self.altered('programs/julia-oracle/src/JuliaOracleLab.jl'):
            with self.assertRaisesRegex(AssertionError, 'working file changed'):
                guard.verify()

    def test_namespace_collision_is_rejected(self):
        with self.altered('ESTATE.toml', 'claim_namespace = "JO"', 'claim_namespace = "FM"'):
            with self.assertRaises(AssertionError):
                guard.verify()

    def test_transferred_source_authority_is_rejected(self):
        with self.altered('programs/julia-oracle/PROGRAM.toml', 'authority = "retained"', 'authority = "transferred"'):
            with self.assertRaises(AssertionError):
                guard.verify()

    def test_oracle_acceptance_authority_is_rejected(self):
        old = 'name = "Julia"\nauthority = "supporting"\nroles = ["oracle"]\nacceptance_authority = false'
        with self.altered('ESTATE.toml', old, old.replace('false', 'true')):
            with self.assertRaises(AssertionError):
                guard.verify()

    def test_private_content_is_rejected(self):
        path = self.root / 'programs/finite-julia/disclosure-negative-control.txt'
        try:
            path.write_text('negative control')
            with self.assertRaises(AssertionError):
                guard.verify()
        finally:
            path.unlink()

    def test_snapshot_without_source_ancestry_is_rejected(self):
        subprocess.run(['git', '-C', str(self.root), 'checkout', '--quiet', '--detach', '14eed27ce37e8910ba8d41235036f0a1e9ae6cfb'], check=True)
        try:
            with self.assertRaises(subprocess.CalledProcessError):
                guard.verify()
        finally:
            subprocess.run(['git', '-C', str(self.root), 'checkout', '--quiet', '-'], check=True)


if __name__ == '__main__':
    unittest.main()
