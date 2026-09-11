# Scarlet Realm #4 — extermination-ep1/q164-bb-e

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/extermination-ep1/q164-bb-e.zip?download=1)**

[Original QST](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/extermination-ep1/q164-bb-e.qst?download=1) · [Extracted BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/extermination-ep1/q164-bb-e/q164-bb-e.qst-quest0.bin?download=1) · [Extracted DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/extermination-ep1/q164-bb-e/q164-bb-e.qst-quest0.dat?download=1)

QST is the preserved original package. BIN and DAT are its decoded payload files, not reassembled scripts. The ZIP contains all three formats.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 164; language E. Static scan: **469 objects, 385 enemy/NPC records, 124 events, 484 script labels.** Script roundtrip: alignment-only.

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
| 9 | 300 | 215 | 74 |
| 10 | 139 | 161 | 50 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 9 | 2 | 40 / 1 | 4 | 1 | trigger_event(3); stop |
| 9 | 3 | 40 / 2 | 3 | 30 | trigger_event(4); stop |
| 9 | 4 | 40 / 3 | 2 | 30 | set_switch(2); stop |
| 9 | 5 | 31 / 1 | 3 | 30 | trigger_event(6); stop |
| 9 | 6 | 31 / 2 | 3 | 30 | trigger_event(7); stop |
| 9 | 7 | 31 / 3 | 1 | 30 | trigger_event(8); stop |
| 9 | 8 | 31 / 4 | 2 | 30 | set_switch(3); construct_objects(room=31,group_or_wave=1); trigger_event(9); stop |
| 9 | 1000 | 31 / 5 | 0 | 1 | set_switch(1); stop |
| 9 | 1001 | 31 / 6 | 0 | 1 | set_switch(1); stop |
| 9 | 1002 | 31 / 7 | 0 | 1 | set_switch(1); stop |
| 9 | 1003 | 31 / 8 | 0 | 1 | set_switch(1); stop |
| 9 | 9 | 43 / 1 | 3 | 1 | trigger_event(10); stop |
| 9 | 10 | 43 / 2 | 3 | 30 | set_switch(9); stop |
| 9 | 11 | 23 / 1 | 2 | 30 | trigger_event(12); stop |
| 9 | 12 | 23 / 2 | 3 | 30 | trigger_event(13); stop |
| 9 | 13 | 23 / 3 | 3 | 30 | trigger_event(14); stop |
| 9 | 14 | 23 / 4 | 1 | 30 | trigger_event(15); trigger_event(16); stop |
| 9 | 15 | 23 / 5 | 2 | 30 | trigger_event(17); stop |
| 9 | 16 | 23 / 6 | 1 | 30 | trigger_event(18); stop |
| 9 | 17 | 23 / 7 | 1 | 30 | set_switch(10); stop |
| 9 | 18 | 23 / 8 | 2 | 30 | set_switch(11); stop |
| 9 | 19 | 75 / 1 | 2 | 60 | trigger_event(20); stop |
| 9 | 20 | 75 / 2 | 2 | 30 | trigger_event(21); stop |
| 9 | 21 | 75 / 3 | 1 | 30 | trigger_event(1004); trigger_event(1005); trigger_event(1006); trigger_event(1007); trigger_event(1008); stop |
| 9 | 1004 | 75 / 50 | 0 | 1 | set_switch(13); stop |
| 9 | 1005 | 75 / 51 | 0 | 31 | set_switch(14); stop |
| 9 | 1006 | 75 / 52 | 0 | 61 | set_switch(15); stop |
| 9 | 1007 | 75 / 53 | 0 | 91 | set_switch(16); stop |
| 9 | 1008 | 75 / 54 | 0 | 121 | set_switch(17); stop |
| 9 | 22 | 20 / 1 | 4 | 30 | trigger_event(23); stop |
| 9 | 23 | 20 / 2 | 4 | 30 | trigger_event(24); stop |
| 9 | 24 | 20 / 3 | 5 | 30 | set_switch(19); stop |
| 9 | 25 | 55 / 1 | 2 | 25 | trigger_event(26); stop |
| 9 | 26 | 55 / 2 | 2 | 30 | trigger_event(27); stop |
| 9 | 27 | 55 / 3 | 3 | 30 | set_switch(1); construct_objects(room=55,group_or_wave=1); trigger_event(28); stop |
| 9 | 28 | 55 / 4 | 3 | 45 | trigger_event(29); stop |
| 9 | 29 | 55 / 5 | 3 | 30 | set_switch(20); construct_objects(room=8,group_or_wave=1); construct_objects(room=13,group_or_wave=1); trigger_event(30); stop |
| 9 | 30 | 75 / 4 | 5 | 1 | trigger_event(31); stop |
| 9 | 31 | 75 / 5 | 3 | 30 | trigger_event(32); stop |
| 9 | 32 | 75 / 6 | 5 | 30 | trigger_event(33); stop |
| 9 | 33 | 75 / 7 | 4 | 30 | set_switch(21); stop |
| 9 | 34 | 24 / 1 | 2 | 60 | trigger_event(35); stop |
| 9 | 35 | 24 / 2 | 2 | 30 | trigger_event(36); stop |
| 9 | 36 | 24 / 3 | 4 | 30 | trigger_event(37); stop |
| 9 | 37 | 24 / 4 | 2 | 30 | trigger_event(38); stop |
| 9 | 38 | 24 / 5 | 4 | 30 | set_switch(22); stop |
| 9 | 39 | 80 / 1 | 3 | 15 | trigger_event(40); stop |
| 9 | 40 | 80 / 2 | 5 | 30 | trigger_event(41); stop |
| 9 | 41 | 80 / 3 | 3 | 30 | trigger_event(42); stop |
| 9 | 42 | 80 / 4 | 3 | 30 | trigger_event(43); stop |
| 9 | 43 | 80 / 5 | 3 | 30 | trigger_event(44); stop |
| 9 | 44 | 80 / 6 | 3 | 30 | set_switch(23); stop |
| 9 | 45 | 44 / 1 | 6 | 15 | trigger_event(46); stop |
| 9 | 46 | 44 / 2 | 5 | 30 | trigger_event(47); stop |
| 9 | 47 | 44 / 3 | 5 | 30 | set_switch(25); stop |
| 9 | 48 | 22 / 1 | 2 | 30 | trigger_event(49); stop |
| 9 | 49 | 22 / 2 | 4 | 30 | set_switch(26); construct_objects(room=22,group_or_wave=1); stop |
| 9 | 50 | 60 / 1 | 5 | 30 | trigger_event(51); stop |
| 9 | 51 | 60 / 2 | 4 | 30 | construct_objects(room=60,group_or_wave=1); trigger_event(52); stop |
| 9 | 52 | 60 / 3 | 6 | 30 | set_switch(29); construct_objects(room=60,group_or_wave=2); stop |
| 9 | 53 | 33 / 1 | 4 | 75 | trigger_event(54); stop |
| 9 | 54 | 33 / 2 | 4 | 30 | trigger_event(55); stop |
| 9 | 55 | 33 / 3 | 4 | 30 | set_switch(30); stop |
| 9 | 56 | 42 / 1 | 4 | 40 | construct_objects(room=42,group_or_wave=1); stop |
| 9 | 57 | 42 / 2 | 5 | 1 | trigger_event(58); stop |
| 9 | 58 | 42 / 3 | 6 | 30 | trigger_event(59); stop |
| 9 | 59 | 42 / 4 | 4 | 30 | set_switch(32); construct_objects(room=80,group_or_wave=1); stop |
| 9 | 60 | 80 / 7 | 6 | 1 | trigger_event(61); stop |
| 9 | 61 | 80 / 8 | 3 | 30 | trigger_event(62); stop |
| 9 | 62 | 80 / 9 | 7 | 30 | trigger_event(63); stop |
| 9 | 63 | 80 / 10 | 5 | 30 | trigger_event(64); stop |
| 9 | 64 | 80 / 11 | 2 | 1 | set_switch(33); stop |
| 9 | 65 | 7 / 0 | 0 | 1 | construct_objects(room=7,group_or_wave=1); construct_objects(room=60,group_or_wave=1); stop |
| 9 | 66 | 41 / 1 | 3 | 30 | set_switch(39); stop |
| 10 | 1 | 40 / 1 | 1 | 1 | trigger_event(2); stop |
| 10 | 2 | 40 / 2 | 5 | 40 | trigger_event(3); stop |
| 10 | 3 | 40 / 3 | 3 | 60 | set_switch(1); stop |
| 10 | 4 | 70 / 1 | 3 | 30 | trigger_event(5); stop |
| 10 | 5 | 70 / 2 | 3 | 30 | trigger_event(6); stop |
| 10 | 6 | 70 / 3 | 3 | 30 | trigger_event(7); stop |
| 10 | 7 | 70 / 4 | 2 | 30 | trigger_event(8); stop |
| 10 | 8 | 70 / 5 | 5 | 30 | trigger_event(9); stop |
| 10 | 9 | 70 / 6 | 3 | 30 | trigger_event(10); stop |
| 10 | 10 | 70 / 7 | 4 | 30 | trigger_event(11); stop |
| 10 | 11 | 70 / 8 | 2 | 30 | trigger_event(12); stop |
| 10 | 12 | 70 / 9 | 4 | 30 | set_switch(2); stop |
| 10 | 13 | 22 / 1 | 2 | 10 | trigger_event(14); stop |
| 10 | 14 | 22 / 2 | 5 | 30 | trigger_event(15); stop |
| 10 | 15 | 22 / 3 | 4 | 30 | trigger_event(16); stop |
| 10 | 16 | 22 / 4 | 4 | 30 | trigger_event(17); stop |
| 10 | 17 | 22 / 5 | 0 | 30 | set_switch(3); stop |
| 10 | 18 | 80 / 1 | 4 | 50 | trigger_event(19); stop |
| 10 | 19 | 80 / 2 | 5 | 30 | trigger_event(20); stop |
| 10 | 20 | 80 / 3 | 5 | 30 | trigger_event(21); stop |
| 10 | 21 | 80 / 4 | 3 | 60 | set_switch(4); stop |
| 10 | 22 | 20 / 1 | 5 | 30 | trigger_event(23); stop |
| 10 | 23 | 20 / 2 | 4 | 1 | trigger_event(24); stop |
| 10 | 24 | 20 / 3 | 3 | 30 | set_switch(5); stop |
| 10 | 25 | 80 / 5 | 5 | 30 | trigger_event(26); stop |
| 10 | 26 | 80 / 6 | 7 | 30 | set_switch(7); stop |
| 10 | 27 | 21 / 1 | 2 | 30 | trigger_event(28); stop |
| 10 | 28 | 21 / 2 | 2 | 30 | trigger_event(29); stop |
| 10 | 29 | 21 / 3 | 2 | 30 | trigger_event(30); stop |
| 10 | 30 | 21 / 4 | 2 | 30 | set_switch(8); stop |
| 10 | 31 | 80 / 0 | 0 | 1 | set_switch(9); stop |
| 10 | 32 | 85 / 0 | 0 | 1 | trigger_event(33); trigger_event(34); stop |
| 10 | 33 | 85 / 1 | 3 | 15 | trigger_event(35); stop |
| 10 | 34 | 85 / 2 | 3 | 30 | trigger_event(36); stop |
| 10 | 35 | 85 / 3 | 3 | 30 | trigger_event(37); stop |
| 10 | 36 | 85 / 4 | 2 | 30 | trigger_event(38); stop |
| 10 | 37 | 85 / 5 | 4 | 30 | trigger_event(39); stop |
| 10 | 38 | 85 / 6 | 1 | 30 | trigger_event(40); stop |
| 10 | 39 | 85 / 7 | 2 | 30 | trigger_event(41); stop |
| 10 | 40 | 85 / 8 | 1 | 30 | trigger_event(42); stop |
| 10 | 41 | 85 / 9 | 1 | 30 | set_switch(12); stop |
| 10 | 42 | 85 / 10 | 2 | 30 | set_switch(13); stop |
| 10 | 43 | 85 / 11 | 5 | 30 | trigger_event(44); stop |
| 10 | 44 | 85 / 12 | 6 | 1 | trigger_event(45); stop |
| 10 | 45 | 85 / 13 | 5 | 30 | trigger_event(46); stop |
| 10 | 46 | 85 / 14 | 3 | 30 | trigger_event(47); stop |
| 10 | 47 | 85 / 15 | 5 | 30 | trigger_event(48); stop |
| 10 | 48 | 85 / 16 | 5 | 30 | trigger_event(49); stop |
| 10 | 49 | 85 / 17 | 4 | 30 | trigger_event(50); stop |
| 10 | 50 | 85 / 18 | 4 | 30 | set_switch(14); stop |

## Review notes

- Nonzero data after terminal header
