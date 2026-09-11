# Sweep-up Operation #8 — q169-bb-e

Episode2; header quest ID 169; language E. Static scan: **171 objects, 208 enemy/NPC records, 62 events, 42 script labels.** Script roundtrip: byte-identical.

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
| 0 | 43 | 8 | 0 |
| 10 | 128 | 200 | 62 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 10 | 801 | 80 / 1 | 3 | 60 | trigger_event(802); stop |
| 10 | 802 | 80 / 2 | 4 | 30 | trigger_event(803); stop |
| 10 | 803 | 80 / 3 | 3 | 60 | set_switch(17); set_switch(18); stop |
| 10 | 2211 | 221 / 1 | 1 | 1 | stop |
| 10 | 611 | 61 / 1 | 5 | 1 | trigger_event(612); stop |
| 10 | 612 | 61 / 2 | 3 | 30 | trigger_event(613); stop |
| 10 | 613 | 61 / 3 | 4 | 30 | trigger_event(614); stop |
| 10 | 614 | 61 / 4 | 3 | 30 | set_switch(27); stop |
| 10 | 31 | 3 / 1 | 2 | 1 | trigger_event(32); stop |
| 10 | 32 | 3 / 2 | 1 | 30 | set_switch(22); trigger_event(2521); stop |
| 10 | 2521 | 252 / 1 | 1 | 1 | stop |
| 10 | 706 | 70 / 6 | 4 | 1 | stop |
| 10 | 702 | 70 / 2 | 2 | 20 | trigger_event(703); stop |
| 10 | 703 | 70 / 3 | 4 | 30 | trigger_event(704); stop |
| 10 | 704 | 70 / 4 | 3 | 30 | trigger_event(705); stop |
| 10 | 705 | 70 / 5 | 2 | 90 | set_switch(23); set_switch(24); stop |
| 10 | 641 | 64 / 1 | 4 | 30 | trigger_event(642); stop |
| 10 | 642 | 64 / 2 | 4 | 30 | trigger_event(643); stop |
| 10 | 643 | 64 / 3 | 3 | 30 | set_switch(25); set_switch(26); stop |
| 10 | 644 | 64 / 4 | 3 | 30 | trigger_event(645); stop |
| 10 | 645 | 64 / 5 | 3 | 30 | set_switch(34); set_switch(35); stop |
| 10 | 711 | 71 / 1 | 3 | 30 | trigger_event(712); stop |
| 10 | 712 | 71 / 2 | 7 | 30 | trigger_event(713); stop |
| 10 | 713 | 71 / 3 | 4 | 0 | trigger_event(714); stop |
| 10 | 714 | 71 / 4 | 7 | 30 | set_switch(36); set_switch(37); stop |
| 10 | 811 | 81 / 1 | 5 | 1 | stop |
| 10 | 812 | 81 / 2 | 1 | 30 | trigger_event(813); stop |
| 10 | 813 | 81 / 3 | 8 | 30 | trigger_event(814); stop |
| 10 | 814 | 81 / 4 | 7 | 30 | set_switch(38); set_switch(39); stop |
| 10 | 211 | 21 / 1 | 4 | 60 | trigger_event(212); stop |
| 10 | 212 | 21 / 2 | 4 | 30 | trigger_event(2531); set_switch(40); set_switch(41); set_switch(42); stop |
| 10 | 2531 | 253 / 1 | 4 | 60 | stop |
| 10 | 631 | 63 / 1 | 4 | 30 | trigger_event(632); stop |
| 10 | 632 | 63 / 2 | 7 | 30 | trigger_event(633); stop |
| 10 | 633 | 63 / 3 | 1 | 30 | set_switch(45); set_switch(46); set_switch(1); set_switch(2); stop |
| 10 | 2811 | 281 / 1 | 2 | 1 | trigger_event(2812); stop |
| 10 | 2812 | 281 / 2 | 2 | 0 | stop |
| 10 | 201 | 20 / 1 | 4 | 1 | stop |
| 10 | 202 | 20 / 2 | 5 | 1 | trigger_event(203); stop |
| 10 | 203 | 20 / 3 | 1 | 90 | set_switch(3); set_switch(4); set_switch(5); stop |
| 10 | 601 | 60 / 1 | 5 | 1 | trigger_event(602); stop |
| 10 | 602 | 60 / 2 | 6 | 60 | set_switch(6); set_switch(8); set_switch(9); set_switch(10); set_switch(11); set_switch(12); stop |
| 10 | 301 | 30 / 1 | 4 | 1 | stop |
| 10 | 901 | 90 / 1 | 2 | 1 | trigger_event(902); trigger_event(905); trigger_event(908); trigger_event(9011); stop |
| 10 | 902 | 90 / 2 | 1 | 10 | trigger_event(903); stop |
| 10 | 903 | 90 / 3 | 2 | 10 | trigger_event(904); stop |
| 10 | 904 | 90 / 4 | 2 | 10 | set_switch(101); stop |
| 10 | 905 | 90 / 5 | 1 | 10 | trigger_event(906); stop |
| 10 | 906 | 90 / 6 | 1 | 10 | trigger_event(907); stop |
| 10 | 907 | 90 / 7 | 2 | 10 | set_switch(102); stop |
| 10 | 908 | 90 / 8 | 1 | 10 | trigger_event(909); stop |
| 10 | 909 | 90 / 9 | 2 | 10 | trigger_event(9010); stop |
| 10 | 9010 | 90 / 10 | 2 | 10 | set_switch(103); stop |
| 10 | 9011 | 90 / 11 | 1 | 10 | trigger_event(9012); stop |
| 10 | 9012 | 90 / 12 | 1 | 10 | trigger_event(9013); stop |
| 10 | 9013 | 90 / 13 | 2 | 10 | set_switch(104); stop |
| 10 | 9014 | 90 / 14 | 6 | 60 | trigger_event(9015); stop |
| 10 | 9015 | 90 / 15 | 6 | 30 | trigger_event(9016); stop |
| 10 | 9016 | 90 / 16 | 3 | 30 | trigger_event(9017); stop |
| 10 | 9017 | 90 / 17 | 4 | 30 | trigger_event(9018); stop |
| 10 | 9018 | 90 / 18 | 4 | 120 | set_switch(13); stop |
| 10 | 9099 | 90 / 0 | 0 | 1 | construct_objects(room=90,group_or_wave=1); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
