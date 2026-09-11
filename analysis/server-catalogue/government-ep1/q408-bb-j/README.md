# ３－１：地に塗れた施設 — government-ep1/q408-bb-j

Episode1; header quest ID 408; language J. Static scan: **282 objects, 186 enemy/NPC records, 45 events, 77 script labels.** Script roundtrip: byte-identical.

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
0x07, 0x06, 0x00, 0x01, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 27 | 20 | 0 |
| 6 | 211 | 122 | 32 |
| 7 | 44 | 44 | 13 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 6 | 211 | 21 / 1 | 1 | 1 | set_switch(26); set_switch(27); set_switch(28); set_switch(29); set_switch(30); stop |
| 6 | 301 | 30 / 1 | 1 | 1 | trigger_event(3011); stop |
| 6 | 3011 | 30 / 2 | 4 | 60 | trigger_event(3012); stop |
| 6 | 3012 | 30 / 3 | 4 | 20 | trigger_event(3013); stop |
| 6 | 3013 | 30 / 4 | 2 | 1 | set_switch(17); set_switch(18); stop |
| 6 | 501 | 50 / 1 | 4 | 1 | trigger_event(5011); stop |
| 6 | 5011 | 50 / 2 | 4 | 15 | set_switch(2); set_switch(3); stop |
| 6 | 511 | 51 / 1 | 5 | 1 | trigger_event(5111); stop |
| 6 | 5111 | 51 / 2 | 6 | 1 | trigger_event(5112); stop |
| 6 | 5112 | 51 / 3 | 6 | 60 | set_switch(8); set_switch(9); set_switch(11); set_switch(12); set_switch(13); set_switch(38); stop |
| 6 | 512 | 51 / 4 | 4 | 1 | stop |
| 6 | 521 | 52 / 1 | 1 | 1 | trigger_event(5211); stop |
| 6 | 5211 | 52 / 2 | 6 | 30 | trigger_event(5212); stop |
| 6 | 5212 | 52 / 3 | 6 | 10 | set_switch(21); set_switch(22); set_switch(23); stop |
| 6 | 531 | 53 / 1 | 1 | 1 | set_switch(34); set_switch(37); stop |
| 6 | 532 | 53 / 2 | 4 | 1 | set_switch(37); stop |
| 6 | 541 | 54 / 1 | 4 | 1 | trigger_event(5411); stop |
| 6 | 5411 | 54 / 2 | 4 | 1 | set_switch(33); set_switch(34); set_switch(35); set_switch(36); stop |
| 6 | 601 | 60 / 1 | 4 | 1 | trigger_event(6011); stop |
| 6 | 6011 | 60 / 2 | 4 | 1 | set_switch(3); set_switch(5); set_switch(6); set_switch(7); set_switch(8); stop |
| 6 | 611 | 61 / 1 | 1 | 1 | trigger_event(6111); stop |
| 6 | 6111 | 61 / 2 | 4 | 20 | trigger_event(6112); stop |
| 6 | 6112 | 61 / 3 | 6 | 20 | trigger_event(6113); stop |
| 6 | 6113 | 61 / 4 | 4 | 1 | trigger_event(6114); stop |
| 6 | 6114 | 61 / 5 | 2 | 1 | set_switch(31); set_switch(32); stop |
| 6 | 752 | 75 / 1 | 4 | 60 | set_switch(14); stop |
| 6 | 753 | 75 / 2 | 4 | 1 | stop |
| 6 | 751 | 75 / 3 | 4 | 1 | trigger_event(7511); stop |
| 6 | 7511 | 75 / 4 | 4 | 1 | set_switch(15); set_switch(16); stop |
| 6 | 901 | 90 / 1 | 6 | 1 | trigger_event(9011); stop |
| 6 | 9011 | 90 / 2 | 4 | 1 | set_switch(19); set_switch(20); set_switch(21); set_switch(22); set_switch(24); stop |
| 6 | 902 | 90 / 3 | 4 | 90 | set_switch(23); stop |
| 7 | 2201 | 220 / 1 | 4 | 30 | set_switch(17); set_switch(18); set_switch(19); stop |
| 7 | 611 | 61 / 1 | 4 | 30 | trigger_event(6111); stop |
| 7 | 6111 | 61 / 2 | 6 | 30 | trigger_event(6112); stop |
| 7 | 6112 | 61 / 3 | 5 | 30 | trigger_event(6113); stop |
| 7 | 6113 | 61 / 4 | 6 | 30 | trigger_event(6114); stop |
| 7 | 6114 | 61 / 5 | 5 | 30 | trigger_event(6115); stop |
| 7 | 6115 | 61 / 6 | 7 | 30 | trigger_event(6116); stop |
| 7 | 6116 | 61 / 7 | 1 | 90 | trigger_event(6117); stop |
| 7 | 6117 | 61 / 8 | 2 | 60 | set_switch(101); stop |
| 7 | 612 | 61 / 9 | 1 | 120 | stop |
| 7 | 613 | 61 / 10 | 1 | 210 | stop |
| 7 | 614 | 61 / 11 | 1 | 300 | stop |
| 7 | 615 | 61 / 12 | 1 | 390 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
