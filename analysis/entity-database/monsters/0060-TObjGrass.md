# Grass Asassin

DAT ID **0x0060 / 96**, constructor **TObjGrass**.

[Definition source](../../quest-knowledge/reference/server-source/Map.cc#L2841) · [Database index](../monsters.md)

## Source-documented areas

Episode 1: Cave 1 (area 0x03, default floor 3); Episode 1: Cave 2 (area 0x04, default floor 4); Episode 1: Spaceship (area 0x10, default floor 16); Episode 1: Palace (area 0x11, default floor 17); Episode 2: VR Temple Alpha (area 0x13, default floor 1); Episode 2: VR Temple Beta (area 0x14, default floor 2)

Floor numbers are script slots. Resolve the quest map designation to an area before checking compatibility. Custom client patches may change constructor availability; this table describes the stored reference, not a live client test.

## Parameters and source notes

```text
Grass Assassin. Params:
param1 = TODO
param2 = TODO (some state is set based on whether this is <= 0 or not, but the value is also used directly in
some places)
param3 = TODO (see TObjGrass_update_case8)
param4 = TODO (see TObjGrass_update_case8)

```

## Observed quest placements

1769 records, including language duplicates. These are observations, not spawn permissions.

[All observed positions, angles, parameters and handler candidates](../observations/0060.csv)

| Quest | Floor | Room / wave | Handler candidate |
|---|---:|---|---|
| [battle/b88003-bb-e](../../server-catalogue/battle/b88003-bb-e/README.md) | 16 | 30 / 1 | — |
| [battle/b88003-bb-j](../../server-catalogue/battle/b88003-bb-j/README.md) | 16 | 30 / 1 | — |
| [challenge-ep2/d88201-bb-e](../../server-catalogue/challenge-ep2/d88201-bb-e/README.md) | 1 | 61 / 1 | — |
| [challenge-ep2/d88201-bb-e](../../server-catalogue/challenge-ep2/d88201-bb-e/README.md) | 1 | 61 / 1 | — |
| [challenge-ep2/d88201-bb-e](../../server-catalogue/challenge-ep2/d88201-bb-e/README.md) | 1 | 70 / 3 | — |
| [challenge-ep2/d88201-bb-e](../../server-catalogue/challenge-ep2/d88201-bb-e/README.md) | 1 | 70 / 4 | — |
| [challenge-ep2/d88201-bb-e](../../server-catalogue/challenge-ep2/d88201-bb-e/README.md) | 1 | 70 / 4 | — |
| [challenge-ep2/d88201-bb-e](../../server-catalogue/challenge-ep2/d88201-bb-e/README.md) | 2 | 40 / 3 | — |
| [challenge-ep2/d88201-bb-e](../../server-catalogue/challenge-ep2/d88201-bb-e/README.md) | 2 | 41 / 4 | — |
| [challenge-ep2/d88201-bb-e](../../server-catalogue/challenge-ep2/d88201-bb-e/README.md) | 2 | 41 / 4 | — |
| [challenge-ep2/d88201-bb-e](../../server-catalogue/challenge-ep2/d88201-bb-e/README.md) | 3 | 61 / 2 | — |
| [challenge-ep2/d88201-bb-e](../../server-catalogue/challenge-ep2/d88201-bb-e/README.md) | 4 | 50 / 1 | — |
| [challenge-ep2/d88201-bb-e](../../server-catalogue/challenge-ep2/d88201-bb-e/README.md) | 4 | 60 / 2 | — |
| [challenge-ep2/d88201-bb-e](../../server-catalogue/challenge-ep2/d88201-bb-e/README.md) | 4 | 70 / 1 | — |
| [challenge-ep2/d88201-bb-e](../../server-catalogue/challenge-ep2/d88201-bb-e/README.md) | 4 | 70 / 1 | — |
| [challenge-ep2/d88201-bb-e](../../server-catalogue/challenge-ep2/d88201-bb-e/README.md) | 5 | 70 / 2 | — |
| [challenge-ep2/d88201-bb-e](../../server-catalogue/challenge-ep2/d88201-bb-e/README.md) | 5 | 101 / 1 | — |
| [challenge-ep2/d88201-bb-e](../../server-catalogue/challenge-ep2/d88201-bb-e/README.md) | 6 | 41 / 3 | — |
| [challenge-ep2/d88201-bb-e](../../server-catalogue/challenge-ep2/d88201-bb-e/README.md) | 6 | 41 / 3 | — |
| [challenge-ep2/d88201-bb-e](../../server-catalogue/challenge-ep2/d88201-bb-e/README.md) | 6 | 50 / 2 | — |
| [challenge-ep2/d88201-bb-e](../../server-catalogue/challenge-ep2/d88201-bb-e/README.md) | 6 | 50 / 2 | — |
| [challenge-ep2/d88201-bb-e](../../server-catalogue/challenge-ep2/d88201-bb-e/README.md) | 6 | 70 / 2 | — |
| [challenge-ep2/d88201-bb-e](../../server-catalogue/challenge-ep2/d88201-bb-e/README.md) | 6 | 70 / 2 | — |
| [challenge-ep2/d88201-bb-j](../../server-catalogue/challenge-ep2/d88201-bb-j/README.md) | 1 | 61 / 1 | — |
| [challenge-ep2/d88201-bb-j](../../server-catalogue/challenge-ep2/d88201-bb-j/README.md) | 1 | 61 / 1 | — |
| [challenge-ep2/d88201-bb-j](../../server-catalogue/challenge-ep2/d88201-bb-j/README.md) | 1 | 70 / 3 | — |
| [challenge-ep2/d88201-bb-j](../../server-catalogue/challenge-ep2/d88201-bb-j/README.md) | 1 | 70 / 4 | — |
| [challenge-ep2/d88201-bb-j](../../server-catalogue/challenge-ep2/d88201-bb-j/README.md) | 1 | 70 / 4 | — |
| [challenge-ep2/d88201-bb-j](../../server-catalogue/challenge-ep2/d88201-bb-j/README.md) | 2 | 40 / 3 | — |
| [challenge-ep2/d88201-bb-j](../../server-catalogue/challenge-ep2/d88201-bb-j/README.md) | 2 | 41 / 4 | — |
