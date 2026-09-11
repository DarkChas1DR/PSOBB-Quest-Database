# 幻界の果てに ２ — q234-bb-j

Episode2; header quest ID 234; language J. Static scan: **401 objects, 378 enemy/NPC records, 90 events, 126 script labels.** Script roundtrip: alignment-only.

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
0x05, 0x17, 0x00, 0x00, 0x00
0x08, 0x1A, 0x00, 0x00, 0x01
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 44 | 20 | 0 |
| 5 | 139 | 191 | 51 |
| 8 | 218 | 167 | 39 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 5 | 21 | 2 / 1 | 4 | 60 | trigger_event(211); stop |
| 5 | 211 | 2 / 2 | 5 | 30 | set_switch(2); stop |
| 5 | 31 | 3 / 1 | 5 | 30 | trigger_event(311); stop |
| 5 | 311 | 3 / 2 | 5 | 30 | set_switch(3); stop |
| 5 | 41 | 4 / 1 | 6 | 60 | trigger_event(411); stop |
| 5 | 411 | 4 / 2 | 3 | 30 | trigger_event(412); stop |
| 5 | 412 | 4 / 3 | 1 | 30 | set_switch(4); stop |
| 5 | 51 | 5 / 1 | 3 | 60 | trigger_event(511); stop |
| 5 | 511 | 5 / 2 | 5 | 30 | trigger_event(512); stop |
| 5 | 512 | 5 / 3 | 4 | 30 | trigger_event(513); stop |
| 5 | 513 | 5 / 4 | 3 | 60 | trigger_event(514); stop |
| 5 | 514 | 5 / 5 | 0 | 90 | construct_objects(room=5,group_or_wave=1); stop |
| 5 | 101 | 10 / 1 | 2 | 10 | trigger_event(1011); stop |
| 5 | 1011 | 10 / 2 | 4 | 60 | set_switch(7); stop |
| 5 | 91 | 9 / 1 | 2 | 30 | trigger_event(911); stop |
| 5 | 911 | 9 / 2 | 6 | 60 | trigger_event(912); stop |
| 5 | 912 | 9 / 3 | 3 | 30 | set_switch(8); stop |
| 5 | 81 | 8 / 1 | 8 | 120 | construct_objects(room=8,group_or_wave=1); stop |
| 5 | 131 | 13 / 1 | 7 | 30 | trigger_event(1311); stop |
| 5 | 1311 | 13 / 2 | 4 | 30 | trigger_event(1312); stop |
| 5 | 1312 | 13 / 3 | 5 | 60 | construct_objects(room=13,group_or_wave=1); stop |
| 5 | 121 | 12 / 1 | 2 | 30 | set_switch(175); stop |
| 5 | 122 | 12 / 2 | 2 | 30 | set_switch(165); stop |
| 5 | 123 | 12 / 3 | 2 | 30 | set_switch(170); stop |
| 5 | 124 | 12 / 4 | 2 | 30 | set_switch(180); stop |
| 5 | 125 | 12 / 5 | 2 | 180 | set_switch(185); stop |
| 5 | 111 | 11 / 1 | 3 | 30 | trigger_event(1111); stop |
| 5 | 1111 | 11 / 2 | 4 | 30 | trigger_event(1112); stop |
| 5 | 1112 | 11 / 3 | 3 | 60 | trigger_event(1113); stop |
| 5 | 1113 | 11 / 4 | 4 | 30 | trigger_event(1114); stop |
| 5 | 1114 | 11 / 5 | 4 | 60 | trigger_event(1115); stop |
| 5 | 1115 | 11 / 6 | 5 | 30 | trigger_event(1116); stop |
| 5 | 1116 | 11 / 7 | 4 | 90 | trigger_event(1117); stop |
| 5 | 1117 | 11 / 8 | 4 | 30 | trigger_event(1118); stop |
| 5 | 1118 | 11 / 9 | 5 | 60 | trigger_event(1119); stop |
| 5 | 1119 | 11 / 10 | 5 | 60 | trigger_event(11111); stop |
| 5 | 11111 | 11 / 11 | 5 | 30 | trigger_event(11112); stop |
| 5 | 11112 | 11 / 12 | 4 | 30 | trigger_event(11113); stop |
| 5 | 11113 | 11 / 13 | 4 | 30 | trigger_event(11114); stop |
| 5 | 11114 | 11 / 14 | 6 | 60 | trigger_event(11115); stop |
| 5 | 11115 | 11 / 15 | 6 | 90 | trigger_event(11116); stop |
| 5 | 11116 | 11 / 16 | 3 | 60 | trigger_event(11117); stop |
| 5 | 11117 | 11 / 17 | 5 | 30 | set_switch(100); stop |
| 5 | 112 | 11 / 18 | 4 | 60 | trigger_event(1121); stop |
| 5 | 1121 | 11 / 19 | 4 | 150 | trigger_event(1122); stop |
| 5 | 1122 | 11 / 20 | 1 | 150 | trigger_event(1123); stop |
| 5 | 1123 | 11 / 21 | 3 | 150 | trigger_event(1124); stop |
| 5 | 1124 | 11 / 22 | 1 | 60 | set_switch(101); stop |
| 5 | 113 | 11 / 23 | 2 | 60 | trigger_event(1131); stop |
| 5 | 1131 | 11 / 24 | 2 | 90 | trigger_event(1132); stop |
| 5 | 1132 | 11 / 25 | 5 | 120 | construct_objects(room=11,group_or_wave=2); stop |
| 8 | 81 | 8 / 1 | 3 | 30 | trigger_event(811); stop |
| 8 | 811 | 8 / 2 | 7 | 90 | set_switch(100); stop |
| 8 | 82 | 8 / 3 | 4 | 30 | trigger_event(821); stop |
| 8 | 821 | 8 / 4 | 2 | 30 | set_switch(101); stop |
| 8 | 83 | 8 / 5 | 3 | 30 | trigger_event(831); stop |
| 8 | 831 | 8 / 6 | 2 | 60 | set_switch(105); stop |
| 8 | 84 | 8 / 7 | 5 | 10 | set_switch(10); stop |
| 8 | 41 | 4 / 1 | 1 | 90 | stop |
| 8 | 31 | 3 / 1 | 6 | 30 | trigger_event(311); stop |
| 8 | 311 | 3 / 2 | 7 | 60 | trigger_event(312); stop |
| 8 | 312 | 3 / 3 | 6 | 30 | trigger_event(313); stop |
| 8 | 313 | 3 / 4 | 6 | 15 | trigger_event(314); stop |
| 8 | 314 | 3 / 5 | 8 | 30 | trigger_event(315); stop |
| 8 | 315 | 3 / 6 | 1 | 90 | set_switch(11); stop |
| 8 | 51 | 5 / 1 | 6 | 60 | trigger_event(511); stop |
| 8 | 511 | 5 / 2 | 2 | 30 | trigger_event(512); stop |
| 8 | 512 | 5 / 3 | 5 | 30 | trigger_event(513); stop |
| 8 | 513 | 5 / 4 | 5 | 30 | trigger_event(514); stop |
| 8 | 514 | 5 / 5 | 8 | 150 | set_switch(18); stop |
| 8 | 101 | 10 / 1 | 1 | 60 | trigger_event(1011); stop |
| 8 | 1011 | 10 / 2 | 1 | 60 | trigger_event(1012); stop |
| 8 | 1012 | 10 / 3 | 3 | 120 | set_switch(3); stop |
| 8 | 21 | 2 / 1 | 1 | 30 | construct_objects(room=2,group_or_wave=2); stop |
| 8 | 22 | 2 / 2 | 6 | 45 | trigger_event(221); stop |
| 8 | 221 | 2 / 3 | 2 | 30 | trigger_event(222); stop |
| 8 | 222 | 2 / 4 | 3 | 60 | trigger_event(223); stop |
| 8 | 223 | 2 / 5 | 3 | 30 | trigger_event(224); stop |
| 8 | 224 | 2 / 6 | 3 | 30 | trigger_event(225); stop |
| 8 | 225 | 2 / 7 | 6 | 30 | trigger_event(226); stop |
| 8 | 226 | 2 / 8 | 5 | 30 | trigger_event(227); stop |
| 8 | 227 | 2 / 9 | 8 | 60 | trigger_event(228); stop |
| 8 | 228 | 2 / 10 | 8 | 30 | trigger_event(229); stop |
| 8 | 229 | 2 / 11 | 6 | 30 | trigger_event(2211); stop |
| 8 | 2211 | 2 / 12 | 8 | 30 | trigger_event(2212); stop |
| 8 | 2212 | 2 / 13 | 8 | 60 | set_switch(102); stop |
| 8 | 23 | 2 / 14 | 1 | 120 | trigger_event(231); stop |
| 8 | 231 | 2 / 15 | 2 | 150 | trigger_event(232); stop |
| 8 | 232 | 2 / 16 | 1 | 150 | set_switch(103); stop |
| 8 | 24 | 2 / 17 | 4 | 240 | set_switch(150); set_switch(1); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
