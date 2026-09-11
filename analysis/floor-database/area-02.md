# Episode 1: Forest 2

[General floor database](README.md)

| Identifier | Value |
|---|---|
| Default floor slot | 2 |
| Area ID | 2 / 0x02 |

A quest can designate an area into a different floor slot. These identifiers must not be treated as interchangeable.

## Available map-table entries

Layout and entity variation are separate indices. On = multiplayer; Off = solo; Ulti tables are the Ultimate-specific map tables. Entries reflect supplied client resources, not a quest’s chosen runtime configuration.

| Table | Layout | Entity variation | Object basename | Enemy/event basename | Setup basename |
|---|---:|---:|---|---|---|
| [SetDataTableOff](tables/SetDataTableOff.txt#L6) | 0 | 0 | map_forest02_00 | map_forest02_00_off | map_forest02 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L7) | 0 | 1 | map_forest02_03 | map_forest02_03_off | map_forest02 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L8) | 0 | 2 | map_forest02_04 | map_forest02_04_off | map_forest02 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L6) | 0 | 0 | map_forest02_00 | map_forest02_00_off | map_forest02 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L7) | 0 | 1 | map_forest02_03 | map_forest02_03_off | map_forest02 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L8) | 0 | 2 | map_forest02_04 | map_forest02_04_off | map_forest02 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L8) | 0 | 0 | map_forest02_00 | map_forest02_00 | map_forest02 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L9) | 0 | 1 | map_forest02_01 | map_forest02_01 | map_forest02 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L10) | 0 | 2 | map_forest02_02 | map_forest02_02 | map_forest02 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L11) | 0 | 3 | map_forest02_03 | map_forest02_03 | map_forest02 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L12) | 0 | 4 | map_forest02_04 | map_forest02_04 | map_forest02 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L8) | 0 | 0 | map_forest02_00 | map_forest02_00 | map_forest02 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L9) | 0 | 1 | map_forest02_01 | map_forest02_01 | map_forest02 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L10) | 0 | 2 | map_forest02_02 | map_forest02_02 | map_forest02 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L11) | 0 | 3 | map_forest02_03 | map_forest02_03 | map_forest02 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L12) | 0 | 4 | map_forest02_04 | map_forest02_04 | map_forest02 |

## Qedit placement menus

Bundled and external definitions remain separate. The external BB list is monsv4/itemv4. Menu inclusion is editor evidence, not a runtime compatibility test.

### qedit-config

**mons:** 68 (Booma), 67 (Savage Wolf), 66 (Monest), 65 (Rag Rappy / Sand Rappy), 64 (Hildebear), 69 (Rappy NPC), 70 (Small hildebear NPC), 51 (Stage NPC's)

**item:** 0, 1, 2, 3, 7, 8, 10, 11, 12, 13, 14, 18, 19, 24, 25, 27, 32, 33, 34, 35, 36, 37, 128, 129, 130, 131, 132, 134, 135, 136, 137, 139, 140, 141, 142, 143, 144, 145, 146, 147, 149, 150, 151, 222, 257, 342, 22


### qedit-external

**monsv4:** 51 (Stage NPC's), 64 (Hildebear), 65 (Rag Rappy / Sand Rappy), 66 (Monest), 67 (Savage Wolf), 68 (Booma), 69 (Rappy NPC), 70 (Small hildebear NPC)

**itemv4:** 0, 1, 6, 40, 41, 10, 11, 12, 13, 15, 7, 14, 8, 17, 18, 21, 696, 698, 9, 20, 22, 23, 24, 30, 128, 129, 130, 150, 131, 132, 133, 134, 135, 136, 145, 146, 147, 137, 139, 140, 2, 3, 27, 25, 697, 4, 141, 142, 143, 144, 19, 342, 149, 31, 34, 35, 32, 33, 36, 257, 222, 37, 38


## Rooms, collision and coordinates

Room boundaries, transforms, empty-room IDs, valid walkable spawn positions and safe player spawn points have not yet been decoded for this layout family. This page is a general floor/resource reference, not a finished geometry atlas.

[Observed quest section index](../map-sections/README.md) can supply examples, but copying a room ID or coordinate requires verifying the exact layout.

[Documented monster constructor availability](../entity-database/areas.md) · [Qedit entity fields](../entity-database/qedit/entity-fields.md)
