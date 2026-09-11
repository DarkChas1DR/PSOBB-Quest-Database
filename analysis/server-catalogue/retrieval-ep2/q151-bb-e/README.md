# Lost CHARGE VULCAN — retrieval-ep2/q151-bb-e

Episode2; header quest ID 151; language E. Static scan: **446 objects, 266 enemy/NPC records, 148 events, 97 script labels.** Script roundtrip: byte-identical.

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
| 0 | 37 | 9 | 0 |
| 16 | 201 | 137 | 70 |
| 17 | 208 | 120 | 78 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 16 | 301 | 30 / 1 | 2 | 60 | trigger_event(302); stop |
| 16 | 302 | 30 / 2 | 1 | 40 | trigger_event(303); stop |
| 16 | 303 | 30 / 3 | 1 | 40 | trigger_event(304); stop |
| 16 | 304 | 30 / 4 | 1 | 60 | set_switch(10); construct_objects(room=30,group_or_wave=1); stop |
| 16 | 221 | 22 / 1 | 1 | 15 | trigger_event(222); stop |
| 16 | 222 | 22 / 2 | 1 | 20 | trigger_event(223); stop |
| 16 | 223 | 22 / 3 | 2 | 60 | trigger_event(225); stop |
| 16 | 225 | 22 / 5 | 2 | 60 | set_switch(9); stop |
| 16 | 51 | 5 / 1 | 0 | 10 | trigger_event(52); stop |
| 16 | 52 | 5 / 2 | 0 | 20 | trigger_event(53); construct_objects(room=5,group_or_wave=1); stop |
| 16 | 53 | 5 / 3 | 2 | 10 | trigger_event(54); stop |
| 16 | 54 | 5 / 4 | 2 | 40 | trigger_event(55); stop |
| 16 | 55 | 5 / 5 | 3 | 30 | trigger_event(56); stop |
| 16 | 56 | 5 / 6 | 3 | 70 | set_switch(8); stop |
| 16 | 211 | 21 / 1 | 2 | 5 | trigger_event(212); stop |
| 16 | 212 | 21 / 2 | 2 | 30 | trigger_event(213); stop |
| 16 | 213 | 21 / 3 | 3 | 30 | trigger_event(214); stop |
| 16 | 214 | 21 / 4 | 2 | 45 | set_switch(100); trigger_event(215); construct_objects(room=21,group_or_wave=1); stop |
| 16 | 215 | 21 / 5 | 2 | 45 | trigger_event(216); stop |
| 16 | 216 | 21 / 6 | 2 | 40 | trigger_event(217); stop |
| 16 | 217 | 21 / 7 | 2 | 20 | set_switch(7); stop |
| 16 | 41 | 4 / 1 | 2 | 30 | trigger_event(42); stop |
| 16 | 42 | 4 / 2 | 1 | 30 | trigger_event(43); stop |
| 16 | 43 | 4 / 3 | 2 | 30 | trigger_event(44); stop |
| 16 | 44 | 4 / 4 | 3 | 30 | trigger_event(45); stop |
| 16 | 45 | 4 / 5 | 2 | 30 | trigger_event(46); stop |
| 16 | 46 | 4 / 6 | 2 | 45 | set_switch(6); construct_objects(room=3,group_or_wave=1); stop |
| 16 | 31 | 3 / 1 | 1 | 60 | trigger_event(32); stop |
| 16 | 32 | 3 / 2 | 2 | 45 | trigger_event(33); stop |
| 16 | 33 | 3 / 3 | 2 | 45 | trigger_event(34); trigger_event(37); stop |
| 16 | 34 | 3 / 4 | 1 | 30 | trigger_event(35); stop |
| 16 | 35 | 3 / 5 | 2 | 90 | set_switch(51); stop |
| 16 | 37 | 3 / 7 | 2 | 105 | trigger_event(38); stop |
| 16 | 38 | 3 / 8 | 1 | 30 | set_switch(52); trigger_event(101); stop |
| 16 | 310 | 3 / 10 | 1 | 5 | construct_objects(room=3,group_or_wave=2); stop |
| 16 | 101 | 10 / 1 | 1 | 30 | trigger_event(102); stop |
| 16 | 102 | 10 / 2 | 2 | 20 | trigger_event(103); stop |
| 16 | 103 | 10 / 3 | 2 | 20 | construct_objects(room=10,group_or_wave=1); trigger_event(105); stop |
| 16 | 105 | 10 / 5 | 3 | 10 | trigger_event(106); stop |
| 16 | 106 | 10 / 6 | 1 | 15 | trigger_event(107); stop |
| 16 | 107 | 10 / 7 | 2 | 30 | set_switch(4); stop |
| 16 | 201 | 20 / 1 | 3 | 10 | trigger_event(202); stop |
| 16 | 202 | 20 / 2 | 2 | 30 | trigger_event(203); stop |
| 16 | 203 | 20 / 3 | 1 | 30 | trigger_event(204); stop |
| 16 | 204 | 20 / 4 | 2 | 30 | trigger_event(205); stop |
| 16 | 205 | 20 / 5 | 2 | 30 | set_switch(31); stop |
| 16 | 2010 | 20 / 10 | 1 | 10 | set_switch(32); stop |
| 16 | 21 | 2 / 1 | 1 | 10 | trigger_event(22); stop |
| 16 | 22 | 2 / 2 | 2 | 25 | trigger_event(23); stop |
| 16 | 23 | 2 / 3 | 2 | 30 | trigger_event(24); stop |
| 16 | 24 | 2 / 4 | 2 | 20 | set_switch(22); stop |
| 16 | 26 | 2 / 6 | 2 | 10 | trigger_event(27); stop |
| 16 | 27 | 2 / 7 | 2 | 15 | trigger_event(28); stop |
| 16 | 28 | 2 / 8 | 2 | 20 | trigger_event(29); stop |
| 16 | 29 | 2 / 9 | 2 | 20 | set_switch(21); construct_objects(room=1,group_or_wave=11); stop |
| 16 | 11 | 1 / 1 | 2 | 10 | trigger_event(12); stop |
| 16 | 12 | 1 / 2 | 2 | 30 | trigger_event(13); stop |
| 16 | 13 | 1 / 3 | 1 | 30 | trigger_event(14); stop |
| 16 | 14 | 1 / 4 | 3 | 30 | trigger_event(15); stop |
| 16 | 15 | 1 / 5 | 2 | 30 | trigger_event(16); stop |
| 16 | 16 | 1 / 6 | 3 | 30 | trigger_event(17); stop |
| 16 | 17 | 1 / 7 | 2 | 30 | trigger_event(18); stop |
| 16 | 18 | 1 / 8 | 3 | 45 | trigger_event(19); stop |
| 16 | 19 | 1 / 9 | 3 | 30 | trigger_event(110); trigger_event(120); stop |
| 16 | 110 | 1 / 10 | 3 | 40 | trigger_event(111); stop |
| 16 | 111 | 1 / 11 | 4 | 40 | set_switch(201); stop |
| 16 | 120 | 1 / 20 | 1 | 15 | set_switch(202); stop |
| 16 | 121 | 1 / 21 | 3 | 90 | trigger_event(122); stop |
| 16 | 122 | 1 / 22 | 3 | 90 | trigger_event(123); stop |
| 16 | 123 | 1 / 23 | 5 | 90 | set_switch(1); construct_objects(room=1,group_or_wave=1); stop |
| 17 | 11 | 1 / 1 | 1 | 60 | trigger_event(12); stop |
| 17 | 12 | 1 / 2 | 1 | 60 | trigger_event(13); stop |
| 17 | 13 | 1 / 3 | 1 | 60 | set_switch(101); stop |
| 17 | 14 | 1 / 4 | 1 | 30 | trigger_event(15); stop |
| 17 | 15 | 1 / 5 | 1 | 30 | set_switch(102); construct_objects(room=1,group_or_wave=4); stop |
| 17 | 16 | 1 / 6 | 2 | 30 | set_switch(103); construct_objects(room=1,group_or_wave=5); stop |
| 17 | 17 | 1 / 7 | 1 | 100 | trigger_event(18); stop |
| 17 | 18 | 1 / 8 | 1 | 30 | set_switch(1); trigger_event(21); stop |
| 17 | 21 | 2 / 1 | 2 | 90 | trigger_event(22); stop |
| 17 | 22 | 2 / 2 | 2 | 90 | trigger_event(23); stop |
| 17 | 23 | 2 / 3 | 2 | 60 | trigger_event(24); stop |
| 17 | 24 | 2 / 4 | 1 | 60 | set_switch(2); stop |
| 17 | 201 | 20 / 1 | 2 | 75 | trigger_event(202); stop |
| 17 | 202 | 20 / 2 | 2 | 30 | trigger_event(203); stop |
| 17 | 203 | 20 / 3 | 1 | 30 | set_switch(105); stop |
| 17 | 205 | 20 / 5 | 1 | 10 | trigger_event(206); stop |
| 17 | 206 | 20 / 6 | 3 | 25 | set_switch(3); stop |
| 17 | 101 | 10 / 1 | 2 | 60 | trigger_event(102); stop |
| 17 | 102 | 10 / 2 | 1 | 60 | construct_objects(room=10,group_or_wave=1); trigger_event(103); stop |
| 17 | 103 | 10 / 3 | 1 | 20 | trigger_event(104); stop |
| 17 | 104 | 10 / 4 | 2 | 60 | trigger_event(105); stop |
| 17 | 105 | 10 / 5 | 2 | 60 | set_switch(4); construct_objects(room=3,group_or_wave=1); stop |
| 17 | 331 | 3 / 31 | 0 | 5 | stop |
| 17 | 31 | 3 / 1 | 2 | 60 | trigger_event(33); stop |
| 17 | 33 | 3 / 3 | 1 | 60 | trigger_event(310); stop |
| 17 | 310 | 3 / 10 | 1 | 60 | trigger_event(311); stop |
| 17 | 311 | 3 / 11 | 2 | 60 | trigger_event(313); stop |
| 17 | 313 | 3 / 13 | 2 | 60 | set_switch(5); stop |
| 17 | 46 | 4 / 6 | 1 | 30 | trigger_event(47); stop |
| 17 | 47 | 4 / 7 | 1 | 30 | trigger_event(41); stop |
| 17 | 41 | 4 / 1 | 2 | 90 | trigger_event(42); stop |
| 17 | 42 | 4 / 2 | 2 | 30 | trigger_event(43); stop |
| 17 | 43 | 4 / 3 | 2 | 30 | trigger_event(44); stop |
| 17 | 44 | 4 / 4 | 2 | 45 | set_switch(6); stop |
| 17 | 2111 | 21 / 11 | 2 | 15 | construct_objects(room=21,group_or_wave=2); stop |
| 17 | 211 | 21 / 1 | 2 | 45 | trigger_event(212); stop |
| 17 | 212 | 21 / 2 | 2 | 45 | trigger_event(213); construct_objects(room=21,group_or_wave=1); stop |
| 17 | 213 | 21 / 3 | 2 | 45 | trigger_event(214); stop |
| 17 | 214 | 21 / 4 | 3 | 45 | trigger_event(215); stop |
| 17 | 215 | 21 / 5 | 1 | 60 | set_switch(7); stop |
| 17 | 2120 | 21 / 20 | 2 | 40 | stop |
| 17 | 51 | 5 / 1 | 1 | 73 | trigger_event(52); stop |
| 17 | 52 | 5 / 2 | 2 | 15 | trigger_event(53); stop |
| 17 | 53 | 5 / 3 | 1 | 15 | set_switch(211); stop |
| 17 | 54 | 5 / 4 | 1 | 15 | trigger_event(55); stop |
| 17 | 55 | 5 / 5 | 3 | 15 | set_switch(212); trigger_event(58); stop |
| 17 | 58 | 5 / 8 | 2 | 15 | set_switch(230); stop |
| 17 | 513 | 5 / 13 | 2 | 15 | set_switch(8); stop |
| 17 | 514 | 5 / 14 | 0 | 15 | trigger_event(515); trigger_event(520); stop |
| 17 | 515 | 5 / 15 | 0 | 15 | set_switch(30); stop |
| 17 | 520 | 5 / 20 | 0 | 210 | trigger_event(521); stop |
| 17 | 521 | 5 / 21 | 0 | 90 | set_switch(31); stop |
| 17 | 2200 | 22 / 0 | 0 | 1 | trigger_event(221); construct_objects(room=22,group_or_wave=1); stop |
| 17 | 221 | 22 / 1 | 2 | 1 | trigger_event(222); construct_objects(room=22,group_or_wave=2); stop |
| 17 | 222 | 22 / 2 | 2 | 30 | set_switch(237); trigger_event(223); stop |
| 17 | 223 | 22 / 3 | 4 | 60 | trigger_event(224); stop |
| 17 | 224 | 22 / 4 | 2 | 90 | trigger_event(225); stop |
| 17 | 225 | 22 / 5 | 2 | 60 | set_switch(9); stop |
| 17 | 301 | 30 / 1 | 2 | 30 | trigger_event(302); stop |
| 17 | 302 | 30 / 2 | 1 | 45 | trigger_event(303); stop |
| 17 | 303 | 30 / 3 | 1 | 45 | trigger_event(304); trigger_event(3012); stop |
| 17 | 304 | 30 / 4 | 2 | 60 | trigger_event(305); stop |
| 17 | 305 | 30 / 5 | 1 | 60 | trigger_event(306); stop |
| 17 | 306 | 30 / 6 | 1 | 75 | trigger_event(307); stop |
| 17 | 307 | 30 / 7 | 1 | 60 | trigger_event(308); stop |
| 17 | 308 | 30 / 8 | 2 | 50 | trigger_event(309); stop |
| 17 | 309 | 30 / 9 | 2 | 60 | trigger_event(3010); stop |
| 17 | 3010 | 30 / 10 | 2 | 60 | set_switch(235); stop |
| 17 | 3012 | 30 / 12 | 2 | 60 | trigger_event(3013); stop |
| 17 | 3013 | 30 / 13 | 1 | 60 | trigger_event(3014); stop |
| 17 | 3014 | 30 / 14 | 1 | 60 | trigger_event(3015); stop |
| 17 | 3015 | 30 / 15 | 1 | 60 | trigger_event(3016); stop |
| 17 | 3016 | 30 / 16 | 1 | 60 | trigger_event(3017); stop |
| 17 | 3017 | 30 / 17 | 2 | 60 | trigger_event(3018); stop |
| 17 | 3018 | 30 / 18 | 1 | 60 | set_switch(236); stop |
| 17 | 3020 | 30 / 20 | 3 | 60 | trigger_event(3021); stop |
| 17 | 3021 | 30 / 21 | 4 | 60 | set_switch(10); stop |
| 17 | 3000 | 30 / 0 | 0 | 1 | construct_objects(room=30,group_or_wave=5); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
