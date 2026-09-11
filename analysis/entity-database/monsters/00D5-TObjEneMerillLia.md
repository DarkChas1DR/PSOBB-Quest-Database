# Merillias

DAT ID **0x00D5 / 213**, constructor **TObjEneMerillLia**.

[Definition source](../../quest-knowledge/reference/server-source/Map.cc#L2990) · [Database index](../monsters.md)

## Source-documented areas

Episode 2: Central Control Area (area 0x17, default floor 5); Episode 2: Jungle Area North (area 0x18, default floor 6); Episode 2: Jungle Area East (area 0x19, default floor 7); Episode 2: Mountain Area (area 0x1A, default floor 8); Episode 2: Seaside Area (area 0x1B, default floor 9); Episode 2: Seaside Area (night) (area 0x22, default floor 16)

Floor numbers are script slots. Resolve the quest map designation to an area before checking compatibility. Custom client patches may change constructor availability; this table describes the stored reference, not a live client test.

## Parameters and source notes

```text
Merillia / Meriltas. Params:
param1 = chance to run away after being hit (value used is param1 - 0.2, clamped below to 0)
param3 = chance to do poison attack after being hit (value used is param3 - 0.2, clamped below to 0)
param4 = distance to run away (value used is param4 + 300)
param5 = wakeup radius delta (value used is param5 + 100, clamped below to 15; enemy will wake up when any
player is nearby)
param6 = type (0 = Merillia, 1 = Meriltas)

```

## Observed quest placements

5267 records, including language duplicates. These are observations, not spawn permissions.

[All observed positions, angles, parameters and handler candidates](../observations/00D5.csv)

| Quest | Floor | Room / wave | Handler candidate |
|---|---:|---|---|
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 3 / 5 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 3 / 5 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 3 / 5 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 3 / 6 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 3 / 6 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 3 / 6 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 3 / 2 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 3 / 2 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 4 / 4 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 4 / 4 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 4 / 4 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 4 / 1 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 4 / 1 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 4 / 2 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 4 / 2 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 7 / 1 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 7 / 1 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 7 / 1 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 11 / 1 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 11 / 1 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 11 / 2 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 11 / 2 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 15 / 1 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 15 / 1 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 15 / 2 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 15 / 2 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 15 / 3 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 15 / 3 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 15 / 3 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 2 | 3 / 3 | — |
