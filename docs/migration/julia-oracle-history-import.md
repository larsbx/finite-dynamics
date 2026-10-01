# Julia oracle history import experiment

Source: `larsbx/julia-oracle-lab`, locked head `8acb50fc2fea52077a2f3afc9c8407dc07cee799`.
Source authority: **retained**. Claim namespace: **JO**.

## History and content

Unsquashed subtree merge: `8280358cfcb157ea977144aa7f3de3fc55695739`. The original source head is the second
parent, preserving all 61 reachable commits and their original IDs and merge topology.
Source tree: `159c09ab402ca4613617dbd3121fd2e17c8f1437`. All 24 source files, including the original workflows,
remain byte-for-byte and mode-for-mode identical under `programs/julia-oracle/`.
`PROGRAM.toml` is workspace metadata added alongside that original tree.
No source gate, registry entry, theorem status, or acceptance boundary was rewritten.
Release tags, hosted releases, and issues remain at the source; they were not transferred.

## Verification

[Verification run](https://github.com/larsbx/finite-dynamics/actions/runs/36925391425) used `julia version 1.11.9` and reproduced:

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
