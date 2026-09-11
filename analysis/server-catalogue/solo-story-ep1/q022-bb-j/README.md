# 鋼の魂 — solo-story-ep1/q022-bb-j

Episode1; header quest ID 22; language J. Static scan: **525 objects, 154 enemy/NPC records, 41 events, 434 script labels.** Script roundtrip: byte-identical.

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
0x07, 0x07, 0x00, 0x02, 0x00
0x0A, 0x0A, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 14 | 0 |
| 1 | 96 | 0 | 0 |
| 7 | 227 | 26 | 21 |
| 10 | 176 | 114 | 20 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 10 | 201 | 20 / 1 | 6 | 1 | trigger_event(2011); stop |
| 10 | 2011 | 20 / 2 | 6 | 30 | trigger_event(2012); stop |
| 10 | 2012 | 20 / 3 | 6 | 300 | set_switch(5); set_switch(6); stop |
| 10 | 211 | 21 / 1 | 5 | 100 | trigger_event(2111); stop |
| 10 | 2111 | 21 / 2 | 5 | 1 | set_switch(41); stop |
| 10 | 301 | 30 / 1 | 8 | 100 | trigger_event(3011); stop |
| 10 | 3011 | 30 / 2 | 4 | 90 | set_switch(9); set_switch(10); set_switch(11); set_switch(12); set_switch(13); set_switch(14); set_switch(15); set_switch(16); set_switch(19); set_switch(20); set_switch(21); set_switch(22); set_switch(23); set_switch(24); set_switch(25); set_switch(26); set_switch(29); set_switch(30); set_switch(31); set_switch(32); set_switch(33); set_switch(34); set_switch(35); set_switch(36); set_switch(37); set_switch(38); set_switch(39); set_switch(40); stop |
| 10 | 302 | 30 / 3 | 5 | 60 | stop |
| 10 | 311 | 31 / 1 | 5 | 10 | trigger_event(3111); stop |
| 10 | 3111 | 31 / 2 | 8 | 10 | set_switch(17); set_switch(18); stop |
| 10 | 401 | 40 / 1 | 4 | 10 | trigger_event(4011); stop |
| 10 | 4011 | 40 / 2 | 5 | 10 | trigger_event(4012); stop |
| 10 | 4012 | 40 / 3 | 6 | 10 | set_switch(3); set_switch(4); stop |
| 10 | 411 | 41 / 1 | 5 | 10 | trigger_event(4111); stop |
| 10 | 4111 | 41 / 2 | 7 | 60 | trigger_event(4112); stop |
| 10 | 4112 | 41 / 3 | 5 | 200 | set_switch(7); set_switch(8); stop |
| 10 | 421 | 42 / 1 | 3 | 100 | trigger_event(4211); stop |
| 10 | 4211 | 42 / 2 | 9 | 1 | set_switch(27); set_switch(28); stop |
| 10 | 751 | 75 / 1 | 4 | 1 | trigger_event(7511); stop |
| 10 | 7511 | 75 / 2 | 8 | 1 | stop |
| 7 | 411 | 41 / 1 | 1 | 100 | trigger_event(4111); stop |
| 7 | 4111 | 41 / 2 | 3 | 10 | trigger_event(411103); trigger_event(411106); trigger_event(411109); trigger_event(411112); trigger_event(411115); trigger_event(411118); stop |
| 7 | 411103 | 41 / 3 | 1 | 1 | trigger_event(411104); stop |
| 7 | 411104 | 41 / 4 | 1 | 1 | trigger_event(411105); stop |
| 7 | 411105 | 41 / 5 | 1 | 1 | stop |
| 7 | 411106 | 41 / 6 | 1 | 1 | trigger_event(411107); stop |
| 7 | 411107 | 41 / 7 | 1 | 1 | trigger_event(411108); stop |
| 7 | 411108 | 41 / 8 | 1 | 1 | stop |
| 7 | 411109 | 41 / 9 | 1 | 1 | trigger_event(411110); stop |
| 7 | 411110 | 41 / 10 | 1 | 1 | trigger_event(411111); stop |
| 7 | 411111 | 41 / 11 | 1 | 1 | stop |
| 7 | 411112 | 41 / 12 | 1 | 1 | trigger_event(411113); stop |
| 7 | 411113 | 41 / 13 | 1 | 1 | trigger_event(411114); stop |
| 7 | 411114 | 41 / 14 | 1 | 1 | stop |
| 7 | 411115 | 41 / 15 | 1 | 1 | trigger_event(411116); stop |
| 7 | 411116 | 41 / 16 | 1 | 1 | trigger_event(411117); stop |
| 7 | 411117 | 41 / 17 | 1 | 1 | stop |
| 7 | 411118 | 41 / 18 | 1 | 1 | trigger_event(411119); stop |
| 7 | 411119 | 41 / 19 | 1 | 1 | trigger_event(411120); stop |
| 7 | 411120 | 41 / 20 | 1 | 1 | set_switch(1); set_switch(2); set_switch(3); set_switch(4); set_switch(8); set_switch(9); set_switch(10); set_switch(11); set_switch(12); set_switch(13); set_switch(14); set_switch(15); set_switch(16); set_switch(17); set_switch(18); set_switch(19); set_switch(20); set_switch(21); set_switch(22); set_switch(23); set_switch(24); set_switch(25); set_switch(26); set_switch(27); set_switch(28); set_switch(29); set_switch(31); set_switch(32); set_switch(33); set_switch(45); set_switch(48); set_switch(49); set_switch(50); set_switch(51); stop |
| 7 | 701 | 70 / 1 | 4 | 1 | set_switch(5); set_switch(6); set_switch(7); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
