# 掃討作戦 第三号 — extermination-ep1/q103-bb-j

Episode1; header quest ID 103; language J. Static scan: **244 objects, 160 enemy/NPC records, 39 events, 141 script labels.** Script roundtrip: byte-identical.

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
0x06, 0x06, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 28 | 19 | 0 |
| 6 | 216 | 141 | 39 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 6 | 301 | 30 / 1 | 3 | 1 | trigger_event(3011); stop |
| 6 | 3011 | 30 / 2 | 4 | 60 | trigger_event(3012); stop |
| 6 | 3012 | 30 / 3 | 2 | 20 | trigger_event(3013); stop |
| 6 | 3013 | 30 / 4 | 2 | 1 | set_switch(17); set_switch(18); set_switch(20); set_switch(21); set_switch(22); set_switch(23); stop |
| 6 | 302 | 30 / 5 | 4 | 45 | trigger_event(3021); stop |
| 6 | 3021 | 30 / 6 | 4 | 60 | trigger_event(3022); stop |
| 6 | 3022 | 30 / 7 | 2 | 20 | trigger_event(3023); stop |
| 6 | 3023 | 30 / 8 | 2 | 1 | stop |
| 6 | 501 | 50 / 1 | 1 | 1 | trigger_event(5011); stop |
| 6 | 5011 | 50 / 2 | 7 | 15 | set_switch(2); set_switch(3); set_switch(235); stop |
| 6 | 511 | 51 / 1 | 4 | 1 | trigger_event(5111); stop |
| 6 | 5111 | 51 / 2 | 4 | 1 | stop |
| 6 | 512 | 51 / 3 | 2 | 1 | trigger_event(5121); stop |
| 6 | 5121 | 51 / 4 | 4 | 40 | trigger_event(5122); stop |
| 6 | 5122 | 51 / 5 | 1 | 60 | set_switch(8); set_switch(9); set_switch(12); set_switch(13); set_switch(38); stop |
| 6 | 531 | 53 / 1 | 5 | 60 | trigger_event(5311); stop |
| 6 | 5311 | 53 / 2 | 6 | 30 | trigger_event(5312); stop |
| 6 | 5312 | 53 / 3 | 6 | 50 | trigger_event(5313); stop |
| 6 | 5313 | 53 / 4 | 4 | 50 | stop |
| 6 | 532 | 53 / 5 | 3 | 70 | trigger_event(5321); stop |
| 6 | 5321 | 53 / 6 | 1 | 30 | trigger_event(5322); stop |
| 6 | 5322 | 53 / 7 | 2 | 30 | trigger_event(5323); stop |
| 6 | 5323 | 53 / 8 | 2 | 30 | set_switch(34); stop |
| 6 | 541 | 54 / 1 | 4 | 1 | trigger_event(5411); stop |
| 6 | 5411 | 54 / 2 | 4 | 1 | set_switch(33); set_switch(34); set_switch(36); stop |
| 6 | 601 | 60 / 1 | 3 | 1 | trigger_event(6011); stop |
| 6 | 6011 | 60 / 2 | 4 | 40 | trigger_event(6012); stop |
| 6 | 6012 | 60 / 3 | 2 | 60 | stop |
| 6 | 602 | 60 / 4 | 5 | 40 | trigger_event(6021); stop |
| 6 | 6021 | 60 / 5 | 4 | 40 | set_switch(5); set_switch(6); set_switch(8); stop |
| 6 | 611 | 61 / 1 | 7 | 1 | trigger_event(6111); stop |
| 6 | 6111 | 61 / 2 | 2 | 20 | trigger_event(6112); stop |
| 6 | 6112 | 61 / 3 | 9 | 20 | trigger_event(6113); stop |
| 6 | 6113 | 61 / 4 | 6 | 1 | set_switch(31); set_switch(32); stop |
| 6 | 751 | 75 / 1 | 1 | 1 | trigger_event(7511); stop |
| 6 | 7511 | 75 / 2 | 5 | 1 | set_switch(16); stop |
| 6 | 752 | 75 / 3 | 2 | 1 | stop |
| 6 | 901 | 90 / 1 | 2 | 120 | trigger_event(9011); stop |
| 6 | 9011 | 90 / 2 | 6 | 40 | set_switch(24); set_switch(26); set_switch(27); set_switch(28); set_switch(29); set_switch(30); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
