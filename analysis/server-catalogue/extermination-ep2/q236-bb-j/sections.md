# Recorded rooms / sections — 幻界の果てに ４

[Quest dossier](README.md) · [Section coverage guide](../../../map-sections/README.md)

These IDs are observed in this quest’s DAT placements/events/random-room records. They are not a complete list of geometric sections. Positions and facing are in the linked placement files; no section boundary has been inferred from those points.

[Enemy/NPC placements](enemies.csv) · [Object placements](objects.csv) · [Full map data](map.txt)

## Map designation evidence

These are extracted designation operands, not evaluated runtime state. Multiple designations can be alternatives; missing entries are unresolved rather than assumed from the floor number.

```text
0x00, 0x12, 0x00, 0x00, 0x00
0x11, 0x23, 0x00, 0x00, 0x00
0x10, 0x23, 0x00, 0x01, 0x00
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
| 16 | 1 | 45 | 5 | 1, 2 | 11, 111 | 0 |
| 16 | 2 | 29 | 7 | 1 | 21 | 0 |
| 16 | 3 | 18 | 10 | 1, 2, 3 | 33, 331, 332 | 0 |
| 16 | 4 | 11 | 10 | 1, 2 | 41, 411 | 0 |
| 16 | 5 | 30 | 13 | 1, 2, 3, 4, 5 | 51, 52, 511, 512, 513 | 0 |
| 16 | 10 | 21 | 13 | 1, 2, 3, 4 | 101, 1011, 1012, 1013 | 0 |
| 16 | 20 | 21 | 7 | 1, 2, 3, 4 | 201, 202, 203, 2011 | 0 |
| 16 | 21 | 29 | 8 | 1, 2, 3 | 211, 2111, 2112 | 0 |
| 16 | 22 | 15 | 7 | 1, 2, 3, 4 | 221, 2211, 2212, 2213 | 0 |
| 16 | 30 | 11 | 59 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30 | 301, 302, 303, 3011, 3012, 3013, 3014, 3015, 3016, 3017, 3018, 3019, 3021, 3022, 3023, 3024, 3025, 3026, 3027, 3028, 3029, 3031, 3032, 3033, 3034, 3035, 30111, 30112, 30211, 30212 | 0 |
| 17 | 1 | 54 | 5 | 1, 2, 3, 4 | 11, 111, 112, 113 | 0 |
| 17 | 2 | 21 | 5 | 1, 2 | 21, 215 | 0 |
| 17 | 3 | 10 | 9 | 1, 2, 3 | 31, 311, 312 | 0 |
| 17 | 4 | 34 | 5 | 1, 2 | 41, 42 | 0 |
| 17 | 5 | 42 | 5 | 1, 2, 3 | 51, 52, 53 | 0 |
| 17 | 10 | 14 | 9 | 1, 2, 3 | 101, 1011, 1012 | 0 |
| 17 | 20 | 22 | 7 | 1 | 201 | 0 |
| 17 | 21 | 10 | 8 | 1, 2 | 211, 2111 | 0 |
| 17 | 22 | 33 | 6 | 1, 2 | 221, 2211 | 0 |
| 17 | 30 | 12 | 44 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 | 301, 302, 303, 3011, 3012, 3013, 3014, 3015, 3016, 3017, 3021, 3022, 3023, 3024, 3025, 3026, 3027, 3031, 3032, 3033 | 0 |
