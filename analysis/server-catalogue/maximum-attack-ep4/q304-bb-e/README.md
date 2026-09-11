# Maximum Attack 4th Stage -4B- — maximum-attack-ep4/q304-bb-e

Episode4; header quest ID 304; language E. Static scan: **108 objects, 420 enemy/NPC records, 67 events, 223 script labels.** Script roundtrip: byte-identical.

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
| 5 | 30 | 200 | 32 |
| 8 | 49 | 200 | 35 |

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
| 5 | 301 | 30 / 1 | 5 | 3 | trigger_event(302); stop |
| 5 | 302 | 30 / 2 | 5 | 3 | trigger_event(303); stop |
| 5 | 303 | 30 / 3 | 5 | 3 | trigger_event(304); stop |
| 5 | 304 | 30 / 4 | 5 | 3 | trigger_event(305); stop |
| 5 | 305 | 30 / 5 | 8 | 3 | trigger_event(306); stop |
| 5 | 306 | 30 / 6 | 8 | 3 | trigger_event(307); stop |
| 5 | 307 | 30 / 7 | 8 | 3 | trigger_event(308); stop |
| 5 | 308 | 30 / 8 | 6 | 3 | trigger_event(309); stop |
| 5 | 309 | 30 / 9 | 5 | 3 | trigger_event(310); stop |
| 5 | 310 | 30 / 10 | 8 | 3 | trigger_event(311); stop |
| 5 | 311 | 30 / 11 | 8 | 3 | trigger_event(312); stop |
| 5 | 312 | 30 / 12 | 8 | 3 | trigger_event(313); stop |
| 5 | 313 | 30 / 13 | 8 | 3 | trigger_event(314); stop |
| 5 | 314 | 30 / 14 | 4 | 3 | trigger_event(315); stop |
| 5 | 315 | 30 / 15 | 4 | 3 | trigger_event(316); stop |
| 5 | 316 | 30 / 16 | 5 | 3 | stop |
| 8 | 901 | 90 / 1 | 6 | 3 | trigger_event(902); stop |
| 8 | 902 | 90 / 2 | 8 | 3 | trigger_event(903); stop |
| 8 | 903 | 90 / 3 | 7 | 3 | trigger_event(904); stop |
| 8 | 904 | 90 / 4 | 8 | 3 | trigger_event(905); stop |
| 8 | 905 | 90 / 5 | 7 | 3 | set_switch(90); stop |
| 8 | 701 | 70 / 1 | 8 | 3 | trigger_event(702); stop |
| 8 | 702 | 70 / 2 | 8 | 3 | trigger_event(703); stop |
| 8 | 703 | 70 / 3 | 8 | 3 | construct_objects(room=70,group_or_wave=1); stop |
| 8 | 704 | 70 / 4 | 8 | 3 | trigger_event(705); stop |
| 8 | 705 | 70 / 5 | 8 | 3 | trigger_event(706); stop |
| 8 | 706 | 70 / 6 | 4 | 3 | trigger_event(707); stop |
| 8 | 707 | 70 / 7 | 5 | 3 | set_switch(71); stop |
| 8 | 801 | 80 / 1 | 5 | 3 | trigger_event(802); stop |
| 8 | 802 | 80 / 2 | 5 | 3 | trigger_event(803); stop |
| 8 | 803 | 80 / 3 | 5 | 3 | construct_objects(room=80,group_or_wave=1); stop |
| 8 | 804 | 80 / 4 | 6 | 3 | trigger_event(805); stop |
| 8 | 805 | 80 / 5 | 8 | 3 | trigger_event(806); stop |
| 8 | 806 | 80 / 6 | 6 | 3 | construct_objects(room=80,group_or_wave=2); stop |
| 8 | 807 | 80 / 7 | 2 | 3 | trigger_event(808); stop |
| 8 | 808 | 80 / 8 | 5 | 3 | trigger_event(809); stop |
| 8 | 809 | 80 / 9 | 5 | 3 | trigger_event(8010); stop |
| 8 | 8010 | 80 / 10 | 4 | 3 | trigger_event(8011); stop |
| 8 | 8011 | 80 / 11 | 4 | 3 | set_switch(80); stop |
| 8 | 411 | 41 / 1 | 7 | 3 | trigger_event(412); stop |
| 8 | 412 | 41 / 2 | 2 | 3 | trigger_event(413); stop |
| 8 | 413 | 41 / 3 | 5 | 3 | trigger_event(414); stop |
| 8 | 414 | 41 / 4 | 3 | 3 | trigger_event(415); stop |
| 8 | 415 | 41 / 5 | 5 | 3 | trigger_event(416); stop |
| 8 | 416 | 41 / 6 | 3 | 3 | set_switch(41); stop |
| 8 | 201 | 20 / 1 | 6 | 3 | trigger_event(202); stop |
| 8 | 202 | 20 / 2 | 4 | 3 | trigger_event(203); stop |
| 8 | 203 | 20 / 3 | 8 | 3 | trigger_event(204); stop |
| 8 | 204 | 20 / 4 | 8 | 3 | trigger_event(205); stop |
| 8 | 205 | 20 / 5 | 3 | 3 | trigger_event(206); stop |
| 8 | 206 | 20 / 6 | 6 | 3 | set_switch(20); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

A backup is present; decompressed content identical: True. See [text differences](<backup-diff.txt>).

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
