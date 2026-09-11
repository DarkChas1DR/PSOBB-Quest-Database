# Episode 2: Seabed Upper Levels

[General floor database](README.md)

| Identifier | Value |
|---|---|
| Default floor slot | 10 |
| Area ID | 28 / 0x1C |

A quest can designate an area into a different floor slot. These identifiers must not be treated as interchangeable.

## Available map-table entries

Layout and entity variation are separate indices. On = multiplayer; Off = solo; Ulti tables are the Ultimate-specific map tables. Entries reflect supplied client resources, not a quest’s chosen runtime configuration.

| Table | Layout | Entity variation | Object basename | Enemy/event basename | Setup basename |
|---|---:|---:|---|---|---|
| [SetDataTableOff](tables/SetDataTableOff.txt#L136) | 0 | 0 | map_seabed01_00_00_off | map_seabed01_00_00_off | map_seabed01_00 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L137) | 1 | 0 | map_seabed01_01_00_off | map_seabed01_01_00_off | map_seabed01_01 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L138) | 2 | 0 | map_seabed01_02_00_off | map_seabed01_02_00_off | map_seabed01_02 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L136) | 0 | 0 | map_seabed01_00_00_off | map_seabed01_00_00_off | map_seabed01_00 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L137) | 1 | 0 | map_seabed01_01_00_off | map_seabed01_01_00_off | map_seabed01_01 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L138) | 2 | 0 | map_seabed01_02_00_off | map_seabed01_02_00_off | map_seabed01_02 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L157) | 0 | 0 | map_seabed01_00_00 | map_seabed01_00_00 | map_seabed01_00 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L158) | 0 | 1 | map_seabed01_00_01 | map_seabed01_00_01 | map_seabed01_00 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L159) | 1 | 0 | map_seabed01_01_00 | map_seabed01_01_00 | map_seabed01_01 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L160) | 1 | 1 | map_seabed01_01_01 | map_seabed01_01_01 | map_seabed01_01 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L161) | 2 | 0 | map_seabed01_02_00 | map_seabed01_02_00 | map_seabed01_02 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L162) | 2 | 1 | map_seabed01_02_01 | map_seabed01_02_01 | map_seabed01_02 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L157) | 0 | 0 | map_seabed01_00_00 | map_seabed01_00_00 | map_seabed01_00 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L158) | 0 | 1 | map_seabed01_00_01 | map_seabed01_00_01 | map_seabed01_00 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L159) | 1 | 0 | map_seabed01_01_00 | map_seabed01_01_00 | map_seabed01_01 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L160) | 1 | 1 | map_seabed01_01_01 | map_seabed01_01_01 | map_seabed01_01 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L161) | 2 | 0 | map_seabed01_02_00 | map_seabed01_02_00 | map_seabed01_02 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L162) | 2 | 1 | map_seabed01_02_01 | map_seabed01_02_01 | map_seabed01_02 |

## Qedit placement menus

Bundled and external definitions remain separate. The external BB list is monsv4/itemv4. Menu inclusion is editor evidence, not a runtime compatibility test.

### qedit-config

**mons:** 51 (Stage NPC's), 220 (delbiter), 219 (deldepth), 221 (dolmdarl), 222 (morfos), 223 (Reconbox), 224 (Epsilon / Sinow Zoa)

**item:** 0, 1, 3, 4, 7, 8, 10, 11, 12, 13, 14, 18, 19, 24, 25, 34, 35, 36, 37, 39, 129, 130, 131, 132, 139, 144, 150, 151, 192, 222, 257, 359, 400, 403, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 527, 528, 531, 545, 546, 547, 458, 552, 553, 688, 697, 136, 548, 146, 548, 549, 550, 136, 696, 146, 352, 145


### qedit-external

**monsv4:** 221 (dolmdarl), 222 (morfos), 223 (Reconbox), 224 (Epsilon / Sinow Zoa), 219 (deldepth), 220 (delbiter), 51 (Stage NPC's), 244 (Leo)

**itemv4:** 0, 4, 14, 6, 40, 41, 7, 24, 1, 23, 20, 10, 11, 12, 13, 8, 18, 21, 696, 698, 22, 31, 34, 32, 33, 139, 37, 38, 544, 545, 546, 513, 547, 548, 549, 550, 136, 145, 146, 147, 359, 551, 150, 131, 19, 132, 144, 192, 222, 3, 25, 697, 552, 553, 527, 528, 35, 204, 39, 352, 36


## Rooms, collision and coordinates

Room boundaries, transforms, empty-room IDs, valid walkable spawn positions and safe player spawn points have not yet been decoded for this layout family. This page is a general floor/resource reference, not a finished geometry atlas.

[Observed quest section index](../map-sections/README.md) can supply examples, but copying a room ID or coordinate requires verifying the exact layout.

[Documented monster constructor availability](../entity-database/areas.md) · [Qedit entity fields](../entity-database/qedit/entity-fields.md)


<!-- geometry-atlas:start -->
## Extracted map wireframes

[map_seabed01_00](geometry/map_seabed01_00.md) · [map_seabed01_01](geometry/map_seabed01_01.md) · [map_seabed01_02](geometry/map_seabed01_02.md)

Matching uses setup-resource filenames. Section reference positions and collision triangles are extracted; section boundary ownership and safe spawning remain unverified.
<!-- geometry-atlas:end -->
