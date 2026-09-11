# Recorded rooms / sections — New Mop-Up Operation #2

[Quest dossier](README.md) · [Section coverage guide](../../../map-sections/README.md)

These IDs are observed in this quest’s DAT placements/events/random-room records. They are not a complete list of geometric sections. Positions and facing are in the linked placement files; no section boundary has been inferred from those points.

[Enemy/NPC placements](enemies.csv) · [Object placements](objects.csv) · [Full map data](map.txt)

## Map designation evidence

These are extracted designation operands, not evaluated runtime state. Multiple designations can be alternatives; missing entries are unresolved rather than assumed from the floor number.

```text
0x00, 0x2D, 0x00, 0x00, 0x00
0x05, 0x28, 0x00, 0x00, 0x00
```

## Observed section IDs

| Floor slot | Room / section | Objects | Enemy/NPC records | Waves | Event IDs | Random locations |
|---:|---:|---:|---:|---|---|---:|
| 0 | 10 | 26 | 2 | 0 |  | 0 |
| 0 | 20 | 0 | 8 | 0 |  | 0 |
| 0 | 30 | 0 | 5 | 0 |  | 0 |
| 0 | 40 | 0 | 2 | 0 |  | 0 |
| 5 | 10 | 2 | 31 | 1, 2, 3, 4, 5, 6, 7, 8, 9 | 102, 103, 106, 1011, 1012, 1041, 1042, 1051, 1052 | 0 |
| 5 | 20 | 2 | 29 | 1, 2, 3, 4, 5, 6, 7, 8, 9 | 204, 205, 206, 2011, 2012, 2021, 2022, 2031, 2032 | 0 |
| 5 | 30 | 2 | 40 | 1, 2, 3, 4, 5, 6, 7, 8, 9 | 301, 302, 303, 304, 306, 307, 308, 3051, 3052 | 0 |
| 5 | 40 | 2 | 28 | 1, 2, 3, 4, 5, 6, 7, 8 | 401, 402, 405, 406, 4031, 4032, 4041, 4042 | 0 |
| 5 | 50 | 22 | 30 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 | 501, 502, 503, 507, 5041, 5042, 5051, 5052, 5061, 5062 | 0 |
| 5 | 60 | 4 | 28 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 | 601, 605, 606, 607, 608, 6021, 6022, 6031, 6032, 6041, 6042 | 0 |
