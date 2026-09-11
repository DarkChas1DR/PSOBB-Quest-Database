# Edy CUP -Maximum Attack- — maximum-attack-ep1/q142-bb-j

Episode1; header quest ID 142; language J. Static scan: **603 objects, 606 enemy/NPC records, 198 events, 323 script labels.** Script roundtrip: byte-identical.

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
0x00, 0x00, 0x00, 0x00, 0x00
0x02, 0x02, 0x00, 0x00, 0x00
0x05, 0x05, 0x00, 0x03, 0x00
0x06, 0x06, 0x00, 0x03, 0x00
0x07, 0x07, 0x00, 0x04, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 54 | 16 | 0 |
| 2 | 143 | 175 | 78 |
| 5 | 189 | 195 | 44 |
| 6 | 35 | 0 | 0 |
| 7 | 182 | 220 | 76 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 2 | 21 | 2 / 1 | 1 | 1 | trigger_event(211); stop |
| 2 | 211 | 2 / 2 | 1 | 1 | trigger_event(212); stop |
| 2 | 212 | 2 / 3 | 1 | 1 | trigger_event(213); stop |
| 2 | 213 | 2 / 4 | 1 | 1 | trigger_event(214); stop |
| 2 | 214 | 2 / 5 | 1 | 1 | stop |
| 2 | 22 | 2 / 6 | 1 | 1 | trigger_event(221); stop |
| 2 | 221 | 2 / 7 | 1 | 1 | trigger_event(222); stop |
| 2 | 222 | 2 / 8 | 1 | 1 | trigger_event(223); stop |
| 2 | 223 | 2 / 9 | 1 | 1 | trigger_event(224); stop |
| 2 | 224 | 2 / 10 | 1 | 1 | stop |
| 2 | 23 | 2 / 11 | 1 | 1 | trigger_event(231); stop |
| 2 | 231 | 2 / 12 | 1 | 1 | trigger_event(232); stop |
| 2 | 232 | 2 / 13 | 1 | 1 | trigger_event(233); stop |
| 2 | 233 | 2 / 14 | 1 | 1 | trigger_event(234); stop |
| 2 | 234 | 2 / 15 | 1 | 1 | stop |
| 2 | 24 | 2 / 16 | 1 | 1 | trigger_event(241); stop |
| 2 | 241 | 2 / 17 | 1 | 1 | trigger_event(242); stop |
| 2 | 242 | 2 / 18 | 1 | 1 | trigger_event(243); stop |
| 2 | 243 | 2 / 19 | 1 | 1 | trigger_event(244); stop |
| 2 | 244 | 2 / 20 | 1 | 1 | stop |
| 2 | 25 | 2 / 21 | 1 | 1 | trigger_event(251); stop |
| 2 | 251 | 2 / 22 | 1 | 1 | trigger_event(252); stop |
| 2 | 252 | 2 / 23 | 1 | 1 | trigger_event(253); stop |
| 2 | 253 | 2 / 24 | 1 | 1 | trigger_event(254); stop |
| 2 | 254 | 2 / 25 | 1 | 1 | set_switch(1); stop |
| 2 | 26 | 2 / 26 | 1 | 1 | stop |
| 2 | 41 | 4 / 1 | 6 | 1 | trigger_event(411); stop |
| 2 | 411 | 4 / 2 | 6 | 1 | trigger_event(412); stop |
| 2 | 412 | 4 / 3 | 6 | 1 | trigger_event(413); stop |
| 2 | 413 | 4 / 4 | 3 | 1 | stop |
| 2 | 61 | 6 / 1 | 5 | 1 | trigger_event(611); stop |
| 2 | 611 | 6 / 2 | 5 | 1 | trigger_event(612); stop |
| 2 | 612 | 6 / 3 | 6 | 1 | trigger_event(613); stop |
| 2 | 613 | 6 / 4 | 4 | 1 | trigger_event(614); stop |
| 2 | 614 | 6 / 5 | 4 | 1 | trigger_event(615); stop |
| 2 | 615 | 6 / 6 | 3 | 1 | set_switch(2); set_switch(3); stop |
| 2 | 101 | 10 / 1 | 3 | 1 | trigger_event(1011); stop |
| 2 | 1011 | 10 / 2 | 3 | 1 | trigger_event(1012); stop |
| 2 | 1012 | 10 / 3 | 3 | 1 | trigger_event(1013); stop |
| 2 | 1013 | 10 / 4 | 3 | 1 | trigger_event(1014); stop |
| 2 | 1014 | 10 / 5 | 3 | 1 | trigger_event(1015); stop |
| 2 | 1015 | 10 / 6 | 6 | 1 | trigger_event(1016); set_switch(104); stop |
| 2 | 1016 | 10 / 7 | 1 | 150 | stop |
| 2 | 111 | 11 / 1 | 1 | 1 | stop |
| 2 | 112 | 11 / 2 | 1 | 20 | stop |
| 2 | 113 | 11 / 3 | 1 | 40 | stop |
| 2 | 114 | 11 / 4 | 1 | 60 | stop |
| 2 | 115 | 11 / 5 | 1 | 80 | trigger_event(1111); stop |
| 2 | 1111 | 11 / 6 | 4 | 10 | trigger_event(1112); stop |
| 2 | 1112 | 11 / 7 | 4 | 10 | trigger_event(1113); stop |
| 2 | 1113 | 11 / 8 | 4 | 10 | trigger_event(1114); stop |
| 2 | 1114 | 11 / 9 | 6 | 10 | set_switch(4); set_switch(6); set_switch(7); set_switch(8); set_switch(11); stop |
| 2 | 121 | 12 / 1 | 3 | 10 | trigger_event(1211); stop |
| 2 | 1211 | 12 / 2 | 3 | 10 | trigger_event(1212); stop |
| 2 | 1212 | 12 / 3 | 4 | 10 | trigger_event(1213); stop |
| 2 | 1213 | 12 / 4 | 5 | 10 | trigger_event(1214); stop |
| 2 | 1214 | 12 / 5 | 4 | 10 | set_switch(10); stop |
| 2 | 131 | 13 / 1 | 5 | 1 | trigger_event(1311); stop |
| 2 | 1311 | 13 / 2 | 6 | 1 | trigger_event(1312); stop |
| 2 | 1312 | 13 / 3 | 3 | 1 | trigger_event(1313); stop |
| 2 | 1313 | 13 / 4 | 6 | 1 | set_switch(9); stop |
| 2 | 151 | 15 / 1 | 1 | 70 | trigger_event(1511); trigger_event(1526); trigger_event(1531); trigger_event(15416); stop |
| 2 | 1511 | 15 / 2 | 1 | 1 | trigger_event(1512); stop |
| 2 | 1512 | 15 / 3 | 1 | 1 | trigger_event(1513); stop |
| 2 | 1513 | 15 / 4 | 1 | 1 | trigger_event(1514); stop |
| 2 | 1514 | 15 / 5 | 1 | 1 | stop |
| 2 | 1526 | 15 / 6 | 1 | 1 | trigger_event(1527); stop |
| 2 | 1527 | 15 / 7 | 1 | 1 | trigger_event(1528); stop |
| 2 | 1528 | 15 / 8 | 1 | 1 | trigger_event(1529); stop |
| 2 | 1529 | 15 / 9 | 1 | 1 | stop |
| 2 | 1531 | 15 / 10 | 1 | 1 | trigger_event(1532); stop |
| 2 | 1532 | 15 / 11 | 1 | 1 | trigger_event(1533); stop |
| 2 | 1533 | 15 / 12 | 1 | 1 | trigger_event(1534); stop |
| 2 | 1534 | 15 / 13 | 1 | 1 | stop |
| 2 | 15416 | 15 / 14 | 1 | 1 | trigger_event(15417); stop |
| 2 | 15417 | 15 / 15 | 1 | 1 | trigger_event(15418); stop |
| 2 | 15418 | 15 / 16 | 1 | 1 | trigger_event(15419); stop |
| 2 | 15419 | 15 / 17 | 1 | 1 | set_switch(106); stop |
| 5 | 201 | 20 / 1 | 4 | 10 | trigger_event(2011); stop |
| 5 | 2011 | 20 / 2 | 4 | 10 | set_switch(16); set_switch(17); set_switch(18); set_switch(19); set_switch(20); set_switch(21); stop |
| 5 | 211 | 21 / 1 | 4 | 10 | trigger_event(2111); stop |
| 5 | 2111 | 21 / 2 | 6 | 10 | set_switch(14); set_switch(15); set_switch(16); set_switch(17); set_switch(18); set_switch(19); stop |
| 5 | 301 | 30 / 1 | 5 | 10 | trigger_event(3011); stop |
| 5 | 3011 | 30 / 2 | 6 | 10 | set_switch(11); stop |
| 5 | 311 | 31 / 1 | 5 | 10 | trigger_event(3111); stop |
| 5 | 3111 | 31 / 2 | 6 | 10 | trigger_event(3112); stop |
| 5 | 3112 | 31 / 3 | 4 | 10 | set_switch(31); set_switch(32); set_switch(33); stop |
| 5 | 321 | 32 / 1 | 4 | 10 | trigger_event(3211); stop |
| 5 | 3211 | 32 / 2 | 4 | 10 | trigger_event(3212); stop |
| 5 | 3212 | 32 / 3 | 4 | 10 | set_switch(4); set_switch(5); set_switch(6); set_switch(7); set_switch(14); set_switch(15); stop |
| 5 | 331 | 33 / 1 | 2 | 10 | set_switch(26); set_switch(27); stop |
| 5 | 411 | 41 / 1 | 4 | 60 | trigger_event(4111); stop |
| 5 | 4111 | 41 / 2 | 4 | 10 | trigger_event(4112); stop |
| 5 | 4112 | 41 / 3 | 8 | 10 | trigger_event(4113); stop |
| 5 | 4113 | 41 / 4 | 6 | 10 | set_switch(20); set_switch(21); set_switch(22); set_switch(23); set_switch(29); set_switch(30); stop |
| 5 | 501 | 50 / 1 | 1 | 1 | stop |
| 5 | 502 | 50 / 2 | 4 | 1 | trigger_event(5022); stop |
| 5 | 5022 | 50 / 3 | 6 | 10 | trigger_event(5023); stop |
| 5 | 5023 | 50 / 4 | 3 | 10 | set_switch(9); set_switch(10); set_switch(36); set_switch(14); set_switch(15); stop |
| 5 | 511 | 51 / 1 | 1 | 1 | trigger_event(5111); stop |
| 5 | 5111 | 51 / 2 | 4 | 10 | trigger_event(5112); stop |
| 5 | 5112 | 51 / 3 | 6 | 10 | set_switch(22); set_switch(23); set_switch(24); set_switch(25); set_switch(26); stop |
| 5 | 521 | 52 / 1 | 3 | 10 | trigger_event(5211); stop |
| 5 | 5211 | 52 / 2 | 4 | 10 | trigger_event(5212); stop |
| 5 | 5212 | 52 / 3 | 4 | 10 | trigger_event(5213); stop |
| 5 | 5213 | 52 / 4 | 6 | 10 | trigger_event(5214); stop |
| 5 | 5214 | 52 / 5 | 3 | 10 | set_switch(34); stop |
| 5 | 531 | 53 / 1 | 2 | 10 | set_switch(3); stop |
| 5 | 701 | 70 / 1 | 6 | 90 | trigger_event(7011); stop |
| 5 | 7011 | 70 / 2 | 6 | 10 | trigger_event(7012); stop |
| 5 | 7012 | 70 / 3 | 8 | 10 | trigger_event(7013); stop |
| 5 | 7013 | 70 / 4 | 0 | 10 | set_switch(12); stop |
| 5 | 711 | 71 / 1 | 5 | 1 | trigger_event(7111); stop |
| 5 | 7111 | 71 / 2 | 4 | 10 | set_switch(2); stop |
| 5 | 721 | 72 / 1 | 4 | 90 | trigger_event(7211); stop |
| 5 | 7211 | 72 / 2 | 6 | 10 | set_switch(27); stop |
| 5 | 731 | 73 / 1 | 5 | 1 | trigger_event(7311); stop |
| 5 | 7311 | 73 / 2 | 5 | 10 | trigger_event(7312); stop |
| 5 | 7312 | 73 / 3 | 5 | 10 | trigger_event(7313); stop |
| 5 | 7313 | 73 / 4 | 4 | 10 | trigger_event(7314); stop |
| 5 | 7314 | 73 / 5 | 6 | 10 | trigger_event(7315); stop |
| 5 | 7315 | 73 / 6 | 4 | 10 | set_switch(35); stop |
| 7 | 201 | 20 / 1 | 1 | 1 | trigger_event(2011); stop |
| 7 | 2011 | 20 / 2 | 1 | 1 | trigger_event(2012); stop |
| 7 | 2012 | 20 / 3 | 1 | 1 | trigger_event(2013); stop |
| 7 | 2013 | 20 / 4 | 1 | 1 | stop |
| 7 | 202 | 20 / 5 | 1 | 1 | trigger_event(2021); stop |
| 7 | 2021 | 20 / 6 | 1 | 1 | trigger_event(2022); stop |
| 7 | 2022 | 20 / 7 | 1 | 1 | trigger_event(2023); stop |
| 7 | 2023 | 20 / 8 | 1 | 1 | stop |
| 7 | 203 | 20 / 9 | 1 | 1 | trigger_event(2031); stop |
| 7 | 2031 | 20 / 10 | 1 | 1 | trigger_event(2032); stop |
| 7 | 2032 | 20 / 11 | 1 | 1 | trigger_event(2033); stop |
| 7 | 2033 | 20 / 12 | 1 | 1 | stop |
| 7 | 204 | 20 / 13 | 1 | 1 | trigger_event(2041); stop |
| 7 | 2041 | 20 / 14 | 1 | 1 | trigger_event(2042); stop |
| 7 | 2042 | 20 / 15 | 1 | 1 | trigger_event(2043); stop |
| 7 | 2043 | 20 / 16 | 1 | 1 | trigger_event(2044); stop |
| 7 | 205 | 20 / 17 | 1 | 1 | trigger_event(2051); stop |
| 7 | 2051 | 20 / 18 | 1 | 1 | trigger_event(2052); stop |
| 7 | 2052 | 20 / 19 | 1 | 1 | trigger_event(2053); stop |
| 7 | 2053 | 20 / 20 | 1 | 1 | set_switch(9); stop |
| 7 | 401 | 40 / 1 | 1 | 1 | trigger_event(4011); stop |
| 7 | 4011 | 40 / 2 | 1 | 1 | trigger_event(4012); stop |
| 7 | 4012 | 40 / 3 | 1 | 1 | stop |
| 7 | 402 | 40 / 5 | 1 | 1 | trigger_event(4021); stop |
| 7 | 4021 | 40 / 6 | 1 | 1 | trigger_event(4022); stop |
| 7 | 4022 | 40 / 7 | 1 | 1 | stop |
| 7 | 403 | 40 / 9 | 1 | 1 | trigger_event(4031); stop |
| 7 | 4031 | 40 / 10 | 1 | 1 | trigger_event(4032); stop |
| 7 | 4032 | 40 / 11 | 1 | 1 | stop |
| 7 | 404 | 40 / 13 | 1 | 1 | trigger_event(4041); stop |
| 7 | 4041 | 40 / 14 | 1 | 1 | trigger_event(4042); stop |
| 7 | 4042 | 40 / 15 | 1 | 1 | stop |
| 7 | 405 | 40 / 17 | 0 | 1 | trigger_event(4051); stop |
| 7 | 4051 | 40 / 18 | 0 | 1 | trigger_event(4052); stop |
| 7 | 4052 | 40 / 19 | 0 | 1 | set_switch(2); set_switch(22); stop |
| 7 | 411 | 41 / 1 | 2 | 1 | stop |
| 7 | 412 | 41 / 2 | 2 | 1 | stop |
| 7 | 413 | 41 / 3 | 2 | 1 | trigger_event(4131); stop |
| 7 | 4131 | 41 / 4 | 8 | 1 | trigger_event(4132); stop |
| 7 | 4132 | 41 / 5 | 1 | 1 | trigger_event(4133); stop |
| 7 | 4133 | 41 / 6 | 4 | 1 | set_switch(6); stop |
| 7 | 501 | 50 / 1 | 6 | 1 | trigger_event(5011); stop |
| 7 | 5011 | 50 / 2 | 6 | 1 | trigger_event(5012); stop |
| 7 | 5012 | 50 / 3 | 6 | 1 | trigger_event(5013); stop |
| 7 | 5013 | 50 / 4 | 6 | 1 | trigger_event(5014); stop |
| 7 | 5014 | 50 / 5 | 4 | 600 | trigger_event(5015); stop |
| 7 | 5015 | 50 / 6 | 4 | 10 | set_switch(3); set_switch(14); set_switch(15); set_switch(16); set_switch(17); set_switch(18); stop |
| 7 | 511 | 51 / 1 | 5 | 1 | trigger_event(5111); stop |
| 7 | 5111 | 51 / 2 | 8 | 1 | trigger_event(5112); stop |
| 7 | 5112 | 51 / 3 | 4 | 1 | trigger_event(5113); stop |
| 7 | 5113 | 51 / 4 | 4 | 1 | trigger_event(5114); stop |
| 7 | 5114 | 51 / 5 | 4 | 1 | trigger_event(5115); trigger_event(5118); trigger_event(51111); stop |
| 7 | 5115 | 51 / 6 | 2 | 1 | trigger_event(5116); stop |
| 7 | 5116 | 51 / 7 | 2 | 1 | stop |
| 7 | 5118 | 51 / 8 | 2 | 1 | trigger_event(5119); stop |
| 7 | 5119 | 51 / 9 | 2 | 1 | stop |
| 7 | 51111 | 51 / 10 | 1 | 1 | trigger_event(51112); stop |
| 7 | 51112 | 51 / 11 | 1 | 1 | set_switch(10); stop |
| 7 | 521 | 52 / 1 | 7 | 1 | trigger_event(5211); stop |
| 7 | 5211 | 52 / 2 | 6 | 1 | trigger_event(5212); stop |
| 7 | 5212 | 52 / 3 | 8 | 1 | trigger_event(5213); stop |
| 7 | 5213 | 52 / 4 | 4 | 1 | set_switch(21); set_switch(22); stop |
| 7 | 601 | 60 / 1 | 6 | 1 | trigger_event(6011); stop |
| 7 | 6011 | 60 / 2 | 6 | 1 | trigger_event(6012); stop |
| 7 | 6012 | 60 / 3 | 4 | 1 | trigger_event(6013); stop |
| 7 | 6013 | 60 / 4 | 3 | 1 | set_switch(11); set_switch(12); set_switch(7); set_switch(8); stop |
| 7 | 611 | 61 / 1 | 6 | 1 | trigger_event(6111); stop |
| 7 | 6111 | 61 / 2 | 2 | 1 | trigger_event(6112); stop |
| 7 | 6112 | 61 / 3 | 8 | 1 | trigger_event(6113); stop |
| 7 | 6113 | 61 / 4 | 8 | 1 | trigger_event(6114); stop |
| 7 | 6114 | 61 / 5 | 4 | 1 | set_switch(1); set_switch(2); set_switch(3); set_switch(4); set_switch(15); stop |
| 7 | 701 | 70 / 1 | 1 | 1 | trigger_event(7011); stop |
| 7 | 7011 | 70 / 2 | 6 | 1 | trigger_event(7012); stop |
| 7 | 7012 | 70 / 3 | 6 | 1 | trigger_event(7013); stop |
| 7 | 7013 | 70 / 4 | 6 | 1 | trigger_event(7014); stop |
| 7 | 7014 | 70 / 5 | 8 | 1 | set_switch(14); set_switch(13); stop |

## Review notes

- Floor 7: event 2043 targets absent event 2044

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
