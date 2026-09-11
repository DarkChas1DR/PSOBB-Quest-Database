# Penumbral Surge #4 — extermination-ep2/q174-bb-e

Episode2; header quest ID 174; language E. Static scan: **353 objects, 384 enemy/NPC records, 140 events, 120 script labels.** Script roundtrip: byte-identical.

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
| 0 | 53 | 10 | 0 |
| 5 | 300 | 374 | 140 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 5 | 1 | 8 / 1 | 2 | 1 | trigger_event(2); stop |
| 5 | 2 | 8 / 2 | 1 | 30 | set_switch(2); set_switch(50); stop |
| 5 | 4 | 9 / 1 | 4 | 20 | trigger_event(5); stop |
| 5 | 5 | 9 / 2 | 6 | 40 | trigger_event(6); stop |
| 5 | 6 | 9 / 3 | 3 | 35 | set_switch(3); set_switch(51); stop |
| 5 | 7 | 10 / 1 | 1 | 15 | trigger_event(8); stop |
| 5 | 8 | 10 / 2 | 3 | 30 | set_switch(4); stop |
| 5 | 9 | 6 / 1 | 3 | 30 | set_switch(5); set_switch(52); stop |
| 5 | 10 | 5 / 1 | 4 | 30 | trigger_event(11); stop |
| 5 | 11 | 5 / 2 | 5 | 40 | trigger_event(12); stop |
| 5 | 12 | 5 / 3 | 3 | 35 | trigger_event(13); stop |
| 5 | 13 | 5 / 4 | 6 | 30 | set_switch(6); set_switch(53); stop |
| 5 | 14 | 4 / 1 | 1 | 40 | trigger_event(15); stop |
| 5 | 15 | 4 / 2 | 5 | 35 | trigger_event(16); stop |
| 5 | 16 | 4 / 3 | 5 | 30 | trigger_event(17); stop |
| 5 | 17 | 4 / 4 | 4 | 35 | set_switch(7); set_switch(54); stop |
| 5 | 18 | 3 / 1 | 5 | 30 | trigger_event(19); stop |
| 5 | 19 | 3 / 2 | 5 | 40 | set_switch(8); set_switch(55); stop |
| 5 | 20 | 2 / 1 | 6 | 75 | trigger_event(21); stop |
| 5 | 21 | 2 / 2 | 4 | 35 | trigger_event(22); stop |
| 5 | 22 | 2 / 3 | 3 | 30 | trigger_event(23); set_switch(9); set_switch(56); stop |
| 5 | 23 | 1 / 1 | 3 | 1 | set_switch(10); stop |
| 5 | 24 | 13 / 1 | 2 | 30 | trigger_event(26); stop |
| 5 | 25 | 13 / 2 | 1 | 30 | trigger_event(27); stop |
| 5 | 26 | 13 / 3 | 3 | 30 | trigger_event(28); stop |
| 5 | 27 | 13 / 4 | 2 | 30 | trigger_event(29); stop |
| 5 | 28 | 13 / 5 | 2 | 30 | trigger_event(30); stop |
| 5 | 29 | 13 / 6 | 3 | 30 | trigger_event(31); stop |
| 5 | 30 | 13 / 7 | 4 | 30 | trigger_event(32); stop |
| 5 | 31 | 13 / 8 | 2 | 30 | trigger_event(33); stop |
| 5 | 32 | 13 / 9 | 1 | 30 | set_switch(100); stop |
| 5 | 33 | 13 / 10 | 1 | 10 | set_switch(101); stop |
| 5 | 34 | 13 / 11 | 0 | 1 | trigger_event(500); construct_objects(room=1,group_or_wave=1); construct_objects(room=2,group_or_wave=1); construct_objects(room=3,group_or_wave=1); construct_objects(room=4,group_or_wave=1); construct_objects(room=5,group_or_wave=1); construct_objects(room=6,group_or_wave=1); construct_objects(room=7,group_or_wave=1); construct_objects(room=8,group_or_wave=1); construct_objects(room=9,group_or_wave=1); construct_objects(room=10,group_or_wave=1); construct_objects(room=11,group_or_wave=1); construct_objects(room=12,group_or_wave=1); clear_switch(10); clear_switch(50); clear_switch(51); clear_switch(52); clear_switch(53); clear_switch(54); clear_switch(55); clear_switch(56); stop |
| 5 | 35 | 8 / 4 | 2 | 20 | trigger_event(36); stop |
| 5 | 36 | 8 / 5 | 1 | 45 | set_switch(1); construct_objects(room=8,group_or_wave=3); stop |
| 5 | 37 | 8 / 6 | 4 | 35 | trigger_event(38); stop |
| 5 | 38 | 8 / 7 | 4 | 45 | set_switch(13); set_switch(50); construct_objects(room=9,group_or_wave=3); stop |
| 5 | 39 | 9 / 4 | 2 | 40 | trigger_event(40); stop |
| 5 | 40 | 9 / 5 | 5 | 30 | set_switch(14); set_switch(51); construct_objects(room=10,group_or_wave=3); stop |
| 5 | 41 | 10 / 3 | 4 | 30 | trigger_event(42); stop |
| 5 | 42 | 10 / 4 | 3 | 35 | set_switch(15); construct_objects(room=7,group_or_wave=3); stop |
| 5 | 44 | 7 / 2 | 1 | 30 | trigger_event(45); stop |
| 5 | 45 | 7 / 3 | 2 | 35 | set_switch(16); construct_objects(room=6,group_or_wave=3); stop |
| 5 | 46 | 6 / 2 | 1 | 30 | trigger_event(47); stop |
| 5 | 47 | 6 / 3 | 2 | 30 | set_switch(12); trigger_event(48); stop |
| 5 | 48 | 6 / 4 | 4 | 45 | trigger_event(49); stop |
| 5 | 49 | 6 / 5 | 2 | 45 | set_switch(17); set_switch(52); construct_objects(room=5,group_or_wave=3); stop |
| 5 | 50 | 5 / 5 | 3 | 60 | trigger_event(51); stop |
| 5 | 51 | 5 / 6 | 6 | 40 | trigger_event(52); stop |
| 5 | 52 | 5 / 7 | 4 | 35 | set_switch(18); set_switch(53); construct_objects(room=4,group_or_wave=3); stop |
| 5 | 53 | 4 / 5 | 5 | 50 | trigger_event(54); stop |
| 5 | 54 | 4 / 6 | 4 | 40 | trigger_event(56); stop |
| 5 | 56 | 4 / 8 | 4 | 30 | set_switch(19); set_switch(54); construct_objects(room=3,group_or_wave=3); stop |
| 5 | 57 | 3 / 3 | 1 | 40 | trigger_event(58); stop |
| 5 | 58 | 3 / 4 | 6 | 35 | trigger_event(59); stop |
| 5 | 59 | 3 / 5 | 5 | 35 | set_switch(20); set_switch(55); construct_objects(room=2,group_or_wave=3); stop |
| 5 | 60 | 2 / 4 | 1 | 30 | set_switch(102); stop |
| 5 | 61 | 2 / 5 | 2 | 1 | set_switch(103); stop |
| 5 | 62 | 2 / 0 | 0 | 1 | construct_objects(room=1,group_or_wave=3); stop |
| 5 | 63 | 1 / 2 | 2 | 30 | trigger_event(64); stop |
| 5 | 64 | 1 / 3 | 2 | 50 | set_switch(22); stop |
| 5 | 65 | 12 / 1 | 3 | 40 | trigger_event(67); stop |
| 5 | 66 | 12 / 2 | 2 | 40 | trigger_event(68); stop |
| 5 | 67 | 12 / 3 | 2 | 35 | trigger_event(69); stop |
| 5 | 68 | 12 / 4 | 1 | 35 | trigger_event(70); stop |
| 5 | 69 | 12 / 5 | 2 | 35 | trigger_event(71); stop |
| 5 | 70 | 12 / 6 | 3 | 35 | trigger_event(72); stop |
| 5 | 71 | 12 / 7 | 2 | 35 | trigger_event(73); stop |
| 5 | 72 | 12 / 8 | 1 | 35 | trigger_event(74); stop |
| 5 | 73 | 12 / 9 | 1 | 35 | trigger_event(75); stop |
| 5 | 74 | 12 / 10 | 1 | 35 | set_switch(104); stop |
| 5 | 75 | 12 / 11 | 1 | 35 | set_switch(105); stop |
| 5 | 76 | 12 / 12 | 1 | 45 | trigger_event(501); set_switch(23); stop |
| 5 | 510 | 12 / 66 | 0 | 1 | construct_objects(room=1,group_or_wave=2); construct_objects(room=2,group_or_wave=2); construct_objects(room=3,group_or_wave=2); construct_objects(room=4,group_or_wave=2); construct_objects(room=5,group_or_wave=2); construct_objects(room=6,group_or_wave=2); construct_objects(room=7,group_or_wave=2); construct_objects(room=8,group_or_wave=2); construct_objects(room=9,group_or_wave=2); construct_objects(room=10,group_or_wave=2); construct_objects(room=11,group_or_wave=2); construct_objects(room=8,group_or_wave=4); clear_switch(22); clear_switch(16); clear_switch(50); clear_switch(51); clear_switch(52); clear_switch(53); clear_switch(54); clear_switch(55); clear_switch(56); stop |
| 5 | 77 | 8 / 8 | 1 | 20 | set_switch(1); trigger_event(78); stop |
| 5 | 78 | 8 / 9 | 4 | 45 | trigger_event(79); stop |
| 5 | 79 | 8 / 10 | 1 | 35 | set_switch(24); trigger_event(80); stop |
| 5 | 80 | 8 / 11 | 2 | 50 | trigger_event(81); stop |
| 5 | 81 | 8 / 12 | 5 | 40 | trigger_event(82); stop |
| 5 | 82 | 8 / 13 | 1 | 30 | set_switch(25); set_switch(50); construct_objects(room=9,group_or_wave=4); stop |
| 5 | 83 | 9 / 6 | 2 | 90 | trigger_event(84); stop |
| 5 | 84 | 9 / 7 | 2 | 40 | trigger_event(85); stop |
| 5 | 85 | 9 / 8 | 3 | 40 | set_switch(26); set_switch(51); construct_objects(room=10,group_or_wave=4); stop |
| 5 | 86 | 10 / 5 | 4 | 45 | set_switch(27); construct_objects(room=7,group_or_wave=4); stop |
| 5 | 87 | 7 / 4 | 5 | 45 | set_switch(16); set_switch(28); construct_objects(room=6,group_or_wave=4); stop |
| 5 | 88 | 6 / 6 | 3 | 45 | set_switch(29); construct_objects(room=6,group_or_wave=5); stop |
| 5 | 89 | 6 / 7 | 2 | 45 | set_switch(30); construct_objects(room=6,group_or_wave=6); stop |
| 5 | 90 | 6 / 8 | 2 | 45 | set_switch(31); set_switch(32); set_switch(52); construct_objects(room=5,group_or_wave=4); stop |
| 5 | 92 | 5 / 8 | 3 | 45 | trigger_event(93); stop |
| 5 | 93 | 5 / 9 | 6 | 40 | trigger_event(94); stop |
| 5 | 94 | 5 / 10 | 2 | 35 | set_switch(33); construct_objects(room=5,group_or_wave=5); stop |
| 5 | 95 | 5 / 11 | 2 | 45 | trigger_event(96); stop |
| 5 | 96 | 5 / 12 | 7 | 45 | trigger_event(97); stop |
| 5 | 97 | 5 / 13 | 5 | 45 | trigger_event(98); stop |
| 5 | 98 | 5 / 14 | 4 | 40 | set_switch(34); set_switch(53); construct_objects(room=4,group_or_wave=4); stop |
| 5 | 99 | 4 / 9 | 3 | 40 | trigger_event(100); stop |
| 5 | 100 | 4 / 10 | 2 | 45 | set_switch(35); trigger_event(101); stop |
| 5 | 101 | 4 / 11 | 3 | 1 | set_switch(36); set_switch(54); construct_objects(room=3,group_or_wave=4); stop |
| 5 | 102 | 3 / 6 | 8 | 40 | trigger_event(103); stop |
| 5 | 103 | 3 / 7 | 3 | 35 | trigger_event(104); stop |
| 5 | 104 | 3 / 8 | 4 | 40 | set_switch(37); set_switch(55); construct_objects(room=2,group_or_wave=4); stop |
| 5 | 105 | 2 / 6 | 1 | 35 | trigger_event(106); stop |
| 5 | 106 | 2 / 7 | 2 | 40 | trigger_event(107); stop |
| 5 | 107 | 2 / 8 | 1 | 40 | trigger_event(108); stop |
| 5 | 108 | 2 / 9 | 3 | 45 | set_switch(38); trigger_event(109); stop |
| 5 | 109 | 2 / 10 | 2 | 120 | set_switch(39); construct_objects(room=1,group_or_wave=4); stop |
| 5 | 111 | 1 / 4 | 3 | 30 | set_switch(40); construct_objects(room=1,group_or_wave=3); stop |
| 5 | 112 | 11 / 1 | 2 | 30 | trigger_event(114); stop |
| 5 | 113 | 11 / 2 | 2 | 30 | trigger_event(115); stop |
| 5 | 114 | 11 / 3 | 1 | 30 | trigger_event(116); stop |
| 5 | 115 | 11 / 4 | 2 | 30 | trigger_event(117); stop |
| 5 | 116 | 11 / 5 | 3 | 30 | trigger_event(118); stop |
| 5 | 117 | 11 / 6 | 2 | 30 | trigger_event(119); stop |
| 5 | 118 | 11 / 7 | 1 | 30 | trigger_event(120); stop |
| 5 | 119 | 11 / 8 | 3 | 30 | trigger_event(121); stop |
| 5 | 120 | 11 / 9 | 3 | 30 | trigger_event(122); stop |
| 5 | 121 | 11 / 10 | 4 | 30 | trigger_event(123); stop |
| 5 | 122 | 11 / 11 | 3 | 30 | trigger_event(124); stop |
| 5 | 123 | 11 / 12 | 1 | 30 | trigger_event(125); stop |
| 5 | 124 | 11 / 13 | 1 | 30 | trigger_event(126); stop |
| 5 | 125 | 11 / 14 | 2 | 30 | trigger_event(127); stop |
| 5 | 126 | 11 / 15 | 3 | 30 | trigger_event(128); stop |
| 5 | 127 | 11 / 16 | 3 | 30 | trigger_event(129); stop |
| 5 | 128 | 11 / 17 | 2 | 30 | trigger_event(130); stop |
| 5 | 129 | 11 / 18 | 4 | 30 | trigger_event(131); stop |
| 5 | 130 | 11 / 19 | 2 | 30 | set_switch(108); stop |
| 5 | 131 | 11 / 20 | 1 | 30 | set_switch(109); stop |
| 5 | 132 | 11 / 21 | 2 | 30 | trigger_event(134); stop |
| 5 | 133 | 11 / 22 | 3 | 30 | trigger_event(135); stop |
| 5 | 134 | 11 / 23 | 2 | 30 | trigger_event(136); stop |
| 5 | 135 | 11 / 24 | 3 | 30 | trigger_event(137); stop |
| 5 | 136 | 11 / 25 | 1 | 30 | trigger_event(138); stop |
| 5 | 137 | 11 / 26 | 1 | 30 | trigger_event(139); stop |
| 5 | 138 | 11 / 27 | 4 | 30 | trigger_event(140); stop |
| 5 | 139 | 11 / 28 | 1 | 30 | trigger_event(141); stop |
| 5 | 140 | 11 / 29 | 3 | 30 | set_switch(106); stop |
| 5 | 141 | 11 / 30 | 1 | 30 | set_switch(107); stop |
| 5 | 142 | 11 / 31 | 2 | 45 | set_switch(110); construct_objects(room=11,group_or_wave=11); stop |
| 5 | 500 | 13 / 55 | 0 | 300 | construct_objects(room=13,group_or_wave=1); stop |
| 5 | 501 | 12 / 55 | 0 | 300 | construct_objects(room=12,group_or_wave=2); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
