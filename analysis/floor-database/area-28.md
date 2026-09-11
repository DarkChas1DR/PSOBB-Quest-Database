# Episode 4: Crater Interior

[General floor database](README.md)

| Identifier | Value |
|---|---|
| Default floor slot | 5 |
| Area ID | 40 / 0x28 |

A quest can designate an area into a different floor slot. These identifiers must not be treated as interchangeable.

## Available map-table entries

Layout and entity variation are separate indices. On = multiplayer; Off = solo; Ulti tables are the Ultimate-specific map tables. Entries reflect supplied client resources, not a quest’s chosen runtime configuration.

| Table | Layout | Entity variation | Object basename | Enemy/event basename | Setup basename |
|---|---:|---:|---|---|---|
| [SetDataTableOff](tables/SetDataTableOff.txt#L164) | 0 | 0 | map_crater01_00_00 | map_crater01_00_00 | map_crater01_00 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L165) | 0 | 1 | map_crater01_00_01 | map_crater01_00_01 | map_crater01_00 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L166) | 0 | 2 | map_crater01_00_02 | map_crater01_00_02 | map_crater01_00 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L191) | 0 | 0 | map_crater01_00_00 | map_crater01_00_00 | map_crater01_00 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L192) | 0 | 1 | map_crater01_00_01 | map_crater01_00_01 | map_crater01_00 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L193) | 0 | 2 | map_crater01_00_02 | map_crater01_00_02 | map_crater01_00 |

## Qedit placement menus

Bundled and external definitions remain separate. The external BB list is monsv4/itemv4. Menu inclusion is editor evidence, not a runtime compatibility test.

### qedit-config

**mons:** 277 (Boota), 273 (Saterlite Lizard), 278 (Dorphon), 272 (astark), 276 (Zu), 65 (Rag Rappy / Sand Rappy), 69 (Rappy NPC), 25 (Blue Soldier), 280 (Rupika), 243 (Default Ramarl (Karen)), 244 (Leo)

**item:** 0, 129, 130, 136, 515, 2, 3, 8, 10, 132, 129, 770, 19, 11, 769, 902, 139, 18, 131, 424, 7, 771, 35, 14, 211, 150, 257, 192, 144, 145, 22, 27


### qedit-external

**monsv4:** 272 (astark), 273 (Saterlite Lizard), 277 (Boota), 276 (Zu), 278 (Dorphon), 65 (Rag Rappy / Sand Rappy), 243 (Default Ramarl (Karen)), 244 (Leo), 25 (Blue Soldier), 280 (Rupika), 69 (Rappy NPC)

**itemv4:** 0, 4, 14, 6, 40, 41, 7, 24, 1, 23, 2, 3, 25, 697, 10, 11, 12, 13, 8, 18, 21, 696, 698, 22, 150, 130, 131, 132, 129, 144, 192, 257, 31, 34, 35, 32, 33, 139, 222, 37, 38, 136, 145, 515, 147, 149, 19, 39, 352, 142, 211, 334, 335, 512, 30, 424, 201, 769, 770, 771, 902, 768


## Rooms, collision and coordinates

Room boundaries, transforms, empty-room IDs, valid walkable spawn positions and safe player spawn points have not yet been decoded for this layout family. This page is a general floor/resource reference, not a finished geometry atlas.

[Observed quest section index](../map-sections/README.md) can supply examples, but copying a room ID or coordinate requires verifying the exact layout.

[Documented monster constructor availability](../entity-database/areas.md) · [Qedit entity fields](../entity-database/qedit/entity-fields.md)


<!-- geometry-atlas:start -->
## Extracted map wireframes

[map_crater01_00](geometry/map_crater01_00.md)

Matching uses setup-resource filenames. Section reference positions and collision triangles are extracted; section boundary ownership and safe spawning remain unverified.
<!-- geometry-atlas:end -->
