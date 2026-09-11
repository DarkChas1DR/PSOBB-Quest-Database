# Penumbral Surge #6 — extermination-ep2/q176-bb-e

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/extermination-ep2/q176-bb-e.zip?download=1)**

[Original QST](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/extermination-ep2/q176-bb-e.qst?download=1) · [Extracted BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/extermination-ep2/q176-bb-e/q176-bb-e.qst-quest0.bin?download=1) · [Extracted DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/extermination-ep2/q176-bb-e/q176-bb-e.qst-quest0.dat?download=1)

QST is the preserved original package. BIN and DAT are its decoded payload files, not reassembled scripts. The ZIP contains all three formats.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 176; language E. Static scan: **703 objects, 295 enemy/NPC records, 142 events, 109 script labels.** Script roundtrip: byte-identical.

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
| 0 | 53 | 9 | 0 |
| 15 | 9 | 9 | 1 |
| 16 | 330 | 156 | 78 |
| 17 | 311 | 121 | 63 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 15 | 1 | 30 / 1 | 9 | 1 | stop |
| 16 | 1 | 1 / 1 | 2 | 30 | trigger_event(2); stop |
| 16 | 2 | 1 / 2 | 3 | 35 | trigger_event(3); stop |
| 16 | 3 | 1 / 3 | 3 | 30 | set_switch(1); stop |
| 16 | 4 | 2 / 1 | 0 | 30 | stop |
| 16 | 5 | 2 / 2 | 2 | 30 | set_switch(2); construct_objects(room=2,group_or_wave=1); stop |
| 16 | 6 | 2 / 3 | 5 | 30 | set_switch(3); construct_objects(room=2,group_or_wave=2); stop |
| 16 | 7 | 2 / 4 | 2 | 45 | set_switch(4); construct_objects(room=2,group_or_wave=3); stop |
| 16 | 8 | 2 / 5 | 2 | 45 | set_switch(5); construct_objects(room=2,group_or_wave=4); stop |
| 16 | 9 | 2 / 6 | 3 | 1 | trigger_event(10); stop |
| 16 | 10 | 2 / 7 | 2 | 30 | set_switch(6); stop |
| 16 | 11 | 20 / 1 | 2 | 15 | trigger_event(12); stop |
| 16 | 12 | 20 / 2 | 3 | 40 | trigger_event(13); stop |
| 16 | 13 | 20 / 3 | 2 | 30 | set_switch(8); stop |
| 16 | 14 | 10 / 1 | 1 | 30 | set_switch(10); stop |
| 16 | 15 | 10 / 2 | 1 | 60 | trigger_event(16); stop |
| 16 | 16 | 10 / 3 | 1 | 30 | trigger_event(17); stop |
| 16 | 17 | 10 / 4 | 1 | 30 | set_switch(9); stop |
| 16 | 23 | 10 / 10 | 2 | 40 | set_switch(11); construct_objects(room=3,group_or_wave=1); stop |
| 16 | 24 | 3 / 1 | 4 | 30 | trigger_event(25); stop |
| 16 | 25 | 3 / 2 | 3 | 30 | set_switch(12); stop |
| 16 | 26 | 21 / 1 | 5 | 35 | trigger_event(27); stop |
| 16 | 27 | 21 / 2 | 4 | 30 | trigger_event(28); stop |
| 16 | 28 | 21 / 3 | 2 | 40 | construct_objects(room=21,group_or_wave=1); set_switch(71); stop |
| 16 | 29 | 21 / 4 | 7 | 90 | set_switch(13); stop |
| 16 | 30 | 5 / 1 | 2 | 30 | trigger_event(31); stop |
| 16 | 31 | 5 / 2 | 3 | 30 | trigger_event(32); stop |
| 16 | 32 | 5 / 3 | 2 | 75 | set_switch(14); stop |
| 16 | 33 | 4 / 1 | 2 | 40 | trigger_event(34); stop |
| 16 | 34 | 4 / 2 | 2 | 35 | set_switch(15); stop |
| 16 | 35 | 4 / 3 | 2 | 45 | trigger_event(36); stop |
| 16 | 36 | 4 / 4 | 3 | 35 | set_switch(16); construct_objects(room=4,group_or_wave=1); stop |
| 16 | 37 | 4 / 5 | 3 | 15 | set_switch(17); trigger_event(38); stop |
| 16 | 38 | 4 / 6 | 2 | 30 | trigger_event(39); stop |
| 16 | 39 | 4 / 7 | 2 | 30 | trigger_event(40); stop |
| 16 | 40 | 4 / 8 | 4 | 30 | trigger_event(41); stop |
| 16 | 41 | 4 / 9 | 2 | 30 | set_switch(18); stop |
| 16 | 43 | 22 / 1 | 1 | 30 | trigger_event(45); stop |
| 16 | 44 | 22 / 2 | 2 | 30 | trigger_event(46); stop |
| 16 | 45 | 22 / 3 | 1 | 30 | trigger_event(47); stop |
| 16 | 46 | 22 / 4 | 1 | 30 | trigger_event(48); stop |
| 16 | 47 | 22 / 5 | 1 | 30 | set_switch(20); stop |
| 16 | 48 | 22 / 6 | 1 | 45 | set_switch(21); stop |
| 16 | 49 | 30 / 36 | 2 | 60 | set_switch(22); trigger_event(50); trigger_event(51); trigger_event(52); trigger_event(53); stop |
| 16 | 50 | 30 / 1 | 1 | 90 | trigger_event(54); stop |
| 16 | 51 | 30 / 2 | 1 | 120 | trigger_event(55); stop |
| 16 | 52 | 30 / 3 | 1 | 150 | trigger_event(56); stop |
| 16 | 53 | 30 / 4 | 1 | 180 | trigger_event(57); stop |
| 16 | 54 | 30 / 5 | 1 | 60 | trigger_event(58); stop |
| 16 | 55 | 30 / 6 | 1 | 180 | trigger_event(59); stop |
| 16 | 56 | 30 / 7 | 1 | 90 | trigger_event(60); stop |
| 16 | 57 | 30 / 8 | 1 | 200 | trigger_event(61); stop |
| 16 | 58 | 30 / 9 | 1 | 250 | trigger_event(62); stop |
| 16 | 59 | 30 / 10 | 1 | 150 | trigger_event(63); stop |
| 16 | 60 | 30 / 11 | 1 | 60 | trigger_event(64); stop |
| 16 | 61 | 30 / 12 | 1 | 400 | trigger_event(65); stop |
| 16 | 62 | 30 / 13 | 1 | 100 | trigger_event(66); stop |
| 16 | 63 | 30 / 14 | 1 | 30 | trigger_event(67); stop |
| 16 | 64 | 30 / 15 | 1 | 300 | trigger_event(68); stop |
| 16 | 65 | 30 / 16 | 1 | 120 | trigger_event(69); stop |
| 16 | 66 | 30 / 17 | 2 | 90 | trigger_event(70); stop |
| 16 | 67 | 30 / 18 | 1 | 200 | trigger_event(71); stop |
| 16 | 68 | 30 / 19 | 1 | 100 | trigger_event(72); stop |
| 16 | 69 | 30 / 20 | 2 | 90 | trigger_event(73); stop |
| 16 | 70 | 30 / 21 | 1 | 155 | trigger_event(74); stop |
| 16 | 71 | 30 / 22 | 1 | 240 | trigger_event(75); stop |
| 16 | 72 | 30 / 23 | 1 | 130 | trigger_event(76); stop |
| 16 | 73 | 30 / 24 | 2 | 45 | trigger_event(77); trigger_event(78); stop |
| 16 | 74 | 30 / 25 | 1 | 60 | set_switch(23); stop |
| 16 | 75 | 30 / 26 | 1 | 155 | set_switch(24); stop |
| 16 | 76 | 30 / 27 | 1 | 350 | set_switch(25); stop |
| 16 | 77 | 30 / 28 | 1 | 100 | set_switch(26); stop |
| 16 | 78 | 30 / 29 | 1 | 200 | set_switch(27); stop |
| 16 | 79 | 30 / 30 | 4 | 120 | trigger_event(80); stop |
| 16 | 80 | 30 / 31 | 4 | 30 | trigger_event(81); stop |
| 16 | 81 | 30 / 32 | 4 | 30 | trigger_event(82); stop |
| 16 | 82 | 30 / 33 | 2 | 30 | trigger_event(83); stop |
| 16 | 83 | 30 / 34 | 5 | 30 | trigger_event(85); stop |
| 16 | 85 | 30 / 37 | 4 | 1 | set_switch(28); set_switch(29); stop |
| 17 | 1 | 1 / 1 | 0 | 60 | set_switch(1); trigger_event(2); stop |
| 17 | 2 | 1 / 2 | 1 | 30 | set_switch(2); stop |
| 17 | 3 | 2 / 1 | 2 | 40 | trigger_event(4); stop |
| 17 | 4 | 2 / 2 | 2 | 40 | set_switch(3); stop |
| 17 | 5 | 20 / 1 | 3 | 30 | trigger_event(6); stop |
| 17 | 6 | 20 / 2 | 3 | 40 | set_switch(4); stop |
| 17 | 7 | 10 / 1 | 1 | 20 | trigger_event(8); stop |
| 17 | 8 | 10 / 2 | 5 | 30 | trigger_event(9); stop |
| 17 | 9 | 10 / 3 | 2 | 30 | set_switch(5); construct_objects(room=3,group_or_wave=1); stop |
| 17 | 10 | 3 / 2 | 2 | 30 | set_switch(6); set_switch(3); stop |
| 17 | 12 | 3 / 3 | 5 | 45 | trigger_event(13); stop |
| 17 | 13 | 3 / 4 | 3 | 35 | trigger_event(14); stop |
| 17 | 14 | 3 / 5 | 3 | 35 | set_switch(7); stop |
| 17 | 15 | 4 / 1 | 2 | 30 | construct_objects(room=4,group_or_wave=1); stop |
| 17 | 16 | 4 / 2 | 2 | 25 | trigger_event(17); stop |
| 17 | 17 | 4 / 3 | 1 | 30 | construct_objects(room=4,group_or_wave=2); trigger_event(18); stop |
| 17 | 18 | 4 / 4 | 4 | 1 | construct_objects(room=4,group_or_wave=3); stop |
| 17 | 19 | 4 / 5 | 3 | 45 | construct_objects(room=4,group_or_wave=4); stop |
| 17 | 20 | 4 / 6 | 1 | 30 | set_switch(9); construct_objects(room=4,group_or_wave=5); stop |
| 17 | 21 | 21 / 1 | 3 | 30 | trigger_event(22); stop |
| 17 | 22 | 21 / 2 | 2 | 30 | trigger_event(23); stop |
| 17 | 23 | 21 / 3 | 4 | 35 | set_switch(10); construct_objects(room=21,group_or_wave=1); stop |
| 17 | 24 | 21 / 4 | 1 | 60 | trigger_event(25); stop |
| 17 | 25 | 21 / 5 | 2 | 35 | set_switch(11); stop |
| 17 | 26 | 5 / 1 | 2 | 30 | trigger_event(27); stop |
| 17 | 27 | 5 / 2 | 2 | 30 | trigger_event(28); stop |
| 17 | 28 | 5 / 3 | 3 | 30 | trigger_event(29); stop |
| 17 | 29 | 5 / 4 | 3 | 35 | set_switch(12); stop |
| 17 | 30 | 22 / 1 | 4 | 40 | trigger_event(31); stop |
| 17 | 31 | 22 / 2 | 4 | 30 | set_switch(13); trigger_event(33); stop |
| 17 | 32 | 22 / 3 | 2 | 35 | set_switch(14); trigger_event(34); stop |
| 17 | 33 | 22 / 4 | 1 | 60 | trigger_event(32); stop |
| 17 | 34 | 22 / 5 | 4 | 90 | set_switch(15); stop |
| 17 | 36 | 30 / 1 | 1 | 30 | set_switch(70); trigger_event(37); trigger_event(38); stop |
| 17 | 37 | 30 / 3 | 1 | 60 | trigger_event(39); stop |
| 17 | 38 | 30 / 4 | 2 | 90 | trigger_event(40); stop |
| 17 | 39 | 30 / 5 | 1 | 30 | trigger_event(41); stop |
| 17 | 40 | 30 / 6 | 1 | 30 | trigger_event(42); stop |
| 17 | 41 | 30 / 7 | 2 | 30 | trigger_event(43); stop |
| 17 | 42 | 30 / 8 | 1 | 30 | trigger_event(44); stop |
| 17 | 43 | 30 / 9 | 2 | 30 | trigger_event(45); stop |
| 17 | 44 | 30 / 10 | 1 | 30 | trigger_event(46); stop |
| 17 | 45 | 30 / 11 | 1 | 30 | trigger_event(47); stop |
| 17 | 46 | 30 / 12 | 1 | 30 | trigger_event(48); stop |
| 17 | 47 | 30 / 13 | 1 | 30 | trigger_event(49); stop |
| 17 | 48 | 30 / 14 | 1 | 30 | trigger_event(50); stop |
| 17 | 49 | 30 / 15 | 2 | 30 | trigger_event(51); stop |
| 17 | 50 | 30 / 16 | 1 | 30 | trigger_event(52); stop |
| 17 | 51 | 30 / 17 | 2 | 30 | trigger_event(53); stop |
| 17 | 52 | 30 / 18 | 1 | 30 | trigger_event(54); stop |
| 17 | 53 | 30 / 19 | 2 | 30 | trigger_event(55); stop |
| 17 | 54 | 30 / 20 | 1 | 30 | trigger_event(56); stop |
| 17 | 55 | 30 / 21 | 1 | 30 | trigger_event(57); stop |
| 17 | 56 | 30 / 22 | 2 | 30 | trigger_event(58); stop |
| 17 | 57 | 30 / 23 | 1 | 30 | trigger_event(59); stop |
| 17 | 58 | 30 / 24 | 1 | 30 | trigger_event(60); stop |
| 17 | 59 | 30 / 25 | 2 | 30 | trigger_event(61); stop |
| 17 | 60 | 30 / 26 | 1 | 30 | trigger_event(62); stop |
| 17 | 61 | 30 / 27 | 1 | 30 | trigger_event(63); stop |
| 17 | 62 | 30 / 28 | 1 | 30 | trigger_event(64); stop |
| 17 | 63 | 30 / 29 | 1 | 30 | set_switch(16); stop |
| 17 | 64 | 30 / 30 | 1 | 30 | set_switch(17); stop |
| 17 | 65 | 30 / 31 | 2 | 60 | set_switch(18); construct_objects(room=30,group_or_wave=1); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
