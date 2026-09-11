# Point of Disaster — team-ep4/q709-bb-e

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/team-ep4/q709-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/team-ep4/q709-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/team-ep4/q709-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode4; header quest ID 709; language E. Static scan: **339 objects, 278 enemy/NPC records, 107 events, 158 script labels.** Script roundtrip: byte-identical.

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
0x01, 0x24, 0x00, 0x00, 0x00
0x05, 0x28, 0x00, 0x00, 0x00
0x08, 0x2B, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 22 | 0 |
| 1 | 108 | 99 | 41 |
| 5 | 103 | 93 | 37 |
| 8 | 60 | 63 | 29 |
| 9 | 42 | 1 | 0 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 101 | 10 / 1 | 4 | 30 | trigger_event(102); stop |
| 1 | 102 | 10 / 2 | 5 | 30 | trigger_event(103); stop |
| 1 | 103 | 10 / 3 | 4 | 30 | set_switch(10); stop |
| 1 | 201 | 20 / 99 | 0 | 30 | trigger_event(2011); trigger_event(2012); trigger_event(2013); trigger_event(2014); stop |
| 1 | 2011 | 20 / 1 | 2 | 30 | trigger_event(202); stop |
| 1 | 2012 | 20 / 2 | 2 | 30 | trigger_event(203); stop |
| 1 | 2013 | 20 / 3 | 2 | 30 | trigger_event(204); stop |
| 1 | 2014 | 20 / 4 | 3 | 30 | set_switch(201); stop |
| 1 | 202 | 20 / 5 | 5 | 30 | trigger_event(205); stop |
| 1 | 203 | 20 / 6 | 1 | 30 | set_switch(202); stop |
| 1 | 204 | 20 / 7 | 4 | 30 | trigger_event(206); stop |
| 1 | 205 | 20 / 8 | 6 | 30 | trigger_event(207); stop |
| 1 | 206 | 20 / 9 | 2 | 30 | trigger_event(208); stop |
| 1 | 207 | 20 / 10 | 1 | 30 | set_switch(203); stop |
| 1 | 208 | 20 / 11 | 4 | 30 | trigger_event(209); stop |
| 1 | 209 | 20 / 12 | 4 | 30 | trigger_event(2010); stop |
| 1 | 2010 | 20 / 13 | 3 | 30 | set_switch(204); stop |
| 1 | 501 | 50 / 99 | 0 | 30 | trigger_event(5011); trigger_event(5012); trigger_event(5013); trigger_event(5014); trigger_event(5015); stop |
| 1 | 5011 | 50 / 1 | 2 | 30 | trigger_event(502); stop |
| 1 | 5012 | 50 / 2 | 3 | 30 | trigger_event(503); stop |
| 1 | 5013 | 50 / 3 | 2 | 30 | trigger_event(504); stop |
| 1 | 5014 | 50 / 4 | 1 | 30 | trigger_event(505); stop |
| 1 | 5015 | 50 / 5 | 1 | 30 | trigger_event(506); stop |
| 1 | 502 | 50 / 6 | 2 | 30 | trigger_event(507); stop |
| 1 | 503 | 50 / 7 | 4 | 30 | set_switch(56); stop |
| 1 | 504 | 50 / 8 | 1 | 30 | set_switch(52); stop |
| 1 | 505 | 50 / 9 | 3 | 30 | set_switch(53); stop |
| 1 | 506 | 50 / 10 | 4 | 30 | set_switch(54); stop |
| 1 | 507 | 50 / 11 | 3 | 30 | set_switch(55); stop |
| 1 | 508 | 50 / 12 | 4 | 30 | construct_objects(room=50,group_or_wave=9); stop |
| 1 | 509 | 50 / 13 | 3 | 30 | construct_objects(room=50,group_or_wave=10); set_switch(51); stop |
| 1 | 601 | 60 / 99 | 0 | 30 | trigger_event(6011); trigger_event(6012); trigger_event(6013); stop |
| 1 | 6011 | 60 / 1 | 1 | 30 | trigger_event(602); stop |
| 1 | 6012 | 60 / 2 | 2 | 30 | trigger_event(603); stop |
| 1 | 6013 | 60 / 3 | 1 | 30 | trigger_event(604); stop |
| 1 | 602 | 60 / 4 | 1 | 30 | trigger_event(605); stop |
| 1 | 603 | 60 / 5 | 2 | 30 | trigger_event(606); stop |
| 1 | 604 | 60 / 6 | 2 | 30 | trigger_event(607); stop |
| 1 | 605 | 60 / 7 | 1 | 30 | set_switch(61); stop |
| 1 | 606 | 60 / 8 | 2 | 30 | set_switch(62); stop |
| 1 | 607 | 60 / 9 | 1 | 30 | set_switch(63); stop |
| 5 | 401 | 40 / 99 | 0 | 30 | trigger_event(4001); trigger_event(4002); trigger_event(4003); stop |
| 5 | 4001 | 40 / 1 | 1 | 30 | trigger_event(404); stop |
| 5 | 4002 | 40 / 2 | 2 | 30 | trigger_event(405); stop |
| 5 | 4003 | 40 / 3 | 2 | 30 | trigger_event(406); stop |
| 5 | 404 | 40 / 4 | 2 | 30 | trigger_event(407); stop |
| 5 | 405 | 40 / 5 | 2 | 30 | trigger_event(408); stop |
| 5 | 406 | 40 / 6 | 3 | 30 | trigger_event(409); stop |
| 5 | 407 | 40 / 7 | 5 | 30 | trigger_event(4010); stop |
| 5 | 408 | 40 / 8 | 5 | 30 | set_switch(41); stop |
| 5 | 409 | 40 / 9 | 2 | 30 | trigger_event(4011); stop |
| 5 | 4010 | 40 / 10 | 1 | 30 | trigger_event(4012); stop |
| 5 | 4011 | 40 / 11 | 8 | 30 | trigger_event(4013); stop |
| 5 | 4012 | 40 / 12 | 1 | 30 | trigger_event(4014); stop |
| 5 | 4013 | 40 / 13 | 2 | 30 | trigger_event(4015); stop |
| 5 | 4014 | 40 / 14 | 2 | 30 | trigger_event(4016); stop |
| 5 | 4015 | 40 / 15 | 3 | 30 | trigger_event(4017); stop |
| 5 | 4016 | 40 / 16 | 3 | 30 | trigger_event(4018); stop |
| 5 | 4017 | 40 / 17 | 4 | 30 | trigger_event(4019); stop |
| 5 | 4018 | 40 / 18 | 4 | 30 | trigger_event(4020); stop |
| 5 | 4019 | 40 / 19 | 5 | 30 | set_switch(42); stop |
| 5 | 4020 | 40 / 20 | 9 | 30 | set_switch(43); stop |
| 5 | 601 | 60 / 99 | 0 | 30 | trigger_event(6001); trigger_event(6002); trigger_event(6003); stop |
| 5 | 6001 | 60 / 1 | 1 | 30 | trigger_event(604); stop |
| 5 | 6002 | 60 / 2 | 1 | 30 | trigger_event(605); stop |
| 5 | 6003 | 60 / 3 | 2 | 30 | set_switch(62); stop |
| 5 | 604 | 60 / 4 | 2 | 30 | trigger_event(606); stop |
| 5 | 605 | 60 / 5 | 1 | 30 | trigger_event(607); stop |
| 5 | 606 | 60 / 6 | 1 | 30 | trigger_event(608); stop |
| 5 | 607 | 60 / 7 | 2 | 30 | trigger_event(609); stop |
| 5 | 608 | 60 / 8 | 3 | 30 | trigger_event(6010); stop |
| 5 | 609 | 60 / 9 | 1 | 30 | trigger_event(6011); stop |
| 5 | 6010 | 60 / 10 | 3 | 30 | trigger_event(6012); trigger_event(6013); stop |
| 5 | 6011 | 60 / 11 | 2 | 30 | set_switch(63); stop |
| 5 | 6012 | 60 / 12 | 2 | 30 | trigger_event(6014); stop |
| 5 | 6013 | 60 / 13 | 3 | 30 | trigger_event(6015); stop |
| 5 | 6014 | 60 / 14 | 1 | 30 | set_switch(64); stop |
| 5 | 6015 | 60 / 15 | 1 | 30 | set_switch(65); stop |
| 8 | 421 | 42 / 1 | 4 | 30 | trigger_event(422); stop |
| 8 | 422 | 42 / 2 | 4 | 30 | trigger_event(423); set_switch(42); stop |
| 8 | 511 | 51 / 1 | 3 | 30 | trigger_event(512); stop |
| 8 | 512 | 51 / 2 | 3 | 30 | trigger_event(513); stop |
| 8 | 513 | 51 / 3 | 1 | 30 | trigger_event(514); stop |
| 8 | 514 | 51 / 4 | 5 | 30 | trigger_event(515); set_switch(51); stop |
| 8 | 701 | 70 / 99 | 0 | 30 | trigger_event(7001); trigger_event(7002); trigger_event(7003); stop |
| 8 | 7001 | 70 / 1 | 1 | 30 | trigger_event(704); stop |
| 8 | 7002 | 70 / 2 | 1 | 30 | trigger_event(705); stop |
| 8 | 7003 | 70 / 3 | 1 | 30 | trigger_event(706); stop |
| 8 | 704 | 70 / 4 | 3 | 30 | trigger_event(707); stop |
| 8 | 705 | 70 / 5 | 3 | 30 | trigger_event(708); stop |
| 8 | 706 | 70 / 6 | 1 | 30 | trigger_event(709); stop |
| 8 | 707 | 70 / 7 | 3 | 30 | trigger_event(7010); stop |
| 8 | 708 | 70 / 8 | 2 | 30 | trigger_event(7011); stop |
| 8 | 709 | 70 / 9 | 1 | 30 | set_switch(71); stop |
| 8 | 7010 | 70 / 10 | 4 | 30 | set_switch(72); stop |
| 8 | 7011 | 70 / 11 | 5 | 30 | set_switch(73); stop |
| 8 | 101 | 100 / 99 | 0 | 30 | trigger_event(1001); trigger_event(1002); trigger_event(1003); stop |
| 8 | 1001 | 100 / 1 | 1 | 30 | trigger_event(1004); stop |
| 8 | 1002 | 100 / 2 | 1 | 30 | set_switch(101); stop |
| 8 | 1003 | 100 / 3 | 1 | 30 | trigger_event(1005); stop |
| 8 | 1004 | 100 / 4 | 2 | 30 | set_switch(102); stop |
| 8 | 1005 | 100 / 5 | 2 | 30 | trigger_event(1006); trigger_event(1007); trigger_event(1008); stop |
| 8 | 1006 | 100 / 6 | 1 | 30 | trigger_event(1009); stop |
| 8 | 1007 | 100 / 7 | 2 | 30 | trigger_event(1010); stop |
| 8 | 1008 | 100 / 8 | 1 | 30 | set_switch(103); stop |
| 8 | 1009 | 100 / 9 | 2 | 30 | set_switch(104); stop |
| 8 | 1010 | 100 / 10 | 3 | 30 | set_switch(105); stop |

## Review notes

- Floor 8: event 422 targets absent event 423
- Floor 8: event 514 targets absent event 515

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
