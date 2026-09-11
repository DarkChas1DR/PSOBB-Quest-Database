# Maximum Attack E -Gal- — maximum-attack-ep2/q40-bb-j

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/maximum-attack-ep2/q40-bb-j.zip?download=1)**

[Original QST](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/maximum-attack-ep2/q40-bb-j.qst?download=1) · [Extracted BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/maximum-attack-ep2/q40-bb-j/q40-bb-j.qst-quest0.bin?download=1) · [Extracted DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/maximum-attack-ep2/q40-bb-j/q40-bb-j.qst-quest0.dat?download=1)

QST is the preserved original package. BIN and DAT are its decoded payload files, not reassembled scripts. The ZIP contains all three formats.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 40; language J. Static scan: **171 objects, 311 enemy/NPC records, 84 events, 54 script labels.** Script roundtrip: byte-identical.

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
| 0 | 41 | 8 | 0 |
| 5 | 26 | 95 | 25 |
| 10 | 48 | 121 | 28 |
| 13 | 27 | 1 | 1 |
| 17 | 29 | 86 | 30 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 5 | 41 | 4 / 1 | 1 | 20 | trigger_event(42); stop |
| 5 | 42 | 4 / 2 | 5 | 20 | trigger_event(43); stop |
| 5 | 43 | 4 / 3 | 5 | 20 | trigger_event(45); stop |
| 5 | 45 | 4 / 5 | 5 | 20 | trigger_event(46); stop |
| 5 | 46 | 4 / 6 | 4 | 20 | trigger_event(47); stop |
| 5 | 47 | 4 / 7 | 3 | 20 | set_switch(2); construct_objects(room=3,group_or_wave=1); stop |
| 5 | 51 | 5 / 1 | 5 | 20 | trigger_event(52); stop |
| 5 | 52 | 5 / 2 | 6 | 20 | trigger_event(53); stop |
| 5 | 53 | 5 / 3 | 5 | 20 | trigger_event(54); stop |
| 5 | 54 | 5 / 4 | 2 | 20 | trigger_event(55); stop |
| 5 | 55 | 5 / 5 | 3 | 20 | trigger_event(56); stop |
| 5 | 56 | 5 / 6 | 2 | 20 | trigger_event(57); stop |
| 5 | 57 | 5 / 7 | 2 | 20 | set_switch(1); stop |
| 5 | 131 | 13 / 1 | 4 | 20 | trigger_event(132); stop |
| 5 | 132 | 13 / 2 | 3 | 20 | trigger_event(133); stop |
| 5 | 133 | 13 / 3 | 4 | 20 | trigger_event(134); stop |
| 5 | 134 | 13 / 4 | 2 | 20 | trigger_event(135); stop |
| 5 | 135 | 13 / 5 | 6 | 20 | trigger_event(136); stop |
| 5 | 136 | 13 / 6 | 6 | 20 | trigger_event(138); stop |
| 5 | 138 | 13 / 8 | 5 | 20 | trigger_event(139); stop |
| 5 | 139 | 13 / 9 | 4 | 20 | trigger_event(1310); stop |
| 5 | 1310 | 13 / 10 | 3 | 20 | trigger_event(1311); stop |
| 5 | 1311 | 13 / 11 | 3 | 20 | trigger_event(1312); stop |
| 5 | 1312 | 13 / 12 | 4 | 20 | trigger_event(1313); stop |
| 5 | 1313 | 13 / 13 | 3 | 20 | set_switch(4); construct_objects(room=13,group_or_wave=1); stop |
| 10 | 201 | 20 / 1 | 5 | 0 | trigger_event(202); stop |
| 10 | 202 | 20 / 2 | 6 | 0 | trigger_event(203); stop |
| 10 | 203 | 20 / 3 | 4 | 20 | trigger_event(204); stop |
| 10 | 204 | 20 / 4 | 4 | 20 | trigger_event(205); stop |
| 10 | 205 | 20 / 5 | 4 | 20 | trigger_event(206); stop |
| 10 | 206 | 20 / 6 | 3 | 90 | set_switch(4); stop |
| 10 | 211 | 21 / 1 | 4 | 20 | trigger_event(212); stop |
| 10 | 212 | 21 / 2 | 2 | 20 | trigger_event(213); stop |
| 10 | 213 | 21 / 3 | 7 | 20 | trigger_event(214); stop |
| 10 | 214 | 21 / 4 | 3 | 20 | trigger_event(215); stop |
| 10 | 215 | 21 / 5 | 1 | 20 | set_switch(2); stop |
| 10 | 611 | 61 / 1 | 5 | 20 | trigger_event(612); stop |
| 10 | 612 | 61 / 2 | 5 | 20 | construct_objects(room=61,group_or_wave=1); stop |
| 10 | 613 | 61 / 3 | 3 | 0 | trigger_event(614); stop |
| 10 | 614 | 61 / 4 | 8 | 20 | set_switch(1); stop |
| 10 | 615 | 61 / 5 | 2 | 20 | stop |
| 10 | 701 | 70 / 1 | 6 | 20 | trigger_event(702); stop |
| 10 | 702 | 70 / 2 | 6 | 20 | trigger_event(703); stop |
| 10 | 703 | 70 / 3 | 5 | 20 | trigger_event(704); stop |
| 10 | 704 | 70 / 4 | 4 | 20 | trigger_event(705); stop |
| 10 | 705 | 70 / 5 | 7 | 20 | trigger_event(706); stop |
| 10 | 706 | 70 / 6 | 6 | 20 | trigger_event(707); stop |
| 10 | 707 | 70 / 7 | 3 | 90 | trigger_event(708); stop |
| 10 | 708 | 70 / 8 | 6 | 20 | trigger_event(709); stop |
| 10 | 709 | 70 / 9 | 4 | 90 | set_switch(5); stop |
| 10 | 7010 | 70 / 10 | 4 | 20 | stop |
| 10 | 2811 | 281 / 1 | 2 | 0 | stop |
| 10 | 2812 | 281 / 2 | 2 | 0 | stop |
| 13 | 1 | 0 / 1 | 1 | 0 | construct_objects(room=1,group_or_wave=1); stop |
| 17 | 11 | 1 / 1 | 2 | 60 | trigger_event(12); stop |
| 17 | 12 | 1 / 2 | 3 | 60 | trigger_event(13); stop |
| 17 | 13 | 1 / 3 | 2 | 60 | trigger_event(14); stop |
| 17 | 14 | 1 / 4 | 2 | 60 | trigger_event(15); stop |
| 17 | 15 | 1 / 5 | 2 | 60 | trigger_event(16); stop |
| 17 | 16 | 1 / 6 | 2 | 60 | set_switch(1); stop |
| 17 | 101 | 10 / 1 | 2 | 60 | trigger_event(102); stop |
| 17 | 102 | 10 / 2 | 2 | 60 | trigger_event(103); stop |
| 17 | 103 | 10 / 3 | 2 | 60 | construct_objects(room=10,group_or_wave=1); stop |
| 17 | 104 | 10 / 4 | 4 | 60 | trigger_event(105); stop |
| 17 | 105 | 10 / 5 | 2 | 60 | trigger_event(106); stop |
| 17 | 106 | 10 / 6 | 4 | 60 | trigger_event(107); stop |
| 17 | 107 | 10 / 7 | 3 | 60 | trigger_event(108); stop |
| 17 | 108 | 10 / 8 | 2 | 60 | set_switch(4); construct_objects(room=10,group_or_wave=2); stop |
| 17 | 201 | 20 / 1 | 2 | 60 | trigger_event(202); stop |
| 17 | 202 | 20 / 2 | 3 | 60 | trigger_event(203); stop |
| 17 | 203 | 20 / 3 | 4 | 60 | trigger_event(204); stop |
| 17 | 204 | 20 / 4 | 4 | 60 | trigger_event(205); stop |
| 17 | 205 | 20 / 5 | 3 | 60 | set_switch(3); stop |
| 17 | 301 | 30 / 1 | 1 | 60 | trigger_event(302); stop |
| 17 | 302 | 30 / 2 | 6 | 60 | trigger_event(303); stop |
| 17 | 303 | 30 / 3 | 3 | 60 | trigger_event(304); stop |
| 17 | 304 | 30 / 4 | 3 | 60 | trigger_event(305); stop |
| 17 | 305 | 30 / 5 | 4 | 60 | trigger_event(307); stop |
| 17 | 307 | 30 / 7 | 2 | 60 | trigger_event(308); stop |
| 17 | 308 | 30 / 8 | 3 | 60 | trigger_event(309); stop |
| 17 | 309 | 30 / 9 | 2 | 90 | trigger_event(3010); stop |
| 17 | 3010 | 30 / 10 | 3 | 60 | trigger_event(3011); stop |
| 17 | 3011 | 30 / 11 | 4 | 60 | trigger_event(3012); stop |
| 17 | 3012 | 30 / 12 | 5 | 60 | construct_objects(room=30,group_or_wave=1); set_switch(5); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
