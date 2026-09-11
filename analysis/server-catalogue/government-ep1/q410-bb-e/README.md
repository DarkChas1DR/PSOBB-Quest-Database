# 3-3:Central Control — government-ep1/q410-bb-e

Episode1; header quest ID 410; language E. Static scan: **412 objects, 224 enemy/NPC records, 61 events, 107 script labels.** Script roundtrip: byte-identical.

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
0x06, 0x06, 0x00, 0x02, 0x01
0x07, 0x07, 0x00, 0x02, 0x01
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 27 | 20 | 0 |
| 6 | 194 | 96 | 32 |
| 7 | 163 | 106 | 29 |
| 13 | 28 | 2 | 0 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 6 | 201 | 20 / 1 | 1 | 1 | set_switch(4); stop |
| 6 | 211 | 21 / 1 | 4 | 1 | set_switch(29); set_switch(30); set_switch(31); stop |
| 6 | 301 | 30 / 1 | 1 | 1 | trigger_event(3011); stop |
| 6 | 3011 | 30 / 2 | 4 | 30 | trigger_event(3012); stop |
| 6 | 3012 | 30 / 3 | 4 | 20 | trigger_event(3013); stop |
| 6 | 3013 | 30 / 4 | 2 | 1 | set_switch(12); set_switch(13); set_switch(14); set_switch(15); stop |
| 6 | 411 | 41 / 1 | 5 | 90 | set_switch(19); set_switch(23); stop |
| 6 | 501 | 50 / 1 | 5 | 1 | trigger_event(5011); stop |
| 6 | 5011 | 50 / 2 | 1 | 60 | set_switch(1); set_switch(3); stop |
| 6 | 511 | 51 / 1 | 1 | 1 | set_switch(9); set_switch(10); set_switch(11); stop |
| 6 | 512 | 51 / 2 | 2 | 1 | set_switch(10); set_switch(11); stop |
| 6 | 513 | 51 / 3 | 2 | 1 | set_switch(10); set_switch(11); stop |
| 6 | 514 | 51 / 4 | 1 | 1 | set_switch(9); set_switch(10); set_switch(11); stop |
| 6 | 521 | 52 / 1 | 3 | 1 | trigger_event(5211); stop |
| 6 | 5211 | 52 / 2 | 6 | 60 | set_switch(16); set_switch(17); set_switch(18); set_switch(19); set_switch(20); set_switch(21); stop |
| 6 | 531 | 53 / 1 | 4 | 1 | stop |
| 6 | 532 | 53 / 2 | 4 | 1 | set_switch(24); stop |
| 6 | 601 | 60 / 1 | 1 | 1 | trigger_event(6011); stop |
| 6 | 6011 | 60 / 2 | 3 | 20 | trigger_event(6012); stop |
| 6 | 6012 | 60 / 3 | 4 | 20 | trigger_event(6013); stop |
| 6 | 6013 | 60 / 4 | 4 | 1 | stop |
| 6 | 602 | 60 / 5 | 2 | 1200 | trigger_event(6021); stop |
| 6 | 6021 | 60 / 6 | 2 | 45 | trigger_event(6022); stop |
| 6 | 6022 | 60 / 7 | 2 | 60 | trigger_event(6023); stop |
| 6 | 6023 | 60 / 8 | 2 | 300 | set_switch(2); set_switch(3); set_switch(8); stop |
| 6 | 611 | 61 / 1 | 6 | 1 | trigger_event(6111); stop |
| 6 | 6111 | 61 / 2 | 4 | 45 | set_switch(22); set_switch(25); set_switch(26); set_switch(27); set_switch(32); stop |
| 6 | 612 | 61 / 3 | 4 | 60 | stop |
| 6 | 901 | 90 / 1 | 3 | 1 | stop |
| 6 | 902 | 90 / 2 | 4 | 1 | stop |
| 6 | 903 | 90 / 3 | 2 | 1 | trigger_event(9031); stop |
| 6 | 9031 | 90 / 4 | 3 | 1 | set_switch(6); set_switch(7); set_switch(9); stop |
| 7 | 201 | 20 / 1 | 3 | 1 | set_switch(1); set_switch(2); stop |
| 7 | 211 | 21 / 1 | 2 | 1 | set_switch(16); set_switch(17); stop |
| 7 | 301 | 30 / 1 | 7 | 1 | trigger_event(3011); stop |
| 7 | 3011 | 30 / 2 | 6 | 60 | trigger_event(3012); stop |
| 7 | 3012 | 30 / 3 | 2 | 30 | set_switch(14); set_switch(15); stop |
| 7 | 401 | 40 / 1 | 1 | 1 | set_switch(7); stop |
| 7 | 411 | 41 / 1 | 4 | 1 | set_switch(30); stop |
| 7 | 511 | 51 / 1 | 4 | 10 | trigger_event(5111); stop |
| 7 | 5111 | 51 / 2 | 3 | 45 | trigger_event(5112); stop |
| 7 | 5112 | 51 / 3 | 1 | 45 | stop |
| 7 | 512 | 51 / 4 | 4 | 35 | trigger_event(5121); stop |
| 7 | 5121 | 51 / 5 | 3 | 45 | trigger_event(5122); stop |
| 7 | 5122 | 51 / 6 | 5 | 45 | trigger_event(5123); stop |
| 7 | 5123 | 51 / 7 | 2 | 100 | trigger_event(5124); stop |
| 7 | 5124 | 51 / 8 | 2 | 100 | set_switch(3); set_switch(4); set_switch(9); stop |
| 7 | 521 | 52 / 1 | 7 | 1 | trigger_event(5211); stop |
| 7 | 5211 | 52 / 2 | 6 | 60 | trigger_event(5212); stop |
| 7 | 5212 | 52 / 3 | 1 | 60 | set_switch(18); set_switch(19); set_switch(20); set_switch(23); stop |
| 7 | 531 | 53 / 1 | 6 | 1 | trigger_event(5311); stop |
| 7 | 5311 | 53 / 2 | 5 | 60 | set_switch(21); set_switch(22); set_switch(23); set_switch(24); set_switch(25); stop |
| 7 | 532 | 53 / 3 | 1 | 160 | trigger_event(5321); stop |
| 7 | 5321 | 53 / 4 | 1 | 50 | stop |
| 7 | 601 | 60 / 1 | 1 | 1 | trigger_event(6011); stop |
| 7 | 6011 | 60 / 2 | 6 | 80 | set_switch(11); set_switch(13); stop |
| 7 | 611 | 61 / 1 | 7 | 1 | trigger_event(6111); stop |
| 7 | 6111 | 61 / 2 | 6 | 60 | set_switch(26); set_switch(27); set_switch(28); set_switch(29); stop |
| 7 | 612 | 61 / 3 | 5 | 45 | stop |
| 7 | 701 | 70 / 1 | 1 | 1 | trigger_event(7011); stop |
| 7 | 7011 | 70 / 2 | 4 | 40 | set_switch(5); set_switch(6); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
