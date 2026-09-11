# Penumbral Surge #1 — q171-bb-e

Episode2; header quest ID 171; language E. Static scan: **375 objects, 506 enemy/NPC records, 171 events, 100 script labels.** Script roundtrip: alignment-only.

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
| 0 | 52 | 10 | 0 |
| 1 | 234 | 277 | 104 |
| 2 | 89 | 219 | 67 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 1 | 80 / 0 | 0 | 1 | construct_objects(room=80,group_or_wave=70); stop |
| 1 | 2 | 41 / 1 | 3 | 50 | trigger_event(3); stop |
| 1 | 3 | 41 / 2 | 3 | 40 | trigger_event(4); stop |
| 1 | 4 | 41 / 3 | 2 | 40 | set_switch(1); stop |
| 1 | 7 | 91 / 1 | 1 | 5 | trigger_event(9); stop |
| 1 | 9 | 91 / 3 | 2 | 50 | trigger_event(10); stop |
| 1 | 10 | 91 / 4 | 2 | 60 | set_switch(3); stop |
| 1 | 13 | 40 / 1 | 2 | 50 | trigger_event(14); stop |
| 1 | 14 | 40 / 2 | 4 | 40 | trigger_event(15); stop |
| 1 | 15 | 40 / 3 | 3 | 1 | trigger_event(16); stop |
| 1 | 16 | 40 / 4 | 3 | 40 | set_switch(8); stop |
| 1 | 18 | 90 / 1 | 2 | 10 | trigger_event(19); stop |
| 1 | 19 | 90 / 2 | 5 | 60 | set_switch(9); stop |
| 1 | 21 | 90 / 4 | 3 | 40 | trigger_event(22); stop |
| 1 | 22 | 90 / 5 | 1 | 40 | set_switch(10); stop |
| 1 | 23 | 90 / 6 | 1 | 35 | trigger_event(24); stop |
| 1 | 24 | 90 / 7 | 4 | 60 | set_switch(11); stop |
| 1 | 25 | 4 / 1 | 2 | 10 | trigger_event(26); stop |
| 1 | 26 | 4 / 2 | 2 | 40 | trigger_event(2660); stop |
| 1 | 2660 | 119 / 1 | 2 | 20 | trigger_event(27); stop |
| 1 | 27 | 4 / 3 | 1 | 50 | trigger_event(28); construct_objects(room=4,group_or_wave=25); stop |
| 1 | 28 | 40 / 6 | 4 | 60 | set_switch(12); trigger_event(29); stop |
| 1 | 29 | 40 / 7 | 4 | 40 | trigger_event(30); stop |
| 1 | 30 | 40 / 8 | 3 | 45 | set_switch(13); trigger_event(31); stop |
| 1 | 32 | 70 / 1 | 3 | 80 | trigger_event(33); stop |
| 1 | 33 | 70 / 2 | 3 | 60 | trigger_event(34); stop |
| 1 | 34 | 70 / 3 | 4 | 30 | trigger_event(35); stop |
| 1 | 35 | 70 / 4 | 2 | 35 | set_switch(14); stop |
| 1 | 36 | 11 / 1 | 4 | 40 | trigger_event(37); stop |
| 1 | 37 | 11 / 2 | 5 | 1 | trigger_event(38); stop |
| 1 | 38 | 11 / 3 | 5 | 30 | trigger_event(39); stop |
| 1 | 39 | 11 / 4 | 4 | 25 | set_switch(15); stop |
| 1 | 40 | 520 / 1 | 2 | 1 | set_switch(16); stop |
| 1 | 42 | 61 / 1 | 2 | 90 | trigger_event(43); stop |
| 1 | 43 | 61 / 2 | 3 | 40 | trigger_event(44); stop |
| 1 | 44 | 61 / 3 | 6 | 35 | trigger_event(45); stop |
| 1 | 45 | 61 / 4 | 3 | 30 | set_switch(17); stop |
| 1 | 47 | 80 / 1 | 1 | 30 | set_switch(18); stop |
| 1 | 48 | 150 / 1 | 1 | 10 | trigger_event(100); stop |
| 1 | 100 | 150 / 2 | 2 | 45 | set_switch(19); stop |
| 1 | 49 | 30 / 1 | 5 | 15 | trigger_event(50); stop |
| 1 | 50 | 30 / 2 | 3 | 40 | trigger_event(51); stop |
| 1 | 51 | 30 / 3 | 2 | 35 | trigger_event(52); stop |
| 1 | 52 | 30 / 4 | 5 | 30 | set_switch(20); stop |
| 1 | 53 | 115 / 1 | 2 | 20 | trigger_event(101); stop |
| 1 | 101 | 115 / 2 | 1 | 40 | set_switch(21); construct_objects(room=30,group_or_wave=15); stop |
| 1 | 54 | 30 / 5 | 2 | 60 | set_switch(22); trigger_event(55); stop |
| 1 | 55 | 93 / 1 | 3 | 60 | trigger_event(56); stop |
| 1 | 56 | 93 / 2 | 3 | 60 | set_switch(23); trigger_event(102); stop |
| 1 | 102 | 141 / 1 | 1 | 1 | trigger_event(103); stop |
| 1 | 103 | 141 / 2 | 3 | 45 | set_switch(49); stop |
| 1 | 57 | 50 / 1 | 3 | 50 | trigger_event(58); stop |
| 1 | 58 | 50 / 2 | 4 | 35 | trigger_event(59); stop |
| 1 | 59 | 50 / 3 | 1 | 30 | set_switch(24); trigger_event(60); trigger_event(61); stop |
| 1 | 60 | 50 / 4 | 2 | 1 | set_switch(25); stop |
| 1 | 61 | 50 / 5 | 2 | 30 | trigger_event(62); stop |
| 1 | 62 | 50 / 6 | 3 | 30 | set_switch(26); stop |
| 1 | 64 | 50 / 8 | 1 | 5 | trigger_event(65); stop |
| 1 | 65 | 50 / 9 | 3 | 30 | trigger_event(66); stop |
| 1 | 66 | 50 / 10 | 4 | 40 | set_switch(115); stop |
| 1 | 150 | 50 / 11 | 1 | 5 | set_switch(116); stop |
| 1 | 104 | 162 / 1 | 1 | 1 | set_switch(56); stop |
| 1 | 67 | 70 / 5 | 4 | 20 | trigger_event(68); stop |
| 1 | 68 | 70 / 6 | 6 | 50 | trigger_event(69); stop |
| 1 | 69 | 70 / 7 | 4 | 30 | trigger_event(70); stop |
| 1 | 70 | 70 / 8 | 4 | 40 | set_switch(28); stop |
| 1 | 71 | 100 / 1 | 3 | 1 | trigger_event(105); stop |
| 1 | 105 | 100 / 2 | 1 | 45 | set_switch(29); stop |
| 1 | 72 | 10 / 1 | 2 | 50 | trigger_event(73); stop |
| 1 | 73 | 10 / 3 | 3 | 30 | trigger_event(74); stop |
| 1 | 74 | 10 / 2 | 6 | 35 | trigger_event(75); stop |
| 1 | 75 | 10 / 4 | 4 | 40 | set_switch(30); stop |
| 1 | 11990 | 161 / 1 | 1 | 30 | trigger_event(11991); stop |
| 1 | 11991 | 161 / 2 | 2 | 30 | set_switch(97); stop |
| 1 | 106 | 92 / 1 | 2 | 30 | trigger_event(107); stop |
| 1 | 107 | 92 / 2 | 2 | 30 | trigger_event(108); stop |
| 1 | 108 | 92 / 3 | 1 | 30 | trigger_event(109); stop |
| 1 | 109 | 92 / 4 | 3 | 30 | set_switch(57); stop |
| 1 | 76 | 20 / 1 | 4 | 30 | trigger_event(77); stop |
| 1 | 77 | 20 / 2 | 4 | 30 | trigger_event(78); stop |
| 1 | 78 | 20 / 3 | 4 | 30 | trigger_event(79); stop |
| 1 | 79 | 20 / 4 | 2 | 30 | set_switch(32); stop |
| 1 | 81 | 20 / 6 | 3 | 50 | trigger_event(82); stop |
| 1 | 82 | 20 / 7 | 2 | 30 | trigger_event(83); stop |
| 1 | 83 | 20 / 8 | 2 | 30 | trigger_event(84); stop |
| 1 | 84 | 20 / 9 | 1 | 30 | trigger_event(85); stop |
| 1 | 85 | 20 / 10 | 2 | 30 | trigger_event(86); stop |
| 1 | 86 | 20 / 11 | 2 | 30 | trigger_event(87); stop |
| 1 | 87 | 20 / 12 | 5 | 30 | set_switch(33); construct_objects(room=20,group_or_wave=6); stop |
| 1 | 110 | 111 / 1 | 1 | 30 | trigger_event(111); stop |
| 1 | 111 | 111 / 2 | 2 | 30 | trigger_event(112); stop |
| 1 | 112 | 111 / 3 | 3 | 30 | set_switch(58); stop |
| 1 | 88 | 60 / 1 | 2 | 100 | trigger_event(89); stop |
| 1 | 89 | 60 / 2 | 4 | 50 | trigger_event(90); stop |
| 1 | 90 | 60 / 3 | 6 | 45 | trigger_event(91); stop |
| 1 | 91 | 60 / 4 | 2 | 30 | set_switch(189); construct_objects(room=60,group_or_wave=1); stop |
| 1 | 92 | 60 / 5 | 3 | 40 | trigger_event(93); stop |
| 1 | 93 | 60 / 6 | 4 | 1 | trigger_event(94); stop |
| 1 | 94 | 60 / 7 | 4 | 30 | trigger_event(95); stop |
| 1 | 95 | 60 / 8 | 3 | 45 | set_switch(188); construct_objects(room=60,group_or_wave=2); stop |
| 1 | 9000 | 60 / 50 | 0 | 1 | construct_objects(room=60,group_or_wave=5); stop |
| 1 | 9001 | 60 / 51 | 0 | 1 | construct_objects(room=60,group_or_wave=6); stop |
| 1 | 9002 | 80 / 40 | 0 | 1 | construct_objects(room=80,group_or_wave=1); stop |
| 1 | 9003 | 80 / 41 | 0 | 1 | construct_objects(room=80,group_or_wave=2); stop |
| 2 | 1 | 70 / 1 | 4 | 15 | trigger_event(2); stop |
| 2 | 2 | 70 / 2 | 6 | 40 | trigger_event(3300); stop |
| 2 | 3300 | 70 / 3 | 4 | 25 | trigger_event(3301); stop |
| 2 | 3301 | 70 / 4 | 7 | 30 | set_switch(1); construct_objects(room=540,group_or_wave=1); stop |
| 2 | 3302 | 540 / 1 | 4 | 1 | trigger_event(3303); stop |
| 2 | 3303 | 540 / 2 | 2 | 30 | set_switch(2); trigger_event(3); stop |
| 2 | 3 | 70 / 5 | 4 | 20 | trigger_event(4); stop |
| 2 | 4 | 70 / 6 | 6 | 1 | trigger_event(5); stop |
| 2 | 5 | 70 / 7 | 3 | 30 | set_switch(3); stop |
| 2 | 3304 | 160 / 1 | 3 | 1 | set_switch(4); stop |
| 2 | 6 | 90 / 1 | 3 | 15 | trigger_event(7); stop |
| 2 | 7 | 90 / 2 | 5 | 40 | trigger_event(8); stop |
| 2 | 8 | 90 / 3 | 2 | 40 | set_switch(5); trigger_event(9); stop |
| 2 | 9 | 112 / 1 | 1 | 1 | set_switch(44); stop |
| 2 | 10 | 91 / 1 | 4 | 20 | trigger_event(11); stop |
| 2 | 11 | 91 / 2 | 4 | 20 | trigger_event(3305); stop |
| 2 | 3305 | 91 / 3 | 4 | 30 | set_switch(7); stop |
| 2 | 12 | 161 / 1 | 1 | 1 | set_switch(77); stop |
| 2 | 13 | 80 / 1 | 4 | 30 | trigger_event(14); stop |
| 2 | 14 | 80 / 2 | 5 | 20 | trigger_event(15); stop |
| 2 | 15 | 80 / 3 | 5 | 50 | trigger_event(16); stop |
| 2 | 16 | 80 / 4 | 5 | 50 | trigger_event(17); stop |
| 2 | 17 | 80 / 5 | 8 | 40 | set_switch(8); construct_objects(room=80,group_or_wave=1); stop |
| 2 | 18 | 30 / 1 | 5 | 30 | trigger_event(19); stop |
| 2 | 19 | 30 / 2 | 7 | 40 | trigger_event(20); stop |
| 2 | 20 | 30 / 3 | 6 | 40 | trigger_event(21); stop |
| 2 | 21 | 30 / 4 | 6 | 30 | set_switch(9); stop |
| 2 | 22 | 20 / 1 | 5 | 20 | trigger_event(23); stop |
| 2 | 23 | 20 / 2 | 7 | 1 | trigger_event(24); stop |
| 2 | 24 | 20 / 3 | 6 | 40 | trigger_event(25); stop |
| 2 | 25 | 20 / 4 | 6 | 30 | set_switch(10); stop |
| 2 | 26 | 50 / 1 | 0 | 30 | set_switch(11); construct_objects(room=50,group_or_wave=14); stop |
| 2 | 27 | 50 / 2 | 3 | 20 | set_switch(12); stop |
| 2 | 28 | 50 / 3 | 0 | 1 | trigger_event(29); trigger_event(30); stop |
| 2 | 29 | 50 / 4 | 1 | 30 | trigger_event(31); stop |
| 2 | 30 | 50 / 5 | 2 | 30 | trigger_event(32); stop |
| 2 | 31 | 50 / 6 | 2 | 30 | trigger_event(33); stop |
| 2 | 32 | 50 / 7 | 1 | 30 | trigger_event(34); stop |
| 2 | 33 | 50 / 8 | 2 | 30 | trigger_event(35); stop |
| 2 | 34 | 50 / 9 | 4 | 30 | trigger_event(36); stop |
| 2 | 35 | 50 / 10 | 3 | 30 | trigger_event(37); stop |
| 2 | 36 | 50 / 11 | 2 | 30 | trigger_event(38); stop |
| 2 | 37 | 50 / 12 | 1 | 30 | trigger_event(39); stop |
| 2 | 38 | 50 / 13 | 2 | 30 | trigger_event(40); stop |
| 2 | 39 | 50 / 14 | 2 | 30 | trigger_event(41); stop |
| 2 | 40 | 50 / 15 | 2 | 30 | trigger_event(42); stop |
| 2 | 41 | 50 / 16 | 2 | 30 | trigger_event(43); stop |
| 2 | 42 | 50 / 17 | 1 | 30 | trigger_event(44); stop |
| 2 | 43 | 50 / 18 | 2 | 30 | trigger_event(45); stop |
| 2 | 44 | 50 / 19 | 2 | 30 | trigger_event(46); stop |
| 2 | 45 | 50 / 20 | 3 | 30 | trigger_event(47); stop |
| 2 | 46 | 50 / 21 | 3 | 30 | trigger_event(48); stop |
| 2 | 47 | 50 / 22 | 2 | 30 | trigger_event(49); stop |
| 2 | 48 | 50 / 23 | 1 | 30 | trigger_event(50); stop |
| 2 | 49 | 50 / 24 | 2 | 30 | trigger_event(51); stop |
| 2 | 50 | 50 / 25 | 2 | 30 | trigger_event(52); stop |
| 2 | 51 | 50 / 26 | 2 | 30 | trigger_event(53); stop |
| 2 | 52 | 50 / 27 | 2 | 30 | trigger_event(54); stop |
| 2 | 53 | 50 / 28 | 3 | 30 | trigger_event(55); stop |
| 2 | 54 | 50 / 29 | 3 | 30 | trigger_event(56); stop |
| 2 | 55 | 50 / 30 | 4 | 30 | trigger_event(57); stop |
| 2 | 56 | 50 / 31 | 2 | 30 | trigger_event(58); stop |
| 2 | 57 | 50 / 32 | 2 | 30 | trigger_event(59); stop |
| 2 | 58 | 50 / 33 | 1 | 30 | set_switch(15); stop |
| 2 | 59 | 50 / 34 | 4 | 30 | set_switch(16); stop |
| 2 | 60 | 50 / 35 | 6 | 90 | set_switch(17); construct_objects(room=50,group_or_wave=1); stop |
| 2 | 200 | 501 / 1 | 1 | 1 | stop |

## Review notes

- Nonzero data after terminal header
- Floor 1: event 30 targets absent event 31
