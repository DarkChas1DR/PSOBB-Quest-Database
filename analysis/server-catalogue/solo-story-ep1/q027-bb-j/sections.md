# Recorded rooms / sections — 心の座

[Quest dossier](README.md) · [Section coverage guide](../../../map-sections/README.md)

These IDs are observed in this quest’s DAT placements/events/random-room records. They are not a complete list of geometric sections. Positions and facing are in the linked placement files; no section boundary has been inferred from those points.

[Enemy/NPC placements](enemies.csv) · [Object placements](objects.csv) · [Full map data](map.txt)

## Map designation evidence

These are extracted designation operands, not evaluated runtime state. Multiple designations can be alternatives; missing entries are unresolved rather than assumed from the floor number.

```text
0x00, 0x12, 0x00, 0x00, 0x00
0x02, 0x14, 0x00, 0x01, 0x00
0x04, 0x16, 0x00, 0x00, 0x00
0x05, 0x17, 0x00, 0x00, 0x00
0x10, 0x22, 0x00, 0x00, 0x00
0x11, 0x23, 0x00, 0x00, 0x00
0x0F, 0x21, 0x00, 0x00, 0x00
```

## Observed section IDs

| Floor slot | Room / section | Objects | Enemy/NPC records | Waves | Event IDs | Random locations |
|---:|---:|---:|---:|---|---|---:|
| 0 | 10 | 17 | 5 | 0 |  | 0 |
| 0 | 20 | 2 | 0 |  |  | 0 |
| 0 | 30 | 12 | 10 | 0 |  | 0 |
| 0 | 40 | 7 | 3 | 0 |  | 0 |
| 0 | 42 | 11 | 5 | 0 |  | 0 |
| 0 | 50 | 2 | 0 |  |  | 0 |
| 0 | 70 | 16 | 3 | 0 |  | 0 |
| 2 | 1 | 18 | 0 |  |  | 0 |
| 2 | 4 | 8 | 0 |  |  | 0 |
| 2 | 10 | 9 | 12 | 1, 2, 3 | 101, 1011, 1012 | 0 |
| 2 | 11 | 14 | 9 | 1, 2, 3 | 111, 1111, 1112 | 0 |
| 2 | 30 | 10 | 1 | 1 | 301 | 0 |
| 2 | 41 | 21 | 10 | 1, 2, 3 | 411, 4111, 4112 | 0 |
| 2 | 50 | 9 | 8 | 1, 2, 3 | 501, 502, 5011, 5012 | 0 |
| 2 | 61 | 17 | 2 | 1 | 611 | 0 |
| 2 | 70 | 30 | 8 | 1, 2, 3 | 701, 702, 7011 | 0 |
| 2 | 91 | 8 | 4 | 1 | 911 | 0 |
| 2 | 92 | 0 | 3 | 1 | 921 | 0 |
| 2 | 93 | 8 | 4 | 1 | 931 | 0 |
| 2 | 161 | 4 | 0 |  |  | 0 |
| 4 | 3 | 24 | 0 |  |  | 0 |
| 4 | 4 | 3 | 0 |  |  | 0 |
| 4 | 10 | 6 | 5 | 1, 2 | 101, 1011 | 0 |
| 4 | 11 | 7 | 0 |  |  | 0 |
| 4 | 12 | 19 | 1 | 1 | 121 | 0 |
| 4 | 30 | 10 | 20 | 1, 2, 3, 4, 5 | 301, 3011, 3012, 3013, 3014 | 0 |
| 4 | 40 | 21 | 9 | 1, 2 | 401, 4011 | 0 |
| 4 | 41 | 13 | 9 | 1 | 411 | 0 |
| 4 | 50 | 20 | 5 | 1 | 501 | 0 |
| 4 | 52 | 20 | 11 | 1, 2 | 521, 5211 | 0 |
| 4 | 161 | 0 | 2 | 1 | 1611 | 0 |
| 4 | 181 | 0 | 2 | 1 | 1811 | 0 |
| 5 | 1 | 32 | 0 |  |  | 0 |
| 5 | 2 | 1 | 5 | 1, 2 | 21, 211 | 0 |
| 5 | 3 | 7 | 8 | 1, 2 | 31, 311 | 0 |
| 5 | 4 | 13 | 12 | 1, 2, 3 | 41, 411, 412 | 0 |
| 5 | 5 | 3 | 0 |  |  | 0 |
| 5 | 6 | 0 | 2 | 1 | 61 | 0 |
| 5 | 7 | 3 | 0 |  |  | 0 |
| 5 | 8 | 22 | 10 | 1, 2, 3 | 81, 811, 812 | 0 |
| 5 | 9 | 18 | 9 | 1, 2 | 91, 911, 912 | 0 |
| 5 | 10 | 32 | 1 | 1 | 101 | 0 |
| 15 | 1 | 6 | 1 | 1 | 1 | 0 |
| 16 | 1 | 8 | 0 |  |  | 0 |
| 16 | 5 | 21 | 0 |  |  | 0 |
| 17 | 1 | 40 | 7 | 1, 2, 3 |  | 0 |
| 17 | 3 | 50 | 9 | 1, 2, 3, 4, 5 |  | 0 |
| 17 | 20 | 35 | 8 | 1, 2, 3, 4, 5 | 201 | 0 |
| 17 | 21 | 31 | 4 | 1, 2, 3, 4 |  | 0 |
| 17 | 22 | 62 | 7 | 1, 2, 3, 4, 5, 6, 7 |  | 0 |
| 17 | 30 | 6 | 5 | 1, 2, 3 | 301, 302, 303 | 0 |
