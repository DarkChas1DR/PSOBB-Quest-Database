# Land of Lily — extermination-ep1/q53-bb-e

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/extermination-ep1/q53-bb-e.zip?download=1)**

[Original QST](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/extermination-ep1/q53-bb-e.qst?download=1) · [Extracted BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/extermination-ep1/q53-bb-e/q53-bb-e.qst-quest0.bin?download=1) · [Extracted DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/extermination-ep1/q53-bb-e/q53-bb-e.qst-quest0.dat?download=1)

QST is the preserved original package. BIN and DAT are its decoded payload files, not reassembled scripts. The ZIP contains all three formats.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 53; language E. Static scan: **313 objects, 312 enemy/NPC records, 74 events, 40 script labels.** Script roundtrip: alignment-only.

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
| 0 | 26 | 25 | 0 |
| 3 | 160 | 154 | 33 |
| 4 | 127 | 133 | 41 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 3 | 521 | 52 / 1 | 4 | 1 | trigger_event(5211); stop |
| 3 | 5211 | 52 / 2 | 4 | 1 | trigger_event(5212); stop |
| 3 | 5212 | 52 / 3 | 1 | 1 | trigger_event(5213); stop |
| 3 | 5213 | 52 / 4 | 6 | 1 | set_switch(21); stop |
| 3 | 311 | 20 / 1 | 3 | 1 | trigger_event(2011); stop |
| 3 | 2011 | 20 / 2 | 3 | 1 | set_switch(19); stop |
| 3 | 511 | 51 / 1 | 5 | 1 | trigger_event(5111); stop |
| 3 | 5111 | 51 / 2 | 1 | 1 | trigger_event(5112); stop |
| 3 | 5112 | 51 / 3 | 4 | 1 | trigger_event(5113); stop |
| 3 | 5113 | 51 / 4 | 4 | 1 | trigger_event(5114); stop |
| 3 | 5114 | 51 / 5 | 6 | 1 | set_switch(16); set_switch(17); set_switch(15); set_switch(18); set_switch(14); set_switch(13); stop |
| 3 | 331 | 33 / 1 | 3 | 1 | trigger_event(3311); stop |
| 3 | 3311 | 33 / 2 | 6 | 1 | stop |
| 3 | 601 | 60 / 1 | 5 | 1 | trigger_event(6011); stop |
| 3 | 6011 | 60 / 2 | 6 | 1 | trigger_event(6012); stop |
| 3 | 6012 | 60 / 3 | 5 | 1 | trigger_event(6013); stop |
| 3 | 6013 | 60 / 4 | 6 | 1 | set_switch(11); set_switch(12); set_switch(8); set_switch(9); stop |
| 3 | 531 | 53 / 1 | 6 | 1 | trigger_event(5311); stop |
| 3 | 5311 | 53 / 2 | 4 | 1 | trigger_event(5312); stop |
| 3 | 5312 | 53 / 3 | 6 | 1 | trigger_event(5313); stop |
| 3 | 5313 | 53 / 4 | 5 | 1 | set_switch(10); set_switch(6); stop |
| 3 | 101 | 10 / 1 | 4 | 1 | trigger_event(1011); stop |
| 3 | 1011 | 10 / 2 | 4 | 1 | set_switch(7); set_switch(8); set_switch(4); stop |
| 3 | 341 | 34 / 1 | 4 | 1 | trigger_event(3411); stop |
| 3 | 3411 | 34 / 2 | 8 | 1 | trigger_event(3412); stop |
| 3 | 3412 | 34 / 3 | 6 | 1 | set_switch(4); set_switch(5); set_switch(7); stop |
| 3 | 501 | 50 / 1 | 4 | 1 | set_switch(2); set_switch(3); stop |
| 3 | 502 | 50 / 2 | 5 | 1 | trigger_event(5021); stop |
| 3 | 5021 | 50 / 3 | 6 | 1 | trigger_event(5022); stop |
| 3 | 5022 | 50 / 4 | 5 | 1 | set_switch(1); stop |
| 3 | 321 | 32 / 1 | 5 | 1 | trigger_event(3211); stop |
| 3 | 3211 | 32 / 2 | 5 | 1 | trigger_event(3212); stop |
| 3 | 3212 | 32 / 3 | 5 | 1 | set_switch(27); stop |
| 4 | 141 | 14 / 1 | 3 | 10 | trigger_event(1411); stop |
| 4 | 1411 | 14 / 2 | 3 | 10 | trigger_event(1412); stop |
| 4 | 1412 | 14 / 3 | 3 | 10 | trigger_event(1413); stop |
| 4 | 1413 | 14 / 4 | 3 | 10 | stop |
| 4 | 142 | 14 / 5 | 3 | 10 | trigger_event(1421); stop |
| 4 | 1421 | 14 / 6 | 1 | 10 | trigger_event(1422); stop |
| 4 | 1422 | 14 / 7 | 4 | 10 | trigger_event(1423); stop |
| 4 | 1423 | 14 / 8 | 2 | 10 | set_switch(33); stop |
| 4 | 231 | 23 / 1 | 5 | 10 | trigger_event(2311); stop |
| 4 | 2311 | 23 / 2 | 5 | 10 | set_switch(32); set_switch(31); stop |
| 4 | 302 | 30 / 1 | 4 | 10 | set_switch(25); set_switch(30); set_switch(27); set_switch(24); stop |
| 4 | 303 | 30 / 2 | 5 | 10 | stop |
| 4 | 351 | 35 / 1 | 4 | 10 | trigger_event(3511); stop |
| 4 | 3511 | 35 / 2 | 4 | 10 | set_switch(26); set_switch(28); stop |
| 4 | 352 | 35 / 3 | 3 | 10 | stop |
| 4 | 402 | 40 / 1 | 3 | 30 | trigger_event(4021); stop |
| 4 | 4021 | 40 / 2 | 4 | 30 | set_switch(22); set_switch(23); set_switch(17); set_switch(18); set_switch(21); set_switch(35); set_switch(20); set_switch(19); set_switch(15); stop |
| 4 | 122 | 12 / 1 | 4 | 10 | trigger_event(1221); stop |
| 4 | 1221 | 12 / 2 | 5 | 10 | set_switch(29); stop |
| 4 | 131 | 13 / 1 | 5 | 10 | set_switch(20); set_switch(19); set_switch(15); stop |
| 4 | 132 | 13 / 2 | 4 | 10 | stop |
| 4 | 111 | 11 / 1 | 3 | 10 | trigger_event(1111); stop |
| 4 | 1111 | 11 / 2 | 3 | 10 | trigger_event(1112); stop |
| 4 | 1112 | 11 / 3 | 3 | 10 | trigger_event(1113); stop |
| 4 | 1113 | 11 / 4 | 1 | 10 | trigger_event(1114); stop |
| 4 | 1114 | 11 / 5 | 3 | 10 | trigger_event(1115); stop |
| 4 | 1115 | 11 / 6 | 3 | 10 | trigger_event(1116); stop |
| 4 | 1116 | 11 / 7 | 4 | 10 | trigger_event(1117); stop |
| 4 | 1117 | 11 / 8 | 2 | 10 | trigger_event(1118); stop |
| 4 | 1118 | 11 / 9 | 2 | 10 | trigger_event(1119); stop |
| 4 | 1119 | 11 / 10 | 3 | 10 | stop |
| 4 | 112 | 11 / 11 | 4 | 10 | trigger_event(1121); stop |
| 4 | 1121 | 11 / 12 | 4 | 10 | trigger_event(1122); stop |
| 4 | 1122 | 11 / 13 | 2 | 10 | trigger_event(1123); stop |
| 4 | 1123 | 11 / 14 | 3 | 10 | trigger_event(1124); stop |
| 4 | 1124 | 11 / 15 | 4 | 10 | trigger_event(1125); stop |
| 4 | 1125 | 11 / 16 | 2 | 10 | trigger_event(1126); stop |
| 4 | 1126 | 11 / 17 | 1 | 10 | trigger_event(1127); stop |
| 4 | 1127 | 11 / 18 | 4 | 10 | trigger_event(1128); stop |
| 4 | 1128 | 11 / 19 | 2 | 10 | trigger_event(1129); stop |
| 4 | 1129 | 11 / 20 | 3 | 10 | set_switch(12); set_switch(11); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
