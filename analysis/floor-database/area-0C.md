# Episode 1: Underground Channel (De Rol Le)

[General floor database](README.md)

| Identifier | Value |
|---|---|
| Default floor slot | 12 |
| Area ID | 12 / 0x0C |

A quest can designate an area into a different floor slot. These identifiers must not be treated as interchangeable.

## Available map-table entries

Layout and entity variation are separate indices. On = multiplayer; Off = solo; Ulti tables are the Ultimate-specific map tables. Entries reflect supplied client resources, not a quest’s chosen runtime configuration.

| Table | Layout | Entity variation | Object basename | Enemy/event basename | Setup basename |
|---|---:|---:|---|---|---|
| [SetDataTableOff](tables/SetDataTableOff.txt#L81) | 0 | 0 | map_boss02 | map_boss02 | map_boss02 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L81) | 0 | 0 | map_boss02 | map_boss02 | map_boss02 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L102) | 0 | 0 | map_boss02 | map_boss02 | map_boss02 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L102) | 0 | 0 | map_boss02 | map_boss02 | map_boss02 |

## Qedit placement menus

Bundled and external definitions remain separate. The external BB list is monsv4/itemv4. Menu inclusion is editor evidence, not a runtime compatibility test.

### qedit-config

**mons:** 193 (de ro le)

**item:** 0, 1, 2, 8, 14, 25, 27, 136, 146, 18


### qedit-external

**monsv4:** 193 (de ro le)

**itemv4:** 0, 1, 2, 3, 27, 697, 7, 14, 8, 18, 21, 696, 698, 22, 23, 24, 146


## Rooms, collision and coordinates

Room boundaries, transforms, empty-room IDs, valid walkable spawn positions and safe player spawn points have not yet been decoded for this layout family. This page is a general floor/resource reference, not a finished geometry atlas.

[Observed quest section index](../map-sections/README.md) can supply examples, but copying a room ID or coordinate requires verifying the exact layout.

[Documented monster constructor availability](../entity-database/areas.md) · [Qedit entity fields](../entity-database/qedit/entity-fields.md)
