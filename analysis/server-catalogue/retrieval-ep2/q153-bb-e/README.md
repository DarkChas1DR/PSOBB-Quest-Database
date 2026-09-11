# Lost FILL CANNON — retrieval-ep2/q153-bb-e

Episode2; header quest ID 153; language E. Static scan: **960 objects, 670 enemy/NPC records, 160 events, 72 script labels.** Script roundtrip: alignment-only.

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
| 0 | 38 | 8 | 0 |
| 5 | 166 | 137 | 28 |
| 6 | 189 | 139 | 41 |
| 7 | 148 | 108 | 29 |
| 8 | 225 | 147 | 33 |
| 9 | 172 | 130 | 28 |
| 12 | 22 | 1 | 1 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 5 | 21 | 2 / 1 | 5 | 1 | trigger_event(22); stop |
| 5 | 22 | 2 / 2 | 5 | 30 | trigger_event(23); stop |
| 5 | 23 | 2 / 3 | 8 | 30 | set_switch(2); stop |
| 5 | 31 | 3 / 1 | 4 | 1 | trigger_event(32); stop |
| 5 | 32 | 3 / 2 | 5 | 30 | trigger_event(33); stop |
| 5 | 33 | 3 / 3 | 5 | 30 | set_switch(3); trigger_event(41); stop |
| 5 | 41 | 4 / 1 | 8 | 1 | trigger_event(42); stop |
| 5 | 42 | 4 / 2 | 3 | 30 | trigger_event(43); stop |
| 5 | 43 | 4 / 3 | 6 | 30 | set_switch(4); stop |
| 5 | 51 | 5 / 1 | 5 | 10 | set_switch(5); construct_objects(room=5,group_or_wave=1); stop |
| 5 | 52 | 5 / 2 | 5 | 10 | set_switch(6); construct_objects(room=5,group_or_wave=2); stop |
| 5 | 53 | 5 / 3 | 5 | 10 | set_switch(7); trigger_event(54); stop |
| 5 | 54 | 5 / 4 | 3 | 30 | trigger_event(55); stop |
| 5 | 55 | 5 / 5 | 3 | 30 | set_switch(8); stop |
| 5 | 131 | 13 / 1 | 2 | 5 | construct_objects(room=13,group_or_wave=1); set_switch(201); stop |
| 5 | 81 | 8 / 1 | 5 | 5 | trigger_event(82); stop |
| 5 | 82 | 8 / 2 | 6 | 30 | construct_objects(room=8,group_or_wave=1); stop |
| 5 | 121 | 12 / 1 | 2 | 5 | trigger_event(122); stop |
| 5 | 122 | 12 / 2 | 6 | 15 | trigger_event(123); stop |
| 5 | 123 | 12 / 3 | 6 | 5 | construct_objects(room=12,group_or_wave=1); set_switch(202); stop |
| 5 | 91 | 9 / 1 | 5 | 5 | trigger_event(92); stop |
| 5 | 92 | 9 / 2 | 5 | 30 | construct_objects(room=9,group_or_wave=1); stop |
| 5 | 111 | 11 / 1 | 5 | 5 | trigger_event(112); stop |
| 5 | 112 | 11 / 2 | 6 | 5 | trigger_event(113); stop |
| 5 | 113 | 11 / 3 | 3 | 5 | trigger_event(114); stop |
| 5 | 114 | 11 / 4 | 4 | 5 | trigger_event(115); stop |
| 5 | 115 | 11 / 5 | 5 | 5 | construct_objects(room=11,group_or_wave=1); set_switch(203); stop |
| 5 | 101 | 10 / 1 | 6 | 5 | construct_objects(room=10,group_or_wave=1); stop |
| 6 | 20105 | 11 / 0 | 0 | 1 | set_switch(105); stop |
| 6 | 81 | 8 / 1 | 4 | 1 | trigger_event(82); stop |
| 6 | 82 | 8 / 2 | 1 | 30 | set_switch(1); stop |
| 6 | 41 | 4 / 1 | 5 | 10 | trigger_event(42); stop |
| 6 | 42 | 4 / 2 | 4 | 30 | trigger_event(43); stop |
| 6 | 43 | 4 / 3 | 4 | 30 | trigger_event(44); stop |
| 6 | 44 | 4 / 4 | 7 | 30 | trigger_event(45); stop |
| 6 | 45 | 4 / 5 | 1 | 30 | trigger_event(46); stop |
| 6 | 46 | 4 / 6 | 2 | 45 | set_switch(2); stop |
| 6 | 61 | 6 / 1 | 3 | 15 | trigger_event(62); stop |
| 6 | 62 | 6 / 2 | 3 | 10 | construct_objects(room=6,group_or_wave=1); stop |
| 6 | 150 | 15 / 0 | 0 | 1 | trigger_event(151); trigger_event(1510); stop |
| 6 | 151 | 15 / 1 | 2 | 20 | trigger_event(152); stop |
| 6 | 1510 | 15 / 10 | 3 | 20 | trigger_event(1512); stop |
| 6 | 152 | 15 / 2 | 4 | 30 | stop |
| 6 | 153 | 15 / 3 | 2 | 1 | trigger_event(154); stop |
| 6 | 154 | 15 / 4 | 1 | 30 | trigger_event(155); stop |
| 6 | 155 | 15 / 5 | 1 | 30 | set_switch(201); stop |
| 6 | 156 | 15 / 6 | 4 | 30 | trigger_event(157); stop |
| 6 | 157 | 15 / 7 | 7 | 30 | trigger_event(158); stop |
| 6 | 158 | 15 / 8 | 2 | 45 | set_switch(4); stop |
| 6 | 1512 | 15 / 12 | 3 | 30 | stop |
| 6 | 1599 | 15 / 0 | 0 | 1 | set_switch(102); construct_objects(room=15,group_or_wave=1); trigger_event(1511); stop |
| 6 | 1511 | 15 / 11 | 1 | 120 | stop |
| 6 | 121 | 12 / 1 | 1 | 1 | set_switch(5); stop |
| 6 | 111 | 11 / 1 | 5 | 30 | trigger_event(112); stop |
| 6 | 112 | 11 / 2 | 5 | 30 | trigger_event(113); stop |
| 6 | 113 | 11 / 3 | 5 | 30 | trigger_event(114); stop |
| 6 | 114 | 11 / 4 | 8 | 30 | trigger_event(115); stop |
| 6 | 115 | 11 / 5 | 6 | 60 | trigger_event(116); stop |
| 6 | 116 | 11 / 6 | 7 | 15 | trigger_event(117); stop |
| 6 | 117 | 11 / 7 | 7 | 30 | set_switch(6); stop |
| 6 | 1199 | 11 / 0 | 0 | 1 | set_switch(101); stop |
| 6 | 11 | 1 / 1 | 3 | 15 | set_switch(7); set_switch(8); stop |
| 6 | 31 | 3 / 1 | 5 | 10 | trigger_event(32); stop |
| 6 | 32 | 3 / 2 | 5 | 15 | trigger_event(33); stop |
| 6 | 33 | 3 / 3 | 3 | 45 | trigger_event(34); stop |
| 6 | 34 | 3 / 4 | 8 | 45 | trigger_event(35); stop |
| 6 | 35 | 3 / 5 | 5 | 15 | set_switch(109); set_switch(9); stop |
| 6 | 310 | 3 / 10 | 2 | 90 | set_switch(202); stop |
| 6 | 3099 | 3 / 0 | 0 | 90 | set_switch(109); set_switch(9); stop |
| 7 | 9901 | 2 / 0 | 0 | 1 | construct_objects(room=2,group_or_wave=1); stop |
| 7 | 9902 | 2 / 0 | 0 | 1 | construct_objects(room=2,group_or_wave=2); stop |
| 7 | 9903 | 4 / 0 | 0 | 1 | construct_objects(room=4,group_or_wave=1); stop |
| 7 | 9904 | 5 / 0 | 0 | 1 | construct_objects(room=5,group_or_wave=1); stop |
| 7 | 71 | 7 / 1 | 3 | 30 | trigger_event(72); stop |
| 7 | 72 | 7 / 2 | 5 | 30 | set_switch(1); stop |
| 7 | 11 | 1 / 1 | 1 | 1 | set_switch(2); construct_objects(room=2,group_or_wave=1); stop |
| 7 | 21 | 2 / 1 | 5 | 30 | trigger_event(22); stop |
| 7 | 22 | 2 / 2 | 3 | 30 | trigger_event(23); stop |
| 7 | 23 | 2 / 3 | 7 | 30 | set_switch(3); stop |
| 7 | 31 | 3 / 1 | 5 | 60 | trigger_event(32); stop |
| 7 | 32 | 3 / 2 | 6 | 30 | trigger_event(33); stop |
| 7 | 33 | 3 / 3 | 6 | 45 | set_switch(4); stop |
| 7 | 81 | 8 / 1 | 4 | 1 | trigger_event(82); stop |
| 7 | 82 | 8 / 2 | 7 | 15 | set_switch(5); stop |
| 7 | 61 | 6 / 1 | 5 | 30 | set_switch(6); stop |
| 7 | 51 | 5 / 1 | 4 | 30 | trigger_event(52); stop |
| 7 | 52 | 5 / 2 | 4 | 15 | trigger_event(53); stop |
| 7 | 53 | 5 / 3 | 5 | 15 | construct_objects(room=5,group_or_wave=1); trigger_event(54); stop |
| 7 | 54 | 5 / 4 | 2 | 75 | trigger_event(55); stop |
| 7 | 55 | 5 / 5 | 5 | 30 | trigger_event(56); stop |
| 7 | 56 | 5 / 6 | 2 | 60 | trigger_event(57); stop |
| 7 | 57 | 5 / 7 | 8 | 30 | trigger_event(58); stop |
| 7 | 58 | 5 / 8 | 2 | 60 | trigger_event(59); stop |
| 7 | 59 | 5 / 9 | 4 | 30 | trigger_event(510); stop |
| 7 | 510 | 5 / 10 | 3 | 60 | set_switch(7); set_switch(110); stop |
| 7 | 519 | 5 / 19 | 6 | 150 | trigger_event(520); stop |
| 7 | 520 | 5 / 20 | 3 | 90 | trigger_event(521); stop |
| 7 | 521 | 5 / 21 | 2 | 90 | stop |
| 8 | 20105 | 2 / 0 | 0 | 1 | set_switch(105); construct_objects(room=2,group_or_wave=1); stop |
| 8 | 8099 | 8 / 0 | 0 | 1 | construct_objects(room=8,group_or_wave=1); stop |
| 8 | 21 | 2 / 1 | 5 | 1 | trigger_event(22); stop |
| 8 | 22 | 2 / 2 | 5 | 30 | trigger_event(23); stop |
| 8 | 23 | 2 / 3 | 3 | 30 | trigger_event(24); stop |
| 8 | 24 | 2 / 4 | 5 | 30 | set_switch(1); stop |
| 8 | 25 | 2 / 5 | 5 | 75 | trigger_event(26); stop |
| 8 | 26 | 2 / 6 | 6 | 30 | set_switch(2); trigger_event(31); stop |
| 8 | 31 | 3 / 1 | 4 | 75 | trigger_event(32); stop |
| 8 | 32 | 3 / 2 | 4 | 30 | trigger_event(33); stop |
| 8 | 33 | 3 / 3 | 4 | 30 | trigger_event(34); stop |
| 8 | 34 | 3 / 4 | 6 | 30 | set_switch(3); stop |
| 8 | 35 | 3 / 5 | 5 | 1 | trigger_event(36); stop |
| 8 | 36 | 3 / 6 | 6 | 30 | trigger_event(37); stop |
| 8 | 37 | 3 / 7 | 4 | 30 | set_switch(4); stop |
| 8 | 41 | 4 / 1 | 4 | 1 | trigger_event(42); stop |
| 8 | 42 | 4 / 2 | 4 | 30 | trigger_event(43); stop |
| 8 | 43 | 4 / 3 | 5 | 30 | trigger_event(44); stop |
| 8 | 44 | 4 / 4 | 6 | 30 | set_switch(5); stop |
| 8 | 101 | 10 / 1 | 5 | 15 | set_switch(6); trigger_event(51); stop |
| 8 | 51 | 5 / 1 | 6 | 30 | trigger_event(52); stop |
| 8 | 27 | 2 / 7 | 1 | 1 | stop |
| 8 | 52 | 5 / 2 | 8 | 30 | trigger_event(53); stop |
| 8 | 53 | 5 / 3 | 8 | 30 | set_switch(8); stop |
| 8 | 71 | 7 / 1 | 2 | 1 | set_switch(12); stop |
| 8 | 81 | 8 / 1 | 5 | 1 | trigger_event(82); stop |
| 8 | 82 | 8 / 2 | 6 | 30 | trigger_event(83); stop |
| 8 | 83 | 8 / 3 | 5 | 30 | trigger_event(84); stop |
| 8 | 84 | 8 / 4 | 4 | 30 | set_switch(13); stop |
| 8 | 85 | 8 / 5 | 0 | 30 | trigger_event(86); stop |
| 8 | 86 | 8 / 6 | 5 | 30 | trigger_event(87); stop |
| 8 | 87 | 8 / 7 | 6 | 30 | trigger_event(88); stop |
| 8 | 88 | 8 / 8 | 5 | 30 | set_switch(14); stop |
| 9 | 20105 | 11 / 0 | 0 | 1 | set_switch(105); stop |
| 9 | 31 | 3 / 1 | 5 | 1 | trigger_event(32); stop |
| 9 | 32 | 3 / 2 | 5 | 30 | trigger_event(33); stop |
| 9 | 33 | 3 / 3 | 5 | 30 | trigger_event(34); stop |
| 9 | 34 | 3 / 4 | 6 | 30 | set_switch(202); stop |
| 9 | 310 | 3 / 10 | 5 | 1 | trigger_event(311); stop |
| 9 | 311 | 3 / 11 | 7 | 30 | trigger_event(312); stop |
| 9 | 312 | 3 / 12 | 5 | 30 | trigger_event(313); stop |
| 9 | 313 | 3 / 13 | 7 | 30 | set_switch(1); set_switch(2); stop |
| 9 | 320 | 3 / 20 | 6 | 90 | set_switch(201); stop |
| 9 | 111 | 11 / 1 | 6 | 30 | trigger_event(112); stop |
| 9 | 112 | 11 / 2 | 7 | 30 | trigger_event(113); stop |
| 9 | 113 | 11 / 3 | 5 | 30 | set_switch(3); trigger_event(101); stop |
| 9 | 101 | 10 / 1 | 5 | 15 | trigger_event(102); stop |
| 9 | 102 | 10 / 2 | 1 | 30 | set_switch(4); stop |
| 9 | 91 | 9 / 1 | 7 | 1 | trigger_event(92); stop |
| 9 | 92 | 9 / 2 | 6 | 30 | trigger_event(93); stop |
| 9 | 93 | 9 / 3 | 6 | 30 | set_switch(5); set_switch(6); stop |
| 9 | 141 | 14 / 1 | 1 | 1 | stop |
| 9 | 71 | 7 / 1 | 4 | 1 | trigger_event(72); stop |
| 9 | 72 | 7 / 2 | 2 | 30 | trigger_event(710); trigger_event(73); stop |
| 9 | 710 | 7 / 10 | 5 | 30 | trigger_event(711); stop |
| 9 | 73 | 7 / 3 | 5 | 60 | trigger_event(74); stop |
| 9 | 74 | 7 / 4 | 5 | 30 | trigger_event(75); stop |
| 9 | 75 | 7 / 5 | 3 | 30 | trigger_event(76); stop |
| 9 | 76 | 7 / 6 | 1 | 30 | set_switch(7); set_switch(100); stop |
| 9 | 711 | 7 / 11 | 6 | 30 | trigger_event(712); stop |
| 9 | 712 | 7 / 12 | 4 | 30 | set_switch(8); stop |
| 12 | 1 | 1 / 1 | 1 | 50 | construct_objects(room=1,group_or_wave=1); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
