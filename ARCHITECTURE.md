# Finite dynamics architecture

This repository is a multi-program consolidation pilot governed by
estate-repository-v2. Durable research concerns live under `programs/<id>/`;
branches are temporary change lines.

## Authority state

No mathematical implementation, proof record, result register, release, or issue
authority has moved here yet. Each `PROGRAM.toml` identifies its source repository
and immutable staging commit. Those source repositories remain authoritative until
a reviewed migration proves history preservation and reproduces their original gates.

## Public-boundary rule

This repository is public. Metadata may name the migration sources, but content from
a private source repository must not be copied here without an explicit disclosure
decision. The initial scaffold contains no private source content.

## Migration gates

1. Pin source heads and enumerate files, claims, releases, issues, and CI gates.
2. Design history-preserving imports under the declared program roots.
3. Resolve shared code through explicit dependency interfaces.
4. Run each source repository's acceptance, theorem-status, and provenance gates.
5. Transfer authority program by program; never by a bulk repository switch.
6. Archive a source only after redirects and immutable provenance are published.
