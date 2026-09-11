# Gibbles

DAT ID **0x00D8 / 216**, constructor **TObjEneGibbles**.

[Definition source](../../quest-knowledge/reference/server-source/Map.cc#L3023) · [Database index](../monsters.md)

## Source-documented areas

Episode 2: Central Control Area (area 0x17, default floor 5); Episode 2: Jungle Area North (area 0x18, default floor 6); Episode 2: Jungle Area East (area 0x19, default floor 7); Episode 2: Mountain Area (area 0x1A, default floor 8); Episode 2: Seaside Area (area 0x1B, default floor 9); Episode 2: Control Tower (area 0x23, default floor 17)

Floor numbers are script slots. Resolve the quest map designation to an area before checking compatibility. Custom client patches may change constructor availability; this table describes the stored reference, not a live client test.

## Parameters and source notes

```text
Gibbles. Params:
param1 = jump distance delta (value used is param1 + 100)
param2 = prejudice flag (see 0x00A0 (TObjEneSaver); the behavior here is exactly the same)
param3 = chance to jump at each decision point (0-1)
param4 = chance to jump after being hit (0-1)

```

## Observed quest placements

919 records, including language duplicates. These are observations, not spawn permissions.

[All observed positions, angles, parameters and handler candidates](../observations/00D8.csv)

| Quest | Floor | Room / wave | Handler candidate |
|---|---:|---|---|
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 4 | 11 / 1 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 5 | 9 / 1 | — |
| [challenge-ep2/d88203-bb-j](../../server-catalogue/challenge-ep2/d88203-bb-j/README.md) | 4 | 11 / 1 | — |
| [challenge-ep2/d88203-bb-j](../../server-catalogue/challenge-ep2/d88203-bb-j/README.md) | 5 | 9 / 1 | — |
| [challenge-ep2/d88205-bb-e](../../server-catalogue/challenge-ep2/d88205-bb-e/README.md) | 1 | 2 / 2 | — |
| [challenge-ep2/d88205-bb-e](../../server-catalogue/challenge-ep2/d88205-bb-e/README.md) | 1 | 3 / 1 | — |
| [challenge-ep2/d88205-bb-e](../../server-catalogue/challenge-ep2/d88205-bb-e/README.md) | 1 | 3 / 1 | — |
| [challenge-ep2/d88205-bb-e](../../server-catalogue/challenge-ep2/d88205-bb-e/README.md) | 1 | 5 / 2 | — |
| [challenge-ep2/d88205-bb-e](../../server-catalogue/challenge-ep2/d88205-bb-e/README.md) | 2 | 2 / 1 | — |
| [challenge-ep2/d88205-bb-e](../../server-catalogue/challenge-ep2/d88205-bb-e/README.md) | 2 | 5 / 1 | — |
| [challenge-ep2/d88205-bb-e](../../server-catalogue/challenge-ep2/d88205-bb-e/README.md) | 2 | 5 / 1 | — |
| [challenge-ep2/d88205-bb-j](../../server-catalogue/challenge-ep2/d88205-bb-j/README.md) | 1 | 2 / 2 | — |
| [challenge-ep2/d88205-bb-j](../../server-catalogue/challenge-ep2/d88205-bb-j/README.md) | 1 | 3 / 1 | — |
| [challenge-ep2/d88205-bb-j](../../server-catalogue/challenge-ep2/d88205-bb-j/README.md) | 1 | 3 / 1 | — |
| [challenge-ep2/d88205-bb-j](../../server-catalogue/challenge-ep2/d88205-bb-j/README.md) | 1 | 5 / 2 | — |
| [challenge-ep2/d88205-bb-j](../../server-catalogue/challenge-ep2/d88205-bb-j/README.md) | 2 | 2 / 1 | — |
| [challenge-ep2/d88205-bb-j](../../server-catalogue/challenge-ep2/d88205-bb-j/README.md) | 2 | 5 / 1 | — |
| [challenge-ep2/d88205-bb-j](../../server-catalogue/challenge-ep2/d88205-bb-j/README.md) | 2 | 5 / 1 | — |
| [events-ep2/q56-bb-e](../../server-catalogue/events-ep2/q56-bb-e/README.md) | 17 | 2 / 2 | — |
| [events-ep2/q56-bb-e](../../server-catalogue/events-ep2/q56-bb-e/README.md) | 17 | 3 / 1 | — |
| [events-ep2/q56-bb-e](../../server-catalogue/events-ep2/q56-bb-e/README.md) | 17 | 3 / 1 | — |
| [events-ep2/q56-bb-e](../../server-catalogue/events-ep2/q56-bb-e/README.md) | 17 | 5 / 2 | — |
| [events-ep2/q56-bb-j](../../server-catalogue/events-ep2/q56-bb-j/README.md) | 17 | 2 / 2 | — |
| [events-ep2/q56-bb-j](../../server-catalogue/events-ep2/q56-bb-j/README.md) | 17 | 3 / 1 | — |
| [events-ep2/q56-bb-j](../../server-catalogue/events-ep2/q56-bb-j/README.md) | 17 | 3 / 1 | — |
| [events-ep2/q56-bb-j](../../server-catalogue/events-ep2/q56-bb-j/README.md) | 17 | 5 / 2 | — |
| [events-ep2/q83-bb-e](../../server-catalogue/events-ep2/q83-bb-e/README.md) | 5 | 3 / 3 | — |
| [events-ep2/q83-bb-e](../../server-catalogue/events-ep2/q83-bb-e/README.md) | 5 | 3 / 3 | — |
| [events-ep2/q83-bb-e](../../server-catalogue/events-ep2/q83-bb-e/README.md) | 5 | 10 / 2 | — |
| [events-ep2/q83-bb-e](../../server-catalogue/events-ep2/q83-bb-e/README.md) | 6 | 4 / 4 | — |
