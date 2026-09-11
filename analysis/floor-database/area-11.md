# Episode 1: Palace

[General floor database](README.md)

| Identifier | Value |
|---|---|
| Default floor slot | 17 |
| Area ID | 17 / 0x11 |

A quest can designate an area into a different floor slot. These identifiers must not be treated as interchangeable.

## Available map-table entries

Layout and entity variation are separate indices. On = multiplayer; Off = solo; Ulti tables are the Ultimate-specific map tables. Entries reflect supplied client resources, not a quest’s chosen runtime configuration.

| Table | Layout | Entity variation | Object basename | Enemy/event basename | Setup basename |
|---|---:|---:|---|---|---|
| [SetDataTableOff](tables/SetDataTableOff.txt#L102) | 0 | 0 | map_vs02_00 | map_vs02_00 | map_vs02_00 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L103) | 1 | 0 | map_vs02_01 | map_vs02_01 | map_vs02_01 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L104) | 2 | 0 | map_vs02_02 | map_vs02_02 | map_vs02_02 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L102) | 0 | 0 | map_vs02_00 | map_vs02_00 | map_vs02_00 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L103) | 1 | 0 | map_vs02_01 | map_vs02_01 | map_vs02_01 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L104) | 2 | 0 | map_vs02_02 | map_vs02_02 | map_vs02_02 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L123) | 0 | 0 | map_vs02_00 | map_vs02_00 | map_vs02_00 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L124) | 1 | 0 | map_vs02_01 | map_vs02_01 | map_vs02_01 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L125) | 2 | 0 | map_vs02_02 | map_vs02_02 | map_vs02_02 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L123) | 0 | 0 | map_vs02_00 | map_vs02_00 | map_vs02_00 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L124) | 1 | 0 | map_vs02_01 | map_vs02_01 | map_vs02_01 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L125) | 2 | 0 | map_vs02_02 | map_vs02_02 | map_vs02_02 |

## Qedit placement menus

Bundled and external definitions remain separate. The external BB list is monsv4/itemv4. Menu inclusion is editor evidence, not a runtime compatibility test.

### qedit-config

**mons:** Empty list

**item:** 0, 1, 2, 3, 4, 7, 8, 10, 11, 12, 13, 14, 18, 19, 24, 25, 27, 30, 32, 33, 34, 35, 36, 37, 39, 130, 132, 144, 150, 222, 257, 352, 353, 354, 355, 356, 357, 359, 400, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 553


### qedit-external

**monsv4:** 64 (Hildebear), 99 (evil shark), 96 (Grass Asassin), 130 (Sinow Blue), 160 (Delsaber), 164 (Chaos Bringer), 51 (Stage NPC's)

**itemv4:** 0, 4, 6, 40, 41, 7, 30, 424, 1, 416, 417, 418, 419, 420, 421, 422, 423, 20, 353, 354, 355, 356, 10, 11, 12, 13, 8, 130, 150, 131, 132, 3, 697, 144, 192, 257, 425, 426, 31, 34, 35, 32, 33, 357, 222, 36, 139, 37, 38


## Rooms, collision and coordinates

Room boundaries, transforms, empty-room IDs, valid walkable spawn positions and safe player spawn points have not yet been decoded for this layout family. This page is a general floor/resource reference, not a finished geometry atlas.

[Observed quest section index](../map-sections/README.md) can supply examples, but copying a room ID or coordinate requires verifying the exact layout.

[Documented monster constructor availability](../entity-database/areas.md) · [Qedit entity fields](../entity-database/qedit/entity-fields.md)
