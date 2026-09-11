# Recorded rooms / sections — 幻界の果てに ２

[Quest dossier](README.md) · [Section coverage guide](../../../map-sections/README.md)

These IDs are observed in this quest’s DAT placements/events/random-room records. They are not a complete list of geometric sections. Positions and facing are in the linked placement files; no section boundary has been inferred from those points.

[Enemy/NPC placements](enemies.csv) · [Object placements](objects.csv) · [Full map data](map.txt)

## Map designation evidence

These are extracted designation operands, not evaluated runtime state. Multiple designations can be alternatives; missing entries are unresolved rather than assumed from the floor number.

```text
0x00, 0x12, 0x00, 0x00, 0x00
0x05, 0x17, 0x00, 0x00, 0x00
0x08, 0x1A, 0x00, 0x00, 0x01
```

## Observed section IDs

| Floor slot | Room / section | Objects | Enemy/NPC records | Waves | Event IDs | Random locations |
|---:|---:|---:|---:|---|---|---:|
| 0 | 10 | 15 | 2 | 0 |  | 0 |
| 0 | 20 | 2 | 0 |  |  | 0 |
| 0 | 30 | 12 | 10 | 0 |  | 0 |
| 0 | 40 | 2 | 0 |  |  | 0 |
| 0 | 42 | 11 | 7 | 0, 1 |  | 0 |
| 0 | 50 | 2 | 1 | 0 |  | 0 |
| 5 | 1 | 34 | 0 |  |  | 0 |
| 5 | 2 | 5 | 9 | 1, 2 | 21, 211 | 0 |
| 5 | 3 | 5 | 10 | 1, 2 | 31, 311 | 0 |
| 5 | 4 | 9 | 10 | 1, 2, 3 | 41, 411, 412 | 0 |
| 5 | 5 | 17 | 15 | 1, 2, 3, 4 | 51, 511, 512, 513, 514 | 0 |
| 5 | 6 | 10 | 0 |  |  | 0 |
| 5 | 7 | 2 | 0 |  |  | 0 |
| 5 | 8 | 16 | 8 | 1 | 81 | 0 |
| 5 | 9 | 12 | 11 | 1, 2, 3 | 91, 911, 912 | 0 |
| 5 | 10 | 5 | 6 | 1, 2 | 101, 1011 | 0 |
| 5 | 11 | 3 | 96 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25 | 111, 112, 113, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1121, 1122, 1123, 1124, 1131, 1132, 11111, 11112, 11113, 11114, 11115, 11116, 11117 | 0 |
| 5 | 12 | 7 | 10 | 1, 2, 3, 4, 5 | 121, 122, 123, 124, 125 | 0 |
| 5 | 13 | 14 | 16 | 1, 2, 3 | 131, 1311, 1312 | 0 |
| 8 | 1 | 5 | 0 |  |  | 0 |
| 8 | 2 | 32 | 75 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17 | 21, 22, 23, 24, 221, 222, 223, 224, 225, 226, 227, 228, 229, 231, 232, 2211, 2212 | 0 |
| 8 | 3 | 73 | 34 | 1, 2, 3, 4, 5, 6 | 31, 311, 312, 313, 314, 315 | 0 |
| 8 | 4 | 37 | 1 | 1 | 41 | 0 |
| 8 | 5 | 13 | 26 | 1, 2, 3, 4, 5 | 51, 511, 512, 513, 514 | 0 |
| 8 | 8 | 28 | 26 | 1, 2, 3, 4, 5, 6, 7 | 81, 82, 83, 84, 811, 821, 831 | 0 |
| 8 | 9 | 25 | 0 |  |  | 0 |
| 8 | 10 | 5 | 5 | 1, 2, 3 | 101, 1011, 1012 | 0 |
