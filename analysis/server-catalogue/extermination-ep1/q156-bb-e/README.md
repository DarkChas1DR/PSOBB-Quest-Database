# Aberrant Grove — extermination-ep1/q156-bb-e

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/extermination-ep1/q156-bb-e.zip?download=1)**

[Original QST](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/extermination-ep1/q156-bb-e.qst?download=1) · [Extracted BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/extermination-ep1/q156-bb-e/q156-bb-e.qst-quest0.bin?download=1) · [Extracted DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/extermination-ep1/q156-bb-e/q156-bb-e.qst-quest0.dat?download=1)

QST is the preserved original package. BIN and DAT are its decoded payload files, not reassembled scripts. The ZIP contains all three formats.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 156; language E. Static scan: **138 objects, 204 enemy/NPC records, 53 events, 33 script labels.** Script roundtrip: alignment-only.

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
| 0 | 26 | 8 | 0 |
| 1 | 39 | 60 | 16 |
| 2 | 73 | 136 | 37 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 21 | 2 / 1 | 3 | 20 | trigger_event(22); stop |
| 1 | 22 | 2 / 2 | 3 | 20 | trigger_event(23); stop |
| 1 | 23 | 2 / 3 | 2 | 20 | trigger_event(24); stop |
| 1 | 24 | 2 / 4 | 3 | 20 | trigger_event(25); stop |
| 1 | 25 | 2 / 5 | 4 | 20 | trigger_event(26); stop |
| 1 | 26 | 2 / 6 | 2 | 20 | set_switch(2); stop |
| 1 | 41 | 4 / 1 | 6 | 20 | trigger_event(42); stop |
| 1 | 42 | 4 / 2 | 5 | 20 | trigger_event(43); stop |
| 1 | 43 | 4 / 3 | 5 | 20 | trigger_event(44); stop |
| 1 | 44 | 4 / 4 | 4 | 20 | trigger_event(45); stop |
| 1 | 45 | 4 / 5 | 5 | 20 | set_switch(9); stop |
| 1 | 71 | 7 / 1 | 2 | 20 | trigger_event(72); stop |
| 1 | 72 | 7 / 2 | 3 | 20 | trigger_event(73); stop |
| 1 | 73 | 7 / 3 | 4 | 20 | trigger_event(74); stop |
| 1 | 74 | 7 / 4 | 3 | 20 | trigger_event(75); stop |
| 1 | 75 | 7 / 5 | 6 | 20 | set_switch(3); stop |
| 2 | 11 | 1 / 1 | 1 | 20 | trigger_event(12); stop |
| 2 | 12 | 1 / 2 | 4 | 20 | trigger_event(13); stop |
| 2 | 13 | 1 / 3 | 4 | 20 | trigger_event(14); set_switch(100); stop |
| 2 | 14 | 1 / 4 | 3 | 20 | trigger_event(15); stop |
| 2 | 15 | 1 / 5 | 4 | 20 | trigger_event(16); stop |
| 2 | 16 | 1 / 6 | 3 | 20 | trigger_event(17); stop |
| 2 | 17 | 1 / 7 | 3 | 20 | set_switch(1); stop |
| 2 | 21 | 2 / 1 | 5 | 0 | trigger_event(22); stop |
| 2 | 22 | 2 / 2 | 5 | 20 | trigger_event(23); stop |
| 2 | 23 | 2 / 3 | 2 | 20 | trigger_event(24); stop |
| 2 | 24 | 2 / 4 | 4 | 20 | set_switch(60); set_switch(61); set_switch(101); stop |
| 2 | 31 | 3 / 1 | 3 | 20 | trigger_event(32); stop |
| 2 | 32 | 3 / 2 | 5 | 20 | trigger_event(33); stop |
| 2 | 33 | 3 / 3 | 3 | 20 | trigger_event(34); stop |
| 2 | 34 | 3 / 4 | 1 | 20 | trigger_event(35); stop |
| 2 | 35 | 3 / 5 | 4 | 20 | trigger_event(36); stop |
| 2 | 36 | 3 / 6 | 3 | 20 | construct_objects(room=3,group_or_wave=1); stop |
| 2 | 41 | 4 / 1 | 6 | 150 | stop |
| 2 | 61 | 6 / 1 | 1 | 20 | trigger_event(62); stop |
| 2 | 62 | 6 / 2 | 5 | 20 | trigger_event(63); stop |
| 2 | 63 | 6 / 3 | 4 | 20 | trigger_event(64); stop |
| 2 | 64 | 6 / 4 | 4 | 20 | trigger_event(65); stop |
| 2 | 65 | 6 / 5 | 3 | 20 | set_switch(62); stop |
| 2 | 111 | 11 / 1 | 4 | 20 | trigger_event(112); stop |
| 2 | 112 | 11 / 2 | 4 | 20 | trigger_event(113); stop |
| 2 | 113 | 11 / 3 | 3 | 20 | trigger_event(114); stop |
| 2 | 114 | 11 / 4 | 4 | 20 | trigger_event(115); stop |
| 2 | 115 | 11 / 5 | 5 | 20 | set_switch(4); set_switch(5); set_switch(6); stop |
| 2 | 121 | 12 / 1 | 2 | 20 | trigger_event(122); stop |
| 2 | 122 | 12 / 2 | 5 | 20 | trigger_event(123); stop |
| 2 | 123 | 12 / 3 | 6 | 20 | trigger_event(124); stop |
| 2 | 124 | 12 / 4 | 5 | 20 | trigger_event(125); stop |
| 2 | 125 | 12 / 5 | 3 | 20 | set_switch(10); stop |
| 2 | 131 | 13 / 1 | 5 | 20 | trigger_event(132); stop |
| 2 | 132 | 13 / 2 | 4 | 20 | trigger_event(133); stop |
| 2 | 133 | 13 / 3 | 4 | 20 | trigger_event(134); stop |
| 2 | 134 | 13 / 4 | 2 | 20 | set_switch(8); stop |

## Review notes

- Nonzero data after terminal header
