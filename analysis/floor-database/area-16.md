# Episode 2: VR Spaceship Beta

[General floor database](README.md)

| Identifier | Value |
|---|---|
| Default floor slot | 4 |
| Area ID | 22 / 0x16 |

A quest can designate an area into a different floor slot. These identifiers must not be treated as interchangeable.

## Available map-table entries

Layout and entity variation are separate indices. On = multiplayer; Off = solo; Ulti tables are the Ultimate-specific map tables. Entries reflect supplied client resources, not a quest’s chosen runtime configuration.

| Table | Layout | Entity variation | Object basename | Enemy/event basename | Setup basename |
|---|---:|---:|---|---|---|
| [SetDataTableOff](tables/SetDataTableOff.txt#L115) | 0 | 0 | map_space02_00_00_off | map_space02_00_00_off | map_space02_00 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L116) | 1 | 0 | map_space02_01_00_off | map_space02_01_00_off | map_space02_01 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L117) | 2 | 0 | map_space02_02_00_off | map_space02_02_00_off | map_space02_02 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L115) | 0 | 0 | map_space02_00_00_off | map_space02_00_00_off | map_space02_00 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L116) | 1 | 0 | map_space02_01_00_off | map_space02_01_00_off | map_space02_01 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L117) | 2 | 0 | map_space02_02_00_off | map_space02_02_00_off | map_space02_02 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L136) | 0 | 0 | map_space02_00_00 | map_space02_00_00 | map_space02_00 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L137) | 1 | 0 | map_space02_01_00 | map_space02_01_00 | map_space02_01 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L138) | 2 | 0 | map_space02_02_00 | map_space02_02_00 | map_space02_02 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L136) | 0 | 0 | map_space02_00_00 | map_space02_00_00 | map_space02_00 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L137) | 1 | 0 | map_space02_01_00 | map_space02_01_00 | map_space02_01 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L138) | 2 | 0 | map_space02_02_00 | map_space02_02_00 | map_space02_02 |

## Qedit placement menus

Bundled and external definitions remain separate. The external BB list is monsv4/itemv4. Menu inclusion is editor evidence, not a runtime compatibility test.

### qedit-config

**mons:** 51 (Stage NPC's), 67 (Savage Wolf), 160 (Delsaber), 161 (Chaos Sorcerer), 128 (Gillchic), 133 (Dubchic Switch), 129 (Garanz), 101 (Pan Arms)

**item:** 0, 1, 2, 3, 4, 7, 8, 10, 11, 12, 13, 14, 18, 19, 24, 25, 27, 34, 35, 36, 37, 39, 131, 222, 339, 352, 353, 354, 355, 356, 357, 359, 400, 401, 402, 403, 448, 553, 139, 144, 696, 195, 150, 132, 129, 257


### qedit-external

**monsv4:** 133 (Dubchic Switch), 128 (Gillchic), 67 (Savage Wolf), 101 (Pan Arms), 160 (Delsaber), 161 (Chaos Sorcerer), 51 (Stage NPC's)

**itemv4:** 0, 4, 14, 6, 40, 41, 7, 24, 1, 23, 2, 3, 25, 697, 10, 11, 12, 13, 8, 18, 21, 696, 698, 22, 150, 131, 132, 129, 144, 192, 257, 31, 34, 35, 32, 33, 139, 222, 37, 38, 402, 353, 354, 355, 356, 357, 368, 400, 401, 403, 205, 195, 359, 339, 448, 19, 553, 39, 352


## Rooms, collision and coordinates

Room boundaries, transforms, empty-room IDs, valid walkable spawn positions and safe player spawn points have not yet been decoded for this layout family. This page is a general floor/resource reference, not a finished geometry atlas.

[Observed quest section index](../map-sections/README.md) can supply examples, but copying a room ID or coordinate requires verifying the exact layout.

[Documented monster constructor availability](../entity-database/areas.md) · [Qedit entity fields](../entity-database/qedit/entity-fields.md)


<!-- geometry-atlas:start -->
## Extracted map wireframes

[map_space02_00](geometry/map_space02_00.md) · [map_space02_01](geometry/map_space02_01.md) · [map_space02_02](geometry/map_space02_02.md)

Matching uses setup-resource filenames. Section reference positions and collision triangles are extracted; section boundary ownership and safe spawning remain unverified.
<!-- geometry-atlas:end -->
