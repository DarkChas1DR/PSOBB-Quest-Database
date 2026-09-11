# Soul of a Blacksmith — solo-story-ep1/q015-bb-e

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/solo-story-ep1/q015-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/solo-story-ep1/q015-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/solo-story-ep1/q015-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 15; language E. Static scan: **804 objects, 426 enemy/NPC records, 176 events, 75 script labels.** Script roundtrip: byte-identical.

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
0x00, 0x00, 0x00, 0x00, 0x00
0x01, 0x01, 0x00, 0x00, 0x03
0x02, 0x02, 0x00, 0x00, 0x03
0x03, 0x03, 0x00, 0x02, 0x00
0x04, 0x04, 0x00, 0x02, 0x00
0x05, 0x05, 0x00, 0x01, 0x01
0x0B, 0x0B, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 18 | 0 |
| 1 | 104 | 38 | 20 |
| 2 | 126 | 109 | 40 |
| 3 | 190 | 76 | 45 |
| 4 | 169 | 53 | 29 |
| 5 | 169 | 131 | 41 |
| 11 | 20 | 1 | 1 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 111 | 11 / 1 | 2 | 30 | trigger_event(1111); stop |
| 1 | 1111 | 11 / 2 | 4 | 30 | set_switch(4); stop |
| 1 | 71 | 7 / 1 | 2 | 30 | trigger_event(711); stop |
| 1 | 711 | 7 / 2 | 2 | 30 | trigger_event(712); stop |
| 1 | 712 | 7 / 3 | 2 | 30 | set_switch(2); set_switch(3); stop |
| 1 | 41 | 4 / 1 | 1 | 30 | trigger_event(411); stop |
| 1 | 411 | 4 / 2 | 4 | 30 | trigger_event(412); stop |
| 1 | 412 | 4 / 3 | 1 | 30 | trigger_event(413); stop |
| 1 | 413 | 4 / 4 | 2 | 30 | set_switch(9); stop |
| 1 | 81 | 8 / 1 | 1 | 30 | trigger_event(82); stop |
| 1 | 82 | 8 / 2 | 1 | 30 | stop |
| 1 | 21 | 2 / 1 | 1 | 30 | trigger_event(211); stop |
| 1 | 211 | 2 / 2 | 1 | 30 | trigger_event(212); stop |
| 1 | 212 | 2 / 3 | 3 | 30 | set_switch(1); stop |
| 1 | 22 | 2 / 4 | 2 | 30 | stop |
| 1 | 51 | 5 / 1 | 2 | 30 | trigger_event(511); stop |
| 1 | 511 | 5 / 2 | 2 | 30 | trigger_event(512); stop |
| 1 | 512 | 5 / 3 | 2 | 30 | trigger_event(513); stop |
| 1 | 513 | 5 / 4 | 2 | 30 | set_switch(7); set_switch(8); set_switch(6); set_switch(5); stop |
| 1 | 52 | 5 / 5 | 1 | 30 | stop |
| 2 | 11 | 1 / 1 | 3 | 50 | stop |
| 2 | 12 | 1 / 2 | 4 | 20 | set_switch(2); stop |
| 2 | 21 | 2 / 1 | 3 | 80 | trigger_event(211); stop |
| 2 | 211 | 2 / 2 | 3 | 30 | stop |
| 2 | 22 | 2 / 3 | 2 | 50 | trigger_event(221); stop |
| 2 | 221 | 2 / 4 | 2 | 15 | trigger_event(222); stop |
| 2 | 222 | 2 / 5 | 1 | 1 | set_switch(1); stop |
| 2 | 31 | 3 / 1 | 5 | 50 | trigger_event(311); stop |
| 2 | 311 | 3 / 2 | 1 | 1 | trigger_event(312); stop |
| 2 | 312 | 3 / 3 | 3 | 1 | stop |
| 2 | 41 | 4 / 1 | 3 | 50 | trigger_event(411); stop |
| 2 | 411 | 4 / 2 | 4 | 20 | set_switch(31); stop |
| 2 | 61 | 6 / 1 | 2 | 40 | trigger_event(611); stop |
| 2 | 611 | 6 / 2 | 3 | 30 | trigger_event(612); stop |
| 2 | 612 | 6 / 3 | 2 | 30 | stop |
| 2 | 62 | 6 / 4 | 2 | 50 | trigger_event(621); stop |
| 2 | 621 | 6 / 5 | 3 | 30 | trigger_event(622); stop |
| 2 | 622 | 6 / 6 | 2 | 45 | set_switch(3); set_switch(9); stop |
| 2 | 111 | 11 / 1 | 2 | 30 | trigger_event(1111); stop |
| 2 | 1111 | 11 / 2 | 2 | 20 | trigger_event(1112); stop |
| 2 | 1112 | 11 / 3 | 2 | 25 | set_switch(4); set_switch(5); set_switch(6); set_switch(7); stop |
| 2 | 112 | 11 / 4 | 2 | 60 | trigger_event(1121); stop |
| 2 | 1121 | 11 / 5 | 3 | 10 | trigger_event(1122); stop |
| 2 | 1122 | 11 / 6 | 3 | 15 | stop |
| 2 | 113 | 11 / 7 | 3 | 1 | set_switch(4); set_switch(5); set_switch(6); stop |
| 2 | 121 | 12 / 1 | 4 | 1 | trigger_event(1211); stop |
| 2 | 1211 | 12 / 2 | 5 | 1 | trigger_event(1212); stop |
| 2 | 1212 | 12 / 3 | 2 | 30 | set_switch(10); stop |
| 2 | 131 | 13 / 1 | 2 | 1 | trigger_event(1311); stop |
| 2 | 1311 | 13 / 2 | 3 | 15 | trigger_event(1312); stop |
| 2 | 1312 | 13 / 3 | 2 | 15 | trigger_event(1313); stop |
| 2 | 1313 | 13 / 4 | 3 | 30 | stop |
| 2 | 132 | 13 / 5 | 1 | 1 | trigger_event(1321); stop |
| 2 | 1321 | 13 / 6 | 3 | 15 | trigger_event(1322); stop |
| 2 | 1322 | 13 / 7 | 3 | 45 | trigger_event(1323); stop |
| 2 | 1323 | 13 / 8 | 2 | 45 | trigger_event(1324); stop |
| 2 | 1324 | 13 / 9 | 2 | 60 | set_switch(30); stop |
| 2 | 151 | 15 / 1 | 4 | 45 | trigger_event(1511); stop |
| 2 | 1511 | 15 / 2 | 4 | 1 | trigger_event(1512); stop |
| 2 | 1512 | 15 / 3 | 4 | 60 | stop |
| 11 | 1 | 1 / 1 | 1 | 50 | construct_objects(room=1,group_or_wave=1); stop |
| 3 | 101 | 10 / 1 | 2 | 60 | trigger_event(1011); stop |
| 3 | 1011 | 10 / 2 | 2 | 60 | set_switch(8); set_switch(4); stop |
| 3 | 102 | 10 / 3 | 1 | 60 | trigger_event(1021); stop |
| 3 | 1021 | 10 / 4 | 2 | 60 | set_switch(8); stop |
| 3 | 341 | 34 / 1 | 1 | 60 | trigger_event(3411); stop |
| 3 | 3411 | 34 / 2 | 1 | 60 | trigger_event(3412); stop |
| 3 | 3412 | 34 / 3 | 2 | 60 | set_switch(1); set_switch(3); set_switch(7); set_switch(6); stop |
| 3 | 501 | 50 / 1 | 2 | 60 | set_switch(11); set_switch(12); set_switch(16); set_switch(13); set_switch(14); stop |
| 3 | 504 | 50 / 4 | 0 | 60 | stop |
| 3 | 301 | 30 / 1 | 2 | 60 | trigger_event(3011); stop |
| 3 | 3011 | 30 / 2 | 1 | 60 | trigger_event(3012); stop |
| 3 | 3012 | 30 / 3 | 2 | 60 | set_switch(15); stop |
| 3 | 302 | 30 / 4 | 2 | 60 | trigger_event(3021); stop |
| 3 | 3021 | 30 / 5 | 1 | 60 | stop |
| 3 | 601 | 60 / 1 | 1 | 60 | trigger_event(6011); stop |
| 3 | 6011 | 60 / 2 | 1 | 60 | trigger_event(6012); stop |
| 3 | 6012 | 60 / 3 | 1 | 60 | trigger_event(6013); stop |
| 3 | 6013 | 60 / 4 | 1 | 60 | trigger_event(6014); stop |
| 3 | 6014 | 60 / 5 | 1 | 60 | set_switch(17); set_switch(18); stop |
| 3 | 602 | 60 / 6 | 2 | 60 | trigger_event(6021); stop |
| 3 | 6021 | 60 / 7 | 2 | 60 | trigger_event(6022); stop |
| 3 | 6022 | 60 / 8 | 2 | 60 | trigger_event(6023); stop |
| 3 | 6023 | 60 / 9 | 2 | 60 | trigger_event(6024); stop |
| 3 | 6024 | 60 / 10 | 2 | 60 | stop |
| 3 | 111 | 11 / 1 | 1 | 60 | set_switch(19); set_switch(20); set_switch(21); stop |
| 3 | 311 | 31 / 1 | 2 | 60 | set_switch(22); set_switch(23); set_switch(24); set_switch(27); set_switch(28); set_switch(26); stop |
| 3 | 511 | 51 / 1 | 3 | 60 | trigger_event(5111); stop |
| 3 | 5111 | 51 / 2 | 1 | 60 | trigger_event(5112); stop |
| 3 | 5112 | 51 / 3 | 2 | 60 | set_switch(25); set_switch(30); stop |
| 3 | 512 | 51 / 4 | 1 | 60 | trigger_event(5121); stop |
| 3 | 5121 | 51 / 5 | 2 | 60 | trigger_event(5122); stop |
| 3 | 5122 | 51 / 6 | 1 | 60 | stop |
| 3 | 321 | 32 / 1 | 1 | 60 | trigger_event(3211); stop |
| 3 | 3211 | 32 / 2 | 2 | 60 | trigger_event(3212); stop |
| 3 | 3212 | 32 / 3 | 2 | 60 | set_switch(20); set_switch(29); set_switch(28); set_switch(27); set_switch(23); set_switch(24); stop |
| 3 | 521 | 52 / 1 | 3 | 60 | trigger_event(5211); stop |
| 3 | 5211 | 52 / 2 | 2 | 60 | trigger_event(5212); stop |
| 3 | 5212 | 52 / 3 | 3 | 60 | trigger_event(5213); stop |
| 3 | 5213 | 52 / 4 | 3 | 60 | set_switch(31); set_switch(32); set_switch(29); stop |
| 3 | 331 | 33 / 1 | 1 | 60 | trigger_event(3311); stop |
| 3 | 3311 | 33 / 2 | 1 | 60 | trigger_event(3312); stop |
| 3 | 3312 | 33 / 3 | 1 | 60 | set_switch(33); set_switch(34); stop |
| 3 | 332 | 33 / 4 | 2 | 60 | trigger_event(3321); stop |
| 3 | 3321 | 33 / 5 | 2 | 60 | trigger_event(3322); stop |
| 3 | 3322 | 33 / 6 | 1 | 60 | stop |
| 4 | 131 | 13 / 1 | 2 | 10 | set_switch(5); stop |
| 4 | 201 | 20 / 1 | 2 | 10 | trigger_event(2011); stop |
| 4 | 2011 | 20 / 2 | 1 | 10 | trigger_event(2012); stop |
| 4 | 2012 | 20 / 3 | 2 | 10 | set_switch(3); set_switch(2); set_switch(4); set_switch(7); stop |
| 4 | 111 | 11 / 1 | 2 | 10 | set_switch(1); stop |
| 4 | 211 | 21 / 1 | 1 | 10 | trigger_event(2111); stop |
| 4 | 2111 | 21 / 2 | 2 | 10 | trigger_event(2112); stop |
| 4 | 2112 | 21 / 3 | 2 | 10 | set_switch(8); set_switch(9); set_switch(11); set_switch(12); set_switch(10); set_switch(14); stop |
| 4 | 212 | 21 / 4 | 2 | 10 | trigger_event(2121); stop |
| 4 | 2121 | 21 / 5 | 1 | 10 | trigger_event(2122); stop |
| 4 | 2122 | 21 / 6 | 1 | 10 | stop |
| 4 | 221 | 22 / 1 | 1 | 10 | trigger_event(2211); stop |
| 4 | 2211 | 22 / 2 | 1 | 10 | trigger_event(2212); stop |
| 4 | 2212 | 22 / 3 | 2 | 10 | set_switch(13); stop |
| 4 | 451 | 45 / 1 | 3 | 10 | set_switch(17); set_switch(18); set_switch(19); set_switch(22); stop |
| 4 | 452 | 45 / 2 | 1 | 10 | stop |
| 4 | 141 | 14 / 1 | 2 | 10 | trigger_event(1411); stop |
| 4 | 1411 | 14 / 2 | 3 | 10 | set_switch(20); set_switch(21); set_switch(23); set_switch(24); stop |
| 4 | 301 | 30 / 1 | 2 | 10 | set_switch(28); set_switch(29); set_switch(30); set_switch(26); set_switch(27); set_switch(25); set_switch(32); stop |
| 4 | 231 | 23 / 1 | 2 | 10 | trigger_event(2311); stop |
| 4 | 2311 | 23 / 2 | 2 | 10 | set_switch(31); stop |
| 4 | 232 | 23 / 3 | 2 | 10 | stop |
| 4 | 401 | 40 / 1 | 3 | 10 | trigger_event(4011); stop |
| 4 | 4011 | 40 / 2 | 2 | 10 | trigger_event(4012); stop |
| 4 | 4012 | 40 / 3 | 2 | 10 | set_switch(33); set_switch(34); set_switch(35); stop |
| 4 | 402 | 40 / 4 | 1 | 10 | stop |
| 4 | 151 | 15 / 1 | 1 | 10 | trigger_event(1511); stop |
| 4 | 1511 | 15 / 2 | 2 | 10 | trigger_event(1512); stop |
| 4 | 1512 | 15 / 3 | 3 | 10 | set_switch(36); stop |
| 5 | 501 | 50 / 1 | 6 | 30 | trigger_event(5011); stop |
| 5 | 5011 | 50 / 2 | 2 | 30 | trigger_event(5012); stop |
| 5 | 5012 | 50 / 3 | 4 | 30 | set_switch(7); set_switch(8); set_switch(9); set_switch(10); set_switch(12); set_switch(11); set_switch(22); stop |
| 5 | 511 | 51 / 1 | 3 | 30 | trigger_event(5111); stop |
| 5 | 5111 | 51 / 2 | 3 | 30 | trigger_event(5112); stop |
| 5 | 5112 | 51 / 3 | 1 | 30 | trigger_event(5113); stop |
| 5 | 5113 | 51 / 4 | 4 | 30 | set_switch(13); set_switch(14); set_switch(15); stop |
| 5 | 512 | 51 / 5 | 5 | 30 | stop |
| 5 | 211 | 21 / 1 | 2 | 30 | trigger_event(2111); stop |
| 5 | 2111 | 21 / 2 | 3 | 30 | set_switch(16); set_switch(17); stop |
| 5 | 711 | 71 / 1 | 2 | 30 | set_switch(18); set_switch(19); stop |
| 5 | 712 | 71 / 2 | 2 | 30 | stop |
| 5 | 713 | 71 / 3 | 1 | 30 | stop |
| 5 | 7114 | 71 / 4 | 1 | 30 | stop |
| 5 | 541 | 54 / 1 | 5 | 30 | trigger_event(5411); stop |
| 5 | 5411 | 54 / 2 | 3 | 30 | trigger_event(5412); stop |
| 5 | 5412 | 54 / 3 | 4 | 30 | trigger_event(5413); stop |
| 5 | 5413 | 54 / 4 | 5 | 30 | set_switch(20); set_switch(21); set_switch(1); stop |
| 5 | 201 | 20 / 1 | 4 | 30 | trigger_event(2011); stop |
| 5 | 2011 | 20 / 2 | 4 | 40 | trigger_event(2012); stop |
| 5 | 2012 | 20 / 3 | 6 | 30 | set_switch(2); stop |
| 5 | 301 | 30 / 1 | 2 | 30 | trigger_event(3011); stop |
| 5 | 3011 | 30 / 2 | 4 | 30 | trigger_event(3012); stop |
| 5 | 3012 | 30 / 3 | 5 | 1 | construct_objects(room=30,group_or_wave=1); set_switch(3); stop |
| 5 | 302 | 30 / 4 | 5 | 30 | stop |
| 5 | 311 | 31 / 1 | 7 | 30 | trigger_event(3111); stop |
| 5 | 3111 | 31 / 2 | 3 | 30 | trigger_event(3112); stop |
| 5 | 3112 | 31 / 3 | 1 | 30 | set_switch(24); set_switch(27); stop |
| 5 | 602 | 60 / 1 | 5 | 1 | stop |
| 5 | 701 | 70 / 1 | 2 | 30 | set_switch(26); set_switch(32); set_switch(37); set_switch(23); set_switch(25); stop |
| 5 | 702 | 70 / 2 | 2 | 30 | stop |
| 5 | 703 | 70 / 3 | 1 | 30 | stop |
| 5 | 704 | 70 / 4 | 2 | 30 | stop |
| 5 | 531 | 53 / 1 | 3 | 30 | trigger_event(5311); stop |
| 5 | 5311 | 53 / 2 | 3 | 30 | set_switch(33); set_switch(32); set_switch(30); set_switch(38); set_switch(29); set_switch(31); set_switch(34); set_switch(28); stop |
| 5 | 532 | 53 / 3 | 2 | 30 | stop |
| 5 | 533 | 53 / 4 | 2 | 30 | stop |
| 5 | 221 | 22 / 1 | 2 | 30 | set_switch(24); set_switch(27); set_switch(28); set_switch(29); set_switch(30); set_switch(38); set_switch(31); set_switch(34); stop |
| 5 | 321 | 32 / 1 | 3 | 30 | trigger_event(3211); stop |
| 5 | 3211 | 32 / 2 | 4 | 30 | trigger_event(3212); stop |
| 5 | 3212 | 32 / 3 | 3 | 30 | set_switch(35); set_switch(36); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
