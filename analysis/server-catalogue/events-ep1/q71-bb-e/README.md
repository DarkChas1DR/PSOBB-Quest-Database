# Milla Hunt — events-ep1/q71-bb-e

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/events-ep1/q71-bb-e.zip?download=1)**

[Original QST](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/events-ep1/q71-bb-e.qst?download=1) · [Extracted BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/events-ep1/q71-bb-e/q71-bb-e.qst-quest0.bin?download=1) · [Extracted DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/events-ep1/q71-bb-e/q71-bb-e.qst-quest0.dat?download=1)

QST is the preserved original package. BIN and DAT are its decoded payload files, not reassembled scripts. The ZIP contains all three formats.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 71; language E. Static scan: **296 objects, 211 enemy/NPC records, 50 events, 37 script labels.** Script roundtrip: alignment-only.

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
| 0 | 33 | 23 | 0 |
| 1 | 103 | 84 | 21 |
| 2 | 140 | 103 | 28 |
| 11 | 20 | 1 | 1 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 111 | 11 / 1 | 5 | 50 | trigger_event(1111); stop |
| 1 | 1111 | 11 / 2 | 5 | 50 | trigger_event(1112); stop |
| 1 | 1112 | 11 / 3 | 5 | 50 | trigger_event(1113); stop |
| 1 | 1113 | 11 / 4 | 6 | 50 | set_switch(5); set_switch(6); stop |
| 1 | 101 | 10 / 1 | 3 | 1 | trigger_event(1011); stop |
| 1 | 1011 | 10 / 2 | 3 | 1 | trigger_event(1012); stop |
| 1 | 1012 | 10 / 3 | 3 | 1 | set_switch(7); set_switch(8); stop |
| 1 | 51 | 5 / 1 | 3 | 1 | trigger_event(511); stop |
| 1 | 511 | 5 / 2 | 5 | 1 | trigger_event(512); stop |
| 1 | 512 | 5 / 3 | 4 | 1 | set_switch(1); stop |
| 1 | 52 | 5 / 4 | 5 | 1 | stop |
| 1 | 53 | 5 / 5 | 5 | 1 | stop |
| 1 | 22 | 2 / 1 | 4 | 1 | trigger_event(211); stop |
| 1 | 211 | 2 / 2 | 4 | 1 | trigger_event(212); stop |
| 1 | 212 | 2 / 3 | 4 | 1 | set_switch(2); stop |
| 1 | 71 | 7 / 1 | 1 | 1 | trigger_event(711); stop |
| 1 | 711 | 7 / 2 | 4 | 1 | trigger_event(712); stop |
| 1 | 712 | 7 / 3 | 1 | 1 | set_switch(3); stop |
| 1 | 41 | 4 / 1 | 6 | 1 | trigger_event(411); stop |
| 1 | 411 | 4 / 2 | 4 | 1 | set_switch(9); stop |
| 1 | 82 | 8 / 1 | 4 | 1 | stop |
| 2 | 21 | 2 / 1 | 1 | 1 | trigger_event(211); stop |
| 2 | 211 | 2 / 2 | 5 | 30 | trigger_event(2111); stop |
| 2 | 2111 | 2 / 3 | 4 | 20 | set_switch(4); set_switch(5); set_switch(6); stop |
| 2 | 31 | 3 / 1 | 7 | 200 | stop |
| 2 | 41 | 4 / 1 | 4 | 30 | set_switch(31); stop |
| 2 | 61 | 6 / 1 | 5 | 1 | trigger_event(611); stop |
| 2 | 611 | 6 / 2 | 5 | 15 | trigger_event(612); stop |
| 2 | 612 | 6 / 3 | 4 | 30 | set_switch(2); set_switch(3); stop |
| 2 | 71 | 7 / 1 | 3 | 100 | stop |
| 2 | 81 | 8 / 1 | 2 | 1 | stop |
| 2 | 101 | 10 / 1 | 5 | 1 | stop |
| 2 | 111 | 11 / 1 | 3 | 1 | trigger_event(1111); stop |
| 2 | 1111 | 11 / 2 | 4 | 10 | trigger_event(1112); stop |
| 2 | 1112 | 11 / 3 | 4 | 10 | trigger_event(1113); stop |
| 2 | 1113 | 11 / 4 | 5 | 10 | trigger_event(1114); stop |
| 2 | 1114 | 11 / 5 | 2 | 1 | set_switch(7); set_switch(8); set_switch(11); stop |
| 2 | 121 | 12 / 1 | 2 | 1 | trigger_event(1211); stop |
| 2 | 1211 | 12 / 2 | 7 | 1 | set_switch(10); stop |
| 2 | 131 | 13 / 1 | 1 | 1 | trigger_event(1311); stop |
| 2 | 1311 | 13 / 2 | 5 | 1 | set_switch(9); stop |
| 2 | 151 | 15 / 1 | 4 | 1 | trigger_event(1511); stop |
| 2 | 1511 | 15 / 2 | 4 | 60 | trigger_event(1512); stop |
| 2 | 1512 | 15 / 3 | 5 | 30 | trigger_event(1513); stop |
| 2 | 1513 | 15 / 4 | 1 | 1 | trigger_event(1514); stop |
| 2 | 1514 | 15 / 5 | 3 | 1 | set_switch(30); stop |
| 2 | 152 | 15 / 6 | 1 | 1 | trigger_event(1521); stop |
| 2 | 1521 | 15 / 7 | 5 | 30 | trigger_event(1522); stop |
| 2 | 1522 | 15 / 8 | 2 | 10 | stop |
| 11 | 1 | 1 / 1 | 1 | 50 | construct_objects(room=1,group_or_wave=1); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
