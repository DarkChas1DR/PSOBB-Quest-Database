# Maximum Attack 4th Stage -C- — maximum-attack-ep4/q305-bb-j

Episode4; header quest ID 305; language J. Static scan: **109 objects, 480 enemy/NPC records, 75 events, 225 script labels.** Script roundtrip: byte-identical.

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
0x00, 0x2D, 0x00, 0x00, 0x00
0x08, 0x2B, 0x00, 0x01, 0x00
0x05, 0x28, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 29 | 20 | 0 |
| 5 | 30 | 220 | 34 |
| 8 | 50 | 240 | 41 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 5 | 601 | 60 / 1 | 6 | 3 | trigger_event(602); stop |
| 5 | 602 | 60 / 2 | 6 | 3 | trigger_event(603); stop |
| 5 | 603 | 60 / 3 | 8 | 3 | trigger_event(604); stop |
| 5 | 604 | 60 / 4 | 8 | 3 | trigger_event(605); stop |
| 5 | 605 | 60 / 5 | 8 | 3 | trigger_event(606); stop |
| 5 | 606 | 60 / 6 | 8 | 3 | trigger_event(607); stop |
| 5 | 607 | 60 / 7 | 8 | 3 | set_switch(61); trigger_event(608); stop |
| 5 | 608 | 60 / 8 | 8 | 3 | trigger_event(609); stop |
| 5 | 609 | 60 / 9 | 8 | 3 | trigger_event(610); stop |
| 5 | 610 | 60 / 10 | 3 | 3 | trigger_event(611); stop |
| 5 | 611 | 60 / 11 | 3 | 3 | trigger_event(612); stop |
| 5 | 612 | 60 / 12 | 5 | 3 | trigger_event(613); stop |
| 5 | 613 | 60 / 13 | 8 | 3 | trigger_event(614); stop |
| 5 | 614 | 60 / 14 | 2 | 3 | trigger_event(615); stop |
| 5 | 615 | 60 / 15 | 8 | 3 | trigger_event(616); stop |
| 5 | 616 | 60 / 16 | 3 | 3 | stop |
| 5 | 401 | 40 / 1 | 8 | 3 | trigger_event(402); stop |
| 5 | 402 | 40 / 2 | 8 | 3 | trigger_event(403); stop |
| 5 | 403 | 40 / 3 | 5 | 3 | trigger_event(404); stop |
| 5 | 404 | 40 / 4 | 7 | 3 | trigger_event(405); stop |
| 5 | 405 | 40 / 5 | 7 | 3 | trigger_event(406); stop |
| 5 | 406 | 40 / 6 | 8 | 3 | trigger_event(407); stop |
| 5 | 407 | 40 / 7 | 8 | 3 | trigger_event(408); stop |
| 5 | 408 | 40 / 8 | 5 | 3 | trigger_event(409); stop |
| 5 | 409 | 40 / 9 | 7 | 3 | trigger_event(410); stop |
| 5 | 410 | 40 / 10 | 7 | 3 | trigger_event(411); stop |
| 5 | 411 | 40 / 11 | 8 | 3 | trigger_event(412); stop |
| 5 | 412 | 40 / 12 | 8 | 3 | trigger_event(413); stop |
| 5 | 413 | 40 / 13 | 5 | 3 | trigger_event(414); stop |
| 5 | 414 | 40 / 14 | 7 | 3 | trigger_event(415); stop |
| 5 | 415 | 40 / 15 | 7 | 3 | trigger_event(416); stop |
| 5 | 416 | 40 / 16 | 5 | 3 | trigger_event(417); stop |
| 5 | 417 | 40 / 17 | 5 | 3 | trigger_event(418); stop |
| 5 | 418 | 40 / 18 | 5 | 3 | stop |
| 8 | 901 | 90 / 1 | 6 | 3 | trigger_event(902); stop |
| 8 | 902 | 90 / 2 | 8 | 3 | trigger_event(903); stop |
| 8 | 903 | 90 / 3 | 7 | 3 | trigger_event(904); stop |
| 8 | 904 | 90 / 4 | 8 | 3 | trigger_event(905); stop |
| 8 | 905 | 90 / 5 | 7 | 3 | set_switch(90); stop |
| 8 | 701 | 70 / 1 | 8 | 3 | trigger_event(702); stop |
| 8 | 702 | 70 / 2 | 8 | 3 | trigger_event(703); stop |
| 8 | 703 | 70 / 3 | 8 | 3 | construct_objects(room=70,group_or_wave=1); stop |
| 8 | 704 | 70 / 4 | 8 | 3 | trigger_event(705); stop |
| 8 | 705 | 70 / 5 | 5 | 3 | trigger_event(706); stop |
| 8 | 706 | 70 / 6 | 6 | 3 | trigger_event(707); stop |
| 8 | 707 | 70 / 7 | 1 | 3 | set_switch(122); stop |
| 8 | 511 | 51 / 1 | 5 | 3 | trigger_event(512); stop |
| 8 | 512 | 51 / 2 | 7 | 3 | trigger_event(513); stop |
| 8 | 513 | 51 / 3 | 3 | 3 | trigger_event(514); stop |
| 8 | 514 | 51 / 4 | 8 | 3 | trigger_event(515); stop |
| 8 | 515 | 51 / 5 | 5 | 3 | trigger_event(516); stop |
| 8 | 516 | 51 / 6 | 7 | 3 | set_switch(51); stop |
| 8 | 1011 | 101 / 1 | 8 | 3 | trigger_event(1012); stop |
| 8 | 1012 | 101 / 2 | 8 | 3 | trigger_event(1013); stop |
| 8 | 1013 | 101 / 3 | 6 | 3 | trigger_event(1014); stop |
| 8 | 1014 | 101 / 4 | 3 | 3 | set_switch(101); stop |
| 8 | 421 | 42 / 1 | 3 | 3 | trigger_event(422); stop |
| 8 | 422 | 42 / 2 | 6 | 3 | trigger_event(423); stop |
| 8 | 423 | 42 / 3 | 3 | 3 | trigger_event(424); stop |
| 8 | 424 | 42 / 4 | 6 | 3 | trigger_event(425); stop |
| 8 | 425 | 42 / 5 | 2 | 3 | set_switch(42); stop |
| 8 | 1101 | 110 / 1 | 6 | 3 | trigger_event(1102); stop |
| 8 | 1102 | 110 / 2 | 6 | 3 | trigger_event(1103); stop |
| 8 | 1103 | 110 / 3 | 3 | 3 | trigger_event(1104); stop |
| 8 | 1104 | 110 / 4 | 3 | 3 | trigger_event(1105); stop |
| 8 | 1105 | 110 / 5 | 8 | 3 | trigger_event(1106); stop |
| 8 | 1106 | 110 / 6 | 7 | 3 | trigger_event(1107); stop |
| 8 | 1107 | 110 / 7 | 7 | 3 | trigger_event(1108); stop |
| 8 | 1108 | 110 / 8 | 5 | 3 | trigger_event(1109); stop |
| 8 | 1109 | 110 / 9 | 8 | 3 | trigger_event(1110); stop |
| 8 | 1110 | 110 / 10 | 4 | 3 | trigger_event(1111); stop |
| 8 | 1111 | 110 / 11 | 7 | 3 | trigger_event(1112); stop |
| 8 | 1112 | 110 / 12 | 7 | 3 | trigger_event(1113); stop |
| 8 | 1113 | 110 / 13 | 6 | 3 | trigger_event(1114); stop |
| 8 | 1114 | 110 / 14 | 3 | 3 | set_switch(192); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
