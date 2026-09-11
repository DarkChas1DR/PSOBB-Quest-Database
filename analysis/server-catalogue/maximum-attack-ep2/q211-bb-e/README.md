# Maximum Attack 2 — maximum-attack-ep2/q211-bb-e

Episode2; header quest ID 211; language E. Static scan: **871 objects, 865 enemy/NPC records, 327 events, 493 script labels.** Script roundtrip: byte-identical.

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
0x00, 0x12, 0x00, 0x00, 0x00
0x02, 0x14, 0x00, 0x00, 0x00
0x03, 0x15, 0x00, 0x01, 0x00
0x06, 0x18, 0x00, 0x00, 0x00
0x07, 0x19, 0x00, 0x00, 0x00
0x08, 0x1A, 0x00, 0x00, 0x00
0x09, 0x1B, 0x00, 0x00, 0x00
0x05, 0x17, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 67 | 22 | 0 |
| 2 | 122 | 141 | 41 |
| 3 | 134 | 176 | 56 |
| 5 | 88 | 126 | 56 |
| 6 | 78 | 62 | 55 |
| 7 | 71 | 95 | 34 |
| 8 | 199 | 128 | 43 |
| 9 | 112 | 115 | 42 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 2 | 101 | 10 / 1 | 8 | 10 | trigger_event(1011); stop |
| 2 | 1011 | 10 / 2 | 8 | 10 | trigger_event(1012); stop |
| 2 | 1012 | 10 / 3 | 8 | 10 | set_switch(40); stop |
| 2 | 111 | 11 / 1 | 3 | 10 | trigger_event(111011); trigger_event(111021); trigger_event(111031); stop |
| 2 | 111011 | 11 / 2 | 1 | 100 | trigger_event(111012); stop |
| 2 | 111012 | 11 / 3 | 1 | 100 | trigger_event(111013); stop |
| 2 | 111013 | 11 / 4 | 1 | 100 | trigger_event(111014); stop |
| 2 | 111014 | 11 / 5 | 1 | 100 | set_switch(3); set_switch(4); stop |
| 2 | 111021 | 11 / 6 | 1 | 30 | trigger_event(111022); stop |
| 2 | 111022 | 11 / 7 | 1 | 30 | trigger_event(111023); stop |
| 2 | 111023 | 11 / 8 | 1 | 30 | stop |
| 2 | 111031 | 11 / 9 | 1 | 60 | trigger_event(111032); stop |
| 2 | 111032 | 11 / 10 | 1 | 60 | trigger_event(111033); stop |
| 2 | 111033 | 11 / 11 | 1 | 60 | stop |
| 2 | 201 | 20 / 1 | 4 | 10 | trigger_event(2011); stop |
| 2 | 2011 | 20 / 2 | 4 | 10 | trigger_event(2012); stop |
| 2 | 2012 | 20 / 3 | 4 | 10 | set_switch(41); stop |
| 2 | 301 | 30 / 1 | 4 | 10 | set_switch(34); set_switch(35); stop |
| 2 | 401 | 40 / 1 | 5 | 10 | trigger_event(4011); stop |
| 2 | 4011 | 40 / 2 | 5 | 100 | trigger_event(4012); stop |
| 2 | 4012 | 40 / 3 | 5 | 200 | set_switch(1); set_switch(2); stop |
| 2 | 501 | 50 / 1 | 5 | 10 | trigger_event(5011); stop |
| 2 | 5011 | 50 / 2 | 5 | 10 | trigger_event(5012); stop |
| 2 | 5012 | 50 / 3 | 5 | 150 | trigger_event(5013); set_switch(5); set_switch(6); set_switch(7); set_switch(8); set_switch(9); set_switch(10); set_switch(11); set_switch(14); set_switch(15); set_switch(16); set_switch(17); set_switch(18); set_switch(19); set_switch(20); set_switch(21); set_switch(22); set_switch(23); set_switch(24); set_switch(25); set_switch(26); set_switch(27); set_switch(28); set_switch(29); set_switch(30); set_switch(31); set_switch(32); set_switch(33); set_switch(48); set_switch(45); set_switch(48); set_switch(49); set_switch(50); set_switch(51); stop |
| 2 | 5013 | 50 / 4 | 5 | 350 | stop |
| 2 | 601 | 60 / 1 | 1 | 10 | trigger_event(6011); stop |
| 2 | 6011 | 60 / 2 | 3 | 10 | trigger_event(6012); stop |
| 2 | 6012 | 60 / 3 | 6 | 100 | trigger_event(6013); stop |
| 2 | 6013 | 60 / 4 | 3 | 200 | set_switch(36); set_switch(37); set_switch(38); set_switch(39); stop |
| 2 | 701 | 70 / 1 | 5 | 10 | trigger_event(7011); stop |
| 2 | 7011 | 70 / 2 | 5 | 100 | trigger_event(7012); stop |
| 2 | 7012 | 70 / 3 | 2 | 10 | trigger_event(7013); set_switch(42); stop |
| 2 | 7013 | 70 / 4 | 6 | 300 | set_switch(46); set_switch(47); stop |
| 2 | 702 | 70 / 5 | 2 | 10 | trigger_event(7021); stop |
| 2 | 7021 | 70 / 6 | 3 | 150 | trigger_event(7022); stop |
| 2 | 7022 | 70 / 7 | 4 | 300 | set_switch(43); set_switch(44); stop |
| 2 | 911 | 91 / 1 | 3 | 10 | stop |
| 2 | 921 | 92 / 1 | 3 | 10 | stop |
| 2 | 931 | 93 / 1 | 3 | 10 | stop |
| 2 | 941 | 94 / 1 | 3 | 10 | stop |
| 2 | 1501 | 150 / 1 | 1 | 10 | stop |
| 3 | 101 | 10 / 1 | 6 | 10 | trigger_event(1011); stop |
| 3 | 1011 | 10 / 2 | 6 | 150 | trigger_event(1012); stop |
| 3 | 1012 | 10 / 3 | 5 | 10 | set_switch(5); set_switch(6); stop |
| 3 | 102 | 10 / 4 | 1 | 600 | stop |
| 3 | 121 | 12 / 1 | 1 | 300 | trigger_event(1211); stop |
| 3 | 1211 | 12 / 2 | 3 | 10 | trigger_event(1212); stop |
| 3 | 1212 | 12 / 3 | 4 | 300 | set_switch(19); set_switch(23); set_switch(25); stop |
| 3 | 201 | 20 / 1 | 3 | 10 | trigger_event(2011); stop |
| 3 | 2011 | 20 / 2 | 5 | 150 | trigger_event(2012); stop |
| 3 | 2012 | 20 / 3 | 6 | 10 | trigger_event(2013); stop |
| 3 | 2013 | 20 / 4 | 6 | 100 | trigger_event(2014); stop |
| 3 | 2014 | 20 / 5 | 8 | 150 | set_switch(3); set_switch(4); stop |
| 3 | 211 | 21 / 1 | 3 | 10 | trigger_event(2111); stop |
| 3 | 2111 | 21 / 2 | 3 | 10 | trigger_event(2112); stop |
| 3 | 2112 | 21 / 3 | 2 | 10 | set_switch(20); set_switch(24); set_switch(26); stop |
| 3 | 311 | 31 / 1 | 3 | 10 | trigger_event(311011); trigger_event(311021); trigger_event(311031); trigger_event(311041); trigger_event(311051); stop |
| 3 | 311011 | 31 / 2 | 1 | 10 | trigger_event(311012); stop |
| 3 | 311012 | 31 / 3 | 1 | 10 | trigger_event(311013); stop |
| 3 | 311013 | 31 / 4 | 1 | 10 | trigger_event(311014); stop |
| 3 | 311014 | 31 / 5 | 1 | 150 | set_switch(38); set_switch(41); set_switch(42); stop |
| 3 | 311021 | 31 / 6 | 1 | 10 | trigger_event(311022); stop |
| 3 | 311022 | 31 / 7 | 1 | 10 | trigger_event(311023); stop |
| 3 | 311023 | 31 / 8 | 1 | 10 | stop |
| 3 | 311031 | 31 / 9 | 1 | 10 | trigger_event(311032); stop |
| 3 | 311032 | 31 / 10 | 1 | 10 | trigger_event(311033); stop |
| 3 | 311033 | 31 / 11 | 1 | 10 | stop |
| 3 | 311041 | 31 / 12 | 1 | 10 | trigger_event(311042); stop |
| 3 | 311042 | 31 / 13 | 1 | 10 | trigger_event(311043); stop |
| 3 | 311043 | 31 / 14 | 1 | 10 | stop |
| 3 | 311051 | 31 / 15 | 1 | 10 | trigger_event(311052); stop |
| 3 | 311052 | 31 / 16 | 1 | 10 | trigger_event(311053); stop |
| 3 | 311053 | 31 / 17 | 1 | 10 | stop |
| 3 | 312 | 31 / 18 | 1 | 500 | stop |
| 3 | 401 | 40 / 1 | 4 | 10 | trigger_event(4011); stop |
| 3 | 4011 | 40 / 2 | 5 | 100 | trigger_event(4012); stop |
| 3 | 4012 | 40 / 3 | 8 | 200 | trigger_event(4013); stop |
| 3 | 4013 | 40 / 4 | 6 | 10 | trigger_event(4014); stop |
| 3 | 4014 | 40 / 5 | 3 | 10 | set_switch(7); set_switch(8); set_switch(9); set_switch(10); stop |
| 3 | 411 | 41 / 1 | 3 | 10 | trigger_event(4111); stop |
| 3 | 4111 | 41 / 2 | 6 | 10 | trigger_event(4112); stop |
| 3 | 4112 | 41 / 3 | 6 | 10 | trigger_event(4113); stop |
| 3 | 4113 | 41 / 4 | 4 | 200 | set_switch(33); set_switch(34); stop |
| 3 | 421 | 42 / 1 | 1 | 150 | trigger_event(4211); stop |
| 3 | 4211 | 42 / 2 | 2 | 10 | trigger_event(4212); stop |
| 3 | 4212 | 42 / 3 | 4 | 10 | set_switch(27); set_switch(28); set_switch(29); set_switch(30); set_switch(31); set_switch(32); stop |
| 3 | 501 | 50 / 1 | 5 | 100 | trigger_event(5011); stop |
| 3 | 5011 | 50 / 2 | 6 | 10 | trigger_event(5012); stop |
| 3 | 5012 | 50 / 3 | 5 | 100 | trigger_event(5013); stop |
| 3 | 5013 | 50 / 4 | 5 | 150 | set_switch(35); set_switch(36); set_switch(37); stop |
| 3 | 511 | 51 / 1 | 2 | 200 | trigger_event(5111); stop |
| 3 | 5111 | 51 / 2 | 3 | 10 | trigger_event(5112); stop |
| 3 | 5112 | 51 / 3 | 4 | 10 | trigger_event(5113); stop |
| 3 | 5113 | 51 / 4 | 5 | 300 | set_switch(11); set_switch(12); set_switch(13); set_switch(14); set_switch(15); set_switch(16); stop |
| 3 | 521 | 52 / 1 | 2 | 150 | trigger_event(5211); stop |
| 3 | 5211 | 52 / 2 | 2 | 10 | trigger_event(5212); stop |
| 3 | 5212 | 52 / 3 | 3 | 10 | set_switch(17); set_switch(18); set_switch(21); set_switch(22); stop |
| 5 | 21 | 2 / 1 | 5 | 10 | trigger_event(211); stop |
| 5 | 211 | 2 / 2 | 5 | 10 | trigger_event(212); stop |
| 5 | 212 | 2 / 3 | 5 | 10 | trigger_event(213); stop |
| 5 | 213 | 2 / 4 | 2 | 200 | set_switch(2); stop |
| 5 | 31 | 3 / 1 | 5 | 150 | trigger_event(311); stop |
| 5 | 311 | 3 / 2 | 6 | 10 | trigger_event(312); stop |
| 5 | 312 | 3 / 3 | 6 | 100 | trigger_event(313); stop |
| 5 | 313 | 3 / 4 | 6 | 100 | trigger_event(314); stop |
| 5 | 314 | 3 / 5 | 5 | 10 | set_switch(3); set_switch(4); stop |
| 5 | 51 | 5 / 1 | 2 | 10 | trigger_event(51011); trigger_event(51021); stop |
| 5 | 51011 | 5 / 2 | 1 | 100 | trigger_event(51012); stop |
| 5 | 51012 | 5 / 3 | 1 | 100 | trigger_event(51013); stop |
| 5 | 51013 | 5 / 4 | 1 | 100 | stop |
| 5 | 51021 | 5 / 5 | 2 | 100 | trigger_event(51022); stop |
| 5 | 51022 | 5 / 6 | 2 | 100 | trigger_event(51023); stop |
| 5 | 51023 | 5 / 7 | 2 | 100 | trigger_event(51024); stop |
| 5 | 51024 | 5 / 8 | 2 | 100 | set_switch(5); set_switch(6); stop |
| 5 | 111 | 11 / 1 | 4 | 10 | trigger_event(11011); trigger_event(11021); trigger_event(11031); stop |
| 5 | 11011 | 11 / 2 | 2 | 10 | trigger_event(11012); stop |
| 5 | 11012 | 11 / 3 | 3 | 10 | trigger_event(11013); stop |
| 5 | 11013 | 11 / 4 | 2 | 10 | trigger_event(11014); stop |
| 5 | 11014 | 11 / 5 | 2 | 10 | trigger_event(11015); stop |
| 5 | 11015 | 11 / 6 | 3 | 10 | trigger_event(11016); stop |
| 5 | 11016 | 11 / 7 | 2 | 10 | trigger_event(11017); stop |
| 5 | 11017 | 11 / 8 | 2 | 10 | trigger_event(11018); stop |
| 5 | 11018 | 11 / 9 | 3 | 10 | trigger_event(11019); stop |
| 5 | 11019 | 11 / 10 | 3 | 10 | trigger_event(110110); stop |
| 5 | 110110 | 11 / 29 | 1 | 10 | trigger_event(110111); stop |
| 5 | 110111 | 11 / 30 | 1 | 10 | trigger_event(110112); stop |
| 5 | 110112 | 11 / 31 | 1 | 10 | stop |
| 5 | 11021 | 11 / 11 | 2 | 10 | trigger_event(11022); stop |
| 5 | 11022 | 11 / 12 | 3 | 10 | trigger_event(11023); stop |
| 5 | 11023 | 11 / 13 | 1 | 10 | trigger_event(11024); stop |
| 5 | 11024 | 11 / 14 | 2 | 10 | trigger_event(11025); stop |
| 5 | 11025 | 11 / 15 | 2 | 10 | trigger_event(11026); stop |
| 5 | 11026 | 11 / 16 | 2 | 10 | trigger_event(11027); stop |
| 5 | 11027 | 11 / 17 | 2 | 10 | trigger_event(11028); stop |
| 5 | 11028 | 11 / 18 | 3 | 10 | trigger_event(11029); stop |
| 5 | 11029 | 11 / 19 | 3 | 10 | trigger_event(110210); stop |
| 5 | 110210 | 11 / 32 | 1 | 10 | trigger_event(110211); stop |
| 5 | 110211 | 11 / 33 | 0 | 10 | trigger_event(110212); stop |
| 5 | 110212 | 11 / 34 | 0 | 10 | stop |
| 5 | 11031 | 11 / 20 | 1 | 10 | trigger_event(11032); stop |
| 5 | 11032 | 11 / 21 | 2 | 10 | trigger_event(11033); stop |
| 5 | 11033 | 11 / 22 | 2 | 10 | trigger_event(11034); stop |
| 5 | 11034 | 11 / 23 | 2 | 10 | trigger_event(11035); stop |
| 5 | 11035 | 11 / 24 | 3 | 10 | trigger_event(11036); stop |
| 5 | 11036 | 11 / 25 | 1 | 10 | trigger_event(11037); stop |
| 5 | 11037 | 11 / 26 | 2 | 10 | trigger_event(11038); stop |
| 5 | 11038 | 11 / 27 | 2 | 10 | trigger_event(11039); stop |
| 5 | 11039 | 11 / 28 | 3 | 10 | trigger_event(110310); stop |
| 5 | 110310 | 11 / 35 | 0 | 10 | trigger_event(110311); stop |
| 5 | 110311 | 11 / 36 | 0 | 10 | trigger_event(110312); stop |
| 5 | 110312 | 11 / 37 | 0 | 10 | trigger_event(110313); stop |
| 5 | 110313 | 11 / 38 | 0 | 10 | trigger_event(110314); stop |
| 5 | 110314 | 11 / 39 | 0 | 10 | construct_objects(room=13,group_or_wave=20); set_switch(20); stop |
| 6 | 31 | 3 / 1 | 1 | 100 | trigger_event(311); stop |
| 6 | 311 | 3 / 2 | 3 | 300 | set_switch(5); set_switch(8); set_switch(12); stop |
| 6 | 32 | 3 / 3 | 1 | 300 | trigger_event(321); stop |
| 6 | 321 | 3 / 4 | 1 | 10 | trigger_event(322); stop |
| 6 | 322 | 3 / 5 | 1 | 10 | trigger_event(323); stop |
| 6 | 323 | 3 / 6 | 1 | 10 | trigger_event(324); stop |
| 6 | 324 | 3 / 7 | 1 | 10 | stop |
| 6 | 33 | 3 / 8 | 1 | 300 | trigger_event(331); stop |
| 6 | 331 | 3 / 9 | 1 | 10 | trigger_event(332); stop |
| 6 | 332 | 3 / 10 | 1 | 10 | trigger_event(333); stop |
| 6 | 333 | 3 / 11 | 1 | 10 | trigger_event(334); stop |
| 6 | 334 | 3 / 12 | 1 | 10 | stop |
| 6 | 34 | 3 / 13 | 1 | 300 | trigger_event(341); stop |
| 6 | 341 | 3 / 14 | 1 | 10 | trigger_event(342); stop |
| 6 | 342 | 3 / 15 | 1 | 10 | trigger_event(343); stop |
| 6 | 343 | 3 / 16 | 1 | 10 | trigger_event(344); stop |
| 6 | 344 | 3 / 17 | 1 | 10 | stop |
| 6 | 41 | 4 / 1 | 1 | 100 | trigger_event(411); stop |
| 6 | 411 | 4 / 2 | 2 | 300 | set_switch(4); set_switch(7); set_switch(9); set_switch(10); set_switch(11); set_switch(14); set_switch(15); stop |
| 6 | 42 | 4 / 3 | 1 | 300 | trigger_event(421); stop |
| 6 | 421 | 4 / 4 | 1 | 10 | trigger_event(422); stop |
| 6 | 422 | 4 / 5 | 1 | 10 | trigger_event(423); stop |
| 6 | 423 | 4 / 6 | 1 | 10 | trigger_event(424); stop |
| 6 | 424 | 4 / 7 | 1 | 10 | stop |
| 6 | 43 | 4 / 8 | 1 | 300 | trigger_event(431); stop |
| 6 | 431 | 4 / 9 | 1 | 10 | trigger_event(432); stop |
| 6 | 432 | 4 / 10 | 1 | 10 | trigger_event(433); stop |
| 6 | 433 | 4 / 11 | 1 | 10 | trigger_event(434); stop |
| 6 | 434 | 4 / 12 | 1 | 10 | stop |
| 6 | 44 | 4 / 13 | 1 | 300 | trigger_event(441); stop |
| 6 | 441 | 4 / 14 | 1 | 10 | trigger_event(442); stop |
| 6 | 442 | 4 / 15 | 1 | 10 | trigger_event(443); stop |
| 6 | 443 | 4 / 16 | 1 | 10 | trigger_event(444); stop |
| 6 | 444 | 4 / 17 | 1 | 10 | stop |
| 6 | 111 | 11 / 1 | 1 | 100 | trigger_event(1111); stop |
| 6 | 1111 | 11 / 2 | 3 | 300 | set_switch(3); set_switch(6); stop |
| 6 | 112 | 11 / 3 | 1 | 300 | trigger_event(1121); stop |
| 6 | 1121 | 11 / 4 | 1 | 10 | trigger_event(1122); stop |
| 6 | 1122 | 11 / 5 | 1 | 10 | trigger_event(1123); stop |
| 6 | 1123 | 11 / 6 | 1 | 10 | trigger_event(1124); stop |
| 6 | 1124 | 11 / 7 | 1 | 10 | stop |
| 6 | 113 | 11 / 8 | 1 | 300 | trigger_event(1131); stop |
| 6 | 1131 | 11 / 9 | 1 | 10 | trigger_event(1132); stop |
| 6 | 1132 | 11 / 10 | 1 | 10 | trigger_event(1133); stop |
| 6 | 1133 | 11 / 11 | 1 | 10 | trigger_event(1134); stop |
| 6 | 1134 | 11 / 12 | 1 | 10 | stop |
| 6 | 114 | 11 / 13 | 1 | 300 | trigger_event(1141); stop |
| 6 | 1141 | 11 / 14 | 1 | 10 | trigger_event(1142); stop |
| 6 | 1142 | 11 / 15 | 1 | 10 | trigger_event(1143); stop |
| 6 | 1143 | 11 / 16 | 1 | 10 | trigger_event(1144); stop |
| 6 | 1144 | 11 / 17 | 1 | 10 | stop |
| 6 | 151 | 15 / 1 | 1 | 150 | trigger_event(1511); stop |
| 6 | 1511 | 15 / 2 | 1 | 150 | trigger_event(1512); stop |
| 6 | 1512 | 15 / 3 | 1 | 150 | trigger_event(1513); stop |
| 6 | 1513 | 15 / 4 | 3 | 300 | set_switch(1); set_switch(2); stop |
| 7 | 31 | 3 / 1 | 2 | 150 | trigger_event(311); stop |
| 7 | 311 | 3 / 2 | 6 | 10 | trigger_event(312); stop |
| 7 | 312 | 3 / 3 | 5 | 100 | trigger_event(313); stop |
| 7 | 313 | 3 / 4 | 6 | 10 | set_switch(4); set_switch(5); stop |
| 7 | 51 | 5 / 1 | 3 | 10 | construct_objects(room=5,group_or_wave=1); trigger_event(51011); trigger_event(51021); trigger_event(51031); trigger_event(51041); trigger_event(51051); trigger_event(51061); stop |
| 7 | 51011 | 5 / 2 | 1 | 150 | stop |
| 7 | 51021 | 5 / 3 | 1 | 300 | stop |
| 7 | 51031 | 5 / 4 | 1 | 450 | set_switch(6); set_switch(7); set_switch(102); stop |
| 7 | 51041 | 5 / 5 | 1 | 10 | trigger_event(51042); stop |
| 7 | 51042 | 5 / 6 | 1 | 10 | trigger_event(51043); stop |
| 7 | 51043 | 5 / 7 | 1 | 10 | trigger_event(51044); stop |
| 7 | 51044 | 5 / 8 | 1 | 10 | trigger_event(51045); stop |
| 7 | 51045 | 5 / 9 | 1 | 10 | stop |
| 7 | 51051 | 5 / 10 | 1 | 10 | trigger_event(51052); stop |
| 7 | 51052 | 5 / 11 | 1 | 10 | trigger_event(51053); stop |
| 7 | 51053 | 5 / 12 | 1 | 10 | trigger_event(51054); stop |
| 7 | 51054 | 5 / 13 | 1 | 10 | trigger_event(51055); stop |
| 7 | 51055 | 5 / 14 | 1 | 10 | stop |
| 7 | 51061 | 5 / 15 | 1 | 10 | trigger_event(51062); stop |
| 7 | 51062 | 5 / 16 | 1 | 10 | trigger_event(51063); stop |
| 7 | 51063 | 5 / 17 | 1 | 10 | trigger_event(51064); stop |
| 7 | 51064 | 5 / 18 | 1 | 10 | trigger_event(51065); stop |
| 7 | 51065 | 5 / 19 | 1 | 10 | stop |
| 7 | 71 | 7 / 1 | 5 | 10 | trigger_event(711); stop |
| 7 | 711 | 7 / 2 | 4 | 10 | trigger_event(712); stop |
| 7 | 712 | 7 / 3 | 5 | 10 | trigger_event(713); stop |
| 7 | 713 | 7 / 4 | 5 | 10 | trigger_event(714); stop |
| 7 | 714 | 7 / 5 | 6 | 10 | trigger_event(715); stop |
| 7 | 715 | 7 / 6 | 1 | 1000 | stop |
| 7 | 81 | 8 / 1 | 5 | 10 | trigger_event(811); stop |
| 7 | 811 | 8 / 2 | 5 | 10 | trigger_event(812); stop |
| 7 | 812 | 8 / 3 | 6 | 100 | trigger_event(813); stop |
| 7 | 813 | 8 / 4 | 6 | 100 | trigger_event(814); stop |
| 7 | 814 | 8 / 5 | 7 | 10 | stop |
| 8 | 21 | 2 / 1 | 1 | 10 | set_switch(1); set_switch(102); stop |
| 8 | 22 | 2 / 2 | 2 | 100 | stop |
| 8 | 31 | 3 / 1 | 3 | 100 | trigger_event(311); stop |
| 8 | 311 | 3 / 2 | 3 | 10 | trigger_event(312); stop |
| 8 | 312 | 3 / 3 | 3 | 100 | trigger_event(313); stop |
| 8 | 313 | 3 / 4 | 4 | 10 | trigger_event(314); stop |
| 8 | 314 | 3 / 5 | 2 | 100 | trigger_event(315); stop |
| 8 | 315 | 3 / 6 | 3 | 10 | trigger_event(316); stop |
| 8 | 316 | 3 / 7 | 4 | 150 | set_switch(2); set_switch(4); stop |
| 8 | 32 | 3 / 8 | 2 | 10 | trigger_event(321); stop |
| 8 | 321 | 3 / 9 | 3 | 100 | trigger_event(322); stop |
| 8 | 322 | 3 / 10 | 2 | 10 | trigger_event(323); stop |
| 8 | 323 | 3 / 11 | 3 | 100 | trigger_event(324); stop |
| 8 | 324 | 3 / 12 | 2 | 10 | trigger_event(325); stop |
| 8 | 325 | 3 / 13 | 2 | 10 | stop |
| 8 | 33 | 3 / 14 | 3 | 10 | stop |
| 8 | 41 | 4 / 1 | 4 | 200 | trigger_event(411); stop |
| 8 | 411 | 4 / 2 | 5 | 10 | trigger_event(412); stop |
| 8 | 412 | 4 / 3 | 6 | 10 | trigger_event(413); stop |
| 8 | 413 | 4 / 4 | 5 | 100 | set_switch(3); set_switch(7); set_switch(18); stop |
| 8 | 51 | 5 / 1 | 5 | 10 | trigger_event(511); stop |
| 8 | 511 | 5 / 2 | 5 | 10 | trigger_event(512); stop |
| 8 | 512 | 5 / 3 | 6 | 10 | trigger_event(513); stop |
| 8 | 513 | 5 / 4 | 6 | 100 | trigger_event(514); stop |
| 8 | 514 | 5 / 5 | 8 | 10 | set_switch(11); stop |
| 8 | 81 | 8 / 1 | 3 | 10 | trigger_event(81011); trigger_event(81021); stop |
| 8 | 81011 | 8 / 2 | 3 | 10 | trigger_event(81012); stop |
| 8 | 81012 | 8 / 3 | 4 | 100 | trigger_event(81013); stop |
| 8 | 81013 | 8 / 4 | 3 | 10 | trigger_event(81014); stop |
| 8 | 81014 | 8 / 5 | 4 | 150 | set_switch(8); set_switch(9); set_switch(10); set_switch(12); set_switch(13); set_switch(14); stop |
| 8 | 81021 | 8 / 6 | 3 | 10 | trigger_event(81022); stop |
| 8 | 81022 | 8 / 7 | 2 | 10 | trigger_event(81023); stop |
| 8 | 81023 | 8 / 8 | 2 | 10 | stop |
| 8 | 82 | 8 / 9 | 3 | 200 | trigger_event(82011); trigger_event(82021); trigger_event(82031); stop |
| 8 | 82011 | 8 / 10 | 1 | 10 | trigger_event(82012); stop |
| 8 | 82012 | 8 / 11 | 1 | 10 | trigger_event(82013); stop |
| 8 | 82013 | 8 / 12 | 1 | 10 | stop |
| 8 | 82021 | 8 / 13 | 1 | 10 | trigger_event(82022); stop |
| 8 | 82022 | 8 / 14 | 1 | 10 | trigger_event(82023); stop |
| 8 | 82023 | 8 / 15 | 1 | 10 | stop |
| 8 | 82031 | 8 / 16 | 1 | 10 | trigger_event(82032); stop |
| 8 | 82032 | 8 / 17 | 1 | 10 | trigger_event(82033); stop |
| 8 | 82033 | 8 / 18 | 1 | 10 | stop |
| 9 | 31 | 3 / 1 | 2 | 10 | trigger_event(311); stop |
| 9 | 311 | 3 / 2 | 3 | 10 | trigger_event(312); stop |
| 9 | 312 | 3 / 3 | 2 | 10 | trigger_event(313); stop |
| 9 | 313 | 3 / 4 | 3 | 10 | trigger_event(314); stop |
| 9 | 314 | 3 / 5 | 3 | 10 | set_switch(1); stop |
| 9 | 32 | 3 / 6 | 3 | 10 | trigger_event(321); stop |
| 9 | 321 | 3 / 7 | 3 | 10 | trigger_event(322); stop |
| 9 | 322 | 3 / 8 | 3 | 10 | trigger_event(323); stop |
| 9 | 323 | 3 / 9 | 3 | 10 | trigger_event(324); stop |
| 9 | 324 | 3 / 10 | 3 | 10 | trigger_event(325); stop |
| 9 | 325 | 3 / 11 | 4 | 10 | stop |
| 9 | 33 | 3 / 12 | 1 | 10 | stop |
| 9 | 71 | 7 / 1 | 3 | 150 | set_switch(2); set_switch(3); set_switch(100); stop |
| 9 | 72 | 7 / 2 | 3 | 300 | trigger_event(72011); trigger_event(72021); trigger_event(72031); stop |
| 9 | 72011 | 7 / 3 | 1 | 10 | trigger_event(72012); stop |
| 9 | 72012 | 7 / 4 | 1 | 10 | trigger_event(72013); stop |
| 9 | 72013 | 7 / 5 | 1 | 10 | trigger_event(72014); stop |
| 9 | 72014 | 7 / 6 | 1 | 10 | stop |
| 9 | 72021 | 7 / 7 | 1 | 10 | trigger_event(72022); stop |
| 9 | 72022 | 7 / 8 | 1 | 10 | trigger_event(72023); stop |
| 9 | 72023 | 7 / 9 | 1 | 10 | trigger_event(72024); stop |
| 9 | 72024 | 7 / 10 | 1 | 10 | stop |
| 9 | 72031 | 7 / 11 | 1 | 10 | trigger_event(72032); stop |
| 9 | 72032 | 7 / 12 | 1 | 10 | trigger_event(72033); stop |
| 9 | 72033 | 7 / 13 | 1 | 10 | trigger_event(72034); stop |
| 9 | 72034 | 7 / 14 | 1 | 10 | stop |
| 9 | 91 | 9 / 1 | 3 | 10 | trigger_event(911); stop |
| 9 | 911 | 9 / 2 | 3 | 10 | trigger_event(912); stop |
| 9 | 912 | 9 / 3 | 3 | 10 | trigger_event(913); stop |
| 9 | 913 | 9 / 4 | 3 | 100 | trigger_event(914); stop |
| 9 | 914 | 9 / 5 | 3 | 10 | trigger_event(915); stop |
| 9 | 915 | 9 / 6 | 4 | 100 | set_switch(4); set_switch(5); stop |
| 9 | 92 | 9 / 7 | 3 | 150 | trigger_event(921); stop |
| 9 | 921 | 9 / 8 | 3 | 100 | trigger_event(922); stop |
| 9 | 922 | 9 / 9 | 2 | 10 | trigger_event(923); stop |
| 9 | 923 | 9 / 10 | 3 | 10 | trigger_event(924); stop |
| 9 | 924 | 9 / 11 | 4 | 150 | stop |
| 9 | 111 | 11 / 1 | 5 | 60 | trigger_event(1111); stop |
| 9 | 1111 | 11 / 2 | 6 | 60 | trigger_event(1112); stop |
| 9 | 1112 | 11 / 3 | 5 | 60 | trigger_event(1113); stop |
| 9 | 1113 | 11 / 4 | 6 | 60 | trigger_event(1114); stop |
| 9 | 1114 | 11 / 5 | 8 | 60 | set_switch(6); set_switch(8); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

A backup is present; decompressed content identical: True. See [text differences](<backup-diff.txt>).

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
