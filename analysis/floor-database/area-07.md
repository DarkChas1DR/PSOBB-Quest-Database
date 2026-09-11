# Episode 1: Mine 2

[General floor database](README.md)

| Identifier | Value |
|---|---|
| Default floor slot | 7 |
| Area ID | 7 / 0x07 |

A quest can designate an area into a different floor slot. These identifiers must not be treated as interchangeable.

## Available map-table entries

Layout and entity variation are separate indices. On = multiplayer; Off = solo; Ulti tables are the Ultimate-specific map tables. Entries reflect supplied client resources, not a quest’s chosen runtime configuration.

| Table | Layout | Entity variation | Object basename | Enemy/event basename | Setup basename |
|---|---:|---:|---|---|---|
| [SetDataTableOff](tables/SetDataTableOff.txt#L38) | 0 | 0 | map_machine02_00_00 | map_machine02_00_00 | map_machine02_00 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L39) | 0 | 1 | map_machine02_00_01 | map_machine02_00_01 | map_machine02_00 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L40) | 1 | 0 | map_machine02_01_00 | map_machine02_01_00 | map_machine02_01 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L41) | 1 | 1 | map_machine02_01_01 | map_machine02_01_01 | map_machine02_01 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L42) | 2 | 0 | map_machine02_02_00 | map_machine02_02_00 | map_machine02_02 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L43) | 2 | 1 | map_machine02_02_01 | map_machine02_02_01 | map_machine02_02 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L44) | 3 | 0 | map_machine02_03_00 | map_machine02_03_00 | map_machine02_03 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L45) | 3 | 1 | map_machine02_03_01 | map_machine02_03_01 | map_machine02_03 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L46) | 4 | 0 | map_machine02_04_00 | map_machine02_04_00 | map_machine02_04 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L47) | 4 | 1 | map_machine02_04_01 | map_machine02_04_01 | map_machine02_04 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L48) | 5 | 0 | map_machine02_05_00 | map_machine02_05_00 | map_machine02_05 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L49) | 5 | 1 | map_machine02_05_01 | map_machine02_05_01 | map_machine02_05 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L38) | 0 | 0 | map_machine02_00_00 | map_machine02_00_00 | map_machine02_00 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L39) | 0 | 1 | map_machine02_00_01 | map_machine02_00_01 | map_machine02_00 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L40) | 1 | 0 | map_machine02_01_00 | map_machine02_01_00 | map_machine02_01 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L41) | 1 | 1 | map_machine02_01_01 | map_machine02_01_01 | map_machine02_01 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L42) | 2 | 0 | map_machine02_02_00 | map_machine02_02_00 | map_machine02_02 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L43) | 2 | 1 | map_machine02_02_01 | map_machine02_02_01 | map_machine02_02 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L44) | 3 | 0 | map_machine02_03_00 | map_machine02_03_00 | map_machine02_03 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L45) | 3 | 1 | map_machine02_03_01 | map_machine02_03_01 | map_machine02_03 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L46) | 4 | 0 | map_machine02_04_00 | map_machine02_04_00 | map_machine02_04 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L47) | 4 | 1 | map_machine02_04_01 | map_machine02_04_01 | map_machine02_04 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L48) | 5 | 0 | map_machine02_05_00 | map_machine02_05_00 | map_machine02_05 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L49) | 5 | 1 | map_machine02_05_01 | map_machine02_05_01 | map_machine02_05 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L59) | 0 | 0 | map_machine02_00_00 | map_machine02_00_00 | map_machine02_00 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L60) | 0 | 1 | map_machine02_00_01 | map_machine02_00_01 | map_machine02_00 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L61) | 1 | 0 | map_machine02_01_00 | map_machine02_01_00 | map_machine02_01 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L62) | 1 | 1 | map_machine02_01_01 | map_machine02_01_01 | map_machine02_01 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L63) | 2 | 0 | map_machine02_02_00 | map_machine02_02_00 | map_machine02_02 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L64) | 2 | 1 | map_machine02_02_01 | map_machine02_02_01 | map_machine02_02 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L65) | 3 | 0 | map_machine02_03_00 | map_machine02_03_00 | map_machine02_03 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L66) | 3 | 1 | map_machine02_03_01 | map_machine02_03_01 | map_machine02_03 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L67) | 4 | 0 | map_machine02_04_00 | map_machine02_04_00 | map_machine02_04 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L68) | 4 | 1 | map_machine02_04_01 | map_machine02_04_01 | map_machine02_04 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L69) | 5 | 0 | map_machine02_05_00 | map_machine02_05_00 | map_machine02_05 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L70) | 5 | 1 | map_machine02_05_01 | map_machine02_05_01 | map_machine02_05 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L59) | 0 | 0 | map_machine02_00_00 | map_machine02_00_00 | map_machine02_00 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L60) | 0 | 1 | map_machine02_00_01 | map_machine02_00_01 | map_machine02_00 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L61) | 1 | 0 | map_machine02_01_00 | map_machine02_01_00 | map_machine02_01 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L62) | 1 | 1 | map_machine02_01_01 | map_machine02_01_01 | map_machine02_01 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L63) | 2 | 0 | map_machine02_02_00 | map_machine02_02_00 | map_machine02_02 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L64) | 2 | 1 | map_machine02_02_01 | map_machine02_02_01 | map_machine02_02 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L65) | 3 | 0 | map_machine02_03_00 | map_machine02_03_00 | map_machine02_03 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L66) | 3 | 1 | map_machine02_03_01 | map_machine02_03_01 | map_machine02_03 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L67) | 4 | 0 | map_machine02_04_00 | map_machine02_04_00 | map_machine02_04 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L68) | 4 | 1 | map_machine02_04_01 | map_machine02_04_01 | map_machine02_04 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L69) | 5 | 0 | map_machine02_05_00 | map_machine02_05_00 | map_machine02_05 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L70) | 5 | 1 | map_machine02_05_01 | map_machine02_05_01 | map_machine02_05 |

## Qedit placement menus

Bundled and external definitions remain separate. The external BB list is monsv4/itemv4. Menu inclusion is editor evidence, not a runtime compatibility test.

### qedit-config

**mons:** 128 (Gillchic), 129 (Garanz), 130 (Sinow Blue), 131 (Canadine), 132 (Canane), 133 (Dubchic Switch)

**item:** 0, 1, 2, 3, 7, 8, 10, 11, 12, 13, 14, 18, 19, 24, 25, 27, 32, 33, 34, 35, 36, 37, 129, 130, 131, 132, 136, 139, 141, 142, 144, 145, 146, 147, 149, 207, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 304, 342, 359, 222, 150


### qedit-external

**monsv4:** 51 (Stage NPC's), 128 (Gillchic), 129 (Garanz), 130 (Sinow Blue), 131 (Canadine), 132 (Canane), 133 (Dubchic Switch)

**itemv4:** 0, 1, 4, 14, 2, 3, 27, 25, 697, 141, 142, 10, 11, 12, 13, 15, 7, 144, 8, 6, 40, 41, 18, 21, 696, 698, 136, 145, 146, 147, 19, 22, 23, 24, 130, 150, 131, 132, 256, 258, 257, 207, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 342, 149, 31, 34, 35, 32, 33, 222, 36, 139, 37, 38, 359


## Rooms, collision and coordinates

Room boundaries, transforms, empty-room IDs, valid walkable spawn positions and safe player spawn points have not yet been decoded for this layout family. This page is a general floor/resource reference, not a finished geometry atlas.

[Observed quest section index](../map-sections/README.md) can supply examples, but copying a room ID or coordinate requires verifying the exact layout.

[Documented monster constructor availability](../entity-database/areas.md) · [Qedit entity fields](../entity-database/qedit/entity-fields.md)


<!-- geometry-atlas:start -->
## Extracted map wireframes

[map_machine02_00](geometry/map_machine02_00.md) · [map_machine02_01](geometry/map_machine02_01.md) · [map_machine02_02](geometry/map_machine02_02.md) · [map_machine02_03](geometry/map_machine02_03.md) · [map_machine02_04](geometry/map_machine02_04.md) · [map_machine02_05](geometry/map_machine02_05.md)

Matching uses setup-resource filenames. Section reference positions and collision triangles are extracted; section boundary ownership and safe spawning remain unverified.
<!-- geometry-atlas:end -->
