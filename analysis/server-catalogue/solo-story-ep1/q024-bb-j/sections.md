# Recorded rooms / sections — ハンターの右腕

[Quest dossier](README.md) · [Section coverage guide](../../../map-sections/README.md)

These IDs are observed in this quest’s DAT placements/events/random-room records. They are not a complete list of geometric sections. Positions and facing are in the linked placement files; no section boundary has been inferred from those points.

[Enemy/NPC placements](enemies.csv) · [Object placements](objects.csv) · [Full map data](map.txt)

## Map designation evidence

These are extracted designation operands, not evaluated runtime state. Multiple designations can be alternatives; missing entries are unresolved rather than assumed from the floor number.

```text
0x00, 0x00, 0x00, 0x00, 0x00
0x08, 0x08, 0x00, 0x00, 0x00
0x09, 0x09, 0x00, 0x00, 0x00
```

## Observed section IDs

| Floor slot | Room / section | Objects | Enemy/NPC records | Waves | Event IDs | Random locations |
|---:|---:|---:|---:|---|---|---:|
| 0 | 10 | 26 | 1 | 0 |  | 0 |
| 0 | 20 | 0 | 10 | 0 |  | 0 |
| 0 | 30 | 0 | 5 | 0 |  | 0 |
| 0 | 40 | 0 | 2 | 0 |  | 0 |
| 8 | 1 | 27 | 0 |  |  | 0 |
| 8 | 2 | 8 | 0 |  |  | 0 |
| 8 | 3 | 2 | 0 |  |  | 0 |
| 8 | 4 | 2 | 0 |  |  | 0 |
| 8 | 5 | 6 | 0 |  |  | 0 |
| 8 | 6 | 2 | 0 |  |  | 0 |
| 8 | 7 | 8 | 0 |  |  | 0 |
| 8 | 8 | 2 | 0 |  |  | 0 |
| 8 | 9 | 1 | 0 |  |  | 0 |
| 8 | 10 | 6 | 0 |  |  | 0 |
| 8 | 11 | 8 | 0 |  |  | 0 |
| 8 | 20 | 7 | 6 | 1 | 201 | 0 |
| 8 | 21 | 4 | 5 | 1 | 211 | 0 |
| 8 | 22 | 8 | 4 | 1 | 221 | 0 |
| 8 | 23 | 9 | 8 | 1, 2 | 231, 2311 | 0 |
| 8 | 24 | 9 | 6 | 1 | 241 | 0 |
| 8 | 30 | 42 | 0 |  |  | 0 |
| 8 | 31 | 3 | 2 | 1 | 311 | 0 |
| 8 | 32 | 5 | 5 | 1 | 321 | 0 |
| 8 | 33 | 7 | 14 | 1, 2, 3 | 331, 3311, 3312 | 0 |
| 8 | 40 | 10 | 9 | 1 | 401 | 0 |
| 8 | 50 | 10 | 8 | 1 | 502 | 0 |
| 8 | 60 | 3 | 14 | 1, 2 | 601, 602 | 0 |
| 8 | 61 | 13 | 0 |  |  | 0 |
| 8 | 65 | 12 | 0 |  |  | 0 |
| 8 | 70 | 8 | 20 | 1, 2, 3 | 701, 7011, 7012 | 0 |
| 9 | 1 | 23 | 0 |  |  | 0 |
| 9 | 2 | 4 | 0 |  |  | 0 |
| 9 | 3 | 2 | 0 |  |  | 0 |
| 9 | 4 | 2 | 0 |  |  | 0 |
| 9 | 5 | 2 | 0 |  |  | 0 |
| 9 | 6 | 2 | 0 |  |  | 0 |
| 9 | 7 | 2 | 0 |  |  | 0 |
| 9 | 8 | 2 | 0 |  |  | 0 |
| 9 | 9 | 2 | 0 |  |  | 0 |
| 9 | 10 | 8 | 0 |  |  | 0 |
| 9 | 11 | 3 | 0 |  |  | 0 |
| 9 | 12 | 2 | 0 |  |  | 0 |
| 9 | 13 | 2 | 0 |  |  | 0 |
| 9 | 14 | 2 | 0 |  |  | 0 |
| 9 | 15 | 8 | 0 |  |  | 0 |
| 9 | 20 | 5 | 2 | 1 | 201 | 0 |
| 9 | 21 | 2 | 9 | 1, 2 | 211, 212 | 0 |
| 9 | 22 | 8 | 0 |  |  | 0 |
| 9 | 23 | 6 | 15 | 1, 2, 3 | 231, 2311, 2312 | 0 |
| 9 | 24 | 3 | 9 | 1, 2 | 241, 2411 | 0 |
| 9 | 30 | 6 | 6 | 1 | 301 | 0 |
| 9 | 31 | 7 | 12 | 1, 2, 3 | 311, 312, 3111 | 0 |
| 9 | 32 | 2 | 0 |  |  | 0 |
| 9 | 33 | 4 | 8 | 1, 2 | 331, 3311 | 0 |
| 9 | 40 | 5 | 8 | 1, 2 | 401, 4011 | 0 |
| 9 | 41 | 10 | 3 | 1, 2 | 411, 4111 | 0 |
| 9 | 42 | 4 | 4 | 1 | 421 | 0 |
| 9 | 43 | 8 | 0 |  |  | 0 |
| 9 | 44 | 6 | 11 | 1, 2 | 441, 4411 | 0 |
| 9 | 50 | 14 | 0 |  |  | 0 |
| 9 | 55 | 12 | 0 |  |  | 0 |
| 9 | 60 | 8 | 5 | 1 | 601 | 0 |
| 9 | 75 | 21 | 0 |  |  | 0 |
| 9 | 80 | 16 | 25 | 1, 2, 3, 4 | 801, 8011, 8012, 8013 | 0 |
