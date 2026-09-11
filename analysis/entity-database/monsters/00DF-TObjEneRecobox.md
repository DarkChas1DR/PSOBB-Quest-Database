# Reconbox

DAT ID **0x00DF / 223**, constructor **TObjEneRecobox**.

[Definition source](../../quest-knowledge/reference/server-source/Map.cc#L3081) · [Database index](../monsters.md)

## Source-documented areas

Episode 2: Seabed Upper Levels (area 0x1C, default floor 10); Episode 2: Seabed Lower Levels (area 0x1D, default floor 11); Episode 2: Seaside Area (night) (area 0x22, default floor 16); Episode 2: Control Tower (area 0x23, default floor 17)

Floor numbers are script slots. Resolve the quest map designation to an area before checking compatibility. Custom client patches may change constructor availability; this table describes the stored reference, not a live client test.

## Parameters and source notes

```text
Recobox. Params:
param1 = Recon floating height (value used for each Recon is 45 + rand(-2, 2) + param1)
param2 = Recon target radius (distance from target; value used for each Recon is 50 + rand(-5, 5) + param2;
param2 is clamped below to -30)
param4 = maximum number of concurrently-active Recons (clamped to [0, min(6, num_children - 1)])
param6 = type:
zero or negative = floor (Recons exit upward)
1 = ceiling (Recons exit downward)
2 or greater = wall (Recons exit horizontally)
Note: The debug strings in TObjEneRecobox_v6A seem to imply that the total Recon count in the box is (param7 +
1); however, this is not true. The total Recon count in the box is actually (num_children - 1).

```

## Observed quest placements

3227 records, including language duplicates. These are observations, not spawn permissions.

[All observed positions, angles, parameters and handler candidates](../observations/00DF.csv)

| Quest | Floor | Room / wave | Handler candidate |
|---|---:|---|---|
| [challenge-ep2/d88204-bb-e](../../server-catalogue/challenge-ep2/d88204-bb-e/README.md) | 1 | 20 / 2 | — |
| [challenge-ep2/d88204-bb-e](../../server-catalogue/challenge-ep2/d88204-bb-e/README.md) | 1 | 20 / 2 | — |
| [challenge-ep2/d88204-bb-e](../../server-catalogue/challenge-ep2/d88204-bb-e/README.md) | 1 | 20 / 2 | — |
| [challenge-ep2/d88204-bb-e](../../server-catalogue/challenge-ep2/d88204-bb-e/README.md) | 1 | 30 / 1 | — |
| [challenge-ep2/d88204-bb-e](../../server-catalogue/challenge-ep2/d88204-bb-e/README.md) | 1 | 30 / 1 | — |
| [challenge-ep2/d88204-bb-e](../../server-catalogue/challenge-ep2/d88204-bb-e/README.md) | 1 | 30 / 1 | — |
| [challenge-ep2/d88204-bb-e](../../server-catalogue/challenge-ep2/d88204-bb-e/README.md) | 1 | 30 / 1 | — |
| [challenge-ep2/d88204-bb-e](../../server-catalogue/challenge-ep2/d88204-bb-e/README.md) | 1 | 30 / 1 | — |
| [challenge-ep2/d88204-bb-e](../../server-catalogue/challenge-ep2/d88204-bb-e/README.md) | 1 | 30 / 1 | — |
| [challenge-ep2/d88204-bb-e](../../server-catalogue/challenge-ep2/d88204-bb-e/README.md) | 1 | 40 / 2 | — |
| [challenge-ep2/d88204-bb-e](../../server-catalogue/challenge-ep2/d88204-bb-e/README.md) | 1 | 40 / 2 | — |
| [challenge-ep2/d88204-bb-e](../../server-catalogue/challenge-ep2/d88204-bb-e/README.md) | 1 | 40 / 1 | — |
| [challenge-ep2/d88204-bb-e](../../server-catalogue/challenge-ep2/d88204-bb-e/README.md) | 1 | 40 / 1 | — |
| [challenge-ep2/d88204-bb-e](../../server-catalogue/challenge-ep2/d88204-bb-e/README.md) | 1 | 40 / 1 | — |
| [challenge-ep2/d88204-bb-e](../../server-catalogue/challenge-ep2/d88204-bb-e/README.md) | 1 | 64 / 2 | — |
| [challenge-ep2/d88204-bb-e](../../server-catalogue/challenge-ep2/d88204-bb-e/README.md) | 1 | 64 / 2 | — |
| [challenge-ep2/d88204-bb-e](../../server-catalogue/challenge-ep2/d88204-bb-e/README.md) | 1 | 64 / 2 | — |
| [challenge-ep2/d88204-bb-e](../../server-catalogue/challenge-ep2/d88204-bb-e/README.md) | 1 | 81 / 2 | — |
| [challenge-ep2/d88204-bb-e](../../server-catalogue/challenge-ep2/d88204-bb-e/README.md) | 1 | 81 / 2 | — |
| [challenge-ep2/d88204-bb-e](../../server-catalogue/challenge-ep2/d88204-bb-e/README.md) | 1 | 81 / 1 | — |
| [challenge-ep2/d88204-bb-e](../../server-catalogue/challenge-ep2/d88204-bb-e/README.md) | 1 | 81 / 1 | — |
| [challenge-ep2/d88204-bb-e](../../server-catalogue/challenge-ep2/d88204-bb-e/README.md) | 1 | 213 / 1 | — |
| [challenge-ep2/d88204-bb-e](../../server-catalogue/challenge-ep2/d88204-bb-e/README.md) | 1 | 213 / 1 | — |
| [challenge-ep2/d88204-bb-e](../../server-catalogue/challenge-ep2/d88204-bb-e/README.md) | 1 | 213 / 1 | — |
| [challenge-ep2/d88204-bb-e](../../server-catalogue/challenge-ep2/d88204-bb-e/README.md) | 1 | 213 / 1 | — |
| [challenge-ep2/d88204-bb-e](../../server-catalogue/challenge-ep2/d88204-bb-e/README.md) | 2 | 20 / 2 | — |
| [challenge-ep2/d88204-bb-e](../../server-catalogue/challenge-ep2/d88204-bb-e/README.md) | 2 | 20 / 2 | — |
| [challenge-ep2/d88204-bb-e](../../server-catalogue/challenge-ep2/d88204-bb-e/README.md) | 2 | 20 / 2 | — |
| [challenge-ep2/d88204-bb-e](../../server-catalogue/challenge-ep2/d88204-bb-e/README.md) | 2 | 20 / 2 | — |
| [challenge-ep2/d88204-bb-e](../../server-catalogue/challenge-ep2/d88204-bb-e/README.md) | 2 | 21 / 3 | — |
