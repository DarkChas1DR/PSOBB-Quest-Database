# Hildebear

DAT ID **0x0040 / 64**, constructor **TObjEneMoja**.

[Definition source](../../quest-knowledge/reference/server-source/Map.cc#L2789) · [Database index](../monsters.md)

## Source-documented areas

Episode 1: Forest 2 (area 0x02, default floor 2); Episode 1: Spaceship (area 0x10, default floor 16); Episode 1: Palace (area 0x11, default floor 17); Episode 2: VR Temple Alpha (area 0x13, default floor 1); Episode 2: VR Temple Beta (area 0x14, default floor 2)

Floor numbers are script slots. Resolve the quest map designation to an area before checking compatibility. Custom client patches may change constructor availability; this table describes the stored reference, not a live client test.

## Parameters and source notes

```text
Hildebear. Params:
param1 = initial location (zero or negative = ground, positive = jump)
param2 = chance to use tech (value is param3 + 0.6, clamped to [0, 1]; TODO: it's not clear when exactly the
decision points are)
param3 = chance to jump when more than 150 units away (value is param2 + 0.3, clamped to [0, 1])
param6 = if >= 1, always rare

```

## Observed quest placements

2686 records, including language duplicates. These are observations, not spawn permissions.

[All observed positions, angles, parameters and handler candidates](../observations/0040.csv)

| Quest | Floor | Room / wave | Handler candidate |
|---|---:|---|---|
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 2 / 1 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 2 / 2 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 2 / 2 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 2 / 3 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 6 / 1 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 6 / 2 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 6 / 2 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 6 / 2 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 6 / 2 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 6 / 2 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 6 / 5 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 7 / 2 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 15 / 5 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 15 / 5 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 15 / 5 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 12 / 1 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 12 / 1 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 12 / 2 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 12 / 2 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 12 / 3 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 12 / 3 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 12 / 4 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 12 / 4 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 12 / 12 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 12 / 12 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 12 / 12 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 12 / 13 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 12 / 14 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 12 / 14 | — |
| [Test/q37-bb-j](../../server-catalogue/Test/q37-bb-j/README.md) | 2 | 2 / 1 | — |
