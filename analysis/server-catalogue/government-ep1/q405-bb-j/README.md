# ２－２：地中深くで — government-ep1/q405-bb-j

Episode1; header quest ID 405; language J. Static scan: **503 objects, 333 enemy/NPC records, 76 events, 80 script labels.** Script roundtrip: byte-identical.

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
0x03, 0x03, 0x00, 0x01, 0x00
0x04, 0x04, 0x00, 0x00, 0x00
0x05, 0x04, 0x00, 0x01, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 27 | 20 | 0 |
| 3 | 152 | 152 | 33 |
| 4 | 174 | 115 | 32 |
| 5 | 150 | 46 | 11 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 3 | 301 | 30 / 1 | 4 | 60 | trigger_event(3011); stop |
| 3 | 3011 | 30 / 2 | 4 | 60 | set_switch(10); set_switch(4); stop |
| 3 | 121 | 12 / 1 | 4 | 60 | trigger_event(1211); stop |
| 3 | 1211 | 12 / 2 | 5 | 60 | set_switch(2); set_switch(5); set_switch(6); stop |
| 3 | 511 | 51 / 1 | 5 | 60 | trigger_event(5111); stop |
| 3 | 5111 | 51 / 2 | 7 | 60 | trigger_event(5112); stop |
| 3 | 5112 | 51 / 3 | 4 | 60 | trigger_event(5113); stop |
| 3 | 5113 | 51 / 4 | 1 | 60 | set_switch(1); set_switch(3); set_switch(6); set_switch(7); set_switch(8); set_switch(9); set_switch(13); set_switch(14); stop |
| 3 | 101 | 10 / 1 | 4 | 60 | trigger_event(1011); stop |
| 3 | 1011 | 10 / 2 | 4 | 60 | trigger_event(1012); stop |
| 3 | 1012 | 10 / 3 | 3 | 60 | stop |
| 3 | 501 | 50 / 1 | 6 | 60 | set_switch(15); set_switch(16); set_switch(17); stop |
| 3 | 502 | 50 / 2 | 7 | 60 | trigger_event(5021); stop |
| 3 | 5021 | 50 / 3 | 1 | 60 | stop |
| 3 | 601 | 60 / 1 | 5 | 60 | trigger_event(6011); stop |
| 3 | 6011 | 60 / 2 | 4 | 60 | trigger_event(6012); stop |
| 3 | 6012 | 60 / 3 | 6 | 60 | trigger_event(6013); stop |
| 3 | 6013 | 60 / 4 | 5 | 60 | set_switch(18); set_switch(19); set_switch(20); set_switch(23); set_switch(25); stop |
| 3 | 321 | 32 / 1 | 5 | 60 | trigger_event(3211); stop |
| 3 | 3211 | 32 / 2 | 4 | 60 | set_switch(21); set_switch(22); set_switch(24); stop |
| 3 | 322 | 32 / 3 | 5 | 60 | stop |
| 3 | 521 | 52 / 1 | 5 | 60 | trigger_event(5211); stop |
| 3 | 5211 | 52 / 2 | 3 | 60 | trigger_event(5212); stop |
| 3 | 5212 | 52 / 3 | 4 | 60 | trigger_event(5213); stop |
| 3 | 5213 | 52 / 4 | 6 | 60 | set_switch(26); stop |
| 3 | 341 | 34 / 1 | 6 | 60 | trigger_event(3411); stop |
| 3 | 3411 | 34 / 2 | 6 | 60 | set_switch(27); set_switch(28); set_switch(29); set_switch(31); stop |
| 3 | 342 | 34 / 3 | 8 | 60 | stop |
| 3 | 111 | 11 / 1 | 1 | 60 | trigger_event(1111); stop |
| 3 | 1111 | 11 / 2 | 4 | 60 | trigger_event(1112); stop |
| 3 | 1112 | 11 / 3 | 3 | 60 | set_switch(30); stop |
| 3 | 331 | 33 / 1 | 5 | 60 | trigger_event(3311); stop |
| 3 | 3311 | 33 / 2 | 8 | 60 | set_switch(32); set_switch(33); stop |
| 4 | 141 | 14 / 1 | 3 | 60 | trigger_event(1411); stop |
| 4 | 1411 | 14 / 2 | 3 | 60 | set_switch(33); stop |
| 4 | 231 | 23 / 1 | 3 | 60 | trigger_event(2311); stop |
| 4 | 2311 | 23 / 2 | 4 | 60 | set_switch(32); set_switch(31); stop |
| 4 | 302 | 30 / 1 | 4 | 60 | set_switch(25); set_switch(30); set_switch(27); set_switch(24); stop |
| 4 | 303 | 30 / 2 | 7 | 60 | stop |
| 4 | 351 | 35 / 1 | 5 | 60 | trigger_event(3511); stop |
| 4 | 3511 | 35 / 2 | 4 | 60 | set_switch(26); set_switch(28); stop |
| 4 | 352 | 35 / 2 | 4 | 60 | stop |
| 4 | 402 | 40 / 1 | 3 | 30 | trigger_event(4021); stop |
| 4 | 4021 | 40 / 2 | 4 | 30 | set_switch(22); set_switch(23); set_switch(17); set_switch(18); set_switch(21); set_switch(35); set_switch(20); set_switch(19); set_switch(15); stop |
| 4 | 121 | 12 / 1 | 7 | 60 | stop |
| 4 | 122 | 12 / 2 | 1 | 60 | trigger_event(1221); stop |
| 4 | 1221 | 12 / 3 | 3 | 60 | set_switch(29); stop |
| 4 | 131 | 13 / 1 | 5 | 60 | set_switch(20); set_switch(19); set_switch(15); stop |
| 4 | 132 | 13 / 2 | 1 | 60 | stop |
| 4 | 601 | 60 / 1 | 2 | 60 | trigger_event(6011); stop |
| 4 | 6011 | 60 / 2 | 2 | 60 | trigger_event(6012); stop |
| 4 | 6012 | 60 / 3 | 5 | 60 | trigger_event(6013); stop |
| 4 | 6013 | 60 / 4 | 6 | 60 | set_switch(13); set_switch(14); stop |
| 4 | 111 | 11 / 1 | 1 | 60 | trigger_event(1111); stop |
| 4 | 1111 | 11 / 2 | 4 | 60 | set_switch(12); stop |
| 4 | 211 | 21 / 1 | 3 | 60 | trigger_event(2111); stop |
| 4 | 2111 | 21 / 2 | 5 | 60 | trigger_event(2112); stop |
| 4 | 2112 | 21 / 3 | 2 | 60 | set_switch(6); set_switch(5); set_switch(9); set_switch(4); set_switch(7); set_switch(3); stop |
| 4 | 161 | 16 / 1 | 3 | 60 | trigger_event(1611); stop |
| 4 | 1611 | 16 / 2 | 6 | 60 | set_switch(10); stop |
| 4 | 221 | 22 / 1 | 2 | 60 | set_switch(8); stop |
| 4 | 201 | 20 / 1 | 6 | 60 | trigger_event(2011); stop |
| 4 | 2011 | 20 / 2 | 1 | 60 | trigger_event(2012); stop |
| 4 | 2012 | 20 / 3 | 6 | 60 | set_switch(2); stop |
| 4 | 151 | 15 / 1 | 1 | 60 | set_switch(1); stop |
| 5 | 221 | 22 / 1 | 5 | 30 | set_switch(2); stop |
| 5 | 201 | 20 / 1 | 3 | 30 | trigger_event(2011); stop |
| 5 | 2011 | 20 / 2 | 4 | 120 | trigger_event(2012); stop |
| 5 | 2012 | 20 / 3 | 3 | 120 | trigger_event(2013); stop |
| 5 | 2013 | 20 / 4 | 4 | 120 | set_switch(101); stop |
| 5 | 202 | 20 / 5 | 4 | 30 | trigger_event(2021); stop |
| 5 | 2021 | 20 / 6 | 3 | 120 | trigger_event(2022); stop |
| 5 | 2022 | 20 / 7 | 4 | 120 | trigger_event(2023); stop |
| 5 | 2023 | 20 / 8 | 3 | 120 | set_switch(102); stop |
| 5 | 203 | 20 / 9 | 8 | 120 | trigger_event(2031); stop |
| 5 | 2031 | 20 / 10 | 5 | 60 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
