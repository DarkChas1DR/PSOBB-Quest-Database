# Episode 1: Cave 1

[General floor database](README.md)

| Identifier | Value |
|---|---|
| Default floor slot | 3 |
| Area ID | 3 / 0x03 |

A quest can designate an area into a different floor slot. These identifiers must not be treated as interchangeable.

## Available map-table entries

Layout and entity variation are separate indices. On = multiplayer; Off = solo; Ulti tables are the Ultimate-specific map tables. Entries reflect supplied client resources, not a quest’s chosen runtime configuration.

| Table | Layout | Entity variation | Object basename | Enemy/event basename | Setup basename |
|---|---:|---:|---|---|---|
| [SetDataTableOff](tables/SetDataTableOff.txt#L9) | 0 | 0 | map_cave01_00_00 | map_cave01_00_00_off | map_cave01_00 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L10) | 1 | 0 | map_cave01_01_00 | map_cave01_01_00_off | map_cave01_01 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L11) | 2 | 0 | map_cave01_02_00 | map_cave01_02_00_off | map_cave01_02 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L12) | 3 | 0 | map_cave01_03_00 | map_cave01_03_00_off | map_cave01_03 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L13) | 4 | 0 | map_cave01_04_00 | map_cave01_04_00_off | map_cave01_04 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L14) | 5 | 0 | map_cave01_05_00 | map_cave01_05_00_off | map_cave01_05 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L9) | 0 | 0 | map_cave01_00_00 | map_cave01_00_00_off | map_cave01_00 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L10) | 1 | 0 | map_cave01_01_00 | map_cave01_01_00_off | map_cave01_01 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L11) | 2 | 0 | map_cave01_02_00 | map_cave01_02_00_off | map_cave01_02 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L12) | 3 | 0 | map_cave01_03_00 | map_cave01_03_00_off | map_cave01_03 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L13) | 4 | 0 | map_cave01_04_00 | map_cave01_04_00_off | map_cave01_04 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L14) | 5 | 0 | map_cave01_05_00 | map_cave01_05_00_off | map_cave01_05 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L13) | 0 | 0 | map_cave01_00_00 | map_cave01_00_00 | map_cave01_00 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L14) | 0 | 1 | map_cave01_00_01 | map_cave01_00_01 | map_cave01_00 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L15) | 1 | 0 | map_cave01_01_00 | map_cave01_01_00 | map_cave01_01 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L16) | 1 | 1 | map_cave01_01_01 | map_cave01_01_01 | map_cave01_01 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L17) | 2 | 0 | map_cave01_02_00 | map_cave01_02_00 | map_cave01_02 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L18) | 2 | 1 | map_cave01_02_01 | map_cave01_02_01 | map_cave01_02 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L19) | 3 | 0 | map_cave01_03_00 | map_cave01_03_00 | map_cave01_03 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L20) | 3 | 1 | map_cave01_03_01 | map_cave01_03_01 | map_cave01_03 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L21) | 4 | 0 | map_cave01_04_00 | map_cave01_04_00 | map_cave01_04 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L22) | 4 | 1 | map_cave01_04_01 | map_cave01_04_01 | map_cave01_04 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L23) | 5 | 0 | map_cave01_05_00 | map_cave01_05_00 | map_cave01_05 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L24) | 5 | 1 | map_cave01_05_01 | map_cave01_05_01 | map_cave01_05 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L13) | 0 | 0 | map_cave01_00_00 | map_cave01_00_00 | map_cave01_00 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L14) | 0 | 1 | map_cave01_00_01 | map_cave01_00_01 | map_cave01_00 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L15) | 1 | 0 | map_cave01_01_00 | map_cave01_01_00 | map_cave01_01 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L16) | 1 | 1 | map_cave01_01_01 | map_cave01_01_01 | map_cave01_01 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L17) | 2 | 0 | map_cave01_02_00 | map_cave01_02_00 | map_cave01_02 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L18) | 2 | 1 | map_cave01_02_01 | map_cave01_02_01 | map_cave01_02 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L19) | 3 | 0 | map_cave01_03_00 | map_cave01_03_00 | map_cave01_03 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L20) | 3 | 1 | map_cave01_03_01 | map_cave01_03_01 | map_cave01_03 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L21) | 4 | 0 | map_cave01_04_00 | map_cave01_04_00 | map_cave01_04 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L22) | 4 | 1 | map_cave01_04_01 | map_cave01_04_01 | map_cave01_04 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L23) | 5 | 0 | map_cave01_05_00 | map_cave01_05_00 | map_cave01_05 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L24) | 5 | 1 | map_cave01_05_01 | map_cave01_05_01 | map_cave01_05 |

## Qedit placement menus

Bundled and external definitions remain separate. The external BB list is monsv4/itemv4. Menu inclusion is editor evidence, not a runtime compatibility test.

### qedit-config

**mons:** 97 (Poison Lily / Del Lily), 100 (Pofuilly Slime), 99 (evil shark), 98 (Nano Dragon), 101 (Pan Arms), 96 (Grass Asassin), 29 (Guild Lady)

**item:** 22, 0, 1, 2, 3, 7, 8, 10, 11, 12, 13, 14, 18, 19, 24, 25, 27, 32, 33, 34, 35, 36, 37, 129, 130, 131, 132, 136, 139, 140, 141, 142, 144, 145, 146, 147, 149, 150, 151, 192, 193, 194, 195, 196, 197, 198, 206, 207, 209, 210, 211, 222, 223, 257


### qedit-external

**monsv4:** 51 (Stage NPC's), 96 (Grass Asassin), 97 (Poison Lily / Del Lily), 98 (Nano Dragon), 99 (evil shark), 101 (Pan Arms)

**itemv4:** 0, 1, 4, 14, 7, 8, 6, 9, 20, 17, 2, 3, 27, 697, 141, 10, 11, 12, 13, 129, 18, 21, 696, 698, 22, 23, 24, 192, 193, 194, 206, 195, 207, 209, 210, 211, 130, 150, 131, 132, 136, 145, 146, 147, 19, 149, 31, 32, 33, 34, 35, 140, 222, 36, 223, 139, 37, 38


## Rooms, collision and coordinates

Room boundaries, transforms, empty-room IDs, valid walkable spawn positions and safe player spawn points have not yet been decoded for this layout family. This page is a general floor/resource reference, not a finished geometry atlas.

[Observed quest section index](../map-sections/README.md) can supply examples, but copying a room ID or coordinate requires verifying the exact layout.

[Documented monster constructor availability](../entity-database/areas.md) · [Qedit entity fields](../entity-database/qedit/entity-fields.md)


<!-- geometry-atlas:start -->
## Extracted map wireframes

[map_cave01_00](geometry/map_cave01_00.md) · [map_cave01_01](geometry/map_cave01_01.md) · [map_cave01_02](geometry/map_cave01_02.md) · [map_cave01_03](geometry/map_cave01_03.md) · [map_cave01_04](geometry/map_cave01_04.md) · [map_cave01_05](geometry/map_cave01_05.md)

Matching uses setup-resource filenames. Section reference positions and collision triangles are extracted; section boundary ownership and safe spawning remain unverified.
<!-- geometry-atlas:end -->
