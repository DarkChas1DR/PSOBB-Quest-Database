# Scarlet Realm #1 — extermination-ep1/q161-bb-e

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/extermination-ep1/q161-bb-e.zip?download=1)**

[Original QST](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/extermination-ep1/q161-bb-e.qst?download=1) · [Extracted BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/extermination-ep1/q161-bb-e/q161-bb-e.qst-quest0.bin?download=1) · [Extracted DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/extermination-ep1/q161-bb-e/q161-bb-e.qst-quest0.dat?download=1)

QST is the preserved original package. BIN and DAT are its decoded payload files, not reassembled scripts. The ZIP contains all three formats.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 161; language E. Static scan: **246 objects, 235 enemy/NPC records, 93 events, 79 script labels.** Script roundtrip: alignment-only.

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
| 0 | 30 | 9 | 0 |
| 1 | 94 | 100 | 38 |
| 2 | 122 | 126 | 55 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 1 | 5 / 3 | 1 | 1 | stop |
| 1 | 2 | 5 / 1 | 2 | 30 | trigger_event(3); stop |
| 1 | 3 | 5 / 2 | 2 | 30 | set_switch(2); stop |
| 1 | 4 | 2 / 1 | 2 | 35 | trigger_event(5); stop |
| 1 | 5 | 2 / 2 | 3 | 30 | trigger_event(6); stop |
| 1 | 6 | 2 / 3 | 3 | 30 | set_switch(80); trigger_event(8); stop |
| 1 | 7 | 2 / 4 | 4 | 30 | stop |
| 1 | 8 | 7 / 7 | 0 | 1 | stop |
| 1 | 9 | 7 / 1 | 3 | 30 | trigger_event(10); stop |
| 1 | 10 | 7 / 2 | 2 | 30 | set_switch(4); construct_objects(room=4,group_or_wave=1); stop |
| 1 | 11 | 4 / 1 | 2 | 10 | trigger_event(12); stop |
| 1 | 12 | 4 / 2 | 2 | 1 | trigger_event(13); stop |
| 1 | 13 | 4 / 3 | 0 | 35 | trigger_event(14); stop |
| 1 | 14 | 4 / 4 | 2 | 30 | set_switch(5); stop |
| 1 | 15 | 8 / 1 | 2 | 40 | trigger_event(16); stop |
| 1 | 16 | 8 / 2 | 4 | 40 | trigger_event(17); stop |
| 1 | 17 | 8 / 3 | 4 | 30 | trigger_event(18); stop |
| 1 | 18 | 8 / 4 | 4 | 30 | set_switch(84); stop |
| 1 | 19 | 7 / 3 | 2 | 30 | trigger_event(20); stop |
| 1 | 20 | 7 / 4 | 3 | 30 | trigger_event(21); stop |
| 1 | 21 | 7 / 5 | 4 | 30 | trigger_event(22); stop |
| 1 | 22 | 7 / 6 | 5 | 30 | set_switch(82); set_switch(6); trigger_event(23); stop |
| 1 | 23 | 16 / 1 | 1 | 1 | trigger_event(29); stop |
| 1 | 24 | 16 / 2 | 2 | 30 | trigger_event(25); stop |
| 1 | 25 | 16 / 3 | 2 | 30 | trigger_event(26); stop |
| 1 | 26 | 16 / 4 | 1 | 30 | trigger_event(27); stop |
| 1 | 27 | 16 / 5 | 2 | 30 | trigger_event(28); stop |
| 1 | 28 | 16 / 6 | 2 | 30 | set_switch(88); stop |
| 1 | 29 | 16 / 7 | 2 | 1 | trigger_event(30); stop |
| 1 | 30 | 16 / 8 | 2 | 30 | set_switch(89); stop |
| 1 | 31 | 11 / 1 | 3 | 10 | trigger_event(32); stop |
| 1 | 32 | 11 / 2 | 6 | 30 | set_switch(7); stop |
| 1 | 33 | 10 / 1 | 1 | 30 | trigger_event(34); stop |
| 1 | 34 | 10 / 2 | 2 | 30 | set_switch(91); stop |
| 1 | 35 | 10 / 3 | 2 | 30 | set_switch(8); construct_objects(room=10,group_or_wave=1); stop |
| 1 | 36 | 10 / 4 | 4 | 30 | trigger_event(37); stop |
| 1 | 37 | 10 / 5 | 3 | 30 | trigger_event(38); stop |
| 1 | 38 | 10 / 6 | 4 | 30 | set_switch(9); stop |
| 2 | 1 | 15 / 1 | 2 | 40 | trigger_event(2); stop |
| 2 | 2 | 15 / 2 | 2 | 30 | trigger_event(3); stop |
| 2 | 3 | 15 / 3 | 2 | 30 | set_switch(250); trigger_event(4); stop |
| 2 | 4 | 15 / 4 | 4 | 30 | set_switch(1); set_switch(2); set_switch(79); stop |
| 2 | 7 | 13 / 1 | 1 | 60 | trigger_event(8); stop |
| 2 | 8 | 13 / 2 | 3 | 30 | trigger_event(9); trigger_event(100); stop |
| 2 | 9 | 13 / 3 | 3 | 30 | trigger_event(10); stop |
| 2 | 10 | 13 / 4 | 2 | 30 | set_switch(3); stop |
| 2 | 100 | 13 / 5 | 1 | 30 | stop |
| 2 | 11 | 5 / 1 | 2 | 15 | trigger_event(12); stop |
| 2 | 12 | 5 / 2 | 2 | 30 | trigger_event(14); stop |
| 2 | 14 | 5 / 4 | 3 | 30 | set_switch(70); stop |
| 2 | 15 | 6 / 1 | 3 | 60 | trigger_event(16); stop |
| 2 | 16 | 6 / 2 | 2 | 30 | set_switch(4); stop |
| 2 | 17 | 1 / 1 | 3 | 30 | trigger_event(18); stop |
| 2 | 18 | 1 / 2 | 3 | 30 | trigger_event(19); stop |
| 2 | 19 | 1 / 3 | 4 | 30 | set_switch(71); trigger_event(20); stop |
| 2 | 20 | 1 / 20 | 0 | 20 | set_switch(72); trigger_event(21); stop |
| 2 | 21 | 1 / 21 | 0 | 20 | set_switch(73); trigger_event(22); stop |
| 2 | 22 | 1 / 4 | 1 | 1 | trigger_event(23); stop |
| 2 | 23 | 1 / 5 | 4 | 30 | set_switch(5); stop |
| 2 | 24 | 2 / 1 | 3 | 60 | trigger_event(25); stop |
| 2 | 25 | 2 / 2 | 4 | 30 | trigger_event(26); stop |
| 2 | 26 | 2 / 3 | 6 | 30 | set_switch(6); construct_objects(room=6,group_or_wave=1); trigger_event(30); stop |
| 2 | 29 | 2 / 6 | 2 | 30 | set_switch(75); stop |
| 2 | 30 | 3 / 1 | 3 | 1 | trigger_event(31); stop |
| 2 | 31 | 3 / 2 | 4 | 30 | set_switch(7); trigger_event(32); stop |
| 2 | 32 | 11 / 1 | 1 | 1 | stop |
| 2 | 33 | 11 / 2 | 3 | 120 | set_switch(76); set_switch(77); stop |
| 2 | 34 | 15 / 7 | 4 | 30 | trigger_event(35); trigger_event(36); stop |
| 2 | 35 | 15 / 8 | 3 | 1 | set_switch(80); stop |
| 2 | 36 | 15 / 9 | 3 | 200 | trigger_event(37); stop |
| 2 | 37 | 15 / 10 | 3 | 100 | set_switch(81); stop |
| 2 | 38 | 4 / 1 | 5 | 20 | construct_objects(room=4,group_or_wave=1); stop |
| 2 | 39 | 4 / 2 | 3 | 40 | set_switch(8); stop |
| 2 | 40 | 12 / 1 | 2 | 30 | trigger_event(43); stop |
| 2 | 41 | 12 / 2 | 1 | 30 | trigger_event(44); stop |
| 2 | 42 | 12 / 3 | 1 | 30 | trigger_event(45); stop |
| 2 | 43 | 12 / 4 | 1 | 30 | trigger_event(46); stop |
| 2 | 44 | 12 / 5 | 2 | 30 | trigger_event(47); stop |
| 2 | 45 | 12 / 6 | 2 | 30 | trigger_event(48); stop |
| 2 | 46 | 12 / 7 | 1 | 30 | trigger_event(49); stop |
| 2 | 47 | 12 / 8 | 2 | 30 | trigger_event(50); stop |
| 2 | 48 | 12 / 9 | 2 | 30 | trigger_event(51); stop |
| 2 | 49 | 12 / 10 | 2 | 30 | trigger_event(52); stop |
| 2 | 50 | 12 / 11 | 3 | 30 | trigger_event(53); stop |
| 2 | 51 | 12 / 12 | 1 | 30 | trigger_event(54); stop |
| 2 | 52 | 12 / 13 | 2 | 30 | trigger_event(55); stop |
| 2 | 53 | 12 / 14 | 2 | 30 | trigger_event(56); stop |
| 2 | 54 | 12 / 15 | 1 | 30 | trigger_event(57); stop |
| 2 | 55 | 12 / 16 | 3 | 30 | set_switch(90); stop |
| 2 | 56 | 12 / 17 | 1 | 30 | set_switch(91); stop |
| 2 | 57 | 12 / 18 | 2 | 30 | set_switch(92); construct_objects(room=10,group_or_wave=1); stop |
| 2 | 60 | 7 / 0 | 0 | 1 | construct_objects(room=7,group_or_wave=1); stop |
| 2 | 61 | 10 / 1 | 1 | 1 | stop |

## Review notes

- Nonzero data after terminal header
