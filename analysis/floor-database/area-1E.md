# Episode 2: Cliffs of Gal Da Val (Gal Gryphon)

[General floor database](README.md)

| Identifier | Value |
|---|---|
| Default floor slot | 12 |
| Area ID | 30 / 0x1E |

A quest can designate an area into a different floor slot. These identifiers must not be treated as interchangeable.

## Available map-table entries

Layout and entity variation are separate indices. On = multiplayer; Off = solo; Ulti tables are the Ultimate-specific map tables. Entries reflect supplied client resources, not a quest’s chosen runtime configuration.

| Table | Layout | Entity variation | Object basename | Enemy/event basename | Setup basename |
|---|---:|---:|---|---|---|
| [SetDataTableOff](tables/SetDataTableOff.txt#L142) | 0 | 0 | map_boss05_off | map_boss05 | map_boss05 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L142) | 0 | 0 | map_boss05_off | map_boss05 | map_boss05 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L169) | 0 | 0 | map_boss05 | map_boss05 | map_boss05 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L169) | 0 | 0 | map_boss05 | map_boss05 | map_boss05 |

## Qedit placement menus

Bundled and external definitions remain separate. The external BB list is monsv4/itemv4. Menu inclusion is editor evidence, not a runtime compatibility test.

### qedit-config

**mons:** 192 (Dragon /  Gal Griffin)

**item:** 0, 1, 8, 14, 25, 512, 515, 513, 553


### qedit-external

**monsv4:** 192 (Dragon /  Gal Griffin)

**itemv4:** 0, 1, 2, 7, 14, 8, 18, 21, 696, 698, 22, 23, 24, 512, 515, 523, 39, 553, 36, 513, 576


## Rooms, collision and coordinates

Room boundaries, transforms, empty-room IDs, valid walkable spawn positions and safe player spawn points have not yet been decoded for this layout family. This page is a general floor/resource reference, not a finished geometry atlas.

[Observed quest section index](../map-sections/README.md) can supply examples, but copying a room ID or coordinate requires verifying the exact layout.

[Documented monster constructor availability](../entity-database/areas.md) · [Qedit entity fields](../entity-database/qedit/entity-fields.md)
