# Forsaken Friends — events-ep1/q66-bb-j

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/events-ep1/q66-bb-j.zip?download=1)**

[Original QST](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/events-ep1/q66-bb-j.qst?download=1) · [Extracted BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/events-ep1/q66-bb-j/q66-bb-j.qst-quest0.bin?download=1) · [Extracted DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/events-ep1/q66-bb-j/q66-bb-j.qst-quest0.dat?download=1)

QST is the preserved original package. BIN and DAT are its decoded payload files, not reassembled scripts. The ZIP contains all three formats.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 66; language J. Static scan: **408 objects, 678 enemy/NPC records, 116 events, 77 script labels.** Script roundtrip: byte-identical.

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
| 0 | 19 | 10 | 0 |
| 7 | 102 | 140 | 32 |
| 8 | 28 | 5 | 1 |
| 9 | 51 | 226 | 27 |
| 10 | 173 | 296 | 55 |
| 14 | 35 | 1 | 1 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 7 | 11 | 20 / 1 | 4 | 1 | trigger_event(12); stop |
| 7 | 12 | 20 / 2 | 5 | 25 | trigger_event(13); stop |
| 7 | 13 | 20 / 3 | 1 | 60 | set_switch(1); stop |
| 7 | 21 | 51 / 1 | 9 | 80 | trigger_event(22); stop |
| 7 | 22 | 51 / 2 | 1 | 15 | trigger_event(23); stop |
| 7 | 23 | 51 / 3 | 7 | 30 | set_switch(2); stop |
| 7 | 31 | 61 / 1 | 8 | 10 | trigger_event(32); stop |
| 7 | 32 | 61 / 2 | 10 | 20 | trigger_event(33); stop |
| 7 | 33 | 61 / 3 | 1 | 40 | trigger_event(34); stop |
| 7 | 34 | 61 / 4 | 1 | 1 | trigger_event(35); stop |
| 7 | 35 | 61 / 5 | 2 | 1 | set_switch(3); stop |
| 7 | 41 | 53 / 1 | 9 | 1 | trigger_event(42); stop |
| 7 | 42 | 53 / 2 | 8 | 10 | trigger_event(43); stop |
| 7 | 43 | 53 / 3 | 2 | 25 | trigger_event(44); stop |
| 7 | 44 | 53 / 4 | 4 | 25 | set_switch(4); stop |
| 7 | 51 | 80 / 1 | 7 | 10 | set_switch(0); stop |
| 7 | 52 | 80 / 2 | 3 | 10 | set_switch(0); stop |
| 7 | 53 | 80 / 3 | 9 | 10 | set_switch(5); stop |
| 7 | 61 | 30 / 1 | 2 | 1 | trigger_event(62); stop |
| 7 | 62 | 30 / 2 | 4 | 20 | trigger_event(63); stop |
| 7 | 63 | 30 / 3 | 1 | 20 | trigger_event(64); stop |
| 7 | 64 | 30 / 4 | 1 | 20 | set_switch(6); stop |
| 7 | 71 | 60 / 1 | 1 | 1 | trigger_event(72); stop |
| 7 | 72 | 60 / 2 | 9 | 30 | trigger_event(73); stop |
| 7 | 73 | 60 / 3 | 5 | 30 | trigger_event(74); stop |
| 7 | 74 | 60 / 4 | 4 | 40 | set_switch(7); stop |
| 7 | 81 | 50 / 1 | 2 | 100 | trigger_event(82); stop |
| 7 | 82 | 50 / 2 | 4 | 20 | trigger_event(83); stop |
| 7 | 83 | 50 / 3 | 5 | 40 | set_switch(8); stop |
| 7 | 91 | 220 / 1 | 1 | 1 | set_switch(9); stop |
| 7 | 36 | 21 / 1 | 4 | 300 | trigger_event(37); stop |
| 7 | 37 | 21 / 2 | 5 | 50 | set_switch(3); construct_objects(room=21,group_or_wave=1); stop |
| 8 | 11 | 10 / 1 | 5 | 1 | set_switch(11); stop |
| 9 | 11 | 40 / 1 | 6 | 30 | trigger_event(12); stop |
| 9 | 12 | 40 / 2 | 4 | 10 | trigger_event(13); stop |
| 9 | 13 | 40 / 3 | 11 | 10 | set_switch(1); set_switch(10); set_switch(11); stop |
| 9 | 21 | 20 / 1 | 5 | 1 | trigger_event(22); stop |
| 9 | 22 | 20 / 2 | 4 | 20 | trigger_event(23); stop |
| 9 | 23 | 20 / 3 | 4 | 20 | trigger_event(24); stop |
| 9 | 24 | 20 / 4 | 1 | 30 | trigger_event(25); stop |
| 9 | 25 | 20 / 5 | 2 | 20 | set_switch(2); stop |
| 9 | 31 | 31 / 1 | 5 | 1 | trigger_event(32); stop |
| 9 | 32 | 31 / 2 | 5 | 20 | trigger_event(33); stop |
| 9 | 33 | 31 / 3 | 6 | 20 | trigger_event(34); stop |
| 9 | 34 | 31 / 4 | 4 | 20 | trigger_event(35); stop |
| 9 | 35 | 31 / 5 | 8 | 30 | set_switch(3); stop |
| 9 | 41 | 20 / 6 | 6 | 1 | trigger_event(42); stop |
| 9 | 42 | 20 / 7 | 7 | 50 | set_switch(10); stop |
| 9 | 51 | 31 / 6 | 12 | 1 | trigger_event(52); stop |
| 9 | 52 | 31 / 7 | 8 | 50 | set_switch(11); stop |
| 9 | 61 | 80 / 1 | 9 | 70 | trigger_event(62); stop |
| 9 | 62 | 80 / 2 | 10 | 10 | trigger_event(63); stop |
| 9 | 63 | 80 / 3 | 15 | 10 | trigger_event(64); stop |
| 9 | 64 | 80 / 4 | 24 | 40 | trigger_event(65); stop |
| 9 | 65 | 80 / 5 | 13 | 20 | trigger_event(66); stop |
| 9 | 66 | 80 / 6 | 8 | 10 | trigger_event(67); trigger_event(68); stop |
| 9 | 67 | 80 / 7 | 6 | 10 | stop |
| 9 | 68 | 80 / 8 | 6 | 70 | trigger_event(69); stop |
| 9 | 69 | 80 / 9 | 12 | 50 | trigger_event(70); stop |
| 9 | 70 | 80 / 10 | 25 | 1 | set_switch(4); stop |
| 10 | 11 | 40 / 1 | 5 | 50 | trigger_event(12); stop |
| 10 | 12 | 40 / 2 | 3 | 10 | trigger_event(13); stop |
| 10 | 13 | 40 / 3 | 3 | 30 | set_switch(1); stop |
| 10 | 21 | 30 / 1 | 9 | 1 | trigger_event(22); stop |
| 10 | 22 | 30 / 2 | 3 | 10 | trigger_event(23); stop |
| 10 | 23 | 30 / 3 | 6 | 30 | trigger_event(24); stop |
| 10 | 24 | 30 / 4 | 7 | 10 | trigger_event(25); stop |
| 10 | 25 | 30 / 5 | 0 | 20 | set_switch(2); stop |
| 10 | 31 | 43 / 1 | 4 | 1 | trigger_event(32); stop |
| 10 | 32 | 43 / 2 | 11 | 10 | trigger_event(33); stop |
| 10 | 33 | 43 / 3 | 8 | 20 | trigger_event(34); stop |
| 10 | 34 | 43 / 4 | 7 | 10 | set_switch(3); stop |
| 10 | 41 | 22 / 1 | 5 | 1 | trigger_event(42); stop |
| 10 | 42 | 22 / 2 | 5 | 10 | trigger_event(43); stop |
| 10 | 43 | 22 / 3 | 4 | 40 | set_switch(4); stop |
| 10 | 51 | 60 / 1 | 6 | 1 | set_switch(5); stop |
| 10 | 61 | 32 / 1 | 6 | 1 | trigger_event(62); stop |
| 10 | 62 | 32 / 2 | 11 | 40 | set_switch(6); stop |
| 10 | 71 | 75 / 1 | 6 | 1 | trigger_event(72); stop |
| 10 | 72 | 75 / 2 | 7 | 60 | trigger_event(73); stop |
| 10 | 73 | 75 / 3 | 3 | 20 | set_switch(7); construct_objects(room=75,group_or_wave=1); stop |
| 10 | 81 | 21 / 1 | 1 | 1 | trigger_event(82); stop |
| 10 | 82 | 21 / 2 | 2 | 10 | trigger_event(83); stop |
| 10 | 83 | 21 / 3 | 12 | 50 | trigger_event(84); stop |
| 10 | 84 | 21 / 4 | 8 | 30 | set_switch(8); stop |
| 10 | 52 | 60 / 2 | 8 | 1 | set_switch(9); stop |
| 10 | 91 | 44 / 1 | 1 | 1 | set_switch(10); construct_objects(room=75,group_or_wave=2); stop |
| 10 | 101 | 85 / 1 | 8 | 1 | set_switch(10); stop |
| 10 | 92 | 44 / 2 | 10 | 20 | trigger_event(93); stop |
| 10 | 93 | 44 / 3 | 7 | 10 | set_switch(9); set_switch(11); stop |
| 10 | 85 | 21 / 5 | 8 | 1 | set_switch(7); stop |
| 10 | 102 | 50 / 1 | 5 | 1 | trigger_event(103); stop |
| 10 | 103 | 50 / 2 | 4 | 30 | set_switch(5); stop |
| 10 | 104 | 42 / 1 | 8 | 100 | trigger_event(105); stop |
| 10 | 105 | 42 / 2 | 4 | 1 | set_switch(12); stop |
| 10 | 106 | 31 / 1 | 8 | 1 | trigger_event(107); stop |
| 10 | 107 | 31 / 2 | 3 | 1 | trigger_event(108); stop |
| 10 | 108 | 31 / 3 | 4 | 1 | set_switch(13); stop |
| 10 | 109 | 41 / 1 | 4 | 1 | trigger_event(110); stop |
| 10 | 110 | 41 / 2 | 12 | 70 | trigger_event(111); stop |
| 10 | 111 | 41 / 3 | 4 | 1 | set_switch(14); stop |
| 10 | 120 | 80 / 1 | 4 | 1 | trigger_event(121); stop |
| 10 | 121 | 80 / 2 | 4 | 50 | trigger_event(122); stop |
| 10 | 122 | 80 / 3 | 4 | 50 | trigger_event(123); stop |
| 10 | 123 | 80 / 4 | 6 | 50 | trigger_event(124); set_switch(21); stop |
| 10 | 124 | 80 / 5 | 4 | 120 | trigger_event(125); stop |
| 10 | 125 | 80 / 6 | 5 | 50 | trigger_event(126); stop |
| 10 | 126 | 80 / 7 | 4 | 50 | trigger_event(127); set_switch(22); stop |
| 10 | 127 | 80 / 8 | 3 | 120 | trigger_event(128); stop |
| 10 | 128 | 80 / 9 | 3 | 50 | trigger_event(129); stop |
| 10 | 129 | 80 / 10 | 4 | 50 | set_switch(0); construct_objects(room=80,group_or_wave=1); stop |
| 10 | 130 | 80 / 11 | 3 | 1 | stop |
| 10 | 131 | 80 / 12 | 4 | 70 | stop |
| 10 | 132 | 80 / 13 | 4 | 140 | stop |
| 10 | 150 | 60 / 3 | 3 | 1 | set_switch(4); stop |
| 14 | 1 | 0 / 1 | 1 | 50 | construct_objects(room=0,group_or_wave=1); construct_objects(room=1,group_or_wave=1); construct_objects(room=2,group_or_wave=1); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
