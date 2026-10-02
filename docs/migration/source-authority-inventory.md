# Finite-dynamics source authority inventory

Captured: 2026-10-01. This is a bounded inventory of the immutable source heads
recorded in `policy/source-locks.toml`. It does not transfer authority.

| Program | Visibility | Files | Source head | Existing acceptance surface |
| --- | --- | ---: | --- | --- |
| finite-mandelbrot | public | 413 | `3500d660a1ebc5e16c61910ebdfcbbbc0721aec0` | Six-plane workflow: policy, canonical Mojo kernel, proof ledger, references/oracles, paper, integration |
| finite-julia | private | 152 | `04db96236fd5c583414905b7014f05a4f9b00a75` | Mojo build/smoke, exact arithmetic, reference resolution, terminology, generated corpus, differential replay |
| bulb-ford | private | 117 | `449611eddb4e1a0fa7f5bd14c5a97d4362d9df6b` | Estate audit, finite-register no-limits audit, Python tests |
| julia-oracle | public | 24 | `8acb50fc2fea52077a2f3afc9c8407dc07cee799` | Estate audit and Julia 1.11 package tests |

## Non-negotiable migration gates

- Preserve complete source histories; a snapshot copy is insufficient.
- Preserve each program's claim and theorem-status namespace.
- Reproduce every listed source gate from the imported history.
- Do not allow an oracle or reference implementation to become acceptance authority.
- Do not publish files imported from a private repository without a separate disclosure decision.
- Keep source authority marked `retained` until its imported program passes both its
  original gates and the consolidated workspace gate.
- Treat cross-program shared code as an explicit dependency, not an opportunistic copy.

## Import order

1. **Julia oracle** — smallest public program; validates the history-import and path-filter design.
2. **Finite Mandelbrot** — public but authority-rich; validates claim, proof, paper, and Mojo boundaries.
3. **Finite Julia** — private; import only after the public repository disclosure boundary is decided.
4. **Bulb/Ford** — private and experiment-heavy; import after result-register collision and provenance rules are settled.

The machine-readable gate inventory is `policy/migration-inventory.toml`.

## First history-import experiment

Julia oracle is imported and verified; source authority remains **retained**.
All 61 original commits and 24 exact files are preserved. Original-source,
imported-program, and consolidated-workspace gates passed before this status was
recorded. See [the verification record](julia-oracle-history-import.md).
The remaining programs are still `not_started`; no private content was imported.
