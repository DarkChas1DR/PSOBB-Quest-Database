# Episode 4: Crater (Eastern Route)

[General floor database](README.md)

| Identifier | Value |
|---|---|
| Default floor slot | 1 |
| Area ID | 36 / 0x24 |

A quest can designate an area into a different floor slot. These identifiers must not be treated as interchangeable.

## Available map-table entries

Layout and entity variation are separate indices. On = multiplayer; Off = solo; Ulti tables are the Ultimate-specific map tables. Entries reflect supplied client resources, not a quest’s chosen runtime configuration.

| Table | Layout | Entity variation | Object basename | Enemy/event basename | Setup basename |
|---|---:|---:|---|---|---|
| [SetDataTableOff](tables/SetDataTableOff.txt#L152) | 0 | 0 | map_wilds01_00_00 | map_wilds01_00_00 | map_wilds01_00 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L153) | 0 | 1 | map_wilds01_00_01 | map_wilds01_00_01 | map_wilds01_00 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L154) | 0 | 2 | map_wilds01_00_02 | map_wilds01_00_02 | map_wilds01_00 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L179) | 0 | 0 | map_wilds01_00_00 | map_wilds01_00_00 | map_wilds01_00 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L180) | 0 | 1 | map_wilds01_00_01 | map_wilds01_00_01 | map_wilds01_00 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L181) | 0 | 2 | map_wilds01_00_02 | map_wilds01_00_02 | map_wilds01_00 |

## Qedit placement menus

Bundled and external definitions remain separate. The external BB list is monsv4/itemv4. Menu inclusion is editor evidence, not a runtime compatibility test.

### qedit-config

**mons:** 277 (Boota), 273 (Saterlite Lizard), 278 (Dorphon), 272 (astark), 276 (Zu), 65 (Rag Rappy / Sand Rappy), 69 (Rappy NPC), 25 (Blue Soldier), 280 (Rupika), 243 (Default Ramarl (Karen)), 244 (Leo)

**item:** 0, 130, 136, 515, 2, 3, 8, 10, 132, 129, 770, 19, 11, 769, 902, 139, 18, 131, 424, 7, 771, 35, 14, 211, 150, 257, 192, 144, 145, 22, 27


### qedit-external

**monsv4:** 272 (astark), 273 (Saterlite Lizard), 277 (Boota), 276 (Zu), 278 (Dorphon), 65 (Rag Rappy / Sand Rappy), 243 (Default Ramarl (Karen)), 244 (Leo), 25 (Blue Soldier), 211 (Unknown 211), 280 (Rupika), 69 (Rappy NPC)

**itemv4:** 0, 10, 11, 12, 13, 2, 3, 6, 8, 14, 24, 30, 40, 130, 131, 424, 768, 769, 770, 771, 35, 19, 132, 18, 136, 146, 902, 39, 139, 37, 211, 334, 335, 515, 4, 41, 7, 1, 23, 697, 21, 696, 698, 22, 150, 129, 144, 192, 257, 31, 34, 32, 33, 222, 38, 145, 147, 149, 352, 142


## Rooms, collision and coordinates

Room boundaries, transforms, empty-room IDs, valid walkable spawn positions and safe player spawn points have not yet been decoded for this layout family. This page is a general floor/resource reference, not a finished geometry atlas.

[Observed quest section index](../map-sections/README.md) can supply examples, but copying a room ID or coordinate requires verifying the exact layout.

[Documented monster constructor availability](../entity-database/areas.md) · [Qedit entity fields](../entity-database/qedit/entity-fields.md)
