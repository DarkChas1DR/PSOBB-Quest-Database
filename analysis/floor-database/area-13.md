# Episode 2: VR Temple Alpha

[General floor database](README.md)

| Identifier | Value |
|---|---|
| Default floor slot | 1 |
| Area ID | 19 / 0x13 |

A quest can designate an area into a different floor slot. These identifiers must not be treated as interchangeable.

## Available map-table entries

Layout and entity variation are separate indices. On = multiplayer; Off = solo; Ulti tables are the Ultimate-specific map tables. Entries reflect supplied client resources, not a quest’s chosen runtime configuration.

| Table | Layout | Entity variation | Object basename | Enemy/event basename | Setup basename |
|---|---:|---:|---|---|---|
| [SetDataTableOff](tables/SetDataTableOff.txt#L106) | 0 | 0 | map_ruins01_00_00_off | map_ruins01_00_00_off | map_ruins01_00 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L107) | 1 | 0 | map_ruins01_01_00_off | map_ruins01_01_00_off | map_ruins01_01 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L108) | 2 | 0 | map_ruins01_02_00_off | map_ruins01_02_00_off | map_ruins01_02 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L106) | 0 | 0 | map_ruins01_00_00_off | map_ruins01_00_00_off | map_ruins01_00 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L107) | 1 | 0 | map_ruins01_01_00_off | map_ruins01_01_00_off | map_ruins01_01 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L108) | 2 | 0 | map_ruins01_02_00_off | map_ruins01_02_00_off | map_ruins01_02 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L127) | 0 | 0 | map_ruins01_00_00 | map_ruins01_00_00 | map_ruins01_00 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L128) | 1 | 0 | map_ruins01_01_00 | map_ruins01_01_00 | map_ruins01_01 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L129) | 2 | 0 | map_ruins01_02_00 | map_ruins01_02_00 | map_ruins01_02 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L127) | 0 | 0 | map_ruins01_00_00 | map_ruins01_00_00 | map_ruins01_00 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L128) | 1 | 0 | map_ruins01_01_00 | map_ruins01_01_00 | map_ruins01_01 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L129) | 2 | 0 | map_ruins01_02_00 | map_ruins01_02_00 | map_ruins01_02 |

## Qedit placement menus

Bundled and external definitions remain separate. The external BB list is monsv4/itemv4. Menu inclusion is editor evidence, not a runtime compatibility test.

### qedit-config

**mons:** 165 (Darth Belra), 166 (Dimenian), 96 (Grass Asassin), 64 (Hildebear), 65 (Rag Rappy / Sand Rappy), 66 (Monest), 97 (Poison Lily / Del Lily)

**item:** 0, 1, 2, 3, 4, 7, 8, 10, 11, 12, 13, 14, 18, 19, 24, 25, 27, 34, 35, 36, 37, 39, 222, 352, 353, 354, 355, 356, 357, 359, 400, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 553, 139, 144, 696, 195, 150, 132, 129, 192, 339


### qedit-external

**monsv4:** 65 (Rag Rappy / Sand Rappy), 64 (Hildebear), 96 (Grass Asassin), 97 (Poison Lily / Del Lily), 66 (Monest), 166 (Dimenian), 165 (Darth Belra), 51 (Stage NPC's)

**itemv4:** 0, 4, 14, 6, 40, 41, 7, 24, 1, 23, 2, 3, 25, 697, 10, 11, 12, 13, 8, 18, 21, 696, 698, 22, 150, 131, 132, 129, 144, 192, 257, 31, 34, 35, 32, 33, 139, 222, 37, 38, 416, 353, 354, 355, 356, 357, 30, 424, 417, 418, 419, 420, 421, 422, 423, 425, 426, 195, 359, 339, 427, 19, 39, 553, 36


## Rooms, collision and coordinates

Room boundaries, transforms, empty-room IDs, valid walkable spawn positions and safe player spawn points have not yet been decoded for this layout family. This page is a general floor/resource reference, not a finished geometry atlas.

[Observed quest section index](../map-sections/README.md) can supply examples, but copying a room ID or coordinate requires verifying the exact layout.

[Documented monster constructor availability](../entity-database/areas.md) · [Qedit entity fields](../entity-database/qedit/entity-fields.md)
