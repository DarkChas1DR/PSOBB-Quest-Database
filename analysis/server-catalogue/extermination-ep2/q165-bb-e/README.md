# Twilight Sanctuary — extermination-ep2/q165-bb-e

Episode2; header quest ID 165; language E. Static scan: **470 objects, 537 enemy/NPC records, 194 events, 63 script labels.** Script roundtrip: byte-identical.

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
| 0 | 52 | 26 | 0 |
| 7 | 141 | 83 | 56 |
| 17 | 277 | 428 | 138 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 7 | 1 | 1 / 1 | 0 | 180 | set_switch(1); stop |
| 7 | 5 | 2 / 1 | 4 | 1 | trigger_event(6); stop |
| 7 | 6 | 2 / 2 | 2 | 60 | trigger_event(12); trigger_event(15); trigger_event(17); set_switch(2); stop |
| 7 | 10 | 20 / 1 | 0 | 90 | trigger_event(11); stop |
| 7 | 11 | 20 / 2 | 0 | 150 | set_switch(3); stop |
| 7 | 12 | 20 / 3 | 0 | 1 | stop |
| 7 | 15 | 20 / 4 | 0 | 1 | trigger_event(16); stop |
| 7 | 16 | 20 / 5 | 0 | 1 | stop |
| 7 | 17 | 20 / 6 | 0 | 1 | trigger_event(18); stop |
| 7 | 18 | 20 / 7 | 0 | 1 | stop |
| 7 | 20 | 10 / 1 | 0 | 90 | construct_objects(room=10,group_or_wave=1); stop |
| 7 | 21 | 10 / 2 | 0 | 1 | set_switch(4); stop |
| 7 | 25 | 3 / 1 | 0 | 90 | trigger_event(26); stop |
| 7 | 26 | 3 / 2 | 0 | 60 | trigger_event(35); trigger_event(37); set_switch(5); stop |
| 7 | 30 | 4 / 1 | 1 | 30 | set_switch(23); stop |
| 7 | 31 | 4 / 2 | 0 | 90 | trigger_event(42); set_switch(6); stop |
| 7 | 35 | 4 / 3 | 0 | 1 | trigger_event(36); stop |
| 7 | 36 | 4 / 4 | 0 | 1 | stop |
| 7 | 37 | 4 / 5 | 0 | 1 | trigger_event(38); stop |
| 7 | 38 | 4 / 6 | 0 | 1 | stop |
| 7 | 40 | 21 / 1 | 0 | 60 | trigger_event(41); stop |
| 7 | 41 | 21 / 2 | 0 | 120 | trigger_event(47); set_switch(7); stop |
| 7 | 42 | 21 / 3 | 0 | 1 | stop |
| 7 | 45 | 5 / 1 | 7 | 120 | trigger_event(46); stop |
| 7 | 46 | 5 / 2 | 8 | 120 | set_switch(8); stop |
| 7 | 47 | 5 / 3 | 8 | 1 | stop |
| 7 | 50 | 22 / 1 | 0 | 150 | trigger_event(51); stop |
| 7 | 51 | 22 / 2 | 0 | 60 | set_switch(21); stop |
| 7 | 52 | 22 / 3 | 0 | 30 | trigger_event(53); stop |
| 7 | 53 | 22 / 4 | 0 | 180 | set_switch(9); stop |
| 7 | 55 | 30 / 1 | 0 | 10 | trigger_event(56); stop |
| 7 | 56 | 30 / 2 | 0 | 60 | set_switch(10); stop |
| 7 | 300 | 7 / 1 | 3 | 1 | set_switch(73); stop |
| 7 | 301 | 2 / 1 | 4 | 40 | trigger_event(302); stop |
| 7 | 302 | 2 / 2 | 2 | 30 | trigger_event(303); stop |
| 7 | 303 | 2 / 3 | 6 | 60 | trigger_event(304); stop |
| 7 | 304 | 2 / 4 | 4 | 50 | trigger_event(305); stop |
| 7 | 305 | 2 / 5 | 4 | 40 | trigger_event(306); set_switch(74); stop |
| 7 | 306 | 4 / 1 | 1 | 1 | set_switch(75); stop |
| 7 | 307 | 5 / 1 | 7 | 40 | trigger_event(308); stop |
| 7 | 308 | 5 / 2 | 8 | 30 | trigger_event(309); stop |
| 7 | 309 | 5 / 3 | 8 | 50 | trigger_event(310); stop |
| 7 | 310 | 5 / 4 | 8 | 60 | set_switch(76); stop |
| 7 | 312 | 8 / 1 | 2 | 65 | trigger_event(313); stop |
| 7 | 313 | 8 / 2 | 5 | 40 | trigger_event(314); stop |
| 7 | 314 | 8 / 3 | 2 | 45 | trigger_event(315); stop |
| 7 | 315 | 8 / 4 | 3 | 30 | trigger_event(316); stop |
| 7 | 316 | 8 / 5 | 8 | 50 | trigger_event(317); stop |
| 7 | 317 | 8 / 6 | 4 | 40 | trigger_event(318); stop |
| 7 | 318 | 8 / 7 | 4 | 60 | set_switch(81); construct_objects(room=3,group_or_wave=222); stop |
| 7 | 1234 | 10 / 5 | 0 | 1 | stop |
| 7 | 1235 | 20 / 5 | 0 | 1 | stop |
| 7 | 1236 | 30 / 5 | 0 | 1 | stop |
| 7 | 1237 | 70 / 5 | 0 | 1 | stop |
| 7 | 1238 | 30 / 10 | 0 | 1 | construct_objects(room=30,group_or_wave=219); stop |
| 7 | 500 | 2 / 0 | 0 | 1 | construct_objects(room=2,group_or_wave=171); stop |
| 17 | 1 | 1 / 1 | 2 | 30 | trigger_event(2); stop |
| 17 | 2 | 1 / 2 | 1 | 30 | trigger_event(3); stop |
| 17 | 3 | 1 / 3 | 3 | 40 | trigger_event(4); stop |
| 17 | 4 | 1 / 4 | 1 | 60 | set_switch(1); set_switch(71); trigger_event(5); stop |
| 17 | 5 | 20 / 1 | 5 | 1 | trigger_event(7); stop |
| 17 | 6 | 20 / 2 | 3 | 30 | trigger_event(8); stop |
| 17 | 7 | 20 / 3 | 1 | 30 | set_switch(2); stop |
| 17 | 8 | 20 / 4 | 1 | 30 | trigger_event(9); stop |
| 17 | 9 | 20 / 5 | 3 | 30 | set_switch(3); stop |
| 17 | 10 | 10 / 1 | 2 | 75 | trigger_event(11); stop |
| 17 | 11 | 10 / 2 | 4 | 30 | trigger_event(12); stop |
| 17 | 12 | 10 / 3 | 3 | 30 | trigger_event(13); stop |
| 17 | 13 | 10 / 4 | 1 | 30 | set_switch(4); trigger_event(15); stop |
| 17 | 15 | 10 / 6 | 3 | 30 | set_switch(5); stop |
| 17 | 16 | 21 / 1 | 2 | 90 | trigger_event(17); stop |
| 17 | 17 | 21 / 2 | 3 | 40 | trigger_event(18); stop |
| 17 | 18 | 21 / 3 | 3 | 30 | trigger_event(19); stop |
| 17 | 19 | 21 / 4 | 3 | 30 | set_switch(6); trigger_event(20); stop |
| 17 | 20 | 21 / 5 | 1 | 90 | set_switch(7); stop |
| 17 | 21 | 21 / 6 | 4 | 40 | trigger_event(22); stop |
| 17 | 22 | 21 / 7 | 2 | 30 | trigger_event(23); stop |
| 17 | 23 | 21 / 8 | 2 | 30 | trigger_event(24); stop |
| 17 | 24 | 21 / 9 | 1 | 40 | set_switch(8); stop |
| 17 | 25 | 2 / 1 | 3 | 30 | trigger_event(26); stop |
| 17 | 26 | 2 / 2 | 3 | 30 | trigger_event(27); stop |
| 17 | 27 | 2 / 3 | 4 | 1 | trigger_event(28); stop |
| 17 | 28 | 2 / 4 | 2 | 30 | trigger_event(29); stop |
| 17 | 29 | 2 / 5 | 4 | 30 | set_switch(9); trigger_event(30); stop |
| 17 | 30 | 2 / 6 | 5 | 120 | trigger_event(31); stop |
| 17 | 31 | 2 / 7 | 3 | 30 | trigger_event(32); stop |
| 17 | 32 | 2 / 8 | 5 | 30 | trigger_event(34); stop |
| 17 | 34 | 2 / 10 | 2 | 30 | trigger_event(35); stop |
| 17 | 35 | 2 / 11 | 4 | 40 | trigger_event(36); stop |
| 17 | 36 | 2 / 12 | 3 | 150 | set_switch(10); stop |
| 17 | 37 | 5 / 1 | 2 | 15 | set_switch(11); trigger_event(38); stop |
| 17 | 38 | 5 / 2 | 4 | 30 | trigger_event(39); stop |
| 17 | 39 | 5 / 3 | 3 | 30 | set_switch(12); construct_objects(room=5,group_or_wave=1); stop |
| 17 | 40 | 5 / 4 | 2 | 30 | trigger_event(41); stop |
| 17 | 41 | 5 / 5 | 2 | 40 | set_switch(13); trigger_event(42); stop |
| 17 | 42 | 5 / 6 | 4 | 30 | trigger_event(43); stop |
| 17 | 43 | 5 / 7 | 1 | 30 | trigger_event(44); stop |
| 17 | 44 | 5 / 8 | 1 | 30 | trigger_event(45); stop |
| 17 | 45 | 5 / 9 | 2 | 45 | set_switch(14); trigger_event(46); stop |
| 17 | 46 | 5 / 10 | 4 | 30 | trigger_event(47); stop |
| 17 | 47 | 5 / 11 | 3 | 30 | trigger_event(48); stop |
| 17 | 48 | 5 / 12 | 2 | 30 | trigger_event(50); stop |
| 17 | 50 | 5 / 14 | 6 | 30 | trigger_event(51); stop |
| 17 | 51 | 5 / 15 | 6 | 30 | set_switch(15); construct_objects(room=3,group_or_wave=1); stop |
| 17 | 52 | 3 / 0 | 0 | 1 | set_switch(16); stop |
| 17 | 53 | 3 / 1 | 4 | 150 | trigger_event(54); stop |
| 17 | 54 | 3 / 2 | 4 | 30 | trigger_event(55); stop |
| 17 | 55 | 3 / 3 | 3 | 30 | trigger_event(56); stop |
| 17 | 56 | 3 / 4 | 3 | 40 | trigger_event(57); stop |
| 17 | 57 | 3 / 5 | 4 | 30 | trigger_event(58); stop |
| 17 | 58 | 3 / 6 | 3 | 30 | trigger_event(59); stop |
| 17 | 59 | 3 / 7 | 4 | 30 | trigger_event(60); stop |
| 17 | 60 | 3 / 8 | 4 | 30 | trigger_event(61); stop |
| 17 | 61 | 3 / 9 | 5 | 40 | trigger_event(62); stop |
| 17 | 62 | 3 / 10 | 4 | 30 | trigger_event(63); stop |
| 17 | 63 | 3 / 11 | 4 | 90 | trigger_event(64); stop |
| 17 | 64 | 3 / 12 | 3 | 30 | trigger_event(65); stop |
| 17 | 65 | 3 / 13 | 4 | 15 | trigger_event(66); stop |
| 17 | 66 | 3 / 14 | 3 | 30 | trigger_event(67); stop |
| 17 | 67 | 3 / 15 | 4 | 60 | trigger_event(68); stop |
| 17 | 68 | 3 / 16 | 3 | 1 | set_switch(17); set_switch(70); stop |
| 17 | 69 | 4 / 1 | 4 | 40 | trigger_event(70); stop |
| 17 | 70 | 4 / 2 | 5 | 30 | trigger_event(71); stop |
| 17 | 71 | 4 / 3 | 3 | 60 | trigger_event(72); stop |
| 17 | 72 | 4 / 4 | 5 | 30 | set_switch(18); stop |
| 17 | 73 | 4 / 5 | 2 | 90 | trigger_event(74); stop |
| 17 | 74 | 4 / 6 | 3 | 75 | trigger_event(75); stop |
| 17 | 75 | 4 / 7 | 3 | 30 | trigger_event(76); stop |
| 17 | 76 | 4 / 8 | 3 | 30 | trigger_event(77); stop |
| 17 | 77 | 4 / 9 | 3 | 30 | trigger_event(78); stop |
| 17 | 78 | 4 / 10 | 3 | 30 | set_switch(19); construct_objects(room=4,group_or_wave=1); stop |
| 17 | 79 | 4 / 11 | 4 | 30 | trigger_event(80); stop |
| 17 | 80 | 4 / 12 | 4 | 30 | trigger_event(81); stop |
| 17 | 81 | 4 / 13 | 4 | 30 | set_switch(20); trigger_event(82); trigger_event(83); stop |
| 17 | 82 | 4 / 14 | 4 | 30 | set_switch(1); trigger_event(84); stop |
| 17 | 83 | 4 / 15 | 3 | 120 | set_switch(1); trigger_event(85); stop |
| 17 | 84 | 4 / 16 | 3 | 30 | trigger_event(86); stop |
| 17 | 85 | 4 / 17 | 4 | 30 | trigger_event(87); stop |
| 17 | 86 | 4 / 18 | 3 | 30 | trigger_event(88); stop |
| 17 | 87 | 4 / 19 | 3 | 30 | trigger_event(89); stop |
| 17 | 88 | 4 / 20 | 1 | 30 | trigger_event(90); stop |
| 17 | 89 | 4 / 21 | 1 | 30 | trigger_event(91); stop |
| 17 | 90 | 4 / 22 | 1 | 30 | trigger_event(92); stop |
| 17 | 91 | 4 / 23 | 1 | 30 | trigger_event(93); stop |
| 17 | 92 | 4 / 24 | 4 | 30 | set_switch(210); stop |
| 17 | 93 | 4 / 25 | 4 | 30 | set_switch(211); stop |
| 17 | 94 | 4 / 26 | 3 | 30 | trigger_event(95); stop |
| 17 | 95 | 4 / 27 | 7 | 30 | trigger_event(96); stop |
| 17 | 96 | 4 / 28 | 6 | 150 | set_switch(21); clear_switch(73); stop |
| 17 | 97 | 22 / 1 | 3 | 30 | trigger_event(98); stop |
| 17 | 98 | 22 / 2 | 4 | 30 | trigger_event(99); stop |
| 17 | 99 | 22 / 3 | 4 | 30 | trigger_event(100); stop |
| 17 | 100 | 22 / 4 | 3 | 30 | trigger_event(101); stop |
| 17 | 101 | 22 / 5 | 4 | 30 | trigger_event(142); stop |
| 17 | 142 | 22 / 6 | 3 | 30 | trigger_event(102); stop |
| 17 | 102 | 22 / 7 | 3 | 30 | trigger_event(103); set_switch(22); trigger_event(104); stop |
| 17 | 104 | 22 / 8 | 2 | 100 | trigger_event(105); stop |
| 17 | 105 | 22 / 9 | 7 | 30 | trigger_event(106); stop |
| 17 | 106 | 22 / 10 | 5 | 60 | trigger_event(107); stop |
| 17 | 107 | 22 / 11 | 7 | 30 | trigger_event(108); stop |
| 17 | 108 | 22 / 12 | 4 | 40 | set_switch(23); construct_objects(room=22,group_or_wave=1); construct_objects(room=22,group_or_wave=2); construct_objects(room=1,group_or_wave=1); stop |
| 17 | 109 | 22 / 13 | 3 | 45 | trigger_event(110); stop |
| 17 | 110 | 22 / 14 | 3 | 60 | clear_switch(71); set_switch(73); trigger_event(111); trigger_event(112); trigger_event(113); stop |
| 17 | 111 | 22 / 15 | 2 | 120 | trigger_event(114); stop |
| 17 | 112 | 22 / 16 | 2 | 210 | trigger_event(115); stop |
| 17 | 113 | 22 / 17 | 1 | 300 | trigger_event(116); stop |
| 17 | 114 | 22 / 18 | 2 | 30 | trigger_event(117); stop |
| 17 | 115 | 22 / 19 | 2 | 30 | trigger_event(118); stop |
| 17 | 116 | 22 / 20 | 3 | 30 | trigger_event(119); stop |
| 17 | 117 | 22 / 21 | 2 | 30 | trigger_event(120); stop |
| 17 | 118 | 22 / 22 | 3 | 30 | trigger_event(121); stop |
| 17 | 119 | 22 / 23 | 2 | 30 | trigger_event(122); stop |
| 17 | 120 | 22 / 24 | 1 | 30 | trigger_event(123); stop |
| 17 | 121 | 22 / 25 | 3 | 30 | trigger_event(124); stop |
| 17 | 122 | 22 / 26 | 3 | 30 | trigger_event(125); stop |
| 17 | 123 | 22 / 27 | 2 | 30 | trigger_event(126); stop |
| 17 | 124 | 22 / 28 | 2 | 30 | trigger_event(127); stop |
| 17 | 125 | 22 / 29 | 2 | 30 | trigger_event(128); stop |
| 17 | 126 | 22 / 30 | 2 | 30 | trigger_event(129); stop |
| 17 | 127 | 22 / 31 | 1 | 30 | trigger_event(130); stop |
| 17 | 128 | 22 / 32 | 2 | 30 | trigger_event(131); stop |
| 17 | 129 | 22 / 33 | 2 | 30 | trigger_event(132); stop |
| 17 | 130 | 22 / 34 | 2 | 30 | trigger_event(133); stop |
| 17 | 131 | 22 / 35 | 3 | 30 | trigger_event(134); stop |
| 17 | 132 | 22 / 36 | 2 | 30 | trigger_event(135); stop |
| 17 | 133 | 22 / 37 | 4 | 30 | trigger_event(136); stop |
| 17 | 134 | 22 / 38 | 4 | 30 | trigger_event(137); stop |
| 17 | 135 | 22 / 39 | 4 | 30 | trigger_event(138); stop |
| 17 | 136 | 22 / 40 | 4 | 30 | trigger_event(139); stop |
| 17 | 137 | 22 / 41 | 2 | 30 | trigger_event(140); stop |
| 17 | 138 | 22 / 42 | 5 | 150 | set_switch(24); stop |
| 17 | 139 | 22 / 43 | 2 | 30 | set_switch(25); stop |
| 17 | 140 | 22 / 44 | 1 | 30 | set_switch(26); stop |
| 17 | 141 | 22 / 45 | 14 | 300 | set_switch(27); set_switch(71); set_switch(75); stop |

## Review notes

- Nonzero data after terminal header
- Floor 17: event 102 targets absent event 103
