# Rag Rappy / Sand Rappy

DAT ID **0x0041 / 65**, constructor **TObjEneLappy**.

[Definition source](../../quest-knowledge/reference/server-source/Map.cc#L2806) · [Database index](../monsters.md)

## Source-documented areas

Episode 1: Forest 1 (area 0x01, default floor 1); Episode 1: Forest 2 (area 0x02, default floor 2); Episode 2: VR Temple Alpha (area 0x13, default floor 1); Episode 2: VR Temple Beta (area 0x14, default floor 2); Episode 4: Crater (Eastern Route) (area 0x24, default floor 1); Episode 4: Crater (Western Route) (area 0x25, default floor 2); Episode 4: Crater (Southern Route) (area 0x26, default floor 3); Episode 4: Crater (Northern Route) (area 0x27, default floor 4); Episode 4: Crater Interior (area 0x28, default floor 5); Episode 4: Subterranean Desert 1 (area 0x29, default floor 6); Episode 4: Subterranean Desert 2 (area 0x2A, default floor 7); Episode 4: Subterranean Desert 3 (area 0x2B, default floor 8); Episode 4: Test Map (area 0x2E, default floor 10)

Floor numbers are script slots. Resolve the quest map designation to an area before checking compatibility. Custom client patches may change constructor availability; this table describes the stored reference, not a live client test.

## Parameters and source notes

```text
Rappy. Params:
param1 = initial location (zero or negative = ground, positive = sky; ignored if wave_number is > 0 in which
case it's always sky)
param6 = rare flag (on v1-v3, rappy is rare if param6 != 0; on v4, rappy is rare if (param6 & 1) != 0)
param7 = TODO
Exactly which rappy is constructed depends on param6 (or the random
rare check) and the current season event:
Ep1/Ep2 non-rare = Rag Rappy
Ep4 non-rare = Sand Rappy (Crater or Desert variation)
Ep1 rare = Al Rappy
Ep2 rare, Christmas = Saint Rappy
Ep2 rare, Easter = Egg Rappy
Ep2 rare, Halloween = Hallo Rappy
Ep2 rare, any other season event (or none) = Love Rappy
Ep4 rare = Del Rappy (Crater or Desert variation)

```

## Observed quest placements

5909 records, including language duplicates. These are observations, not spawn permissions.

[All observed positions, angles, parameters and handler candidates](../observations/0041.csv)

| Quest | Floor | Room / wave | Handler candidate |
|---|---:|---|---|
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 2 / 3 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 2 / 3 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 2 / 3 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 2 / 3 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 13 / 1 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 13 / 1 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 13 / 1 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 13 / 1 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 13 / 1 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 13 / 1 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 13 / 1 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 13 / 1 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 13 / 1 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 13 / 2 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 13 / 2 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 13 / 2 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 13 / 2 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 13 / 2 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 13 / 2 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 15 / 5 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 15 / 6 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 12 / 9 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 12 / 9 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 12 / 9 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 12 / 9 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 12 / 9 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 12 / 9 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 12 / 13 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 12 / 14 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 12 / 14 | — |
