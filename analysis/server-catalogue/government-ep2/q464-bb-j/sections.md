# Recorded rooms / sections — ７－４：中央管理区

[Quest dossier](README.md) · [Section coverage guide](../../../map-sections/README.md)

These IDs are observed in this quest’s DAT placements/events/random-room records. They are not a complete list of geometric sections. Positions and facing are in the linked placement files; no section boundary has been inferred from those points.

[Enemy/NPC placements](enemies.csv) · [Object placements](objects.csv) · [Full map data](map.txt)

## Map designation evidence

These are extracted designation operands, not evaluated runtime state. Multiple designations can be alternatives; missing entries are unresolved rather than assumed from the floor number.

```text
0x00, 0x12, 0x00, 0x00, 0x00
0x05, 0x17, 0x00, 0x00, 0x00
```

## Observed section IDs

| Floor slot | Room / section | Objects | Enemy/NPC records | Waves | Event IDs | Random locations |
|---:|---:|---:|---:|---|---|---:|
| 0 | 10 | 23 | 1 | 0 |  | 0 |
| 0 | 20 | 2 | 0 |  |  | 0 |
| 0 | 30 | 12 | 10 | 0 |  | 0 |
| 0 | 40 | 2 | 0 |  |  | 0 |
| 0 | 42 | 12 | 7 | 0 |  | 0 |
| 0 | 50 | 2 | 1 | 0 |  | 0 |
| 5 | 1 | 30 | 0 |  |  | 0 |
| 5 | 2 | 8 | 2 | 1 | 21 | 0 |
| 5 | 3 | 7 | 6 | 1, 2 | 31, 311 | 0 |
| 5 | 4 | 20 | 7 | 1, 2, 3 | 41, 42, 411 | 0 |
| 5 | 5 | 12 | 8 | 1, 2, 3 | 51, 52, 511 | 0 |
| 5 | 6 | 7 | 0 |  |  | 0 |
| 5 | 11 | 1 | 31 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | 111, 112, 113, 114, 1111, 1112, 1113, 1121, 1122, 1123, 1131, 1132, 1133, 1141, 1142, 1143 | 0 |
| 5 | 12 | 1 | 29 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17 | 121, 122, 123, 124, 1211, 1212, 1213, 1214, 1221, 1222, 1223, 1231, 1232, 1233, 1241, 1242, 1243 | 0 |
| 5 | 13 | 5 | 42 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 | 131, 132, 133, 1311, 1312, 1313, 1314, 1315, 1316, 1317, 1321, 1331 | 0 |
