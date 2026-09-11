# Stage4 — challenge-ep2/d88204-bb-e

Episode2; header quest ID 65535; language E. Static scan: **1151 objects, 438 enemy/NPC records, 151 events, 56 script labels.** Script roundtrip: byte-identical.

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
0x01, 0x1C, 0x00, 0x00, 0x00
0x02, 0x1C, 0x00, 0x02, 0x00
0x03, 0x1C, 0x00, 0x01, 0x00
0x04, 0x1D, 0x00, 0x00, 0x00
0x05, 0x1D, 0x00, 0x02, 0x00
0x06, 0x1D, 0x00, 0x01, 0x00
0x0D, 0x1F, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 40 | 12 | 0 |
| 1 | 195 | 78 | 26 |
| 2 | 124 | 59 | 23 |
| 3 | 287 | 84 | 32 |
| 4 | 187 | 67 | 22 |
| 5 | 100 | 51 | 19 |
| 6 | 211 | 86 | 28 |
| 13 | 7 | 1 | 1 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 201 | 20 / 1 | 2 | 120 | set_switch(1); set_switch(2); stop |
| 1 | 202 | 20 / 2 | 3 | 10 | stop |
| 1 | 211 | 21 / 1 | 4 | 10 | trigger_event(2111); stop |
| 1 | 2111 | 21 / 2 | 1 | 60 | set_switch(4); set_switch(8); set_switch(6); set_switch(7); set_switch(9); set_switch(38); set_switch(39); stop |
| 1 | 301 | 30 / 1 | 6 | 10 | stop |
| 1 | 401 | 40 / 1 | 3 | 10 | set_switch(28); stop |
| 1 | 402 | 40 / 2 | 2 | 10 | stop |
| 1 | 601 | 60 / 1 | 4 | 100 | set_switch(3); set_switch(5); stop |
| 1 | 611 | 61 / 1 | 2 | 10 | set_switch(15); set_switch(16); set_switch(13); set_switch(19); set_switch(18); set_switch(17); stop |
| 1 | 621 | 62 / 1 | 4 | 10 | set_switch(29); set_switch(20); stop |
| 1 | 631 | 63 / 1 | 3 | 60 | set_switch(14); set_switch(40); set_switch(41); set_switch(42); stop |
| 1 | 641 | 64 / 1 | 2 | 10 | set_switch(23); set_switch(24); set_switch(34); set_switch(35); stop |
| 1 | 642 | 64 / 2 | 3 | 10 | stop |
| 1 | 701 | 70 / 1 | 4 | 10 | trigger_event(7011); stop |
| 1 | 7011 | 70 / 2 | 1 | 100 | set_switch(21); set_switch(22); set_switch(27); stop |
| 1 | 711 | 71 / 1 | 2 | 10 | trigger_event(7111); set_switch(36); set_switch(37); stop |
| 1 | 7111 | 71 / 2 | 2 | 1500 | set_switch(33); set_switch(32); set_switch(34); set_switch(35); stop |
| 1 | 801 | 80 / 1 | 1 | 10 | stop |
| 1 | 811 | 81 / 1 | 2 | 10 | set_switch(36); set_switch(37); stop |
| 1 | 812 | 81 / 2 | 2 | 10 | stop |
| 1 | 901 | 90 / 1 | 2 | 150 | trigger_event(9011); stop |
| 1 | 9011 | 90 / 2 | 4 | 100 | trigger_event(9012); stop |
| 1 | 9012 | 90 / 3 | 6 | 100 | trigger_event(9013); stop |
| 1 | 9013 | 90 / 4 | 8 | 100 | set_switch(100); set_switch(101); set_switch(102); set_switch(103); stop |
| 1 | 2115 | 211 / 1 | 1 | 10 | stop |
| 1 | 2131 | 213 / 1 | 4 | 10 | stop |
| 2 | 201 | 20 / 1 | 2 | 150 | set_switch(38); set_switch(39); stop |
| 2 | 202 | 20 / 2 | 4 | 10 | stop |
| 2 | 211 | 21 / 1 | 4 | 10 | trigger_event(2111); stop |
| 2 | 2111 | 21 / 2 | 1 | 100 | set_switch(24); set_switch(25); set_switch(26); set_switch(27); set_switch(28); stop |
| 2 | 212 | 21 / 3 | 3 | 10 | stop |
| 2 | 301 | 30 / 1 | 4 | 10 | set_switch(27); set_switch(28); stop |
| 2 | 302 | 30 / 2 | 2 | 10 | stop |
| 2 | 401 | 40 / 1 | 3 | 10 | set_switch(40); set_switch(41); set_switch(46); set_switch(45); set_switch(39); stop |
| 2 | 402 | 40 / 2 | 3 | 10 | stop |
| 2 | 621 | 62 / 1 | 2 | 10 | set_switch(29); set_switch(30); set_switch(31); stop |
| 2 | 622 | 62 / 2 | 3 | 10 | stop |
| 2 | 641 | 64 / 1 | 3 | 10 | set_switch(32); set_switch(33); stop |
| 2 | 642 | 64 / 2 | 2 | 10 | stop |
| 2 | 801 | 80 / 1 | 2 | 150 | trigger_event(8011); stop |
| 2 | 8011 | 80 / 2 | 3 | 10 | set_switch(23); set_switch(22); set_switch(45); stop |
| 2 | 802 | 80 / 3 | 4 | 10 | stop |
| 2 | 811 | 81 / 1 | 2 | 150 | trigger_event(8111); stop |
| 2 | 8111 | 81 / 2 | 3 | 10 | trigger_event(8112); stop |
| 2 | 8112 | 81 / 3 | 2 | 100 | set_switch(34); set_switch(37); set_switch(36); stop |
| 2 | 812 | 81 / 4 | 3 | 10 | stop |
| 2 | 2131 | 213 / 1 | 1 | 1 | stop |
| 2 | 2201 | 220 / 1 | 1 | 1 | stop |
| 2 | 2641 | 264 / 1 | 2 | 1 | stop |
| 3 | 201 | 20 / 1 | 4 | 60 | trigger_event(2011); stop |
| 3 | 2011 | 20 / 2 | 2 | 10 | trigger_event(2012); stop |
| 3 | 2012 | 20 / 3 | 3 | 10 | set_switch(19); set_switch(26); set_switch(25); stop |
| 3 | 202 | 20 / 4 | 3 | 10 | stop |
| 3 | 211 | 21 / 1 | 3 | 10 | trigger_event(2111); stop |
| 3 | 2111 | 21 / 2 | 2 | 100 | set_switch(5); set_switch(6); set_switch(35); set_switch(32); set_switch(30); stop |
| 3 | 301 | 30 / 1 | 1 | 30 | set_switch(120); stop |
| 3 | 302 | 30 / 2 | 6 | 10 | stop |
| 3 | 401 | 40 / 1 | 3 | 10 | construct_objects(room=40,group_or_wave=4); set_switch(15); set_switch(16); set_switch(17); stop |
| 3 | 402 | 40 / 2 | 2 | 10 | stop |
| 3 | 601 | 60 / 1 | 1 | 100 | set_switch(21); set_switch(20); stop |
| 3 | 602 | 60 / 2 | 1 | 100 | set_switch(22); stop |
| 3 | 611 | 61 / 1 | 4 | 10 | set_switch(3); set_switch(4); stop |
| 3 | 621 | 62 / 1 | 1 | 100 | set_switch(42); set_switch(43); stop |
| 3 | 631 | 63 / 1 | 3 | 10 | set_switch(121); stop |
| 3 | 641 | 64 / 1 | 3 | 10 | set_switch(11); set_switch(12); stop |
| 3 | 642 | 64 / 2 | 2 | 10 | stop |
| 3 | 701 | 70 / 1 | 3 | 10 | set_switch(8); set_switch(9); set_switch(10); construct_objects(room=70,group_or_wave=3); stop |
| 3 | 711 | 71 / 1 | 3 | 60 | trigger_event(7111); stop |
| 3 | 7111 | 71 / 2 | 1 | 150 | construct_objects(room=71,group_or_wave=2); set_switch(121); stop |
| 3 | 712 | 71 / 3 | 3 | 10 | stop |
| 3 | 801 | 80 / 1 | 1 | 10 | trigger_event(8011); stop |
| 3 | 8011 | 80 / 2 | 2 | 10 | trigger_event(8012); stop |
| 3 | 8012 | 80 / 3 | 3 | 100 | construct_objects(room=80,group_or_wave=5); stop |
| 3 | 802 | 80 / 4 | 4 | 10 | stop |
| 3 | 811 | 81 / 1 | 6 | 10 | set_switch(123); stop |
| 3 | 901 | 90 / 1 | 2 | 180 | set_switch(13); set_switch(14); set_switch(8); stop |
| 3 | 2101 | 210 / 1 | 3 | 10 | set_switch(10); stop |
| 3 | 2131 | 213 / 1 | 3 | 10 | stop |
| 3 | 2631 | 263 / 1 | 1 | 10 | set_switch(122); stop |
| 3 | 2651 | 265 / 1 | 3 | 100 | stop |
| 3 | 2811 | 281 / 1 | 2 | 60 | stop |
| 4 | 201 | 20 / 1 | 1 | 100 | set_switch(36); set_switch(32); stop |
| 4 | 401 | 40 / 1 | 3 | 10 | set_switch(24); set_switch(9); set_switch(8); set_switch(6); set_switch(22); set_switch(23); stop |
| 4 | 402 | 40 / 2 | 3 | 10 | stop |
| 4 | 501 | 50 / 1 | 3 | 10 | set_switch(45); set_switch(47); set_switch(7); set_switch(8); set_switch(9); set_switch(6); stop |
| 4 | 511 | 51 / 1 | 4 | 10 | set_switch(39); stop |
| 4 | 521 | 52 / 1 | 4 | 10 | set_switch(1); set_switch(2); set_switch(43); set_switch(44); set_switch(45); set_switch(46); stop |
| 4 | 522 | 52 / 2 | 2 | 10 | stop |
| 4 | 701 | 70 / 1 | 4 | 10 | trigger_event(7011); stop |
| 4 | 7011 | 70 / 2 | 2 | 100 | set_switch(4); set_switch(5); stop |
| 4 | 702 | 70 / 3 | 3 | 10 | stop |
| 4 | 711 | 71 / 1 | 6 | 10 | set_switch(30); set_switch(28); set_switch(26); set_switch(27); set_switch(25); set_switch(21); stop |
| 4 | 801 | 80 / 1 | 3 | 100 | set_switch(11); set_switch(12); set_switch(10); stop |
| 4 | 802 | 80 / 2 | 1 | 300 | stop |
| 4 | 811 | 81 / 1 | 1 | 150 | set_switch(40); set_switch(41); set_switch(42); stop |
| 4 | 901 | 90 / 1 | 6 | 100 | trigger_event(9011); stop |
| 4 | 9011 | 90 / 2 | 6 | 10 | trigger_event(9012); stop |
| 4 | 9012 | 90 / 2 | 6 | 10 | set_switch(20); set_switch(21); stop |
| 4 | 951 | 95 / 1 | 1 | 150 | set_switch(46); set_switch(14); set_switch(15); set_switch(13); set_switch(16); set_switch(17); set_switch(18); stop |
| 4 | 952 | 95 / 2 | 5 | 10 | stop |
| 4 | 2151 | 215 / 1 | 1 | 100 | stop |
| 4 | 2511 | 251 / 1 | 1 | 30 | stop |
| 4 | 2901 | 290 / 1 | 1 | 10 | stop |
| 5 | 201 | 20 / 1 | 2 | 300 | stop |
| 5 | 202 | 20 / 2 | 4 | 10 | set_switch(3); set_switch(6); stop |
| 5 | 401 | 40 / 1 | 3 | 10 | set_switch(20); set_switch(22); set_switch(21); stop |
| 5 | 402 | 40 / 2 | 3 | 10 | stop |
| 5 | 501 | 50 / 1 | 2 | 150 | set_switch(15); set_switch(16); set_switch(17); set_switch(18); set_switch(19); stop |
| 5 | 502 | 50 / 2 | 4 | 10 | stop |
| 5 | 701 | 70 / 1 | 1 | 200 | set_switch(25); set_switch(26); set_switch(9); set_switch(10); stop |
| 5 | 702 | 70 / 2 | 4 | 10 | stop |
| 5 | 801 | 80 / 1 | 3 | 10 | trigger_event(8011); stop |
| 5 | 8011 | 80 / 2 | 1 | 100 | set_switch(23); set_switch(24); stop |
| 5 | 802 | 80 / 3 | 3 | 10 | stop |
| 5 | 901 | 90 / 1 | 2 | 150 | set_switch(7); set_switch(8); stop |
| 5 | 902 | 90 / 2 | 4 | 10 | stop |
| 5 | 951 | 95 / 1 | 2 | 250 | set_switch(4); set_switch(5); set_switch(2); set_switch(1); stop |
| 5 | 952 | 95 / 2 | 5 | 10 | stop |
| 5 | 2801 | 280 / 1 | 3 | 10 | stop |
| 5 | 2641 | 264 / 1 | 1 | 10 | stop |
| 5 | 2111 | 211 / 1 | 2 | 10 | stop |
| 5 | 2901 | 290 / 1 | 2 | 10 | stop |
| 6 | 511 | 51 / 1 | 4 | 10 | set_switch(26); set_switch(25); set_switch(24); stop |
| 6 | 521 | 52 / 1 | 6 | 10 | set_switch(27); stop |
| 6 | 701 | 70 / 1 | 2 | 10 | trigger_event(7011); stop |
| 6 | 7011 | 70 / 2 | 3 | 150 | trigger_event(7012); stop |
| 6 | 7012 | 70 / 3 | 1 | 10 | set_switch(1); set_switch(4); set_switch(5); set_switch(2); set_switch(3); set_switch(8); set_switch(10); stop |
| 6 | 702 | 70 / 4 | 2 | 1000 | stop |
| 6 | 711 | 71 / 1 | 6 | 10 | trigger_event(7111); stop |
| 6 | 7111 | 71 / 2 | 2 | 10 | set_switch(21); set_switch(22); set_switch(23); set_switch(15); set_switch(16); stop |
| 6 | 712 | 71 / 3 | 2 | 300 | stop |
| 6 | 801 | 80 / 1 | 1 | 100 | set_switch(36); set_switch(39); stop |
| 6 | 811 | 81 / 1 | 2 | 100 | set_switch(13); stop |
| 6 | 811 | 81 / 2 | 2 | 1000 | stop |
| 6 | 901 | 90 / 1 | 1 | 150 | set_switch(34); set_switch(33); set_switch(32); set_switch(31); set_switch(28); set_switch(35); stop |
| 6 | 902 | 90 / 2 | 5 | 10 | stop |
| 6 | 951 | 95 / 1 | 2 | 100 | set_switch(17); set_switch(4); set_switch(6); set_switch(7); set_switch(14); stop |
| 6 | 952 | 95 / 2 | 5 | 10 | stop |
| 6 | 201 | 20 / 1 | 3 | 10 | construct_objects(room=20,group_or_wave=1); stop |
| 6 | 301 | 30 / 1 | 1 | 10 | construct_objects(room=30,group_or_wave=2); stop |
| 6 | 302 | 30 / 2 | 1 | 10 | construct_objects(room=30,group_or_wave=3); stop |
| 6 | 311 | 31 / 1 | 6 | 10 | construct_objects(room=31,group_or_wave=4); stop |
| 6 | 312 | 31 / 2 | 6 | 10 | construct_objects(room=31,group_or_wave=5); stop |
| 6 | 501 | 50 / 1 | 6 | 10 | construct_objects(room=50,group_or_wave=6); stop |
| 6 | 502 | 50 / 2 | 6 | 10 | construct_objects(room=50,group_or_wave=7); stop |
| 6 | 531 | 53 / 1 | 2 | 10 | construct_objects(room=53,group_or_wave=8); stop |
| 6 | 532 | 53 / 2 | 3 | 10 | construct_objects(room=53,group_or_wave=9); stop |
| 6 | 2601 | 260 / 1 | 1 | 10 | construct_objects(room=260,group_or_wave=10); stop |
| 6 | 2651 | 265 / 1 | 1 | 10 | stop |
| 6 | 2921 | 292 / 1 | 4 | 1 | set_switch(41); set_switch(40); stop |
| 13 | 1 | 0 / 1 | 1 | 0 | construct_objects(room=1,group_or_wave=1); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
