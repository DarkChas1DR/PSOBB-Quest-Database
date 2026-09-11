# Episode 2: Test Subject Disposal Area (Olga Flow)

[General floor database](README.md)

| Identifier | Value |
|---|---|
| Default floor slot | 13 |
| Area ID | 31 / 0x1F |

A quest can designate an area into a different floor slot. These identifiers must not be treated as interchangeable.

## Available map-table entries

Layout and entity variation are separate indices. On = multiplayer; Off = solo; Ulti tables are the Ultimate-specific map tables. Entries reflect supplied client resources, not a quest’s chosen runtime configuration.

| Table | Layout | Entity variation | Object basename | Enemy/event basename | Setup basename |
|---|---:|---:|---|---|---|
| [SetDataTableOff](tables/SetDataTableOff.txt#L143) | 0 | 0 | map_boss06_off | map_boss06 | map_boss06 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L143) | 0 | 0 | map_boss06 | map_boss06 | map_boss06 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L170) | 0 | 0 | map_boss06 | map_boss06 | map_boss06 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L170) | 0 | 0 | map_boss06 | map_boss06 | map_boss06 |

## Qedit placement menus

Bundled and external definitions remain separate. The external BB list is monsv4/itemv4. Menu inclusion is editor evidence, not a runtime compatibility test.

### qedit-config

**mons:** 202 (Barba Ray), 246 (Unknown 246)

**item:** 0, 1, 8, 14, 25, 512, 515, 513, 146, 131, 257


### qedit-external

**monsv4:** 202 (Barba Ray), 246 (Unknown 246)

**itemv4:** 0, 1, 2, 28, 513, 7, 14, 8, 18, 21, 696, 698, 22, 23, 24, 136, 146, 39, 553, 36, 6, 40, 41, 700


## Rooms, collision and coordinates

Room boundaries, transforms, empty-room IDs, valid walkable spawn positions and safe player spawn points have not yet been decoded for this layout family. This page is a general floor/resource reference, not a finished geometry atlas.

[Observed quest section index](../map-sections/README.md) can supply examples, but copying a room ID or coordinate requires verifying the exact layout.

[Documented monster constructor availability](../entity-database/areas.md) · [Qedit entity fields](../entity-database/qedit/entity-fields.md)
