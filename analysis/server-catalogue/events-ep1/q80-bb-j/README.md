# Tyrell\'s Last Hope — events-ep1/q80-bb-j

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/events-ep1/q80-bb-j.zip?download=1)**

[Original QST](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/events-ep1/q80-bb-j.qst?download=1) · [Extracted BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/events-ep1/q80-bb-j/q80-bb-j.qst-quest0.bin?download=1) · [Extracted DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/events-ep1/q80-bb-j/q80-bb-j.qst-quest0.dat?download=1)

QST is the preserved original package. BIN and DAT are its decoded payload files, not reassembled scripts. The ZIP contains all three formats.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 80; language J. Static scan: **860 objects, 815 enemy/NPC records, 180 events, 39 script labels.** Script roundtrip: alignment-only.

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
| 0 | 32 | 22 | 0 |
| 2 | 135 | 121 | 28 |
| 5 | 160 | 171 | 40 |
| 7 | 142 | 210 | 42 |
| 8 | 241 | 217 | 55 |
| 10 | 46 | 69 | 12 |
| 11 | 23 | 1 | 1 |
| 12 | 16 | 1 | 1 |
| 13 | 30 | 2 | 0 |
| 14 | 35 | 1 | 1 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 2 | 21 | 2 / 1 | 5 | 1 | trigger_event(211); stop |
| 2 | 211 | 2 / 2 | 5 | 30 | trigger_event(2111); stop |
| 2 | 2111 | 2 / 3 | 3 | 20 | set_switch(4); set_switch(5); set_switch(6); stop |
| 2 | 31 | 3 / 1 | 5 | 200 | stop |
| 2 | 41 | 4 / 1 | 5 | 30 | set_switch(31); stop |
| 2 | 61 | 6 / 1 | 5 | 1 | trigger_event(611); stop |
| 2 | 611 | 6 / 2 | 3 | 15 | trigger_event(612); stop |
| 2 | 612 | 6 / 3 | 3 | 30 | set_switch(2); set_switch(3); stop |
| 2 | 71 | 7 / 1 | 3 | 100 | stop |
| 2 | 81 | 8 / 1 | 0 | 1 | stop |
| 2 | 101 | 10 / 1 | 9 | 1 | stop |
| 2 | 111 | 11 / 1 | 3 | 1 | trigger_event(1111); stop |
| 2 | 1111 | 11 / 2 | 4 | 10 | trigger_event(1112); stop |
| 2 | 1112 | 11 / 3 | 4 | 10 | trigger_event(1113); stop |
| 2 | 1113 | 11 / 4 | 5 | 10 | trigger_event(1114); stop |
| 2 | 1114 | 11 / 5 | 2 | 1 | set_switch(7); set_switch(8); set_switch(11); stop |
| 2 | 121 | 12 / 1 | 7 | 1 | trigger_event(1211); stop |
| 2 | 1211 | 12 / 2 | 9 | 1 | set_switch(10); stop |
| 2 | 131 | 13 / 1 | 5 | 1 | trigger_event(1311); stop |
| 2 | 1311 | 13 / 2 | 7 | 1 | set_switch(9); stop |
| 2 | 151 | 15 / 1 | 4 | 1 | trigger_event(1511); stop |
| 2 | 1511 | 15 / 2 | 0 | 60 | trigger_event(1512); stop |
| 2 | 1512 | 15 / 3 | 6 | 30 | trigger_event(1513); stop |
| 2 | 1513 | 15 / 4 | 1 | 1 | trigger_event(1514); stop |
| 2 | 1514 | 15 / 5 | 4 | 1 | set_switch(30); stop |
| 2 | 152 | 15 / 6 | 1 | 1 | trigger_event(1521); stop |
| 2 | 1521 | 15 / 7 | 5 | 30 | trigger_event(1522); stop |
| 2 | 1522 | 15 / 8 | 1 | 10 | stop |
| 5 | 301 | 30 / 1 | 1 | 10 | stop |
| 5 | 302 | 30 / 2 | 1 | 10 | trigger_event(3021); stop |
| 5 | 3021 | 30 / 3 | 3 | 10 | trigger_event(3022); stop |
| 5 | 3022 | 30 / 4 | 2 | 10 | stop |
| 5 | 303 | 30 / 5 | 4 | 10 | trigger_event(3031); stop |
| 5 | 3031 | 30 / 6 | 3 | 10 | trigger_event(3032); stop |
| 5 | 3032 | 30 / 7 | 2 | 10 | set_switch(235); set_switch(4); set_switch(1); set_switch(5); set_switch(7); set_switch(8); set_switch(26); set_switch(32); set_switch(29); set_switch(27); set_switch(28); stop |
| 5 | 221 | 22 / 1 | 7 | 10 | trigger_event(2211); stop |
| 5 | 2211 | 22 / 2 | 6 | 10 | trigger_event(2212); stop |
| 5 | 2212 | 22 / 3 | 6 | 10 | trigger_event(2213); stop |
| 5 | 2213 | 22 / 4 | 5 | 10 | set_switch(38); set_switch(33); stop |
| 5 | 601 | 60 / 1 | 0 | 10 | trigger_event(6011); stop |
| 5 | 6011 | 60 / 2 | 0 | 10 | trigger_event(6012); stop |
| 5 | 6012 | 60 / 3 | 0 | 10 | set_switch(35); stop |
| 5 | 701 | 70 / 1 | 7 | 10 | trigger_event(7011); stop |
| 5 | 7011 | 70 / 2 | 8 | 10 | trigger_event(7012); stop |
| 5 | 7012 | 70 / 3 | 4 | 240 | trigger_event(7013); stop |
| 5 | 7013 | 70 / 4 | 5 | 10 | set_switch(36); set_switch(37); stop |
| 5 | 331 | 33 / 1 | 5 | 10 | trigger_event(3311); stop |
| 5 | 3311 | 33 / 2 | 5 | 10 | trigger_event(3312); stop |
| 5 | 3312 | 33 / 3 | 3 | 10 | set_switch(29); set_switch(30); stop |
| 5 | 201 | 20 / 1 | 3 | 10 | trigger_event(2011); stop |
| 5 | 2011 | 20 / 2 | 3 | 40 | trigger_event(2012); stop |
| 5 | 2012 | 20 / 3 | 4 | 10 | set_switch(30); set_switch(31); set_switch(22); set_switch(15); stop |
| 5 | 511 | 51 / 1 | 3 | 10 | trigger_event(5111); stop |
| 5 | 5111 | 51 / 2 | 3 | 10 | trigger_event(5112); stop |
| 5 | 5112 | 51 / 3 | 5 | 10 | trigger_event(5113); stop |
| 5 | 5113 | 51 / 4 | 2 | 10 | set_switch(23); set_switch(24); set_switch(25); stop |
| 5 | 211 | 21 / 1 | 3 | 10 | trigger_event(2111); stop |
| 5 | 2111 | 21 / 2 | 6 | 10 | set_switch(7); set_switch(8); set_switch(9); set_switch(10); stop |
| 5 | 321 | 32 / 1 | 6 | 10 | set_switch(11); set_switch(12); set_switch(13); stop |
| 5 | 322 | 32 / 2 | 5 | 10 | trigger_event(3211); stop |
| 5 | 3211 | 32 / 3 | 3 | 10 | set_switch(22); stop |
| 5 | 711 | 71 / 1 | 4 | 10 | trigger_event(7111); stop |
| 5 | 7111 | 71 / 2 | 3 | 10 | trigger_event(7112); stop |
| 5 | 7112 | 71 / 3 | 2 | 10 | trigger_event(7113); stop |
| 5 | 7113 | 71 / 4 | 2 | 360 | set_switch(19); set_switch(20); stop |
| 5 | 231 | 23 / 1 | 1 | 10 | trigger_event(2311); stop |
| 5 | 2311 | 23 / 2 | 1 | 10 | trigger_event(2312); stop |
| 5 | 2312 | 23 / 3 | 1 | 10 | set_switch(21); stop |
| 7 | 211 | 21 / 1 | 0 | 1 | set_switch(17); stop |
| 7 | 301 | 30 / 1 | 6 | 1 | trigger_event(3011); stop |
| 7 | 3011 | 30 / 2 | 7 | 45 | trigger_event(3012); stop |
| 7 | 3012 | 30 / 3 | 5 | 20 | trigger_event(3013); stop |
| 7 | 3013 | 30 / 4 | 8 | 20 | trigger_event(3014); stop |
| 7 | 3015 | 30 / 5 | 0 | 20 | set_switch(215); stop |
| 7 | 401 | 40 / 1 | 2 | 1 | set_switch(1); set_switch(2); stop |
| 7 | 501 | 50 / 1 | 8 | 1 | trigger_event(5011); stop |
| 7 | 5011 | 50 / 2 | 8 | 40 | trigger_event(5012); stop |
| 7 | 5012 | 50 / 3 | 7 | 1 | set_switch(5); stop |
| 7 | 531 | 53 / 1 | 5 | 1 | trigger_event(5311); stop |
| 7 | 5311 | 53 / 2 | 4 | 60 | trigger_event(5312); stop |
| 7 | 5312 | 53 / 3 | 4 | 60 | trigger_event(5313); stop |
| 7 | 5313 | 53 / 4 | 4 | 60 | trigger_event(5314); stop |
| 7 | 5314 | 53 / 5 | 3 | 19 | trigger_event(5315); stop |
| 7 | 5315 | 53 / 6 | 1 | 1 | trigger_event(5316); stop |
| 7 | 5316 | 53 / 7 | 2 | 1 | trigger_event(5317); stop |
| 7 | 5317 | 53 / 8 | 4 | 60 | trigger_event(5318); stop |
| 7 | 5318 | 53 / 9 | 1 | 30 | trigger_event(5319); stop |
| 7 | 5319 | 53 / 10 | 2 | 30 | stop |
| 7 | 532 | 53 / 11 | 2 | 1 | trigger_event(5321); stop |
| 7 | 5321 | 53 / 12 | 5 | 20 | trigger_event(5322); stop |
| 7 | 5322 | 53 / 13 | 4 | 60 | trigger_event(5323); stop |
| 7 | 5323 | 53 / 14 | 0 | 45 | trigger_event(5324); stop |
| 7 | 5324 | 53 / 15 | 3 | 22 | trigger_event(5325); stop |
| 7 | 5325 | 53 / 16 | 4 | 20 | trigger_event(5326); stop |
| 7 | 5326 | 53 / 17 | 2 | 15 | trigger_event(5327); stop |
| 7 | 5327 | 53 / 18 | 3 | 60 | trigger_event(5328); stop |
| 7 | 5328 | 53 / 19 | 2 | 30 | trigger_event(5329); stop |
| 7 | 5329 | 53 / 20 | 2 | 40 | stop |
| 7 | 601 | 60 / 1 | 13 | 1 | trigger_event(6011); stop |
| 7 | 6011 | 60 / 2 | 3 | 30 | trigger_event(6012); stop |
| 7 | 6012 | 60 / 3 | 3 | 1 | stop |
| 7 | 602 | 60 / 4 | 5 | 1 | trigger_event(6021); stop |
| 7 | 6021 | 60 / 5 | 5 | 60 | trigger_event(6022); stop |
| 7 | 6022 | 60 / 6 | 2 | 60 | set_switch(5); set_switch(6); set_switch(7); set_switch(8); set_switch(9); set_switch(11); set_switch(12); stop |
| 7 | 801 | 80 / 1 | 6 | 1 | trigger_event(8011); stop |
| 7 | 8011 | 80 / 2 | 4 | 1 | trigger_event(8012); stop |
| 7 | 8012 | 80 / 3 | 3 | 1 | trigger_event(8013); stop |
| 7 | 8013 | 80 / 4 | 5 | 1 | trigger_event(8014); stop |
| 7 | 8014 | 80 / 5 | 3 | 1 | trigger_event(8015); stop |
| 7 | 8015 | 80 / 6 | 4 | 1 | set_switch(13); set_switch(14); stop |
| 8 | 602 | 60 / 1 | 10 | 30 | set_switch(55); set_switch(56); set_switch(52); set_switch(51); stop |
| 8 | 201 | 20 / 1 | 6 | 30 | trigger_event(2011); stop |
| 8 | 2011 | 20 / 2 | 5 | 30 | trigger_event(2012); stop |
| 8 | 2012 | 20 / 3 | 4 | 30 | set_switch(50); set_switch(49); set_switch(45); set_switch(46); set_switch(47); set_switch(48); stop |
| 8 | 701 | 70 / 1 | 5 | 30 | trigger_event(7011); stop |
| 8 | 7011 | 70 / 2 | 6 | 30 | trigger_event(7012); stop |
| 8 | 7012 | 70 / 3 | 3 | 30 | set_switch(43); set_switch(44); stop |
| 8 | 311 | 31 / 1 | 4 | 30 | trigger_event(3111); stop |
| 8 | 3111 | 31 / 2 | 3 | 30 | trigger_event(3112); stop |
| 8 | 3112 | 31 / 3 | 5 | 30 | set_switch(34); set_switch(33); set_switch(36); set_switch(35); set_switch(39); set_switch(40); set_switch(37); set_switch(38); set_switch(31); set_switch(32); stop |
| 8 | 211 | 21 / 1 | 2 | 30 | set_switch(41); set_switch(42); stop |
| 8 | 212 | 21 / 2 | 6 | 30 | stop |
| 8 | 221 | 22 / 1 | 5 | 30 | trigger_event(2211); stop |
| 8 | 2211 | 22 / 2 | 5 | 30 | set_switch(28); set_switch(27); stop |
| 8 | 501 | 50 / 1 | 3 | 30 | set_switch(23); set_switch(24); stop |
| 8 | 502 | 50 / 2 | 4 | 30 | set_switch(29); set_switch(30); set_switch(31); set_switch(32); stop |
| 8 | 321 | 32 / 1 | 8 | 30 | trigger_event(3211); stop |
| 8 | 3211 | 32 / 2 | 0 | 30 | trigger_event(3212); stop |
| 8 | 3212 | 32 / 3 | 5 | 30 | set_switch(25); set_switch(26); set_switch(21); set_switch(22); set_switch(20); set_switch(19); set_switch(17); set_switch(18); set_switch(16); set_switch(15); set_switch(13); set_switch(14); set_switch(11); set_switch(12); set_switch(10); set_switch(9); set_switch(1); set_switch(2); set_switch(3); set_switch(4); stop |
| 8 | 241 | 24 / 1 | 6 | 30 | trigger_event(2411); stop |
| 8 | 2411 | 24 / 2 | 5 | 30 | trigger_event(2412); stop |
| 8 | 2412 | 24 / 3 | 8 | 30 | stop |
| 8 | 231 | 23 / 1 | 3 | 30 | trigger_event(2311); stop |
| 8 | 2311 | 23 / 2 | 4 | 30 | trigger_event(2312); stop |
| 8 | 2312 | 23 / 3 | 1 | 30 | trigger_event(2313); stop |
| 8 | 2313 | 23 / 4 | 5 | 30 | trigger_event(2314); stop |
| 8 | 2314 | 23 / 5 | 6 | 30 | trigger_event(2315); stop |
| 8 | 2315 | 23 / 6 | 1 | 30 | trigger_event(2316); stop |
| 8 | 2316 | 23 / 7 | 5 | 30 | set_switch(5); set_switch(6); set_switch(3); set_switch(4); stop |
| 8 | 331 | 33 / 1 | 3 | 30 | trigger_event(3311); stop |
| 8 | 3311 | 33 / 2 | 3 | 30 | trigger_event(3312); stop |
| 8 | 3312 | 33 / 3 | 3 | 30 | trigger_event(3313); stop |
| 8 | 3313 | 33 / 4 | 2 | 30 | trigger_event(3314); stop |
| 8 | 3314 | 33 / 5 | 2 | 30 | trigger_event(3315); stop |
| 8 | 3315 | 33 / 6 | 2 | 30 | trigger_event(3316); stop |
| 8 | 3316 | 33 / 7 | 1 | 30 | trigger_event(3317); stop |
| 8 | 3317 | 33 / 8 | 1 | 30 | trigger_event(3318); stop |
| 8 | 3318 | 33 / 9 | 2 | 30 | trigger_event(3319); stop |
| 8 | 3319 | 33 / 10 | 1 | 30 | trigger_event(3380); stop |
| 8 | 3380 | 33 / 11 | 0 | 30 | trigger_event(3381); stop |
| 8 | 3381 | 33 / 12 | 1 | 30 | trigger_event(3382); stop |
| 8 | 3382 | 33 / 13 | 2 | 30 | set_switch(7); set_switch(8); stop |
| 8 | 332 | 33 / 14 | 2 | 30 | trigger_event(3321); stop |
| 8 | 3321 | 33 / 15 | 2 | 30 | trigger_event(3322); stop |
| 8 | 3322 | 33 / 16 | 2 | 30 | trigger_event(3323); stop |
| 8 | 3323 | 33 / 17 | 3 | 30 | trigger_event(3324); stop |
| 8 | 3324 | 33 / 18 | 3 | 30 | trigger_event(3325); stop |
| 8 | 3325 | 33 / 19 | 4 | 30 | trigger_event(3326); stop |
| 8 | 3326 | 33 / 20 | 3 | 30 | trigger_event(3327); stop |
| 8 | 3327 | 33 / 21 | 3 | 30 | trigger_event(3328); stop |
| 8 | 3328 | 33 / 22 | 3 | 30 | trigger_event(3329); stop |
| 8 | 3329 | 33 / 23 | 1 | 30 | trigger_event(3390); stop |
| 8 | 3390 | 33 / 24 | 1 | 30 | trigger_event(3391); stop |
| 8 | 3391 | 33 / 25 | 1 | 30 | trigger_event(3392); stop |
| 8 | 3392 | 33 / 26 | 2 | 30 | stop |
| 10 | 221 | 22 / 1 | 6 | 1 | trigger_event(2211); stop |
| 10 | 2211 | 22 / 2 | 5 | 100 | trigger_event(2212); stop |
| 10 | 2212 | 22 / 3 | 4 | 100 | set_switch(16); set_switch(17); set_switch(18); set_switch(19); stop |
| 10 | 222 | 22 / 4 | 4 | 60 | set_switch(16); set_switch(17); set_switch(18); set_switch(19); stop |
| 10 | 401 | 40 / 1 | 4 | 30 | trigger_event(4011); stop |
| 10 | 4011 | 40 / 2 | 6 | 100 | trigger_event(4012); stop |
| 10 | 4012 | 40 / 3 | 4 | 100 | set_switch(24); set_switch(25); set_switch(90); stop |
| 10 | 402 | 40 / 4 | 4 | 30 | set_switch(24); set_switch(25); set_switch(90); stop |
| 10 | 701 | 70 / 1 | 2 | 30 | trigger_event(7011); stop |
| 10 | 7011 | 70 / 2 | 6 | 60 | trigger_event(7012); stop |
| 10 | 7012 | 70 / 3 | 7 | 60 | set_switch(22); set_switch(23); stop |
| 10 | 702 | 70 / 4 | 3 | 100 | set_switch(22); set_switch(23); stop |
| 11 | 1 | 1 / 1 | 1 | 50 | construct_objects(room=1,group_or_wave=1); stop |
| 12 | 1 | 1 / 1 | 1 | 50 | construct_objects(room=1,group_or_wave=1); stop |
| 14 | 1 | 0 / 1 | 1 | 50 | construct_objects(room=0,group_or_wave=1); construct_objects(room=1,group_or_wave=1); construct_objects(room=2,group_or_wave=1); stop |

## Review notes

- Floor 7: event 3013 targets absent event 3014
