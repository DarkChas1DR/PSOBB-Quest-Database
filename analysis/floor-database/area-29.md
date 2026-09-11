# Episode 4: Subterranean Desert 1

[General floor database](README.md)

| Identifier | Value |
|---|---|
| Default floor slot | 6 |
| Area ID | 41 / 0x29 |

A quest can designate an area into a different floor slot. These identifiers must not be treated as interchangeable.

## Available map-table entries

Layout and entity variation are separate indices. On = multiplayer; Off = solo; Ulti tables are the Ultimate-specific map tables. Entries reflect supplied client resources, not a quest’s chosen runtime configuration.

| Table | Layout | Entity variation | Object basename | Enemy/event basename | Setup basename |
|---|---:|---:|---|---|---|
| [SetDataTableOff](tables/SetDataTableOff.txt#L167) | 0 | 0 | map_desert01_00_00 | map_desert01_00_00 | map_desert01_00 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L168) | 1 | 0 | map_desert01_01_00 | map_desert01_01_00 | map_desert01_01 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L169) | 2 | 0 | map_desert01_02_00 | map_desert01_02_00 | map_desert01_02 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L194) | 0 | 0 | map_desert01_00_00 | map_desert01_00_00 | map_desert01_00 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L195) | 1 | 0 | map_desert01_01_00 | map_desert01_01_00 | map_desert01_01 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L196) | 2 | 0 | map_desert01_02_00 | map_desert01_02_00 | map_desert01_02 |

## Qedit placement menus

Bundled and external definitions remain separate. The external BB list is monsv4/itemv4. Menu inclusion is editor evidence, not a runtime compatibility test.

### qedit-config

**mons:** 65 (Rag Rappy / Sand Rappy), 275 (Girt), 279 (Goran), 274 (Merissa A), 276 (Zu), 273 (Saterlite Lizard), 69 (Rappy NPC), 25 (Blue Soldier), 280 (Rupika), 243 (Default Ramarl (Karen)), 244 (Leo), 41 (Default Fomewearl (Rupika))

**item:** 258, 2, 0, 8, 899, 908, 24, 192, 352, 909, 907, 911, 3, 770, 136, 19, 146, 913, 11, 130, 144, 10, 902, 211, 18, 139, 131, 257, 142, 896, 338, 910, 205, 134, 901, 769, 27, 335, 334, 210, 209, 131, 688, 521, 7, 14, 771


### qedit-external

**monsv4:** 273 (Saterlite Lizard), 274 (Merissa A), 275 (Girt), 276 (Zu), 279 (Goran), 65 (Rag Rappy / Sand Rappy), 243 (Default Ramarl (Karen)), 244 (Leo), 25 (Blue Soldier), 280 (Rupika), 69 (Rappy NPC)

**itemv4:** 0, 4, 14, 6, 40, 41, 7, 24, 1, 23, 2, 3, 25, 697, 10, 11, 12, 13, 8, 18, 21, 696, 698, 22, 150, 130, 131, 132, 129, 144, 192, 257, 31, 34, 35, 32, 33, 139, 222, 37, 38, 258, 136, 145, 146, 147, 149, 19, 39, 352, 142, 211, 334, 335, 902, 907, 909, 911, 913, 133, 134, 205, 338, 524, 529, 531, 688, 769, 770, 771, 896, 897, 898, 899, 901, 903, 904, 908, 912, 768


## Rooms, collision and coordinates

Room boundaries, transforms, empty-room IDs, valid walkable spawn positions and safe player spawn points have not yet been decoded for this layout family. This page is a general floor/resource reference, not a finished geometry atlas.

[Observed quest section index](../map-sections/README.md) can supply examples, but copying a room ID or coordinate requires verifying the exact layout.

[Documented monster constructor availability](../entity-database/areas.md) · [Qedit entity fields](../entity-database/qedit/entity-fields.md)
