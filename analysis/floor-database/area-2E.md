# Episode 4: Test Map

[General floor database](README.md)

| Identifier | Value |
|---|---|
| Default floor slot | 10 |
| Area ID | 46 / 0x2E |

A quest can designate an area into a different floor slot. These identifiers must not be treated as interchangeable.

## Available map-table entries

Layout and entity variation are separate indices. On = multiplayer; Off = solo; Ulti tables are the Ultimate-specific map tables. Entries reflect supplied client resources, not a quest’s chosen runtime configuration.

| Table | Layout | Entity variation | Object basename | Enemy/event basename | Setup basename |
|---|---:|---:|---|---|---|
| [SetDataTableOff](tables/SetDataTableOff.txt#L178) | 0 | 0 | map_test01_00_00 | map_test01_00_00 | map_test01_00 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L205) | 0 | 0 | map_test01_00_00 | map_test01_00_00 | map_test01_00 |

## Qedit placement menus

Bundled and external definitions remain separate. The external BB list is monsv4/itemv4. Menu inclusion is editor evidence, not a runtime compatibility test.

### qedit-external

**monsv4:** 272 (astark), 273 (Saterlite Lizard), 274 (Merissa A), 275 (Girt), 276 (Zu), 277 (Boota), 278 (Dorphon), 279 (Goran), 65 (Rag Rappy / Sand Rappy), 280 (Rupika)

**itemv4:** Empty list


## Rooms, collision and coordinates

Room boundaries, transforms, empty-room IDs, valid walkable spawn positions and safe player spawn points have not yet been decoded for this layout family. This page is a general floor/resource reference, not a finished geometry atlas.

[Observed quest section index](../map-sections/README.md) can supply examples, but copying a room ID or coordinate requires verifying the exact layout.

[Documented monster constructor availability](../entity-database/areas.md) · [Qedit entity fields](../entity-database/qedit/entity-fields.md)


<!-- geometry-atlas:start -->
## Extracted map wireframes

[map_test01_00](geometry/map_test01_00.md)

Matching uses setup-resource filenames. Section reference positions and collision triangles are extracted; section boundary ownership and safe spawning remain unverified.
<!-- geometry-atlas:end -->
