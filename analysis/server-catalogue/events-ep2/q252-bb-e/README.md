# Revisiting Darkness — events-ep2/q252-bb-e

Episode2; header quest ID 252; language E. Static scan: **507 objects, 354 enemy/NPC records, 93 events, 129 script labels.** Script roundtrip: byte-identical.

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
0x00, 0x12, 0x00, 0x00, 0x00
0x01, 0x13, 0x00, 0x00, 0x00
0x02, 0x14, 0x00, 0x01, 0x00
0x04, 0x16, 0x00, 0x01, 0x00
0x0E, 0x20, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 50 | 17 | 0 |
| 1 | 17 | 11 | 4 |
| 2 | 173 | 107 | 35 |
| 4 | 236 | 218 | 53 |
| 14 | 31 | 1 | 1 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 1 | 80 / 0 | 0 | 0 | set_switch(101); trigger_event(2); stop |
| 1 | 2 | 150 / 1 | 3 | 130 | trigger_event(3); stop |
| 1 | 3 | 150 / 2 | 3 | 60 | trigger_event(4); stop |
| 1 | 4 | 150 / 3 | 5 | 60 | set_switch(20); stop |
| 2 | 1 | 90 / 1 | 3 | 30 | trigger_event(2); stop |
| 2 | 2 | 90 / 2 | 5 | 60 | set_switch(10); set_switch(12); set_switch(50); stop |
| 2 | 3 | 541 / 1 | 2 | 20 | stop |
| 2 | 999 | 0 / 0 | 0 | 0 | clear_switch(12); trigger_event(7); stop |
| 2 | 7 | 60 / 1 | 3 | 30 | trigger_event(8); stop |
| 2 | 8 | 60 / 2 | 2 | 30 | trigger_event(9); trigger_event(10); stop |
| 2 | 9 | 60 / 3 | 3 | 30 | stop |
| 2 | 10 | 111 / 1 | 3 | 650 | set_switch(12); trigger_event(11); stop |
| 2 | 11 | 60 / 4 | 3 | 30 | set_switch(13); stop |
| 2 | 1000 | 0 / 0 | 0 | 0 | set_switch(14); stop |
| 2 | 12 | 40 / 1 | 5 | 30 | trigger_event(13); trigger_event(14); set_switch(18); clear_switch(13); construct_objects(room=162,group_or_wave=1); construct_objects(room=60,group_or_wave=1); stop |
| 2 | 13 | 40 / 2 | 4 | 30 | stop |
| 2 | 14 | 40 / 3 | 6 | 600 | trigger_event(15); stop |
| 2 | 15 | 40 / 4 | 4 | 30 | set_switch(15); set_switch(13); clear_switch(18); stop |
| 2 | 16 | 61 / 1 | 3 | 30 | trigger_event(17); stop |
| 2 | 17 | 61 / 2 | 4 | 30 | trigger_event(18); trigger_event(19); stop |
| 2 | 18 | 61 / 3 | 3 | 350 | stop |
| 2 | 19 | 61 / 4 | 3 | 40 | set_switch(19); stop |
| 2 | 20 | 0 / 0 | 0 | 1 | trigger_event(21); construct_objects(room=61,group_or_wave=1); stop |
| 2 | 21 | 61 / 5 | 5 | 30 | set_switch(21); stop |
| 2 | 22 | 100 / 1 | 2 | 30 | set_switch(22); set_switch(23); set_switch(24); set_switch(25); set_switch(26); set_switch(27); stop |
| 2 | 23 | 0 / 0 | 0 | 0 | clear_switch(23); construct_objects(room=141,group_or_wave=1); trigger_event(24); clear_switch(24); clear_switch(25); clear_switch(26); clear_switch(27); stop |
| 2 | 24 | 41 / 1 | 3 | 30 | set_switch(24); trigger_event(25); stop |
| 2 | 25 | 41 / 2 | 3 | 30 | trigger_event(26); stop |
| 2 | 26 | 41 / 3 | 3 | 30 | set_switch(25); trigger_event(27); stop |
| 2 | 27 | 41 / 4 | 4 | 40 | trigger_event(28); trigger_event(29); stop |
| 2 | 28 | 41 / 5 | 7 | 30 | stop |
| 2 | 29 | 41 / 6 | 3 | 400 | set_switch(26); trigger_event(30); set_switch(28); construct_objects(room=41,group_or_wave=1); stop |
| 2 | 30 | 41 / 7 | 6 | 30 | trigger_event(31); stop |
| 2 | 31 | 41 / 8 | 3 | 30 | set_switch(27); clear_switch(28); set_switch(29); set_switch(30); set_switch(23); set_switch(31); set_switch(32); stop |
| 2 | 32 | 50 / 1 | 3 | 20 | trigger_event(33); stop |
| 2 | 33 | 50 / 2 | 3 | 30 | trigger_event(34); set_switch(33); stop |
| 2 | 34 | 50 / 3 | 3 | 25 | set_switch(34); stop |
| 2 | 1001 | 0 / 0 | 0 | 0 | clear_switch(50); construct_objects(room=116,group_or_wave=1); trigger_event(1002); stop |
| 2 | 1002 | 20 / 1 | 3 | 50 | construct_objects(room=20,group_or_wave=1); set_switch(50); construct_objects(room=20,group_or_wave=1); stop |
| 4 | 1 | 51 / 1 | 6 | 50 | trigger_event(2); trigger_event(3); stop |
| 4 | 2 | 51 / 2 | 3 | 40 | stop |
| 4 | 3 | 51 / 3 | 3 | 150 | set_switch(10); set_switch(34); stop |
| 4 | 4 | 11 / 1 | 3 | 25 | trigger_event(5); stop |
| 4 | 5 | 11 / 2 | 3 | 35 | set_switch(12); stop |
| 4 | 6 | 11 / 3 | 3 | 30 | stop |
| 4 | 7 | 33 / 1 | 1 | 35 | set_switch(14); trigger_event(8); stop |
| 4 | 8 | 33 / 2 | 4 | 40 | trigger_event(9); stop |
| 4 | 9 | 33 / 3 | 3 | 30 | set_switch(15); trigger_event(10); stop |
| 4 | 10 | 33 / 4 | 3 | 40 | set_switch(16); trigger_event(12); stop |
| 4 | 11 | 33 / 5 | 3 | 30 | stop |
| 4 | 12 | 161 / 1 | 4 | 40 | stop |
| 4 | 102 | 41 / 1 | 6 | 20 | trigger_event(103); stop |
| 4 | 103 | 41 / 2 | 3 | 30 | set_switch(18); stop |
| 4 | 104 | 10 / 1 | 5 | 40 | trigger_event(105); stop |
| 4 | 105 | 10 / 2 | 3 | 40 | set_switch(19); stop |
| 4 | 106 | 10 / 3 | 7 | 50 | trigger_event(107); stop |
| 4 | 107 | 10 / 4 | 4 | 30 | set_switch(32); stop |
| 4 | 108 | 32 / 1 | 4 | 30 | set_switch(21); stop |
| 4 | 109 | 32 / 2 | 3 | 30 | construct_objects(room=32,group_or_wave=1); stop |
| 4 | 110 | 32 / 3 | 3 | 30 | set_switch(23); stop |
| 4 | 111 | 192 / 1 | 3 | 30 | set_switch(25); construct_objects(room=192,group_or_wave=1); stop |
| 4 | 112 | 21 / 1 | 3 | 30 | set_switch(26); stop |
| 4 | 113 | 21 / 2 | 6 | 30 | set_switch(28); construct_objects(room=21,group_or_wave=1); stop |
| 4 | 114 | 52 / 1 | 5 | 50 | trigger_event(115); stop |
| 4 | 115 | 52 / 2 | 8 | 30 | trigger_event(116); stop |
| 4 | 116 | 52 / 3 | 6 | 40 | set_switch(29); set_switch(30); stop |
| 4 | 117 | 31 / 0 | 0 | 0 | clear_switch(30); trigger_event(118); set_switch(31); stop |
| 4 | 118 | 31 / 1 | 3 | 100 | set_switch(30); clear_switch(31); stop |
| 4 | 202 | 41 / 5 | 6 | 25 | trigger_event(203); stop |
| 4 | 203 | 41 / 6 | 5 | 35 | construct_objects(room=41,group_or_wave=1); stop |
| 4 | 204 | 20 / 1 | 7 | 120 | trigger_event(205); trigger_event(206); set_switch(32); clear_switch(34); construct_objects(room=142,group_or_wave=1); stop |
| 4 | 205 | 20 / 2 | 6 | 45 | stop |
| 4 | 206 | 20 / 3 | 5 | 350 | trigger_event(207); stop |
| 4 | 207 | 20 / 4 | 1 | 30 | set_switch(33); clear_switch(32); set_switch(34); stop |
| 4 | 208 | 102 / 1 | 2 | 25 | stop |
| 4 | 209 | 40 / 1 | 5 | 80 | trigger_event(210); stop |
| 4 | 210 | 40 / 2 | 5 | 50 | set_switch(37); stop |
| 4 | 211 | 40 / 3 | 5 | 50 | set_switch(38); set_switch(40); stop |
| 4 | 212 | 50 / 1 | 8 | 50 | trigger_event(213); stop |
| 4 | 213 | 50 / 2 | 6 | 50 | set_switch(39); stop |
| 4 | 214 | 50 / 0 | 0 | 1 | clear_switch(40); construct_objects(room=50,group_or_wave=3); trigger_event(215); stop |
| 4 | 215 | 50 / 3 | 6 | 30 | set_switch(40); stop |
| 4 | 216 | 42 / 1 | 3 | 40 | stop |
| 4 | 217 | 42 / 2 | 3 | 30 | trigger_event(218); stop |
| 4 | 218 | 42 / 3 | 7 | 30 | set_switch(42); stop |
| 4 | 219 | 182 / 1 | 3 | 30 | set_switch(43); stop |
| 4 | 301 | 30 / 1 | 9 | 30 | construct_objects(room=182,group_or_wave=1); clear_switch(43); set_switch(45); trigger_event(302); trigger_event(303); stop |
| 4 | 302 | 30 / 2 | 3 | 30 | stop |
| 4 | 303 | 30 / 3 | 7 | 150 | trigger_event(304); construct_objects(room=30,group_or_wave=1); stop |
| 4 | 304 | 30 / 4 | 5 | 30 | clear_switch(45); set_switch(46); stop |
| 4 | 403 | 191 / 0 | 0 | 0 | construct_objects(room=191,group_or_wave=1); stop |
| 4 | 404 | 191 / 0 | 0 | 0 | construct_objects(room=191,group_or_wave=2); stop |
| 14 | 1 | 1 / 1 | 1 | 50 | construct_objects(room=1,group_or_wave=1); set_switch(50); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

A backup is present; decompressed content identical: False. See [text differences](<backup-diff.txt>).

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
