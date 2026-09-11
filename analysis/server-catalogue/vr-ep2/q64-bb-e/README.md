# A New Hope — vr-ep2/q64-bb-e

Episode2; header quest ID 64; language E. Static scan: **635 objects, 775 enemy/NPC records, 227 events, 169 script labels.** Script roundtrip: alignment-only.

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
| 0 | 52 | 24 | 0 |
| 2 | 33 | 424 | 58 |
| 5 | 113 | 29 | 51 |
| 7 | 53 | 78 | 34 |
| 9 | 118 | 118 | 42 |
| 10 | 71 | 73 | 18 |
| 12 | 22 | 1 | 1 |
| 13 | 23 | 1 | 1 |
| 17 | 150 | 27 | 22 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 9 | 31 | 3 / 1 | 0 | 10 | trigger_event(311); stop |
| 9 | 311 | 11 / 4 | 3 | 10 | trigger_event(312); stop |
| 9 | 312 | 11 / 5 | 10 | 10 | trigger_event(1114); stop |
| 9 | 313 | 3 / 4 | 0 | 10 | trigger_event(314); stop |
| 9 | 314 | 7 / 6 | 1 | 10 | set_switch(9); stop |
| 9 | 32 | 3 / 6 | 0 | 10 | trigger_event(321); stop |
| 9 | 321 | 6 / 1 | 0 | 10 | set_switch(1); nop; nop; stop |
| 9 | 322 | 3 / 8 | 0 | 10 | trigger_event(323); stop |
| 9 | 323 | 3 / 9 | 0 | 10 | trigger_event(324); stop |
| 9 | 324 | 3 / 10 | 0 | 10 | trigger_event(325); stop |
| 9 | 325 | 3 / 11 | 0 | 10 | stop |
| 9 | 33 | 3 / 12 | 0 | 10 | stop |
| 9 | 71 | 7 / 1 | 6 | 10 | trigger_event(72); nop; nop; nop; nop; stop |
| 9 | 72 | 7 / 2 | 7 | 10 | trigger_event(72011); trigger_event(72021); trigger_event(72031); stop |
| 9 | 72011 | 7 / 3 | 11 | 10 | trigger_event(72012); stop |
| 9 | 72012 | 7 / 4 | 13 | 10 | trigger_event(72013); stop |
| 9 | 72013 | 7 / 5 | 2 | 10 | trigger_event(314); stop |
| 9 | 72014 | 7 / 6 | 1 | 10 | stop |
| 9 | 72021 | 7 / 7 | 0 | 10 | trigger_event(72022); stop |
| 9 | 72022 | 7 / 8 | 0 | 10 | trigger_event(72023); stop |
| 9 | 72023 | 7 / 9 | 0 | 10 | trigger_event(72024); stop |
| 9 | 72024 | 7 / 10 | 0 | 10 | stop |
| 9 | 72031 | 7 / 11 | 0 | 10 | trigger_event(72032); stop |
| 9 | 72032 | 7 / 12 | 0 | 10 | trigger_event(72033); stop |
| 9 | 72033 | 7 / 13 | 0 | 10 | trigger_event(72034); stop |
| 9 | 72034 | 7 / 14 | 0 | 10 | stop |
| 9 | 91 | 9 / 1 | 6 | 10 | trigger_event(911); stop |
| 9 | 911 | 9 / 2 | 6 | 10 | trigger_event(912); stop |
| 9 | 912 | 9 / 3 | 9 | 10 | trigger_event(913); stop |
| 9 | 913 | 9 / 4 | 9 | 100 | trigger_event(914); stop |
| 9 | 914 | 9 / 5 | 5 | 10 | trigger_event(915); stop |
| 9 | 915 | 9 / 6 | 0 | 100 | set_switch(4); set_switch(5); stop |
| 9 | 92 | 9 / 7 | 0 | 150 | trigger_event(921); stop |
| 9 | 921 | 9 / 8 | 0 | 100 | trigger_event(922); stop |
| 9 | 922 | 9 / 9 | 0 | 10 | trigger_event(923); stop |
| 9 | 923 | 9 / 10 | 0 | 10 | trigger_event(924); stop |
| 9 | 924 | 10 / 1 | 3 | 150 | stop |
| 9 | 111 | 11 / 1 | 5 | 10 | trigger_event(1111); stop |
| 9 | 1111 | 11 / 2 | 8 | 60 | trigger_event(1112); stop |
| 9 | 1112 | 11 / 3 | 8 | 60 | trigger_event(1113); stop |
| 9 | 1113 | 11 / 4 | 3 | 60 | trigger_event(311); stop |
| 9 | 1114 | 11 / 6 | 6 | 60 | set_switch(6); set_switch(8); stop |
| 7 | 31 | 3 / 1 | 8 | 150 | trigger_event(311); stop |
| 7 | 311 | 3 / 2 | 10 | 10 | trigger_event(312); stop |
| 7 | 312 | 3 / 3 | 10 | 100 | trigger_event(313); stop |
| 7 | 313 | 3 / 4 | 2 | 10 | set_switch(4); set_switch(5); stop |
| 7 | 51 | 5 / 1 | 6 | 10 | construct_objects(room=5,group_or_wave=1); trigger_event(51041); nop; nop; nop; nop; nop; nop; nop; nop; nop; nop; nop; nop; nop; nop; nop; nop; nop; nop; nop; nop; nop; nop; nop; nop; nop; stop |
| 7 | 51011 | 5 / 81 | 0 | 150 | stop |
| 7 | 51021 | 5 / 82 | 0 | 300 | stop |
| 7 | 51031 | 5 / 7 | 2 | 450 | set_switch(6); nop; nop; nop; nop; nop; nop; stop |
| 7 | 51041 | 5 / 2 | 10 | 10 | trigger_event(51042); stop |
| 7 | 51042 | 5 / 3 | 7 | 10 | trigger_event(51043); stop |
| 7 | 51043 | 5 / 4 | 1 | 10 | trigger_event(51044); stop |
| 7 | 51044 | 5 / 5 | 1 | 10 | trigger_event(51051); stop |
| 7 | 51045 | 5 / 9 | 0 | 10 | stop |
| 7 | 51051 | 5 / 6 | 1 | 10 | trigger_event(51031); stop |
| 7 | 51052 | 5 / 11 | 0 | 10 | trigger_event(51053); stop |
| 7 | 51053 | 5 / 12 | 0 | 10 | trigger_event(51054); stop |
| 7 | 51054 | 5 / 13 | 0 | 10 | trigger_event(51055); stop |
| 7 | 51055 | 5 / 14 | 0 | 10 | stop |
| 7 | 51061 | 5 / 15 | 0 | 10 | trigger_event(51062); stop |
| 7 | 51062 | 5 / 16 | 0 | 10 | trigger_event(51063); stop |
| 7 | 51063 | 5 / 17 | 0 | 10 | trigger_event(51064); stop |
| 7 | 51064 | 5 / 18 | 0 | 10 | trigger_event(51065); stop |
| 7 | 51065 | 5 / 19 | 0 | 10 | stop |
| 7 | 71 | 2 / 1 | 9 | 10 | trigger_event(711); stop |
| 7 | 711 | 2 / 2 | 8 | 10 | trigger_event(813); stop |
| 7 | 712 | 2 / 3 | 3 | 10 | trigger_event(713); stop |
| 7 | 713 | 2 / 4 | 0 | 10 | trigger_event(714); stop |
| 7 | 714 | 2 / 5 | 0 | 10 | trigger_event(715); stop |
| 7 | 715 | 2 / 6 | 0 | 1000 | stop |
| 7 | 81 | 8 / 1 | 0 | 10 | trigger_event(811); stop |
| 7 | 811 | 8 / 2 | 0 | 10 | trigger_event(812); stop |
| 7 | 812 | 8 / 3 | 0 | 100 | trigger_event(813); stop |
| 7 | 813 | 2 / 3 | 3 | 100 | set_switch(1); stop |
| 7 | 814 | 8 / 5 | 0 | 10 | stop |
| 5 | 211 | 4 / 3 | 3 | 60 | trigger_event(412); stop |
| 5 | 21 | 2 / 1 | 4 | 30 | set_switch(2); stop |
| 5 | 31 | 3 / 1 | 0 | 30 | trigger_event(311); stop |
| 5 | 311 | 3 / 2 | 0 | 30 | set_switch(3); stop |
| 5 | 41 | 4 / 1 | 1 | 60 | trigger_event(411); stop |
| 5 | 411 | 4 / 2 | 2 | 30 | trigger_event(211); stop |
| 5 | 412 | 4 / 4 | 4 | 30 | set_switch(4); stop |
| 5 | 51 | 5 / 1 | 1 | 60 | trigger_event(511); stop |
| 5 | 511 | 5 / 2 | 2 | 30 | trigger_event(512); stop |
| 5 | 512 | 5 / 3 | 3 | 30 | trigger_event(513); stop |
| 5 | 513 | 5 / 4 | 4 | 60 | set_switch(5); nop; nop; stop |
| 5 | 514 | 6 / 1 | 5 | 90 | construct_objects(room=7,group_or_wave=1); stop |
| 5 | 209 | 3 / 1 | 0 | 10 | set_switch(12); nop; nop; stop |
| 5 | 210 | 3 / 1 | 0 | 10 | set_switch(12); stop |
| 5 | 211 | 3 / 1 | 0 | 10 | set_switch(12); nop; nop; stop |
| 5 | 212 | 3 / 1 | 0 | 10 | set_switch(12); nop; nop; stop |
| 5 | 213 | 3 / 1 | 0 | 10 | set_switch(13); stop |
| 5 | 214 | 3 / 1 | 0 | 10 | set_switch(13); nop; nop; stop |
| 5 | 215 | 3 / 1 | 0 | 10 | set_switch(13); nop; nop; stop |
| 5 | 216 | 3 / 1 | 0 | 10 | set_switch(13); nop; nop; stop |
| 5 | 1312 | 13 / 3 | 0 | 60 | construct_objects(room=14,group_or_wave=1); stop |
| 5 | 121 | 12 / 1 | 0 | 30 | set_switch(175); stop |
| 5 | 122 | 12 / 2 | 0 | 30 | set_switch(165); stop |
| 5 | 123 | 12 / 3 | 0 | 30 | set_switch(170); stop |
| 5 | 124 | 12 / 4 | 0 | 30 | set_switch(180); stop |
| 5 | 125 | 12 / 5 | 0 | 180 | set_switch(185); stop |
| 5 | 111 | 11 / 1 | 0 | 30 | trigger_event(1111); stop |
| 5 | 1111 | 11 / 2 | 0 | 30 | trigger_event(1112); stop |
| 5 | 1112 | 11 / 3 | 0 | 60 | trigger_event(1113); stop |
| 5 | 1113 | 11 / 4 | 0 | 30 | trigger_event(1114); stop |
| 5 | 1114 | 11 / 5 | 0 | 60 | trigger_event(1115); stop |
| 5 | 1115 | 11 / 6 | 0 | 30 | trigger_event(1116); stop |
| 5 | 1116 | 11 / 7 | 0 | 90 | trigger_event(1117); stop |
| 5 | 1117 | 11 / 8 | 0 | 30 | trigger_event(1118); stop |
| 5 | 1118 | 11 / 9 | 0 | 60 | trigger_event(1119); stop |
| 5 | 1119 | 11 / 10 | 0 | 60 | trigger_event(11111); stop |
| 5 | 11111 | 11 / 11 | 0 | 30 | trigger_event(11112); stop |
| 5 | 11112 | 11 / 12 | 0 | 30 | trigger_event(11113); stop |
| 5 | 11113 | 11 / 13 | 0 | 30 | trigger_event(11114); stop |
| 5 | 11114 | 11 / 14 | 0 | 60 | trigger_event(11115); stop |
| 5 | 11115 | 11 / 15 | 0 | 90 | trigger_event(11116); stop |
| 5 | 11116 | 11 / 16 | 0 | 60 | trigger_event(11117); stop |
| 5 | 11117 | 11 / 17 | 0 | 30 | set_switch(100); stop |
| 5 | 112 | 11 / 18 | 0 | 60 | trigger_event(1121); stop |
| 5 | 1121 | 11 / 19 | 0 | 150 | trigger_event(1122); stop |
| 5 | 1122 | 11 / 20 | 0 | 150 | trigger_event(1123); stop |
| 5 | 1123 | 11 / 21 | 0 | 150 | trigger_event(1124); stop |
| 5 | 1124 | 11 / 22 | 0 | 60 | set_switch(101); stop |
| 5 | 113 | 11 / 23 | 0 | 60 | trigger_event(1131); stop |
| 5 | 1131 | 11 / 24 | 0 | 90 | trigger_event(1132); stop |
| 5 | 1132 | 11 / 25 | 0 | 120 | construct_objects(room=11,group_or_wave=2); stop |
| 17 | 11 | 1 / 1 | 6 | 180 | set_switch(1); stop |
| 17 | 21 | 2 / 1 | 0 | 10 | set_switch(2); stop |
| 17 | 31 | 3 / 1 | 0 | 10 | trigger_event(311); stop |
| 17 | 311 | 3 / 2 | 0 | 120 | set_switch(5); stop |
| 17 | 41 | 30 / 1 | 2 | 10 | trigger_event(204); stop |
| 17 | 411 | 4 / 2 | 0 | 240 | set_switch(6); stop |
| 17 | 51 | 5 / 1 | 0 | 10 | set_switch(8); stop |
| 17 | 101 | 10 / 1 | 3 | 10 | set_switch(4); stop |
| 17 | 201 | 20 / 1 | 7 | 10 | set_switch(3); stop |
| 17 | 2011 | 1 / 2 | 8 | 10 | stop |
| 17 | 202 | 20 / 2 | 0 | 10 | trigger_event(2021); stop |
| 17 | 2021 | 20 / 6 | 0 | 10 | stop |
| 17 | 203 | 20 / 3 | 0 | 10 | stop |
| 17 | 204 | 30 / 2 | 1 | 10 | construct_objects(room=30,group_or_wave=1); stop |
| 17 | 2041 | 20 / 7 | 0 | 10 | set_switch(3); stop |
| 17 | 211 | 21 / 1 | 0 | 10 | trigger_event(2111); stop |
| 17 | 2111 | 21 / 2 | 0 | 90 | set_switch(7); stop |
| 17 | 221 | 22 / 1 | 0 | 10 | trigger_event(2211); stop |
| 17 | 2211 | 22 / 2 | 0 | 10 | trigger_event(2212); stop |
| 17 | 2212 | 22 / 3 | 0 | 10 | trigger_event(2213); stop |
| 17 | 2213 | 22 / 4 | 0 | 240 | set_switch(9); stop |
| 17 | 301 | 30 / 2 | 1 | 10 | set_switch(10); stop |
| 10 | 301 | 90 / 1 | 2 | 10 | trigger_event(401); stop |
| 10 | 401 | 90 / 2 | 4 | 10 | trigger_event(601); stop |
| 10 | 601 | 90 / 3 | 3 | 10 | set_switch(2); stop |
| 10 | 611 | 90 / 4 | 4 | 10 | set_switch(2); stop |
| 10 | 631 | 80 / 1 | 9 | 154 | trigger_event(701); stop |
| 10 | 701 | 80 / 2 | 6 | 10 | trigger_event(7011); stop |
| 10 | 7011 | 80 / 3 | 2 | 10 | set_switch(3); stop |
| 10 | 7012 | 21 / 1 | 4 | 100 | set_switch(4); stop |
| 10 | 711 | 61 / 1 | 8 | 10 | set_switch(5); stop |
| 10 | 7111 | 70 / 1 | 7 | 10 | trigger_event(7112); stop |
| 10 | 7112 | 70 / 2 | 5 | 10 | trigger_event(801); stop |
| 10 | 801 | 70 / 3 | 3 | 10 | trigger_event(811); stop |
| 10 | 811 | 70 / 4 | 3 | 10 | trigger_event(901); stop |
| 10 | 901 | 70 / 5 | 4 | 10 | trigger_event(2101); stop |
| 10 | 2101 | 70 / 6 | 8 | 10 | set_switch(1); stop |
| 10 | 2102 | 70 / 7 | 1 | 154 | set_switch(1); stop |
| 10 | 2202 | 220 / 1 | 0 | 10 |  |
| 10 | 2522 | 252 / 1 | 0 | 10 |  |
| 2 | 11 | 40 / 1 | 3 | 10 | trigger_event(61); stop |
| 2 | 61 | 40 / 2 | 6 | 10 | trigger_event(201); stop |
| 2 | 201 | 40 / 3 | 9 | 10 | trigger_event(20111); stop |
| 2 | 20111 | 40 / 4 | 12 | 10 | trigger_event(20112); stop |
| 2 | 20112 | 40 / 5 | 15 | 10 | trigger_event(9533); stop |
| 2 | 20113 | 40 / 50 | 3 | 10 | construct_objects(room=40,group_or_wave=1); stop |
| 2 | 301 | 40 / 7 | 6 | 10 | trigger_event(311); stop |
| 2 | 311 | 40 / 8 | 6 | 10 | trigger_event(401); stop |
| 2 | 401 | 40 / 9 | 6 | 10 | trigger_event(4011); stop |
| 2 | 4011 | 40 / 10 | 6 | 10 | trigger_event(501); stop |
| 2 | 501 | 40 / 11 | 6 | 10 | trigger_event(511); stop |
| 2 | 511 | 40 / 12 | 12 | 10 | trigger_event(521); stop |
| 2 | 521 | 40 / 13 | 7 | 10 | trigger_event(531); stop |
| 2 | 531 | 40 / 14 | 7 | 10 | trigger_event(701); stop |
| 2 | 701 | 40 / 15 | 7 | 10 | trigger_event(7011); stop |
| 2 | 7011 | 40 / 16 | 8 | 10 | trigger_event(711); stop |
| 2 | 711 | 40 / 17 | 5 | 10 | trigger_event(7111); stop |
| 2 | 7111 | 40 / 18 | 10 | 10 | trigger_event(7112); stop |
| 2 | 7112 | 40 / 19 | 7 | 10 | trigger_event(2921); stop |
| 2 | 712 | 80 / 4 | 0 | 10 | construct_objects(room=80,group_or_wave=2); stop |
| 2 | 801 | 40 / 21 | 4 | 10 | trigger_event(8011); stop |
| 2 | 8011 | 40 / 22 | 7 | 10 | trigger_event(811); stop |
| 2 | 811 | 40 / 23 | 5 | 10 | trigger_event(8111); stop |
| 2 | 8111 | 40 / 24 | 6 | 10 | trigger_event(8112); stop |
| 2 | 8112 | 40 / 25 | 7 | 10 | trigger_event(901); stop |
| 2 | 901 | 40 / 26 | 6 | 10 | trigger_event(902); stop |
| 2 | 902 | 40 / 27 | 6 | 10 | trigger_event(951); stop |
| 2 | 951 | 40 / 28 | 9 | 10 | trigger_event(9511); stop |
| 2 | 9511 | 40 / 29 | 8 | 10 | trigger_event(9512); stop |
| 2 | 9512 | 40 / 30 | 8 | 10 | trigger_event(9514); stop |
| 2 | 9513 | 40 / 30 | 8 | 10 | trigger_event(9727); stop |
| 2 | 9514 | 40 / 31 | 8 | 10 | trigger_event(9515); stop |
| 2 | 9515 | 40 / 32 | 12 | 10 | trigger_event(9516); stop |
| 2 | 9516 | 40 / 33 | 5 | 10 | trigger_event(9517); stop |
| 2 | 9517 | 40 / 34 | 6 | 10 | trigger_event(9518); stop |
| 2 | 9518 | 40 / 35 | 8 | 10 | trigger_event(9519); stop |
| 2 | 9519 | 40 / 36 | 6 | 10 | trigger_event(952); stop |
| 2 | 952 | 40 / 37 | 6 | 10 | trigger_event(9521); stop |
| 2 | 9521 | 40 / 38 | 7 | 10 | trigger_event(9522); stop |
| 2 | 9522 | 40 / 39 | 9 | 10 | trigger_event(9523); stop |
| 2 | 9523 | 40 / 40 | 7 | 10 | trigger_event(9524); stop |
| 2 | 9524 | 40 / 41 | 9 | 10 | trigger_event(9525); stop |
| 2 | 9525 | 40 / 42 | 7 | 10 | trigger_event(9526); stop |
| 2 | 9526 | 40 / 43 | 8 | 10 | trigger_event(9527); stop |
| 2 | 9527 | 40 / 44 | 6 | 10 | trigger_event(9528); stop |
| 2 | 9528 | 40 / 45 | 12 | 10 | trigger_event(9529); stop |
| 2 | 9529 | 40 / 46 | 16 | 10 | trigger_event(953); stop |
| 2 | 953 | 40 / 47 | 9 | 10 | trigger_event(9531); stop |
| 2 | 9531 | 40 / 48 | 10 | 10 | trigger_event(9532); stop |
| 2 | 9532 | 40 / 49 | 10 | 10 | trigger_event(20113); stop |
| 2 | 9533 | 40 / 6 | 10 | 10 | trigger_event(301); stop |
| 2 | 9534 | 80 / 1 | 13 | 10 | trigger_event(2031); stop |
| 2 | 2031 | 80 / 2 | 12 | 10 | trigger_event(2801); stop |
| 2 | 2111 | 254 / 1 | 0 | 10 | stop |
| 2 | 2121 | 255 / 1 | 0 | 10 | stop |
| 2 | 2122 | 255 / 2 | 0 | 10 | stop |
| 2 | 2801 | 80 / 3 | 13 | 10 | trigger_event(712); stop |
| 2 | 2921 | 40 / 20 | 8 | 10 | trigger_event(801); stop |
| 12 | 1 | 1 / 1 | 1 | 50 | construct_objects(room=1,group_or_wave=1); stop |
| 13 | 1 | 0 / 1 | 1 | 0 | construct_objects(room=1,group_or_wave=1); stop |

## Review notes

- Nonzero data after terminal header
- Floor 2: event 9513 targets absent event 9727
