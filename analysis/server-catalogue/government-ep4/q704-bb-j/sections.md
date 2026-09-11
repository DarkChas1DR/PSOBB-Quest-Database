# Recorded rooms / sections — ９－４：追跡

[Quest dossier](README.md) · [Section coverage guide](../../../map-sections/README.md)

These IDs are observed in this quest’s DAT placements/events/random-room records. They are not a complete list of geometric sections. Positions and facing are in the linked placement files; no section boundary has been inferred from those points.

[Enemy/NPC placements](enemies.csv) · [Object placements](objects.csv) · [Full map data](map.txt)

## Map designation evidence

These are extracted designation operands, not evaluated runtime state. Multiple designations can be alternatives; missing entries are unresolved rather than assumed from the floor number.

```text
0x00, 0x2D, 0x00, 0x00, 0x00
0x04, 0x27, 0x00, 0x00, 0x00
0x05, 0x28, 0x00, 0x00, 0x00
```

## Observed section IDs

| Floor slot | Room / section | Objects | Enemy/NPC records | Waves | Event IDs | Random locations |
|---:|---:|---:|---:|---|---|---:|
| 0 | 10 | 27 | 0 |  |  | 0 |
| 0 | 20 | 0 | 8 | 0 |  | 0 |
| 0 | 30 | 0 | 5 | 0 |  | 0 |
| 0 | 40 | 0 | 2 | 0 |  | 0 |
| 0 | 41 | 0 | 5 | 0 |  | 0 |
| 4 | 22 | 60 | 36 | 1, 2, 3, 4, 5, 6, 7 | 221, 222, 2211, 2212, 2213, 2221, 2222 | 0 |
| 4 | 41 | 21 | 32 | 0, 1, 2, 3, 4, 5, 6 | 411, 412, 4111, 4112, 4121, 4122 | 0 |
| 4 | 60 | 38 | 41 | 0, 1, 2, 3, 4, 5, 6, 7 | 601, 6011, 6012, 6013, 6014, 6015, 6016 | 0 |
| 4 | 81 | 23 | 2 | 0, 1 | 811 | 0 |
| 5 | 10 | 20 | 35 | 0, 1, 2, 3 | 101, 1011, 1012 | 0 |
| 5 | 20 | 18 | 21 | 1, 2, 3 | 201, 2011, 2012 | 0 |
| 5 | 30 | 12 | 25 | 1, 2, 3, 4 | 301, 3011, 3012, 3013 | 0 |
| 5 | 40 | 14 | 19 | 1, 2, 3 | 401, 4011, 4012 | 0 |
| 5 | 50 | 9 | 21 | 1, 2, 3, 4 | 501, 5011, 5012, 5013 | 0 |
| 5 | 60 | 41 | 27 | 1, 2, 3, 4, 5 | 601, 6011, 6012, 6013, 6014, 6015 | 0 |
