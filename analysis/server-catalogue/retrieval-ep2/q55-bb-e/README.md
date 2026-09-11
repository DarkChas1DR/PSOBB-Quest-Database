# Lost SHOCK GUNGNIR — retrieval-ep2/q55-bb-e

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/retrieval-ep2/q55-bb-e.zip?download=1)**

[Original QST](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/retrieval-ep2/q55-bb-e.qst?download=1) · [Extracted BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/retrieval-ep2/q55-bb-e/q55-bb-e.qst-quest0.bin?download=1) · [Extracted DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/retrieval-ep2/q55-bb-e/q55-bb-e.qst-quest0.dat?download=1)

QST is the preserved original package. BIN and DAT are its decoded payload files, not reassembled scripts. The ZIP contains all three formats.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 55; language E. Static scan: **501 objects, 415 enemy/NPC records, 73 events, 57 script labels.** Script roundtrip: alignment-only.

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
| 0 | 57 | 16 | 0 |
| 1 | 220 | 203 | 37 |
| 2 | 196 | 195 | 35 |
| 14 | 28 | 1 | 1 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 101 | 10 / 1 | 5 | 10 | trigger_event(102); stop |
| 1 | 102 | 10 / 2 | 5 | 10 | trigger_event(103); stop |
| 1 | 103 | 10 / 3 | 5 | 10 | trigger_event(104); stop |
| 1 | 104 | 10 / 4 | 5 | 10 | set_switch(3); stop |
| 1 | 111 | 11 / 1 | 0 | 1 | set_switch(39); set_switch(40); stop |
| 1 | 301 | 30 / 1 | 5 | 1 | set_switch(24); stop |
| 1 | 401 | 40 / 1 | 8 | 1 | trigger_event(4011); stop |
| 1 | 4011 | 40 / 2 | 9 | 20 | set_switch(21); set_switch(22); stop |
| 1 | 411 | 41 / 1 | 5 | 60 | trigger_event(4111); stop |
| 1 | 4111 | 41 / 2 | 5 | 100 | trigger_event(4112); stop |
| 1 | 4112 | 41 / 3 | 5 | 1 | trigger_event(4113); stop |
| 1 | 4113 | 41 / 4 | 5 | 1 | trigger_event(4114); stop |
| 1 | 4114 | 41 / 5 | 5 | 1 | trigger_event(4115); stop |
| 1 | 4115 | 41 / 6 | 5 | 1 | set_switch(25); set_switch(26); set_switch(27); set_switch(28); stop |
| 1 | 501 | 50 / 1 | 7 | 10 | trigger_event(5011); stop |
| 1 | 5011 | 50 / 2 | 8 | 10 | trigger_event(5012); stop |
| 1 | 5012 | 50 / 3 | 4 | 10 | set_switch(15); set_switch(16); stop |
| 1 | 601 | 60 / 1 | 6 | 10 | trigger_event(6011); stop |
| 1 | 6011 | 60 / 2 | 8 | 10 | trigger_event(6012); stop |
| 1 | 6012 | 60 / 3 | 3 | 10 | set_switch(5); set_switch(6); stop |
| 1 | 610 | 61 / 1 | 11 | 10 | trigger_event(6110); stop |
| 1 | 6110 | 61 / 2 | 8 | 10 | trigger_event(6111); stop |
| 1 | 6111 | 61 / 3 | 4 | 10 | set_switch(41); set_switch(42); set_switch(44); stop |
| 1 | 701 | 70 / 1 | 5 | 10 | stop |
| 1 | 702 | 70 / 2 | 5 | 10 | set_switch(35); set_switch(36); set_switch(37); set_switch(38); set_switch(39); set_switch(40); stop |
| 1 | 801 | 80 / 1 | 5 | 10 | trigger_event(811); stop |
| 1 | 811 | 80 / 2 | 8 | 10 | construct_objects(room=80,group_or_wave=1); stop |
| 1 | 8010 | 80 / 5 | 6 | 0 | set_switch(20); stop |
| 1 | 901 | 90 / 1 | 5 | 10 | set_switch(43); stop |
| 1 | 911 | 91 / 1 | 6 | 1 | set_switch(30); set_switch(29); stop |
| 1 | 921 | 92 / 1 | 8 | 20 | set_switch(32); set_switch(33); set_switch(34); stop |
| 1 | 931 | 93 / 1 | 5 | 10 | set_switch(7); set_switch(8); stop |
| 1 | 941 | 94 / 1 | 7 | 100 | trigger_event(9411); stop |
| 1 | 9411 | 94 / 2 | 6 | 100 | set_switch(7); set_switch(8); set_switch(9); set_switch(10); set_switch(12); set_switch(13); set_switch(14); set_switch(17); stop |
| 1 | 1021 | 102 / 1 | 4 | 1 | set_switch(4); stop |
| 1 | 1401 | 140 / 1 | 0 | 1 | stop |
| 1 | 1641 | 100 / 1 | 0 | 1 | stop |
| 2 | 101 | 10 / 1 | 4 | 10 | trigger_event(102); stop |
| 2 | 102 | 10 / 2 | 4 | 10 | trigger_event(103); stop |
| 2 | 103 | 10 / 3 | 4 | 10 | trigger_event(104); stop |
| 2 | 104 | 10 / 4 | 4 | 10 | set_switch(35); set_switch(36); stop |
| 2 | 111 | 11 / 1 | 3 | 10 | trigger_event(1111); stop |
| 2 | 1111 | 11 / 2 | 3 | 10 | trigger_event(1112); stop |
| 2 | 1112 | 11 / 3 | 10 | 60 | set_switch(39); set_switch(40); stop |
| 2 | 201 | 20 / 1 | 8 | 10 | construct_objects(room=20,group_or_wave=2); set_switch(19); set_switch(20); set_switch(22); stop |
| 2 | 301 | 30 / 1 | 5 | 30 | trigger_event(3011); stop |
| 2 | 3011 | 30 / 2 | 8 | 10 | set_switch(31); set_switch(32); set_switch(34); stop |
| 2 | 401 | 40 / 1 | 6 | 10 | trigger_event(4011); stop |
| 2 | 4011 | 40 / 2 | 8 | 10 | trigger_event(4012); stop |
| 2 | 4012 | 40 / 3 | 7 | 20 | set_switch(7); stop |
| 2 | 411 | 41 / 1 | 3 | 10 | trigger_event(4111); stop |
| 2 | 4111 | 41 / 2 | 3 | 10 | trigger_event(4112); stop |
| 2 | 4112 | 41 / 3 | 2 | 10 | trigger_event(4113); stop |
| 2 | 4113 | 41 / 4 | 4 | 10 | set_switch(13); set_switch(14); stop |
| 2 | 501 | 50 / 1 | 6 | 10 | set_switch(9); set_switch(10); stop |
| 2 | 502 | 50 / 2 | 6 | 10 | trigger_event(5021); stop |
| 2 | 5021 | 50 / 3 | 8 | 30 | set_switch(11); set_switch(12); stop |
| 2 | 601 | 60 / 1 | 10 | 10 | trigger_event(6011); stop |
| 2 | 6011 | 60 / 2 | 6 | 10 | set_switch(5); set_switch(6); stop |
| 2 | 611 | 61 / 1 | 1 | 0 | trigger_event(6111); stop |
| 2 | 6111 | 61 / 2 | 9 | 10 | trigger_event(6112); stop |
| 2 | 6112 | 61 / 3 | 9 | 10 | trigger_event(6113); stop |
| 2 | 6113 | 61 / 4 | 8 | 30 | set_switch(15); set_switch(17); set_switch(18); stop |
| 2 | 701 | 70 / 1 | 7 | 10 | trigger_event(7011); stop |
| 2 | 7011 | 70 / 2 | 7 | 10 | set_switch(26); stop |
| 2 | 702 | 70 / 3 | 4 | 10 | set_switch(29); set_switch(30); stop |
| 2 | 801 | 80 / 1 | 7 | 10 | construct_objects(room=80,group_or_wave=1); stop |
| 2 | 802 | 80 / 2 | 3 | 0 | set_switch(27); set_switch(28); set_switch(105); stop |
| 2 | 901 | 90 / 1 | 5 | 10 | set_switch(3); stop |
| 2 | 911 | 91 / 1 | 6 | 30 | set_switch(23); set_switch(24); stop |
| 2 | 931 | 93 / 1 | 5 | 30 | set_switch(37); set_switch(38); stop |
| 2 | 1031 | 103 / 1 | 2 | 10 | set_switch(8); stop |
| 14 | 1 | 1 / 1 | 1 | 50 | construct_objects(room=1,group_or_wave=1); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
