# Scarlet Realm #3 — extermination-ep1/q163-bb-e

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/extermination-ep1/q163-bb-e.zip?download=1)**

[Original QST](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/extermination-ep1/q163-bb-e.qst?download=1) · [Extracted BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/extermination-ep1/q163-bb-e/q163-bb-e.qst-quest0.bin?download=1) · [Extracted DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/extermination-ep1/q163-bb-e/q163-bb-e.qst-quest0.dat?download=1)

QST is the preserved original package. BIN and DAT are its decoded payload files, not reassembled scripts. The ZIP contains all three formats.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 163; language E. Static scan: **562 objects, 437 enemy/NPC records, 151 events, 115 script labels.** Script roundtrip: alignment-only.

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
| 6 | 285 | 166 | 69 |
| 7 | 247 | 262 | 82 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 6 | 1 | 60 / 1 | 3 | 30 | trigger_event(2); stop |
| 6 | 2 | 60 / 2 | 4 | 30 | set_switch(2); trigger_event(3); stop |
| 6 | 3 | 50 / 1 | 3 | 30 | trigger_event(4); stop |
| 6 | 4 | 50 / 2 | 3 | 30 | trigger_event(5); stop |
| 6 | 5 | 50 / 3 | 3 | 30 | set_switch(3); trigger_event(60); stop |
| 6 | 6 | 60 / 3 | 2 | 30 | trigger_event(7); stop |
| 6 | 7 | 60 / 4 | 3 | 40 | set_switch(4); stop |
| 6 | 8 | 51 / 1 | 4 | 30 | trigger_event(9); stop |
| 6 | 9 | 51 / 2 | 3 | 40 | trigger_event(10); stop |
| 6 | 10 | 51 / 3 | 4 | 40 | set_switch(1); construct_objects(room=51,group_or_wave=1); stop |
| 6 | 11 | 40 / 1 | 2 | 30 | trigger_event(12); stop |
| 6 | 12 | 40 / 2 | 1 | 30 | trigger_event(13); stop |
| 6 | 13 | 40 / 3 | 5 | 30 | trigger_event(14); stop |
| 6 | 14 | 40 / 4 | 4 | 30 | set_switch(5); set_switch(7); construct_objects(room=40,group_or_wave=1); construct_objects(room=75,group_or_wave=2); stop |
| 6 | 15 | 22 / 1 | 2 | 30 | trigger_event(16); stop |
| 6 | 16 | 22 / 2 | 2 | 30 | trigger_event(17); stop |
| 6 | 17 | 22 / 3 | 1 | 30 | trigger_event(170); stop |
| 6 | 170 | 22 / 4 | 4 | 30 | set_switch(6); set_switch(8); stop |
| 6 | 18 | 75 / 1 | 2 | 30 | trigger_event(19); stop |
| 6 | 19 | 75 / 2 | 1 | 30 | set_switch(9); stop |
| 6 | 20 | 75 / 3 | 4 | 40 | trigger_event(21); stop |
| 6 | 21 | 75 / 4 | 4 | 30 | trigger_event(22); stop |
| 6 | 22 | 75 / 5 | 1 | 30 | trigger_event(23); stop |
| 6 | 23 | 75 / 6 | 4 | 30 | set_switch(10); construct_objects(room=75,group_or_wave=1); stop |
| 6 | 24 | 30 / 1 | 3 | 30 | trigger_event(25); stop |
| 6 | 25 | 30 / 2 | 2 | 30 | trigger_event(26); stop |
| 6 | 26 | 30 / 3 | 3 | 30 | trigger_event(27); trigger_event(28); stop |
| 6 | 27 | 30 / 4 | 2 | 15 | trigger_event(29); stop |
| 6 | 28 | 30 / 5 | 2 | 30 | trigger_event(30); stop |
| 6 | 29 | 30 / 6 | 2 | 30 | trigger_event(31); stop |
| 6 | 30 | 30 / 7 | 2 | 30 | trigger_event(32); stop |
| 6 | 31 | 30 / 8 | 2 | 30 | set_switch(13); set_switch(14); stop |
| 6 | 32 | 30 / 9 | 2 | 30 | set_switch(15); set_switch(17); set_switch(18); stop |
| 6 | 34 | 90 / 1 | 2 | 40 | trigger_event(35); stop |
| 6 | 35 | 90 / 0 | 0 | 1 | set_switch(1); clear_switch(17); trigger_event(36); stop |
| 6 | 36 | 90 / 2 | 3 | 30 | trigger_event(37); stop |
| 6 | 37 | 90 / 3 | 3 | 30 | trigger_event(38); stop |
| 6 | 38 | 90 / 4 | 4 | 30 | trigger_event(39); stop |
| 6 | 39 | 90 / 5 | 4 | 30 | trigger_event(40); stop |
| 6 | 40 | 90 / 6 | 3 | 30 | trigger_event(4000); stop |
| 6 | 4000 | 90 / 7 | 2 | 30 | trigger_event(41); stop |
| 6 | 41 | 90 / 8 | 3 | 30 | set_switch(17); set_switch(20); stop |
| 6 | 42 | 52 / 1 | 2 | 30 | trigger_event(43); stop |
| 6 | 43 | 52 / 2 | 3 | 30 | trigger_event(44); stop |
| 6 | 44 | 52 / 3 | 4 | 30 | set_switch(21); construct_objects(room=52,group_or_wave=1); stop |
| 6 | 45 | 52 / 4 | 1 | 30 | trigger_event(46); stop |
| 6 | 46 | 52 / 5 | 3 | 30 | trigger_event(47); stop |
| 6 | 47 | 52 / 6 | 4 | 30 | set_switch(22); construct_objects(room=52,group_or_wave=2); stop |
| 6 | 48 | 6 / 1 | 2 | 40 | set_switch(27); construct_objects(room=6,group_or_wave=1); trigger_event(49); stop |
| 6 | 49 | 41 / 1 | 2 | 30 | trigger_event(50); stop |
| 6 | 50 | 41 / 2 | 3 | 30 | set_switch(28); trigger_event(51); stop |
| 6 | 51 | 54 / 1 | 3 | 1 | trigger_event(52); stop |
| 6 | 52 | 54 / 2 | 5 | 30 | set_switch(29); stop |
| 6 | 53 | 61 / 1 | 4 | 30 | trigger_event(54); stop |
| 6 | 54 | 61 / 2 | 5 | 30 | trigger_event(55); stop |
| 6 | 55 | 61 / 3 | 3 | 30 | set_switch(30); stop |
| 6 | 56 | 220 / 1 | 0 | 1 | set_switch(31); trigger_event(57); stop |
| 6 | 57 | 21 / 1 | 1 | 30 | set_switch(32); stop |
| 6 | 58 | 90 / 9 | 3 | 15 | trigger_event(59); stop |
| 6 | 59 | 90 / 10 | 2 | 30 | set_switch(33); stop |
| 6 | 60 | 8 / 1 | 2 | 30 | set_switch(34); construct_objects(room=8,group_or_wave=1); trigger_event(6); stop |
| 6 | 61 | 7 / 0 | 0 | 1 | construct_objects(room=7,group_or_wave=1); stop |
| 6 | 62 | 20 / 1 | 1 | 1 | stop |
| 6 | 63 | 20 / 2 | 0 | 1 | construct_objects(room=20,group_or_wave=2); stop |
| 6 | 64 | 20 / 3 | 0 | 1 | construct_objects(room=20,group_or_wave=3); stop |
| 6 | 65 | 20 / 4 | 0 | 1 | construct_objects(room=20,group_or_wave=4); stop |
| 6 | 66 | 20 / 5 | 0 | 1 | construct_objects(room=20,group_or_wave=5); stop |
| 6 | 67 | 20 / 6 | 0 | 1 | construct_objects(room=20,group_or_wave=6); stop |
| 6 | 68 | 20 / 7 | 0 | 1 | construct_objects(room=20,group_or_wave=1); stop |
| 7 | 1 | 50 / 0 | 0 | 1 | trigger_event(2); trigger_event(3); trigger_event(4); trigger_event(5); trigger_event(6); stop |
| 7 | 2 | 50 / 1 | 1 | 15 | set_switch(1); stop |
| 7 | 3 | 50 / 2 | 1 | 30 | set_switch(2); stop |
| 7 | 4 | 50 / 3 | 1 | 45 | set_switch(3); stop |
| 7 | 5 | 50 / 4 | 1 | 60 | set_switch(4); stop |
| 7 | 6 | 50 / 5 | 1 | 75 | set_switch(5); stop |
| 7 | 7 | 50 / 6 | 7 | 30 | set_switch(6); stop |
| 7 | 8 | 220 / 1 | 2 | 30 | trigger_event(9); stop |
| 7 | 9 | 220 / 2 | 1 | 30 | set_switch(7); stop |
| 7 | 10 | 51 / 1 | 4 | 30 | trigger_event(11); stop |
| 7 | 11 | 51 / 2 | 4 | 30 | set_switch(125); trigger_event(12); stop |
| 7 | 12 | 51 / 3 | 7 | 30 | trigger_event(13); stop |
| 7 | 13 | 51 / 4 | 6 | 30 | trigger_event(14); stop |
| 7 | 14 | 51 / 5 | 6 | 30 | trigger_event(15); stop |
| 7 | 15 | 51 / 6 | 6 | 30 | trigger_event(16); stop |
| 7 | 16 | 51 / 7 | 1 | 30 | trigger_event(17); stop |
| 7 | 17 | 51 / 8 | 4 | 30 | trigger_event(18); stop |
| 7 | 18 | 51 / 9 | 4 | 30 | trigger_event(19); stop |
| 7 | 19 | 51 / 10 | 4 | 30 | trigger_event(20); stop |
| 7 | 20 | 51 / 11 | 6 | 30 | trigger_event(21); stop |
| 7 | 21 | 51 / 12 | 2 | 30 | set_switch(8); stop |
| 7 | 22 | 51 / 13 | 0 | 30 | set_switch(100); set_switch(101); set_switch(102); set_switch(103); set_switch(104); set_switch(105); set_switch(106); set_switch(107); set_switch(108); set_switch(109); set_switch(110); set_switch(111); set_switch(112); set_switch(113); set_switch(114); set_switch(115); set_switch(116); set_switch(117); set_switch(118); set_switch(119); set_switch(120); set_switch(121); set_switch(122); set_switch(123); set_switch(124); stop |
| 7 | 23 | 20 / 1 | 3 | 30 | trigger_event(24); stop |
| 7 | 24 | 20 / 2 | 4 | 30 | set_switch(9); stop |
| 7 | 25 | 80 / 1 | 4 | 30 | trigger_event(26); stop |
| 7 | 26 | 80 / 2 | 5 | 30 | trigger_event(27); stop |
| 7 | 27 | 80 / 3 | 7 | 30 | set_switch(10); stop |
| 7 | 28 | 90 / 1 | 2 | 30 | trigger_event(29); stop |
| 7 | 29 | 90 / 2 | 4 | 30 | trigger_event(30); stop |
| 7 | 30 | 90 / 3 | 6 | 30 | set_switch(1); construct_objects(room=90,group_or_wave=1); trigger_event(31); stop |
| 7 | 31 | 90 / 4 | 1 | 30 | trigger_event(32); stop |
| 7 | 32 | 90 / 5 | 5 | 30 | trigger_event(33); stop |
| 7 | 33 | 90 / 6 | 5 | 30 | set_switch(12); trigger_event(34); stop |
| 7 | 34 | 4 / 1 | 1 | 30 | set_switch(13); construct_objects(room=4,group_or_wave=1); stop |
| 7 | 35 | 60 / 1 | 5 | 30 | trigger_event(36); stop |
| 7 | 36 | 60 / 2 | 6 | 30 | trigger_event(37); stop |
| 7 | 37 | 60 / 3 | 6 | 30 | set_switch(14); stop |
| 7 | 38 | 30 / 1 | 3 | 1 | trigger_event(39); stop |
| 7 | 39 | 30 / 2 | 5 | 30 | set_switch(15); trigger_event(40); stop |
| 7 | 40 | 80 / 4 | 5 | 1 | trigger_event(41); stop |
| 7 | 41 | 80 / 5 | 2 | 30 | trigger_event(42); stop |
| 7 | 42 | 80 / 6 | 2 | 30 | trigger_event(43); stop |
| 7 | 43 | 80 / 7 | 5 | 30 | set_switch(20); construct_objects(room=80,group_or_wave=1); trigger_event(44); stop |
| 7 | 44 | 40 / 1 | 4 | 1 | set_switch(21); trigger_event(45); stop |
| 7 | 45 | 5 / 1 | 1 | 30 | set_switch(22); construct_objects(room=5,group_or_wave=1); trigger_event(46); stop |
| 7 | 46 | 221 / 1 | 2 | 15 | trigger_event(47); stop |
| 7 | 47 | 221 / 2 | 6 | 30 | set_switch(23); stop |
| 7 | 48 | 53 / 1 | 4 | 30 | trigger_event(49); stop |
| 7 | 49 | 53 / 2 | 4 | 30 | trigger_event(50); stop |
| 7 | 50 | 53 / 3 | 4 | 30 | trigger_event(51); trigger_event(52); trigger_event(53); trigger_event(54); stop |
| 7 | 51 | 53 / 4 | 2 | 30 | set_switch(24); stop |
| 7 | 52 | 53 / 5 | 1 | 60 | set_switch(25); stop |
| 7 | 53 | 53 / 6 | 1 | 90 | set_switch(26); stop |
| 7 | 54 | 53 / 7 | 3 | 120 | set_switch(27); stop |
| 7 | 55 | 80 / 8 | 2 | 15 | trigger_event(550); stop |
| 7 | 550 | 80 / 9 | 3 | 30 | set_switch(28); trigger_event(56); stop |
| 7 | 56 | 7 / 1 | 2 | 30 | set_switch(29); construct_objects(room=7,group_or_wave=1); trigger_event(57); stop |
| 7 | 57 | 61 / 1 | 4 | 30 | trigger_event(58); stop |
| 7 | 58 | 61 / 2 | 5 | 30 | trigger_event(59); stop |
| 7 | 59 | 61 / 3 | 5 | 30 | trigger_event(60); stop |
| 7 | 60 | 61 / 4 | 8 | 30 | set_switch(30); stop |
| 7 | 61 | 21 / 1 | 4 | 30 | trigger_event(62); stop |
| 7 | 62 | 21 / 2 | 2 | 30 | trigger_event(63); trigger_event(64); trigger_event(65); trigger_event(66); stop |
| 7 | 63 | 21 / 3 | 1 | 30 | trigger_event(67); stop |
| 7 | 64 | 21 / 4 | 1 | 30 | trigger_event(68); stop |
| 7 | 65 | 21 / 5 | 1 | 30 | trigger_event(69); stop |
| 7 | 66 | 21 / 6 | 1 | 30 | trigger_event(70); stop |
| 7 | 67 | 21 / 7 | 2 | 30 | set_switch(31); trigger_event(71); stop |
| 7 | 68 | 21 / 8 | 2 | 30 | set_switch(32); trigger_event(72); stop |
| 7 | 69 | 21 / 9 | 2 | 30 | set_switch(33); trigger_event(73); stop |
| 7 | 70 | 21 / 10 | 2 | 30 | set_switch(34); trigger_event(74); stop |
| 7 | 71 | 21 / 11 | 1 | 30 | set_switch(35); stop |
| 7 | 72 | 21 / 12 | 1 | 30 | set_switch(36); stop |
| 7 | 73 | 21 / 13 | 1 | 30 | set_switch(37); stop |
| 7 | 74 | 21 / 14 | 1 | 30 | set_switch(38); stop |
| 7 | 75 | 21 / 15 | 1 | 60 | trigger_event(76); stop |
| 7 | 76 | 21 / 16 | 2 | 30 | set_switch(39); stop |
| 7 | 77 | 21 / 17 | 4 | 30 | trigger_event(78); stop |
| 7 | 78 | 21 / 18 | 4 | 30 | trigger_event(79); stop |
| 7 | 79 | 21 / 19 | 4 | 30 | trigger_event(80); stop |
| 7 | 80 | 21 / 20 | 5 | 30 | trigger_event(81); stop |
| 7 | 81 | 21 / 21 | 4 | 30 | set_switch(40); construct_objects(room=123,group_or_wave=1); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
