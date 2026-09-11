# Mericarol

DAT ID **0x00D6 / 214**, constructor **TObjEneBm9Mericarol**.

[Definition source](../../quest-knowledge/reference/server-source/Map.cc#L3006) · [Database index](../monsters.md)

## Source-documented areas

Episode 2: Central Control Area (area 0x17, default floor 5); Episode 2: Jungle Area North (area 0x18, default floor 6); Episode 2: Jungle Area East (area 0x19, default floor 7); Episode 2: Mountain Area (area 0x1A, default floor 8); Episode 2: Seaside Area (area 0x1B, default floor 9); Episode 2: Control Tower (area 0x23, default floor 17)

Floor numbers are script slots. Resolve the quest map designation to an area before checking compatibility. Custom client patches may change constructor availability; this table describes the stored reference, not a live client test.

## Parameters and source notes

```text
Mericarol / Mericus / Merikle / Mericarand. Params:
param1 = chance of run attack after being hit when HP is less than half of max (value used is param1 + 0.5)
param2 = speed during run attack (units per frame; value used is param2 + 3, clamped below to 1)
param3 = chance of doing spit attack when player is nearby (actual probability is param3 + 0.1; if the check
fails, it will do the slash attack instead)
param6 = subtype:
0 = Mericarol
1 = Mericus
2 = Merikle
anything else = Mericarand (see below)
If this is a Mericarand, it is "randomly" chosen to be one of the three subtypes at construction time. On v3,
the client chooses randomly (but consistently, based on the entity ID) between Mericarol (80%), Mericus (10%) or
Merikle (10%). On v4, if the entity ID isn't marked rare by the server, the Mericarand becomes a Mericarol;
otherwise, it becomes a Mericus if its entity ID is even or a Merikle if it's odd.

```

## Observed quest placements

1877 records, including language duplicates. These are observations, not spawn permissions.

[All observed positions, angles, parameters and handler candidates](../observations/00D6.csv)

| Quest | Floor | Room / wave | Handler candidate |
|---|---:|---|---|
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 2 | 2 / 1 | — |
| [challenge-ep2/d88203-bb-e](../../server-catalogue/challenge-ep2/d88203-bb-e/README.md) | 5 | 10 / 1 | — |
| [challenge-ep2/d88203-bb-j](../../server-catalogue/challenge-ep2/d88203-bb-j/README.md) | 2 | 2 / 1 | — |
| [challenge-ep2/d88203-bb-j](../../server-catalogue/challenge-ep2/d88203-bb-j/README.md) | 5 | 10 / 1 | — |
| [challenge-ep2/d88205-bb-e](../../server-catalogue/challenge-ep2/d88205-bb-e/README.md) | 1 | 2 / 1 | — |
| [challenge-ep2/d88205-bb-e](../../server-catalogue/challenge-ep2/d88205-bb-e/README.md) | 1 | 2 / 1 | — |
| [challenge-ep2/d88205-bb-e](../../server-catalogue/challenge-ep2/d88205-bb-e/README.md) | 1 | 3 / 2 | — |
| [challenge-ep2/d88205-bb-e](../../server-catalogue/challenge-ep2/d88205-bb-e/README.md) | 1 | 3 / 2 | — |
| [challenge-ep2/d88205-bb-e](../../server-catalogue/challenge-ep2/d88205-bb-e/README.md) | 1 | 5 / 2 | — |
| [challenge-ep2/d88205-bb-e](../../server-catalogue/challenge-ep2/d88205-bb-e/README.md) | 1 | 5 / 1 | — |
| [challenge-ep2/d88205-bb-e](../../server-catalogue/challenge-ep2/d88205-bb-e/README.md) | 1 | 5 / 1 | — |
| [challenge-ep2/d88205-bb-e](../../server-catalogue/challenge-ep2/d88205-bb-e/README.md) | 1 | 5 / 1 | — |
| [challenge-ep2/d88205-bb-e](../../server-catalogue/challenge-ep2/d88205-bb-e/README.md) | 2 | 2 / 1 | — |
| [challenge-ep2/d88205-bb-e](../../server-catalogue/challenge-ep2/d88205-bb-e/README.md) | 2 | 5 / 2 | — |
| [challenge-ep2/d88205-bb-e](../../server-catalogue/challenge-ep2/d88205-bb-e/README.md) | 2 | 5 / 2 | — |
| [challenge-ep2/d88205-bb-e](../../server-catalogue/challenge-ep2/d88205-bb-e/README.md) | 2 | 5 / 2 | — |
| [challenge-ep2/d88205-bb-e](../../server-catalogue/challenge-ep2/d88205-bb-e/README.md) | 2 | 5 / 2 | — |
| [challenge-ep2/d88205-bb-j](../../server-catalogue/challenge-ep2/d88205-bb-j/README.md) | 1 | 2 / 1 | — |
| [challenge-ep2/d88205-bb-j](../../server-catalogue/challenge-ep2/d88205-bb-j/README.md) | 1 | 2 / 1 | — |
| [challenge-ep2/d88205-bb-j](../../server-catalogue/challenge-ep2/d88205-bb-j/README.md) | 1 | 3 / 2 | — |
| [challenge-ep2/d88205-bb-j](../../server-catalogue/challenge-ep2/d88205-bb-j/README.md) | 1 | 3 / 2 | — |
| [challenge-ep2/d88205-bb-j](../../server-catalogue/challenge-ep2/d88205-bb-j/README.md) | 1 | 5 / 2 | — |
| [challenge-ep2/d88205-bb-j](../../server-catalogue/challenge-ep2/d88205-bb-j/README.md) | 1 | 5 / 1 | — |
| [challenge-ep2/d88205-bb-j](../../server-catalogue/challenge-ep2/d88205-bb-j/README.md) | 1 | 5 / 1 | — |
| [challenge-ep2/d88205-bb-j](../../server-catalogue/challenge-ep2/d88205-bb-j/README.md) | 1 | 5 / 1 | — |
| [challenge-ep2/d88205-bb-j](../../server-catalogue/challenge-ep2/d88205-bb-j/README.md) | 2 | 2 / 1 | — |
| [challenge-ep2/d88205-bb-j](../../server-catalogue/challenge-ep2/d88205-bb-j/README.md) | 2 | 5 / 2 | — |
| [challenge-ep2/d88205-bb-j](../../server-catalogue/challenge-ep2/d88205-bb-j/README.md) | 2 | 5 / 2 | — |
| [challenge-ep2/d88205-bb-j](../../server-catalogue/challenge-ep2/d88205-bb-j/README.md) | 2 | 5 / 2 | — |
| [challenge-ep2/d88205-bb-j](../../server-catalogue/challenge-ep2/d88205-bb-j/README.md) | 2 | 5 / 2 | — |
