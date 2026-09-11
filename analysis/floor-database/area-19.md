# Episode 2: Jungle Area East

[General floor database](README.md)

| Identifier | Value |
|---|---|
| Default floor slot | 7 |
| Area ID | 25 / 0x19 |

A quest can designate an area into a different floor slot. These identifiers must not be treated as interchangeable.

## Available map-table entries

Layout and entity variation are separate indices. On = multiplayer; Off = solo; Ulti tables are the Ultimate-specific map tables. Entries reflect supplied client resources, not a quest’s chosen runtime configuration.

| Table | Layout | Entity variation | Object basename | Enemy/event basename | Setup basename |
|---|---:|---:|---|---|---|
| [SetDataTableOff](tables/SetDataTableOff.txt#L124) | 0 | 0 | map_jungle03_00_off | map_jungle03_00_off | map_jungle03 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L125) | 0 | 1 | map_jungle03_01_off | map_jungle03_01_off | map_jungle03 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L126) | 0 | 2 | map_jungle03_02_off | map_jungle03_02_off | map_jungle03 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L124) | 0 | 0 | map_jungle03_00_off | map_jungle03_00_off | map_jungle03 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L125) | 0 | 1 | map_jungle03_01_off | map_jungle03_01_off | map_jungle03 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L126) | 0 | 2 | map_jungle03_02_off | map_jungle03_02_off | map_jungle03 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L145) | 0 | 0 | map_jungle03_00 | map_jungle03_00 | map_jungle03 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L146) | 0 | 1 | map_jungle03_01 | map_jungle03_01 | map_jungle03 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L147) | 0 | 2 | map_jungle03_02 | map_jungle03_02 | map_jungle03 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L145) | 0 | 0 | map_jungle03_00 | map_jungle03_00 | map_jungle03 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L146) | 0 | 1 | map_jungle03_01 | map_jungle03_01 | map_jungle03 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L147) | 0 | 2 | map_jungle03_02 | map_jungle03_02 | map_jungle03 |

## Qedit placement menus

Bundled and external definitions remain separate. The external BB list is monsv4/itemv4. Menu inclusion is editor evidence, not a runtime compatibility test.

### qedit-config

**mons:** 97 (Poison Lily / Del Lily), 224 (Epsilon / Sinow Zoa), 217 (Gee), 218 (Gi Gue), 216 (Gibbles), 225 (Ill Gill), 214 (Mericarol), 213 (Merillias), 212 (Sinow Berill), 215 (Ul Gibbon), 51 (Stage NPC's), 69 (Rappy NPC), 253 (Ep 2 Hunters Guild)

**item:** 0, 1, 3, 4, 7, 8, 10, 11, 12, 13, 14, 18, 19, 24, 25, 34, 35, 36, 37, 39, 129, 130, 131, 132, 139, 144, 150, 151, 192, 222, 257, 359, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 527, 528, 531, 552, 553, 688, 139, 144, 696, 195, 150, 132, 129, 133, 525, 529, 530, 698, 522


### qedit-external

**monsv4:** 212 (Sinow Berill), 213 (Merillias), 214 (Mericarol), 215 (Ul Gibbon), 216 (Gibbles), 217 (Gee), 218 (Gi Gue), 246 (Unknown 246), 253 (Ep 2 Hunters Guild), 69 (Rappy NPC), 51 (Stage NPC's)

**itemv4:** 0, 4, 14, 6, 40, 41, 7, 24, 1, 23, 20, 10, 11, 12, 13, 8, 18, 21, 696, 698, 22, 31, 34, 32, 33, 139, 37, 38, 133, 512, 513, 514, 150, 131, 19, 132, 144, 192, 515, 517, 518, 519, 520, 521, 522, 338, 688, 524, 525, 553, 552, 526, 222, 3, 25, 697, 527, 528, 529, 530, 531, 35, 39, 36, 359


## Rooms, collision and coordinates

Room boundaries, transforms, empty-room IDs, valid walkable spawn positions and safe player spawn points have not yet been decoded for this layout family. This page is a general floor/resource reference, not a finished geometry atlas.

[Observed quest section index](../map-sections/README.md) can supply examples, but copying a room ID or coordinate requires verifying the exact layout.

[Documented monster constructor availability](../entity-database/areas.md) · [Qedit entity fields](../entity-database/qedit/entity-fields.md)


<!-- geometry-atlas:start -->
## Extracted map wireframes

[map_jungle03_00](geometry/map_jungle03_00.md)

Matching uses setup-resource filenames. Section reference positions and collision triangles are extracted; section boundary ownership and safe spawning remain unverified.
<!-- geometry-atlas:end -->
