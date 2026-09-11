# Leo

DAT ID **0x00F4 / 244**, constructor **TObjNpcNgcBase(0x00F4)**.

[Definition source](../../quest-knowledge/reference/server-source/Map.cc#L2608) · [Database index](../npcs.md)

## Source-documented areas

Episode 2: Lab (area 0x12, default floor 0); Episode 2: Seabed Upper Levels (area 0x1C, default floor 10); Episode 2: Seabed Lower Levels (area 0x1D, default floor 11); Episode 4: Pioneer 2 (area 0x2D, default floor 0); Episode 4: Crater (Eastern Route) (area 0x24, default floor 1); Episode 4: Crater (Western Route) (area 0x25, default floor 2); Episode 4: Crater (Southern Route) (area 0x26, default floor 3); Episode 4: Crater (Northern Route) (area 0x27, default floor 4); Episode 4: Crater Interior (area 0x28, default floor 5); Episode 4: Subterranean Desert 1 (area 0x29, default floor 6); Episode 4: Subterranean Desert 2 (area 0x2A, default floor 7); Episode 4: Subterranean Desert 3 (area 0x2B, default floor 8); Episode 4: Meteor Impact Site (area 0x2C, default floor 9)

Floor numbers are script slots. Resolve the quest map designation to an area before checking compatibility. Custom client patches may change constructor availability; this table describes the stored reference, not a live client test.

## Parameters and source notes

```text
No per-type parameter comment in this definition. Inspect the source and generic NPC rules where applicable.
TODO
```

## Observed quest placements

41 records, including language duplicates. These are observations, not spawn permissions.

[All observed positions, angles, parameters and handler candidates](../observations/00F4.csv)

| Quest | Floor | Room / wave | Handler candidate |
|---|---:|---|---|
| [events-ep2/q134-bb-e](../../server-catalogue/events-ep2/q134-bb-e/README.md) | 0 | 70 / 0 | label0410 |
| [events-ep2/q134-bb-j](../../server-catalogue/events-ep2/q134-bb-j/README.md) | 0 | 70 / 0 | label0410 |
| [extermination-ep2/q165-bb-e](../../server-catalogue/extermination-ep2/q165-bb-e/README.md) | 0 | 10 / 5 | [label0051](../../server-catalogue/extermination-ep2/q165-bb-e/script.txt#L556) |
| [extermination-ep2/q173-bb-e](../../server-catalogue/extermination-ep2/q173-bb-e/README.md) | 0 | 20 / 0 | [label0050](../../server-catalogue/extermination-ep2/q173-bb-e/script.txt#L601) |
| [extermination-ep2/q280-bb-e](../../server-catalogue/extermination-ep2/q280-bb-e/README.md) | 0 | 42 / 0 | [label00C8](../../server-catalogue/extermination-ep2/q280-bb-e/script.txt#L195) |
| [government-ep4/q703-bb-e](../../server-catalogue/government-ep4/q703-bb-e/README.md) | 3 | 60 / 0 | [label044F](../../server-catalogue/government-ep4/q703-bb-e/script.txt#L838) |
| [government-ep4/q703-bb-j](../../server-catalogue/government-ep4/q703-bb-j/README.md) | 3 | 60 / 0 | [label044F](../../server-catalogue/government-ep4/q703-bb-j/script.txt#L838) |
| [government-ep4/q704-bb-e](../../server-catalogue/government-ep4/q704-bb-e/README.md) | 5 | 10 / 0 | label045C |
| [government-ep4/q704-bb-e](../../server-catalogue/government-ep4/q704-bb-e/README.md) | 5 | 10 / 0 | label045C |
| [government-ep4/q704-bb-e](../../server-catalogue/government-ep4/q704-bb-e/README.md) | 5 | 10 / 0 | label045C |
| [government-ep4/q704-bb-j](../../server-catalogue/government-ep4/q704-bb-j/README.md) | 5 | 10 / 0 | label045C |
| [government-ep4/q704-bb-j](../../server-catalogue/government-ep4/q704-bb-j/README.md) | 5 | 10 / 0 | label045C |
| [government-ep4/q704-bb-j](../../server-catalogue/government-ep4/q704-bb-j/README.md) | 5 | 10 / 0 | label045C |
| [government-ep4/q705-bb-e](../../server-catalogue/government-ep4/q705-bb-e/README.md) | 6 | 40 / 0 | label0451 |
| [government-ep4/q705-bb-e](../../server-catalogue/government-ep4/q705-bb-e/README.md) | 6 | 63 / 0 | — |
| [government-ep4/q705-bb-e](../../server-catalogue/government-ep4/q705-bb-e/README.md) | 6 | 63 / 0 | — |
| [government-ep4/q705-bb-j](../../server-catalogue/government-ep4/q705-bb-j/README.md) | 6 | 40 / 0 | label0451 |
| [government-ep4/q705-bb-j](../../server-catalogue/government-ep4/q705-bb-j/README.md) | 6 | 63 / 0 | — |
| [government-ep4/q705-bb-j](../../server-catalogue/government-ep4/q705-bb-j/README.md) | 6 | 63 / 0 | — |
| [government-ep4/q707-bb-e](../../server-catalogue/government-ep4/q707-bb-e/README.md) | 8 | 42 / 0 | label0456 |
| [government-ep4/q707-bb-j](../../server-catalogue/government-ep4/q707-bb-j/README.md) | 8 | 42 / 0 | label0456 |
| [government-ep4/q708-bb-e](../../server-catalogue/government-ep4/q708-bb-e/README.md) | 8 | 110 / 0 | [label0455](../../server-catalogue/government-ep4/q708-bb-e/script.txt#L1116) |
| [government-ep4/q708-bb-e](../../server-catalogue/government-ep4/q708-bb-e/README.md) | 8 | 110 / 0 | label0456 |
| [government-ep4/q708-bb-j](../../server-catalogue/government-ep4/q708-bb-j/README.md) | 8 | 110 / 0 | [label0455](../../server-catalogue/government-ep4/q708-bb-j/script.txt#L1118) |
| [government-ep4/q708-bb-j](../../server-catalogue/government-ep4/q708-bb-j/README.md) | 8 | 110 / 0 | label0456 |
| [solo-extra-ep1/q032-bb-e](../../server-catalogue/solo-extra-ep1/q032-bb-e/README.md) | 6 | 110 / 0 | label0CE4 |
| [solo-extra-ep1/q032-bb-e](../../server-catalogue/solo-extra-ep1/q032-bb-e/README.md) | 6 | 110 / 0 | label0CE4 |
| [solo-extra-ep1/q032-bb-e](../../server-catalogue/solo-extra-ep1/q032-bb-e/README.md) | 6 | 110 / 0 | label0CE4 |
| [solo-extra-ep1/q032-bb-j](../../server-catalogue/solo-extra-ep1/q032-bb-j/README.md) | 6 | 110 / 0 | label0CE4 |
| [solo-extra-ep1/q032-bb-j](../../server-catalogue/solo-extra-ep1/q032-bb-j/README.md) | 6 | 110 / 0 | label0CE4 |
