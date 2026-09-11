# Monest

DAT ID **0x0042 / 66**, constructor **TObjEneBm3FlyNest**.

[Definition source](../../quest-knowledge/reference/server-source/Map.cc#L2816) · [Database index](../monsters.md)

## Source-documented areas

Episode 1: Forest 1 (area 0x01, default floor 1); Episode 1: Forest 2 (area 0x02, default floor 2); Episode 2: VR Temple Alpha (area 0x13, default floor 1); Episode 2: VR Temple Beta (area 0x14, default floor 2)

Floor numbers are script slots. Resolve the quest map designation to an area before checking compatibility. Custom client patches may change constructor availability; this table describes the stored reference, not a live client test.

## Parameters and source notes

```text
Monest (and Mothmants). Params:
param2 = number of Mothmants to expel at start (clamped to [0, 6])
param3 = total Mothmants (clamped to [0, min(30, num_children)] where num_children comes from the
EnemySetEntry; if this is less than param2, then param2 will take precedence but no further Mothmants will
emerge after the first group)
Note: In map_forest01_02e.dat in the vanilla map files there is a Monest that has param1 = 3 and param2 = 10.
This looks like just an off-by-one error on Sega's part where they accidentally shifted the parameters down by
one place. As described above, this Monest expels 6 Mothmants immediately, then none after those 6 are killed.

```

## Observed quest placements

826 records, including language duplicates. These are observations, not spawn permissions.

[All observed positions, angles, parameters and handler candidates](../observations/0042.csv)

| Quest | Floor | Room / wave | Handler candidate |
|---|---:|---|---|
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 2 / 2 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 2 / 3 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 2 / 4 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 2 / 4 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 2 / 4 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 11 / 1 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 11 / 1 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 11 / 1 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 11 / 1 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 11 / 1 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 11 / 1 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 11 / 1 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 11 / 1 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 11 / 1 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 11 / 1 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 6 / 3 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 6 / 3 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 6 / 3 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 6 / 3 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 6 / 4 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 6 / 4 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 6 / 4 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 6 / 4 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 6 / 4 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 6 / 4 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 3 / 1 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 3 / 2 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 3 / 3 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 3 / 4 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 3 / 5 | — |
