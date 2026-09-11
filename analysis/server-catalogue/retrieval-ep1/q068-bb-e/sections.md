# Recorded rooms / sections — The Missing Maracas

[Quest dossier](README.md) · [Section coverage guide](../../../map-sections/README.md)

These IDs are observed in this quest’s DAT placements/events/random-room records. They are not a complete list of geometric sections. Positions and facing are in the linked placement files; no section boundary has been inferred from those points.

[Enemy/NPC placements](enemies.csv) · [Object placements](objects.csv) · [Full map data](map.txt)

## Map designation evidence

These are extracted designation operands, not evaluated runtime state. Multiple designations can be alternatives; missing entries are unresolved rather than assumed from the floor number.

```text
0x00, 0x00, 0x00, 0x00, 0x00
0x01, 0x01, 0x00, 0x00, 0x00
0x03, 0x03, 0x00, 0x00, 0x00
0x05, 0x05, 0x00, 0x00, 0x00
0x0C, 0x0C, 0x00, 0x00, 0x00
```

## Observed section IDs

| Floor slot | Room / section | Objects | Enemy/NPC records | Waves | Event IDs | Random locations |
|---:|---:|---:|---:|---|---|---:|
| 0 | 10 | 26 | 2 | 0 |  | 0 |
| 0 | 20 | 0 | 10 | 0 |  | 0 |
| 0 | 30 | 0 | 5 | 0 |  | 0 |
| 0 | 40 | 0 | 2 | 0 |  | 0 |
| 0 | 41 | 0 | 4 | 0 |  | 0 |
| 1 | 2 | 15 | 0 |  |  | 0 |
| 1 | 4 | 2 | 15 | 1, 2, 3 | 41, 411, 412 | 0 |
| 1 | 5 | 16 | 16 | 1, 2, 3, 4, 5 | 51, 52, 53, 511, 512 | 0 |
| 1 | 7 | 20 | 15 | 1, 2, 3 | 71, 711, 712 | 0 |
| 1 | 8 | 7 | 0 |  |  | 0 |
| 1 | 10 | 10 | 9 | 1, 2, 3 | 101, 1011, 1012 | 0 |
| 1 | 11 | 12 | 12 | 1, 2, 3, 4 | 111, 1111, 1112, 1113 | 0 |
| 1 | 16 | 28 | 0 |  |  | 0 |
| 3 | 1 | 1 | 0 |  |  | 0 |
| 3 | 2 | 1 | 0 |  |  | 0 |
| 3 | 3 | 3 | 0 |  |  | 0 |
| 3 | 4 | 2 | 0 |  |  | 0 |
| 3 | 5 | 39 | 0 |  |  | 0 |
| 3 | 6 | 9 | 0 |  |  | 0 |
| 3 | 7 | 11 | 0 |  |  | 0 |
| 3 | 8 | 2 | 0 |  |  | 0 |
| 3 | 10 | 7 | 9 | 1, 2 | 101, 1011 | 0 |
| 3 | 11 | 15 | 0 |  | 111, 112, 1121 | 0 |
| 3 | 20 | 30 | 6 | 1, 2, 3 | 201, 202, 2021 | 0 |
| 3 | 30 | 22 | 14 | 1, 2, 3 | 301, 3011, 3012 | 0 |
| 3 | 31 | 7 | 33 | 1, 2, 3, 4, 5, 6, 7 | 311, 3111, 3112, 3113, 3114, 3115, 3116 | 0 |
| 3 | 32 | 15 | 13 | 1, 2, 3 | 321, 3211, 3212 | 0 |
| 3 | 33 | 6 | 8 | 1, 2, 3, 4 | 331, 332, 3311, 3312 | 0 |
| 3 | 34 | 4 | 19 | 1, 2, 3 | 341, 3411, 3412 | 0 |
| 3 | 50 | 12 | 18 | 1, 2, 3 | 502, 5021, 5022 | 0 |
| 3 | 51 | 6 | 21 | 1, 2, 3, 4, 5 | 511, 5111, 5112, 5113, 5114 | 0 |
| 3 | 52 | 4 | 19 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17 | 521, 522, 523, 524, 5211, 5212, 5213, 5221, 5222, 5223, 5231, 5232, 5233, 5241, 5242, 5243, 5244 | 0 |
| 3 | 53 | 5 | 16 | 1, 2, 3, 4 | 531, 5311, 5312, 5313 | 0 |
| 3 | 60 | 12 | 29 | 1, 2, 3, 4, 5, 6, 7, 8 | 601, 6011, 6012, 6013, 6014, 6015, 6016, 6017 | 0 |
| 5 | 14 | 5 | 0 |  |  | 0 |
| 5 | 24 | 8 | 0 |  |  | 0 |
| 12 | 1 | 16 | 1 | 1 | 1 | 0 |
