# Episode 1: Cave 2

[General floor database](README.md)

| Identifier | Value |
|---|---|
| Default floor slot | 4 |
| Area ID | 4 / 0x04 |

A quest can designate an area into a different floor slot. These identifiers must not be treated as interchangeable.

## Available map-table entries

Layout and entity variation are separate indices. On = multiplayer; Off = solo; Ulti tables are the Ultimate-specific map tables. Entries reflect supplied client resources, not a quest’s chosen runtime configuration.

| Table | Layout | Entity variation | Object basename | Enemy/event basename | Setup basename |
|---|---:|---:|---|---|---|
| [SetDataTableOff](tables/SetDataTableOff.txt#L15) | 0 | 0 | map_cave02_00_00 | map_cave02_00_00_off | map_cave02_00 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L16) | 1 | 0 | map_cave02_01_00 | map_cave02_01_00_off | map_cave02_01 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L17) | 2 | 0 | map_cave02_02_00 | map_cave02_02_00_off | map_cave02_02 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L18) | 3 | 0 | map_cave02_03_00 | map_cave02_03_00_off | map_cave02_03 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L19) | 4 | 0 | map_cave02_04_00 | map_cave02_04_00_off | map_cave02_04 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L15) | 0 | 0 | map_cave02_00_00 | map_cave02_00_00_off | map_cave02_00 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L16) | 1 | 0 | map_cave02_01_00 | map_cave02_01_00_off | map_cave02_01 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L17) | 2 | 0 | map_cave02_02_00 | map_cave02_02_00_off | map_cave02_02 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L18) | 3 | 0 | map_cave02_03_00 | map_cave02_03_00_off | map_cave02_03 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L19) | 4 | 0 | map_cave02_04_00 | map_cave02_04_00_off | map_cave02_04 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L25) | 0 | 0 | map_cave02_00_00 | map_cave02_00_00 | map_cave02_00 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L26) | 0 | 1 | map_cave02_00_01 | map_cave02_00_01 | map_cave02_00 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L27) | 1 | 0 | map_cave02_01_00 | map_cave02_01_00 | map_cave02_01 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L28) | 1 | 1 | map_cave02_01_01 | map_cave02_01_01 | map_cave02_01 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L29) | 2 | 0 | map_cave02_02_00 | map_cave02_02_00 | map_cave02_02 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L30) | 2 | 1 | map_cave02_02_01 | map_cave02_02_01 | map_cave02_02 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L31) | 3 | 0 | map_cave02_03_00 | map_cave02_03_00 | map_cave02_03 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L32) | 3 | 1 | map_cave02_03_01 | map_cave02_03_01 | map_cave02_03 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L33) | 4 | 0 | map_cave02_04_00 | map_cave02_04_00_off | map_cave02_04 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L34) | 4 | 1 | map_cave02_04_01 | map_cave02_04_01_off | map_cave02_04 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L25) | 0 | 0 | map_cave02_00_00 | map_cave02_00_00 | map_cave02_00 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L26) | 0 | 1 | map_cave02_00_01 | map_cave02_00_01 | map_cave02_00 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L27) | 1 | 0 | map_cave02_01_00 | map_cave02_01_00 | map_cave02_01 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L28) | 1 | 1 | map_cave02_01_01 | map_cave02_01_01 | map_cave02_01 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L29) | 2 | 0 | map_cave02_02_00 | map_cave02_02_00 | map_cave02_02 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L30) | 2 | 1 | map_cave02_02_01 | map_cave02_02_01 | map_cave02_02 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L31) | 3 | 0 | map_cave02_03_00 | map_cave02_03_00 | map_cave02_03 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L32) | 3 | 1 | map_cave02_03_01 | map_cave02_03_01 | map_cave02_03 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L33) | 4 | 0 | map_cave02_04_00 | map_cave02_04_00_off | map_cave02_04 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L34) | 4 | 1 | map_cave02_04_01 | map_cave02_04_01_off | map_cave02_04 |

## Qedit placement menus

Bundled and external definitions remain separate. The external BB list is monsv4/itemv4. Menu inclusion is editor evidence, not a runtime compatibility test.

### qedit-config

**mons:** 97 (Poison Lily / Del Lily), 100 (Pofuilly Slime), 99 (evil shark), 98 (Nano Dragon), 101 (Pan Arms), 96 (Grass Asassin), 29 (Guild Lady)

**item:** 22, 0, 1, 2, 3, 7, 8, 10, 11, 12, 13, 14, 18, 19, 24, 25, 27, 32, 33, 34, 35, 36, 37, 129, 130, 131, 132, 136, 139, 140, 141, 142, 144, 145, 146, 147, 149, 150, 151, 192, 193, 194, 195, 199, 200, 201, 204, 205, 206, 207, 212, 213, 214, 215, 216, 217, 222, 224, 342


### qedit-external

**monsv4:** 51 (Stage NPC's), 96 (Grass Asassin), 97 (Poison Lily / Del Lily), 98 (Nano Dragon), 99 (evil shark), 100 (Pofuilly Slime)

**itemv4:** 0, 1, 4, 14, 7, 8, 6, 40, 41, 9, 20, 17, 2, 3, 27, 697, 141, 142, 10, 11, 12, 13, 15, 129, 192, 193, 194, 206, 195, 207, 23, 24, 196, 197, 198, 199, 200, 201, 203, 204, 205, 212, 213, 214, 215, 216, 217, 18, 21, 696, 698, 22, 130, 150, 131, 132, 136, 145, 146, 147, 19, 342, 149, 31, 34, 35, 222, 32, 33, 36, 224, 139, 37, 38


## Rooms, collision and coordinates

Room boundaries, transforms, empty-room IDs, valid walkable spawn positions and safe player spawn points have not yet been decoded for this layout family. This page is a general floor/resource reference, not a finished geometry atlas.

[Observed quest section index](../map-sections/README.md) can supply examples, but copying a room ID or coordinate requires verifying the exact layout.

[Documented monster constructor availability](../entity-database/areas.md) · [Qedit entity fields](../entity-database/qedit/entity-fields.md)
