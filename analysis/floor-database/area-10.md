# Episode 1: Spaceship

[General floor database](README.md)

| Identifier | Value |
|---|---|
| Default floor slot | 16 |
| Area ID | 16 / 0x10 |

A quest can designate an area into a different floor slot. These identifiers must not be treated as interchangeable.

## Available map-table entries

Layout and entity variation are separate indices. On = multiplayer; Off = solo; Ulti tables are the Ultimate-specific map tables. Entries reflect supplied client resources, not a quest’s chosen runtime configuration.

| Table | Layout | Entity variation | Object basename | Enemy/event basename | Setup basename |
|---|---:|---:|---|---|---|
| [SetDataTableOff](tables/SetDataTableOff.txt#L99) | 0 | 0 | map_vs01_00 | map_vs01_00 | map_vs01_00 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L100) | 1 | 0 | map_vs01_01 | map_vs01_01 | map_vs01_01 |
| [SetDataTableOff](tables/SetDataTableOff.txt#L101) | 2 | 0 | map_vs01_02 | map_vs01_02 | map_vs01_02 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L99) | 0 | 0 | map_vs01_00 | map_vs01_00 | map_vs01_00 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L100) | 1 | 0 | map_vs01_01 | map_vs01_01 | map_vs01_01 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L101) | 2 | 0 | map_vs01_02 | map_vs01_02 | map_vs01_02 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L120) | 0 | 0 | map_vs01_00 | map_vs01_00 | map_vs01_00 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L121) | 1 | 0 | map_vs01_01 | map_vs01_01 | map_vs01_01 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L122) | 2 | 0 | map_vs01_02 | map_vs01_02 | map_vs01_02 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L120) | 0 | 0 | map_vs01_00 | map_vs01_00 | map_vs01_00 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L121) | 1 | 0 | map_vs01_01 | map_vs01_01 | map_vs01_01 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L122) | 2 | 0 | map_vs01_02 | map_vs01_02 | map_vs01_02 |

## Qedit placement menus

Bundled and external definitions remain separate. The external BB list is monsv4/itemv4. Menu inclusion is editor evidence, not a runtime compatibility test.

### qedit-config

**mons:** Empty list

**item:** 0, 1, 2, 3, 4, 7, 8, 10, 11, 12, 13, 14, 18, 19, 24, 25, 27, 34, 35, 36, 37, 39, 130, 132, 144, 150, 192, 222, 339, 352, 353, 354, 355, 356, 357, 359, 400, 401, 402, 403, 448, 553


### qedit-external

**monsv4:** 64 (Hildebear), 99 (evil shark), 96 (Grass Asassin), 130 (Sinow Blue), 160 (Delsaber), 164 (Chaos Bringer), 51 (Stage NPC's)

**itemv4:** 0, 4, 6, 40, 41, 7, 1, 368, 400, 401, 403, 402, 20, 353, 354, 355, 356, 10, 11, 12, 13, 8, 130, 150, 131, 132, 3, 697, 144, 192, 257, 205, 31, 34, 35, 32, 33, 357, 222, 36, 139, 37, 38


## Rooms, collision and coordinates

Room boundaries, transforms, empty-room IDs, valid walkable spawn positions and safe player spawn points have not yet been decoded for this layout family. This page is a general floor/resource reference, not a finished geometry atlas.

[Observed quest section index](../map-sections/README.md) can supply examples, but copying a room ID or coordinate requires verifying the exact layout.

[Documented monster constructor availability](../entity-database/areas.md) · [Qedit entity fields](../entity-database/qedit/entity-fields.md)
