# Recorded rooms / sections — 夢幻のごとく １

[Quest dossier](README.md) · [Section coverage guide](../../../map-sections/README.md)

These IDs are observed in this quest’s DAT placements/events/random-room records. They are not a complete list of geometric sections. Positions and facing are in the linked placement files; no section boundary has been inferred from those points.

[Enemy/NPC placements](enemies.csv) · [Object placements](objects.csv) · [Full map data](map.txt)

## Map designation evidence

These are extracted designation operands, not evaluated runtime state. Multiple designations can be alternatives; missing entries are unresolved rather than assumed from the floor number.

```text
0x00, 0x00, 0x00, 0x00, 0x00
0x01, 0x01, 0x00, 0x00, 0x01
0x02, 0x02, 0x00, 0x00, 0x01
```

## Observed section IDs

| Floor slot | Room / section | Objects | Enemy/NPC records | Waves | Event IDs | Random locations |
|---:|---:|---:|---:|---|---|---:|
| 0 | 10 | 26 | 4 | 0 |  | 0 |
| 0 | 20 | 0 | 10 | 0 |  | 0 |
| 0 | 30 | 0 | 5 | 0 |  | 0 |
| 0 | 40 | 0 | 2 | 0 |  | 0 |
| 1 | 2 | 13 | 10 | 1, 2, 3, 4 | 21, 211, 212, 213 | 0 |
| 1 | 4 | 6 | 8 | 1, 2 | 41, 411 | 0 |
| 1 | 5 | 19 | 12 | 1, 2, 3 | 51, 511, 512 | 0 |
| 1 | 7 | 9 | 12 | 1, 2, 3 | 71, 711, 712 | 0 |
| 1 | 8 | 13 | 7 | 1, 2 | 81, 81 | 0 |
| 1 | 10 | 8 | 5 | 1, 2, 3 | 101, 1011, 1012 | 0 |
| 1 | 11 | 11 | 10 | 1, 2, 3 | 111, 1111, 1112 | 0 |
| 1 | 16 | 26 | 0 |  |  | 0 |
| 2 | 1 | 30 | 0 |  |  | 0 |
| 2 | 2 | 16 | 10 | 1, 2, 3, 4, 5 | 21, 22, 211, 221, 222 | 0 |
| 2 | 3 | 5 | 6 | 1 | 31 | 0 |
| 2 | 4 | 7 | 0 |  |  | 0 |
| 2 | 5 | 5 | 3 | 1 | 51 | 0 |
| 2 | 6 | 5 | 8 | 1, 2, 3 | 61, 611, 612 | 0 |
| 2 | 7 | 5 | 0 |  |  | 0 |
| 2 | 10 | 9 | 3 | 1 | 101 | 0 |
| 2 | 11 | 9 | 9 | 1, 2, 3, 4, 5 | 111, 112, 113, 1111, 1121 | 0 |
| 2 | 12 | 11 | 57 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 | 121, 122, 1211, 1212, 1213, 1214, 1215, 1216, 1217, 1218, 1219, 1221, 1222, 1223, 1224, 1225, 1226, 1227, 1228, 1229 | 0 |
| 2 | 13 | 13 | 8 | 1, 2 | 131, 1311 | 0 |
| 2 | 15 | 22 | 11 | 1, 2, 3, 4, 5, 6 | 151, 152, 153, 154, 1511, 1512 | 0 |
