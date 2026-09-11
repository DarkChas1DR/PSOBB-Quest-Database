# EP1 Quest v1.4 — events-ep1/q113-bb-j

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/events-ep1/q113-bb-j.zip?download=1)**

[Original QST](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/events-ep1/q113-bb-j.qst?download=1) · [Extracted BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/events-ep1/q113-bb-j/q113-bb-j.qst-quest0.bin?download=1) · [Extracted DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/events-ep1/q113-bb-j/q113-bb-j.qst-quest0.dat?download=1)

QST is the preserved original package. BIN and DAT are its decoded payload files, not reassembled scripts. The ZIP contains all three formats.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 113; language J. Static scan: **1105 objects, 855 enemy/NPC records, 169 events, 39 script labels.** Script roundtrip: alignment-only.

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
| 0 | 26 | 23 | 0 |
| 4 | 151 | 224 | 29 |
| 5 | 178 | 110 | 40 |
| 6 | 160 | 130 | 17 |
| 7 | 176 | 49 | 39 |
| 9 | 369 | 316 | 43 |
| 12 | 16 | 1 | 1 |
| 13 | 29 | 2 | 0 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 4 | 141 | 14 / 1 | 7 | 60 | trigger_event(1411); stop |
| 4 | 1411 | 14 / 2 | 3 | 60 | set_switch(33); stop |
| 4 | 231 | 23 / 1 | 5 | 60 | trigger_event(2311); stop |
| 4 | 2311 | 23 / 2 | 10 | 60 | set_switch(32); set_switch(31); stop |
| 4 | 302 | 30 / 1 | 7 | 60 | set_switch(25); set_switch(30); set_switch(27); set_switch(24); stop |
| 4 | 303 | 30 / 2 | 10 | 60 | stop |
| 4 | 351 | 35 / 1 | 5 | 60 | set_switch(26); set_switch(28); stop |
| 4 | 352 | 35 / 2 | 0 | 60 | stop |
| 4 | 402 | 40 / 1 | 0 | 60 | set_switch(22); set_switch(23); set_switch(17); set_switch(18); set_switch(21); set_switch(35); set_switch(20); set_switch(19); set_switch(15); stop |
| 4 | 121 | 12 / 1 | 14 | 60 | stop |
| 4 | 122 | 12 / 2 | 1 | 60 | trigger_event(1221); stop |
| 4 | 1221 | 12 / 3 | 8 | 60 | set_switch(29); stop |
| 4 | 131 | 13 / 1 | 15 | 60 | set_switch(20); set_switch(19); set_switch(15); stop |
| 4 | 132 | 13 / 2 | 6 | 60 | stop |
| 4 | 601 | 60 / 1 | 6 | 60 | trigger_event(6011); stop |
| 4 | 6011 | 60 / 2 | 2 | 60 | trigger_event(6012); stop |
| 4 | 6012 | 60 / 3 | 17 | 60 | set_switch(13); set_switch(14); stop |
| 4 | 111 | 11 / 1 | 4 | 60 | trigger_event(1111); stop |
| 4 | 1111 | 11 / 2 | 13 | 60 | set_switch(12); stop |
| 4 | 211 | 21 / 1 | 6 | 60 | trigger_event(2111); stop |
| 4 | 2111 | 21 / 2 | 13 | 60 | trigger_event(2112); stop |
| 4 | 2112 | 21 / 3 | 3 | 60 | set_switch(6); set_switch(5); set_switch(9); set_switch(4); set_switch(7); set_switch(3); stop |
| 4 | 161 | 16 / 1 | 22 | 60 | trigger_event(1611); stop |
| 4 | 1611 | 16 / 2 | 6 | 60 | set_switch(10); stop |
| 4 | 221 | 22 / 1 | 8 | 60 | set_switch(8); stop |
| 4 | 201 | 20 / 1 | 13 | 60 | trigger_event(2011); stop |
| 4 | 2011 | 20 / 2 | 1 | 60 | trigger_event(2012); stop |
| 4 | 2012 | 20 / 3 | 14 | 60 | set_switch(2); stop |
| 4 | 151 | 15 / 1 | 5 | 60 | set_switch(1); stop |
| 5 | 301 | 30 / 1 | 1 | 10 | stop |
| 5 | 302 | 30 / 2 | 1 | 10 | trigger_event(3021); stop |
| 5 | 3021 | 30 / 3 | 3 | 10 | trigger_event(3022); stop |
| 5 | 3022 | 30 / 4 | 2 | 10 | stop |
| 5 | 303 | 30 / 5 | 4 | 10 | trigger_event(3031); stop |
| 5 | 3031 | 30 / 6 | 3 | 10 | trigger_event(3032); stop |
| 5 | 3032 | 30 / 7 | 2 | 10 | set_switch(235); set_switch(4); set_switch(1); set_switch(5); set_switch(7); set_switch(8); set_switch(26); set_switch(32); set_switch(29); set_switch(27); set_switch(28); stop |
| 5 | 221 | 22 / 1 | 6 | 10 | trigger_event(2211); stop |
| 5 | 2211 | 22 / 2 | 3 | 10 | trigger_event(2212); stop |
| 5 | 2212 | 22 / 3 | 5 | 10 | trigger_event(2213); stop |
| 5 | 2213 | 22 / 4 | 6 | 10 | set_switch(38); set_switch(33); stop |
| 5 | 601 | 60 / 1 | 0 | 10 | trigger_event(6011); stop |
| 5 | 6011 | 60 / 2 | 0 | 10 | trigger_event(6012); stop |
| 5 | 6012 | 60 / 3 | 0 | 10 | set_switch(35); stop |
| 5 | 701 | 70 / 1 | 5 | 10 | trigger_event(7011); stop |
| 5 | 7011 | 70 / 2 | 5 | 10 | trigger_event(7012); stop |
| 5 | 7012 | 70 / 3 | 6 | 240 | trigger_event(7013); stop |
| 5 | 7013 | 70 / 4 | 15 | 10 | set_switch(36); set_switch(37); stop |
| 5 | 331 | 33 / 1 | 2 | 10 | trigger_event(3311); stop |
| 5 | 3311 | 33 / 2 | 2 | 10 | trigger_event(3312); stop |
| 5 | 3312 | 33 / 3 | 2 | 10 | set_switch(29); set_switch(30); stop |
| 5 | 201 | 20 / 1 | 1 | 10 | trigger_event(2011); stop |
| 5 | 2011 | 20 / 2 | 1 | 40 | trigger_event(2012); stop |
| 5 | 2012 | 20 / 3 | 1 | 10 | set_switch(30); set_switch(31); set_switch(22); set_switch(15); stop |
| 5 | 511 | 51 / 1 | 3 | 10 | trigger_event(5111); stop |
| 5 | 5111 | 51 / 2 | 2 | 10 | trigger_event(5112); stop |
| 5 | 5112 | 51 / 3 | 3 | 10 | trigger_event(5113); stop |
| 5 | 5113 | 51 / 4 | 1 | 10 | set_switch(23); set_switch(24); set_switch(25); stop |
| 5 | 211 | 21 / 1 | 2 | 10 | trigger_event(2111); stop |
| 5 | 2111 | 21 / 2 | 3 | 10 | set_switch(7); set_switch(8); set_switch(9); set_switch(10); stop |
| 5 | 321 | 32 / 1 | 2 | 10 | set_switch(11); set_switch(12); set_switch(13); stop |
| 5 | 322 | 32 / 2 | 2 | 10 | trigger_event(3211); stop |
| 5 | 3211 | 32 / 3 | 2 | 10 | set_switch(22); stop |
| 5 | 711 | 71 / 1 | 4 | 10 | trigger_event(7111); stop |
| 5 | 7111 | 71 / 2 | 2 | 10 | trigger_event(7112); stop |
| 5 | 7112 | 71 / 3 | 2 | 10 | trigger_event(7113); stop |
| 5 | 7113 | 71 / 4 | 2 | 360 | set_switch(19); set_switch(20); stop |
| 5 | 231 | 23 / 1 | 1 | 10 | trigger_event(2311); stop |
| 5 | 2311 | 23 / 2 | 1 | 10 | trigger_event(2312); stop |
| 5 | 2312 | 23 / 3 | 1 | 10 | set_switch(21); stop |
| 6 | 301 | 30 / 1 | 8 | 60 | set_switch(16); set_switch(17); stop |
| 6 | 411 | 41 / 1 | 7 | 1 | set_switch(24); stop |
| 6 | 511 | 51 / 1 | 13 | 1 | trigger_event(5111); stop |
| 6 | 5111 | 51 / 2 | 13 | 60 | set_switch(12); set_switch(13); set_switch(14); set_switch(15); stop |
| 6 | 521 | 52 / 1 | 11 | 1 | trigger_event(5211); stop |
| 6 | 5211 | 52 / 2 | 8 | 60 | trigger_event(5212); stop |
| 6 | 5212 | 52 / 3 | 3 | 60 | set_switch(18); set_switch(19); set_switch(20); set_switch(21); set_switch(23); stop |
| 6 | 522 | 52 / 4 | 8 | 1 | trigger_event(5221); stop |
| 6 | 5221 | 52 / 5 | 7 | 60 | stop |
| 6 | 531 | 53 / 1 | 5 | 61 | trigger_event(5311); stop |
| 6 | 5311 | 53 / 2 | 20 | 90 | set_switch(25); set_switch(26); stop |
| 6 | 601 | 60 / 1 | 8 | 1 | trigger_event(6011); stop |
| 6 | 6011 | 60 / 2 | 9 | 60 | set_switch(4); set_switch(6); set_switch(7); set_switch(8); set_switch(9); set_switch(10); set_switch(11); stop |
| 6 | 611 | 61 / 1 | 0 | 1 | trigger_event(6111); stop |
| 6 | 6111 | 61 / 2 | 0 | 45 | trigger_event(6112); stop |
| 6 | 6112 | 61 / 3 | 7 | 45 | trigger_event(6113); stop |
| 6 | 6113 | 61 / 4 | 3 | 60 | set_switch(22); set_switch(27); set_switch(30); set_switch(31); set_switch(32); stop |
| 7 | 211 | 21 / 1 | 0 | 1 | set_switch(17); stop |
| 7 | 301 | 30 / 1 | 0 | 1 | trigger_event(3011); stop |
| 7 | 3011 | 30 / 2 | 0 | 45 | trigger_event(3012); stop |
| 7 | 3012 | 30 / 3 | 0 | 20 | set_switch(15); set_switch(16); stop |
| 7 | 401 | 40 / 1 | 0 | 1 | set_switch(1); set_switch(2); stop |
| 7 | 501 | 50 / 1 | 0 | 1 | trigger_event(5011); stop |
| 7 | 5011 | 50 / 2 | 0 | 1 | set_switch(5); set_switch(235); stop |
| 7 | 511 | 51 / 1 | 0 | 1 | trigger_event(5111); stop |
| 7 | 5111 | 51 / 2 | 0 | 30 | trigger_event(5112); stop |
| 7 | 5112 | 51 / 3 | 0 | 40 | trigger_event(5113); stop |
| 7 | 5113 | 51 / 4 | 0 | 45 | trigger_event(5114); stop |
| 7 | 5114 | 51 / 5 | 0 | 30 | set_switch(21); stop |
| 7 | 521 | 52 / 1 | 0 | 1 | trigger_event(5211); stop |
| 7 | 5211 | 52 / 2 | 0 | 45 | set_switch(10); stop |
| 7 | 531 | 53 / 1 | 0 | 1 | trigger_event(5311); stop |
| 7 | 5311 | 53 / 2 | 0 | 10 | trigger_event(5312); stop |
| 7 | 5312 | 53 / 3 | 0 | 10 | trigger_event(5313); stop |
| 7 | 5313 | 53 / 4 | 0 | 10 | trigger_event(5314); stop |
| 7 | 5314 | 53 / 5 | 0 | 60 | set_switch(17); set_switch(18); set_switch(19); set_switch(20); set_switch(21); set_switch(220); stop |
| 7 | 601 | 60 / 1 | 0 | 1 | trigger_event(6011); stop |
| 7 | 6011 | 60 / 2 | 0 | 30 | trigger_event(6012); stop |
| 7 | 6012 | 60 / 3 | 0 | 30 | trigger_event(6013); stop |
| 7 | 6013 | 60 / 4 | 0 | 1 | trigger_event(6014); stop |
| 7 | 6014 | 60 / 5 | 0 | 60 | trigger_event(6015); stop |
| 7 | 6015 | 60 / 6 | 0 | 30 | trigger_event(6016); stop |
| 7 | 6016 | 60 / 7 | 0 | 1 | trigger_event(6017); stop |
| 7 | 6017 | 60 / 8 | 0 | 1 | set_switch(5); set_switch(6); set_switch(7); set_switch(8); set_switch(9); set_switch(11); set_switch(12); set_switch(215); set_switch(219); stop |
| 7 | 611 | 61 / 1 | 9 | 1 | trigger_event(6111); stop |
| 7 | 6111 | 61 / 2 | 9 | 1 | trigger_event(6112); stop |
| 7 | 6112 | 61 / 3 | 4 | 1 | trigger_event(6113); stop |
| 7 | 6113 | 61 / 4 | 11 | 60 | set_switch(23); set_switch(24); set_switch(25); set_switch(26); stop |
| 7 | 701 | 70 / 1 | 0 | 1 | set_switch(22); stop |
| 7 | 702 | 70 / 2 | 0 | 1 | trigger_event(7021); stop |
| 7 | 7021 | 70 / 3 | 0 | 60 | trigger_event(7022); stop |
| 7 | 7022 | 70 / 4 | 0 | 1 | set_switch(28); set_switch(29); set_switch(30); stop |
| 7 | 801 | 80 / 1 | 0 | 1 | set_switch(11); set_switch(13); stop |
| 7 | 802 | 80 / 2 | 0 | 1 | trigger_event(8021); stop |
| 7 | 8021 | 80 / 3 | 0 | 1 | trigger_event(8022); stop |
| 7 | 8022 | 80 / 4 | 0 | 1 | set_switch(11); set_switch(13); set_switch(14); stop |
| 9 | 201 | 20 / 1 | 4 | 30 | set_switch(37); set_switch(38); stop |
| 9 | 211 | 21 / 1 | 12 | 10 | trigger_event(2111); stop |
| 9 | 2111 | 21 / 2 | 4 | 1 | set_switch(7); set_switch(8); set_switch(35); set_switch(36); stop |
| 9 | 212 | 21 / 3 | 3 | 60 | stop |
| 9 | 301 | 30 / 1 | 25 | 30 | set_switch(31); set_switch(32); stop |
| 9 | 311 | 31 / 1 | 3 | 30 | trigger_event(3111); stop |
| 9 | 3111 | 31 / 2 | 18 | 60 | trigger_event(3112); stop |
| 9 | 3112 | 31 / 3 | 5 | 30 | set_switch(11); set_switch(12); set_switch(13); set_switch(14); set_switch(33); set_switch(34); stop |
| 9 | 312 | 31 / 4 | 5 | 120 | stop |
| 9 | 401 | 40 / 1 | 5 | 1 | trigger_event(4011); stop |
| 9 | 4011 | 40 / 2 | 19 | 30 | set_switch(5); set_switch(6); set_switch(9); set_switch(10); stop |
| 9 | 411 | 41 / 1 | 6 | 30 | trigger_event(4111); stop |
| 9 | 4111 | 41 / 2 | 4 | 60 | trigger_event(4112); stop |
| 9 | 4112 | 41 / 3 | 6 | 60 | set_switch(3); set_switch(4); set_switch(27); set_switch(28); set_switch(29); set_switch(30); stop |
| 9 | 431 | 43 / 1 | 13 | 1 | trigger_event(4311); stop |
| 9 | 4311 | 43 / 2 | 2 | 60 | trigger_event(4312); stop |
| 9 | 4312 | 43 / 3 | 5 | 60 | set_switch(15); set_switch(16); set_switch(17); set_switch(18); set_switch(19); set_switch(20); set_switch(21); set_switch(22); set_switch(23); set_switch(24); stop |
| 9 | 801 | 80 / 1 | 4 | 1 | trigger_event(8011); stop |
| 9 | 8011 | 80 / 2 | 4 | 35 | trigger_event(8012); stop |
| 9 | 8012 | 80 / 3 | 4 | 50 | trigger_event(8013); stop |
| 9 | 8013 | 80 / 4 | 4 | 15 | trigger_event(8014); stop |
| 9 | 8014 | 80 / 5 | 7 | 1 | trigger_event(8015); stop |
| 9 | 8015 | 80 / 6 | 10 | 60 | trigger_event(8016); stop |
| 9 | 8016 | 80 / 7 | 1 | 20 | trigger_event(8017); stop |
| 9 | 8017 | 80 / 8 | 6 | 15 | trigger_event(8018); stop |
| 9 | 8018 | 80 / 9 | 21 | 55 | trigger_event(8019); stop |
| 9 | 8019 | 80 / 10 | 1 | 55 | trigger_event(80191); stop |
| 9 | 80191 | 80 / 21 | 5 | 30 | trigger_event(80192); stop |
| 9 | 80192 | 80 / 23 | 4 | 23 | trigger_event(80193); stop |
| 9 | 80193 | 80 / 25 | 3 | 30 | trigger_event(80194); stop |
| 9 | 80194 | 80 / 26 | 7 | 30 | stop |
| 9 | 802 | 80 / 11 | 11 | 60 | trigger_event(8021); stop |
| 9 | 8021 | 80 / 12 | 1 | 35 | trigger_event(8022); stop |
| 9 | 8022 | 80 / 13 | 1 | 50 | trigger_event(8023); stop |
| 9 | 8023 | 80 / 14 | 4 | 15 | trigger_event(8024); stop |
| 9 | 8024 | 80 / 15 | 1 | 1 | trigger_event(8025); stop |
| 9 | 8025 | 80 / 16 | 4 | 60 | trigger_event(8026); stop |
| 9 | 8026 | 80 / 17 | 21 | 20 | trigger_event(8027); stop |
| 9 | 8027 | 80 / 18 | 4 | 15 | trigger_event(8028); stop |
| 9 | 8028 | 80 / 19 | 4 | 55 | trigger_event(8029); stop |
| 9 | 8029 | 80 / 20 | 2 | 35 | trigger_event(80291); stop |
| 9 | 80291 | 80 / 22 | 1 | 30 | trigger_event(80292); stop |
| 9 | 80292 | 80 / 24 | 3 | 30 | stop |
| 12 | 1 | 1 / 1 | 1 | 50 | construct_objects(room=1,group_or_wave=1); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
