# Scarlet Realm #2 — extermination-ep1/q162-bb-e

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/extermination-ep1/q162-bb-e.zip?download=1)**

[Original QST](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/extermination-ep1/q162-bb-e.qst?download=1) · [Extracted BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/extermination-ep1/q162-bb-e/q162-bb-e.qst-quest0.bin?download=1) · [Extracted DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/extermination-ep1/q162-bb-e/q162-bb-e.qst-quest0.dat?download=1)

QST is the preserved original package. BIN and DAT are its decoded payload files, not reassembled scripts. The ZIP contains all three formats.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 162; language E. Static scan: **375 objects, 358 enemy/NPC records, 104 events, 59 script labels.** Script roundtrip: byte-identical.

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
| 4 | 151 | 153 | 42 |
| 5 | 194 | 196 | 62 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 4 | 1 | 11 / 1 | 2 | 30 | trigger_event(2); stop |
| 4 | 2 | 11 / 2 | 1 | 35 | set_switch(3); stop |
| 4 | 3 | 21 / 1 | 1 | 40 | trigger_event(4); stop |
| 4 | 4 | 21 / 2 | 4 | 30 | trigger_event(5); stop |
| 4 | 5 | 21 / 3 | 4 | 30 | set_switch(4); stop |
| 4 | 6 | 20 / 1 | 3 | 30 | trigger_event(7); stop |
| 4 | 7 | 20 / 2 | 3 | 30 | trigger_event(8); stop |
| 4 | 8 | 20 / 3 | 4 | 30 | set_switch(8); stop |
| 4 | 9 | 15 / 1 | 1 | 30 | trigger_event(10); stop |
| 4 | 10 | 15 / 2 | 4 | 30 | set_switch(9); stop |
| 4 | 11 | 22 / 1 | 5 | 30 | trigger_event(12); stop |
| 4 | 12 | 22 / 2 | 3 | 40 | set_switch(10); stop |
| 4 | 13 | 125 / 1 | 3 | 5 | set_switch(11); stop |
| 4 | 14 | 16 / 1 | 1 | 30 | trigger_event(15); stop |
| 4 | 15 | 16 / 2 | 5 | 30 | trigger_event(16); stop |
| 4 | 16 | 16 / 3 | 6 | 30 | set_switch(12); stop |
| 4 | 17 | 60 / 1 | 0 | 1 | set_switch(15); stop |
| 4 | 18 | 45 / 1 | 5 | 30 | trigger_event(19); stop |
| 4 | 19 | 45 / 2 | 3 | 30 | trigger_event(20); stop |
| 4 | 20 | 45 / 3 | 4 | 30 | set_switch(16); stop |
| 4 | 21 | 13 / 1 | 5 | 15 | trigger_event(22); stop |
| 4 | 22 | 13 / 3 | 4 | 30 | set_switch(17); stop |
| 4 | 23 | 112 / 1 | 2 | 5 | set_switch(19); stop |
| 4 | 24 | 40 / 1 | 5 | 30 | trigger_event(25); stop |
| 4 | 25 | 40 / 2 | 6 | 30 | trigger_event(26); stop |
| 4 | 26 | 40 / 3 | 4 | 30 | trigger_event(27); stop |
| 4 | 27 | 40 / 4 | 3 | 40 | set_switch(20); stop |
| 4 | 28 | 35 / 1 | 4 | 30 | trigger_event(29); stop |
| 4 | 29 | 35 / 2 | 6 | 30 | set_switch(21); construct_objects(room=35,group_or_wave=1); trigger_event(40); stop |
| 4 | 40 | 110 / 1 | 2 | 30 | set_switch(42); stop |
| 4 | 30 | 30 / 1 | 2 | 30 | trigger_event(31); stop |
| 4 | 31 | 30 / 2 | 6 | 1 | trigger_event(41); stop |
| 4 | 41 | 30 / 3 | 5 | 30 | set_switch(26); stop |
| 4 | 32 | 23 / 1 | 5 | 1 | trigger_event(33); stop |
| 4 | 33 | 23 / 2 | 4 | 30 | trigger_event(42); stop |
| 4 | 42 | 23 / 3 | 5 | 30 | set_switch(27); stop |
| 4 | 34 | 14 / 1 | 4 | 15 | trigger_event(36); stop |
| 4 | 35 | 14 / 2 | 4 | 30 | trigger_event(37); stop |
| 4 | 36 | 14 / 3 | 4 | 30 | trigger_event(38); stop |
| 4 | 37 | 14 / 4 | 1 | 30 | trigger_event(39); stop |
| 4 | 38 | 14 / 5 | 5 | 30 | set_switch(28); stop |
| 4 | 39 | 14 / 6 | 2 | 30 | set_switch(29); stop |
| 5 | 1 | 40 / 1 | 4 | 30 | trigger_event(2); stop |
| 5 | 2 | 40 / 2 | 4 | 30 | trigger_event(3); stop |
| 5 | 3 | 40 / 3 | 2 | 30 | trigger_event(4); stop |
| 5 | 4 | 40 / 4 | 3 | 30 | set_switch(1); stop |
| 5 | 5 | 31 / 1 | 3 | 30 | trigger_event(6); stop |
| 5 | 6 | 31 / 2 | 4 | 30 | set_switch(2); stop |
| 5 | 7 | 70 / 1 | 3 | 40 | trigger_event(8); stop |
| 5 | 8 | 70 / 2 | 5 | 30 | trigger_event(9); stop |
| 5 | 9 | 70 / 3 | 6 | 30 | set_switch(3); stop |
| 5 | 10 | 53 / 1 | 5 | 30 | trigger_event(11); stop |
| 5 | 11 | 53 / 2 | 4 | 30 | trigger_event(12); stop |
| 5 | 12 | 53 / 3 | 7 | 30 | trigger_event(13); stop |
| 5 | 13 | 53 / 4 | 5 | 30 | set_switch(4); trigger_event(14); stop |
| 5 | 14 | 40 / 5 | 5 | 30 | set_switch(5); stop |
| 5 | 15 | 51 / 1 | 3 | 30 | trigger_event(16); stop |
| 5 | 16 | 51 / 2 | 3 | 30 | set_switch(6); trigger_event(17); stop |
| 5 | 17 | 51 / 3 | 3 | 30 | trigger_event(18); stop |
| 5 | 18 | 51 / 4 | 1 | 30 | set_switch(7); trigger_event(19); stop |
| 5 | 19 | 51 / 5 | 3 | 30 | trigger_event(60); stop |
| 5 | 60 | 51 / 6 | 1 | 30 | trigger_event(61); stop |
| 5 | 61 | 51 / 7 | 5 | 30 | set_switch(8); trigger_event(62); stop |
| 5 | 62 | 51 / 8 | 1 | 30 | trigger_event(63); stop |
| 5 | 63 | 51 / 9 | 2 | 30 | set_switch(9); stop |
| 5 | 20 | 21 / 1 | 5 | 30 | trigger_event(21); stop |
| 5 | 21 | 21 / 2 | 4 | 30 | trigger_event(22); stop |
| 5 | 22 | 21 / 3 | 3 | 30 | trigger_event(23); stop |
| 5 | 23 | 21 / 4 | 4 | 30 | set_switch(11); stop |
| 5 | 24 | 71 / 1 | 2 | 15 | set_switch(12); trigger_event(25); stop |
| 5 | 25 | 71 / 2 | 3 | 30 | set_switch(13); trigger_event(26); stop |
| 5 | 26 | 71 / 3 | 2 | 30 | trigger_event(27); stop |
| 5 | 27 | 71 / 4 | 3 | 30 | trigger_event(28); stop |
| 5 | 28 | 71 / 5 | 3 | 30 | set_switch(14); stop |
| 5 | 29 | 71 / 6 | 1 | 30 | set_switch(15); trigger_event(30); stop |
| 5 | 30 | 71 / 7 | 4 | 30 | trigger_event(31); stop |
| 5 | 31 | 71 / 8 | 4 | 30 | set_switch(16); stop |
| 5 | 32 | 71 / 9 | 4 | 30 | trigger_event(33); stop |
| 5 | 33 | 71 / 10 | 2 | 30 | set_switch(17); trigger_event(34); stop |
| 5 | 34 | 71 / 11 | 3 | 30 | set_switch(18); stop |
| 5 | 35 | 60 / 1 | 4 | 30 | trigger_event(36); stop |
| 5 | 36 | 60 / 2 | 5 | 30 | set_switch(20); stop |
| 5 | 37 | 54 / 1 | 1 | 30 | trigger_event(41); stop |
| 5 | 38 | 54 / 2 | 1 | 30 | trigger_event(42); stop |
| 5 | 39 | 54 / 3 | 1 | 30 | trigger_event(43); stop |
| 5 | 40 | 54 / 4 | 1 | 30 | trigger_event(44); stop |
| 5 | 41 | 54 / 5 | 1 | 30 | trigger_event(45); stop |
| 5 | 42 | 54 / 6 | 1 | 30 | trigger_event(46); stop |
| 5 | 43 | 54 / 7 | 1 | 30 | trigger_event(47); stop |
| 5 | 44 | 54 / 8 | 1 | 30 | trigger_event(48); stop |
| 5 | 45 | 54 / 9 | 1 | 30 | set_switch(21); stop |
| 5 | 46 | 54 / 10 | 1 | 30 | set_switch(22); stop |
| 5 | 47 | 54 / 11 | 1 | 30 | set_switch(23); stop |
| 5 | 48 | 54 / 12 | 1 | 30 | set_switch(24); stop |
| 5 | 49 | 54 / 13 | 7 | 30 | trigger_event(50); stop |
| 5 | 50 | 54 / 14 | 4 | 30 | trigger_event(51); stop |
| 5 | 51 | 54 / 15 | 6 | 30 | trigger_event(52); stop |
| 5 | 52 | 54 / 16 | 5 | 30 | trigger_event(53); stop |
| 5 | 53 | 54 / 17 | 4 | 30 | trigger_event(54); stop |
| 5 | 54 | 54 / 18 | 4 | 30 | trigger_event(55); stop |
| 5 | 55 | 54 / 19 | 5 | 30 | trigger_event(56); stop |
| 5 | 56 | 54 / 20 | 6 | 30 | set_switch(25); stop |
| 5 | 57 | 30 / 0 | 0 | 1 | set_switch(28); stop |
| 5 | 58 | 20 / 1 | 5 | 30 | set_switch(38); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
