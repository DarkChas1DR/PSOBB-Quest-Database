# Christmas Fiasco — seasonal-ep2/q65535-bb-e

Episode2; header quest ID 65535; language E. Static scan: **157 objects, 545 enemy/NPC records, 85 events, 76 script labels.** Script roundtrip: byte-identical.

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
| 0 | 44 | 14 | 0 |
| 4 | 36 | 166 | 28 |
| 5 | 53 | 183 | 31 |
| 11 | 24 | 182 | 26 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 4 | 101 | 40 / 1 | 3 | 0 | trigger_event(102); stop |
| 4 | 102 | 40 / 2 | 3 | 0 | trigger_event(103); stop |
| 4 | 103 | 40 / 3 | 3 | 0 | trigger_event(104); stop |
| 4 | 104 | 40 / 4 | 4 | 0 | trigger_event(105); stop |
| 4 | 105 | 40 / 5 | 6 | 0 | trigger_event(106); stop |
| 4 | 106 | 40 / 6 | 7 | 0 | trigger_event(107); stop |
| 4 | 107 | 40 / 7 | 8 | 0 | trigger_event(108); stop |
| 4 | 108 | 40 / 8 | 5 | 0 | trigger_event(109); stop |
| 4 | 109 | 40 / 9 | 5 | 0 | trigger_event(110); stop |
| 4 | 110 | 40 / 10 | 5 | 0 | trigger_event(111); stop |
| 4 | 111 | 40 / 11 | 10 | 0 | trigger_event(112); stop |
| 4 | 112 | 40 / 12 | 8 | 0 | construct_objects(room=40,group_or_wave=1); set_switch(1); stop |
| 4 | 201 | 51 / 1 | 3 | 0 | trigger_event(202); stop |
| 4 | 202 | 51 / 2 | 5 | 0 | trigger_event(203); stop |
| 4 | 203 | 51 / 3 | 12 | 0 | trigger_event(204); stop |
| 4 | 204 | 51 / 4 | 10 | 0 | trigger_event(205); set_switch(2); stop |
| 4 | 205 | 51 / 5 | 5 | 0 | trigger_event(206); stop |
| 4 | 206 | 51 / 6 | 6 | 0 | trigger_event(207); trigger_event(208); stop |
| 4 | 207 | 51 / 7 | 7 | 0 | trigger_event(209); stop |
| 4 | 208 | 51 / 8 | 3 | 0 | set_switch(3); stop |
| 4 | 209 | 51 / 9 | 4 | 0 | trigger_event(210); stop |
| 4 | 210 | 51 / 10 | 6 | 0 | construct_objects(room=51,group_or_wave=1); trigger_event(211); stop |
| 4 | 211 | 51 / 11 | 8 | 0 | trigger_event(212); stop |
| 4 | 212 | 51 / 12 | 4 | 0 | trigger_event(213); set_switch(4); stop |
| 4 | 213 | 51 / 13 | 8 | 0 | trigger_event(214); stop |
| 4 | 214 | 51 / 14 | 5 | 0 | trigger_event(215); stop |
| 4 | 215 | 51 / 15 | 6 | 0 | trigger_event(216); stop |
| 4 | 216 | 51 / 16 | 7 | 0 | set_switch(5); stop |
| 5 | 101 | 13 / 1 | 3 | 0 | trigger_event(102); stop |
| 5 | 102 | 13 / 2 | 4 | 0 | trigger_event(103); stop |
| 5 | 103 | 13 / 3 | 3 | 0 | trigger_event(104); stop |
| 5 | 104 | 13 / 4 | 2 | 0 | trigger_event(105); stop |
| 5 | 105 | 13 / 5 | 3 | 0 | trigger_event(106); stop |
| 5 | 106 | 13 / 6 | 2 | 0 | trigger_event(107); stop |
| 5 | 107 | 13 / 7 | 2 | 0 | trigger_event(108); stop |
| 5 | 108 | 13 / 8 | 4 | 0 | trigger_event(109); stop |
| 5 | 109 | 13 / 9 | 3 | 0 | trigger_event(110); stop |
| 5 | 110 | 13 / 10 | 3 | 0 | trigger_event(111); stop |
| 5 | 111 | 13 / 11 | 3 | 0 | trigger_event(112); stop |
| 5 | 112 | 13 / 12 | 7 | 0 | trigger_event(113); stop |
| 5 | 113 | 13 / 13 | 4 | 0 | trigger_event(114); stop |
| 5 | 114 | 13 / 14 | 3 | 0 | trigger_event(115); stop |
| 5 | 115 | 13 / 15 | 5 | 0 | set_switch(101); construct_objects(room=13,group_or_wave=1); stop |
| 5 | 201 | 12 / 1 | 3 | 0 | trigger_event(202); stop |
| 5 | 202 | 12 / 2 | 7 | 0 | trigger_event(203); stop |
| 5 | 203 | 12 / 3 | 17 | 0 | trigger_event(204); stop |
| 5 | 204 | 12 / 4 | 9 | 0 | trigger_event(205); stop |
| 5 | 205 | 12 / 5 | 5 | 0 | trigger_event(206); stop |
| 5 | 206 | 12 / 6 | 5 | 0 | trigger_event(207); stop |
| 5 | 207 | 12 / 7 | 10 | 0 | trigger_event(208); stop |
| 5 | 208 | 12 / 8 | 5 | 0 | set_switch(2); construct_objects(room=12,group_or_wave=1); stop |
| 5 | 301 | 11 / 1 | 10 | 0 | trigger_event(302); stop |
| 5 | 302 | 11 / 2 | 7 | 0 | trigger_event(303); stop |
| 5 | 303 | 11 / 3 | 11 | 0 | trigger_event(304); stop |
| 5 | 304 | 11 / 4 | 8 | 0 | trigger_event(305); stop |
| 5 | 305 | 11 / 5 | 16 | 0 | trigger_event(306); stop |
| 5 | 306 | 11 / 6 | 6 | 0 | trigger_event(307); stop |
| 5 | 307 | 11 / 7 | 8 | 0 | trigger_event(308); stop |
| 5 | 308 | 11 / 8 | 5 | 0 | set_switch(3); stop |
| 11 | 101 | 70 / 1 | 3 | 0 | trigger_event(102); stop |
| 11 | 102 | 70 / 2 | 3 | 0 | trigger_event(103); stop |
| 11 | 103 | 70 / 3 | 8 | 0 | trigger_event(104); stop |
| 11 | 104 | 70 / 4 | 5 | 0 | trigger_event(105); stop |
| 11 | 105 | 70 / 5 | 5 | 0 | trigger_event(106); stop |
| 11 | 106 | 70 / 6 | 5 | 0 | trigger_event(107); stop |
| 11 | 107 | 70 / 7 | 5 | 0 | trigger_event(108); stop |
| 11 | 108 | 70 / 8 | 8 | 0 | set_switch(1); construct_objects(room=70,group_or_wave=1); stop |
| 11 | 201 | 20 / 1 | 8 | 0 | trigger_event(202); stop |
| 11 | 202 | 20 / 2 | 5 | 0 | trigger_event(203); stop |
| 11 | 203 | 20 / 3 | 6 | 0 | trigger_event(204); stop |
| 11 | 204 | 20 / 4 | 6 | 0 | trigger_event(205); stop |
| 11 | 205 | 20 / 5 | 8 | 0 | trigger_event(206); stop |
| 11 | 206 | 20 / 6 | 5 | 0 | trigger_event(207); stop |
| 11 | 207 | 20 / 7 | 6 | 0 | trigger_event(208); stop |
| 11 | 208 | 20 / 8 | 10 | 0 | set_switch(2); construct_objects(room=20,group_or_wave=1); stop |
| 11 | 301 | 95 / 1 | 15 | 0 | trigger_event(302); stop |
| 11 | 302 | 95 / 2 | 5 | 0 | trigger_event(303); stop |
| 11 | 303 | 95 / 3 | 8 | 0 | trigger_event(304); stop |
| 11 | 304 | 95 / 4 | 8 | 0 | trigger_event(305); stop |
| 11 | 305 | 95 / 5 | 8 | 0 | trigger_event(306); stop |
| 11 | 306 | 95 / 6 | 9 | 0 | trigger_event(307); stop |
| 11 | 307 | 95 / 7 | 6 | 0 | trigger_event(308); stop |
| 11 | 308 | 95 / 8 | 8 | 0 | trigger_event(309); stop |
| 11 | 309 | 95 / 9 | 8 | 0 | trigger_event(310); stop |
| 11 | 310 | 95 / 10 | 11 | 0 | set_switch(3); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

A backup is present; decompressed content identical: False. See [text differences](<backup-diff.txt>).

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
