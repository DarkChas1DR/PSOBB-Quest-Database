# ハンターの右腕 — solo-story-ep1/q024-bb-j

Episode1; header quest ID 24; language J. Static scan: **461 objects, 236 enemy/NPC records, 44 events, 198 script labels.** Script roundtrip: byte-identical.

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
0x08, 0x08, 0x00, 0x00, 0x00
0x09, 0x09, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 18 | 0 |
| 8 | 222 | 101 | 18 |
| 9 | 213 | 117 | 26 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 8 | 602 | 60 / 2 | 8 | 10 | set_switch(55); set_switch(56); set_switch(52); set_switch(51); stop |
| 8 | 601 | 60 / 1 | 6 | 10 | stop |
| 8 | 201 | 20 / 1 | 6 | 10 | set_switch(50); set_switch(49); set_switch(45); set_switch(46); set_switch(47); set_switch(48); stop |
| 8 | 701 | 70 / 1 | 7 | 10 | trigger_event(7011); stop |
| 8 | 7011 | 70 / 2 | 6 | 10 | trigger_event(7012); stop |
| 8 | 7012 | 70 / 3 | 7 | 10 | set_switch(43); set_switch(44); stop |
| 8 | 311 | 31 / 1 | 2 | 10 | set_switch(34); set_switch(33); set_switch(36); set_switch(35); set_switch(39); set_switch(40); set_switch(37); set_switch(38); set_switch(31); set_switch(32); stop |
| 8 | 401 | 40 / 1 | 9 | 10 | stop |
| 8 | 211 | 21 / 1 | 5 | 10 | set_switch(41); set_switch(42); stop |
| 8 | 221 | 22 / 1 | 4 | 10 | set_switch(28); set_switch(27); set_switch(23); set_switch(24); stop |
| 8 | 502 | 50 / 1 | 8 | 10 | set_switch(29); set_switch(30); set_switch(31); set_switch(32); stop |
| 8 | 321 | 32 / 1 | 5 | 10 | set_switch(25); set_switch(26); set_switch(21); set_switch(22); set_switch(20); set_switch(19); set_switch(17); set_switch(18); set_switch(16); set_switch(15); set_switch(13); set_switch(14); set_switch(11); set_switch(12); set_switch(10); set_switch(9); set_switch(1); set_switch(2); set_switch(3); set_switch(4); stop |
| 8 | 241 | 24 / 1 | 6 | 10 | stop |
| 8 | 231 | 23 / 1 | 2 | 10 | trigger_event(2311); stop |
| 8 | 2311 | 23 / 2 | 6 | 10 | set_switch(5); set_switch(6); set_switch(3); set_switch(4); stop |
| 8 | 331 | 33 / 1 | 5 | 10 | trigger_event(3311); stop |
| 8 | 3311 | 33 / 2 | 6 | 10 | trigger_event(3312); stop |
| 8 | 3312 | 33 / 3 | 3 | 10 | set_switch(7); set_switch(8); stop |
| 9 | 201 | 20 / 1 | 2 | 30 | set_switch(37); set_switch(38); stop |
| 9 | 211 | 21 / 1 | 6 | 10 | set_switch(7); set_switch(8); set_switch(35); set_switch(36); stop |
| 9 | 212 | 21 / 2 | 3 | 60 | stop |
| 9 | 231 | 23 / 1 | 6 | 1 | trigger_event(2311); stop |
| 9 | 2311 | 23 / 2 | 5 | 1 | trigger_event(2312); stop |
| 9 | 2312 | 23 / 3 | 4 | 1 | set_switch(17); set_switch(18); set_switch(19); set_switch(20); set_switch(21); set_switch(22); stop |
| 9 | 241 | 24 / 1 | 5 | 1 | trigger_event(2411); stop |
| 9 | 2411 | 24 / 2 | 4 | 1 | set_switch(23); set_switch(24); set_switch(25); set_switch(26); set_switch(39); set_switch(40); stop |
| 9 | 301 | 30 / 1 | 6 | 30 | set_switch(31); set_switch(32); stop |
| 9 | 311 | 31 / 1 | 2 | 30 | trigger_event(3111); stop |
| 9 | 3111 | 31 / 2 | 5 | 60 | set_switch(11); set_switch(12); set_switch(13); set_switch(14); set_switch(15); set_switch(16); set_switch(33); set_switch(34); stop |
| 9 | 312 | 31 / 3 | 5 | 120 | stop |
| 9 | 331 | 33 / 1 | 5 | 30 | trigger_event(3311); stop |
| 9 | 3311 | 33 / 2 | 3 | 60 | set_switch(43); set_switch(44); stop |
| 9 | 401 | 40 / 1 | 4 | 1 | trigger_event(4011); stop |
| 9 | 4011 | 40 / 2 | 4 | 30 | set_switch(5); set_switch(6); set_switch(9); set_switch(10); stop |
| 9 | 411 | 41 / 1 | 2 | 30 | trigger_event(4111); stop |
| 9 | 4111 | 41 / 2 | 1 | 60 | set_switch(3); set_switch(4); set_switch(27); set_switch(28); set_switch(29); set_switch(30); stop |
| 9 | 421 | 42 / 1 | 4 | 1 | stop |
| 9 | 441 | 44 / 1 | 6 | 1 | trigger_event(4411); stop |
| 9 | 4411 | 44 / 2 | 5 | 30 | set_switch(59); set_switch(60); set_switch(61); set_switch(62); set_switch(63); set_switch(64); stop |
| 9 | 601 | 60 / 1 | 5 | 1 | set_switch(53); set_switch(54); set_switch(55); set_switch(56); set_switch(57); set_switch(58); stop |
| 9 | 801 | 80 / 1 | 7 | 30 | trigger_event(8011); stop |
| 9 | 8011 | 80 / 2 | 6 | 60 | trigger_event(8012); stop |
| 9 | 8012 | 80 / 3 | 9 | 1 | trigger_event(8013); stop |
| 9 | 8013 | 80 / 4 | 3 | 15 | set_switch(41); set_switch(42); set_switch(43); set_switch(44); set_switch(45); set_switch(46); set_switch(47); set_switch(48); set_switch(49); set_switch(50); set_switch(51); set_switch(52); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
