# Episode 1: Mine 1

[General floor database](README.md)

| Identifier | Value |
|---|---|
| Default floor slot | 6 |
| Area ID | 6 / 0x06 |

A quest can designate an area into a different floor slot. These identifiers must not be treated as interchangeable.

## Available map-table entries

Layout and entity variation are separate indices. On = multiplayer; Off = solo; Ulti tables are the Ultimate-specific map tables. Entries reflect supplied client resources, not a quest’s chosen runtime configuration.

| Table | Layout | Entity variation | Object basename | Enemy/event basename | Setup basename |
|---|---:|---:|---|---|---|
| [SetDataTableOff](tables/SetDataTableOff.txt#L26) | 0 | 0 | map_machine01_00_00 | map_machine01_00_00 | map_machine01_00 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L27) | 0 | 1 | map_machine01_00_01 | map_machine01_00_01 | map_machine01_00 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L28) | 1 | 0 | map_machine01_01_00 | map_machine01_01_00 | map_machine01_01 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L29) | 1 | 1 | map_machine01_01_01 | map_machine01_01_01 | map_machine01_01 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L30) | 2 | 0 | map_machine01_02_00 | map_machine01_02_00 | map_machine01_02 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L31) | 2 | 1 | map_machine01_02_01 | map_machine01_02_01 | map_machine01_02 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L32) | 3 | 0 | map_machine01_03_00 | map_machine01_03_00 | map_machine01_03 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L33) | 3 | 1 | map_machine01_03_01 | map_machine01_03_01 | map_machine01_03 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L34) | 4 | 0 | map_machine01_04_00 | map_machine01_04_00 | map_machine01_04 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L35) | 4 | 1 | map_machine01_04_01 | map_machine01_04_01 | map_machine01_04 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L36) | 5 | 0 | map_machine01_05_00 | map_machine05_04_00 | map_machine01_05 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L37) | 5 | 1 | map_machine01_05_01 | map_machine05_04_01 | map_machine01_05 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L26) | 0 | 0 | map_machine01_00_00 | map_machine01_00_00 | map_machine01_00 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L27) | 0 | 1 | map_machine01_00_01 | map_machine01_00_01 | map_machine01_00 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L28) | 1 | 0 | map_machine01_01_00 | map_machine01_01_00 | map_machine01_01 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L29) | 1 | 1 | map_machine01_01_01 | map_machine01_01_01 | map_machine01_01 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L30) | 2 | 0 | map_machine01_02_00 | map_machine01_02_00 | map_machine01_02 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L31) | 2 | 1 | map_machine01_02_01 | map_machine01_02_01 | map_machine01_02 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L32) | 3 | 0 | map_machine01_03_00 | map_machine01_03_00 | map_machine01_03 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L33) | 3 | 1 | map_machine01_03_01 | map_machine01_03_01 | map_machine01_03 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L34) | 4 | 0 | map_machine01_04_00 | map_machine01_04_00 | map_machine01_04 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L35) | 4 | 1 | map_machine01_04_01 | map_machine01_04_01 | map_machine01_04 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L36) | 5 | 0 | map_machine01_05_00 | map_machine05_04_00 | map_machine01_05 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L37) | 5 | 1 | map_machine01_05_01 | map_machine05_04_01 | map_machine01_05 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L47) | 0 | 0 | map_machine01_00_00 | map_machine01_00_00 | map_machine01_00 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L48) | 0 | 1 | map_machine01_00_01 | map_machine01_00_01 | map_machine01_00 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L49) | 1 | 0 | map_machine01_01_00 | map_machine01_01_00 | map_machine01_01 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L50) | 1 | 1 | map_machine01_01_01 | map_machine01_01_01 | map_machine01_01 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L51) | 2 | 0 | map_machine01_02_00 | map_machine01_02_00 | map_machine01_02 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L52) | 2 | 1 | map_machine01_02_01 | map_machine01_02_01 | map_machine01_02 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L53) | 3 | 0 | map_machine01_03_00 | map_machine01_03_00 | map_machine01_03 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L54) | 3 | 1 | map_machine01_03_01 | map_machine01_03_01 | map_machine01_03 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L55) | 4 | 0 | map_machine01_04_00 | map_machine01_04_00 | map_machine01_04 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L56) | 4 | 1 | map_machine01_04_01 | map_machine01_04_01 | map_machine01_04 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L57) | 5 | 0 | map_machine01_05_00 | map_machine01_05_00 | map_machine01_05 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L58) | 5 | 1 | map_machine01_05_01 | map_machine01_05_01 | map_machine01_05 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L47) | 0 | 0 | map_machine01_00_00 | map_machine01_00_00 | map_machine01_00 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L48) | 0 | 1 | map_machine01_00_01 | map_machine01_00_01 | map_machine01_00 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L49) | 1 | 0 | map_machine01_01_00 | map_machine01_01_00 | map_machine01_01 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L50) | 1 | 1 | map_machine01_01_01 | map_machine01_01_01 | map_machine01_01 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L51) | 2 | 0 | map_machine01_02_00 | map_machine01_02_00 | map_machine01_02 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L52) | 2 | 1 | map_machine01_02_01 | map_machine01_02_01 | map_machine01_02 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L53) | 3 | 0 | map_machine01_03_00 | map_machine01_03_00 | map_machine01_03 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L54) | 3 | 1 | map_machine01_03_01 | map_machine01_03_01 | map_machine01_03 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L55) | 4 | 0 | map_machine01_04_00 | map_machine01_04_00 | map_machine01_04 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L56) | 4 | 1 | map_machine01_04_01 | map_machine01_04_01 | map_machine01_04 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L57) | 5 | 0 | map_machine01_05_00 | map_machine01_05_00 | map_machine01_05 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L58) | 5 | 1 | map_machine01_05_01 | map_machine01_05_01 | map_machine01_05 |

## Qedit placement menus

Bundled and external definitions remain separate. The external BB list is monsv4/itemv4. Menu inclusion is editor evidence, not a runtime compatibility test.

### qedit-config

**mons:** 128 (Gillchic), 129 (Garanz), 130 (Sinow Blue), 131 (Canadine), 132 (Canane), 133 (Dubchic Switch)

**item:** 0, 1, 2, 3, 7, 8, 10, 11, 12, 13, 14, 18, 19, 24, 25, 27, 32, 33, 34, 35, 36, 37, 129, 130, 131, 132, 136, 139, 141, 142, 144, 145, 146, 147, 149, 207, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 304, 359, 222, 150, 136


### qedit-external

**monsv4:** 51 (Stage NPC's), 128 (Gillchic), 129 (Garanz), 130 (Sinow Blue), 131 (Canadine), 132 (Canane), 133 (Dubchic Switch)

**itemv4:** 0, 1, 4, 14, 2, 3, 27, 697, 141, 142, 10, 11, 12, 13, 15, 7, 144, 8, 6, 40, 41, 18, 21, 696, 698, 136, 145, 146, 147, 19, 22, 23, 24, 130, 150, 131, 132, 256, 258, 257, 207, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 149, 31, 34, 35, 32, 33, 222, 36, 139, 37, 38, 359


## Rooms, collision and coordinates

Room boundaries, transforms, empty-room IDs, valid walkable spawn positions and safe player spawn points have not yet been decoded for this layout family. This page is a general floor/resource reference, not a finished geometry atlas.

[Observed quest section index](../map-sections/README.md) can supply examples, but copying a room ID or coordinate requires verifying the exact layout.

[Documented monster constructor availability](../entity-database/areas.md) · [Qedit entity fields](../entity-database/qedit/entity-fields.md)
