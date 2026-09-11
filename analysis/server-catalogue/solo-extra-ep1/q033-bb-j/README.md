# パイオニア・スピリッツ — solo-extra-ep1/q033-bb-j

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/solo-extra-ep1/q033-bb-j.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/solo-extra-ep1/q033-bb-j.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/solo-extra-ep1/q033-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode4; header quest ID 33; language J. Static scan: **358 objects, 291 enemy/NPC records, 81 events, 296 script labels.** Script roundtrip: byte-identical.

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
0x05, 0x28, 0x00, 0x00, 0x00
0x08, 0x2B, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 27 | 0 |
| 5 | 232 | 85 | 40 |
| 8 | 100 | 179 | 41 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 5 | 201 | 20 / 99 | 0 | 30 | trigger_event(2001); trigger_event(2002); trigger_event(2003); stop |
| 5 | 2001 | 20 / 1 | 2 | 30 | trigger_event(204); stop |
| 5 | 2002 | 20 / 2 | 1 | 30 | trigger_event(205); stop |
| 5 | 2003 | 20 / 3 | 2 | 30 | trigger_event(206); stop |
| 5 | 204 | 20 / 4 | 1 | 30 | trigger_event(207); stop |
| 5 | 205 | 20 / 5 | 2 | 30 | trigger_event(208); stop |
| 5 | 206 | 20 / 6 | 3 | 30 | trigger_event(209); stop |
| 5 | 207 | 20 / 7 | 2 | 30 | trigger_event(210); stop |
| 5 | 208 | 20 / 8 | 3 | 30 | trigger_event(211); stop |
| 5 | 209 | 20 / 9 | 3 | 30 | trigger_event(212); stop |
| 5 | 210 | 20 / 10 | 1 | 30 | set_switch(21); stop |
| 5 | 211 | 20 / 11 | 3 | 30 | set_switch(22); stop |
| 5 | 212 | 20 / 12 | 1 | 30 | set_switch(23); stop |
| 5 | 301 | 30 / 1 | 1 | 30 | trigger_event(3011); stop |
| 5 | 3011 | 30 / 2 | 5 | 30 | trigger_event(3012); stop |
| 5 | 3012 | 30 / 3 | 3 | 30 | construct_objects(room=30,group_or_wave=1); stop |
| 5 | 302 | 30 / 4 | 7 | 30 | construct_objects(room=30,group_or_wave=2); stop |
| 5 | 303 | 30 / 5 | 5 | 30 | trigger_event(3031); stop |
| 5 | 3031 | 30 / 6 | 3 | 30 | construct_objects(room=30,group_or_wave=3); stop |
| 5 | 304 | 30 / 6 | 3 | 30 | trigger_event(3041); stop |
| 5 | 3041 | 30 / 7 | 4 | 30 | trigger_event(3042); stop |
| 5 | 3042 | 30 / 8 | 3 | 30 | trigger_event(3043); stop |
| 5 | 3043 | 30 / 9 | 1 | 30 | set_switch(31); stop |
| 5 | 401 | 40 / 99 | 0 | 30 | trigger_event(4001); trigger_event(4002); trigger_event(4003); trigger_event(4004); stop |
| 5 | 4001 | 40 / 1 | 1 | 30 | trigger_event(405); stop |
| 5 | 4002 | 40 / 2 | 1 | 30 | trigger_event(406); stop |
| 5 | 4003 | 40 / 3 | 1 | 30 | trigger_event(407); stop |
| 5 | 4004 | 40 / 4 | 1 | 30 | trigger_event(408); stop |
| 5 | 405 | 40 / 5 | 2 | 30 | trigger_event(409); stop |
| 5 | 406 | 40 / 6 | 3 | 30 | trigger_event(410); stop |
| 5 | 407 | 40 / 7 | 1 | 30 | trigger_event(411); stop |
| 5 | 408 | 40 / 8 | 2 | 30 | trigger_event(412); stop |
| 5 | 409 | 40 / 9 | 2 | 30 | trigger_event(413); stop |
| 5 | 410 | 40 / 10 | 1 | 30 | trigger_event(414); stop |
| 5 | 411 | 40 / 11 | 3 | 30 | trigger_event(415); stop |
| 5 | 412 | 40 / 12 | 2 | 30 | trigger_event(416); stop |
| 5 | 413 | 40 / 13 | 1 | 30 | set_switch(41); stop |
| 5 | 414 | 40 / 14 | 3 | 30 | set_switch(42); stop |
| 5 | 415 | 40 / 15 | 3 | 30 | set_switch(43); stop |
| 5 | 416 | 40 / 16 | 1 | 30 | set_switch(44); stop |
| 8 | 201 | 20 / 1 | 3 | 30 | trigger_event(202); stop |
| 8 | 202 | 20 / 2 | 3 | 30 | trigger_event(203); stop |
| 8 | 203 | 20 / 3 | 4 | 30 | trigger_event(204); stop |
| 8 | 204 | 20 / 4 | 6 | 30 | trigger_event(205); stop |
| 8 | 205 | 20 / 5 | 7 | 30 | set_switch(20); stop |
| 8 | 401 | 40 / 1 | 2 | 30 | trigger_event(402); stop |
| 8 | 402 | 40 / 2 | 6 | 30 | trigger_event(403); stop |
| 8 | 403 | 40 / 3 | 5 | 30 | set_switch(40); stop |
| 8 | 421 | 42 / 1 | 2 | 30 | trigger_event(422); stop |
| 8 | 422 | 42 / 2 | 8 | 30 | trigger_event(423); stop |
| 8 | 423 | 42 / 3 | 8 | 30 | set_switch(42); stop |
| 8 | 501 | 50 / 1 | 5 | 30 | trigger_event(502); stop |
| 8 | 502 | 50 / 2 | 5 | 30 | trigger_event(503); stop |
| 8 | 503 | 50 / 3 | 3 | 30 | trigger_event(504); stop |
| 8 | 504 | 50 / 4 | 4 | 30 | set_switch(50); set_switch(72); stop |
| 8 | 511 | 51 / 1 | 5 | 30 | trigger_event(512); stop |
| 8 | 512 | 51 / 2 | 5 | 30 | trigger_event(513); stop |
| 8 | 513 | 51 / 3 | 6 | 30 | set_switch(51); stop |
| 8 | 601 | 60 / 1 | 4 | 30 | trigger_event(602); stop |
| 8 | 602 | 60 / 2 | 4 | 30 | trigger_event(603); stop |
| 8 | 603 | 60 / 3 | 4 | 30 | set_switch(60); stop |
| 8 | 701 | 70 / 99 | 0 | 30 | trigger_event(7001); trigger_event(7002); trigger_event(7003); stop |
| 8 | 7001 | 70 / 1 | 1 | 30 | trigger_event(704); stop |
| 8 | 7002 | 70 / 2 | 2 | 30 | trigger_event(705); stop |
| 8 | 7003 | 70 / 3 | 3 | 30 | trigger_event(706); stop |
| 8 | 704 | 70 / 4 | 2 | 30 | trigger_event(707); stop |
| 8 | 705 | 70 / 5 | 4 | 30 | trigger_event(708); stop |
| 8 | 706 | 70 / 6 | 4 | 30 | trigger_event(709); stop |
| 8 | 707 | 70 / 7 | 3 | 30 | set_switch(74); stop |
| 8 | 708 | 70 / 8 | 3 | 30 | set_switch(75); stop |
| 8 | 709 | 70 / 9 | 1 | 30 | set_switch(76); stop |
| 8 | 1001 | 100 / 1 | 3 | 30 | trigger_event(1002); stop |
| 8 | 1002 | 100 / 2 | 3 | 30 | trigger_event(1003); stop |
| 8 | 1003 | 100 / 3 | 5 | 30 | set_switch(100); stop |
| 8 | 1101 | 110 / 1 | 5 | 30 | trigger_event(1102); trigger_event(1103); stop |
| 8 | 1102 | 110 / 2 | 4 | 30 | trigger_event(1104); stop |
| 8 | 1103 | 110 / 3 | 4 | 30 | trigger_event(1105); stop |
| 8 | 1104 | 110 / 4 | 5 | 30 | trigger_event(1106); stop |
| 8 | 1105 | 110 / 5 | 5 | 30 | trigger_event(1107); stop |
| 8 | 1106 | 110 / 6 | 5 | 30 | set_switch(111); stop |
| 8 | 1107 | 110 / 7 | 3 | 30 | set_switch(112); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
