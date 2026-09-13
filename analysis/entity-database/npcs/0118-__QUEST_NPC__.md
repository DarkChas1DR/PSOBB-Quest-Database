# Rupika

DAT ID **0x0118 / 280**, constructor **__QUEST_NPC__**.

[Definition source](../../quest-knowledge/reference/server-source/Map.cc#L2637) · [Database index](../npcs.md)

## Source-documented areas

Episode 4: Pioneer 2 (area 0x2D, default floor 0); Episode 4: Crater (Eastern Route) (area 0x24, default floor 1); Episode 4: Crater (Western Route) (area 0x25, default floor 2); Episode 4: Crater (Southern Route) (area 0x26, default floor 3); Episode 4: Crater (Northern Route) (area 0x27, default floor 4); Episode 4: Crater Interior (area 0x28, default floor 5); Episode 4: Subterranean Desert 1 (area 0x29, default floor 6); Episode 4: Subterranean Desert 2 (area 0x2A, default floor 7); Episode 4: Subterranean Desert 3 (area 0x2B, default floor 8); Episode 4: Meteor Impact Site (area 0x2C, default floor 9); Episode 4: Test Map (area 0x2E, default floor 10)

Floor numbers are script slots. Resolve the quest map designation to an area before checking compatibility. Custom client patches may change constructor availability; this table describes the stored reference, not a live client test.

## Parameters and source notes

```text
Quest NPC. Params are the same as for the standard NPCs above, except:
param6 low byte = flags (bit field):
01 = same as param6 above (0 = stand still; 1 = walk around)
10 = TODO
param6 high byte = NPC index in npcplayerchar.dat

```

## Observed quest placements

161 records, including language duplicates. These are observations, not spawn permissions.

[All observed positions, angles, parameters and handler candidates](../observations/0118.csv)

| Quest | Floor | Room / wave | Handler candidate |
|---|---:|---|---|
| [government-ep4/q701-bb-e](../../server-catalogue/government-ep4/q701-bb-e/README.md) | 0 | 40 / 0 | [label044C](../../server-catalogue/government-ep4/q701-bb-e/script.txt#L723) |
| [government-ep4/q701-bb-e](../../server-catalogue/government-ep4/q701-bb-e/README.md) | 1 | 21 / 0 | [label044F](../../server-catalogue/government-ep4/q701-bb-e/script.txt#L853) |
| [government-ep4/q701-bb-e](../../server-catalogue/government-ep4/q701-bb-e/README.md) | 1 | 60 / 0 | [label0452](../../server-catalogue/government-ep4/q701-bb-e/script.txt#L1061) |
| [government-ep4/q701-bb-e](../../server-catalogue/government-ep4/q701-bb-e/README.md) | 1 | 60 / 0 | [label0450](../../server-catalogue/government-ep4/q701-bb-e/script.txt#L951) |
| [government-ep4/q701-bb-e](../../server-catalogue/government-ep4/q701-bb-e/README.md) | 1 | 60 / 0 | [label044F](../../server-catalogue/government-ep4/q701-bb-e/script.txt#L853) |
| [government-ep4/q701-bb-e](../../server-catalogue/government-ep4/q701-bb-e/README.md) | 1 | 60 / 0 | [label044F](../../server-catalogue/government-ep4/q701-bb-e/script.txt#L853) |
| [government-ep4/q701-bb-e](../../server-catalogue/government-ep4/q701-bb-e/README.md) | 1 | 80 / 0 | [label0450](../../server-catalogue/government-ep4/q701-bb-e/script.txt#L951) |
| [government-ep4/q701-bb-j](../../server-catalogue/government-ep4/q701-bb-j/README.md) | 0 | 40 / 0 | [label044C](../../server-catalogue/government-ep4/q701-bb-j/script.txt#L723) |
| [government-ep4/q701-bb-j](../../server-catalogue/government-ep4/q701-bb-j/README.md) | 1 | 21 / 0 | [label044F](../../server-catalogue/government-ep4/q701-bb-j/script.txt#L853) |
| [government-ep4/q701-bb-j](../../server-catalogue/government-ep4/q701-bb-j/README.md) | 1 | 60 / 0 | [label0452](../../server-catalogue/government-ep4/q701-bb-j/script.txt#L1061) |
| [government-ep4/q701-bb-j](../../server-catalogue/government-ep4/q701-bb-j/README.md) | 1 | 60 / 0 | [label0450](../../server-catalogue/government-ep4/q701-bb-j/script.txt#L951) |
| [government-ep4/q701-bb-j](../../server-catalogue/government-ep4/q701-bb-j/README.md) | 1 | 60 / 0 | [label044F](../../server-catalogue/government-ep4/q701-bb-j/script.txt#L853) |
| [government-ep4/q701-bb-j](../../server-catalogue/government-ep4/q701-bb-j/README.md) | 1 | 60 / 0 | [label044F](../../server-catalogue/government-ep4/q701-bb-j/script.txt#L853) |
| [government-ep4/q701-bb-j](../../server-catalogue/government-ep4/q701-bb-j/README.md) | 1 | 80 / 0 | [label0450](../../server-catalogue/government-ep4/q701-bb-j/script.txt#L951) |
| [government-ep4/q702-bb-e](../../server-catalogue/government-ep4/q702-bb-e/README.md) | 2 | 10 / 0 | [label044E](../../server-catalogue/government-ep4/q702-bb-e/script.txt#L1300) |
| [government-ep4/q702-bb-e](../../server-catalogue/government-ep4/q702-bb-e/README.md) | 2 | 20 / 0 | label044F |
| [government-ep4/q702-bb-e](../../server-catalogue/government-ep4/q702-bb-e/README.md) | 2 | 30 / 0 | [label044C](../../server-catalogue/government-ep4/q702-bb-e/script.txt#L937) |
| [government-ep4/q702-bb-e](../../server-catalogue/government-ep4/q702-bb-e/README.md) | 2 | 50 / 0 | [label044D](../../server-catalogue/government-ep4/q702-bb-e/script.txt#L1062) |
| [government-ep4/q702-bb-j](../../server-catalogue/government-ep4/q702-bb-j/README.md) | 2 | 10 / 0 | [label044E](../../server-catalogue/government-ep4/q702-bb-j/script.txt#L1300) |
| [government-ep4/q702-bb-j](../../server-catalogue/government-ep4/q702-bb-j/README.md) | 2 | 20 / 0 | label044F |
| [government-ep4/q702-bb-j](../../server-catalogue/government-ep4/q702-bb-j/README.md) | 2 | 30 / 0 | [label044C](../../server-catalogue/government-ep4/q702-bb-j/script.txt#L937) |
| [government-ep4/q702-bb-j](../../server-catalogue/government-ep4/q702-bb-j/README.md) | 2 | 50 / 0 | [label044D](../../server-catalogue/government-ep4/q702-bb-j/script.txt#L1062) |
| [government-ep4/q703-bb-e](../../server-catalogue/government-ep4/q703-bb-e/README.md) | 3 | 30 / 0 | [label044D](../../server-catalogue/government-ep4/q703-bb-e/script.txt#L781) |
| [government-ep4/q703-bb-e](../../server-catalogue/government-ep4/q703-bb-e/README.md) | 3 | 60 / 0 | [label044E](../../server-catalogue/government-ep4/q703-bb-e/script.txt#L828) |
| [government-ep4/q703-bb-e](../../server-catalogue/government-ep4/q703-bb-e/README.md) | 3 | 60 / 0 | [label0451](../../server-catalogue/government-ep4/q703-bb-e/script.txt#L894) |
| [government-ep4/q703-bb-e](../../server-catalogue/government-ep4/q703-bb-e/README.md) | 3 | 60 / 0 | [label0452](../../server-catalogue/government-ep4/q703-bb-e/script.txt#L906) |
| [government-ep4/q703-bb-e](../../server-catalogue/government-ep4/q703-bb-e/README.md) | 3 | 90 / 0 | [label044C](../../server-catalogue/government-ep4/q703-bb-e/script.txt#L718) |
| [government-ep4/q703-bb-j](../../server-catalogue/government-ep4/q703-bb-j/README.md) | 3 | 30 / 0 | [label044D](../../server-catalogue/government-ep4/q703-bb-j/script.txt#L781) |
| [government-ep4/q703-bb-j](../../server-catalogue/government-ep4/q703-bb-j/README.md) | 3 | 60 / 0 | [label044E](../../server-catalogue/government-ep4/q703-bb-j/script.txt#L828) |
| [government-ep4/q703-bb-j](../../server-catalogue/government-ep4/q703-bb-j/README.md) | 3 | 60 / 0 | [label0451](../../server-catalogue/government-ep4/q703-bb-j/script.txt#L894) |
