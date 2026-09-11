# TObjEneDarkGunCenter

DAT ID **0x00A3 / 163**, constructor **TObjEneDarkGunCenter**.

[Definition source](../../quest-knowledge/reference/server-source/Map.cc#L2921) · [Database index](../monsters.md)

## Source-documented areas

Episode 1: Ruins 2 (area 0x09, default floor 9); Episode 1: Ruins 3 (area 0x0A, default floor 10)

Floor numbers are script slots. Resolve the quest map designation to an area before checking compatibility. Custom client patches may change constructor availability; this table describes the stored reference, not a live client test.

## Parameters and source notes

```text
Dark Gunner control enemy. This enemy doesn't actually exist in-game; it only has logic for choosing a Dark
Gunner from its group to be the leader, and then changing this leader periodically. Params:
param1 = group number (see TObjEneDarkGunner above)

```

## Observed quest placements

385 records, including language duplicates. These are observations, not spawn permissions.

[All observed positions, angles, parameters and handler candidates](../observations/00A3.csv)

| Quest | Floor | Room / wave | Handler candidate |
|---|---:|---|---|
| [events-ep1/q66-bb-e](../../server-catalogue/events-ep1/q66-bb-e/README.md) | 9 | 40 / 3 | — |
| [events-ep1/q66-bb-e](../../server-catalogue/events-ep1/q66-bb-e/README.md) | 9 | 20 / 1 | — |
| [events-ep1/q66-bb-e](../../server-catalogue/events-ep1/q66-bb-e/README.md) | 9 | 31 / 5 | — |
| [events-ep1/q66-bb-e](../../server-catalogue/events-ep1/q66-bb-e/README.md) | 9 | 20 / 7 | — |
| [events-ep1/q66-bb-e](../../server-catalogue/events-ep1/q66-bb-e/README.md) | 9 | 80 / 1 | — |
| [events-ep1/q66-bb-e](../../server-catalogue/events-ep1/q66-bb-e/README.md) | 9 | 80 / 5 | — |
| [events-ep1/q66-bb-e](../../server-catalogue/events-ep1/q66-bb-e/README.md) | 9 | 80 / 10 | — |
| [events-ep1/q66-bb-e](../../server-catalogue/events-ep1/q66-bb-e/README.md) | 10 | 30 / 1 | — |
| [events-ep1/q66-bb-e](../../server-catalogue/events-ep1/q66-bb-e/README.md) | 10 | 43 / 4 | — |
| [events-ep1/q66-bb-e](../../server-catalogue/events-ep1/q66-bb-e/README.md) | 10 | 22 / 2 | — |
| [events-ep1/q66-bb-e](../../server-catalogue/events-ep1/q66-bb-e/README.md) | 10 | 75 / 1 | — |
| [events-ep1/q66-bb-e](../../server-catalogue/events-ep1/q66-bb-e/README.md) | 10 | 44 / 2 | — |
| [events-ep1/q66-bb-e](../../server-catalogue/events-ep1/q66-bb-e/README.md) | 10 | 31 / 1 | — |
| [events-ep1/q66-bb-e](../../server-catalogue/events-ep1/q66-bb-e/README.md) | 10 | 80 / 6 | — |
| [events-ep1/q66-bb-j](../../server-catalogue/events-ep1/q66-bb-j/README.md) | 9 | 40 / 3 | — |
| [events-ep1/q66-bb-j](../../server-catalogue/events-ep1/q66-bb-j/README.md) | 9 | 20 / 1 | — |
| [events-ep1/q66-bb-j](../../server-catalogue/events-ep1/q66-bb-j/README.md) | 9 | 31 / 5 | — |
| [events-ep1/q66-bb-j](../../server-catalogue/events-ep1/q66-bb-j/README.md) | 9 | 20 / 7 | — |
| [events-ep1/q66-bb-j](../../server-catalogue/events-ep1/q66-bb-j/README.md) | 9 | 80 / 1 | — |
| [events-ep1/q66-bb-j](../../server-catalogue/events-ep1/q66-bb-j/README.md) | 9 | 80 / 5 | — |
| [events-ep1/q66-bb-j](../../server-catalogue/events-ep1/q66-bb-j/README.md) | 9 | 80 / 10 | — |
| [events-ep1/q66-bb-j](../../server-catalogue/events-ep1/q66-bb-j/README.md) | 10 | 30 / 1 | — |
| [events-ep1/q66-bb-j](../../server-catalogue/events-ep1/q66-bb-j/README.md) | 10 | 43 / 4 | — |
| [events-ep1/q66-bb-j](../../server-catalogue/events-ep1/q66-bb-j/README.md) | 10 | 22 / 2 | — |
| [events-ep1/q66-bb-j](../../server-catalogue/events-ep1/q66-bb-j/README.md) | 10 | 75 / 1 | — |
| [events-ep1/q66-bb-j](../../server-catalogue/events-ep1/q66-bb-j/README.md) | 10 | 44 / 2 | — |
| [events-ep1/q66-bb-j](../../server-catalogue/events-ep1/q66-bb-j/README.md) | 10 | 31 / 1 | — |
| [events-ep1/q66-bb-j](../../server-catalogue/events-ep1/q66-bb-j/README.md) | 10 | 80 / 6 | — |
| [events-ep1/q070-bb-e](../../server-catalogue/events-ep1/q070-bb-e/README.md) | 9 | 21 / 1 | — |
| [events-ep1/q070-bb-e](../../server-catalogue/events-ep1/q070-bb-e/README.md) | 9 | 23 / 2 | — |
