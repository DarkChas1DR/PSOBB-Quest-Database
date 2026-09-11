# Booma

DAT ID **0x0044 / 68**, constructor **TObjEneBeast**.

[Definition source](../../quest-knowledge/reference/server-source/Map.cc#L2833) · [Database index](../monsters.md)

## Source-documented areas

Episode 1: Forest 1 (area 0x01, default floor 1); Episode 1: Forest 2 (area 0x02, default floor 2)

Floor numbers are script slots. Resolve the quest map designation to an area before checking compatibility. Custom client patches may change constructor availability; this table describes the stored reference, not a live client test.

## Parameters and source notes

```text
Booma, Gobooma, or Gigobooma. The activation radius is fixed and cannot be changed: 50 for Hunters, 100 for
Rangers and Forces; the deactivation radius is 100 for Hunters and 150 for Rangers and Forces. Params:
param1 = TODO (fraction of max HP; see TObjEnemyV8048ee80_v5A)
param2 = idle walk radius (when there's no target, it will walk around its spawn location within this radius;
if this is zero, it stands still instead)
param6 = type (0 = Booma, 1 = Gobooma, 2 = Gigobooma)
param7 = group ID (if nonzero, it looks like this is used to cause groups of enemies in the same room to band
together and all attack the same player, chosen by the highest-ranking enemy (by param6) in the group; TODO:
this explanation is unverified and param7 was never used by Sega; see client code at 3OE1:800F6F3C)

```

## Observed quest placements

7161 records, including language duplicates. These are observations, not spawn permissions.

[All observed positions, angles, parameters and handler candidates](../observations/0044.csv)

| Quest | Floor | Room / wave | Handler candidate |
|---|---:|---|---|
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 1 | 4 / 1 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 1 | 4 / 1 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 1 | 4 / 1 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 1 | 4 / 1 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 1 | 2 / 1 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 1 | 2 / 2 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 1 | 2 / 3 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 1 | 2 / 4 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 1 | 2 / 5 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 1 | 2 / 6 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 1 | 2 / 7 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 1 | 2 / 8 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 1 | 2 / 16 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 1 | 2 / 15 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 1 | 2 / 31 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 1 | 2 / 9 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 1 | 2 / 10 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 1 | 2 / 11 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 1 | 2 / 12 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 1 | 2 / 13 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 1 | 2 / 14 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 1 | 2 / 17 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 1 | 2 / 18 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 1 | 2 / 19 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 1 | 2 / 20 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 1 | 2 / 21 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 1 | 2 / 22 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 1 | 2 / 23 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 1 | 2 / 24 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 1 | 2 / 25 | — |
