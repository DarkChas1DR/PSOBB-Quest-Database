# Episode 4: Pioneer 2

[General floor database](README.md)

| Identifier | Value |
|---|---|
| Default floor slot | 0 |
| Area ID | 45 / 0x2D |

A quest can designate an area into a different floor slot. These identifiers must not be treated as interchangeable.

## Available map-table entries

Layout and entity variation are separate indices. On = multiplayer; Off = solo; Ulti tables are the Ultimate-specific map tables. Entries reflect supplied client resources, not a quest’s chosen runtime configuration.

| Table | Layout | Entity variation | Object basename | Enemy/event basename | Setup basename |
|---|---:|---:|---|---|---|
| [SetDataTableOff](tables/SetDataTableOff.txt#L177) | 0 | 0 | map_city02_00_00 | map_city02_00_00 | map_city02_00 |
| [SetDataTableOn](tables/SetDataTableOn.txt#L204) | 0 | 0 | map_city02_00_00 | map_city02_00_00 | map_city02_00 |

## Qedit placement menus

Bundled and external definitions remain separate. The external BB list is monsv4/itemv4. Menu inclusion is editor evidence, not a runtime compatibility test.

### qedit-config

**mons:** 1 (Unknown 1), 2 (Unknown 2), 3 (Unknown 3), 4 (Unknown 4), 5 (Unknown 5), 6 (Unknown 6), 7 (Unknown 7), 8 (Unknown 8), 9 (Unknown 9), 10 (Uknown 10), 11 (Armor shop), 12 (Weapon Shop), 13 (Zidd), 14 (Unknown 14), 25 (Blue Soldier), 26 (Red Soldier), 27 (Principle), 28 (Tekker), 29 (Guild Lady), 30 (Scientist), 31 (Nurse), 32 (Irene), 33 (Default Humar (Ash)), 34 (Default Hunewearl (Sue)), 36 (Default Ramar (Bernie)), 37 (Default Racast (Gilingham)), 38 (Default Racaseal (Elenor)), 39 (Default Fomarl (Alisha)), 40 (Default Fomewm (Montaque)), 41 (Default Fomewearl (Rupika)), 43 (Unknown 43), 44 (Unknown 44), 45 (Dacci), 48 (unnamed), 49 (unnamed), 50 (unnamed), 208 (Unknown 208), 209 (Natasha), 210 (Dan), 211 (Unknown 211), 240 (Armor shop), 241 (Item Shop), 242 (Default Fomar), 243 (Default Ramarl (Karen)), 244 (Leo), 245 (Pagini), 246 (Unknown 246), 247 (Nol), 248 (Elly), 249 (Unknown 249), 250 (Ep 2 Item Shop), 251 (Ep 2 Weapon Shop), 252 (Security Guard), 253 (Ep 2 Hunters Guild), 254 (Ep 2 Nurse), 255 (Unknown 255), 256 (Momoka), 280 (Rupika)

**item:** 0, 1, 2, 3, 8, 14, 18, 25, 26, 27, 64, 65, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 87


### qedit-external

**monsv4:** 1 (Unknown 1), 2 (Unknown 2), 3 (Unknown 3), 4 (Unknown 4), 5 (Unknown 5), 6 (Unknown 6), 7 (Unknown 7), 8 (Unknown 8), 9 (Unknown 9), 10 (Uknown 10), 11 (Armor shop), 12 (Weapon Shop), 13 (Zidd), 14 (Unknown 14), 28 (Tekker), 25 (Blue Soldier), 26 (Red Soldier), 27 (Principle), 29 (Guild Lady), 30 (Scientist), 31 (Nurse), 32 (Irene), 33 (Default Humar (Ash)), 34 (Default Hunewearl (Sue)), 36 (Default Ramar (Bernie)), 37 (Default Racast (Gilingham)), 38 (Default Racaseal (Elenor)), 39 (Default Fomarl (Alisha)), 40 (Default Fomewm (Montaque)), 41 (Default Fomewearl (Rupika)), 43 (Unknown 43), 44 (Unknown 44), 45 (Dacci), 48 (unnamed), 49 (unnamed), 50 (unnamed), 208 (Unknown 208), 209 (Natasha), 51 (Stage NPC's), 256 (Momoka), 243 (Default Ramarl (Karen)), 244 (Leo), 280 (Rupika)

**itemv4:** 0, 1, 2, 3, 25, 697, 26, 4, 64, 65, 6, 40, 41, 7, 8, 18, 21, 696, 698, 9, 20, 66, 22, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 32, 33, 36, 85, 37, 38, 87


## Rooms, collision and coordinates

Room boundaries, transforms, empty-room IDs, valid walkable spawn positions and safe player spawn points have not yet been decoded for this layout family. This page is a general floor/resource reference, not a finished geometry atlas.

[Observed quest section index](../map-sections/README.md) can supply examples, but copying a room ID or coordinate requires verifying the exact layout.

[Documented monster constructor availability](../entity-database/areas.md) · [Qedit entity fields](../entity-database/qedit/entity-fields.md)


<!-- geometry-atlas:start -->
## Extracted map wireframes

[map_city02_00](geometry/map_city02_00.md)

Matching uses setup-resource filenames. Section reference positions and collision triangles are extracted; section boundary ownership and safe spawning remain unverified.
<!-- geometry-atlas:end -->
