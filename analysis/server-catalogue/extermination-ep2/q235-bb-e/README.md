# Phantasmal World #3 — extermination-ep2/q235-bb-e

Episode2; header quest ID 235; language E. Static scan: **446 objects, 367 enemy/NPC records, 106 events, 214 script labels.** Script roundtrip: byte-identical.

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
0x0A, 0x1C, 0x00, 0x02, 0x00
0x0B, 0x1D, 0x00, 0x01, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 44 | 20 | 0 |
| 10 | 248 | 166 | 48 |
| 11 | 154 | 181 | 58 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 10 | 31 | 3 / 1 | 1 | 90 | trigger_event(311); stop |
| 10 | 311 | 3 / 2 | 2 | 30 | stop |
| 10 | 61 | 6 / 1 | 4 | 30 | construct_objects(room=6,group_or_wave=1); stop |
| 10 | 201 | 20 / 1 | 4 | 30 | trigger_event(20111); stop |
| 10 | 20111 | 20 / 2 | 4 | 90 | set_switch(11); set_switch(35); set_switch(36); stop |
| 10 | 401 | 40 / 1 | 1 | 30 | trigger_event(4011); stop |
| 10 | 4011 | 40 / 2 | 2 | 30 | set_switch(38); set_switch(39); set_switch(40); stop |
| 10 | 801 | 80 / 1 | 5 | 60 | trigger_event(8011); stop |
| 10 | 8011 | 80 / 2 | 4 | 60 | trigger_event(8012); stop |
| 10 | 8012 | 80 / 3 | 1 | 30 | set_switch(45); stop |
| 10 | 802 | 80 / 4 | 5 | 120 | set_switch(48); construct_objects(room=80,group_or_wave=1); stop |
| 10 | 2011 | 201 / 1 | 1 | 30 | stop |
| 10 | 901 | 90 / 1 | 5 | 30 | set_switch(42); stop |
| 10 | 902 | 90 / 2 | 1 | 150 | stop |
| 10 | 2151 | 215 / 1 | 1 | 30 | set_switch(43); set_switch(44); stop |
| 10 | 2211 | 221 / 1 | 1 | 30 | set_switch(37); stop |
| 10 | 2212 | 221 / 2 | 1 | 30 | stop |
| 10 | 2651 | 265 / 1 | 1 | 30 | set_switch(41); stop |
| 10 | 631 | 63 / 1 | 6 | 60 | set_switch(10); set_switch(9); stop |
| 10 | 701 | 70 / 1 | 3 | 90 | trigger_event(7011); stop |
| 10 | 7011 | 70 / 2 | 5 | 30 | trigger_event(7012); stop |
| 10 | 7012 | 70 / 3 | 4 | 60 | set_switch(3); set_switch(8); set_switch(6); set_switch(5); set_switch(7); set_switch(47); stop |
| 10 | 2101 | 210 / 1 | 3 | 60 | stop |
| 10 | 2111 | 211 / 1 | 1 | 60 | stop |
| 10 | 601 | 60 / 1 | 4 | 30 | set_switch(4); set_switch(13); set_switch(14); set_switch(15); set_switch(16); stop |
| 10 | 602 | 60 / 2 | 3 | 30 | stop |
| 10 | 603 | 60 / 3 | 2 | 30 | stop |
| 10 | 604 | 60 / 4 | 1 | 30 | stop |
| 10 | 711 | 71 / 1 | 4 | 30 | trigger_event(7111); stop |
| 10 | 7111 | 71 / 2 | 7 | 30 | trigger_event(7112); stop |
| 10 | 7112 | 70 / 3 | 4 | 30 | trigger_event(7113); stop |
| 10 | 7113 | 70 / 4 | 0 | 60 | set_switch(18); set_switch(17); stop |
| 10 | 611 | 61 / 1 | 6 | 30 | set_switch(20); set_switch(21); stop |
| 10 | 211 | 21 / 1 | 3 | 30 | trigger_event(2115); stop |
| 10 | 2115 | 21 / 2 | 6 | 30 | set_switch(22); set_switch(24); set_switch(25); stop |
| 10 | 2141 | 214 / 1 | 1 | 30 | set_switch(25); stop |
| 10 | 2201 | 220 / 1 | 1 | 30 | set_switch(23); stop |
| 10 | 301 | 30 / 1 | 2 | 30 | set_switch(27); set_switch(28); stop |
| 10 | 621 | 62 / 1 | 6 | 30 | set_switch(29); set_switch(30); stop |
| 10 | 641 | 64 / 1 | 4 | 30 | trigger_event(6411); stop |
| 10 | 6411 | 64 / 2 | 6 | 90 | set_switch(32); set_switch(33); stop |
| 10 | 811 | 81 / 1 | 5 | 120 | trigger_event(8111); stop |
| 10 | 8111 | 81 / 2 | 7 | 60 | trigger_event(8112); stop |
| 10 | 8112 | 81 / 3 | 6 | 30 | trigger_event(8113); stop |
| 10 | 8113 | 81 / 4 | 6 | 60 | trigger_event(8114); stop |
| 10 | 8114 | 81 / 5 | 5 | 30 | trigger_event(8115); stop |
| 10 | 8115 | 81 / 6 | 4 | 150 | set_switch(34); construct_objects(room=4,group_or_wave=1); stop |
| 10 | 812 | 81 / 7 | 3 | 150 | stop |
| 11 | 11 | 1 / 1 | 2 | 30 | set_switch(1); set_switch(2); set_switch(4); stop |
| 11 | 61 | 6 / 1 | 2 | 30 | set_switch(35); stop |
| 11 | 201 | 20 / 1 | 3 | 60 | trigger_event(20111); stop |
| 11 | 20111 | 20 / 2 | 4 | 30 | trigger_event(20112); stop |
| 11 | 20112 | 20 / 3 | 5 | 45 | trigger_event(20113); stop |
| 11 | 20113 | 20 / 4 | 2 | 90 | construct_objects(room=20,group_or_wave=1); construct_objects(room=71,group_or_wave=1); stop |
| 11 | 301 | 30 / 1 | 3 | 30 | set_switch(10); stop |
| 11 | 311 | 31 / 1 | 7 | 30 | set_switch(28); set_switch(30); set_switch(31); stop |
| 11 | 401 | 40 / 1 | 2 | 30 | trigger_event(4011); stop |
| 11 | 4011 | 40 / 2 | 2 | 60 | set_switch(3); set_switch(106); stop |
| 11 | 501 | 50 / 1 | 6 | 30 | set_switch(19); stop |
| 11 | 511 | 51 / 1 | 3 | 30 | set_switch(24); set_switch(25); set_switch(26); stop |
| 11 | 521 | 52 / 1 | 3 | 30 | set_switch(27); set_switch(29); stop |
| 11 | 531 | 53 / 1 | 3 | 30 | set_switch(38); stop |
| 11 | 701 | 70 / 1 | 3 | 90 | trigger_event(7011); stop |
| 11 | 7011 | 70 / 2 | 3 | 30 | set_switch(5); stop |
| 11 | 711 | 71 / 1 | 2 | 60 | trigger_event(7111); stop |
| 11 | 7111 | 71 / 2 | 4 | 30 | trigger_event(7112); stop |
| 11 | 7112 | 71 / 3 | 3 | 90 | set_switch(20); set_switch(21); set_switch(22); set_switch(23); stop |
| 11 | 712 | 71 / 4 | 2 | 30 | construct_objects(room=71,group_or_wave=2); stop |
| 11 | 801 | 80 / 1 | 2 | 60 | trigger_event(8011); stop |
| 11 | 8011 | 80 / 2 | 3 | 30 | set_switch(39); set_switch(36); stop |
| 11 | 811 | 81 / 1 | 3 | 90 | trigger_event(8111); stop |
| 11 | 8111 | 81 / 2 | 4 | 90 | trigger_event(8112); stop |
| 11 | 8112 | 81 / 3 | 2 | 30 | set_switch(13); set_switch(9); stop |
| 11 | 901 | 90 / 1 | 5 | 30 | set_switch(37); stop |
| 11 | 902 | 90 / 2 | 3 | 30 | set_switch(32); set_switch(33); stop |
| 11 | 951 | 95 / 1 | 4 | 60 | trigger_event(9511); stop |
| 11 | 9511 | 95 / 2 | 2 | 30 | trigger_event(9512); stop |
| 11 | 9512 | 95 / 3 | 2 | 60 | trigger_event(9513); stop |
| 11 | 9513 | 95 / 4 | 3 | 30 | trigger_event(9514); stop |
| 11 | 9514 | 95 / 5 | 2 | 30 | trigger_event(9515); stop |
| 11 | 9515 | 95 / 6 | 2 | 60 | trigger_event(9516); stop |
| 11 | 9516 | 95 / 7 | 3 | 30 | trigger_event(9517); stop |
| 11 | 9517 | 95 / 8 | 3 | 30 | trigger_event(9518); stop |
| 11 | 9518 | 95 / 9 | 3 | 60 | trigger_event(9519); stop |
| 11 | 9519 | 95 / 10 | 4 | 30 | set_switch(100); stop |
| 11 | 952 | 95 / 11 | 2 | 180 | trigger_event(9521); stop |
| 11 | 9521 | 95 / 12 | 3 | 90 | trigger_event(9522); stop |
| 11 | 9522 | 95 / 13 | 3 | 120 | trigger_event(9523); stop |
| 11 | 9523 | 95 / 14 | 4 | 30 | trigger_event(9524); stop |
| 11 | 9524 | 95 / 15 | 4 | 90 | trigger_event(9525); stop |
| 11 | 9525 | 95 / 16 | 4 | 120 | trigger_event(9526); stop |
| 11 | 9526 | 95 / 17 | 3 | 30 | trigger_event(9527); stop |
| 11 | 9527 | 95 / 18 | 2 | 60 | trigger_event(9528); stop |
| 11 | 9528 | 95 / 19 | 3 | 30 | trigger_event(9529); stop |
| 11 | 9529 | 95 / 20 | 3 | 60 | set_switch(101); stop |
| 11 | 953 | 95 / 21 | 1 | 60 | trigger_event(9531); stop |
| 11 | 9531 | 95 / 22 | 5 | 30 | trigger_event(9532); stop |
| 11 | 9532 | 95 / 23 | 5 | 30 | trigger_event(9533); stop |
| 11 | 9533 | 95 / 24 | 2 | 120 | trigger_event(9534); stop |
| 11 | 9534 | 95 / 25 | 7 | 180 | set_switch(180); stop |
| 11 | 2031 | 203 / 1 | 3 | 30 | set_switch(8); stop |
| 11 | 2111 | 211 / 1 | 3 | 30 | stop |
| 11 | 2121 | 212 / 1 | 2 | 90 | stop |
| 11 | 2122 | 212 / 2 | 1 | 30 | stop |
| 11 | 2801 | 280 / 1 | 3 | 30 | set_switch(105); set_switch(11); stop |
| 11 | 2921 | 292 / 1 | 4 | 30 | set_switch(40); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

A backup is present; decompressed content identical: True. See [text differences](<backup-diff.txt>).

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
