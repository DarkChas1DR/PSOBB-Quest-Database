# Delsaber

DAT ID **0x00A0 / 160**, constructor **TObjEneSaver**.

[Definition source](../../quest-knowledge/reference/server-source/Map.cc#L2906) · [Database index](../monsters.md)

## Source-documented areas

Episode 1: Ruins 1 (area 0x08, default floor 8); Episode 1: Ruins 2 (area 0x09, default floor 9); Episode 1: Spaceship (area 0x10, default floor 16); Episode 1: Palace (area 0x11, default floor 17); Episode 2: VR Spaceship Alpha (area 0x15, default floor 3); Episode 2: VR Spaceship Beta (area 0x16, default floor 4)

Floor numbers are script slots. Resolve the quest map designation to an area before checking compatibility. Custom client patches may change constructor availability; this table describes the stored reference, not a live client test.

## Parameters and source notes

```text
Delsaber. Params:
param1 = jump distance delta (value used is param1 + 100)
param2 = prejudice flag (these correspond to the bits in PlayerVisualConfigV123T::class_flags):
0 = males
1 = females
2 = humans
3 = newmans
4 = androids
5 = hunters
6 = rangers
7 = forces
8 = no prejudice
By default, the Delsaber will target the nearest player that matches its prejudice flag. If no players match the
flag or there is any player less than 30 units away from the Delsaber, then the Delsaber will target the nearest
player overall and ignore its prejudice flag.

```

## Observed quest placements

2314 records, including language duplicates. These are observations, not spawn permissions.

[All observed positions, angles, parameters and handler candidates](../observations/00A0.csv)

| Quest | Floor | Room / wave | Handler candidate |
|---|---:|---|---|
| [battle/b88001-bb-e](../../server-catalogue/battle/b88001-bb-e/README.md) | 16 | 30 / 1 | — |
| [battle/b88001-bb-e](../../server-catalogue/battle/b88001-bb-e/README.md) | 16 | 32 / 0 | — |
| [battle/b88001-bb-j](../../server-catalogue/battle/b88001-bb-j/README.md) | 16 | 30 / 1 | — |
| [battle/b88001-bb-j](../../server-catalogue/battle/b88001-bb-j/README.md) | 16 | 32 / 0 | — |
| [battle/b88003-bb-e](../../server-catalogue/battle/b88003-bb-e/README.md) | 16 | 11 / 1 | — |
| [battle/b88003-bb-e](../../server-catalogue/battle/b88003-bb-e/README.md) | 16 | 40 / 0 | — |
| [battle/b88003-bb-j](../../server-catalogue/battle/b88003-bb-j/README.md) | 16 | 11 / 1 | — |
| [battle/b88003-bb-j](../../server-catalogue/battle/b88003-bb-j/README.md) | 16 | 40 / 0 | — |
| [challenge-ep2/d88202-bb-e](../../server-catalogue/challenge-ep2/d88202-bb-e/README.md) | 1 | 32 / 1 | — |
| [challenge-ep2/d88202-bb-e](../../server-catalogue/challenge-ep2/d88202-bb-e/README.md) | 1 | 32 / 1 | — |
| [challenge-ep2/d88202-bb-e](../../server-catalogue/challenge-ep2/d88202-bb-e/README.md) | 1 | 40 / 3 | — |
| [challenge-ep2/d88202-bb-e](../../server-catalogue/challenge-ep2/d88202-bb-e/README.md) | 1 | 52 / 2 | — |
| [challenge-ep2/d88202-bb-e](../../server-catalogue/challenge-ep2/d88202-bb-e/README.md) | 1 | 52 / 2 | — |
| [challenge-ep2/d88202-bb-e](../../server-catalogue/challenge-ep2/d88202-bb-e/README.md) | 1 | 140 / 1 | — |
| [challenge-ep2/d88202-bb-e](../../server-catalogue/challenge-ep2/d88202-bb-e/README.md) | 2 | 41 / 1 | — |
| [challenge-ep2/d88202-bb-e](../../server-catalogue/challenge-ep2/d88202-bb-e/README.md) | 3 | 21 / 1 | — |
| [challenge-ep2/d88202-bb-e](../../server-catalogue/challenge-ep2/d88202-bb-e/README.md) | 3 | 32 / 1 | — |
| [challenge-ep2/d88202-bb-e](../../server-catalogue/challenge-ep2/d88202-bb-e/README.md) | 3 | 51 / 2 | — |
| [challenge-ep2/d88202-bb-e](../../server-catalogue/challenge-ep2/d88202-bb-e/README.md) | 3 | 51 / 2 | — |
| [challenge-ep2/d88202-bb-e](../../server-catalogue/challenge-ep2/d88202-bb-e/README.md) | 3 | 51 / 1 | — |
| [challenge-ep2/d88202-bb-e](../../server-catalogue/challenge-ep2/d88202-bb-e/README.md) | 4 | 21 / 1 | — |
| [challenge-ep2/d88202-bb-e](../../server-catalogue/challenge-ep2/d88202-bb-e/README.md) | 4 | 30 / 1 | — |
| [challenge-ep2/d88202-bb-e](../../server-catalogue/challenge-ep2/d88202-bb-e/README.md) | 4 | 30 / 1 | — |
| [challenge-ep2/d88202-bb-e](../../server-catalogue/challenge-ep2/d88202-bb-e/README.md) | 4 | 41 / 3 | — |
| [challenge-ep2/d88202-bb-e](../../server-catalogue/challenge-ep2/d88202-bb-e/README.md) | 4 | 41 / 3 | — |
| [challenge-ep2/d88202-bb-e](../../server-catalogue/challenge-ep2/d88202-bb-e/README.md) | 4 | 42 / 2 | — |
| [challenge-ep2/d88202-bb-e](../../server-catalogue/challenge-ep2/d88202-bb-e/README.md) | 4 | 42 / 2 | — |
| [challenge-ep2/d88202-bb-e](../../server-catalogue/challenge-ep2/d88202-bb-e/README.md) | 4 | 42 / 2 | — |
| [challenge-ep2/d88202-bb-e](../../server-catalogue/challenge-ep2/d88202-bb-e/README.md) | 4 | 50 / 4 | — |
| [challenge-ep2/d88202-bb-e](../../server-catalogue/challenge-ep2/d88202-bb-e/README.md) | 4 | 50 / 4 | — |
