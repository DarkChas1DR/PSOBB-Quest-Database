# Sweep-up Operation #1 — extermination-ep1/q157-bb-e

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/extermination-ep1/q157-bb-e.zip?download=1)**

[Original QST](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/extermination-ep1/q157-bb-e.qst?download=1) · [Extracted BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/extermination-ep1/q157-bb-e/q157-bb-e.qst-quest0.bin?download=1) · [Extracted DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/extermination-ep1/q157-bb-e/q157-bb-e.qst-quest0.dat?download=1)

QST is the preserved original package. BIN and DAT are its decoded payload files, not reassembled scripts. The ZIP contains all three formats.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 157; language E. Static scan: **148 objects, 147 enemy/NPC records, 38 events, 46 script labels.** Script roundtrip: alignment-only.

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
| 0 | 28 | 10 | 0 |
| 2 | 120 | 137 | 38 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 2 | 110 | 11 / 0 | 0 | 0 | set_switch(77); stop |
| 2 | 111 | 11 / 1 | 2 | 30 | trigger_event(112); stop |
| 2 | 112 | 11 / 2 | 2 | 45 | stop |
| 2 | 113 | 11 / 3 | 3 | 30 | trigger_event(114); stop |
| 2 | 114 | 11 / 4 | 4 | 10 | trigger_event(115); stop |
| 2 | 115 | 11 / 5 | 1 | 20 | trigger_event(116); stop |
| 2 | 116 | 11 / 6 | 4 | 30 | stop |
| 2 | 31 | 3 / 1 | 2 | 10 | trigger_event(32); stop |
| 2 | 32 | 3 / 2 | 5 | 10 | trigger_event(33); stop |
| 2 | 33 | 3 / 3 | 3 | 10 | set_switch(51); stop |
| 2 | 21 | 2 / 1 | 5 | 10 | trigger_event(22); stop |
| 2 | 22 | 2 / 2 | 5 | 20 | trigger_event(23); stop |
| 2 | 23 | 2 / 3 | 5 | 25 | set_switch(63); stop |
| 2 | 10 | 1 / 0 | 0 | 0 | set_switch(62); stop |
| 2 | 11 | 1 / 1 | 1 | 10 | trigger_event(12); stop |
| 2 | 12 | 1 / 2 | 4 | 10 | stop |
| 2 | 13 | 1 / 3 | 3 | 10 | trigger_event(14); stop |
| 2 | 14 | 1 / 4 | 4 | 10 | trigger_event(15); stop |
| 2 | 15 | 1 / 5 | 3 | 10 | stop |
| 2 | 61 | 6 / 1 | 4 | 30 | trigger_event(62); stop |
| 2 | 62 | 6 / 2 | 3 | 10 | trigger_event(63); stop |
| 2 | 63 | 6 / 3 | 3 | 10 | set_switch(9); stop |
| 2 | 131 | 13 / 1 | 6 | 20 | trigger_event(132); stop |
| 2 | 132 | 13 / 2 | 6 | 10 | trigger_event(133); stop |
| 2 | 133 | 13 / 3 | 8 | 10 | trigger_event(134); stop |
| 2 | 134 | 13 / 4 | 6 | 10 | construct_objects(room=13,group_or_wave=1); set_switch(120); stop |
| 2 | 151 | 15 / 1 | 1 | 5 | trigger_event(152); stop |
| 2 | 152 | 15 / 2 | 4 | 10 | trigger_event(153); stop |
| 2 | 153 | 15 / 3 | 5 | 10 | trigger_event(154); stop |
| 2 | 154 | 15 / 4 | 7 | 10 | set_switch(90); construct_objects(room=15,group_or_wave=1); stop |
| 2 | 120 | 12 / 0 | 0 | 0 | set_switch(10); stop |
| 2 | 121 | 12 / 1 | 2 | 10 | set_switch(100); stop |
| 2 | 122 | 12 / 2 | 3 | 60 | trigger_event(123); stop |
| 2 | 123 | 12 / 3 | 3 | 20 | trigger_event(124); stop |
| 2 | 127 | 12 / 7 | 5 | 10 | trigger_event(126); stop |
| 2 | 124 | 12 / 4 | 4 | 150 | set_switch(101); stop |
| 2 | 125 | 12 / 5 | 5 | 30 | trigger_event(127); stop |
| 2 | 126 | 12 / 6 | 6 | 20 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
