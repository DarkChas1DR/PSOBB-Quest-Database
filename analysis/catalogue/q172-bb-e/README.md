# Penumbral Surge #2 — q172-bb-e

Episode2; header quest ID 172; language E. Static scan: **456 objects, 676 enemy/NPC records, 149 events, 82 script labels.** Script roundtrip: alignment-only.

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
| 0 | 53 | 11 | 0 |
| 3 | 173 | 304 | 72 |
| 4 | 230 | 361 | 77 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 3 | 1 | 42 / 1 | 0 | 1 | construct_objects(room=42,group_or_wave=1); stop |
| 3 | 2 | 31 / 1 | 2 | 15 | trigger_event(3); stop |
| 3 | 3 | 31 / 2 | 5 | 25 | set_switch(1); stop |
| 3 | 4 | 31 / 3 | 2 | 30 | set_switch(2); stop |
| 3 | 5 | 50 / 1 | 5 | 50 | trigger_event(6); stop |
| 3 | 6 | 50 / 2 | 3 | 30 | trigger_event(7); stop |
| 3 | 7 | 50 / 3 | 3 | 30 | trigger_event(8); stop |
| 3 | 8 | 50 / 4 | 5 | 40 | set_switch(3); stop |
| 3 | 9 | 11 / 1 | 6 | 30 | trigger_event(10); stop |
| 3 | 10 | 11 / 2 | 2 | 30 | trigger_event(11); stop |
| 3 | 11 | 11 / 3 | 6 | 30 | trigger_event(12); stop |
| 3 | 12 | 11 / 4 | 1 | 30 | set_switch(4); construct_objects(room=180,group_or_wave=50); stop |
| 3 | 13 | 180 / 1 | 4 | 45 | set_switch(5); trigger_event(14); stop |
| 3 | 14 | 41 / 1 | 5 | 1 | trigger_event(15); stop |
| 3 | 15 | 41 / 2 | 5 | 40 | trigger_event(16); stop |
| 3 | 16 | 41 / 3 | 5 | 40 | trigger_event(17); stop |
| 3 | 17 | 41 / 4 | 8 | 40 | trigger_event(18); stop |
| 3 | 18 | 41 / 5 | 1 | 50 | set_switch(6); construct_objects(room=105,group_or_wave=90); stop |
| 3 | 19 | 52 / 1 | 3 | 50 | trigger_event(20); stop |
| 3 | 20 | 52 / 2 | 4 | 35 | trigger_event(21); stop |
| 3 | 21 | 52 / 3 | 4 | 40 | trigger_event(22); stop |
| 3 | 22 | 52 / 4 | 3 | 40 | set_switch(7); stop |
| 3 | 23 | 160 / 1 | 2 | 1 | set_switch(8); stop |
| 3 | 24 | 51 / 1 | 4 | 30 | trigger_event(25); stop |
| 3 | 25 | 51 / 2 | 6 | 30 | trigger_event(26); stop |
| 3 | 26 | 51 / 3 | 7 | 40 | set_switch(9); stop |
| 3 | 27 | 51 / 4 | 5 | 75 | trigger_event(28); stop |
| 3 | 28 | 51 / 5 | 6 | 40 | trigger_event(29); stop |
| 3 | 29 | 51 / 6 | 5 | 40 | set_switch(10); stop |
| 3 | 30 | 51 / 7 | 7 | 10 | trigger_event(31); stop |
| 3 | 31 | 51 / 8 | 6 | 30 | trigger_event(32); stop |
| 3 | 32 | 51 / 9 | 6 | 30 | trigger_event(33); stop |
| 3 | 33 | 51 / 10 | 8 | 30 | trigger_event(34); stop |
| 3 | 34 | 51 / 11 | 1 | 5 | set_switch(11); construct_objects(room=140,group_or_wave=91); stop |
| 3 | 35 | 12 / 1 | 3 | 10 | trigger_event(36); stop |
| 3 | 36 | 12 / 2 | 4 | 40 | trigger_event(37); stop |
| 3 | 37 | 12 / 3 | 5 | 40 | set_switch(12); stop |
| 3 | 38 | 182 / 1 | 1 | 25 | trigger_event(39); stop |
| 3 | 39 | 182 / 2 | 1 | 30 | set_switch(13); stop |
| 3 | 40 | 181 / 1 | 2 | 20 | set_switch(14); trigger_event(41); stop |
| 3 | 41 | 181 / 2 | 4 | 35 | set_switch(15); trigger_event(42); stop |
| 3 | 42 | 181 / 3 | 4 | 35 | set_switch(16); trigger_event(43); stop |
| 3 | 43 | 181 / 4 | 4 | 35 | set_switch(17); trigger_event(44); stop |
| 3 | 44 | 181 / 5 | 1 | 30 | set_switch(18); stop |
| 3 | 45 | 32 / 1 | 3 | 30 | trigger_event(46); stop |
| 3 | 46 | 32 / 2 | 6 | 60 | trigger_event(47); stop |
| 3 | 47 | 32 / 3 | 3 | 30 | set_switch(19); stop |
| 3 | 48 | 21 / 1 | 6 | 10 | trigger_event(49); stop |
| 3 | 49 | 21 / 2 | 5 | 25 | trigger_event(50); stop |
| 3 | 50 | 21 / 3 | 5 | 25 | trigger_event(51); stop |
| 3 | 51 | 21 / 4 | 5 | 25 | trigger_event(52); stop |
| 3 | 52 | 21 / 5 | 1 | 30 | set_switch(20); construct_objects(room=12,group_or_wave=92); stop |
| 3 | 53 | 107 / 1 | 3 | 10 | set_switch(21); stop |
| 3 | 54 | 20 / 1 | 5 | 30 | trigger_event(55); stop |
| 3 | 55 | 20 / 2 | 7 | 30 | trigger_event(56); stop |
| 3 | 56 | 20 / 3 | 7 | 30 | set_switch(22); stop |
| 3 | 57 | 121 / 1 | 3 | 1 | trigger_event(58); stop |
| 3 | 58 | 121 / 2 | 3 | 1 | trigger_event(59); stop |
| 3 | 59 | 121 / 3 | 3 | 1 | set_switch(23); stop |
| 3 | 60 | 40 / 1 | 7 | 50 | trigger_event(61); stop |
| 3 | 61 | 40 / 2 | 5 | 40 | trigger_event(62); stop |
| 3 | 62 | 40 / 3 | 7 | 35 | trigger_event(63); stop |
| 3 | 63 | 40 / 4 | 7 | 30 | set_switch(24); stop |
| 3 | 64 | 40 / 5 | 7 | 20 | trigger_event(65); stop |
| 3 | 65 | 40 / 6 | 9 | 25 | trigger_event(66); stop |
| 3 | 66 | 40 / 7 | 9 | 40 | set_switch(25); stop |
| 3 | 67 | 120 / 1 | 2 | 5 | trigger_event(68); stop |
| 3 | 68 | 120 / 2 | 2 | 20 | trigger_event(69); stop |
| 3 | 69 | 120 / 3 | 2 | 25 | trigger_event(70); stop |
| 3 | 70 | 120 / 4 | 5 | 20 | set_switch(26); trigger_event(71); stop |
| 3 | 71 | 10 / 1 | 1 | 1 | set_switch(27); construct_objects(room=107,group_or_wave=93); stop |
| 3 | 72 | 42 / 2 | 2 | 60 | set_switch(28); construct_objects(room=30,group_or_wave=1); stop |
| 4 | 1 | 11 / 1 | 5 | 20 | trigger_event(2); stop |
| 4 | 2 | 11 / 2 | 7 | 40 | trigger_event(3); stop |
| 4 | 3 | 11 / 3 | 4 | 30 | trigger_event(4); stop |
| 4 | 4 | 11 / 4 | 10 | 30 | trigger_event(5); stop |
| 4 | 5 | 11 / 5 | 5 | 35 | trigger_event(6); stop |
| 4 | 6 | 11 / 6 | 7 | 30 | set_switch(1); construct_objects(room=11,group_or_wave=10); construct_objects(room=31,group_or_wave=10); stop |
| 4 | 7 | 31 / 1 | 7 | 50 | trigger_event(8); stop |
| 4 | 8 | 31 / 2 | 8 | 40 | trigger_event(9); stop |
| 4 | 9 | 31 / 3 | 5 | 30 | set_switch(2); construct_objects(room=31,group_or_wave=11); construct_objects(room=50,group_or_wave=11); stop |
| 4 | 10 | 50 / 1 | 12 | 90 | trigger_event(11); stop |
| 4 | 11 | 50 / 2 | 9 | 40 | trigger_event(12); stop |
| 4 | 12 | 50 / 3 | 12 | 40 | trigger_event(13); stop |
| 4 | 13 | 50 / 4 | 4 | 40 | trigger_event(14); stop |
| 4 | 14 | 50 / 5 | 7 | 40 | trigger_event(15); stop |
| 4 | 15 | 50 / 6 | 6 | 40 | trigger_event(16); stop |
| 4 | 16 | 50 / 7 | 5 | 120 | set_switch(3); construct_objects(room=50,group_or_wave=12); construct_objects(room=21,group_or_wave=12); stop |
| 4 | 17 | 21 / 1 | 2 | 50 | trigger_event(18); stop |
| 4 | 18 | 21 / 2 | 2 | 50 | trigger_event(19); stop |
| 4 | 19 | 21 / 3 | 3 | 50 | trigger_event(20); stop |
| 4 | 20 | 21 / 4 | 3 | 50 | trigger_event(21); stop |
| 4 | 21 | 21 / 5 | 5 | 50 | set_switch(111); construct_objects(room=21,group_or_wave=200); stop |
| 4 | 22 | 21 / 7 | 2 | 40 | trigger_event(23); trigger_event(24); stop |
| 4 | 24 | 21 / 8 | 4 | 40 | trigger_event(25); stop |
| 4 | 25 | 21 / 9 | 6 | 40 | trigger_event(26); stop |
| 4 | 26 | 21 / 10 | 9 | 40 | set_switch(4); construct_objects(room=21,group_or_wave=13); stop |
| 4 | 27 | 191 / 1 | 2 | 30 | set_switch(5); construct_objects(room=20,group_or_wave=14); stop |
| 4 | 28 | 20 / 1 | 1 | 30 | trigger_event(29); stop |
| 4 | 29 | 20 / 2 | 2 | 30 | trigger_event(30); stop |
| 4 | 30 | 20 / 3 | 3 | 30 | trigger_event(31); stop |
| 4 | 31 | 20 / 4 | 4 | 30 | trigger_event(32); stop |
| 4 | 32 | 20 / 5 | 10 | 40 | set_switch(6); construct_objects(room=20,group_or_wave=15); construct_objects(room=40,group_or_wave=15); stop |
| 4 | 33 | 40 / 1 | 7 | 35 | trigger_event(34); stop |
| 4 | 34 | 40 / 2 | 6 | 35 | trigger_event(35); stop |
| 4 | 35 | 40 / 3 | 7 | 40 | set_switch(7); trigger_event(36); stop |
| 4 | 36 | 40 / 4 | 7 | 70 | trigger_event(37); stop |
| 4 | 37 | 40 / 5 | 5 | 35 | trigger_event(38); stop |
| 4 | 38 | 40 / 6 | 8 | 40 | set_switch(8); construct_objects(room=40,group_or_wave=16); stop |
| 4 | 39 | 180 / 1 | 2 | 30 | set_switch(9); construct_objects(room=30,group_or_wave=17); stop |
| 4 | 40 | 30 / 1 | 0 | 1 | set_switch(10); set_switch(101); construct_objects(room=30,group_or_wave=18); stop |
| 4 | 41 | 10 / 1 | 4 | 50 | trigger_event(42); stop |
| 4 | 42 | 10 / 2 | 6 | 40 | trigger_event(43); stop |
| 4 | 43 | 10 / 3 | 3 | 45 | trigger_event(44); stop |
| 4 | 44 | 10 / 4 | 4 | 40 | trigger_event(45); stop |
| 4 | 45 | 10 / 5 | 6 | 35 | trigger_event(46); stop |
| 4 | 46 | 10 / 6 | 6 | 30 | trigger_event(47); stop |
| 4 | 47 | 10 / 7 | 9 | 40 | set_switch(11); construct_objects(room=105,group_or_wave=85); stop |
| 4 | 48 | 51 / 0 | 0 | 1 | set_switch(1); trigger_event(49); trigger_event(50); stop |
| 4 | 49 | 51 / 1 | 3 | 40 | trigger_event(51); stop |
| 4 | 50 | 51 / 2 | 2 | 40 | trigger_event(52); stop |
| 4 | 51 | 51 / 3 | 2 | 40 | trigger_event(53); stop |
| 4 | 52 | 51 / 4 | 3 | 40 | trigger_event(54); stop |
| 4 | 53 | 51 / 5 | 4 | 40 | trigger_event(55); stop |
| 4 | 54 | 51 / 6 | 3 | 40 | trigger_event(56); stop |
| 4 | 55 | 51 / 7 | 3 | 40 | trigger_event(57); stop |
| 4 | 56 | 51 / 8 | 5 | 40 | trigger_event(58); stop |
| 4 | 57 | 51 / 9 | 4 | 40 | set_switch(230); stop |
| 4 | 58 | 51 / 10 | 6 | 40 | set_switch(231); stop |
| 4 | 59 | 51 / 11 | 5 | 30 | trigger_event(61); stop |
| 4 | 60 | 51 / 12 | 3 | 30 | trigger_event(62); stop |
| 4 | 61 | 51 / 13 | 3 | 30 | trigger_event(63); stop |
| 4 | 62 | 51 / 14 | 4 | 30 | trigger_event(64); stop |
| 4 | 63 | 51 / 15 | 5 | 30 | trigger_event(65); stop |
| 4 | 64 | 51 / 16 | 4 | 30 | trigger_event(66); stop |
| 4 | 65 | 51 / 17 | 4 | 30 | trigger_event(67); stop |
| 4 | 66 | 51 / 18 | 4 | 30 | trigger_event(68); stop |
| 4 | 67 | 51 / 19 | 2 | 30 | trigger_event(69); stop |
| 4 | 68 | 51 / 20 | 4 | 30 | trigger_event(700); stop |
| 4 | 700 | 51 / 27 | 2 | 30 | trigger_event(70); stop |
| 4 | 69 | 51 / 21 | 5 | 30 | trigger_event(701); stop |
| 4 | 701 | 51 / 28 | 2 | 30 | trigger_event(71); stop |
| 4 | 70 | 51 / 22 | 6 | 30 | trigger_event(72); stop |
| 4 | 71 | 51 / 23 | 5 | 30 | trigger_event(73); stop |
| 4 | 72 | 51 / 24 | 4 | 30 | trigger_event(74); stop |
| 4 | 73 | 51 / 25 | 4 | 30 | set_switch(232); stop |
| 4 | 74 | 51 / 26 | 6 | 30 | set_switch(233); stop |
| 4 | 75 | 51 / 0 | 0 | 1 | construct_objects(room=51,group_or_wave=18); stop |
| 4 | 200 | 521 / 1 | 1 | 1 | stop |

## Review notes

- Floor 4: event 22 targets absent event 23
