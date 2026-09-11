# 戦士の誇り — solo-extra-ep1/q030-bb-j

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/solo-extra-ep1/q030-bb-j.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/solo-extra-ep1/q030-bb-j.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/solo-extra-ep1/q030-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode4; header quest ID 30; language J. Static scan: **358 objects, 353 enemy/NPC records, 73 events, 327 script labels.** Script roundtrip: alignment-only.

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
0x03, 0x26, 0x00, 0x00, 0x00
0x05, 0x28, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 24 | 0 |
| 3 | 83 | 106 | 29 |
| 5 | 249 | 223 | 44 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 3 | 201 | 20 / 99 | 0 | 30 | trigger_event(2001); trigger_event(2002); stop |
| 3 | 2001 | 20 / 1 | 2 | 30 | trigger_event(203); stop |
| 3 | 2002 | 20 / 2 | 2 | 30 | trigger_event(204); stop |
| 3 | 203 | 20 / 3 | 2 | 30 | trigger_event(205); stop |
| 3 | 204 | 20 / 4 | 2 | 30 | trigger_event(206); stop |
| 3 | 205 | 20 / 5 | 2 | 30 | trigger_event(207); stop |
| 3 | 206 | 20 / 6 | 1 | 30 | trigger_event(208); stop |
| 3 | 207 | 20 / 7 | 6 | 30 | trigger_event(209); stop |
| 3 | 208 | 20 / 8 | 1 | 30 | trigger_event(2010); stop |
| 3 | 209 | 20 / 9 | 5 | 30 | trigger_event(2011); stop |
| 3 | 2010 | 20 / 10 | 1 | 30 | set_switch(21); stop |
| 3 | 2011 | 20 / 11 | 6 | 30 | set_switch(22); stop |
| 3 | 301 | 30 / 1 | 5 | 30 | trigger_event(3001); stop |
| 3 | 3001 | 30 / 2 | 5 | 30 | set_switch(30); stop |
| 3 | 302 | 30 / 3 | 7 | 30 | trigger_event(303); stop |
| 3 | 303 | 30 / 4 | 10 | 30 | set_switch(31); stop |
| 3 | 601 | 60 / 99 | 0 | 30 | trigger_event(6011); trigger_event(6012); trigger_event(6013); stop |
| 3 | 6011 | 60 / 1 | 2 | 30 | trigger_event(604); stop |
| 3 | 6012 | 60 / 2 | 1 | 30 | trigger_event(605); stop |
| 3 | 6013 | 60 / 3 | 1 | 30 | trigger_event(606); stop |
| 3 | 604 | 60 / 4 | 3 | 30 | trigger_event(607); stop |
| 3 | 605 | 60 / 5 | 1 | 30 | set_switch(61); stop |
| 3 | 606 | 60 / 6 | 2 | 30 | set_switch(62); stop |
| 3 | 607 | 60 / 7 | 4 | 30 | set_switch(63); stop |
| 3 | 901 | 90 / 1 | 8 | 30 | trigger_event(9001); stop |
| 3 | 9001 | 90 / 2 | 7 | 30 | set_switch(90); stop |
| 3 | 902 | 90 / 3 | 4 | 30 | trigger_event(903); stop |
| 3 | 903 | 90 / 4 | 8 | 30 | trigger_event(904); stop |
| 3 | 904 | 90 / 5 | 7 | 30 | set_switch(91); stop |
| 5 | 101 | 10 / 1 | 4 | 30 | trigger_event(102); stop |
| 5 | 102 | 10 / 2 | 5 | 30 | trigger_event(103); stop |
| 5 | 103 | 10 / 3 | 9 | 30 | trigger_event(104); stop |
| 5 | 104 | 10 / 4 | 7 | 30 | trigger_event(105); stop |
| 5 | 105 | 10 / 5 | 6 | 30 | set_switch(10); stop |
| 5 | 201 | 20 / 1 | 5 | 30 | trigger_event(202); stop |
| 5 | 202 | 20 / 2 | 9 | 30 | trigger_event(203); stop |
| 5 | 203 | 20 / 2 | 9 | 30 | set_switch(20); stop |
| 5 | 301 | 30 / 99 | 0 | 30 | trigger_event(3001); trigger_event(3002); trigger_event(3003); stop |
| 5 | 3001 | 30 / 1 | 3 | 30 | trigger_event(304); stop |
| 5 | 3002 | 30 / 2 | 3 | 30 | trigger_event(305); stop |
| 5 | 3003 | 30 / 3 | 2 | 30 | trigger_event(306); stop |
| 5 | 304 | 30 / 4 | 2 | 30 | trigger_event(307); stop |
| 5 | 305 | 30 / 5 | 3 | 30 | trigger_event(308); stop |
| 5 | 306 | 30 / 6 | 3 | 30 | trigger_event(309); stop |
| 5 | 307 | 30 / 7 | 6 | 30 | set_switch(31); stop |
| 5 | 308 | 30 / 8 | 4 | 30 | set_switch(32); stop |
| 5 | 309 | 30 / 9 | 4 | 30 | set_switch(33); stop |
| 5 | 401 | 40 / 1 | 6 | 30 | construct_objects(room=40,group_or_wave=2); stop |
| 5 | 402 | 40 / 2 | 8 | 30 | construct_objects(room=40,group_or_wave=3); stop |
| 5 | 403 | 40 / 3 | 7 | 30 | construct_objects(room=40,group_or_wave=3); stop |
| 5 | 404 | 40 / 4 | 4 | 30 | set_switch(104); construct_objects(room=40,group_or_wave=4); stop |
| 5 | 405 | 40 / 5 | 5 | 30 | construct_objects(room=40,group_or_wave=5); stop |
| 5 | 410 | 40 / 6 | 7 | 30 | set_switch(40); stop |
| 5 | 501 | 50 / 1 | 6 | 30 | trigger_event(502); stop |
| 5 | 502 | 50 / 2 | 7 | 30 | trigger_event(503); stop |
| 5 | 503 | 50 / 3 | 5 | 30 | set_switch(50); stop |
| 5 | 601 | 60 / 1 | 7 | 30 | trigger_event(6012); stop |
| 5 | 6012 | 60 / 2 | 3 | 30 | trigger_event(6013); stop |
| 5 | 6013 | 60 / 3 | 6 | 30 | set_switch(62); set_switch(63); set_switch(64); stop |
| 5 | 602 | 60 / 99 | 0 | 30 | trigger_event(6021); trigger_event(6022); trigger_event(6023); stop |
| 5 | 6021 | 60 / 4 | 1 | 30 | trigger_event(6024); stop |
| 5 | 6022 | 60 / 5 | 1 | 30 | trigger_event(6025); stop |
| 5 | 6023 | 60 / 6 | 1 | 30 | trigger_event(6026); stop |
| 5 | 6024 | 60 / 7 | 3 | 30 | trigger_event(6027); stop |
| 5 | 6025 | 60 / 8 | 2 | 30 | set_switch(62); stop |
| 5 | 6026 | 60 / 9 | 5 | 30 | set_switch(63); stop |
| 5 | 6027 | 60 / 10 | 8 | 30 | set_switch(64); stop |
| 5 | 611 | 60 / 16 | 6 | 30 | trigger_event(6101); stop |
| 5 | 6101 | 60 / 17 | 8 | 30 | trigger_event(6102); stop |
| 5 | 6102 | 60 / 18 | 8 | 30 | set_switch(65); stop |
| 5 | 612 | 60 / 13 | 6 | 30 | trigger_event(6201); stop |
| 5 | 6201 | 60 / 14 | 6 | 30 | trigger_event(6202); stop |
| 5 | 6202 | 60 / 15 | 5 | 30 | set_switch(65); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
