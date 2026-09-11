# Episode 2: VR Spaceship Final (Gol Dragon)

[General floor database](README.md)

| Identifier | Value |
|---|---|
| Default floor slot | 15 |
| Area ID | 33 / 0x21 |

A quest can designate an area into a different floor slot. These identifiers must not be treated as interchangeable.

## Available map-table entries

Layout and entity variation are separate indices. On = multiplayer; Off = solo; Ulti tables are the Ultimate-specific map tables. Entries reflect supplied client resources, not a quest’s chosen runtime configuration.

| Table | Layout | Entity variation | Object basename | Enemy/event basename | Setup basename |
|---|---:|---:|---|---|---|
| [SetDataTableOff](tables/SetDataTableOff.txt#L145) | 0 | 0 | map_boss08_off | map_boss08 | map_boss08 |
| [SetDataTableOffUlti](tables/SetDataTableOffUlti.txt#L145) | 0 | 0 | map_boss08 | map_boss08 | map_boss08 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L172) | 0 | 0 | map_boss08 | map_boss08 | map_boss08 |
| [SetDataTableOnUlti](tables/SetDataTableOnUlti.txt#L172) | 0 | 0 | map_boss08 | map_boss08 | map_boss08 |

## Qedit placement menus

Bundled and external definitions remain separate. The external BB list is monsv4/itemv4. Menu inclusion is editor evidence, not a runtime compatibility test.

### qedit-config

**mons:** 204 (Gol Dragon )

**item:** 0, 1, 8, 14, 25, 353, 354, 2, 557


### qedit-external

**monsv4:** 204 (Gol Dragon )

**itemv4:** 0, 1, 2, 7, 14, 8, 18, 21, 696, 698, 22, 23, 24, 353, 354, 672, 39, 553, 36


## Rooms, collision and coordinates

Room boundaries, transforms, empty-room IDs, valid walkable spawn positions and safe player spawn points have not yet been decoded for this layout family. This page is a general floor/resource reference, not a finished geometry atlas.

[Observed quest section index](../map-sections/README.md) can supply examples, but copying a room ID or coordinate requires verifying the exact layout.

[Documented monster constructor availability](../entity-database/areas.md) · [Qedit entity fields](../entity-database/qedit/entity-fields.md)


<!-- geometry-atlas:start -->
## Extracted map wireframes

[map_boss08](geometry/map_boss08.md)

Matching uses setup-resource filenames. Section reference positions and collision triangles are extracted; section boundary ownership and safe spawning remain unverified.
<!-- geometry-atlas:end -->
