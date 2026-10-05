# Survey assessment — workspace view (2026-10-05)

Status: exposition. Authority: none. The source repositories stay authoritative
(`ARCHITECTURE.md`); this note only routes the survey to the programs.

Source: the external open-problems survey stored verbatim in
`larsbx/finite-mandelbrot-research` as
`docs/literature/open-problems-survey-2026-10.md` (status October 2026). Each
source repository holds its own assessment as
`docs/survey-assessment-2026-10-05.md`. The survey is not copied here; it
arrives with the finite-mandelbrot import.

## Routing

| Program | Survey sections | Direction (details in the source repository's assessment) |
|---|---|---|
| `finite-mandelbrot` (FM) | §1.1–1.5, §4, §6 | C1 residual exits labelled by the field's open split (Dudko Problems 4.3/4.4); eventually periodic directives as finite names of bounded-type parameters; interior completeness restated as DH-strength; certified `S_d` Galois groups and Gleason `n = 11…14` |
| `finite-julia` (FJ) | §1.3, §1.5, §3, §4 | residual-measure completeness per regime (zero-area tag); `niven` recorded as finite-data undecidable (tail property; Braverman–Yampolsky); roadmap housekeeping |
| `bulb-ford` (BFC) | §1.7, §8 | see below |
| `julia-oracle` (JO) | — | no direct survey item; its parabolic-index oracle is the natural cross-check for the Julia program's parabolic completeness work |

Shared kernels (`larsbx/finite-math-kernels`): `F_p[x]` with distinct-degree
factorisation, a Galois-witness checker, power series over `Q` with `ν_2`, and
rotor continued-fraction prefixes.

## bulb-ford and limb geometry

The program is metadata-only here (`programs/bulb-ford/PROGRAM.toml`, import not
started) and its source repository is private, so this is a routing note, not
an assessment of its content.

The survey's limb question (§1.7) is:

```text
diam L_{p/q} = O(1/q²)     (Milnor's conjecture, as stated by Kapiamba)
```

- Proved only for the family `L_{1/q}` (Kapiamba, arXiv:2103.03211). The
  Pommerenke–Levin–Yoccoz inequality gives `O(1/q)`.
- The heuristic that the bulb is close to a disc of radius `≈ sin(πp/q)/q²` is
  numerically very good and unproved. The Ford-circle scaling `1/(2q²)` at `p/q`
  matches its order in `q`.
- Survey attack surface 1 asks for high-precision numerics of
  `κ(p/q) = q² · diam L_{p/q} / sin(πp/q)`, and for whether `κ` is continuous in
  the Farey/Ford picture.

When the program is imported, three discipline points follow from the survey
and from the estate's no-limits audit:

1. A computed `κ` table is finite data, never evidence for `O(1/q²)` beyond the
   `1/q` family.
2. Statements must separate the proved family (`1/q`), the bounded-type target
   (partial quotients `≤ N`), and the conjecture.
3. Brjuno sums and continued-fraction code in that repository (listed in
   `larsbx/finite-math-kernels` `docs/vendoring-candidates-2026-10-05.md`) are
   the same upstream candidate as the rotor continued-fraction kernel. One
   kernel should serve both consumers.

## Not routed

`larsbx/semantic-categorical-oracle` has no survey item. One advisory candidate
follows from the routing above: the kneading and tuning computations now exist
in three places (the FM residual directive carrier, FJ kneading-and-tuning, and
the kernels' `substitution_dynamics`). An advisory oracle comparing them on
shared vectors would carry no domain authority. Nothing is registered.
