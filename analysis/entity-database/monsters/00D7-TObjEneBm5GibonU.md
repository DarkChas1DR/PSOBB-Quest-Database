# Ul Gibbon

DAT ID **0x00D7 / 215**, constructor **TObjEneBm5GibonU**.

[Definition source](../../quest-knowledge/reference/server-source/Map.cc#L3016) · [Database index](../monsters.md)

## Source-documented areas

Episode 2: Central Control Area (area 0x17, default floor 5); Episode 2: Jungle Area North (area 0x18, default floor 6); Episode 2: Jungle Area East (area 0x19, default floor 7); Episode 2: Mountain Area (area 0x1A, default floor 8); Episode 2: Seaside Area (area 0x1B, default floor 9); Episode 2: Seaside Area (night) (area 0x22, default floor 16)

Floor numbers are script slots. Resolve the quest map designation to an area before checking compatibility. Custom client patches may change constructor availability; this table describes the stored reference, not a live client test.

## Parameters and source notes

```text
Ul Gibbon / Zol Gibbon. Params:
param1 = group number
param2 = appear type (<1 = spot appear; >=1 = jump appear)
param3 = chance of jumping forward or back at each decision point (value used is param3 + 0.4)
param4 = chance of casting a tech when not near any player (value used is param4 + 0.3)
param5 = chance of casting a tech immediately after jumping forward or back (value used is param5 + 0.3; does
not apply after jumps that are attacks)
param6 = type (zero or negative = Ul Gibbon, positive = Zol Gibbon)

```

## Observed quest placements

4783 records, including language duplicates. These are observations, not spawn permissions.

[All observed positions, angles, parameters and handler candidates](../observations/00D7.csv)

| Quest | Floor | Room / wave | Handler candidate |
|---|---:|---|---|
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 1 / 1 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 1 / 1 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 3 / 4 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 3 / 4 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 3 / 1 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 3 / 1 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 3 / 2 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 3 / 3 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 4 / 3 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 4 / 3 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 4 / 2 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 11 / 6 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 12 / 1 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 12 / 1 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 15 / 4 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 15 / 4 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 15 / 5 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 15 / 5 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 15 / 2 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 2 | 3 / 4 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 2 | 3 / 4 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 2 | 4 / 1 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 2 | 4 / 1 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 2 | 4 / 1 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 2 | 6 / 4 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 2 | 6 / 4 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 2 | 6 / 5 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 2 | 6 / 5 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 2 | 6 / 5 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 2 | 7 / 4 | — |
