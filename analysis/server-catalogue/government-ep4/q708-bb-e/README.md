# 9-8:The Final Cycle — government-ep4/q708-bb-e

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/government-ep4/q708-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep4/q708-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep4/q708-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode4; header quest ID 708; language E. Static scan: **428 objects, 365 enemy/NPC records, 74 events, 215 script labels.** Script roundtrip: byte-identical.

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
0x00, 0x2D, 0x00, 0x00, 0x00
0x06, 0x29, 0x00, 0x00, 0x00
0x07, 0x2A, 0x00, 0x00, 0x00
0x08, 0x2B, 0x00, 0x01, 0x00
0x09, 0x2C, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 27 | 22 | 0 |
| 6 | 90 | 112 | 22 |
| 7 | 140 | 102 | 22 |
| 8 | 145 | 126 | 29 |
| 9 | 26 | 3 | 1 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 6 | 621 | 62 / 1 | 6 | 30 | trigger_event(622); stop |
| 6 | 622 | 62 / 2 | 6 | 30 | set_switch(62); stop |
| 6 | 631 | 63 / 1 | 6 | 30 | trigger_event(632); stop |
| 6 | 632 | 63 / 2 | 6 | 30 | set_switch(63); stop |
| 6 | 901 | 90 / 1 | 6 | 30 | trigger_event(902); stop |
| 6 | 902 | 90 / 2 | 8 | 30 | trigger_event(903); stop |
| 6 | 903 | 90 / 3 | 7 | 30 | set_switch(90); stop |
| 6 | 904 | 90 / 4 | 6 | 30 | stop |
| 6 | 1001 | 100 / 1 | 6 | 30 | trigger_event(1002); stop |
| 6 | 1002 | 100 / 2 | 6 | 30 | trigger_event(1003); stop |
| 6 | 1003 | 100 / 3 | 6 | 30 | trigger_event(1004); stop |
| 6 | 1004 | 100 / 4 | 7 | 90 | trigger_event(1005); stop |
| 6 | 1005 | 100 / 5 | 6 | 90 | set_switch(100); stop |
| 6 | 1101 | 110 / 1 | 3 | 30 | trigger_event(1102); stop |
| 6 | 1102 | 110 / 2 | 3 | 30 | trigger_event(1103); stop |
| 6 | 1103 | 110 / 3 | 4 | 75 | trigger_event(1104); stop |
| 6 | 1104 | 110 / 4 | 3 | 30 | set_switch(111); stop |
| 6 | 1105 | 110 / 5 | 4 | 30 | trigger_event(1106); stop |
| 6 | 1106 | 110 / 6 | 3 | 30 | trigger_event(1107); stop |
| 6 | 1107 | 110 / 7 | 4 | 30 | trigger_event(1108); stop |
| 6 | 1108 | 110 / 8 | 4 | 30 | set_switch(112); stop |
| 6 | 311 | 31 / 0 | 2 | 30 | stop |
| 7 | 101 | 10 / 1 | 3 | 30 | trigger_event(102); stop |
| 7 | 102 | 10 / 2 | 2 | 30 | trigger_event(103); stop |
| 7 | 103 | 10 / 3 | 3 | 75 | set_switch(111); stop |
| 7 | 104 | 10 / 4 | 2 | 30 | trigger_event(105); stop |
| 7 | 105 | 10 / 5 | 2 | 30 | trigger_event(106); stop |
| 7 | 106 | 10 / 6 | 3 | 30 | set_switch(112); stop |
| 7 | 107 | 10 / 7 | 2 | 30 | trigger_event(108); stop |
| 7 | 108 | 10 / 8 | 3 | 30 | trigger_event(109); stop |
| 7 | 109 | 10 / 9 | 3 | 30 | set_switch(113); stop |
| 7 | 211 | 21 / 1 | 6 | 30 | trigger_event(212); stop |
| 7 | 212 | 21 / 2 | 6 | 30 | set_switch(21); stop |
| 7 | 221 | 22 / 1 | 7 | 30 | trigger_event(222); stop |
| 7 | 222 | 22 / 2 | 8 | 30 | trigger_event(223); stop |
| 7 | 223 | 22 / 3 | 7 | 30 | set_switch(22); stop |
| 7 | 231 | 23 / 1 | 6 | 30 | trigger_event(232); stop |
| 7 | 232 | 23 / 2 | 6 | 30 | set_switch(23); stop |
| 7 | 241 | 24 / 1 | 8 | 30 | set_switch(24); stop |
| 7 | 251 | 25 / 1 | 6 | 30 | trigger_event(252); stop |
| 7 | 252 | 25 / 2 | 5 | 30 | set_switch(25); stop |
| 7 | 501 | 50 / 1 | 6 | 30 | trigger_event(502); stop |
| 7 | 502 | 50 / 2 | 6 | 30 | set_switch(50); stop |
| 7 | 411 | 41 / 0 | 2 | 1 | stop |
| 8 | 201 | 20 / 1 | 7 | 30 | trigger_event(202); stop |
| 8 | 202 | 20 / 2 | 8 | 30 | trigger_event(203); stop |
| 8 | 203 | 20 / 3 | 7 | 30 | trigger_event(204); stop |
| 8 | 204 | 20 / 4 | 0 | 30 | set_switch(20); stop |
| 8 | 411 | 41 / 1 | 6 | 30 | trigger_event(412); stop |
| 8 | 412 | 41 / 2 | 6 | 30 | set_switch(41); stop |
| 8 | 511 | 51 / 1 | 9 | 150 | set_switch(51); stop |
| 8 | 601 | 60 / 1 | 6 | 30 | trigger_event(602); stop |
| 8 | 602 | 60 / 2 | 6 | 30 | set_switch(60); stop |
| 8 | 701 | 70 / 1 | 7 | 30 | trigger_event(702); stop |
| 8 | 702 | 70 / 2 | 7 | 30 | trigger_event(703); stop |
| 8 | 703 | 70 / 3 | 8 | 30 | set_switch(70); stop |
| 8 | 801 | 80 / 1 | 4 | 30 | construct_objects(room=80,group_or_wave=2); stop |
| 8 | 802 | 80 / 2 | 5 | 30 | construct_objects(room=80,group_or_wave=3); stop |
| 8 | 803 | 80 / 3 | 6 | 30 | set_switch(80); stop |
| 8 | 1011 | 101 / 1 | 3 | 30 | trigger_event(1012); stop |
| 8 | 1012 | 101 / 2 | 1 | 30 | trigger_event(1013); stop |
| 8 | 1013 | 101 / 3 | 2 | 30 | trigger_event(1014); stop |
| 8 | 1014 | 101 / 4 | 1 | 90 | set_switch(111); stop |
| 8 | 1015 | 101 / 5 | 2 | 30 | trigger_event(1016); stop |
| 8 | 1016 | 101 / 6 | 4 | 30 | trigger_event(1017); stop |
| 8 | 1017 | 101 / 7 | 1 | 30 | trigger_event(1018); stop |
| 8 | 1018 | 101 / 8 | 2 | 30 | set_switch(112); stop |
| 8 | 1019 | 101 / 9 | 2 | 30 | trigger_event(1020); stop |
| 8 | 1020 | 101 / 10 | 1 | 30 | trigger_event(1021); stop |
| 8 | 1021 | 101 / 11 | 4 | 30 | trigger_event(1022); stop |
| 8 | 1022 | 101 / 12 | 4 | 30 | set_switch(113); stop |
| 8 | 1101 | 110 / 0 | 5 | 1 | stop |
| 8 | 1102 | 110 / 0 | 5 | 1 | stop |
| 9 | 101 | 10 / 1 | 1 | 0 | set_switch(10); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
