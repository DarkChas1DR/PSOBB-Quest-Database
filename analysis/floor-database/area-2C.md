# Episode 4: Meteor Impact Site

[General floor database](README.md)

| Identifier | Value |
|---|---|
| Default floor slot | 9 |
| Area ID | 44 / 0x2C |

A quest can designate an area into a different floor slot. These identifiers must not be treated as interchangeable.

## Available map-table entries

Layout and entity variation are separate indices. On = multiplayer; Off = solo; Ulti tables are the Ultimate-specific map tables. Entries reflect supplied client resources, not a quest’s chosen runtime configuration.

| Table | Layout | Entity variation | Object basename | Enemy/event basename | Setup basename |
|---|---:|---:|---|---|---|
| [SetDataTableOff](tables/SetDataTableOff.txt#L176) | 0 | 0 | map_boss09_00_00 | map_boss09_00_00 | map_boss09_00 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L203) | 0 | 0 | map_boss09_00_00 | map_boss09_00_00 | map_boss09_00 |

## Qedit placement menus

Bundled and external definitions remain separate. The external BB list is monsv4/itemv4. Menu inclusion is editor evidence, not a runtime compatibility test.

### qedit-config

**mons:** 281 (Saint million), 280 (Rupika), 243 (Default Ramarl (Karen)), 244 (Leo), 41 (Default Fomewearl (Rupika))

**item:** 0, 1, 2, 8, 14, 27, 136, 146, 961


### qedit-external

**monsv4:** 281 (Saint million), 243 (Default Ramarl (Karen)), 244 (Leo), 25 (Blue Soldier), 41 (Default Fomewearl (Rupika)), 280 (Rupika)

**itemv4:** 0, 10, 11, 12, 13, 8, 146, 2, 3, 27, 28, 697, 14, 960, 961, 768


## Rooms, collision and coordinates

Room boundaries, transforms, empty-room IDs, valid walkable spawn positions and safe player spawn points have not yet been decoded for this layout family. This page is a general floor/resource reference, not a finished geometry atlas.

[Observed quest section index](../map-sections/README.md) can supply examples, but copying a room ID or coordinate requires verifying the exact layout.

[Documented monster constructor availability](../entity-database/areas.md) · [Qedit entity fields](../entity-database/qedit/entity-fields.md)
