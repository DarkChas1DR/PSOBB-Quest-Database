# Penumbral Surge #5 — extermination-ep2/q175-bb-e

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/extermination-ep2/q175-bb-e.zip?download=1)**

[Original QST](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/extermination-ep2/q175-bb-e.qst?download=1) · [Extracted BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/extermination-ep2/q175-bb-e/q175-bb-e.qst-quest0.bin?download=1) · [Extracted DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/extermination-ep2/q175-bb-e/q175-bb-e.qst-quest0.dat?download=1)

QST is the preserved original package. BIN and DAT are its decoded payload files, not reassembled scripts. The ZIP contains all three formats.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 175; language E. Static scan: **523 objects, 419 enemy/NPC records, 152 events, 56 script labels.** Script roundtrip: byte-identical.

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
| 10 | 212 | 198 | 67 |
| 11 | 258 | 212 | 85 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 10 | 1 | 230 / 1 | 1 | 25 | set_switch(2); stop |
| 10 | 3 | 2 / 1 | 2 | 20 | trigger_event(4); stop |
| 10 | 4 | 2 / 2 | 2 | 25 | set_switch(4); stop |
| 10 | 5 | 60 / 1 | 4 | 30 | trigger_event(6); stop |
| 10 | 6 | 60 / 2 | 4 | 30 | set_switch(5); stop |
| 10 | 7 | 201 / 1 | 1 | 30 | set_switch(6); stop |
| 10 | 8 | 30 / 1 | 3 | 30 | trigger_event(9); stop |
| 10 | 9 | 30 / 2 | 6 | 30 | set_switch(7); stop |
| 10 | 11 | 20 / 1 | 3 | 30 | trigger_event(12); stop |
| 10 | 12 | 20 / 2 | 3 | 30 | trigger_event(13); stop |
| 10 | 13 | 20 / 3 | 4 | 40 | set_switch(11); stop |
| 10 | 14 | 1 / 1 | 3 | 20 | trigger_event(15); stop |
| 10 | 15 | 1 / 2 | 2 | 30 | set_switch(12); construct_objects(room=1,group_or_wave=1); construct_objects(room=30,group_or_wave=1); stop |
| 10 | 16 | 30 / 4 | 1 | 45 | set_switch(13); stop |
| 10 | 17 | 90 / 1 | 3 | 35 | trigger_event(18); stop |
| 10 | 18 | 90 / 2 | 3 | 25 | trigger_event(19); stop |
| 10 | 19 | 90 / 3 | 3 | 25 | trigger_event(20); stop |
| 10 | 20 | 90 / 4 | 2 | 25 | trigger_event(21); stop |
| 10 | 21 | 90 / 5 | 3 | 30 | set_switch(14); construct_objects(room=90,group_or_wave=1); stop |
| 10 | 22 | 61 / 1 | 3 | 35 | trigger_event(23); stop |
| 10 | 23 | 61 / 2 | 3 | 35 | set_switch(15); stop |
| 10 | 24 | 40 / 1 | 2 | 30 | trigger_event(25); stop |
| 10 | 25 | 40 / 2 | 2 | 25 | trigger_event(26); stop |
| 10 | 26 | 40 / 3 | 3 | 25 | set_switch(16); stop |
| 10 | 27 | 62 / 1 | 3 | 30 | trigger_event(28); stop |
| 10 | 28 | 62 / 2 | 3 | 30 | set_switch(17); construct_objects(room=280,group_or_wave=1); stop |
| 10 | 29 | 280 / 1 | 1 | 45 | set_switch(18); construct_objects(room=280,group_or_wave=2); stop |
| 10 | 30 | 62 / 3 | 2 | 30 | set_switch(19); trigger_event(31); stop |
| 10 | 31 | 213 / 1 | 2 | 10 | set_switch(20); stop |
| 10 | 32 | 71 / 1 | 3 | 45 | trigger_event(33); stop |
| 10 | 33 | 71 / 2 | 3 | 25 | trigger_event(34); stop |
| 10 | 34 | 71 / 3 | 3 | 25 | trigger_event(35); stop |
| 10 | 35 | 71 / 4 | 5 | 30 | set_switch(21); stop |
| 10 | 36 | 81 / 1 | 6 | 20 | trigger_event(37); stop |
| 10 | 37 | 81 / 2 | 3 | 25 | set_switch(22); stop |
| 10 | 38 | 81 / 3 | 5 | 40 | trigger_event(39); stop |
| 10 | 39 | 81 / 4 | 3 | 30 | trigger_event(40); stop |
| 10 | 40 | 81 / 5 | 3 | 60 | set_switch(23); trigger_event(41); stop |
| 10 | 41 | 220 / 1 | 1 | 1 | set_switch(24); stop |
| 10 | 42 | 21 / 1 | 5 | 20 | trigger_event(43); stop |
| 10 | 43 | 21 / 2 | 5 | 25 | set_switch(25); stop |
| 10 | 44 | 63 / 1 | 3 | 40 | set_switch(26); construct_objects(room=281,group_or_wave=1); stop |
| 10 | 45 | 281 / 1 | 2 | 20 | trigger_event(46); stop |
| 10 | 46 | 281 / 2 | 2 | 20 | trigger_event(47); stop |
| 10 | 47 | 281 / 3 | 1 | 40 | set_switch(27); set_switch(100); stop |
| 10 | 48 | 7 / 1 | 2 | 30 | set_switch(28); stop |
| 10 | 49 | 64 / 1 | 3 | 30 | trigger_event(50); stop |
| 10 | 50 | 64 / 2 | 5 | 30 | set_switch(29); stop |
| 10 | 51 | 4 / 1 | 3 | 30 | trigger_event(52); stop |
| 10 | 52 | 4 / 2 | 1 | 30 | set_switch(30); trigger_event(53); stop |
| 10 | 53 | 64 / 3 | 4 | 30 | set_switch(31); stop |
| 10 | 54 | 70 / 1 | 3 | 45 | trigger_event(55); stop |
| 10 | 55 | 70 / 2 | 5 | 30 | trigger_event(56); stop |
| 10 | 56 | 70 / 3 | 3 | 35 | set_switch(32); stop |
| 10 | 57 | 265 / 1 | 3 | 15 | set_switch(33); stop |
| 10 | 58 | 3 / 1 | 1 | 40 | trigger_event(59); stop |
| 10 | 59 | 3 / 2 | 3 | 35 | trigger_event(60); stop |
| 10 | 60 | 3 / 3 | 1 | 35 | set_switch(34); stop |
| 10 | 61 | 61 / 3 | 5 | 45 | trigger_event(62); stop |
| 10 | 62 | 61 / 4 | 1 | 35 | set_switch(35); stop |
| 10 | 63 | 221 / 1 | 3 | 1 | set_switch(36); stop |
| 10 | 64 | 80 / 1 | 6 | 20 | trigger_event(65); stop |
| 10 | 65 | 80 / 2 | 4 | 25 | trigger_event(66); stop |
| 10 | 66 | 80 / 3 | 5 | 40 | set_switch(37); stop |
| 10 | 67 | 80 / 4 | 2 | 30 | set_switch(38); set_switch(101); stop |
| 10 | 68 | 211 / 1 | 4 | 5 | set_switch(40); stop |
| 10 | 70 | 263 / 1 | 1 | 40 | set_switch(43); stop |
| 11 | 2 | 210 / 1 | 1 | 1 | set_switch(2); trigger_event(3); stop |
| 11 | 3 | 95 / 1 | 1 | 40 | trigger_event(4); stop |
| 11 | 4 | 95 / 2 | 1 | 35 | trigger_event(5); stop |
| 11 | 5 | 95 / 3 | 2 | 30 | trigger_event(6); stop |
| 11 | 6 | 95 / 4 | 2 | 45 | set_switch(3); stop |
| 11 | 7 | 95 / 5 | 4 | 45 | trigger_event(8); stop |
| 11 | 8 | 95 / 6 | 2 | 40 | trigger_event(9); stop |
| 11 | 9 | 95 / 7 | 4 | 45 | trigger_event(10); stop |
| 11 | 10 | 95 / 8 | 3 | 40 | set_switch(4); stop |
| 11 | 11 | 290 / 1 | 3 | 5 | trigger_event(12); stop |
| 11 | 12 | 290 / 2 | 1 | 60 | set_switch(5); stop |
| 11 | 13 | 1 / 1 | 2 | 10 | trigger_event(14); stop |
| 11 | 14 | 1 / 2 | 3 | 45 | trigger_event(15); stop |
| 11 | 15 | 1 / 3 | 1 | 40 | set_switch(5); construct_objects(room=290,group_or_wave=1); stop |
| 11 | 16 | 290 / 3 | 1 | 50 | trigger_event(90); stop |
| 11 | 90 | 290 / 4 | 1 | 30 | set_switch(5); construct_objects(room=95,group_or_wave=1); stop |
| 11 | 17 | 95 / 9 | 5 | 30 | set_switch(6); stop |
| 11 | 18 | 291 / 1 | 4 | 15 | set_switch(7); stop |
| 11 | 19 | 20 / 1 | 4 | 40 | trigger_event(20); stop |
| 11 | 20 | 20 / 2 | 5 | 40 | trigger_event(21); stop |
| 11 | 21 | 20 / 3 | 4 | 40 | trigger_event(22); stop |
| 11 | 22 | 20 / 4 | 5 | 40 | set_switch(8); stop |
| 11 | 23 | 90 / 1 | 2 | 1 | trigger_event(24); stop |
| 11 | 24 | 90 / 2 | 4 | 30 | set_switch(9); stop |
| 11 | 25 | 90 / 3 | 3 | 30 | trigger_event(26); stop |
| 11 | 26 | 90 / 4 | 3 | 30 | set_switch(10); stop |
| 11 | 27 | 90 / 5 | 1 | 15 | trigger_event(28); stop |
| 11 | 28 | 90 / 6 | 6 | 35 | trigger_event(29); stop |
| 11 | 29 | 90 / 7 | 1 | 30 | set_switch(11); trigger_event(30); stop |
| 11 | 30 | 90 / 8 | 1 | 45 | trigger_event(32); stop |
| 11 | 31 | 90 / 9 | 3 | 40 | set_switch(80); stop |
| 11 | 32 | 90 / 10 | 1 | 30 | set_switch(81); stop |
| 11 | 33 | 30 / 1 | 3 | 30 | trigger_event(34); stop |
| 11 | 34 | 30 / 2 | 1 | 45 | set_switch(13); stop |
| 11 | 35 | 50 / 1 | 4 | 30 | stop |
| 11 | 36 | 50 / 2 | 2 | 45 | trigger_event(37); stop |
| 11 | 37 | 50 / 3 | 3 | 35 | trigger_event(38); stop |
| 11 | 38 | 50 / 4 | 3 | 40 | trigger_event(39); stop |
| 11 | 39 | 50 / 5 | 4 | 35 | set_switch(14); stop |
| 11 | 40 | 6 / 1 | 2 | 30 | trigger_event(41); stop |
| 11 | 41 | 6 / 2 | 1 | 45 | set_switch(15); construct_objects(room=6,group_or_wave=1); stop |
| 11 | 42 | 263 / 1 | 1 | 10 | set_switch(16); trigger_event(43); stop |
| 11 | 43 | 263 / 2 | 2 | 40 | set_switch(17); trigger_event(44); stop |
| 11 | 44 | 233 / 1 | 2 | 30 | set_switch(18); trigger_event(45); stop |
| 11 | 45 | 201 / 1 | 2 | 30 | set_switch(19); stop |
| 11 | 46 | 264 / 1 | 1 | 15 | set_switch(20); stop |
| 11 | 47 | 80 / 1 | 4 | 45 | set_switch(21); trigger_event(48); stop |
| 11 | 48 | 80 / 2 | 7 | 40 | trigger_event(49); stop |
| 11 | 49 | 80 / 3 | 6 | 40 | trigger_event(50); stop |
| 11 | 50 | 80 / 4 | 4 | 40 | set_switch(22); stop |
| 11 | 51 | 215 / 1 | 1 | 30 | set_switch(23); stop |
| 11 | 52 | 70 / 1 | 1 | 45 | trigger_event(54); stop |
| 11 | 53 | 70 / 2 | 1 | 45 | trigger_event(55); stop |
| 11 | 54 | 70 / 3 | 2 | 45 | trigger_event(56); stop |
| 11 | 55 | 70 / 4 | 2 | 45 | trigger_event(57); stop |
| 11 | 56 | 70 / 5 | 1 | 45 | trigger_event(58); stop |
| 11 | 57 | 70 / 6 | 2 | 45 | trigger_event(59); stop |
| 11 | 58 | 70 / 7 | 2 | 45 | trigger_event(60); stop |
| 11 | 59 | 70 / 8 | 2 | 45 | trigger_event(61); stop |
| 11 | 60 | 70 / 9 | 1 | 45 | trigger_event(62); stop |
| 11 | 61 | 70 / 10 | 2 | 45 | trigger_event(63); stop |
| 11 | 62 | 70 / 11 | 2 | 45 | trigger_event(64); stop |
| 11 | 63 | 70 / 12 | 2 | 45 | trigger_event(65); stop |
| 11 | 64 | 70 / 13 | 1 | 45 | trigger_event(66); stop |
| 11 | 65 | 70 / 14 | 4 | 45 | set_switch(55); stop |
| 11 | 66 | 70 / 15 | 2 | 45 | set_switch(56); stop |
| 11 | 67 | 70 / 16 | 3 | 30 | trigger_event(69); stop |
| 11 | 68 | 70 / 17 | 3 | 30 | trigger_event(70); stop |
| 11 | 69 | 70 / 18 | 2 | 30 | trigger_event(71); stop |
| 11 | 70 | 70 / 19 | 2 | 72 | trigger_event(72); stop |
| 11 | 71 | 70 / 20 | 1 | 30 | trigger_event(73); stop |
| 11 | 72 | 70 / 21 | 2 | 30 | trigger_event(74); stop |
| 11 | 73 | 70 / 22 | 4 | 30 | trigger_event(75); stop |
| 11 | 74 | 70 / 23 | 1 | 30 | trigger_event(76); stop |
| 11 | 75 | 70 / 24 | 4 | 30 | trigger_event(77); stop |
| 11 | 76 | 70 / 25 | 2 | 30 | trigger_event(78); stop |
| 11 | 77 | 70 / 26 | 4 | 30 | trigger_event(79); stop |
| 11 | 78 | 70 / 27 | 2 | 30 | trigger_event(80); stop |
| 11 | 79 | 70 / 28 | 3 | 30 | trigger_event(81); stop |
| 11 | 80 | 70 / 29 | 4 | 30 | set_switch(57); stop |
| 11 | 81 | 70 / 30 | 1 | 30 | set_switch(58); stop |
| 11 | 82 | 70 / 31 | 6 | 60 | set_switch(25); construct_objects(room=50,group_or_wave=1); stop |
| 11 | 83 | 280 / 1 | 1 | 45 | set_switch(30); stop |
| 11 | 200 | 5 / 1 | 2 | 30 | trigger_event(201); construct_objects(room=200,group_or_wave=1); stop |
| 11 | 201 | 5 / 2 | 1 | 1 | stop |

## Review notes

- Nonzero data after terminal header
