# General floor and map database

**[Forest 1 and Forest 2 wireframes and numbered sections](geometry/README.md)** are now extracted directly from the supplied Qedit map files. Other areas still require extraction; section-to-boundary assignment remains unresolved.

This catalogue is independent of individual quests. It covers the 47 named area definitions for Episodes 1, 2 and 4, including boss, lobby, battle and test areas. It joins all four supplied client map tables with Qedit’s bundled and external area menus.

**Coverage:** area IDs, default floor slots, layout/entity variation indices, resource basenames, and editor placement menus. **Not yet complete:** geometric room IDs, boundaries, transforms, collision and safe spawn locations for every layout.

[Machine-readable floor database](floors.json) · [Observed quest sections](../map-sections/README.md) · [Monster database](../entity-database/monsters.md) · [NPC database](../entity-database/npcs.md)

## Creating a quest

1. Choose the episode and area.
2. Choose the appropriate multiplayer/solo and difficulty map table.
3. Select layout and entity variation separately.
4. Check Qedit’s placement menu and the documented constructor restrictions.
5. Obtain verified room geometry and spawn positions for that layout before adding entities.
6. Link rooms/waves/switches to the quest script and test in-game.

## Episode 1

| Area | Default floor | Name | Map-table entries |
|---|---:|---|---:|
| 0x00 | 0 | [Pioneer 2](area-00.md) | 4 |
| 0x01 | 1 | [Forest 1](area-01.md) | 16 |
| 0x02 | 2 | [Forest 2](area-02.md) | 16 |
| 0x03 | 3 | [Cave 1](area-03.md) | 36 |
| 0x04 | 4 | [Cave 2](area-04.md) | 30 |
| 0x05 | 5 | [Cave 3](area-05.md) | 36 |
| 0x06 | 6 | [Mine 1](area-06.md) | 48 |
| 0x07 | 7 | [Mine 2](area-07.md) | 48 |
| 0x08 | 8 | [Ruins 1](area-08.md) | 40 |
| 0x09 | 9 | [Ruins 2](area-09.md) | 40 |
| 0x0A | 10 | [Ruins 3](area-0A.md) | 40 |
| 0x0B | 11 | [Under the Dome (Dragon)](area-0B.md) | 4 |
| 0x0C | 12 | [Underground Channel (De Rol Le)](area-0C.md) | 4 |
| 0x0D | 13 | [Monitor Room (Vol Opt)](area-0D.md) | 4 |
| 0x0E | 14 | [???? (Dark Falz)](area-0E.md) | 4 |
| 0x0F | 15 | [Lobby](area-0F.md) | 60 |
| 0x10 | 16 | [Spaceship](area-10.md) | 12 |
| 0x11 | 17 | [Palace](area-11.md) | 12 |

## Episode 2

| Area | Default floor | Name | Map-table entries |
|---|---:|---|---:|
| 0x12 | 0 | [Lab](area-12.md) | 4 |
| 0x13 | 1 | [VR Temple Alpha](area-13.md) | 12 |
| 0x14 | 2 | [VR Temple Beta](area-14.md) | 12 |
| 0x15 | 3 | [VR Spaceship Alpha](area-15.md) | 12 |
| 0x16 | 4 | [VR Spaceship Beta](area-16.md) | 12 |
| 0x17 | 5 | [Central Control Area](area-17.md) | 12 |
| 0x18 | 6 | [Jungle Area North](area-18.md) | 12 |
| 0x19 | 7 | [Jungle Area East](area-19.md) | 12 |
| 0x1A | 8 | [Mountain Area](area-1A.md) | 24 |
| 0x1B | 9 | [Seaside Area](area-1B.md) | 12 |
| 0x1C | 10 | [Seabed Upper Levels](area-1C.md) | 18 |
| 0x1D | 11 | [Seabed Lower Levels](area-1D.md) | 18 |
| 0x1E | 12 | [Cliffs of Gal Da Val (Gal Gryphon)](area-1E.md) | 4 |
| 0x1F | 13 | [Test Subject Disposal Area (Olga Flow)](area-1F.md) | 4 |
| 0x20 | 14 | [VR Temple Final (Barba Ray)](area-20.md) | 4 |
| 0x21 | 15 | [VR Spaceship Final (Gol Dragon)](area-21.md) | 4 |
| 0x22 | 16 | [Seaside Area (night)](area-22.md) | 4 |
| 0x23 | 17 | [Control Tower](area-23.md) | 20 |

## Episode 4

| Area | Default floor | Name | Map-table entries |
|---|---:|---|---:|
| 0x2D | 0 | [Pioneer 2](area-2D.md) | 2 |
| 0x24 | 1 | [Crater (Eastern Route)](area-24.md) | 6 |
| 0x25 | 2 | [Crater (Western Route)](area-25.md) | 6 |
| 0x26 | 3 | [Crater (Southern Route)](area-26.md) | 6 |
| 0x27 | 4 | [Crater (Northern Route)](area-27.md) | 6 |
| 0x28 | 5 | [Crater Interior](area-28.md) | 6 |
| 0x29 | 6 | [Subterranean Desert 1](area-29.md) | 6 |
| 0x2A | 7 | [Subterranean Desert 2](area-2A.md) | 6 |
| 0x2B | 8 | [Subterranean Desert 3](area-2B.md) | 6 |
| 0x2C | 9 | [Meteor Impact Site](area-2C.md) | 2 |
| 0x2E | 10 | [Test Map](area-2E.md) | 2 |
