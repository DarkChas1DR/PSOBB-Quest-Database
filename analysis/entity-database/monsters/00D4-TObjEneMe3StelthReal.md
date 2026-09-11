# Sinow Berill

DAT ID **0x00D4 / 212**, constructor **TObjEneMe3StelthReal**.

[Definition source](../../quest-knowledge/reference/server-source/Map.cc#L2981) · [Database index](../monsters.md)

## Source-documented areas

Episode 2: Central Control Area (area 0x17, default floor 5); Episode 2: Jungle Area North (area 0x18, default floor 6); Episode 2: Jungle Area East (area 0x19, default floor 7); Episode 2: Mountain Area (area 0x1A, default floor 8); Episode 2: Seaside Area (area 0x1B, default floor 9)

Floor numbers are script slots. Resolve the quest map designation to an area before checking compatibility. Custom client patches may change constructor availability; this table describes the stored reference, not a live client test.

## Parameters and source notes

```text
Sinow Berill or Sinow Spigell. Params:
param1 = spawn type:
0 = invisible + ground
1 = invisible + ceiling
2 = visible + ground
3 = visible + ceiling
param2 = chance to enable stealth (value used is param2 + 0.3)
param3 = chance to cast technique (value used is param3 + 0.4)
param4 = chance to teleport (value used is param4 + 0.5)
param5 = chance to disable stealth (value used is param5 + 0.1; applies when hit, but (TODO) also some other
events)
param6 = type:
zero or negative = Sinow Berill
positive = Sinow Spigell
param2, param3, and param4 are evaluated in that order after the Sinow jumps back. That is, the game first
generates a random float between 0 and 1, and compares it to param2 to decide whether to enable stealth. If it
does, the other params are ignored. If it doesn't, the game then checks param3 in the same manner to determine
whether to cast a tech; if that doesn't happen either, the game checks param4 to determine whether to teleport.
If none of those happen, the Sinow just walks forward again and attacks.

```

## Observed quest placements

1951 records, including language duplicates. These are observations, not spawn permissions.

[All observed positions, angles, parameters and handler candidates](../observations/00D4.csv)

| Quest | Floor | Room / wave | Handler candidate |
|---|---:|---|---|
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 1 | 15 / 6 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 3 | 10 / 1 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 4 | 7 / 6 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 5 | 2 / 4 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 5 | 2 / 5 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 5 | 2 / 5 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 5 | 2 / 3 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 5 | 2 / 1 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 5 | 2 / 1 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 5 | 2 / 2 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 5 | 2 / 2 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 5 | 3 / 1 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 5 | 4 / 1 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 5 | 5 / 1 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 5 | 6 / 1 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 5 | 6 / 1 | — |
| [challenge-ep2/d88203-bb-j](../../server-catalogue/challenge-ep2/d88203-bb-j/README.md) | 1 | 15 / 6 | — |
| [challenge-ep2/d88203-bb-j](../../server-catalogue/challenge-ep2/d88203-bb-j/README.md) | 3 | 10 / 1 | — |
| [challenge-ep2/d88203-bb-j](../../server-catalogue/challenge-ep2/d88203-bb-j/README.md) | 4 | 7 / 6 | — |
| [challenge-ep2/d88203-bb-j](../../server-catalogue/challenge-ep2/d88203-bb-j/README.md) | 5 | 2 / 4 | — |
| [challenge-ep2/d88203-bb-j](../../server-catalogue/challenge-ep2/d88203-bb-j/README.md) | 5 | 2 / 5 | — |
| [challenge-ep2/d88203-bb-j](../../server-catalogue/challenge-ep2/d88203-bb-j/README.md) | 5 | 2 / 5 | — |
| [challenge-ep2/d88203-bb-j](../../server-catalogue/challenge-ep2/d88203-bb-j/README.md) | 5 | 2 / 3 | — |
| [challenge-ep2/d88203-bb-j](../../server-catalogue/challenge-ep2/d88203-bb-j/README.md) | 5 | 2 / 1 | — |
| [challenge-ep2/d88203-bb-j](../../server-catalogue/challenge-ep2/d88203-bb-j/README.md) | 5 | 2 / 1 | — |
| [challenge-ep2/d88203-bb-j](../../server-catalogue/challenge-ep2/d88203-bb-j/README.md) | 5 | 2 / 2 | — |
| [challenge-ep2/d88203-bb-j](../../server-catalogue/challenge-ep2/d88203-bb-j/README.md) | 5 | 2 / 2 | — |
| [challenge-ep2/d88203-bb-j](../../server-catalogue/challenge-ep2/d88203-bb-j/README.md) | 5 | 3 / 1 | — |
| [challenge-ep2/d88203-bb-j](../../server-catalogue/challenge-ep2/d88203-bb-j/README.md) | 5 | 4 / 1 | — |
| [challenge-ep2/d88203-bb-j](../../server-catalogue/challenge-ep2/d88203-bb-j/README.md) | 5 | 5 / 1 | — |
