# Recorded rooms / sections — 9-2:Data Retrieval

[Quest dossier](README.md) · [Section coverage guide](../../../map-sections/README.md)

These IDs are observed in this quest’s DAT placements/events/random-room records. They are not a complete list of geometric sections. Positions and facing are in the linked placement files; no section boundary has been inferred from those points.

[Enemy/NPC placements](enemies.csv) · [Object placements](objects.csv) · [Full map data](map.txt)

## Map designation evidence

These are extracted designation operands, not evaluated runtime state. Multiple designations can be alternatives; missing entries are unresolved rather than assumed from the floor number.

```text
0x00, 0x2D, 0x00, 0x00, 0x00
0x02, 0x25, 0x00, 0x00, 0x00
```

## Observed section IDs

| Floor slot | Room / section | Objects | Enemy/NPC records | Waves | Event IDs | Random locations |
|---:|---:|---:|---:|---|---|---:|
| 0 | 10 | 27 | 0 |  |  | 0 |
| 0 | 20 | 0 | 8 | 0 |  | 0 |
| 0 | 30 | 0 | 5 | 0 |  | 0 |
| 0 | 40 | 0 | 2 | 0 |  | 0 |
| 0 | 41 | 0 | 5 | 0 |  | 0 |
| 2 | 10 | 45 | 16 | 0, 1, 2, 3 | 101, 102, 103 | 0 |
| 2 | 20 | 36 | 52 | 0, 1, 2, 3, 4, 5, 6, 7, 8 | 201, 2011, 2012, 2013, 2014, 2015, 2016, 2017 | 0 |
| 2 | 30 | 50 | 39 | 0, 1, 2, 3, 4, 5, 6, 7 | 301, 302, 303, 304, 305, 306, 307 | 0 |
| 2 | 40 | 32 | 31 | 1, 2, 3, 4, 5, 6 | 401, 402, 403, 404, 405, 406 | 0 |
| 2 | 50 | 65 | 45 | 0, 1, 2, 3, 4, 5, 6, 7, 8 | 501, 502, 503, 504, 505, 506, 507, 508 | 0 |
| 2 | 60 | 57 | 24 | 1, 2, 3, 4, 5 | 601, 602, 603, 604, 605 | 0 |
