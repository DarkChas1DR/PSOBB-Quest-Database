# 極幻の戦火へ ５ — extermination-ep4/q815-bb-j

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/extermination-ep4/q815-bb-j.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/extermination-ep4/q815-bb-j.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/extermination-ep4/q815-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode4; header quest ID 815; language J. Static scan: **216 objects, 255 enemy/NPC records, 81 events, 87 script labels.** Script roundtrip: byte-identical.

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
0x08, 0x2B, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 17 | 0 |
| 8 | 190 | 238 | 81 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 8 | 201 | 20 / 99 | 0 | 30 | trigger_event(2001); trigger_event(2002); trigger_event(2003); stop |
| 8 | 2001 | 20 / 1 | 1 | 30 | trigger_event(204); stop |
| 8 | 2002 | 20 / 2 | 1 | 30 | trigger_event(205); stop |
| 8 | 2003 | 20 / 3 | 1 | 30 | trigger_event(206); stop |
| 8 | 204 | 20 / 4 | 2 | 30 | trigger_event(207); stop |
| 8 | 205 | 20 / 5 | 2 | 30 | trigger_event(208); stop |
| 8 | 206 | 20 / 6 | 3 | 30 | trigger_event(209); stop |
| 8 | 207 | 20 / 7 | 3 | 30 | trigger_event(2010); stop |
| 8 | 208 | 20 / 8 | 1 | 30 | trigger_event(2011); stop |
| 8 | 209 | 20 / 9 | 9 | 30 | trigger_event(2012); stop |
| 8 | 2010 | 20 / 10 | 5 | 30 | trigger_event(2013); stop |
| 8 | 2011 | 20 / 11 | 1 | 30 | trigger_event(2014); stop |
| 8 | 2012 | 20 / 12 | 3 | 30 | trigger_event(2015); stop |
| 8 | 2013 | 20 / 13 | 3 | 30 | set_switch(22); stop |
| 8 | 2014 | 20 / 14 | 3 | 30 | set_switch(23); stop |
| 8 | 2015 | 20 / 15 | 2 | 30 | set_switch(24); stop |
| 8 | 211 | 21 / 99 | 0 | 30 | trigger_event(2111); trigger_event(2112); trigger_event(2113); stop |
| 8 | 2111 | 21 / 1 | 1 | 30 | trigger_event(214); stop |
| 8 | 2112 | 21 / 2 | 1 | 30 | trigger_event(215); stop |
| 8 | 2113 | 21 / 3 | 1 | 30 | trigger_event(216); stop |
| 8 | 214 | 21 / 4 | 1 | 30 | trigger_event(217); stop |
| 8 | 215 | 21 / 5 | 2 | 30 | trigger_event(218); stop |
| 8 | 216 | 21 / 6 | 2 | 30 | trigger_event(219); stop |
| 8 | 217 | 21 / 7 | 3 | 30 | set_switch(25); stop |
| 8 | 218 | 21 / 8 | 5 | 30 | set_switch(26); stop |
| 8 | 219 | 21 / 9 | 1 | 30 | set_switch(27); stop |
| 8 | 401 | 40 / 1 | 3 | 30 | trigger_event(402); stop |
| 8 | 402 | 40 / 2 | 5 | 30 | trigger_event(403); stop |
| 8 | 403 | 40 / 3 | 4 | 30 | set_switch(40); construct_objects(room=40,group_or_wave=1); stop |
| 8 | 411 | 41 / 1 | 3 | 30 | trigger_event(412); stop |
| 8 | 412 | 41 / 2 | 6 | 30 | trigger_event(413); stop |
| 8 | 413 | 41 / 3 | 5 | 30 | set_switch(41); stop |
| 8 | 421 | 42 / 1 | 3 | 30 | trigger_event(422); stop |
| 8 | 422 | 42 / 2 | 8 | 30 | trigger_event(423); stop |
| 8 | 423 | 42 / 3 | 7 | 30 | set_switch(42); stop |
| 8 | 501 | 50 / 1 | 3 | 30 | trigger_event(502); stop |
| 8 | 502 | 50 / 2 | 1 | 30 | trigger_event(503); stop |
| 8 | 503 | 50 / 3 | 3 | 30 | set_switch(50); stop |
| 8 | 511 | 51 / 1 | 6 | 30 | trigger_event(513); stop |
| 8 | 513 | 51 / 2 | 3 | 30 | construct_objects(room=51,group_or_wave=1); stop |
| 8 | 512 | 51 / 3 | 2 | 30 | trigger_event(514); stop |
| 8 | 514 | 51 / 4 | 6 | 30 | set_switch(51); stop |
| 8 | 601 | 60 / 1 | 1 | 30 | trigger_event(602); stop |
| 8 | 602 | 60 / 2 | 4 | 30 | trigger_event(603); stop |
| 8 | 603 | 60 / 3 | 4 | 30 | set_switch(60); stop |
| 8 | 611 | 61 / 1 | 5 | 30 | trigger_event(612); stop |
| 8 | 612 | 61 / 2 | 3 | 30 | trigger_event(613); stop |
| 8 | 613 | 61 / 3 | 4 | 30 | set_switch(61); stop |
| 8 | 701 | 70 / 99 | 0 | 30 | trigger_event(7011); trigger_event(7012); trigger_event(7013); stop |
| 8 | 7011 | 70 / 1 | 1 | 30 | trigger_event(704); stop |
| 8 | 7012 | 70 / 2 | 1 | 30 | trigger_event(705); stop |
| 8 | 7013 | 70 / 3 | 1 | 30 | trigger_event(706); stop |
| 8 | 704 | 70 / 4 | 3 | 30 | trigger_event(707); stop |
| 8 | 705 | 70 / 5 | 3 | 30 | trigger_event(708); stop |
| 8 | 706 | 70 / 6 | 3 | 30 | trigger_event(709); stop |
| 8 | 707 | 70 / 7 | 1 | 30 | set_switch(71); stop |
| 8 | 708 | 70 / 8 | 6 | 30 | set_switch(72); stop |
| 8 | 709 | 70 / 9 | 2 | 30 | set_switch(73); stop |
| 8 | 801 | 80 / 1 | 4 | 30 | stop |
| 8 | 802 | 80 / 2 | 6 | 30 | stop |
| 8 | 803 | 80 / 3 | 4 | 30 | set_switch(80); stop |
| 8 | 1001 | 100 / 1 | 5 | 30 | trigger_event(1002); stop |
| 8 | 1002 | 100 / 2 | 4 | 30 | trigger_event(1003); stop |
| 8 | 1003 | 100 / 3 | 7 | 30 | set_switch(100); stop |
| 8 | 1101 | 110 / 99 | 0 | 30 | trigger_event(1111); trigger_event(1112); trigger_event(1113); stop |
| 8 | 1111 | 110 / 1 | 1 | 30 | trigger_event(1104); stop |
| 8 | 1112 | 110 / 2 | 2 | 30 | trigger_event(1105); stop |
| 8 | 1113 | 110 / 3 | 1 | 30 | trigger_event(1106); stop |
| 8 | 1104 | 110 / 4 | 2 | 30 | trigger_event(1107); stop |
| 8 | 1105 | 110 / 5 | 3 | 30 | trigger_event(1108); stop |
| 8 | 1106 | 110 / 6 | 1 | 30 | trigger_event(1109); stop |
| 8 | 1107 | 110 / 7 | 3 | 30 | trigger_event(11010); stop |
| 8 | 1108 | 110 / 8 | 2 | 30 | trigger_event(11011); stop |
| 8 | 1109 | 110 / 9 | 2 | 30 | trigger_event(11012); stop |
| 8 | 11010 | 110 / 10 | 3 | 30 | trigger_event(11013); stop |
| 8 | 11011 | 110 / 11 | 4 | 30 | trigger_event(11014); stop |
| 8 | 11012 | 110 / 12 | 2 | 30 | trigger_event(11015); stop |
| 8 | 11013 | 110 / 13 | 3 | 30 | set_switch(111); stop |
| 8 | 11014 | 110 / 14 | 7 | 30 | set_switch(112); stop |
| 8 | 11015 | 110 / 15 | 3 | 30 | trigger_event(11016); stop |
| 8 | 11016 | 110 / 16 | 2 | 30 | set_switch(113); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
