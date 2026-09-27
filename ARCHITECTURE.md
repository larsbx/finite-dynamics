# Repository architecture

This repository adopts the estate repository template `estate-repository-v1`,
whose canonical source is `larsbx/estate-governance`.

The machine-readable source of repository structure and authority is
[`estate.toml`](estate.toml). The reusable contract is
[`docs/architecture/estate-repository-template-v1.md`](docs/architecture/estate-repository-template-v1.md),
vendored byte-for-byte and pinned by sha256 in the `[governance]` table of
`estate.toml`. Do not edit it or `tools/audit_estate_layout.py` locally; change
them in governance and re-vendor.

The ordering rule is:

```text
authority -> mathematical/domain concern -> implementation language
```

Julia is canonical only for the lab's own registry and binding validation
(`src/JuliaOracleLab.jl`). Every oracle is non-authoritative: it may return
`agrees`, `disagrees`, `inconclusive`, or `oracle_error`, never an acceptance
verdict (`docs/AUTHORITY_BOUNDARY.md`).

Oracles live under `oracles/<domain>/`, outside the package's `src/`, which
holds only the kernel; `src/JuliaOracleLab.jl` includes them from there.

The layout is canonical: every plane in `estate.toml` maps exactly its `target`
(root-level files aside), every top-level directory is some plane's target, and
no migration step is pending; the audit enforces all three. Directory renames
alone must not change claim status, acceptance, or authority.
