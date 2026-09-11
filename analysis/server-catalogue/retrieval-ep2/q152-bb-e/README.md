# Lost DEMON\'S RAILGUN — retrieval-ep2/q152-bb-e

Episode2; header quest ID 152; language E. Static scan: **425 objects, 375 enemy/NPC records, 152 events, 52 script labels.** Script roundtrip: byte-identical.

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
| 0 | 38 | 8 | 0 |
| 10 | 173 | 172 | 72 |
| 11 | 183 | 194 | 78 |
| 13 | 31 | 1 | 2 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 10 | 621 | 62 / 1 | 2 | 30 | trigger_event(622); stop |
| 10 | 622 | 62 / 2 | 3 | 30 | set_switch(1); stop |
| 10 | 7101 | 71 / 0 | 0 | 1 | trigger_event(711); trigger_event(717); stop |
| 10 | 711 | 71 / 1 | 2 | 60 | trigger_event(712); stop |
| 10 | 712 | 71 / 2 | 4 | 45 | trigger_event(713); stop |
| 10 | 713 | 71 / 3 | 1 | 50 | trigger_event(714); stop |
| 10 | 714 | 71 / 4 | 4 | 45 | set_switch(2); stop |
| 10 | 717 | 71 / 7 | 1 | 10 | stop |
| 10 | 31 | 3 / 1 | 2 | 30 | trigger_event(715); stop |
| 10 | 715 | 71 / 5 | 1 | 90 | stop |
| 10 | 301 | 30 / 1 | 4 | 5 | trigger_event(302); stop |
| 10 | 302 | 30 / 2 | 2 | 30 | set_switch(3); construct_objects(room=63,group_or_wave=1); stop |
| 10 | 631 | 63 / 1 | 2 | 15 | trigger_event(632); stop |
| 10 | 632 | 63 / 2 | 4 | 50 | set_switch(4); stop |
| 10 | 2631 | 263 / 1 | 1 | 5 | construct_objects(room=264,group_or_wave=1); stop |
| 10 | 2641 | 264 / 1 | 1 | 5 | set_switch(99); stop |
| 10 | 811 | 81 / 1 | 1 | 60 | trigger_event(812); stop |
| 10 | 812 | 81 / 2 | 4 | 40 | trigger_event(813); stop |
| 10 | 813 | 81 / 3 | 3 | 50 | trigger_event(814); stop |
| 10 | 814 | 81 / 4 | 4 | 60 | set_switch(101); stop |
| 10 | 8102 | 81 / 0 | 0 | 1 | trigger_event(818); trigger_event(8112); stop |
| 10 | 818 | 81 / 8 | 3 | 45 | set_switch(6); stop |
| 10 | 2081 | 208 / 1 | 2 | 10 | stop |
| 10 | 8113 | 81 / 13 | 3 | 10 | stop |
| 10 | 71 | 7 / 1 | 1 | 30 | construct_objects(room=7,group_or_wave=1); stop |
| 10 | 701 | 70 / 1 | 3 | 15 | trigger_event(702); stop |
| 10 | 702 | 70 / 2 | 5 | 40 | trigger_event(703); stop |
| 10 | 703 | 70 / 3 | 2 | 60 | trigger_event(704); stop |
| 10 | 704 | 70 / 4 | 2 | 75 | set_switch(7); stop |
| 10 | 21 | 2 / 1 | 1 | 5 | construct_objects(room=203,group_or_wave=1); stop |
| 10 | 706 | 70 / 6 | 2 | 60 | stop |
| 10 | 2621 | 262 / 1 | 1 | 3 | set_switch(8); stop |
| 10 | 601 | 60 / 1 | 3 | 10 | trigger_event(602); stop |
| 10 | 602 | 60 / 2 | 4 | 20 | set_switch(9); trigger_event(2131); stop |
| 10 | 2131 | 213 / 1 | 2 | 30 | trigger_event(2132); stop |
| 10 | 2132 | 213 / 2 | 1 | 40 | set_switch(10); trigger_event(2011); stop |
| 10 | 2011 | 20 / 11 | 2 | 20 | stop |
| 10 | 201 | 20 / 1 | 2 | 25 | trigger_event(202); stop |
| 10 | 202 | 20 / 2 | 5 | 15 | trigger_event(203); stop |
| 10 | 203 | 20 / 3 | 3 | 20 | trigger_event(204); stop |
| 10 | 204 | 20 / 4 | 3 | 10 | set_switch(11); stop |
| 10 | 401 | 40 / 1 | 3 | 60 | set_switch(12); stop |
| 10 | 4011 | 40 / 11 | 0 | 15 | stop |
| 10 | 2211 | 221 / 1 | 1 | 15 | trigger_event(2212); stop |
| 10 | 2212 | 221 / 2 | 2 | 20 | set_switch(97); stop |
| 10 | 901 | 90 / 1 | 2 | 10 | trigger_event(902); stop |
| 10 | 902 | 90 / 2 | 1 | 30 | trigger_event(903); stop |
| 10 | 903 | 90 / 3 | 4 | 25 | trigger_event(904); trigger_event(905); stop |
| 10 | 904 | 90 / 4 | 3 | 90 | set_switch(14); stop |
| 10 | 905 | 90 / 5 | 3 | 10 | set_switch(15); stop |
| 10 | 641 | 64 / 1 | 3 | 10 | trigger_event(642); stop |
| 10 | 642 | 64 / 2 | 3 | 20 | set_switch(16); stop |
| 10 | 41 | 4 / 1 | 1 | 10 | trigger_event(42); stop |
| 10 | 42 | 4 / 2 | 2 | 20 | construct_objects(room=4,group_or_wave=1); set_switch(98); stop |
| 10 | 801 | 80 / 1 | 5 | 15 | trigger_event(802); stop |
| 10 | 802 | 80 / 2 | 3 | 30 | trigger_event(803); stop |
| 10 | 803 | 80 / 3 | 4 | 30 | trigger_event(804); stop |
| 10 | 804 | 80 / 4 | 5 | 50 | trigger_event(805); stop |
| 10 | 805 | 80 / 5 | 3 | 50 | trigger_event(806); stop |
| 10 | 806 | 80 / 6 | 2 | 80 | set_switch(17); stop |
| 10 | 81 | 8 / 1 | 1 | 210 | set_switch(99); set_switch(101); stop |
| 10 | 2111 | 21 / 11 | 0 | 10 | stop |
| 10 | 211 | 21 / 1 | 2 | 45 | trigger_event(212); stop |
| 10 | 212 | 21 / 2 | 2 | 45 | trigger_event(213); stop |
| 10 | 213 | 21 / 3 | 4 | 60 | set_switch(18); stop |
| 10 | 2112 | 21 / 12 | 3 | 60 | stop |
| 10 | 611 | 61 / 1 | 2 | 30 | trigger_event(612); stop |
| 10 | 612 | 61 / 2 | 4 | 30 | trigger_event(613); stop |
| 10 | 613 | 61 / 3 | 2 | 30 | set_switch(19); stop |
| 10 | 2811 | 281 / 1 | 2 | 10 | trigger_event(2812); stop |
| 10 | 2812 | 281 / 2 | 2 | 30 | set_switch(102); trigger_event(2813); stop |
| 10 | 2813 | 281 / 3 | 2 | 30 | stop |
| 11 | 2611 | 261 / 1 | 2 | 10 | trigger_event(2612); stop |
| 11 | 2601 | 260 / 1 | 1 | 20 | stop |
| 11 | 501 | 50 / 1 | 3 | 3 | trigger_event(502); stop |
| 11 | 502 | 50 / 2 | 2 | 20 | trigger_event(503); stop |
| 11 | 503 | 50 / 3 | 3 | 30 | set_switch(1); stop |
| 11 | 7011 | 70 / 11 | 1 | 5 | trigger_event(7012); stop |
| 11 | 7012 | 70 / 12 | 1 | 50 | stop |
| 11 | 701 | 70 / 1 | 1 | 30 | trigger_event(702); stop |
| 11 | 702 | 70 / 2 | 3 | 60 | trigger_event(703); stop |
| 11 | 703 | 70 / 3 | 2 | 60 | trigger_event(704); stop |
| 11 | 704 | 70 / 4 | 3 | 45 | trigger_event(705); stop |
| 11 | 705 | 70 / 5 | 2 | 20 | trigger_event(706); stop |
| 11 | 706 | 70 / 6 | 3 | 90 | set_switch(2); stop |
| 11 | 301 | 30 / 1 | 4 | 5 | trigger_event(302); stop |
| 11 | 302 | 30 / 2 | 2 | 40 | set_switch(3); trigger_event(401); stop |
| 11 | 401 | 40 / 1 | 2 | 30 | trigger_event(402); stop |
| 11 | 402 | 40 / 2 | 2 | 40 | set_switch(4); construct_objects(room=71,group_or_wave=1); stop |
| 11 | 7111 | 71 / 11 | 2 | 20 | stop |
| 11 | 711 | 71 / 1 | 4 | 10 | trigger_event(712); stop |
| 11 | 712 | 71 / 2 | 4 | 45 | trigger_event(713); stop |
| 11 | 713 | 71 / 3 | 2 | 45 | trigger_event(714); stop |
| 11 | 714 | 71 / 4 | 3 | 45 | trigger_event(715); stop |
| 11 | 715 | 71 / 5 | 4 | 90 | set_switch(5); stop |
| 11 | 2121 | 212 / 1 | 1 | 10 | trigger_event(2122); stop |
| 11 | 2122 | 212 / 2 | 1 | 20 | trigger_event(2123); stop |
| 11 | 2123 | 212 / 3 | 1 | 50 | stop |
| 11 | 2111 | 211 / 1 | 4 | 10 | trigger_event(2112); stop |
| 11 | 2112 | 211 / 2 | 2 | 40 | stop |
| 11 | 201 | 20 / 1 | 4 | 15 | trigger_event(202); stop |
| 11 | 202 | 20 / 2 | 3 | 20 | set_switch(6); trigger_event(311); stop |
| 11 | 311 | 31 / 1 | 2 | 5 | trigger_event(312); stop |
| 11 | 312 | 31 / 2 | 1 | 20 | trigger_event(313); stop |
| 11 | 313 | 31 / 3 | 4 | 30 | set_switch(7); stop |
| 11 | 2711 | 271 / 1 | 1 | 5 | trigger_event(2712); stop |
| 11 | 2712 | 271 / 2 | 2 | 20 | set_switch(8); construct_objects(room=30,group_or_wave=1); stop |
| 11 | 316 | 31 / 6 | 3 | 10 | trigger_event(317); stop |
| 11 | 317 | 31 / 7 | 1 | 40 | stop |
| 11 | 9011 | 90 / 11 | 2 | 5 | stop |
| 11 | 901 | 90 / 1 | 4 | 30 | trigger_event(902); stop |
| 11 | 902 | 90 / 2 | 4 | 30 | trigger_event(903); stop |
| 11 | 903 | 90 / 3 | 3 | 30 | set_switch(9); stop |
| 11 | 2911 | 291 / 1 | 4 | 10 | set_switch(10); stop |
| 11 | 951 | 95 / 1 | 2 | 5 | trigger_event(952); trigger_event(9511); stop |
| 11 | 952 | 95 / 2 | 2 | 30 | trigger_event(953); stop |
| 11 | 953 | 95 / 3 | 1 | 45 | trigger_event(954); stop |
| 11 | 954 | 95 / 4 | 2 | 45 | trigger_event(955); stop |
| 11 | 955 | 95 / 5 | 2 | 60 | trigger_event(956); stop |
| 11 | 956 | 95 / 6 | 3 | 60 | trigger_event(957); stop |
| 11 | 957 | 95 / 7 | 2 | 90 | trigger_event(958); stop |
| 11 | 958 | 95 / 8 | 1 | 90 | set_switch(11); stop |
| 11 | 9511 | 95 / 11 | 1 | 50 | trigger_event(9512); stop |
| 11 | 9512 | 95 / 12 | 2 | 60 | trigger_event(9513); stop |
| 11 | 9513 | 95 / 13 | 2 | 60 | trigger_event(9514); stop |
| 11 | 9514 | 95 / 14 | 2 | 60 | trigger_event(9515); stop |
| 11 | 9515 | 95 / 15 | 1 | 60 | set_switch(12); stop |
| 11 | 9520 | 95 / 20 | 2 | 90 | stop |
| 11 | 31 | 3 / 1 | 2 | 60 | construct_objects(room=3,group_or_wave=1); stop |
| 11 | 411 | 41 / 1 | 4 | 5 | trigger_event(2161); stop |
| 11 | 2701 | 270 / 1 | 1 | 5 | stop |
| 11 | 2161 | 216 / 1 | 2 | 10 | trigger_event(9520); stop |
| 11 | 2621 | 262 / 1 | 1 | 3 | stop |
| 11 | 801 | 80 / 1 | 3 | 10 | trigger_event(802); stop |
| 11 | 802 | 80 / 2 | 1 | 20 | trigger_event(803); stop |
| 11 | 803 | 80 / 3 | 2 | 60 | trigger_event(804); stop |
| 11 | 804 | 80 / 4 | 3 | 60 | trigger_event(805); stop |
| 11 | 805 | 80 / 5 | 5 | 45 | set_switch(17); trigger_event(511); stop |
| 11 | 511 | 51 / 1 | 5 | 10 | trigger_event(512); stop |
| 11 | 512 | 51 / 2 | 2 | 30 | set_switch(18); trigger_event(811); stop |
| 11 | 811 | 81 / 1 | 4 | 10 | trigger_event(812); stop |
| 11 | 812 | 81 / 2 | 3 | 60 | trigger_event(813); stop |
| 11 | 813 | 81 / 3 | 3 | 20 | trigger_event(814); stop |
| 11 | 814 | 81 / 4 | 5 | 30 | trigger_event(815); stop |
| 11 | 815 | 81 / 5 | 5 | 30 | set_switch(19); stop |
| 11 | 8110 | 81 / 10 | 3 | 30 | stop |
| 11 | 521 | 52 / 1 | 2 | 10 | trigger_event(522); stop |
| 11 | 522 | 52 / 2 | 4 | 30 | trigger_event(523); stop |
| 11 | 523 | 52 / 3 | 3 | 20 | set_switch(20); stop |
| 11 | 2901 | 290 / 1 | 3 | 90 | set_switch(21); stop |
| 13 | 1 | 0 / 1 | 1 | 0 | construct_objects(room=1,group_or_wave=1); set_switch(1); stop |
| 13 | 2 | 0 / 0 | 0 | 1 | construct_objects(room=1,group_or_wave=2); stop |

## Review notes

- Nonzero data after terminal header
- Floor 10: event 8102 targets absent event 8112
- Floor 11: event 2611 targets absent event 2612
