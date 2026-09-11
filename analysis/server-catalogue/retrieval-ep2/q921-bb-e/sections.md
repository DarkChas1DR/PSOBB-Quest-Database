# Recorded rooms / sections — Lost RIOT Raygun

[Quest dossier](README.md) · [Section coverage guide](../../../map-sections/README.md)

These IDs are observed in this quest’s DAT placements/events/random-room records. They are not a complete list of geometric sections. Positions and facing are in the linked placement files; no section boundary has been inferred from those points.

[Enemy/NPC placements](enemies.csv) · [Object placements](objects.csv) · [Full map data](map.txt)

## Map designation evidence

These are extracted designation operands, not evaluated runtime state. Multiple designations can be alternatives; missing entries are unresolved rather than assumed from the floor number.

```text
0x00, 0x12, 0x00, 0x00, 0x00
0x03, 0x15, 0x00, 0x00, 0x00
0x04, 0x16, 0x00, 0x00, 0x00
0x0F, 0x21, 0x00, 0x00, 0x00
```

## Observed section IDs

| Floor slot | Room / section | Objects | Enemy/NPC records | Waves | Event IDs | Random locations |
|---:|---:|---:|---:|---|---|---:|
| 0 | 0 | 1 | 0 |  |  | 0 |
| 0 | 10 | 23 | 1 | 0 |  | 0 |
| 0 | 20 | 2 | 0 |  |  | 0 |
| 0 | 30 | 12 | 11 | 0 |  | 0 |
| 0 | 40 | 2 | 0 |  |  | 0 |
| 0 | 42 | 13 | 2 | 0 |  | 0 |
| 0 | 50 | 1 | 0 |  |  | 0 |
| 0 | 70 | 3 | 2 | 0 |  | 0 |
| 3 | 1 | 15 | 0 |  |  | 0 |
| 3 | 2 | 4 | 0 |  |  | 0 |
| 3 | 3 | 2 | 0 |  |  | 0 |
| 3 | 4 | 3 | 0 |  |  | 0 |
| 3 | 5 | 3 | 0 |  |  | 0 |
| 3 | 6 | 2 | 0 |  |  | 0 |
| 3 | 7 | 4 | 0 |  |  | 0 |
| 3 | 8 | 4 | 0 |  |  | 0 |
| 3 | 10 | 7 | 10 | 1, 2 | 101, 1011 | 0 |
| 3 | 11 | 1 | 18 | 1, 2, 3 | 111, 1111, 1112 | 0 |
| 3 | 20 | 5 | 21 | 1, 2, 3 | 201, 2011, 2012 | 0 |
| 3 | 21 | 12 | 14 | 1, 2, 3 | 211, 2111, 2112, 2113 | 0 |
| 3 | 30 | 9 | 10 | 1, 2 | 301, 3011 | 0 |
| 3 | 31 | 3 | 2 | 1 | 311 | 0 |
| 3 | 32 | 8 | 7 | 1 | 321 | 0 |
| 3 | 33 | 17 | 1 | 1 | 330 | 0 |
| 3 | 40 | 20 | 13 | 1, 2, 4, 5 | 401, 402, 4011, 4100 | 0 |
| 3 | 41 | 7 | 15 | 1, 2, 3 | 411, 4111, 4112 | 0 |
| 3 | 42 | 16 | 23 | 1, 2, 3, 4 | 421, 4211, 4212, 4213 | 0 |
| 3 | 50 | 3 | 12 | 1, 2 | 501, 5011 | 0 |
| 3 | 51 | 5 | 17 | 1, 2 | 511, 5111 | 0 |
| 3 | 52 | 4 | 41 | 1, 2, 3, 4, 5 | 521, 5211, 5212, 5213, 5214 | 0 |
| 3 | 101 | 0 | 1 | 1 | 4101 | 0 |
| 3 | 102 | 0 | 1 | 1 | 5102 | 0 |
| 3 | 160 | 5 | 0 |  |  | 0 |
| 4 | 1 | 2 | 0 |  |  | 0 |
| 4 | 2 | 2 | 0 |  |  | 0 |
| 4 | 3 | 2 | 0 |  |  | 0 |
| 4 | 4 | 2 | 0 |  |  | 0 |
| 4 | 5 | 16 | 0 |  |  | 0 |
| 4 | 6 | 4 | 0 |  |  | 0 |
| 4 | 7 | 2 | 0 |  |  | 0 |
| 4 | 8 | 3 | 0 |  |  | 0 |
| 4 | 10 | 13 | 11 | 1, 2 | 101, 1011 | 0 |
| 4 | 11 | 22 | 0 |  |  | 0 |
| 4 | 12 | 7 | 14 | 1, 2 | 121, 1211 | 0 |
| 4 | 20 | 7 | 10 | 1, 2 | 201, 2011 | 0 |
| 4 | 21 | 6 | 18 | 1, 2 | 211, 2111 | 0 |
| 4 | 30 | 13 | 9 | 1 | 301 | 0 |
| 4 | 31 | 2 | 8 | 1, 2 | 311, 3111 | 0 |
| 4 | 40 | 9 | 31 | 1, 2, 3, 4 | 401, 4011, 4012, 4013 | 0 |
| 4 | 41 | 2 | 28 | 1, 2, 3, 4, 5, 6, 7 | 411, 4111, 4112, 4113, 4114, 4115, 4116 | 0 |
| 4 | 42 | 3 | 9 | 1 | 421, 422, 4211 | 0 |
| 4 | 50 | 20 | 7 | 1, 2 | 501, 502 | 0 |
| 4 | 51 | 11 | 24 | 1, 2, 3 | 511, 5111, 5112 | 0 |
| 4 | 52 | 16 | 25 | 1, 2, 3 | 521, 5211, 5212 | 0 |
| 4 | 160 | 2 | 0 |  |  | 0 |
| 4 | 161 | 1 | 4 | 1 | 1611 | 0 |
| 4 | 180 | 5 | 0 |  |  | 0 |
| 15 | 1 | 22 | 1 | 1 | 1 | 0 |
