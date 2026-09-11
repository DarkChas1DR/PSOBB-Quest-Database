# Maximum Attack E -1- — maximum-attack-ep1/q39-bb-e

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/maximum-attack-ep1/q39-bb-e.zip?download=1)**

[Original QST](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/maximum-attack-ep1/q39-bb-e.qst?download=1) · [Extracted BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/maximum-attack-ep1/q39-bb-e/q39-bb-e.qst-quest0.bin?download=1) · [Extracted DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/maximum-attack-ep1/q39-bb-e/q39-bb-e.qst-quest0.dat?download=1)

QST is the preserved original package. BIN and DAT are its decoded payload files, not reassembled scripts. The ZIP contains all three formats.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 39; language E. Static scan: **180 objects, 547 enemy/NPC records, 102 events, 44 script labels.** Script roundtrip: alignment-only.

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
| 0 | 28 | 8 | 0 |
| 2 | 36 | 125 | 21 |
| 4 | 34 | 166 | 29 |
| 6 | 25 | 118 | 26 |
| 10 | 25 | 129 | 25 |
| 14 | 32 | 1 | 1 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 2 | 111 | 11 / 1 | 2 | 20 | trigger_event(112); stop |
| 2 | 112 | 11 / 2 | 9 | 20 | trigger_event(113); stop |
| 2 | 113 | 11 / 3 | 6 | 20 | trigger_event(114); stop |
| 2 | 114 | 11 / 4 | 6 | 20 | trigger_event(115); stop |
| 2 | 115 | 11 / 5 | 8 | 20 | trigger_event(116); stop |
| 2 | 116 | 11 / 6 | 3 | 20 | set_switch(2); stop |
| 2 | 121 | 12 / 1 | 8 | 20 | trigger_event(122); stop |
| 2 | 122 | 12 / 2 | 6 | 20 | trigger_event(123); stop |
| 2 | 123 | 12 / 3 | 6 | 20 | trigger_event(124); stop |
| 2 | 124 | 12 / 4 | 8 | 20 | trigger_event(125); stop |
| 2 | 125 | 12 / 5 | 6 | 20 | trigger_event(126); stop |
| 2 | 126 | 12 / 6 | 3 | 20 | trigger_event(127); stop |
| 2 | 127 | 12 / 7 | 5 | 20 | trigger_event(128); stop |
| 2 | 128 | 12 / 8 | 6 | 20 | trigger_event(129); stop |
| 2 | 129 | 12 / 9 | 2 | 20 | trigger_event(1210); stop |
| 2 | 1210 | 12 / 10 | 4 | 20 | set_switch(4); stop |
| 2 | 131 | 13 / 1 | 8 | 0 | trigger_event(132); stop |
| 2 | 132 | 13 / 2 | 8 | 20 | trigger_event(133); stop |
| 2 | 133 | 13 / 3 | 8 | 20 | trigger_event(134); stop |
| 2 | 134 | 13 / 4 | 6 | 20 | trigger_event(135); stop |
| 2 | 135 | 13 / 5 | 7 | 20 | set_switch(1); stop |
| 4 | 151 | 15 / 1 | 6 | 20 | trigger_event(152); stop |
| 4 | 152 | 15 / 2 | 5 | 20 | trigger_event(153); stop |
| 4 | 153 | 15 / 3 | 6 | 20 | trigger_event(154); stop |
| 4 | 154 | 15 / 4 | 2 | 20 | trigger_event(155); stop |
| 4 | 155 | 15 / 5 | 2 | 20 | trigger_event(156); stop |
| 4 | 156 | 15 / 6 | 7 | 20 | trigger_event(157); stop |
| 4 | 157 | 15 / 7 | 4 | 20 | set_switch(1); stop |
| 4 | 201 | 20 / 1 | 4 | 20 | trigger_event(202); stop |
| 4 | 202 | 20 / 2 | 8 | 20 | trigger_event(203); stop |
| 4 | 203 | 20 / 3 | 8 | 20 | trigger_event(204); stop |
| 4 | 204 | 20 / 4 | 5 | 20 | trigger_event(205); stop |
| 4 | 205 | 20 / 5 | 9 | 20 | set_switch(2); stop |
| 4 | 101 | 10 / 1 | 5 | 20 | trigger_event(102); stop |
| 4 | 102 | 10 / 2 | 5 | 20 | trigger_event(103); stop |
| 4 | 103 | 10 / 3 | 5 | 20 | trigger_event(104); stop |
| 4 | 104 | 10 / 4 | 5 | 20 | set_switch(3); stop |
| 4 | 211 | 21 / 1 | 6 | 20 | trigger_event(212); stop |
| 4 | 212 | 21 / 2 | 8 | 20 | trigger_event(213); stop |
| 4 | 213 | 21 / 3 | 5 | 20 | trigger_event(214); stop |
| 4 | 214 | 21 / 4 | 8 | 20 | set_switch(4); stop |
| 4 | 451 | 45 / 1 | 3 | 20 | trigger_event(452); stop |
| 4 | 452 | 45 / 2 | 4 | 20 | trigger_event(453); stop |
| 4 | 453 | 45 / 3 | 6 | 20 | trigger_event(454); stop |
| 4 | 454 | 45 / 4 | 7 | 20 | trigger_event(455); stop |
| 4 | 455 | 45 / 5 | 2 | 20 | trigger_event(456); stop |
| 4 | 456 | 45 / 6 | 9 | 20 | trigger_event(457); stop |
| 4 | 457 | 45 / 7 | 9 | 20 | trigger_event(458); stop |
| 4 | 458 | 45 / 8 | 7 | 20 | trigger_event(459); stop |
| 4 | 459 | 45 / 9 | 6 | 20 | set_switch(7); construct_objects(room=45,group_or_wave=1); stop |
| 6 | 411 | 41 / 1 | 1 | 20 | trigger_event(412); stop |
| 6 | 412 | 41 / 2 | 4 | 20 | trigger_event(413); stop |
| 6 | 413 | 41 / 3 | 4 | 20 | trigger_event(414); stop |
| 6 | 414 | 41 / 4 | 4 | 20 | trigger_event(415); stop |
| 6 | 415 | 41 / 5 | 4 | 20 | trigger_event(416); stop |
| 6 | 416 | 41 / 6 | 1 | 20 | trigger_event(417); stop |
| 6 | 417 | 41 / 7 | 6 | 20 | trigger_event(418); stop |
| 6 | 418 | 41 / 8 | 4 | 20 | trigger_event(419); stop |
| 6 | 419 | 41 / 9 | 6 | 20 | trigger_event(4110); stop |
| 6 | 4110 | 41 / 10 | 11 | 20 | trigger_event(4111); stop |
| 6 | 4111 | 41 / 11 | 6 | 90 | trigger_event(4112); stop |
| 6 | 4112 | 41 / 12 | 4 | 150 | set_switch(4); stop |
| 6 | 501 | 50 / 1 | 5 | 20 | trigger_event(502); stop |
| 6 | 502 | 50 / 2 | 8 | 20 | trigger_event(503); stop |
| 6 | 503 | 50 / 3 | 1 | 20 | trigger_event(504); stop |
| 6 | 504 | 50 / 4 | 2 | 20 | trigger_event(505); stop |
| 6 | 505 | 50 / 5 | 4 | 20 | trigger_event(506); stop |
| 6 | 506 | 50 / 6 | 3 | 20 | set_switch(1); stop |
| 6 | 531 | 53 / 1 | 9 | 20 | trigger_event(532); stop |
| 6 | 532 | 53 / 2 | 4 | 20 | trigger_event(533); stop |
| 6 | 533 | 53 / 3 | 4 | 20 | trigger_event(534); stop |
| 6 | 534 | 53 / 4 | 2 | 20 | trigger_event(535); stop |
| 6 | 535 | 53 / 5 | 5 | 20 | trigger_event(536); stop |
| 6 | 536 | 53 / 6 | 8 | 20 | trigger_event(537); stop |
| 6 | 537 | 53 / 7 | 5 | 20 | trigger_event(538); stop |
| 6 | 538 | 53 / 8 | 3 | 20 | set_switch(3); stop |
| 10 | 211 | 21 / 1 | 4 | 20 | trigger_event(212); stop |
| 10 | 212 | 21 / 2 | 6 | 20 | trigger_event(213); stop |
| 10 | 213 | 21 / 3 | 2 | 20 | trigger_event(214); stop |
| 10 | 214 | 21 / 4 | 4 | 20 | trigger_event(215); stop |
| 10 | 215 | 21 / 5 | 6 | 20 | trigger_event(216); stop |
| 10 | 216 | 21 / 6 | 5 | 20 | trigger_event(217); stop |
| 10 | 217 | 21 / 7 | 2 | 20 | trigger_event(218); stop |
| 10 | 218 | 21 / 8 | 1 | 0 | set_switch(1); stop |
| 10 | 321 | 32 / 1 | 2 | 20 | trigger_event(322); stop |
| 10 | 322 | 32 / 2 | 6 | 20 | trigger_event(323); stop |
| 10 | 323 | 32 / 3 | 3 | 20 | trigger_event(324); stop |
| 10 | 324 | 32 / 4 | 8 | 20 | trigger_event(325); stop |
| 10 | 325 | 32 / 5 | 6 | 20 | trigger_event(326); stop |
| 10 | 326 | 32 / 6 | 2 | 20 | set_switch(2); stop |
| 10 | 411 | 41 / 1 | 4 | 20 | trigger_event(412); stop |
| 10 | 412 | 41 / 2 | 7 | 20 | trigger_event(413); stop |
| 10 | 413 | 41 / 3 | 9 | 20 | trigger_event(414); stop |
| 10 | 414 | 41 / 4 | 8 | 20 | trigger_event(415); stop |
| 10 | 415 | 41 / 5 | 4 | 20 | trigger_event(416); stop |
| 10 | 416 | 41 / 6 | 7 | 20 | trigger_event(417); stop |
| 10 | 417 | 41 / 7 | 10 | 20 | trigger_event(418); stop |
| 10 | 418 | 41 / 8 | 6 | 20 | trigger_event(419); stop |
| 10 | 419 | 41 / 9 | 8 | 20 | trigger_event(4110); stop |
| 10 | 4110 | 41 / 10 | 5 | 150 | trigger_event(4111); stop |
| 10 | 4111 | 41 / 11 | 4 | 20 | set_switch(4); set_switch(24); stop |
| 14 | 1 | 0 / 1 | 1 | 50 | construct_objects(room=0,group_or_wave=1); construct_objects(room=1,group_or_wave=1); construct_objects(room=2,group_or_wave=1); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
