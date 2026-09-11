# Episode 1: Monitor Room (Vol Opt)

[General floor database](README.md)

| Identifier | Value |
|---|---|
| Default floor slot | 13 |
| Area ID | 13 / 0x0D |

A quest can designate an area into a different floor slot. These identifiers must not be treated as interchangeable.

## Available map-table entries

Layout and entity variation are separate indices. On = multiplayer; Off = solo; Ulti tables are the Ultimate-specific map tables. Entries reflect supplied client resources, not a quest’s chosen runtime configuration.

| Table | Layout | Entity variation | Object basename | Enemy/event basename | Setup basename |
|---|---:|---:|---|---|---|
| [SetDataTableOff](tables/SetDataTableOff.txt#L82) | 0 | 0 | map_boss03 | map_boss03 | map_boss03 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L82) | 0 | 0 | map_boss03 | map_boss03 | map_boss03 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L103) | 0 | 0 | map_boss03 | map_boss03 | map_boss03 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L103) | 0 | 0 | map_boss03 | map_boss03 | map_boss03 |

## Qedit placement menus

Bundled and external definitions remain separate. The external BB list is monsv4/itemv4. Menu inclusion is editor evidence, not a runtime compatibility test.

### qedit-config

**mons:** 197 (unnamed), 194 (vol opt)

**item:** 0, 1, 2, 8, 14, 25, 27, 136, 146, 3, 304, 141, 18, 352


### qedit-external

**monsv4:** 51 (Stage NPC's), 194 (vol opt), 195 (unnamed), 196 (unnamed), 197 (unnamed), 198 (unnamed), 199 (unnamed)

**itemv4:** 0, 1, 2, 3, 27, 697, 40, 41, 7, 14, 8, 18, 21, 696, 698, 22, 23, 24, 146, 304, 141, 352


## Rooms, collision and coordinates

Room boundaries, transforms, empty-room IDs, valid walkable spawn positions and safe player spawn points have not yet been decoded for this layout family. This page is a general floor/resource reference, not a finished geometry atlas.

[Observed quest section index](../map-sections/README.md) can supply examples, but copying a room ID or coordinate requires verifying the exact layout.

[Documented monster constructor availability](../entity-database/areas.md) · [Qedit entity fields](../entity-database/qedit/entity-fields.md)


<!-- geometry-atlas:start -->
## Extracted map wireframes

[map_boss03](geometry/map_boss03.md)

Matching uses setup-resource filenames. Section reference positions and collision triangles are extracted; section boundary ownership and safe spawning remain unverified.
<!-- geometry-atlas:end -->
