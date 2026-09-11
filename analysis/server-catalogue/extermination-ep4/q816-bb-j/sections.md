# Recorded rooms / sections — 新掃討作戦 第一号

[Quest dossier](README.md) · [Section coverage guide](../../../map-sections/README.md)

These IDs are observed in this quest’s DAT placements/events/random-room records. They are not a complete list of geometric sections. Positions and facing are in the linked placement files; no section boundary has been inferred from those points.

[Enemy/NPC placements](enemies.csv) · [Object placements](objects.csv) · [Full map data](map.txt)

## Map designation evidence

These are extracted designation operands, not evaluated runtime state. Multiple designations can be alternatives; missing entries are unresolved rather than assumed from the floor number.

```text
0x00, 0x2D, 0x00, 0x00, 0x00
0x01, 0x24, 0x00, 0x00, 0x00
```

## Observed section IDs

| Floor slot | Room / section | Objects | Enemy/NPC records | Waves | Event IDs | Random locations |
|---:|---:|---:|---:|---|---|---:|
| 0 | 10 | 26 | 2 | 0 |  | 0 |
| 0 | 20 | 0 | 8 | 0 |  | 0 |
| 0 | 30 | 0 | 5 | 0 |  | 0 |
| 0 | 40 | 0 | 2 | 0 |  | 0 |
| 1 | 10 | 23 | 24 | 1, 2, 3, 4, 5, 6, 7, 8, 9 | 101, 102, 103, 104, 105, 106, 107, 108, 109 | 0 |
| 1 | 11 | 26 | 10 | 1, 2, 3 | 111, 112, 113 | 0 |
| 1 | 20 | 37 | 27 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 | 201, 202, 203, 204, 205, 206, 207, 208, 209, 2010 | 0 |
| 1 | 30 | 16 | 25 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 | 301, 302, 303, 304, 305, 306, 307, 308, 309, 3010 | 0 |
| 1 | 40 | 27 | 30 | 1, 2, 3, 4, 5, 6 | 401, 402, 4011, 4012, 4021, 4022 | 0 |
| 1 | 50 | 34 | 21 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 501, 5001, 5002, 5003, 5011, 5012, 5013, 5021, 5022, 5023, 5031, 5032, 5033, 5041, 5042, 5043 | 0 |
| 1 | 60 | 40 | 14 | 1, 2, 3, 4, 5, 6 | 601, 602, 603, 604, 605, 6011, 6012 | 0 |
