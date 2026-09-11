# Endless Carnage — vr-ep1/q990-bb-e

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/vr-ep1/q990-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/vr-ep1/q990-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/vr-ep1/q990-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 990; language E. Static scan: **989 objects, 1931 enemy/NPC records, 296 events, 416 script labels.** Script roundtrip: byte-identical.

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
0x02, 0x02, 0x00, 0x00, 0x00
0x05, 0x05, 0x00, 0x05, 0x00
0x06, 0x06, 0x00, 0x03, 0x00
0x07, 0x07, 0x00, 0x05, 0x00
0x08, 0x08, 0x00, 0x00, 0x00
0x09, 0x09, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 13 | 0 |
| 2 | 140 | 350 | 78 |
| 5 | 185 | 390 | 44 |
| 7 | 178 | 440 | 76 |
| 8 | 221 | 406 | 55 |
| 9 | 239 | 332 | 43 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 2 | 21 | 2 / 1 | 2 | 1 | trigger_event(211); stop |
| 2 | 211 | 2 / 2 | 2 | 1 | trigger_event(212); stop |
| 2 | 212 | 2 / 3 | 2 | 1 | trigger_event(213); stop |
| 2 | 213 | 2 / 4 | 2 | 1 | trigger_event(214); stop |
| 2 | 214 | 2 / 5 | 2 | 1 | stop |
| 2 | 22 | 2 / 6 | 2 | 1 | trigger_event(221); stop |
| 2 | 221 | 2 / 7 | 2 | 1 | trigger_event(222); stop |
| 2 | 222 | 2 / 8 | 2 | 1 | trigger_event(223); stop |
| 2 | 223 | 2 / 9 | 2 | 1 | trigger_event(224); stop |
| 2 | 224 | 2 / 10 | 2 | 1 | stop |
| 2 | 23 | 2 / 11 | 2 | 1 | trigger_event(231); stop |
| 2 | 231 | 2 / 12 | 2 | 1 | trigger_event(232); stop |
| 2 | 232 | 2 / 13 | 2 | 1 | trigger_event(233); stop |
| 2 | 233 | 2 / 14 | 2 | 1 | trigger_event(234); stop |
| 2 | 234 | 2 / 15 | 2 | 1 | stop |
| 2 | 24 | 2 / 16 | 2 | 1 | trigger_event(241); stop |
| 2 | 241 | 2 / 17 | 2 | 1 | trigger_event(242); stop |
| 2 | 242 | 2 / 18 | 2 | 1 | trigger_event(243); stop |
| 2 | 243 | 2 / 19 | 2 | 1 | trigger_event(244); stop |
| 2 | 244 | 2 / 20 | 2 | 1 | stop |
| 2 | 25 | 2 / 21 | 2 | 1 | trigger_event(251); stop |
| 2 | 251 | 2 / 22 | 2 | 1 | trigger_event(252); stop |
| 2 | 252 | 2 / 23 | 2 | 1 | trigger_event(253); stop |
| 2 | 253 | 2 / 24 | 2 | 1 | trigger_event(254); stop |
| 2 | 254 | 2 / 25 | 2 | 1 | set_switch(1); stop |
| 2 | 26 | 2 / 26 | 2 | 1 | stop |
| 2 | 41 | 4 / 1 | 12 | 1 | trigger_event(411); stop |
| 2 | 411 | 4 / 2 | 12 | 1 | trigger_event(412); stop |
| 2 | 412 | 4 / 3 | 12 | 1 | trigger_event(413); stop |
| 2 | 413 | 4 / 4 | 6 | 1 | stop |
| 2 | 61 | 6 / 1 | 10 | 1 | trigger_event(611); stop |
| 2 | 611 | 6 / 2 | 10 | 1 | trigger_event(612); stop |
| 2 | 612 | 6 / 3 | 12 | 1 | trigger_event(613); stop |
| 2 | 613 | 6 / 4 | 8 | 1 | trigger_event(614); stop |
| 2 | 614 | 6 / 5 | 8 | 1 | trigger_event(615); stop |
| 2 | 615 | 6 / 6 | 6 | 1 | set_switch(2); set_switch(3); stop |
| 2 | 101 | 10 / 1 | 6 | 1 | trigger_event(1011); stop |
| 2 | 1011 | 10 / 2 | 6 | 1 | trigger_event(1012); stop |
| 2 | 1012 | 10 / 3 | 6 | 1 | trigger_event(1013); stop |
| 2 | 1013 | 10 / 4 | 6 | 1 | trigger_event(1014); stop |
| 2 | 1014 | 10 / 5 | 6 | 1 | trigger_event(1015); stop |
| 2 | 1015 | 10 / 6 | 12 | 1 | trigger_event(1016); set_switch(104); stop |
| 2 | 1016 | 10 / 7 | 2 | 150 | stop |
| 2 | 111 | 11 / 1 | 2 | 1 | stop |
| 2 | 112 | 11 / 2 | 2 | 20 | stop |
| 2 | 113 | 11 / 3 | 2 | 40 | stop |
| 2 | 114 | 11 / 4 | 2 | 60 | stop |
| 2 | 115 | 11 / 5 | 2 | 80 | trigger_event(1111); stop |
| 2 | 1111 | 11 / 6 | 8 | 10 | trigger_event(1112); stop |
| 2 | 1112 | 11 / 7 | 8 | 10 | trigger_event(1113); stop |
| 2 | 1113 | 11 / 8 | 8 | 10 | trigger_event(1114); stop |
| 2 | 1114 | 11 / 9 | 12 | 10 | set_switch(4); set_switch(6); set_switch(7); set_switch(8); set_switch(11); stop |
| 2 | 121 | 12 / 1 | 6 | 10 | trigger_event(1211); stop |
| 2 | 1211 | 12 / 2 | 6 | 10 | trigger_event(1212); stop |
| 2 | 1212 | 12 / 3 | 8 | 10 | trigger_event(1213); stop |
| 2 | 1213 | 12 / 4 | 10 | 10 | trigger_event(1214); stop |
| 2 | 1214 | 12 / 5 | 8 | 10 | set_switch(10); stop |
| 2 | 131 | 13 / 1 | 10 | 1 | trigger_event(1311); stop |
| 2 | 1311 | 13 / 2 | 12 | 1 | trigger_event(1312); stop |
| 2 | 1312 | 13 / 3 | 6 | 1 | trigger_event(1313); stop |
| 2 | 1313 | 13 / 4 | 12 | 1 | set_switch(9); stop |
| 2 | 151 | 15 / 1 | 2 | 70 | trigger_event(1511); trigger_event(1526); trigger_event(1531); trigger_event(15416); stop |
| 2 | 1511 | 15 / 2 | 2 | 1 | trigger_event(1512); stop |
| 2 | 1512 | 15 / 3 | 2 | 1 | trigger_event(1513); stop |
| 2 | 1513 | 15 / 4 | 2 | 1 | trigger_event(1514); stop |
| 2 | 1514 | 15 / 5 | 2 | 1 | stop |
| 2 | 1526 | 15 / 6 | 2 | 1 | trigger_event(1527); stop |
| 2 | 1527 | 15 / 7 | 2 | 1 | trigger_event(1528); stop |
| 2 | 1528 | 15 / 8 | 2 | 1 | trigger_event(1529); stop |
| 2 | 1529 | 15 / 9 | 2 | 1 | stop |
| 2 | 1531 | 15 / 10 | 2 | 1 | trigger_event(1532); stop |
| 2 | 1532 | 15 / 11 | 2 | 1 | trigger_event(1533); stop |
| 2 | 1533 | 15 / 12 | 2 | 1 | trigger_event(1534); stop |
| 2 | 1534 | 15 / 13 | 2 | 1 | stop |
| 2 | 15416 | 15 / 14 | 2 | 1 | trigger_event(15417); stop |
| 2 | 15417 | 15 / 15 | 2 | 1 | trigger_event(15418); stop |
| 2 | 15418 | 15 / 16 | 2 | 1 | trigger_event(15419); stop |
| 2 | 15419 | 15 / 17 | 2 | 1 | set_switch(106); stop |
| 5 | 201 | 20 / 1 | 8 | 10 | trigger_event(2011); stop |
| 5 | 2011 | 20 / 2 | 8 | 10 | set_switch(16); set_switch(17); set_switch(18); set_switch(19); set_switch(20); set_switch(21); stop |
| 5 | 211 | 21 / 1 | 8 | 10 | trigger_event(2111); stop |
| 5 | 2111 | 21 / 2 | 12 | 10 | set_switch(14); set_switch(15); set_switch(16); set_switch(17); set_switch(18); set_switch(19); stop |
| 5 | 301 | 30 / 1 | 10 | 10 | trigger_event(3011); stop |
| 5 | 3011 | 30 / 2 | 12 | 10 | set_switch(11); stop |
| 5 | 311 | 31 / 1 | 10 | 10 | trigger_event(3111); stop |
| 5 | 3111 | 31 / 2 | 12 | 10 | trigger_event(3112); stop |
| 5 | 3112 | 31 / 3 | 8 | 10 | set_switch(31); set_switch(32); set_switch(33); stop |
| 5 | 321 | 32 / 1 | 8 | 10 | trigger_event(3211); stop |
| 5 | 3211 | 32 / 2 | 8 | 10 | trigger_event(3212); stop |
| 5 | 3212 | 32 / 3 | 8 | 10 | set_switch(4); set_switch(5); set_switch(6); set_switch(7); set_switch(14); set_switch(15); stop |
| 5 | 331 | 33 / 1 | 4 | 10 | set_switch(26); set_switch(27); stop |
| 5 | 411 | 41 / 1 | 8 | 60 | trigger_event(4111); stop |
| 5 | 4111 | 41 / 2 | 8 | 10 | trigger_event(4112); stop |
| 5 | 4112 | 41 / 3 | 16 | 10 | trigger_event(4113); stop |
| 5 | 4113 | 41 / 4 | 12 | 10 | set_switch(20); set_switch(21); set_switch(22); set_switch(23); set_switch(29); set_switch(30); stop |
| 5 | 501 | 50 / 1 | 2 | 1 | stop |
| 5 | 502 | 50 / 2 | 8 | 1 | trigger_event(5022); stop |
| 5 | 5022 | 50 / 3 | 12 | 10 | trigger_event(5023); stop |
| 5 | 5023 | 50 / 4 | 6 | 10 | set_switch(9); set_switch(10); set_switch(36); set_switch(14); set_switch(15); stop |
| 5 | 511 | 51 / 1 | 2 | 1 | trigger_event(5111); stop |
| 5 | 5111 | 51 / 2 | 8 | 10 | trigger_event(5112); stop |
| 5 | 5112 | 51 / 3 | 12 | 10 | set_switch(22); set_switch(23); set_switch(24); set_switch(25); set_switch(26); stop |
| 5 | 521 | 52 / 1 | 6 | 10 | trigger_event(5211); stop |
| 5 | 5211 | 52 / 2 | 8 | 10 | trigger_event(5212); stop |
| 5 | 5212 | 52 / 3 | 8 | 10 | trigger_event(5213); stop |
| 5 | 5213 | 52 / 4 | 12 | 10 | trigger_event(5214); stop |
| 5 | 5214 | 52 / 5 | 6 | 10 | set_switch(34); stop |
| 5 | 531 | 53 / 1 | 4 | 10 | set_switch(3); stop |
| 5 | 701 | 70 / 1 | 12 | 90 | trigger_event(7011); stop |
| 5 | 7011 | 70 / 2 | 12 | 10 | trigger_event(7012); stop |
| 5 | 7012 | 70 / 3 | 16 | 10 | trigger_event(7013); stop |
| 5 | 7013 | 70 / 4 | 0 | 10 | set_switch(12); stop |
| 5 | 711 | 71 / 1 | 10 | 1 | trigger_event(7111); stop |
| 5 | 7111 | 71 / 2 | 8 | 10 | set_switch(2); stop |
| 5 | 721 | 72 / 1 | 8 | 90 | trigger_event(7211); stop |
| 5 | 7211 | 72 / 2 | 12 | 10 | set_switch(27); stop |
| 5 | 731 | 73 / 1 | 10 | 1 | trigger_event(7311); stop |
| 5 | 7311 | 73 / 2 | 10 | 10 | trigger_event(7312); stop |
| 5 | 7312 | 73 / 3 | 10 | 10 | trigger_event(7313); stop |
| 5 | 7313 | 73 / 4 | 8 | 10 | trigger_event(7314); stop |
| 5 | 7314 | 73 / 5 | 12 | 10 | trigger_event(7315); stop |
| 5 | 7315 | 73 / 6 | 8 | 10 | set_switch(35); stop |
| 7 | 201 | 20 / 1 | 2 | 1 | trigger_event(2011); stop |
| 7 | 2011 | 20 / 2 | 2 | 1 | trigger_event(2012); stop |
| 7 | 2012 | 20 / 3 | 2 | 1 | trigger_event(2013); stop |
| 7 | 2013 | 20 / 4 | 2 | 1 | stop |
| 7 | 202 | 20 / 5 | 2 | 1 | trigger_event(2021); stop |
| 7 | 2021 | 20 / 6 | 2 | 1 | trigger_event(2022); stop |
| 7 | 2022 | 20 / 7 | 2 | 1 | trigger_event(2023); stop |
| 7 | 2023 | 20 / 8 | 2 | 1 | stop |
| 7 | 203 | 20 / 9 | 2 | 1 | trigger_event(2031); stop |
| 7 | 2031 | 20 / 10 | 2 | 1 | trigger_event(2032); stop |
| 7 | 2032 | 20 / 11 | 2 | 1 | trigger_event(2033); stop |
| 7 | 2033 | 20 / 12 | 2 | 1 | stop |
| 7 | 204 | 20 / 13 | 2 | 1 | trigger_event(2041); stop |
| 7 | 2041 | 20 / 14 | 2 | 1 | trigger_event(2042); stop |
| 7 | 2042 | 20 / 15 | 2 | 1 | trigger_event(2043); stop |
| 7 | 2043 | 20 / 16 | 2 | 1 | trigger_event(2044); stop |
| 7 | 205 | 20 / 17 | 2 | 1 | trigger_event(2051); stop |
| 7 | 2051 | 20 / 18 | 2 | 1 | trigger_event(2052); stop |
| 7 | 2052 | 20 / 19 | 2 | 1 | trigger_event(2053); stop |
| 7 | 2053 | 20 / 20 | 2 | 1 | set_switch(9); stop |
| 7 | 401 | 40 / 1 | 2 | 1 | trigger_event(4011); stop |
| 7 | 4011 | 40 / 2 | 2 | 1 | trigger_event(4012); stop |
| 7 | 4012 | 40 / 3 | 2 | 1 | stop |
| 7 | 402 | 40 / 5 | 2 | 1 | trigger_event(4021); stop |
| 7 | 4021 | 40 / 6 | 2 | 1 | trigger_event(4022); stop |
| 7 | 4022 | 40 / 7 | 2 | 1 | stop |
| 7 | 403 | 40 / 9 | 2 | 1 | trigger_event(4031); stop |
| 7 | 4031 | 40 / 10 | 2 | 1 | trigger_event(4032); stop |
| 7 | 4032 | 40 / 11 | 2 | 1 | stop |
| 7 | 404 | 40 / 13 | 2 | 1 | trigger_event(4041); stop |
| 7 | 4041 | 40 / 14 | 2 | 1 | trigger_event(4042); stop |
| 7 | 4042 | 40 / 15 | 2 | 1 | stop |
| 7 | 405 | 40 / 17 | 0 | 1 | trigger_event(4051); stop |
| 7 | 4051 | 40 / 18 | 0 | 1 | trigger_event(4052); stop |
| 7 | 4052 | 40 / 19 | 0 | 1 | set_switch(2); set_switch(22); stop |
| 7 | 411 | 41 / 1 | 4 | 1 | stop |
| 7 | 412 | 41 / 2 | 4 | 1 | stop |
| 7 | 413 | 41 / 3 | 4 | 1 | trigger_event(4131); stop |
| 7 | 4131 | 41 / 4 | 16 | 1 | trigger_event(4132); stop |
| 7 | 4132 | 41 / 5 | 2 | 1 | trigger_event(4133); stop |
| 7 | 4133 | 41 / 6 | 8 | 1 | set_switch(6); stop |
| 7 | 501 | 50 / 1 | 12 | 1 | trigger_event(5011); stop |
| 7 | 5011 | 50 / 2 | 12 | 1 | trigger_event(5012); stop |
| 7 | 5012 | 50 / 3 | 12 | 1 | trigger_event(5013); stop |
| 7 | 5013 | 50 / 4 | 12 | 1 | trigger_event(5014); stop |
| 7 | 5014 | 50 / 5 | 8 | 600 | trigger_event(5015); stop |
| 7 | 5015 | 50 / 6 | 8 | 10 | set_switch(3); set_switch(14); set_switch(15); set_switch(16); set_switch(17); set_switch(18); stop |
| 7 | 511 | 51 / 1 | 10 | 1 | trigger_event(5111); stop |
| 7 | 5111 | 51 / 2 | 16 | 1 | trigger_event(5112); stop |
| 7 | 5112 | 51 / 3 | 8 | 1 | trigger_event(5113); stop |
| 7 | 5113 | 51 / 4 | 8 | 1 | trigger_event(5114); stop |
| 7 | 5114 | 51 / 5 | 8 | 1 | trigger_event(5115); trigger_event(5118); trigger_event(51111); stop |
| 7 | 5115 | 51 / 6 | 4 | 1 | trigger_event(5116); stop |
| 7 | 5116 | 51 / 7 | 4 | 1 | stop |
| 7 | 5118 | 51 / 8 | 4 | 1 | trigger_event(5119); stop |
| 7 | 5119 | 51 / 9 | 4 | 1 | stop |
| 7 | 51111 | 51 / 10 | 2 | 1 | trigger_event(51112); stop |
| 7 | 51112 | 51 / 11 | 2 | 1 | set_switch(10); stop |
| 7 | 521 | 52 / 1 | 14 | 1 | trigger_event(5211); stop |
| 7 | 5211 | 52 / 2 | 12 | 1 | trigger_event(5212); stop |
| 7 | 5212 | 52 / 3 | 16 | 1 | trigger_event(5213); stop |
| 7 | 5213 | 52 / 4 | 8 | 1 | set_switch(21); set_switch(22); stop |
| 7 | 601 | 60 / 1 | 12 | 1 | trigger_event(6011); stop |
| 7 | 6011 | 60 / 2 | 12 | 1 | trigger_event(6012); stop |
| 7 | 6012 | 60 / 3 | 8 | 1 | trigger_event(6013); stop |
| 7 | 6013 | 60 / 4 | 6 | 1 | set_switch(11); set_switch(12); set_switch(7); set_switch(8); stop |
| 7 | 611 | 61 / 1 | 12 | 1 | trigger_event(6111); stop |
| 7 | 6111 | 61 / 2 | 4 | 1 | trigger_event(6112); stop |
| 7 | 6112 | 61 / 3 | 16 | 1 | trigger_event(6113); stop |
| 7 | 6113 | 61 / 4 | 16 | 1 | trigger_event(6114); stop |
| 7 | 6114 | 61 / 5 | 8 | 1 | set_switch(1); set_switch(2); set_switch(3); set_switch(4); set_switch(15); stop |
| 7 | 701 | 70 / 1 | 2 | 1 | trigger_event(7011); stop |
| 7 | 7011 | 70 / 2 | 12 | 1 | trigger_event(7012); stop |
| 7 | 7012 | 70 / 3 | 12 | 1 | trigger_event(7013); stop |
| 7 | 7013 | 70 / 4 | 12 | 1 | trigger_event(7014); stop |
| 7 | 7014 | 70 / 5 | 16 | 1 | set_switch(14); set_switch(13); stop |
| 8 | 602 | 60 / 1 | 16 | 30 | set_switch(55); set_switch(56); set_switch(52); set_switch(51); stop |
| 8 | 201 | 20 / 1 | 12 | 30 | trigger_event(2011); stop |
| 8 | 2011 | 20 / 2 | 12 | 30 | trigger_event(2012); stop |
| 8 | 2012 | 20 / 3 | 12 | 30 | set_switch(50); set_switch(49); set_switch(45); set_switch(46); set_switch(47); set_switch(48); stop |
| 8 | 701 | 70 / 1 | 10 | 30 | trigger_event(7011); stop |
| 8 | 7011 | 70 / 2 | 14 | 30 | trigger_event(7012); stop |
| 8 | 7012 | 70 / 3 | 4 | 30 | set_switch(43); set_switch(44); stop |
| 8 | 311 | 31 / 1 | 4 | 30 | trigger_event(3111); stop |
| 8 | 3111 | 31 / 2 | 6 | 30 | trigger_event(3112); stop |
| 8 | 3112 | 31 / 3 | 12 | 30 | set_switch(34); set_switch(33); set_switch(36); set_switch(35); set_switch(39); set_switch(40); set_switch(37); set_switch(38); set_switch(31); set_switch(32); stop |
| 8 | 211 | 21 / 1 | 8 | 30 | set_switch(41); set_switch(42); stop |
| 8 | 212 | 21 / 2 | 8 | 30 | stop |
| 8 | 221 | 22 / 1 | 16 | 30 | trigger_event(2211); stop |
| 8 | 2211 | 22 / 2 | 10 | 30 | set_switch(28); set_switch(27); stop |
| 8 | 501 | 50 / 1 | 12 | 30 | set_switch(23); set_switch(24); stop |
| 8 | 502 | 50 / 2 | 8 | 30 | set_switch(29); set_switch(30); set_switch(31); set_switch(32); stop |
| 8 | 321 | 32 / 1 | 6 | 30 | trigger_event(3211); stop |
| 8 | 3211 | 32 / 2 | 6 | 30 | trigger_event(3212); stop |
| 8 | 3212 | 32 / 3 | 12 | 30 | set_switch(25); set_switch(26); set_switch(21); set_switch(22); set_switch(20); set_switch(19); set_switch(17); set_switch(18); set_switch(16); set_switch(15); set_switch(13); set_switch(14); set_switch(11); set_switch(12); set_switch(10); set_switch(9); set_switch(1); set_switch(2); set_switch(3); set_switch(4); stop |
| 8 | 241 | 24 / 1 | 6 | 30 | trigger_event(2411); stop |
| 8 | 2411 | 24 / 2 | 6 | 30 | trigger_event(2412); stop |
| 8 | 2412 | 24 / 3 | 10 | 30 | stop |
| 8 | 231 | 23 / 1 | 6 | 30 | trigger_event(2311); stop |
| 8 | 2311 | 23 / 2 | 6 | 30 | trigger_event(2312); stop |
| 8 | 2312 | 23 / 3 | 6 | 30 | trigger_event(2313); stop |
| 8 | 2313 | 23 / 4 | 10 | 30 | trigger_event(2314); stop |
| 8 | 2314 | 23 / 5 | 10 | 30 | trigger_event(2315); stop |
| 8 | 2315 | 23 / 6 | 6 | 30 | trigger_event(2316); stop |
| 8 | 2316 | 23 / 7 | 10 | 30 | set_switch(5); set_switch(6); set_switch(3); set_switch(4); stop |
| 8 | 331 | 33 / 1 | 6 | 30 | trigger_event(3311); stop |
| 8 | 3311 | 33 / 2 | 6 | 30 | trigger_event(3312); stop |
| 8 | 3312 | 33 / 3 | 6 | 30 | trigger_event(3313); stop |
| 8 | 3313 | 33 / 4 | 4 | 30 | trigger_event(3314); stop |
| 8 | 3314 | 33 / 5 | 4 | 30 | trigger_event(3315); stop |
| 8 | 3315 | 33 / 6 | 4 | 30 | trigger_event(3316); stop |
| 8 | 3316 | 33 / 7 | 6 | 30 | trigger_event(3317); stop |
| 8 | 3317 | 33 / 8 | 6 | 30 | trigger_event(3318); stop |
| 8 | 3318 | 33 / 9 | 6 | 30 | trigger_event(3319); stop |
| 8 | 3319 | 33 / 10 | 4 | 30 | trigger_event(3380); stop |
| 8 | 3380 | 33 / 11 | 4 | 30 | trigger_event(3381); stop |
| 8 | 3381 | 33 / 12 | 4 | 30 | trigger_event(3382); stop |
| 8 | 3382 | 33 / 13 | 4 | 30 | set_switch(7); set_switch(8); stop |
| 8 | 332 | 33 / 14 | 6 | 30 | trigger_event(3321); stop |
| 8 | 3321 | 33 / 15 | 6 | 30 | trigger_event(3322); stop |
| 8 | 3322 | 33 / 16 | 6 | 30 | trigger_event(3323); stop |
| 8 | 3323 | 33 / 17 | 8 | 30 | trigger_event(3324); stop |
| 8 | 3324 | 33 / 18 | 8 | 30 | trigger_event(3325); stop |
| 8 | 3325 | 33 / 19 | 8 | 30 | trigger_event(3326); stop |
| 8 | 3326 | 33 / 20 | 8 | 30 | trigger_event(3327); stop |
| 8 | 3327 | 33 / 21 | 6 | 30 | trigger_event(3328); stop |
| 8 | 3328 | 33 / 22 | 6 | 30 | trigger_event(3329); stop |
| 8 | 3329 | 33 / 23 | 2 | 30 | trigger_event(3390); stop |
| 8 | 3390 | 33 / 24 | 6 | 30 | trigger_event(3391); stop |
| 8 | 3391 | 33 / 25 | 2 | 30 | trigger_event(3392); stop |
| 8 | 3392 | 33 / 26 | 6 | 30 | stop |
| 9 | 201 | 20 / 1 | 8 | 30 | set_switch(37); set_switch(38); stop |
| 9 | 211 | 21 / 1 | 12 | 10 | trigger_event(2111); stop |
| 9 | 2111 | 21 / 2 | 8 | 1 | set_switch(7); set_switch(8); set_switch(35); set_switch(36); stop |
| 9 | 212 | 21 / 3 | 6 | 60 | stop |
| 9 | 301 | 30 / 1 | 18 | 30 | set_switch(31); set_switch(32); stop |
| 9 | 311 | 31 / 1 | 6 | 30 | trigger_event(3111); stop |
| 9 | 3111 | 31 / 2 | 16 | 60 | trigger_event(3112); stop |
| 9 | 3112 | 31 / 3 | 10 | 30 | set_switch(11); set_switch(12); set_switch(13); set_switch(14); set_switch(33); set_switch(34); stop |
| 9 | 312 | 31 / 4 | 10 | 120 | stop |
| 9 | 401 | 40 / 1 | 16 | 1 | trigger_event(4011); stop |
| 9 | 4011 | 40 / 2 | 16 | 30 | set_switch(5); set_switch(6); set_switch(9); set_switch(10); stop |
| 9 | 411 | 41 / 1 | 6 | 30 | trigger_event(4111); stop |
| 9 | 4111 | 41 / 2 | 8 | 60 | trigger_event(4112); stop |
| 9 | 4112 | 41 / 3 | 2 | 60 | set_switch(3); set_switch(4); set_switch(27); set_switch(28); set_switch(29); set_switch(30); stop |
| 9 | 431 | 43 / 1 | 16 | 1 | trigger_event(4311); stop |
| 9 | 4311 | 43 / 2 | 6 | 60 | trigger_event(4312); stop |
| 9 | 4312 | 43 / 3 | 6 | 60 | set_switch(15); set_switch(16); set_switch(17); set_switch(18); set_switch(19); set_switch(20); set_switch(21); set_switch(22); set_switch(23); set_switch(24); stop |
| 9 | 801 | 80 / 1 | 2 | 1 | trigger_event(8011); stop |
| 9 | 8011 | 80 / 2 | 6 | 35 | trigger_event(8012); stop |
| 9 | 8012 | 80 / 3 | 8 | 50 | trigger_event(8013); stop |
| 9 | 8013 | 80 / 4 | 8 | 15 | trigger_event(8014); stop |
| 9 | 8014 | 80 / 5 | 8 | 1 | trigger_event(8015); stop |
| 9 | 8015 | 80 / 6 | 8 | 60 | trigger_event(8016); stop |
| 9 | 8016 | 80 / 7 | 2 | 20 | trigger_event(8017); stop |
| 9 | 8017 | 80 / 8 | 6 | 15 | trigger_event(8018); stop |
| 9 | 8018 | 80 / 9 | 8 | 55 | trigger_event(8019); stop |
| 9 | 8019 | 80 / 10 | 2 | 55 | trigger_event(80191); stop |
| 9 | 80191 | 80 / 21 | 10 | 30 | trigger_event(80192); stop |
| 9 | 80192 | 80 / 23 | 8 | 23 | trigger_event(80193); stop |
| 9 | 80193 | 80 / 25 | 8 | 30 | trigger_event(80194); stop |
| 9 | 80194 | 80 / 26 | 8 | 30 | stop |
| 9 | 802 | 80 / 11 | 12 | 60 | trigger_event(8021); stop |
| 9 | 8021 | 80 / 12 | 2 | 35 | trigger_event(8022); stop |
| 9 | 8022 | 80 / 13 | 2 | 50 | trigger_event(8023); stop |
| 9 | 8023 | 80 / 14 | 8 | 15 | trigger_event(8024); stop |
| 9 | 8024 | 80 / 15 | 2 | 1 | trigger_event(8025); stop |
| 9 | 8025 | 80 / 16 | 8 | 60 | trigger_event(8026); stop |
| 9 | 8026 | 80 / 17 | 8 | 20 | trigger_event(8027); stop |
| 9 | 8027 | 80 / 18 | 8 | 15 | trigger_event(8028); stop |
| 9 | 8028 | 80 / 19 | 8 | 55 | trigger_event(8029); stop |
| 9 | 8029 | 80 / 20 | 4 | 35 | trigger_event(80291); stop |
| 9 | 80291 | 80 / 22 | 2 | 30 | trigger_event(80292); stop |
| 9 | 80292 | 80 / 24 | 6 | 30 | stop |

## Review notes

- Floor 7: event 2043 targets absent event 2044

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
