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
| `finite-julia` (FJ) | §1.3, §1.5, §3, §4 | public survey questions on Julia-set geometry, local connectivity and measure; implementation assessment deferred pending an explicit disclosure decision |
| `bulb-ford` (BFC) | §1.7, §8 | see below |
| `julia-oracle` (JO) | — | no direct survey item; its parabolic-index oracle is the natural cross-check for the Julia program's parabolic completeness work |

Shared kernels (`larsbx/finite-math-kernels`): `F_p[x]` with distinct-degree
factorisation, a Galois-witness checker, power series over `Q` with `ν_2`, and
rotor continued-fraction prefixes (exact data).

## bulb-ford and limb geometry

The program is metadata-only here (`programs/bulb-ford/PROGRAM.toml`, import not
started) and its source repository is private, so this is a routing note, not
an assessment of its content. Private-source implementation and dependency
details require an explicit disclosure decision under `ARCHITECTURE.md`.

The survey's limb question (§1.7) is:

```text
diam L_{p/q} = O(1/q²)     (Milnor's conjecture, as stated by Kapiamba)
```

- Kapiamba's 2023 dissertation proves the quadratic bound for all `p/q`-limbs
  whose finite continued fractions have uniformly bounded length; see the
  [University of Michigan defense abstract (June 13, 2023)](https://lsa.umich.edu/math/news-events/all-events.detail.html/108447-21819600.html).
  For each fixed length bound `N`, the estimate is `diam L_{p/q} ≤ C_N/q²`;
  the constant may depend on `N`. The earlier `L_{1/q}` result (2021 preprint)
  is a special case. [Kapiamba, arXiv:2103.03211v4, Theorem 1.3](https://arxiv.org/html/2103.03211v4)
  states this bounded-length result using modified continued fractions.
  The general Pommerenke–Levin–Yoccoz inequality gives `O(1/q)`.
- Bounded length limits the number of continued-fraction entries, while
  bounded type limits their values. The survey's bounded-type target
  (partial quotients `≤ A`, with no length bound) does not follow from
  the bounded-length theorem. The unrestricted `O(1/q²)` bound remains
  conjectural; neither target is established by the cited bounded-length
  result.
- The heuristic that the bulb is close to a disc of radius `≈ sin(πp/q)/q²` is
  numerically very good and unproved. The Ford-circle scaling `1/(2q²)` at `p/q`
  matches its order in `q`.
- Survey attack surface 1 asks for high-precision numerics of
  `κ(p/q) = q² · diam L_{p/q} / sin(πp/q)`, and for whether `κ` is continuous in
  the Farey/Ford picture.

The routing and evidence boundaries are:

1. A computed `κ` table is finite numerical evidence. It does not prove an
   asymptotic bound outside the proved bounded-length regime or provide a
   constant uniform over unbounded lengths.
2. Keep the proved bounded-length regime (including `1/q`), the conjectural
   bounded-type target at unbounded lengths, and the unrestricted conjecture
   distinct. A bound on each finite length separately does not give a single
   constant for all lengths.
3. Assess private-source implementations and propose shared dependencies only
   after an explicit disclosure decision is recorded. This note routes the
   public limb question without those repository-derived details.

## Not routed

`larsbx/semantic-categorical-oracle` has no survey item. An advisory comparison
of kneading and tuning data across publicly disclosed implementations could be
considered once shared vectors are specified. Such an oracle would carry no
domain authority. Nothing is registered.
