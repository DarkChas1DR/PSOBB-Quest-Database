# Den of the Damned — events-ep2/q83-bb-j

Episode2; header quest ID 83; language J. Static scan: **1006 objects, 1121 enemy/NPC records, 245 events, 409 script labels.** Script roundtrip: byte-identical.

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
| 0 | 48 | 17 | 0 |
| 5 | 80 | 113 | 19 |
| 6 | 168 | 229 | 49 |
| 7 | 106 | 168 | 29 |
| 8 | 241 | 254 | 71 |
| 9 | 350 | 285 | 62 |
| 12 | 13 | 55 | 15 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 5 | 1 | 7 / 1 | 3 | 32 | stop |
| 5 | 81 | 8 / 1 | 4 | 20 | trigger_event(32); stop |
| 5 | 82 | 8 / 2 | 6 | 20 | trigger_event(33); stop |
| 5 | 83 | 8 / 3 | 3 | 20 | set_switch(3); stop |
| 5 | 31 | 3 / 1 | 4 | 20 | trigger_event(82); stop |
| 5 | 32 | 3 / 2 | 2 | 20 | trigger_event(83); stop |
| 5 | 33 | 3 / 3 | 5 | 20 | set_switch(8); stop |
| 5 | 91 | 9 / 1 | 6 | 20 | trigger_event(42); stop |
| 5 | 92 | 9 / 2 | 8 | 20 | trigger_event(43); stop |
| 5 | 93 | 9 / 3 | 5 | 20 | set_switch(4); stop |
| 5 | 41 | 4 / 1 | 6 | 20 | trigger_event(92); stop |
| 5 | 42 | 4 / 2 | 9 | 20 | trigger_event(93); stop |
| 5 | 43 | 4 / 3 | 8 | 20 | set_switch(9); stop |
| 5 | 101 | 10 / 1 | 6 | 20 | trigger_event(52); stop |
| 5 | 102 | 10 / 2 | 9 | 20 | trigger_event(53); stop |
| 5 | 103 | 10 / 3 | 9 | 20 | set_switch(7); stop |
| 5 | 51 | 5 / 1 | 6 | 20 | trigger_event(102); stop |
| 5 | 52 | 5 / 2 | 9 | 20 | trigger_event(103); stop |
| 5 | 53 | 5 / 3 | 5 | 20 | set_switch(7); stop |
| 6 | 1 | 13 / 1 | 4 | 10 | trigger_event(2); stop |
| 6 | 2 | 13 / 2 | 6 | 10 | trigger_event(3); stop |
| 6 | 3 | 13 / 3 | 7 | 20 | set_switch(1); trigger_event(4); trigger_event(26); trigger_event(38); stop |
| 6 | 4 | 10 / 1 | 4 | 3 | stop |
| 6 | 5 | 10 / 2 | 1 | 20 | set_switch(2); stop |
| 6 | 6 | 8 / 1 | 4 | 65 | trigger_event(7); trigger_event(9); stop |
| 6 | 7 | 8 / 2 | 1 | 25 | trigger_event(8); stop |
| 6 | 8 | 8 / 3 | 2 | 3 | stop |
| 6 | 9 | 8 / 4 | 5 | 300 | stop |
| 6 | 10 | 8 / 5 | 5 | 40 | stop |
| 6 | 11 | 4 / 1 | 6 | 10 | trigger_event(12); stop |
| 6 | 12 | 4 / 2 | 5 | 50 | trigger_event(13); stop |
| 6 | 13 | 4 / 3 | 4 | 10 | trigger_event(14); stop |
| 6 | 14 | 4 / 4 | 8 | 10 | set_switch(5); stop |
| 6 | 150 | 7 / 0 | 0 | 3 | trigger_event(15); trigger_event(19); stop |
| 6 | 15 | 7 / 1 | 4 | 3 | trigger_event(16); stop |
| 6 | 16 | 7 / 2 | 3 | 3 | trigger_event(17); stop |
| 6 | 17 | 7 / 3 | 8 | 15 | trigger_event(18); stop |
| 6 | 18 | 7 / 4 | 1 | 30 | set_switch(6); stop |
| 6 | 19 | 7 / 10 | 2 | 3 | trigger_event(20); stop |
| 6 | 20 | 7 / 9 | 7 | 3 | stop |
| 6 | 21 | 2 / 1 | 2 | 2 | stop |
| 6 | 210 | 2 / 2 | 5 | 3 | stop |
| 6 | 22 | 1 / 1 | 5 | 10 | stop |
| 6 | 23 | 1 / 2 | 11 | 3 | trigger_event(24); stop |
| 6 | 24 | 1 / 3 | 11 | 8 | trigger_event(25); stop |
| 6 | 25 | 1 / 4 | 2 | 25 | construct_objects(room=1,group_or_wave=1); construct_objects(room=3,group_or_wave=1); construct_objects(room=13,group_or_wave=1); trigger_event(210); trigger_event(34); stop |
| 6 | 26 | 9 / 1 | 4 | 3 | stop |
| 6 | 27 | 9 / 2 | 1 | 40 | trigger_event(28); trigger_event(29); stop |
| 6 | 28 | 9 / 3 | 4 | 3 | stop |
| 6 | 29 | 9 / 4 | 1 | 45 | set_switch(12); stop |
| 6 | 300 | 3 / 0 | 0 | 3 | trigger_event(30); stop |
| 6 | 30 | 3 / 1 | 4 | 20 | trigger_event(31); stop |
| 6 | 31 | 3 / 2 | 9 | 20 | trigger_event(32); stop |
| 6 | 32 | 3 / 3 | 12 | 10 | trigger_event(33); stop |
| 6 | 33 | 3 / 4 | 2 | 3 | set_switch(7); stop |
| 6 | 34 | 13 / 4 | 8 | 150 | trigger_event(35); trigger_event(37); stop |
| 6 | 35 | 13 / 5 | 7 | 10 | trigger_event(36); stop |
| 6 | 36 | 13 / 6 | 6 | 25 | stop |
| 6 | 37 | 13 / 7 | 7 | 50 | stop |
| 6 | 340 | 13 / 10 | 2 | 90 | trigger_event(341); stop |
| 6 | 341 | 13 / 9 | 1 | 90 | stop |
| 6 | 38 | 12 / 1 | 3 | 3 | stop |
| 6 | 39 | 12 / 2 | 2 | 60 | stop |
| 6 | 40 | 11 / 1 | 4 | 100 | trigger_event(41); stop |
| 6 | 41 | 11 / 2 | 10 | 10 | trigger_event(42); stop |
| 6 | 42 | 11 / 3 | 6 | 30 | trigger_event(43); stop |
| 6 | 43 | 11 / 4 | 10 | 5 | set_switch(20); construct_objects(room=4,group_or_wave=1); stop |
| 6 | 45 | 6 / 1 | 3 | 11 | stop |
| 7 | 1 | 2 / 1 | 12 | 65 | trigger_event(2); stop |
| 7 | 2 | 2 / 2 | 2 | 15 | trigger_event(3); stop |
| 7 | 3 | 2 / 3 | 9 | 15 | trigger_event(4); set_switch(1); stop |
| 7 | 4 | 1 / 1 | 1 | 45 | trigger_event(6); stop |
| 7 | 5 | 1 / 2 | 2 | 12 | stop |
| 7 | 6 | 1 / 3 | 8 | 10 | set_switch(2); stop |
| 7 | 7 | 7 / 1 | 1 | 8 | trigger_event(8); stop |
| 7 | 8 | 7 / 2 | 3 | 5 | trigger_event(9); stop |
| 7 | 9 | 7 / 3 | 2 | 3 | trigger_event(10); stop |
| 7 | 10 | 7 / 4 | 1 | 9 | trigger_event(11); stop |
| 7 | 11 | 7 / 5 | 5 | 10 | stop |
| 7 | 16 | 3 / 1 | 1 | 3 | trigger_event(17); stop |
| 7 | 17 | 3 / 2 | 12 | 20 | trigger_event(18); stop |
| 7 | 18 | 3 / 3 | 4 | 10 | trigger_event(19); stop |
| 7 | 19 | 3 / 4 | 2 | 20 | set_switch(3); stop |
| 7 | 20 | 5 / 1 | 7 | 20 | trigger_event(22); stop |
| 7 | 21 | 5 / 2 | 5 | 220 | trigger_event(23); stop |
| 7 | 22 | 5 / 3 | 2 | 15 | trigger_event(24); stop |
| 7 | 23 | 5 / 4 | 12 | 40 | trigger_event(25); stop |
| 7 | 24 | 5 / 5 | 8 | 20 | trigger_event(26); stop |
| 7 | 25 | 5 / 6 | 9 | 20 | trigger_event(27); stop |
| 7 | 26 | 5 / 7 | 3 | 25 | trigger_event(28); stop |
| 7 | 27 | 5 / 8 | 2 | 40 | stop |
| 7 | 28 | 5 / 9 | 3 | 50 | set_switch(4); stop |
| 7 | 30 | 8 / 1 | 4 | 3 | trigger_event(31); stop |
| 7 | 31 | 8 / 2 | 9 | 8 | trigger_event(32); stop |
| 7 | 32 | 8 / 3 | 2 | 25 | trigger_event(33); stop |
| 7 | 33 | 8 / 4 | 14 | 20 | trigger_event(34); stop |
| 7 | 34 | 8 / 5 | 7 | 25 | construct_objects(room=8,group_or_wave=1); stop |
| 8 | 1 | 5 / 1 | 4 | 60 | trigger_event(2); stop |
| 8 | 2 | 5 / 2 | 6 | 15 | trigger_event(3); stop |
| 8 | 3 | 5 / 3 | 5 | 10 | set_switch(1); stop |
| 8 | 40 | 5 / 0 | 0 | 3 | trigger_event(4); trigger_event(5); stop |
| 8 | 4 | 5 / 4 | 3 | 20 | trigger_event(6); stop |
| 8 | 5 | 5 / 5 | 1 | 20 | trigger_event(7); stop |
| 8 | 6 | 5 / 6 | 4 | 10 | set_switch(2); stop |
| 8 | 7 | 5 / 7 | 5 | 20 | set_switch(2); stop |
| 8 | 80 | 5 / 0 | 0 | 80 | trigger_event(8); trigger_event(9); trigger_event(10); stop |
| 8 | 8 | 5 / 8 | 1 | 3 | trigger_event(11); stop |
| 8 | 9 | 5 / 9 | 1 | 3 | trigger_event(12); stop |
| 8 | 10 | 5 / 10 | 1 | 3 | trigger_event(13); stop |
| 8 | 11 | 5 / 11 | 1 | 3 | trigger_event(14); stop |
| 8 | 12 | 5 / 12 | 1 | 3 | trigger_event(15); stop |
| 8 | 13 | 5 / 13 | 1 | 3 | trigger_event(16); stop |
| 8 | 14 | 5 / 14 | 1 | 3 | trigger_event(17); stop |
| 8 | 15 | 5 / 15 | 1 | 3 | trigger_event(18); stop |
| 8 | 16 | 5 / 16 | 1 | 3 | trigger_event(19); stop |
| 8 | 17 | 5 / 17 | 1 | 3 | trigger_event(20); stop |
| 8 | 18 | 5 / 18 | 1 | 3 | trigger_event(21); stop |
| 8 | 19 | 5 / 19 | 1 | 3 | trigger_event(22); stop |
| 8 | 20 | 5 / 20 | 1 | 3 | set_switch(3); stop |
| 8 | 21 | 5 / 21 | 1 | 3 | set_switch(4); stop |
| 8 | 22 | 5 / 22 | 1 | 3 | set_switch(5); stop |
| 8 | 230 | 4 / 0 | 0 | 3 | trigger_event(23); trigger_event(24); stop |
| 8 | 23 | 4 / 1 | 1 | 25 | trigger_event(25); stop |
| 8 | 24 | 4 / 2 | 1 | 25 | trigger_event(26); stop |
| 8 | 25 | 4 / 3 | 3 | 8 | trigger_event(27); stop |
| 8 | 26 | 4 / 4 | 3 | 8 | trigger_event(28); stop |
| 8 | 27 | 4 / 5 | 5 | 8 | trigger_event(29); stop |
| 8 | 28 | 4 / 6 | 5 | 8 | trigger_event(30); stop |
| 8 | 29 | 4 / 7 | 2 | 19 | trigger_event(31); stop |
| 8 | 30 | 4 / 8 | 2 | 19 | trigger_event(32); stop |
| 8 | 31 | 4 / 9 | 7 | 8 | set_switch(7); stop |
| 8 | 32 | 4 / 10 | 7 | 8 | set_switch(6); stop |
| 8 | 330 | 3 / 0 | 0 | 3 | trigger_event(33); trigger_event(34); stop |
| 8 | 33 | 3 / 1 | 12 | 45 | stop |
| 8 | 34 | 3 / 2 | 3 | 45 | trigger_event(35); stop |
| 8 | 35 | 3 / 3 | 6 | 30 | trigger_event(36); stop |
| 8 | 36 | 3 / 4 | 9 | 30 | trigger_event(37); stop |
| 8 | 37 | 3 / 5 | 11 | 3 | trigger_event(38); set_switch(8); stop |
| 8 | 38 | 3 / 6 | 4 | 70 | trigger_event(400); stop |
| 8 | 39 | 3 / 7 | 5 | 60 | trigger_event(41); stop |
| 8 | 400 | 3 / 8 | 4 | 45 | stop |
| 8 | 41 | 3 / 9 | 2 | 20 | trigger_event(42); stop |
| 8 | 42 | 3 / 10 | 5 | 3 | trigger_event(43); stop |
| 8 | 43 | 3 / 11 | 4 | 30 | set_switch(10); construct_objects(room=3,group_or_wave=1); stop |
| 8 | 44 | 2 / 1 | 2 | 38 | trigger_event(45); stop |
| 8 | 45 | 2 / 2 | 7 | 20 | trigger_event(46); stop |
| 8 | 46 | 2 / 3 | 9 | 15 | trigger_event(47); stop |
| 8 | 47 | 2 / 4 | 8 | 5 | construct_objects(room=2,group_or_wave=2); stop |
| 8 | 48 | 2 / 5 | 4 | 8 | trigger_event(49); trigger_event(490); trigger_event(4900); stop |
| 8 | 49 | 2 / 6 | 1 | 5 | set_switch(12); stop |
| 8 | 490 | 2 / 7 | 1 | 41 | set_switch(13); stop |
| 8 | 4900 | 2 / 8 | 1 | 77 | set_switch(14); stop |
| 8 | 50 | 10 / 1 | 8 | 25 | trigger_event(51); stop |
| 8 | 51 | 10 / 2 | 1 | 20 | trigger_event(52); stop |
| 8 | 52 | 10 / 3 | 8 | 3 | trigger_event(53); stop |
| 8 | 53 | 10 / 4 | 4 | 15 | set_switch(15); stop |
| 8 | 54 | 8 / 1 | 4 | 45 | trigger_event(55); stop |
| 8 | 55 | 8 / 2 | 8 | 30 | trigger_event(56); stop |
| 8 | 56 | 8 / 3 | 6 | 50 | trigger_event(57); stop |
| 8 | 57 | 8 / 4 | 8 | 3 | trigger_event(58); stop |
| 8 | 58 | 8 / 5 | 6 | 45 | set_switch(11); construct_objects(room=8,group_or_wave=1); stop |
| 8 | 540 | 8 / 10 | 3 | 250 | trigger_event(541); stop |
| 8 | 541 | 8 / 9 | 4 | 250 | trigger_event(58); stop |
| 8 | 542 | 8 / 8 | 2 | 300 | stop |
| 8 | 59 | 2 / 9 | 5 | 35 | trigger_event(60); stop |
| 8 | 60 | 2 / 10 | 2 | 12 | trigger_event(61); stop |
| 8 | 61 | 2 / 11 | 5 | 15 | set_switch(11); construct_objects(room=2,group_or_wave=4); stop |
| 8 | 62 | 2 / 12 | 3 | 15 | trigger_event(45); stop |
| 9 | 1 | 3 / 1 | 6 | 12 | stop |
| 9 | 2 | 3 / 2 | 4 | 3 | stop |
| 9 | 7 | 7 / 0 | 0 | 15 | trigger_event(8); trigger_event(9); stop |
| 9 | 8 | 7 / 1 | 8 | 20 | trigger_event(11); stop |
| 9 | 9 | 7 / 10 | 3 | 20 | stop |
| 9 | 10 | 7 / 2 | 8 | 250 | trigger_event(12); stop |
| 9 | 11 | 7 / 3 | 4 | 20 | trigger_event(13); stop |
| 9 | 12 | 7 / 4 | 4 | 100 | trigger_event(13); stop |
| 9 | 13 | 7 / 5 | 11 | 20 | set_switch(3); stop |
| 9 | 14 | 14 / 1 | 3 | 1 | trigger_event(15); trigger_event(16); trigger_event(160); set_switch(7); stop |
| 9 | 15 | 14 / 2 | 4 | 3 | stop |
| 9 | 160 | 13 / 10 | 2 | 25 | trigger_event(19); stop |
| 9 | 16 | 13 / 1 | 4 | 25 | trigger_event(17); stop |
| 9 | 17 | 13 / 2 | 6 | 12 | set_switch(8); stop |
| 9 | 18 | 13 / 4 | 4 | 200 | trigger_event(19); stop |
| 9 | 20 | 11 / 0 | 0 | 5 | trigger_event(21); trigger_event(22); stop |
| 9 | 21 | 11 / 10 | 9 | 10 | stop |
| 9 | 22 | 11 / 1 | 8 | 180 | trigger_event(23); stop |
| 9 | 23 | 11 / 2 | 10 | 35 | trigger_event(24); stop |
| 9 | 24 | 11 / 3 | 8 | 15 | trigger_event(65); set_switch(199); construct_objects(room=11,group_or_wave=1); stop |
| 9 | 330 | 5 / 10 | 2 | 5 | stop |
| 9 | 33 | 5 / 1 | 2 | 20 | trigger_event(34); construct_objects(room=5,group_or_wave=2); stop |
| 9 | 34 | 5 / 2 | 4 | 2 | trigger_event(35); construct_objects(room=5,group_or_wave=3); stop |
| 9 | 35 | 5 / 3 | 2 | 2 | trigger_event(36); construct_objects(room=5,group_or_wave=4); stop |
| 9 | 36 | 5 / 4 | 7 | 2 | set_switch(200); construct_objects(room=7,group_or_wave=2); stop |
| 9 | 400 | 4 / 0 | 0 | 3 | trigger_event(40); trigger_event(41); stop |
| 9 | 40 | 4 / 2 | 3 | 8 | trigger_event(42); stop |
| 9 | 41 | 4 / 1 | 4 | 90 | trigger_event(43); stop |
| 9 | 42 | 4 / 4 | 6 | 3 | trigger_event(44); stop |
| 9 | 43 | 4 / 3 | 4 | 5 | trigger_event(44); stop |
| 9 | 44 | 4 / 5 | 5 | 3 | trigger_event(45); stop |
| 9 | 45 | 4 / 6 | 8 | 3 | trigger_event(46); stop |
| 9 | 46 | 4 / 7 | 10 | 3 | trigger_event(48); trigger_event(481); trigger_event(482); trigger_event(483); trigger_event(484); stop |
| 9 | 481 | 4 / 16 | 3 | 3 | stop |
| 9 | 482 | 4 / 10 | 1 | 3 | stop |
| 9 | 483 | 4 / 11 | 1 | 3 | stop |
| 9 | 484 | 4 / 12 | 1 | 3 | stop |
| 9 | 48 | 4 / 8 | 3 | 30 | trigger_event(49); stop |
| 9 | 49 | 4 / 9 | 8 | 3 | construct_objects(room=4,group_or_wave=1); set_switch(25); trigger_event(491); stop |
| 9 | 491 | 4 / 17 | 1 | 10 | stop |
| 9 | 50 | 7 / 6 | 7 | 40 | trigger_event(51); stop |
| 9 | 51 | 7 / 7 | 5 | 3 | set_switch(2); stop |
| 9 | 65 | 12 / 1 | 3 | 40 | trigger_event(67); stop |
| 9 | 66 | 12 / 2 | 4 | 60 | trigger_event(67); stop |
| 9 | 67 | 12 / 3 | 7 | 15 | set_switch(23); trigger_event(330); construct_objects(room=5,group_or_wave=1); construct_objects(room=7,group_or_wave=1); stop |
| 9 | 99 | 3 / 3 | 4 | 1 | stop |
| 9 | 110 | 9 / 0 | 0 | 3 | trigger_event(111); trigger_event(1100); stop |
| 9 | 1100 | 9 / 10 | 2 | 20 | trigger_event(1101); stop |
| 9 | 1101 | 9 / 11 | 3 | 5 | stop |
| 9 | 111 | 9 / 1 | 3 | 20 | trigger_event(112); stop |
| 9 | 112 | 9 / 2 | 8 | 15 | trigger_event(113); stop |
| 9 | 113 | 9 / 3 | 12 | 20 | set_switch(1); construct_objects(room=9,group_or_wave=1); stop |
| 9 | 114 | 9 / 4 | 4 | 3 | stop |
| 9 | 100 | 1 / 0 | 0 | 5 | trigger_event(101); stop |
| 9 | 101 | 1 / 1 | 4 | 15 | trigger_event(102); stop |
| 9 | 102 | 1 / 2 | 6 | 15 | trigger_event(103); stop |
| 9 | 103 | 1 / 3 | 5 | 15 | stop |
| 9 | 104 | 1 / 4 | 5 | 3 | trigger_event(105); stop |
| 9 | 105 | 1 / 5 | 4 | 15 | trigger_event(106); stop |
| 9 | 106 | 1 / 6 | 6 | 15 | stop |
| 9 | 107 | 1 / 7 | 8 | 3 | trigger_event(108); stop |
| 9 | 108 | 1 / 8 | 4 | 15 | stop |
| 12 | 1 | 65 / 1 | 1 | 16 | trigger_event(2); trigger_event(3); stop |
| 12 | 2 | 65 / 2 | 2 | 3 | trigger_event(4); stop |
| 12 | 3 | 65 / 3 | 2 | 25 | trigger_event(5); stop |
| 12 | 4 | 65 / 4 | 4 | 8 | trigger_event(6); stop |
| 12 | 5 | 65 / 5 | 3 | 12 | trigger_event(7); stop |
| 12 | 6 | 65 / 6 | 3 | 3 | trigger_event(8); stop |
| 12 | 7 | 65 / 7 | 4 | 3 | trigger_event(9); stop |
| 12 | 8 | 65 / 8 | 3 | 20 | trigger_event(10); stop |
| 12 | 9 | 65 / 9 | 4 | 50 | trigger_event(11); stop |
| 12 | 10 | 65 / 10 | 4 | 3 | trigger_event(12); stop |
| 12 | 11 | 65 / 11 | 4 | 10 | trigger_event(13); stop |
| 12 | 12 | 65 / 12 | 4 | 3 | trigger_event(14); stop |
| 12 | 13 | 65 / 13 | 6 | 8 | trigger_event(15); stop |
| 12 | 14 | 65 / 14 | 7 | 5 | stop |
| 12 | 15 | 65 / 15 | 4 | 10 | stop |

## Review notes

- Floor 9: event 160 targets absent event 19
- Floor 9: event 18 targets absent event 19
