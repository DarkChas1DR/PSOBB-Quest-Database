# delbiter

DAT ID **0x00DC / 220**, constructor **TObjEneDellBiter**.

[Definition source](../../quest-knowledge/reference/server-source/Map.cc#L3054) · [Database index](../monsters.md)

## Source-documented areas

Episode 2: Seabed Upper Levels (area 0x1C, default floor 10); Episode 2: Seabed Lower Levels (area 0x1D, default floor 11); Episode 2: Control Tower (area 0x23, default floor 17)

Floor numbers are script slots. Resolve the quest map designation to an area before checking compatibility. Custom client patches may change constructor availability; this table describes the stored reference, not a live client test.

## Parameters and source notes

```text
Delbiter. Params:
param1 = chance to howl (value is param1 + 0.3)
param2 = chance to cause confusion via howl (value is param2 + 0.3)
param3 = maximum distance at which howl can cause confusion (value is param3 + 30, clamped below to 10)
param4 = chance to fire laser (value is param4 + 0.3)
param5 = chance to charge (value is param5 + 0.05)
param6 = type (0 = stand, 1 = run)

```

## Observed quest placements

1064 records, including language duplicates. These are observations, not spawn permissions.

[All observed positions, angles, parameters and handler candidates](../observations/00DC.csv)

| Quest | Floor | Room / wave | Handler candidate |
|---|---:|---|---|
| [challenge-ep2/d88204-bb-e](../../server-catalogue/challenge-ep2/d88204-bb-e/README.md) | 1 | 80 / 1 | — |
| [challenge-ep2/d88204-bb-e](../../server-catalogue/challenge-ep2/d88204-bb-e/README.md) | 2 | 213 / 1 | — |
| [challenge-ep2/d88204-bb-e](../../server-catalogue/challenge-ep2/d88204-bb-e/README.md) | 3 | 80 / 1 | — |
| [challenge-ep2/d88204-bb-e](../../server-catalogue/challenge-ep2/d88204-bb-e/README.md) | 4 | 81 / 1 | — |
| [challenge-ep2/d88204-bb-e](../../server-catalogue/challenge-ep2/d88204-bb-e/README.md) | 5 | 70 / 1 | — |
| [challenge-ep2/d88204-bb-e](../../server-catalogue/challenge-ep2/d88204-bb-e/README.md) | 6 | 30 / 2 | — |
| [challenge-ep2/d88204-bb-e](../../server-catalogue/challenge-ep2/d88204-bb-e/README.md) | 6 | 30 / 1 | — |
| [challenge-ep2/d88204-bb-e](../../server-catalogue/challenge-ep2/d88204-bb-e/README.md) | 6 | 70 / 3 | — |
| [challenge-ep2/d88204-bb-e](../../server-catalogue/challenge-ep2/d88204-bb-e/README.md) | 6 | 80 / 1 | — |
| [challenge-ep2/d88204-bb-e](../../server-catalogue/challenge-ep2/d88204-bb-e/README.md) | 6 | 81 / 1 | — |
| [challenge-ep2/d88204-bb-e](../../server-catalogue/challenge-ep2/d88204-bb-e/README.md) | 6 | 81 / 1 | — |
| [challenge-ep2/d88204-bb-j](../../server-catalogue/challenge-ep2/d88204-bb-j/README.md) | 1 | 80 / 1 | — |
| [challenge-ep2/d88204-bb-j](../../server-catalogue/challenge-ep2/d88204-bb-j/README.md) | 2 | 213 / 1 | — |
| [challenge-ep2/d88204-bb-j](../../server-catalogue/challenge-ep2/d88204-bb-j/README.md) | 3 | 80 / 1 | — |
| [challenge-ep2/d88204-bb-j](../../server-catalogue/challenge-ep2/d88204-bb-j/README.md) | 4 | 81 / 1 | — |
| [challenge-ep2/d88204-bb-j](../../server-catalogue/challenge-ep2/d88204-bb-j/README.md) | 5 | 70 / 1 | — |
| [challenge-ep2/d88204-bb-j](../../server-catalogue/challenge-ep2/d88204-bb-j/README.md) | 6 | 30 / 2 | — |
| [challenge-ep2/d88204-bb-j](../../server-catalogue/challenge-ep2/d88204-bb-j/README.md) | 6 | 30 / 1 | — |
| [challenge-ep2/d88204-bb-j](../../server-catalogue/challenge-ep2/d88204-bb-j/README.md) | 6 | 70 / 3 | — |
| [challenge-ep2/d88204-bb-j](../../server-catalogue/challenge-ep2/d88204-bb-j/README.md) | 6 | 80 / 1 | — |
| [challenge-ep2/d88204-bb-j](../../server-catalogue/challenge-ep2/d88204-bb-j/README.md) | 6 | 81 / 1 | — |
| [challenge-ep2/d88204-bb-j](../../server-catalogue/challenge-ep2/d88204-bb-j/README.md) | 6 | 81 / 1 | — |
| [challenge-ep2/d88205-bb-e](../../server-catalogue/challenge-ep2/d88205-bb-e/README.md) | 1 | 30 / 1 | — |
| [challenge-ep2/d88205-bb-e](../../server-catalogue/challenge-ep2/d88205-bb-e/README.md) | 2 | 2 / 3 | — |
| [challenge-ep2/d88205-bb-e](../../server-catalogue/challenge-ep2/d88205-bb-e/README.md) | 2 | 3 / 1 | — |
| [challenge-ep2/d88205-bb-e](../../server-catalogue/challenge-ep2/d88205-bb-e/README.md) | 2 | 3 / 1 | — |
| [challenge-ep2/d88205-bb-j](../../server-catalogue/challenge-ep2/d88205-bb-j/README.md) | 1 | 30 / 1 | — |
| [challenge-ep2/d88205-bb-j](../../server-catalogue/challenge-ep2/d88205-bb-j/README.md) | 2 | 2 / 3 | — |
| [challenge-ep2/d88205-bb-j](../../server-catalogue/challenge-ep2/d88205-bb-j/README.md) | 2 | 3 / 1 | — |
| [challenge-ep2/d88205-bb-j](../../server-catalogue/challenge-ep2/d88205-bb-j/README.md) | 2 | 3 / 1 | — |
