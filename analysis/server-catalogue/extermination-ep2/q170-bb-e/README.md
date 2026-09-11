# Sweep-up Operation #9 — extermination-ep2/q170-bb-e

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/extermination-ep2/q170-bb-e.zip?download=1)**

[Original QST](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/extermination-ep2/q170-bb-e.qst?download=1) · [Extracted BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/extermination-ep2/q170-bb-e/q170-bb-e.qst-quest0.bin?download=1) · [Extracted DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/extermination-ep2/q170-bb-e/q170-bb-e.qst-quest0.dat?download=1)

QST is the preserved original package. BIN and DAT are its decoded payload files, not reassembled scripts. The ZIP contains all three formats.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 170; language E. Static scan: **192 objects, 126 enemy/NPC records, 41 events, 42 script labels.** Script roundtrip: alignment-only.

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
| 17 | 149 | 118 | 41 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 17 | 301 | 30 / 1 | 1 | 90 | trigger_event(302); stop |
| 17 | 302 | 30 / 2 | 3 | 60 | trigger_event(303); stop |
| 17 | 303 | 30 / 3 | 1 | 15 | construct_objects(room=30,group_or_wave=1); stop |
| 17 | 221 | 22 / 1 | 3 | 60 | trigger_event(222); stop |
| 17 | 222 | 22 / 2 | 3 | 60 | trigger_event(223); stop |
| 17 | 223 | 22 / 3 | 1 | 30 | set_switch(9); stop |
| 17 | 51 | 5 / 1 | 3 | 90 | trigger_event(52); stop |
| 17 | 52 | 5 / 2 | 1 | 30 | trigger_event(53); trigger_event(56); stop |
| 17 | 53 | 5 / 3 | 1 | 60 | trigger_event(54); stop |
| 17 | 54 | 5 / 4 | 2 | 60 | stop |
| 17 | 56 | 5 / 6 | 2 | 30 | trigger_event(55); stop |
| 17 | 55 | 5 / 5 | 1 | 60 | stop |
| 17 | 50 | 5 / 0 | 0 | 1 | set_switch(8); stop |
| 17 | 211 | 21 / 1 | 5 | 90 | trigger_event(212); stop |
| 17 | 212 | 21 / 2 | 6 | 90 | trigger_event(213); stop |
| 17 | 213 | 21 / 3 | 3 | 90 | trigger_event(214); stop |
| 17 | 214 | 21 / 4 | 4 | 60 | set_switch(7); stop |
| 17 | 41 | 4 / 1 | 2 | 60 | trigger_event(42); stop |
| 17 | 42 | 4 / 2 | 3 | 60 | trigger_event(43); stop |
| 17 | 43 | 4 / 3 | 3 | 75 | set_switch(6); construct_objects(room=3,group_or_wave=1); stop |
| 17 | 31 | 3 / 1 | 1 | 90 | trigger_event(32); stop |
| 17 | 32 | 3 / 2 | 2 | 60 | trigger_event(33); stop |
| 17 | 33 | 3 / 3 | 5 | 60 | trigger_event(34); stop |
| 17 | 34 | 3 / 4 | 4 | 75 | set_switch(5); stop |
| 17 | 36 | 3 / 6 | 4 | 1 | set_switch(101); stop |
| 17 | 101 | 10 / 1 | 4 | 60 | trigger_event(102); stop |
| 17 | 102 | 10 / 2 | 5 | 30 | construct_objects(room=10,group_or_wave=1); stop |
| 17 | 103 | 10 / 3 | 4 | 30 | trigger_event(104); stop |
| 17 | 104 | 10 / 4 | 2 | 30 | set_switch(4); stop |
| 17 | 201 | 20 / 1 | 2 | 60 | trigger_event(202); stop |
| 17 | 202 | 20 / 2 | 3 | 60 | trigger_event(203); stop |
| 17 | 203 | 20 / 3 | 3 | 30 | set_switch(201); trigger_event(204); stop |
| 17 | 204 | 20 / 4 | 3 | 90 | trigger_event(205); stop |
| 17 | 205 | 20 / 5 | 3 | 90 | set_switch(3); stop |
| 17 | 21 | 2 / 1 | 3 | 120 | trigger_event(22); stop |
| 17 | 22 | 2 / 2 | 5 | 60 | set_switch(2); stop |
| 17 | 11 | 1 / 1 | 1 | 1 | trigger_event(12); stop |
| 17 | 12 | 1 / 2 | 6 | 90 | trigger_event(13); set_switch(99); stop |
| 17 | 13 | 1 / 3 | 2 | 30 | trigger_event(14); stop |
| 17 | 14 | 1 / 4 | 4 | 60 | trigger_event(15); stop |
| 17 | 15 | 1 / 5 | 4 | 120 | construct_objects(room=1,group_or_wave=1); set_switch(1); stop |

## Review notes

- Nonzero data after terminal header
