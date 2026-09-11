# １－３：地下の巣窟 — government-ep1/q403-bb-j

Episode1; header quest ID 403; language J. Static scan: **292 objects, 176 enemy/NPC records, 51 events, 106 script labels.** Script roundtrip: byte-identical.

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
0x00, 0x00, 0x00, 0x00, 0x00
0x01, 0x01, 0x00, 0x00, 0x03
0x02, 0x02, 0x00, 0x00, 0x03
0x0B, 0x0B, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 27 | 20 | 0 |
| 1 | 111 | 69 | 20 |
| 2 | 134 | 86 | 30 |
| 11 | 20 | 1 | 1 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 111 | 11 / 1 | 3 | 30 | trigger_event(1111); stop |
| 1 | 1111 | 11 / 2 | 4 | 30 | set_switch(4); stop |
| 1 | 71 | 7 / 1 | 4 | 30 | trigger_event(711); stop |
| 1 | 711 | 7 / 2 | 4 | 30 | trigger_event(712); stop |
| 1 | 712 | 7 / 3 | 4 | 30 | set_switch(2); set_switch(3); stop |
| 1 | 41 | 4 / 1 | 4 | 30 | trigger_event(411); stop |
| 1 | 411 | 4 / 2 | 4 | 30 | trigger_event(412); stop |
| 1 | 412 | 4 / 3 | 4 | 30 | trigger_event(413); stop |
| 1 | 413 | 4 / 4 | 5 | 30 | set_switch(9); stop |
| 1 | 81 | 8 / 1 | 1 | 30 | trigger_event(82); stop |
| 1 | 82 | 8 / 2 | 4 | 30 | stop |
| 1 | 21 | 2 / 1 | 3 | 30 | trigger_event(211); stop |
| 1 | 211 | 2 / 2 | 2 | 30 | trigger_event(212); stop |
| 1 | 212 | 2 / 3 | 3 | 30 | set_switch(1); stop |
| 1 | 22 | 2 / 4 | 2 | 30 | stop |
| 1 | 51 | 5 / 1 | 4 | 30 | trigger_event(511); stop |
| 1 | 511 | 5 / 2 | 5 | 30 | trigger_event(512); stop |
| 1 | 512 | 5 / 3 | 4 | 30 | trigger_event(513); stop |
| 1 | 513 | 5 / 4 | 4 | 30 | set_switch(7); set_switch(8); set_switch(6); set_switch(5); stop |
| 1 | 52 | 5 / 5 | 1 | 30 | stop |
| 2 | 11 | 1 / 1 | 3 | 50 | stop |
| 2 | 12 | 1 / 2 | 5 | 1 | set_switch(2); stop |
| 2 | 21 | 2 / 1 | 2 | 80 | trigger_event(211); stop |
| 2 | 211 | 2 / 2 | 3 | 30 | stop |
| 2 | 22 | 2 / 3 | 2 | 50 | trigger_event(221); stop |
| 2 | 221 | 2 / 4 | 1 | 15 | trigger_event(222); stop |
| 2 | 222 | 2 / 5 | 3 | 1 | set_switch(1); stop |
| 2 | 31 | 3 / 1 | 5 | 50 | stop |
| 2 | 41 | 4 / 1 | 3 | 50 | trigger_event(411); stop |
| 2 | 411 | 4 / 2 | 4 | 20 | set_switch(31); stop |
| 2 | 61 | 6 / 1 | 4 | 40 | trigger_event(611); stop |
| 2 | 611 | 6 / 2 | 3 | 30 | set_switch(3); set_switch(9); stop |
| 2 | 111 | 11 / 1 | 2 | 30 | trigger_event(1111); stop |
| 2 | 1111 | 11 / 2 | 2 | 20 | set_switch(4); set_switch(5); set_switch(6); set_switch(7); stop |
| 2 | 112 | 11 / 3 | 3 | 60 | trigger_event(1121); stop |
| 2 | 1121 | 11 / 4 | 2 | 10 | stop |
| 2 | 113 | 11 / 5 | 3 | 1 | set_switch(4); set_switch(5); set_switch(6); stop |
| 2 | 121 | 12 / 1 | 2 | 1 | trigger_event(1211); stop |
| 2 | 1211 | 12 / 2 | 5 | 1 | trigger_event(1212); stop |
| 2 | 1212 | 12 / 3 | 4 | 30 | set_switch(10); stop |
| 2 | 131 | 13 / 1 | 1 | 1 | trigger_event(1311); stop |
| 2 | 1311 | 13 / 2 | 3 | 15 | trigger_event(1312); stop |
| 2 | 1312 | 13 / 3 | 2 | 15 | trigger_event(1313); stop |
| 2 | 1313 | 13 / 4 | 2 | 30 | stop |
| 2 | 132 | 13 / 5 | 1 | 1 | trigger_event(1321); stop |
| 2 | 1321 | 13 / 6 | 3 | 15 | trigger_event(1322); stop |
| 2 | 1322 | 13 / 7 | 3 | 45 | trigger_event(1323); stop |
| 2 | 1323 | 13 / 8 | 2 | 45 | set_switch(30); stop |
| 2 | 151 | 15 / 1 | 4 | 45 | trigger_event(1511); stop |
| 2 | 1511 | 15 / 2 | 4 | 30 | stop |
| 11 | 1 | 1 / 1 | 1 | 50 | construct_objects(room=1,group_or_wave=1); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
