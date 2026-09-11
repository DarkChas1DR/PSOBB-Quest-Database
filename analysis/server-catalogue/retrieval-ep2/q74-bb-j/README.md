# Lost CHAOS CALIBUR — retrieval-ep2/q74-bb-j

Episode2; header quest ID 74; language J. Static scan: **478 objects, 523 enemy/NPC records, 111 events, 67 script labels.** Script roundtrip: byte-identical.

This is a structural dossier, not a claim that every branch has been manually interpreted or playtested. Enemy/NPC records are not gameplay kill totals. Event IDs, wave numbers, object groups and script labels are distinct namespaces.

## Read and inspect

- [Script with byte offsets and map references](<script-offsets.txt>)
- [Reassembly syntax with explicit labels](<script.txt>)
- [Complete placements and event actions](<map.txt>)
- [Every parsed wave and its next actions](<waves.csv>)
- [Object fields](<objects.csv>)
- [Enemy/NPC fields](<enemies.csv>)
- [Explicit script references, including handlers; not a complete dynamic call graph](<script-references.csv>)
- [State, timing and reward operation locations](<state-and-rewards.csv>)
- [Function/label index](<labels.csv>)

## Area designations

Operands: floor, area, type, layout variation, entities variation.

```text

```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 57 | 16 | 0 |
| 10 | 189 | 251 | 55 |
| 11 | 205 | 255 | 55 |
| 13 | 27 | 1 | 1 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 10 | 1 | 20 / 1 | 5 | 10 | trigger_event(11); stop |
| 10 | 11 | 20 / 2 | 5 | 30 | trigger_event(12); stop |
| 10 | 12 | 20 / 3 | 6 | 1 | set_switch(2); stop |
| 10 | 13 | 30 / 1 | 8 | 30 | set_switch(4); stop |
| 10 | 14 | 60 / 2 | 6 | 30 | trigger_event(15); stop |
| 10 | 15 | 60 / 3 | 5 | 120 | set_switch(5); stop |
| 10 | 16 | 30 / 4 | 6 | 30 | stop |
| 10 | 17 | 30 / 5 | 2 | 30 | set_switch(7); stop |
| 10 | 18 | 90 / 1 | 7 | 0 | trigger_event(19); stop |
| 10 | 19 | 90 / 2 | 3 | 0 | trigger_event(20); stop |
| 10 | 20 | 90 / 3 | 8 | 30 | trigger_event(21); stop |
| 10 | 21 | 90 / 4 | 5 | 30 | trigger_event(22); stop |
| 10 | 22 | 90 / 4 | 5 | 30 | trigger_event(23); stop |
| 10 | 23 | 90 / 5 | 5 | 30 | set_switch(8); stop |
| 10 | 24 | 263 / 1 | 1 | 120 | stop |
| 10 | 25 | 211 / 2 | 2 | 220 | stop |
| 10 | 26 | 61 / 1 | 6 | 30 | trigger_event(27); stop |
| 10 | 27 | 61 / 2 | 7 | 30 | set_switch(11); stop |
| 10 | 28 | 80 / 1 | 1 | 120 | trigger_event(29); stop |
| 10 | 29 | 80 / 2 | 5 | 1 | trigger_event(30); stop |
| 10 | 30 | 80 / 3 | 8 | 30 | trigger_event(31); stop |
| 10 | 31 | 80 / 4 | 8 | 30 | set_switch(12); stop |
| 10 | 32 | 5 / 4 | 0 | 60 | stop |
| 10 | 33 | 3 / 1 | 2 | 60 | stop |
| 10 | 34 | 70 / 1 | 4 | 0 | trigger_event(35); stop |
| 10 | 35 | 70 / 2 | 4 | 30 | trigger_event(36); stop |
| 10 | 36 | 70 / 3 | 8 | 30 | trigger_event(37); stop |
| 10 | 37 | 70 / 4 | 4 | 30 | set_switch(14); stop |
| 10 | 38 | 64 / 1 | 6 | 30 | trigger_event(39); stop |
| 10 | 39 | 64 / 2 | 7 | 30 | set_switch(15); stop |
| 10 | 40 | 64 / 8 | 0 | 1 | stop |
| 10 | 41 | 40 / 1 | 4 | 30 | set_switch(17); stop |
| 10 | 42 | 62 / 1 | 8 | 30 | stop |
| 10 | 43 | 280 / 1 | 1 | 30 | stop |
| 10 | 44 | 280 / 2 | 2 | 30 | stop |
| 10 | 45 | 62 / 2 | 4 | 30 | set_switch(18); stop |
| 10 | 46 | 71 / 1 | 8 | 30 | trigger_event(47); stop |
| 10 | 47 | 71 / 2 | 7 | 30 | trigger_event(48); stop |
| 10 | 48 | 71 / 3 | 6 | 30 | trigger_event(49); stop |
| 10 | 49 | 71 / 4 | 5 | 30 | trigger_event(50); stop |
| 10 | 50 | 71 / 5 | 4 | 30 | trigger_event(51); stop |
| 10 | 51 | 71 / 6 | 3 | 30 | set_switch(19); set_switch(20); stop |
| 10 | 53 | 206 / 1 | 2 | 30 | stop |
| 10 | 54 | 64 / 3 | 6 | 30 | set_switch(21); stop |
| 10 | 55 | 7 / 1 | 1 | 30 | stop |
| 10 | 56 | 8 / 1 | 1 | 30 | set_switch(22); stop |
| 10 | 57 | 63 / 1 | 8 | 30 | trigger_event(58); stop |
| 10 | 58 | 281 / 1 | 1 | 30 | set_switch(23); stop |
| 10 | 59 | 6 / 1 | 4 | 30 | stop |
| 10 | 60 | 21 / 1 | 8 | 30 | set_switch(24); stop |
| 10 | 61 | 81 / 1 | 6 | 1 | trigger_event(62); stop |
| 10 | 62 | 81 / 2 | 4 | 30 | trigger_event(63); stop |
| 10 | 63 | 81 / 3 | 4 | 30 | trigger_event(64); stop |
| 10 | 64 | 81 / 4 | 8 | 180 | set_switch(25); stop |
| 10 | 66 | 2 / 1 | 2 | 30 | stop |
| 11 | 1 | 50 / 1 | 6 | 30 | trigger_event(2); stop |
| 11 | 2 | 50 / 2 | 9 | 30 | set_switch(1); stop |
| 11 | 3 | 251 / 4 | 0 | 10 | stop |
| 11 | 4 | 2 / 1 | 3 | 1 | stop |
| 11 | 5 | 70 / 1 | 1 | 1 | trigger_event(6); stop |
| 11 | 6 | 70 / 2 | 2 | 30 | trigger_event(7); stop |
| 11 | 7 | 70 / 3 | 3 | 30 | trigger_event(8); stop |
| 11 | 8 | 70 / 4 | 7 | 30 | trigger_event(9); stop |
| 11 | 9 | 70 / 5 | 8 | 30 | trigger_event(10); stop |
| 11 | 10 | 70 / 6 | 0 | 30 | set_switch(3); stop |
| 11 | 11 | 50 / 3 | 5 | 30 | set_switch(4); stop |
| 11 | 12 | 80 / 1 | 22 | 1 | trigger_event(13); stop |
| 11 | 13 | 80 / 2 | 6 | 120 | trigger_event(14); stop |
| 11 | 14 | 80 / 3 | 10 | 30 | set_switch(5); stop |
| 11 | 15 | 210 / 1 | 1 | 30 | stop |
| 11 | 16 | 3 / 1 | 2 | 1 | stop |
| 11 | 17 | 7 / 1 | 1 | 1 | stop |
| 11 | 18 | 41 / 1 | 4 | 60 | set_switch(6); stop |
| 11 | 19 | 270 / 1 | 1 | 60 | set_switch(7); stop |
| 11 | 20 | 216 / 1 | 1 | 30 | set_switch(8); stop |
| 11 | 21 | 95 / 1 | 3 | 30 | stop |
| 11 | 22 | 95 / 2 | 3 | 30 | trigger_event(23); stop |
| 11 | 23 | 95 / 3 | 6 | 120 | trigger_event(24); stop |
| 11 | 24 | 95 / 4 | 5 | 60 | set_switch(9); stop |
| 11 | 26 | 3 / 1 | 2 | 1 | stop |
| 11 | 27 | 291 / 1 | 3 | 10 | trigger_event(28); stop |
| 11 | 28 | 291 / 2 | 3 | 90 | stop |
| 11 | 29 | 291 / 3 | 5 | 1 | set_switch(11); stop |
| 11 | 30 | 90 / 1 | 8 | 15 | set_switch(12); stop |
| 11 | 31 | 90 / 2 | 6 | 1 | stop |
| 11 | 32 | 90 / 3 | 6 | 30 | trigger_event(34); stop |
| 11 | 34 | 90 / 4 | 6 | 120 | set_switch(13); stop |
| 11 | 35 | 30 / 1 | 5 | 30 | stop |
| 11 | 36 | 30 / 2 | 5 | 30 | stop |
| 11 | 37 | 4 / 1 | 1 | 30 | trigger_event(38); stop |
| 11 | 38 | 4 / 2 | 2 | 15 | trigger_event(39); stop |
| 11 | 39 | 30 / 3 | 1 | 120 | stop |
| 11 | 40 | 71 / 1 | 7 | 10 | trigger_event(41); stop |
| 11 | 41 | 71 / 2 | 9 | 1 | trigger_event(57); stop |
| 11 | 57 | 71 / 3 | 8 | 30 | trigger_event(42); stop |
| 11 | 42 | 71 / 4 | 3 | 30 | set_switch(15); set_switch(16); stop |
| 11 | 43 | 31 / 1 | 3 | 30 | stop |
| 11 | 44 | 20 / 1 | 8 | 30 | trigger_event(45); stop |
| 11 | 45 | 20 / 2 | 3 | 30 | set_switch(19); set_switch(20); stop |
| 11 | 46 | 51 / 1 | 8 | 60 | set_switch(21); stop |
| 11 | 47 | 280 / 1 | 2 | 15 | stop |
| 11 | 48 | 81 / 1 | 9 | 30 | trigger_event(49); stop |
| 11 | 49 | 81 / 2 | 1 | 30 | trigger_event(50); stop |
| 11 | 50 | 81 / 3 | 8 | 120 | trigger_event(51); stop |
| 11 | 51 | 81 / 4 | 5 | 240 | set_switch(22); stop |
| 11 | 52 | 5 / 1 | 2 | 30 | stop |
| 11 | 53 | 52 / 1 | 5 | 120 | set_switch(23); stop |
| 11 | 54 | 290 / 1 | 8 | 30 | set_switch(24); stop |
| 11 | 55 | 6 / 1 | 2 | 180 | stop |
| 11 | 56 | 31 / 2 | 3 | 30 | stop |
| 13 | 1 | 0 / 1 | 1 | 0 | construct_objects(room=1,group_or_wave=1); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
