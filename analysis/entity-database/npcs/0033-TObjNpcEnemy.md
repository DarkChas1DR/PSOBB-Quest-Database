# Stage NPC's

DAT ID **0x0033 / 51**, constructor **TObjNpcEnemy**.

[Definition source](../../quest-knowledge/reference/server-source/Map.cc#L2780) · [Database index](../npcs.md)

## Source-documented areas

Episode 1: Pioneer 2 (area 0x00, default floor 0); Episode 1: Forest 1 (area 0x01, default floor 1); Episode 1: Forest 2 (area 0x02, default floor 2); Episode 1: Cave 1 (area 0x03, default floor 3); Episode 1: Cave 2 (area 0x04, default floor 4); Episode 1: Cave 3 (area 0x05, default floor 5); Episode 1: Mine 1 (area 0x06, default floor 6); Episode 1: Mine 2 (area 0x07, default floor 7); Episode 1: Ruins 1 (area 0x08, default floor 8); Episode 1: Ruins 2 (area 0x09, default floor 9); Episode 1: Ruins 3 (area 0x0A, default floor 10); Episode 1: Under the Dome (Dragon) (area 0x0B, default floor 11); Episode 1: Underground Channel (De Rol Le) (area 0x0C, default floor 12); Episode 1: Monitor Room (Vol Opt) (area 0x0D, default floor 13); Episode 1: ???? (Dark Falz) (area 0x0E, default floor 14); Episode 1: Lobby (area 0x0F, default floor 15); Episode 1: Spaceship (area 0x10, default floor 16); Episode 1: Palace (area 0x11, default floor 17); Episode 2: Lab (area 0x12, default floor 0); Episode 2: VR Temple Alpha (area 0x13, default floor 1); Episode 2: VR Temple Beta (area 0x14, default floor 2); Episode 2: VR Spaceship Alpha (area 0x15, default floor 3); Episode 2: VR Spaceship Beta (area 0x16, default floor 4); Episode 2: Central Control Area (area 0x17, default floor 5); Episode 2: Jungle Area North (area 0x18, default floor 6); Episode 2: Jungle Area East (area 0x19, default floor 7); Episode 2: Mountain Area (area 0x1A, default floor 8); Episode 2: Seaside Area (area 0x1B, default floor 9); Episode 2: Seabed Upper Levels (area 0x1C, default floor 10); Episode 2: Seabed Lower Levels (area 0x1D, default floor 11); Episode 2: Cliffs of Gal Da Val (Gal Gryphon) (area 0x1E, default floor 12); Episode 2: Test Subject Disposal Area (Olga Flow) (area 0x1F, default floor 13); Episode 2: VR Temple Final (Barba Ray) (area 0x20, default floor 14); Episode 2: VR Spaceship Final (Gol Dragon) (area 0x21, default floor 15); Episode 2: Seaside Area (night) (area 0x22, default floor 16); Episode 2: Control Tower (area 0x23, default floor 17); Episode 4: Pioneer 2 (area 0x2D, default floor 0)

Floor numbers are script slots. Resolve the quest map designation to an area before checking compatibility. Custom client patches may change constructor availability; this table describes the stored reference, not a live client test.

## Parameters and source notes

```text
Enemy that behaves like an NPC. Has all the same params as the standard NPC types, but also:
angle.x = definition index
The definition index is an integer from 0 to 15 (decimal) specifying which model, animations, and hitbox to use.
The available choices depend on which assets are loaded, which in turn depend on the area (not floor) in which
the NPC appears. To choose the right definition index, first look up the enemy you want in the models list
below, then find the corresponding number in the areas table below that, and use the (zero-based) index of the
number in that table for angle.x. For example, to place a Sinow Gold in Mine 2, angle.x should be 8 since Sinow
Gold is 27, and there are 8 other values before 27 in the Mine 2 list. The available models are:
01: Box (appearance depends on area)
02: Booma (Ep1/2), Boota (Ep4)
03: Gobooma (Ep1/2), Ze Boota (Ep4)
04: Gigobooma (Ep1/2), Ba Boota (Ep4)
05: Rappy (common)
06: Rappy (rare; appearance depends on episode and season event)
07: Mothmant
08: Monest
09: Barbarous Wolf (Ep1/2), Satellite Lizard (Ep4)
0A: Savage Wolf (Ep1/2), Yowie (Ep4)
0B: Chao
0C: Recon
0D: Recobox
0E: Ul Gibbon
0F: Zol Gibbon
10: Gee
11: NiGHTS? (TODO; from bm_ene_npc_nights_bml)
12: NiGHTS? (TODO; from bm_ene_npc_nights_bml)
13: Bulclaw
14: Claw
15: Dark Belra
16: Dark Bringer
17: Canadine
18: Canune
19: Dark Gunner (must be constructed after a Dark Gunner enemy, since the definition is populated in the enemy
constructor, not in the asset loader)
1A: Delsaber
1B: So Dimenian (Ep1/2), Goran (Ep4)
1C: La Dimenian (Ep1/2), Pyro Goran (Ep4)
1D: Dimenian (Ep1/2), Goran Detonator (Ep4)
1E: Dubchic (TODO: may be swapped)
1F: Gillchic (TODO: may be swapped)
20: Garanz
21: TODO (from bm_ene_gyaranzo_bml)
22: Nano Dragon (Ep1/2), Zu (Ep4)
23: Pan Arms
24: Hidoom
25: Migium
26: Sinow Beat
27: Sinow Gold
28: Pofuilly Slime
29: Pouilly Slime
2A: Chaos Sorcerer
2B: Sinow Berill
2C: Merillia
2D: Sinow Spigell (TODO: Could be Sinow Berill, but cloaked)
2E: Meriltas
2F: Evil Shark
30: Pal Shark
31: Guil Shark
32: TODO (from bm_ene_bm2_moja_bml) (Ep1/2), Astark (Ep4)
33: Hildebear
34: Hildeblue
35: Grass Assassin
36: TODO (from bm_ene_cgrass_bml)
37: Poison Lily (non-Tower) or Del Lily (Tower)
38: Floating robot (same as TODragonflyMachine01)
39: Ruins falling trap (TOTrapAncient01)
3A: Truncated column (TOVS2Wreck06)
3B: Ruins poison-spewing blob (Ep1) or Gee nest (Ep2)
3C: TODO (TMotorcycle with model number 0)
3D: TODO (TMotorcycle with model number 1)
3E: Jungle small rock (TORockJungleS01)
3F: Jungle plant (TOGrassJungle)
40: Seabed dolphin (same as __DOLPHIN__)
41: Gi Gue
42: Mericarol (ep2), Girtablulu (ep4)
43: Ill Gill
44: Gibbles
45: Dolmolm
46: Delbiter (ep2), Dorphon (ep4)
47: Deldepth
48: Deldepth
49: Sinow Zoa (visible; TODO: verify this)
4A: Sinow Zele (visible; TODO: verify this)
4B: Sinow Zoa (cloaked; TODO: verify this)
4C: Sinow Zele (cloaked; TODO: verify this)
4D: Morfos
4E: Epsilon
4F: Dolmdarl
This table shows which choices are available in each area:
Episode 1:
00 (Pioneer 2):     (none)
01 (Forest 1):      01 02 03 04 05 06 07 08 09 0A 0B 3C 3D
02 (Forest 2):      01 02 03 04 05 06 07 08 09 0A 0B 32 33 34 3C 3D
03 (Cave 1):        01 22 23 24 25 2F 30 31 35 36 37
04 (Cave 2):        01 22 28 29 2F 30 31 35 36 37
05 (Cave 3):        01 22 23 24 25 28 29 2F 30 31 37
06 (Mine 1):        01 17 18 1E 1F 20 21 26 27 38
07 (Mine 2):        01 17 18 1E 1F 20 21 26 27 38
08 (Ruins 1):       13 14 15 1A 1B 1C 1D 2A 39 3B
09 (Ruins 2):       16 1A 1B 1C 1D 39 3B
0A (Ruins 3):       15 16 1B 1C 1D 2A 39 3B
0B (Dragon):        01
0C (De Rol Le):     01
0D (Vol Opt):       01
0E (Dark Falz):     01
0F (Lobby):         (none)
10 (Spaceship):     16 1A 26 27 2F 30 31 32 33 34 35 36 3A
11 (Temple):        16 1A 26 27 2F 30 31 32 33 34 35 36 3A
Episode 2:
12 (Lab):           (none)
13 (Temple A):      05 06 07 08 15 1B 1C 1D 32 33 34 35 36 37 39 3A
14 (Temple B):      05 06 07 08 15 1B 1C 1D 32 33 34 35 36 37 39 3A
15 (Spaceship A):   09 0A 1A 1E 1F 20 21 23 24 25 39
16 (Spaceship B):   09 0A 1A 1E 1F 23 24 25 2A 39
17 (CCA):           05 06 0E 0F 10 2B 2C 2D 2E 3B 3E 3F 41 42 44
18 (Jungle N):      05 06 0E 0F 10 2B 2C 2D 2E 3B 3E 3F 41 42 44
19 (Jungle E):      05 06 0E 0F 10 2B 2C 2D 2E 3B 3E 3F 41 42 44
1A (Mountain):      05 06 0E 0F 10 2B 2C 2D 2E 3B 3E 3F 41 42 44
1B (Seaside):       05 06 0E 0F 10 2B 2C 2D 2E 3B 3E 3F 41 42 44
1C (Seabed U):      01 0C 0D 40 45 46 47 48 49 4A 4B 4C 4D 4F
1D (Seabed L):      01 0C 0D 40 45 46 47 48 49 4A 4B 4C 4D 4F
1E (Gal Gryphon):   (none)
1F (Olga Flow):     01
20 (Barba Ray):     (none)
21 (Gol Dragon):    (none)
22 (Seaside Night): 05 06 0C 0D 0E 0F 10 11 12 2C 2E 3B 3E 3F 45 4F
23 (Tower):         0C 0D 37 3B 41 42 43 44 46 4E
Episode 4 (these are not usable without a client patch, since this NPC is only available on Pioneer 2):
24 (Crater East):   02 03 04 05 06 09 0A 22 32 46
25 (Crater West):   02 03 04 05 06 09 0A 22 32 46
26 (Crater South):  02 03 04 05 06 09 0A 22 32 46
27 (Crater North):  02 03 04 05 06 09 0A 22 32 46
28 (Crater Int):    02 03 04 05 06 09 0A 22 32 46
29 (Desert 1):      05 06 09 0A 1B 1C 1D 22 3B 42
2A (Desert 2):      05 06 09 0A 1B 1C 1D 22 3B 42
2B (Desert 3):      05 06 09 0A 1B 1C 1D 22 3B 42
2C (Saint-Milion):  38 39 3A 3B 3C 3D 3E 3F 40
2D (Pioneer 2):     (none)
2E (Test area):     01 02 09 0A 22 32 38 39 3A 3B 3C 3D 3E 3F 40 42
This NPC exists in Episode 3, but is only available in the Morgue and in the lobby. There are no available
models in those areas, which makes it essentially useless.

```

## Observed quest placements

598 records, including language duplicates. These are observations, not spawn permissions.

[All observed positions, angles, parameters and handler candidates](../observations/0033.csv)

| Quest | Floor | Room / wave | Handler candidate |
|---|---:|---|---|
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 13 / 0 | — |
| [Test/q37-bb-e](../../server-catalogue/Test/q37-bb-e/README.md) | 2 | 3 / 0 | — |
| [Test/q37-bb-j](../../server-catalogue/Test/q37-bb-j/README.md) | 2 | 13 / 0 | — |
| [Test/q37-bb-j](../../server-catalogue/Test/q37-bb-j/README.md) | 2 | 3 / 0 | — |
| [events-ep1/q28-bb-e](../../server-catalogue/events-ep1/q28-bb-e/README.md) | 8 | 70 / 0 | — |
| [events-ep1/q28-bb-e](../../server-catalogue/events-ep1/q28-bb-e/README.md) | 8 | 70 / 0 | — |
| [events-ep1/q28-bb-e](../../server-catalogue/events-ep1/q28-bb-e/README.md) | 8 | 70 / 0 | — |
| [events-ep1/q28-bb-e](../../server-catalogue/events-ep1/q28-bb-e/README.md) | 8 | 70 / 0 | — |
| [events-ep1/q28-bb-e](../../server-catalogue/events-ep1/q28-bb-e/README.md) | 8 | 70 / 0 | — |
| [events-ep1/q28-bb-e](../../server-catalogue/events-ep1/q28-bb-e/README.md) | 8 | 70 / 0 | — |
| [events-ep1/q28-bb-e](../../server-catalogue/events-ep1/q28-bb-e/README.md) | 8 | 70 / 0 | — |
| [events-ep1/q28-bb-e](../../server-catalogue/events-ep1/q28-bb-e/README.md) | 8 | 70 / 0 | — |
| [events-ep1/q28-bb-e](../../server-catalogue/events-ep1/q28-bb-e/README.md) | 8 | 70 / 0 | — |
| [events-ep1/q28-bb-j](../../server-catalogue/events-ep1/q28-bb-j/README.md) | 8 | 70 / 0 | — |
| [events-ep1/q28-bb-j](../../server-catalogue/events-ep1/q28-bb-j/README.md) | 8 | 70 / 0 | — |
| [events-ep1/q28-bb-j](../../server-catalogue/events-ep1/q28-bb-j/README.md) | 8 | 70 / 0 | — |
| [events-ep1/q28-bb-j](../../server-catalogue/events-ep1/q28-bb-j/README.md) | 8 | 70 / 0 | — |
| [events-ep1/q28-bb-j](../../server-catalogue/events-ep1/q28-bb-j/README.md) | 8 | 70 / 0 | — |
| [events-ep1/q28-bb-j](../../server-catalogue/events-ep1/q28-bb-j/README.md) | 8 | 70 / 0 | — |
| [events-ep1/q28-bb-j](../../server-catalogue/events-ep1/q28-bb-j/README.md) | 8 | 70 / 0 | — |
| [events-ep1/q28-bb-j](../../server-catalogue/events-ep1/q28-bb-j/README.md) | 8 | 70 / 0 | — |
| [events-ep1/q28-bb-j](../../server-catalogue/events-ep1/q28-bb-j/README.md) | 8 | 70 / 0 | — |
| [events-ep1/q93-bb-e](../../server-catalogue/events-ep1/q93-bb-e/README.md) | 1 | 2 / 0 | — |
| [events-ep1/q93-bb-e](../../server-catalogue/events-ep1/q93-bb-e/README.md) | 1 | 2 / 0 | — |
| [events-ep1/q93-bb-j](../../server-catalogue/events-ep1/q93-bb-j/README.md) | 1 | 2 / 0 | — |
| [events-ep1/q93-bb-j](../../server-catalogue/events-ep1/q93-bb-j/README.md) | 1 | 2 / 0 | — |
| [events-ep1/q127-bb-e](../../server-catalogue/events-ep1/q127-bb-e/README.md) | 2 | 3 / 0 | — |
| [events-ep1/q127-bb-e](../../server-catalogue/events-ep1/q127-bb-e/README.md) | 2 | 3 / 0 | — |
| [events-ep1/q127-bb-e](../../server-catalogue/events-ep1/q127-bb-e/README.md) | 2 | 3 / 0 | — |
| [events-ep1/q127-bb-e](../../server-catalogue/events-ep1/q127-bb-e/README.md) | 2 | 5 / 0 | — |
