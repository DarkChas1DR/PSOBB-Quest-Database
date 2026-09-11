# Episode 2: Control Tower

[General floor database](README.md)

| Identifier | Value |
|---|---|
| Default floor slot | 17 |
| Area ID | 35 / 0x23 |

A quest can designate an area into a different floor slot. These identifiers must not be treated as interchangeable.

## Available map-table entries

Layout and entity variation are separate indices. On = multiplayer; Off = solo; Ulti tables are the Ultimate-specific map tables. Entries reflect supplied client resources, not a quest’s chosen runtime configuration.

| Table | Layout | Entity variation | Object basename | Enemy/event basename | Setup basename |
|---|---:|---:|---|---|---|
| [SetDataTableOff](tables/SetDataTableOff.txt#L147) | 0 | 0 | map_jungle07_00_off | map_jungle07_00_off | map_jungle07 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L148) | 1 | 0 | map_jungle07_01_off | map_jungle07_01_off | map_jungle07 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L149) | 2 | 0 | map_jungle07_02_off | map_jungle07_02_off | map_jungle07 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L150) | 3 | 0 | map_jungle07_03_off | map_jungle07_03_off | map_jungle07 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L151) | 4 | 0 | map_jungle07_04_off | map_jungle07_04_off | map_jungle07 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L147) | 0 | 0 | map_jungle07_00_off | map_jungle07_00_off | map_jungle07 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L148) | 1 | 0 | map_jungle07_01_off | map_jungle07_01_off | map_jungle07 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L149) | 2 | 0 | map_jungle07_02_off | map_jungle07_02_off | map_jungle07 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L150) | 3 | 0 | map_jungle07_03_off | map_jungle07_03_off | map_jungle07 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L151) | 4 | 0 | map_jungle07_04_off | map_jungle07_04_off | map_jungle07 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L174) | 0 | 0 | map_jungle07_00 | map_jungle07_00 | map_jungle07 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L175) | 1 | 0 | map_jungle07_01 | map_jungle07_01 | map_jungle07 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L176) | 2 | 0 | map_jungle07_02 | map_jungle07_02 | map_jungle07 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L177) | 3 | 0 | map_jungle07_03 | map_jungle07_03 | map_jungle07 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L178) | 4 | 0 | map_jungle07_04 | map_jungle07_04 | map_jungle07 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L174) | 0 | 0 | map_jungle07_00 | map_jungle07_00 | map_jungle07 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L175) | 1 | 0 | map_jungle07_01 | map_jungle07_01 | map_jungle07 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L176) | 2 | 0 | map_jungle07_02 | map_jungle07_02 | map_jungle07 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L177) | 3 | 0 | map_jungle07_03 | map_jungle07_03 | map_jungle07 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L178) | 4 | 0 | map_jungle07_04 | map_jungle07_04 | map_jungle07 |

## Qedit placement menus

Bundled and external definitions remain separate. The external BB list is monsv4/itemv4. Menu inclusion is editor evidence, not a runtime compatibility test.

### qedit-config

**mons:** 97 (Poison Lily / Del Lily), 224 (Epsilon / Sinow Zoa), 217 (Gee), 218 (Gi Gue), 216 (Gibbles), 225 (Ill Gill), 214 (Mericarol), 213 (Merillias), 212 (Sinow Berill), 215 (Ul Gibbon), 223 (Reconbox), 220 (delbiter), 246 (Unknown 246)

**item:** 0, 1, 3, 4, 7, 8, 10, 11, 12, 13, 14, 18, 19, 24, 25, 34, 35, 36, 37, 39, 129, 130, 131, 132, 139, 144, 150, 151, 192, 222, 257, 359, 400, 403, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 527, 528, 531, 547, 458, 552, 553, 688, 697, 401, 261, 259, 696


### qedit-external

**monsv4:** 214 (Mericarol), 216 (Gibbles), 218 (Gi Gue), 223 (Reconbox), 220 (delbiter), 224 (Epsilon / Sinow Zoa), 97 (Poison Lily / Del Lily), 51 (Stage NPC's), 246 (Unknown 246), 225 (Ill Gill)

**itemv4:** 0, 4, 14, 40, 41, 7, 24, 1, 23, 20, 10, 11, 12, 13, 8, 18, 21, 696, 698, 22, 31, 34, 32, 33, 139, 37, 38, 512, 513, 514, 150, 19, 132, 144, 192, 515, 517, 522, 688, 524, 525, 553, 552, 526, 222, 3, 697, 25, 527, 528, 530, 35, 39, 36, 359, 261, 259, 207, 195, 401, 403, 547, 260


## Rooms, collision and coordinates

Room boundaries, transforms, empty-room IDs, valid walkable spawn positions and safe player spawn points have not yet been decoded for this layout family. This page is a general floor/resource reference, not a finished geometry atlas.

[Observed quest section index](../map-sections/README.md) can supply examples, but copying a room ID or coordinate requires verifying the exact layout.

[Documented monster constructor availability](../entity-database/areas.md) · [Qedit entity fields](../entity-database/qedit/entity-fields.md)
