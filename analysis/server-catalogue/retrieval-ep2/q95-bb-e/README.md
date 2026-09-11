# Lost HEART BREAKER — retrieval-ep2/q95-bb-e

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/retrieval-ep2/q95-bb-e.zip?download=1)**

[Original QST](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/retrieval-ep2/q95-bb-e.qst?download=1) · [Extracted BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/retrieval-ep2/q95-bb-e/q95-bb-e.qst-quest0.bin?download=1) · [Extracted DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/retrieval-ep2/q95-bb-e/q95-bb-e.qst-quest0.dat?download=1)

QST is the preserved original package. BIN and DAT are its decoded payload files, not reassembled scripts. The ZIP contains all three formats.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 95; language E. Static scan: **547 objects, 436 enemy/NPC records, 113 events, 69 script labels.** Script roundtrip: alignment-only.

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

```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 54 | 17 | 0 |
| 5 | 126 | 9 | 4 |
| 16 | 264 | 228 | 62 |
| 17 | 103 | 182 | 47 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 5 | 5555 | 7 / 1 | 2 | 60 | construct_objects(room=7,group_or_wave=1); stop |
| 5 | 5556 | 11 / 1 | 2 | 120 | construct_objects(room=11,group_or_wave=1); stop |
| 5 | 5557 | 12 / 1 | 2 | 120 | construct_objects(room=12,group_or_wave=1); stop |
| 5 | 5558 | 13 / 1 | 2 | 120 | construct_objects(room=13,group_or_wave=1); construct_objects(room=10,group_or_wave=1); construct_objects(room=10,group_or_wave=2); set_switch(1); stop |
| 16 | 1 | 30 / 1 | 2 | 0 | trigger_event(11); stop |
| 16 | 11 | 30 / 2 | 2 | 60 | trigger_event(111); stop |
| 16 | 111 | 30 / 3 | 2 | 60 | construct_objects(room=30,group_or_wave=1); stop |
| 16 | 2 | 20 / 1 | 3 | 30 | trigger_event(21); stop |
| 16 | 21 | 20 / 2 | 4 | 150 | trigger_event(211); stop |
| 16 | 211 | 20 / 3 | 4 | 90 | set_switch(1); stop |
| 16 | 1000 | 20 / 4 | 1 | 1 | stop |
| 16 | 3 | 30 / 4 | 2 | 1 | trigger_event(31); stop |
| 16 | 31 | 30 / 5 | 2 | 60 | trigger_event(311); stop |
| 16 | 311 | 30 / 6 | 2 | 60 | construct_objects(room=30,group_or_wave=2); stop |
| 16 | 4 | 21 / 1 | 4 | 1 | trigger_event(41); stop |
| 16 | 41 | 21 / 2 | 9 | 60 | trigger_event(411); stop |
| 16 | 411 | 21 / 3 | 5 | 150 | set_switch(2); stop |
| 16 | 1001 | 21 / 4 | 1 | 1 | stop |
| 16 | 5 | 30 / 7 | 3 | 30 | trigger_event(51); stop |
| 16 | 51 | 30 / 8 | 3 | 60 | trigger_event(511); stop |
| 16 | 511 | 30 / 9 | 3 | 60 | construct_objects(room=30,group_or_wave=3); stop |
| 16 | 6 | 22 / 1 | 8 | 1 | trigger_event(61); stop |
| 16 | 61 | 22 / 2 | 5 | 120 | trigger_event(611); stop |
| 16 | 611 | 22 / 3 | 6 | 60 | set_switch(3); stop |
| 16 | 1002 | 22 / 4 | 1 | 60 | stop |
| 16 | 7 | 30 / 10 | 2 | 1 | trigger_event(71); stop |
| 16 | 71 | 30 / 11 | 2 | 90 | trigger_event(711); stop |
| 16 | 711 | 30 / 12 | 2 | 120 | construct_objects(room=30,group_or_wave=4); stop |
| 16 | 8 | 1 / 1 | 2 | 120 | trigger_event(81); stop |
| 16 | 81 | 1 / 2 | 5 | 90 | trigger_event(811); stop |
| 16 | 811 | 1 / 3 | 4 | 120 | trigger_event(8111); stop |
| 16 | 8111 | 1 / 4 | 8 | 180 | trigger_event(8112); stop |
| 16 | 8112 | 1 / 5 | 2 | 120 | construct_objects(room=1,group_or_wave=1); stop |
| 16 | 1003 | 1 / 6 | 1 | 1 | stop |
| 16 | 9 | 10 / 1 | 4 | 30 | trigger_event(91); stop |
| 16 | 91 | 10 / 2 | 3 | 60 | trigger_event(911); stop |
| 16 | 911 | 10 / 3 | 1 | 120 | set_switch(4); stop |
| 16 | 100 | 2 / 1 | 3 | 30 | stop |
| 16 | 101 | 2 / 2 | 2 | 1 | stop |
| 16 | 102 | 2 / 3 | 3 | 1 | construct_objects(room=2,group_or_wave=1); stop |
| 16 | 103 | 2 / 4 | 2 | 1 | stop |
| 16 | 104 | 2 / 5 | 3 | 60 | stop |
| 16 | 105 | 2 / 6 | 2 | 90 | construct_objects(room=2,group_or_wave=2); set_switch(5); stop |
| 16 | 1004 | 2 / 7 | 1 | 1 | stop |
| 16 | 106 | 3 / 1 | 1 | 30 | trigger_event(1061); stop |
| 16 | 1061 | 3 / 2 | 5 | 1 | trigger_event(1062); stop |
| 16 | 1062 | 3 / 3 | 5 | 60 | trigger_event(1063); stop |
| 16 | 1063 | 3 / 4 | 4 | 120 | set_switch(6); stop |
| 16 | 1005 | 3 / 5 | 1 | 60 | stop |
| 16 | 107 | 4 / 1 | 4 | 60 | set_switch(7); trigger_event(1071); stop |
| 16 | 1071 | 4 / 2 | 3 | 1 | trigger_event(1072); stop |
| 16 | 1072 | 4 / 3 | 3 | 1 | trigger_event(1073); stop |
| 16 | 1073 | 4 / 4 | 3 | 1 | trigger_event(1074); stop |
| 16 | 1074 | 4 / 5 | 3 | 60 | trigger_event(1075); stop |
| 16 | 1075 | 4 / 6 | 3 | 60 | set_switch(8); stop |
| 16 | 1006 | 4 / 7 | 1 | 1 | stop |
| 16 | 1007 | 4 / 8 | 1 | 1 | stop |
| 16 | 108 | 5 / 1 | 6 | 60 | trigger_event(1081); stop |
| 16 | 1081 | 5 / 2 | 5 | 60 | trigger_event(1082); stop |
| 16 | 1082 | 5 / 3 | 6 | 120 | trigger_event(1083); stop |
| 16 | 1083 | 5 / 4 | 10 | 180 | trigger_event(1084); set_switch(9); stop |
| 16 | 1008 | 10 / 4 | 1 | 120 | trigger_event(1009); stop |
| 16 | 1009 | 10 / 5 | 3 | 120 | trigger_event(1010); stop |
| 16 | 1010 | 10 / 6 | 5 | 120 | construct_objects(room=10,group_or_wave=1); stop |
| 16 | 3333 | 30 / 13 | 1 | 120 | trigger_event(3334); stop |
| 16 | 3334 | 30 / 14 | 2 | 180 | construct_objects(room=30,group_or_wave=6); stop |
| 17 | 1 | 1 / 1 | 1 | 90 | trigger_event(11); stop |
| 17 | 11 | 1 / 2 | 3 | 60 | trigger_event(12); stop |
| 17 | 12 | 1 / 3 | 4 | 60 | trigger_event(13); stop |
| 17 | 13 | 1 / 4 | 3 | 60 | trigger_event(14); stop |
| 17 | 14 | 1 / 5 | 2 | 90 | trigger_event(15); stop |
| 17 | 15 | 1 / 6 | 2 | 90 | set_switch(1); stop |
| 17 | 2 | 2 / 1 | 3 | 0 | trigger_event(21); stop |
| 17 | 21 | 2 / 2 | 3 | 60 | trigger_event(22); stop |
| 17 | 22 | 2 / 3 | 5 | 120 | trigger_event(23); stop |
| 17 | 23 | 2 / 4 | 4 | 90 | set_switch(2); stop |
| 17 | 4 | 4 / 1 | 3 | 60 | construct_objects(room=4,group_or_wave=1); stop |
| 17 | 400 | 4 / 2 | 3 | 60 | construct_objects(room=4,group_or_wave=2); stop |
| 17 | 401 | 4 / 3 | 3 | 30 | construct_objects(room=4,group_or_wave=3); stop |
| 17 | 402 | 4 / 4 | 2 | 120 | set_switch(3); stop |
| 17 | 10 | 10 / 1 | 2 | 30 | trigger_event(101); stop |
| 17 | 101 | 10 / 2 | 2 | 30 | trigger_event(102); stop |
| 17 | 102 | 10 / 3 | 3 | 60 | trigger_event(103); stop |
| 17 | 103 | 10 / 4 | 3 | 120 | trigger_event(104); construct_objects(room=10,group_or_wave=1); stop |
| 17 | 104 | 10 / 5 | 1 | 30 | set_switch(44); stop |
| 17 | 3 | 3 / 1 | 2 | 60 | trigger_event(31); stop |
| 17 | 31 | 3 / 2 | 5 | 120 | trigger_event(32); stop |
| 17 | 32 | 3 / 3 | 6 | 90 | trigger_event(33); stop |
| 17 | 33 | 3 / 4 | 2 | 60 | set_switch(5); stop |
| 17 | 20 | 20 / 1 | 5 | 60 | trigger_event(201); stop |
| 17 | 201 | 20 / 2 | 5 | 60 | trigger_event(202); stop |
| 17 | 202 | 20 / 3 | 7 | 60 | trigger_event(203); stop |
| 17 | 203 | 20 / 4 | 5 | 60 | trigger_event(204); stop |
| 17 | 204 | 20 / 5 | 2 | 60 | set_switch(6); construct_objects(room=20,group_or_wave=1); stop |
| 17 | 25 | 20 / 6 | 2 | 0 | stop |
| 17 | 211 | 21 / 1 | 5 | 30 | trigger_event(212); stop |
| 17 | 212 | 21 / 2 | 6 | 60 | trigger_event(213); stop |
| 17 | 213 | 21 / 3 | 5 | 60 | set_switch(7); stop |
| 17 | 51 | 5 / 1 | 3 | 60 | trigger_event(52); stop |
| 17 | 52 | 5 / 2 | 3 | 30 | trigger_event(53); stop |
| 17 | 53 | 5 / 3 | 4 | 30 | trigger_event(54); stop |
| 17 | 54 | 5 / 4 | 4 | 30 | trigger_event(55); stop |
| 17 | 55 | 5 / 5 | 5 | 90 | set_switch(8); stop |
| 17 | 221 | 22 / 1 | 5 | 60 | trigger_event(222); stop |
| 17 | 222 | 22 / 2 | 6 | 90 | trigger_event(223); stop |
| 17 | 223 | 22 / 3 | 6 | 30 | trigger_event(224); stop |
| 17 | 224 | 22 / 4 | 6 | 90 | set_switch(9); stop |
| 17 | 250 | 22 / 5 | 2 | 300 | stop |
| 17 | 301 | 30 / 1 | 1 | 60 | trigger_event(302); stop |
| 17 | 302 | 30 / 2 | 2 | 30 | trigger_event(303); stop |
| 17 | 303 | 30 / 3 | 1 | 120 | trigger_event(304); stop |
| 17 | 304 | 30 / 4 | 4 | 0 | trigger_event(305); stop |
| 17 | 305 | 30 / 5 | 6 | 180 | construct_objects(room=30,group_or_wave=5); stop |

## Review notes

- Floor 16: event 1083 targets absent event 1084
