# Recorded rooms / sections — ２－１：灼熱の洞窟

[Quest dossier](README.md) · [Section coverage guide](../../../map-sections/README.md)

These IDs are observed in this quest’s DAT placements/events/random-room records. They are not a complete list of geometric sections. Positions and facing are in the linked placement files; no section boundary has been inferred from those points.

[Enemy/NPC placements](enemies.csv) · [Object placements](objects.csv) · [Full map data](map.txt)

## Map designation evidence

These are extracted designation operands, not evaluated runtime state. Multiple designations can be alternatives; missing entries are unresolved rather than assumed from the floor number.

```text
0x00, 0x00, 0x00, 0x00, 0x00
0x03, 0x03, 0x00, 0x00, 0x00
0x04, 0x03, 0x00, 0x01, 0x00
```

## Observed section IDs

| Floor slot | Room / section | Objects | Enemy/NPC records | Waves | Event IDs | Random locations |
|---:|---:|---:|---:|---|---|---:|
| 0 | 10 | 27 | 0 |  |  | 0 |
| 0 | 20 | 0 | 8 | 0 |  | 0 |
| 0 | 30 | 0 | 5 | 0 |  | 0 |
| 0 | 40 | 0 | 2 | 0 |  | 0 |
| 0 | 41 | 0 | 5 | 0 |  | 0 |
| 3 | 1 | 1 | 0 |  |  | 0 |
| 3 | 2 | 1 | 0 |  |  | 0 |
| 3 | 3 | 1 | 0 |  |  | 0 |
| 3 | 4 | 1 | 0 |  |  | 0 |
| 3 | 5 | 24 | 0 |  |  | 0 |
| 3 | 6 | 5 | 0 |  |  | 0 |
| 3 | 7 | 2 | 0 |  |  | 0 |
| 3 | 8 | 1 | 0 |  |  | 0 |
| 3 | 10 | 7 | 7 | 1, 2 | 101, 1011 | 0 |
| 3 | 11 | 16 | 8 | 1, 2, 3 | 112, 113, 1111 | 0 |
| 3 | 20 | 17 | 3 | 1, 2 | 201, 202 | 0 |
| 3 | 30 | 22 | 0 |  |  | 0 |
| 3 | 31 | 14 | 0 |  |  | 0 |
| 3 | 32 | 2 | 14 | 1, 2, 3 | 321, 3211, 3212 | 0 |
| 3 | 33 | 5 | 13 | 1, 2 | 331, 3311 | 0 |
| 3 | 34 | 8 | 20 | 1, 2, 3 | 341, 3411, 3412 | 0 |
| 3 | 50 | 8 | 19 | 1, 2, 3, 4 | 501, 502, 5021, 5022 | 0 |
| 3 | 51 | 1 | 19 | 1, 2, 3, 4, 5 | 511, 5111, 5112, 5113, 5114 | 0 |
| 3 | 52 | 4 | 16 | 1, 2, 3, 4 | 521, 5211, 5212, 5213 | 0 |
| 3 | 53 | 2 | 18 | 1, 2, 3, 4 | 531, 5311, 5312, 5313 | 0 |
| 3 | 60 | 12 | 23 | 1, 2, 3, 4 | 601, 6011, 6012, 6013 | 0 |
| 4 | 5 | 9 | 0 |  |  | 0 |
| 4 | 11 | 8 | 5 | 1 | 111 | 0 |
| 4 | 20 | 16 | 0 |  |  | 0 |
| 4 | 34 | 17 | 0 |  |  | 0 |
| 4 | 52 | 6 | 42 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 | 521, 522, 523, 5211, 5212, 5213, 5221, 5222, 5223, 5231, 5232 | 0 |
