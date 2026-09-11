# Sweep-up Operation #7 — extermination-ep2/q168-bb-e

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/extermination-ep2/q168-bb-e.zip?download=1)**

[Original QST](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/extermination-ep2/q168-bb-e.qst?download=1) · [Extracted BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/extermination-ep2/q168-bb-e/q168-bb-e.qst-quest0.bin?download=1) · [Extracted DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/extermination-ep2/q168-bb-e/q168-bb-e.qst-quest0.dat?download=1)

QST is the preserved original package. BIN and DAT are its decoded payload files, not reassembled scripts. The ZIP contains all three formats.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 168; language E. Static scan: **130 objects, 210 enemy/NPC records, 58 events, 44 script labels.** Script roundtrip: alignment-only.

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
| 0 | 43 | 8 | 0 |
| 6 | 87 | 202 | 58 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 6 | 151 | 15 / 1 | 5 | 1 | trigger_event(152); stop |
| 6 | 152 | 15 / 2 | 5 | 60 | trigger_event(153); stop |
| 6 | 153 | 15 / 3 | 1 | 60 | construct_objects(room=15,group_or_wave=1); stop |
| 6 | 154 | 15 / 4 | 1 | 1 | set_switch(1); trigger_event(156); stop |
| 6 | 156 | 15 / 6 | 6 | 90 | trigger_event(157); stop |
| 6 | 157 | 15 / 7 | 5 | 60 | trigger_event(158); stop |
| 6 | 158 | 15 / 8 | 4 | 60 | trigger_event(159); stop |
| 6 | 159 | 15 / 9 | 3 | 60 | trigger_event(155); stop |
| 6 | 155 | 15 / 5 | 7 | 60 | set_switch(3); set_switch(5); trigger_event(91); trigger_event(92); construct_objects(room=10,group_or_wave=1); stop |
| 6 | 101 | 10 / 1 | 2 | 1 | stop |
| 6 | 91 | 9 / 1 | 2 | 1 | stop |
| 6 | 92 | 9 / 2 | 2 | 1 | stop |
| 6 | 31 | 3 / 1 | 4 | 1 | trigger_event(32); stop |
| 6 | 32 | 3 / 2 | 4 | 60 | trigger_event(33); stop |
| 6 | 33 | 3 / 3 | 3 | 60 | trigger_event(34); stop |
| 6 | 34 | 3 / 4 | 3 | 60 | set_switch(170); stop |
| 6 | 35 | 3 / 5 | 5 | 60 | trigger_event(36); stop |
| 6 | 36 | 3 / 6 | 4 | 30 | trigger_event(37); stop |
| 6 | 37 | 3 / 7 | 3 | 60 | trigger_event(38); stop |
| 6 | 38 | 3 / 8 | 2 | 60 | set_switch(171); stop |
| 6 | 30 | 3 / 0 | 0 | 1 | set_switch(6); stop |
| 6 | 11 | 1 / 1 | 5 | 1 | trigger_event(12); stop |
| 6 | 12 | 1 / 2 | 5 | 30 | construct_objects(room=1,group_or_wave=1); set_switch(100); stop |
| 6 | 13 | 1 / 3 | 4 | 1 | construct_objects(room=3,group_or_wave=1); stop |
| 6 | 310 | 3 / 10 | 1 | 30 | trigger_event(311); stop |
| 6 | 311 | 3 / 11 | 5 | 60 | set_switch(8); stop |
| 6 | 41 | 4 / 1 | 8 | 60 | trigger_event(42); stop |
| 6 | 42 | 4 / 2 | 7 | 60 | trigger_event(43); stop |
| 6 | 43 | 4 / 3 | 5 | 60 | trigger_event(44); stop |
| 6 | 44 | 4 / 4 | 7 | 30 | set_switch(9); stop |
| 6 | 61 | 6 / 1 | 1 | 30 | trigger_event(62); stop |
| 6 | 62 | 6 / 2 | 7 | 20 | set_switch(101); construct_objects(room=4,group_or_wave=1); stop |
| 6 | 45 | 4 / 5 | 6 | 60 | set_switch(10); stop |
| 6 | 81 | 8 / 1 | 1 | 1 | trigger_event(82); stop |
| 6 | 82 | 8 / 2 | 4 | 10 | set_switch(102); construct_objects(room=8,group_or_wave=1); stop |
| 6 | 71 | 7 / 1 | 3 | 1 | stop |
| 6 | 111 | 11 / 1 | 6 | 1 | trigger_event(112); stop |
| 6 | 112 | 11 / 2 | 5 | 60 | trigger_event(113); trigger_event(118); trigger_event(1113); stop |
| 6 | 113 | 11 / 3 | 1 | 60 | trigger_event(114); stop |
| 6 | 114 | 11 / 4 | 1 | 10 | trigger_event(115); stop |
| 6 | 115 | 11 / 5 | 1 | 30 | trigger_event(116); stop |
| 6 | 116 | 11 / 6 | 1 | 30 | trigger_event(117); stop |
| 6 | 117 | 11 / 7 | 2 | 60 | set_switch(111); stop |
| 6 | 118 | 11 / 8 | 1 | 60 | trigger_event(119); stop |
| 6 | 119 | 11 / 9 | 1 | 10 | trigger_event(1110); stop |
| 6 | 1110 | 11 / 10 | 1 | 30 | trigger_event(1111); stop |
| 6 | 1111 | 11 / 11 | 1 | 30 | trigger_event(1112); stop |
| 6 | 1112 | 11 / 12 | 2 | 60 | set_switch(112); stop |
| 6 | 1113 | 11 / 13 | 1 | 60 | trigger_event(1114); stop |
| 6 | 1114 | 11 / 14 | 1 | 10 | trigger_event(1115); stop |
| 6 | 1115 | 11 / 15 | 1 | 30 | trigger_event(1116); stop |
| 6 | 1116 | 11 / 16 | 1 | 30 | trigger_event(1117); stop |
| 6 | 1117 | 11 / 17 | 2 | 60 | set_switch(113); stop |
| 6 | 1118 | 11 / 18 | 8 | 60 | trigger_event(1120); stop |
| 6 | 1120 | 11 / 20 | 8 | 60 | trigger_event(1121); stop |
| 6 | 1121 | 11 / 21 | 7 | 60 | trigger_event(1122); stop |
| 6 | 1122 | 11 / 22 | 3 | 60 | trigger_event(1123); stop |
| 6 | 1123 | 11 / 23 | 7 | 90 | set_switch(12); set_switch(2); stop |

## Review notes

- Nonzero data after terminal header
