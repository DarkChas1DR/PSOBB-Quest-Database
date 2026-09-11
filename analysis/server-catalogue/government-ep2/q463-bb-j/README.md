# ７－３：静寂の砂浜 — government-ep2/q463-bb-j

Episode2; header quest ID 463; language J. Static scan: **394 objects, 235 enemy/NPC records, 71 events, 98 script labels.** Script roundtrip: byte-identical.

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
0x08, 0x1A, 0x00, 0x01, 0x00
0x09, 0x1B, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 53 | 19 | 0 |
| 8 | 212 | 90 | 28 |
| 9 | 129 | 126 | 43 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 8 | 21 | 2 / 1 | 3 | 1 | trigger_event(211); stop |
| 8 | 211 | 2 / 2 | 3 | 100 | trigger_event(212); stop |
| 8 | 212 | 2 / 3 | 4 | 200 | set_switch(5); stop |
| 8 | 22 | 2 / 4 | 2 | 150 | trigger_event(221); stop |
| 8 | 221 | 2 / 5 | 2 | 150 | trigger_event(222); stop |
| 8 | 222 | 2 / 6 | 2 | 100 | stop |
| 8 | 31 | 3 / 1 | 3 | 1 | trigger_event(311); stop |
| 8 | 311 | 3 / 2 | 3 | 60 | trigger_event(312); stop |
| 8 | 312 | 3 / 3 | 3 | 100 | trigger_event(313); stop |
| 8 | 313 | 3 / 4 | 2 | 1 | trigger_event(314); stop |
| 8 | 314 | 3 / 6 | 0 | 100 | set_switch(7); stop |
| 8 | 32 | 3 / 5 | 2 | 1 | stop |
| 8 | 41 | 4 / 1 | 2 | 1 | trigger_event(411); stop |
| 8 | 411 | 4 / 2 | 2 | 100 | trigger_event(412); stop |
| 8 | 412 | 4 / 3 | 2 | 30 | set_switch(11); stop |
| 8 | 42 | 4 / 4 | 2 | 1 | stop |
| 8 | 43 | 4 / 5 | 2 | 1 | stop |
| 8 | 51 | 5 / 1 | 4 | 1 | trigger_event(511); stop |
| 8 | 511 | 5 / 2 | 2 | 30 | trigger_event(512); stop |
| 8 | 512 | 5 / 3 | 4 | 150 | trigger_event(513); stop |
| 8 | 513 | 5 / 4 | 3 | 300 | set_switch(15); set_switch(16); stop |
| 8 | 52 | 5 / 5 | 2 | 1 | stop |
| 8 | 54 | 5 / 6 | 2 | 30 | stop |
| 8 | 81 | 8 / 1 | 1 | 1 | set_switch(102); set_switch(19); set_switch(18); set_switch(9); stop |
| 8 | 82 | 8 / 2 | 3 | 300 | trigger_event(821); construct_objects(room=8,group_or_wave=1); stop |
| 8 | 821 | 8 / 3 | 3 | 300 | trigger_event(822); construct_objects(room=8,group_or_wave=2); stop |
| 8 | 822 | 8 / 4 | 3 | 300 | set_switch(101); stop |
| 8 | 101 | 10 / 1 | 1 | 1 | stop |
| 9 | 31 | 3 / 1 | 3 | 1 | trigger_event(311); trigger_event(3121); stop |
| 9 | 311 | 3 / 2 | 4 | 120 | trigger_event(312); stop |
| 9 | 3121 | 3 / 3 | 2 | 30 | stop |
| 9 | 312 | 3 / 4 | 4 | 10 | trigger_event(313); stop |
| 9 | 313 | 3 / 5 | 4 | 1 | trigger_event(314); trigger_event(3141); stop |
| 9 | 314 | 3 / 6 | 3 | 200 | trigger_event(315); stop |
| 9 | 3141 | 3 / 7 | 2 | 60 | stop |
| 9 | 315 | 3 / 8 | 3 | 100 | trigger_event(316); stop |
| 9 | 316 | 3 / 9 | 2 | 1 | trigger_event(317); trigger_event(3171); stop |
| 9 | 317 | 3 / 10 | 3 | 100 | trigger_event(319); stop |
| 9 | 319 | 3 / 11 | 4 | 60 | set_switch(2); set_switch(3); set_switch(12); stop |
| 9 | 3171 | 3 / 12 | 2 | 1 | stop |
| 9 | 32 | 3 / 13 | 2 | 100 | trigger_event(321); stop |
| 9 | 321 | 3 / 14 | 2 | 60 | trigger_event(3211); stop |
| 9 | 3211 | 3 / 15 | 2 | 30 | trigger_event(3212); stop |
| 9 | 3212 | 3 / 16 | 2 | 130 | trigger_event(3213); stop |
| 9 | 3213 | 3 / 17 | 2 | 100 | trigger_event(3214); stop |
| 9 | 3214 | 3 / 18 | 2 | 10 | stop |
| 9 | 61 | 6 / 1 | 2 | 1 | stop |
| 9 | 71 | 7 / 1 | 3 | 30 | trigger_event(711); stop |
| 9 | 711 | 7 / 2 | 3 | 1 | trigger_event(712); stop |
| 9 | 712 | 7 / 3 | 4 | 50 | trigger_event(713); stop |
| 9 | 713 | 7 / 6 | 6 | 50 | set_switch(4); set_switch(5); stop |
| 9 | 72 | 7 / 4 | 2 | 300 | trigger_event(721); stop |
| 9 | 721 | 7 / 5 | 3 | 500 | stop |
| 9 | 91 | 9 / 1 | 4 | 100 | trigger_event(911); stop |
| 9 | 911 | 9 / 2 | 4 | 200 | set_switch(6); set_switch(8); stop |
| 9 | 92 | 9 / 3 | 3 | 60 | trigger_event(921); stop |
| 9 | 921 | 9 / 4 | 4 | 30 | stop |
| 9 | 101 | 10 / 1 | 3 | 1 | stop |
| 9 | 111 | 11 / 1 | 1 | 240 | trigger_event(1111); stop |
| 9 | 1111 | 11 / 10 | 1 | 10 | trigger_event(1112); stop |
| 9 | 1112 | 11 / 11 | 1 | 10 | trigger_event(1113); stop |
| 9 | 1113 | 11 / 12 | 2 | 200 | construct_objects(room=11,group_or_wave=1); set_switch(7); set_switch(9); set_switch(10); set_switch(11); stop |
| 9 | 112 | 11 / 2 | 3 | 60 | construct_objects(room=11,group_or_wave=2); trigger_event(1121); stop |
| 9 | 1121 | 11 / 3 | 3 | 30 | construct_objects(room=11,group_or_wave=3); trigger_event(1122); stop |
| 9 | 1122 | 11 / 4 | 3 | 30 | trigger_event(1123); stop |
| 9 | 1123 | 11 / 5 | 4 | 1 | trigger_event(1124); stop |
| 9 | 1124 | 11 / 6 | 4 | 1 | trigger_event(1125); stop |
| 9 | 1125 | 11 / 7 | 4 | 1 | trigger_event(1126); stop |
| 9 | 1126 | 11 / 8 | 5 | 1 | trigger_event(1127); stop |
| 9 | 1127 | 11 / 9 | 5 | 1 | stop |
| 9 | 141 | 14 / 1 | 1 | 1 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
