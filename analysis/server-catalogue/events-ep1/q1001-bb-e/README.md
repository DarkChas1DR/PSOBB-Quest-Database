# Echoes in the Forest — events-ep1/q1001-bb-e

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/events-ep1/q1001-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/events-ep1/q1001-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/events-ep1/q1001-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 1001; language E. Static scan: **268 objects, 784 enemy/NPC records, 68 events, 38 script labels.** Script roundtrip: byte-identical.

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
0x00, 0x00, 0x00, 0x00, 0x00
0x01, 0x01, 0x00, 0x00, 0x01
0x02, 0x02, 0x00, 0x00, 0x01
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 21 | 0 |
| 1 | 105 | 253 | 24 |
| 2 | 137 | 510 | 44 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 111 | 11 / 1 | 12 | 50 | trigger_event(1111); stop |
| 1 | 1111 | 11 / 2 | 12 | 50 | trigger_event(1112); stop |
| 1 | 1112 | 11 / 3 | 16 | 50 | set_switch(4); set_switch(5); set_switch(6); stop |
| 1 | 101 | 10 / 1 | 6 | 60 | trigger_event(1011); stop |
| 1 | 1011 | 10 / 2 | 8 | 60 | trigger_event(1012); stop |
| 1 | 1012 | 10 / 3 | 8 | 60 | set_switch(5); set_switch(6); set_switch(7); set_switch(8); stop |
| 1 | 1013 | 10 / 4 | 20 | 60 | stop |
| 1 | 51 | 5 / 1 | 10 | 60 | trigger_event(511); stop |
| 1 | 511 | 5 / 2 | 10 | 60 | trigger_event(512); stop |
| 1 | 512 | 5 / 3 | 10 | 60 | set_switch(1); set_switch(7); set_switch(8); stop |
| 1 | 513 | 5 / 4 | 18 | 60 | stop |
| 1 | 21 | 2 / 1 | 6 | 60 | trigger_event(211); stop |
| 1 | 211 | 2 / 2 | 9 | 60 | trigger_event(212); stop |
| 1 | 212 | 2 / 3 | 7 | 60 | trigger_event(213); stop |
| 1 | 213 | 2 / 4 | 19 | 60 | set_switch(1); set_switch(2); stop |
| 1 | 71 | 7 / 1 | 12 | 60 | trigger_event(711); stop |
| 1 | 711 | 7 / 2 | 12 | 60 | trigger_event(712); stop |
| 1 | 712 | 7 / 3 | 12 | 60 | set_switch(2); set_switch(3); set_switch(4); stop |
| 1 | 41 | 4 / 1 | 10 | 60 | trigger_event(411); stop |
| 1 | 411 | 4 / 2 | 10 | 60 | set_switch(9); stop |
| 1 | 81 | 8 / 1 | 7 | 60 | stop |
| 1 | 81 | 8 / 2 | 6 | 60 | stop |
| 1 | 82 | 8 / 3 | 6 | 60 | stop |
| 1 | 83 | 8 / 4 | 0 | 60 | stop |
| 2 | 21 | 2 / 1 | 2 | 1 | trigger_event(211); stop |
| 2 | 211 | 2 / 3 | 4 | 30 | stop |
| 2 | 22 | 2 / 2 | 5 | 50 | trigger_event(221); stop |
| 2 | 221 | 2 / 4 | 4 | 30 | trigger_event(222); stop |
| 2 | 222 | 2 / 5 | 6 | 30 | set_switch(1); set_switch(3); stop |
| 2 | 31 | 3 / 1 | 12 | 120 | stop |
| 2 | 51 | 5 / 1 | 7 | 120 | stop |
| 2 | 61 | 6 / 1 | 4 | 1 | trigger_event(611); stop |
| 2 | 611 | 6 / 2 | 4 | 30 | trigger_event(612); stop |
| 2 | 612 | 6 / 3 | 5 | 30 | set_switch(9); stop |
| 2 | 101 | 10 / 1 | 12 | 1 | stop |
| 2 | 111 | 11 / 1 | 1 | 1 | trigger_event(1111); stop |
| 2 | 1111 | 11 / 2 | 3 | 120 | stop |
| 2 | 112 | 11 / 3 | 1 | 1 | trigger_event(1121); stop |
| 2 | 1121 | 11 / 4 | 3 | 30 | set_switch(4); set_switch(5); set_switch(6); set_switch(7); set_switch(11); stop |
| 2 | 113 | 11 / 5 | 3 | 180 | stop |
| 2 | 121 | 12 / 1 | 6 | 1 | trigger_event(1211); stop |
| 2 | 1211 | 12 / 2 | 8 | 1 | trigger_event(1212); stop |
| 2 | 1212 | 12 / 3 | 10 | 30 | trigger_event(1213); stop |
| 2 | 1213 | 12 / 4 | 10 | 30 | trigger_event(1214); stop |
| 2 | 1214 | 12 / 5 | 5 | 60 | trigger_event(1215); stop |
| 2 | 1215 | 12 / 6 | 8 | 45 | trigger_event(1216); stop |
| 2 | 1216 | 12 / 7 | 9 | 45 | trigger_event(1217); stop |
| 2 | 1217 | 12 / 8 | 11 | 45 | trigger_event(1218); stop |
| 2 | 1218 | 12 / 9 | 7 | 45 | trigger_event(1219); stop |
| 2 | 1219 | 12 / 10 | 10 | 45 | stop |
| 2 | 122 | 12 / 11 | 9 | 1 | trigger_event(1221); stop |
| 2 | 1221 | 12 / 12 | 8 | 1 | trigger_event(1222); stop |
| 2 | 1222 | 12 / 13 | 4 | 30 | trigger_event(1223); stop |
| 2 | 1223 | 12 / 14 | 3 | 30 | trigger_event(1224); stop |
| 2 | 1224 | 12 / 15 | 1 | 60 | trigger_event(1225); stop |
| 2 | 1225 | 12 / 16 | 3 | 45 | trigger_event(1226); stop |
| 2 | 1226 | 12 / 17 | 2 | 45 | trigger_event(1227); stop |
| 2 | 1227 | 12 / 18 | 3 | 45 | trigger_event(1228); stop |
| 2 | 1228 | 12 / 19 | 4 | 45 | trigger_event(1229); stop |
| 2 | 1229 | 12 / 20 | 2 | 45 | stop |
| 2 | 131 | 13 / 1 | 2 | 1 | trigger_event(1311); stop |
| 2 | 1311 | 13 / 2 | 10 | 15 | set_switch(8); stop |
| 2 | 151 | 15 / 1 | 7 | 1 | trigger_event(1511); stop |
| 2 | 1511 | 15 / 5 | 6 | 30 | trigger_event(1512); stop |
| 2 | 1512 | 15 / 6 | 10 | 35 | set_switch(30); stop |
| 2 | 152 | 15 / 2 | 5 | 1 | stop |
| 2 | 153 | 15 / 3 | 1 | 1 | stop |
| 2 | 154 | 15 / 4 | 7 | 1 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
