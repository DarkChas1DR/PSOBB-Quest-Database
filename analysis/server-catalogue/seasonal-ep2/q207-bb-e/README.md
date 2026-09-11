# Pioneer Halloween — seasonal-ep2/q207-bb-e

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/seasonal-ep2/q207-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/seasonal-ep2/q207-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/seasonal-ep2/q207-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 207; language E. Static scan: **853 objects, 247 enemy/NPC records, 91 events, 335 script labels.** Script roundtrip: byte-identical.

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
0x06, 0x18, 0x00, 0x00, 0x00
0x07, 0x19, 0x00, 0x00, 0x00
0x08, 0x1A, 0x00, 0x00, 0x00
0x09, 0x1B, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 45 | 16 | 0 |
| 6 | 165 | 46 | 18 |
| 7 | 177 | 59 | 26 |
| 8 | 255 | 47 | 23 |
| 9 | 211 | 79 | 24 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 6 | 21 | 2 / 1 | 1 | 1 | stop |
| 6 | 31 | 3 / 1 | 2 | 150 | trigger_event(311); stop |
| 6 | 311 | 3 / 2 | 3 | 60 | trigger_event(312); stop |
| 6 | 312 | 3 / 3 | 2 | 10 | trigger_event(313); stop |
| 6 | 313 | 3 / 4 | 4 | 10 | set_switch(13); set_switch(16); stop |
| 6 | 32 | 3 / 5 | 1 | 220 | trigger_event(321); stop |
| 6 | 321 | 3 / 6 | 2 | 10 | trigger_event(322); stop |
| 6 | 322 | 3 / 7 | 3 | 100 | stop |
| 6 | 41 | 4 / 1 | 4 | 10 | trigger_event(411); stop |
| 6 | 411 | 4 / 2 | 3 | 100 | set_switch(14); set_switch(15); stop |
| 6 | 42 | 4 / 3 | 2 | 1 | stop |
| 6 | 43 | 4 / 4 | 1 | 1 | stop |
| 6 | 61 | 6 / 1 | 5 | 1 | set_switch(12); stop |
| 6 | 151 | 15 / 1 | 3 | 10 | trigger_event(151011); trigger_event(151021); stop |
| 6 | 151011 | 15 / 2 | 3 | 60 | trigger_event(151012); stop |
| 6 | 151012 | 15 / 3 | 3 | 10 | set_switch(3); set_switch(4); set_switch(5); set_switch(7); set_switch(11); stop |
| 6 | 151021 | 15 / 4 | 3 | 200 | stop |
| 6 | 81 | 8 / 1 | 1 | 1 | stop |
| 7 | 11 | 1 / 1 | 1 | 1 | stop |
| 7 | 21 | 2 / 1 | 5 | 1 | trigger_event(21011); trigger_event(21021); stop |
| 7 | 21011 | 2 / 2 | 3 | 60 | trigger_event(21012); stop |
| 7 | 21012 | 2 / 3 | 3 | 10 | set_switch(3); set_switch(4); set_switch(5); stop |
| 7 | 21021 | 2 / 4 | 2 | 150 | trigger_event(221); stop |
| 7 | 23 | 2 / 5 | 1 | 1 | stop |
| 7 | 31 | 3 / 1 | 2 | 1 | stop |
| 7 | 32 | 3 / 2 | 2 | 1 | stop |
| 7 | 41 | 4 / 1 | 1 | 1 | stop |
| 7 | 51 | 5 / 13 | 1 | 10 | set_switch(6); set_switch(7); set_switch(102); stop |
| 7 | 52 | 5 / 1 | 1 | 10 | trigger_event(521); stop |
| 7 | 521 | 5 / 2 | 1 | 10 | trigger_event(522); stop |
| 7 | 522 | 5 / 3 | 1 | 60 | stop |
| 7 | 53 | 5 / 4 | 1 | 10 | trigger_event(531); stop |
| 7 | 531 | 5 / 5 | 1 | 60 | trigger_event(532); stop |
| 7 | 532 | 5 / 6 | 1 | 60 | stop |
| 7 | 54 | 5 / 7 | 1 | 10 | trigger_event(541); stop |
| 7 | 541 | 5 / 8 | 1 | 10 | trigger_event(542); stop |
| 7 | 542 | 5 / 9 | 1 | 100 | stop |
| 7 | 55 | 5 / 10 | 1 | 10 | trigger_event(551); stop |
| 7 | 551 | 5 / 11 | 1 | 100 | trigger_event(552); stop |
| 7 | 552 | 5 / 12 | 1 | 10 | stop |
| 7 | 61 | 6 / 1 | 3 | 1 | stop |
| 7 | 71 | 7 / 1 | 2 | 1 | set_switch(1); set_switch(2); stop |
| 7 | 72 | 7 / 2 | 17 | 1 | stop |
| 7 | 81 | 8 / 1 | 4 | 1 | stop |
| 8 | 21 | 2 / 1 | 1 | 10 | stop |
| 8 | 31 | 3 / 1 | 2 | 10 | trigger_event(311); stop |
| 8 | 311 | 3 / 2 | 2 | 100 | trigger_event(312); stop |
| 8 | 312 | 3 / 3 | 2 | 100 | trigger_event(313); stop |
| 8 | 313 | 3 / 4 | 3 | 100 | stop |
| 8 | 32 | 3 / 5 | 2 | 300 | stop |
| 8 | 33 | 3 / 6 | 1 | 10 | stop |
| 8 | 34 | 3 / 7 | 2 | 60 | stop |
| 8 | 41 | 4 / 1 | 3 | 10 | set_switch(7); set_switch(8); set_switch(9); set_switch(10); stop |
| 8 | 42 | 4 / 2 | 1 | 1 | stop |
| 8 | 43 | 4 / 3 | 1 | 1 | stop |
| 8 | 51 | 5 / 1 | 3 | 100 | trigger_event(511); stop |
| 8 | 511 | 5 / 2 | 3 | 60 | trigger_event(512); stop |
| 8 | 512 | 5 / 3 | 3 | 100 | set_switch(11); stop |
| 8 | 52 | 5 / 4 | 2 | 200 | trigger_event(521); stop |
| 8 | 521 | 5 / 5 | 2 | 200 | stop |
| 8 | 81 | 8 / 1 | 2 | 200 | trigger_event(811); stop |
| 8 | 811 | 8 / 2 | 3 | 100 | trigger_event(81011); trigger_event(81021); stop |
| 8 | 81011 | 8 / 3 | 2 | 10 | trigger_event(81012); stop |
| 8 | 81012 | 8 / 4 | 2 | 150 | set_switch(13); set_switch(14); set_switch(12); stop |
| 8 | 81021 | 8 / 5 | 2 | 150 | stop |
| 8 | 82 | 8 / 6 | 2 | 60 | stop |
| 8 | 91 | 9 / 1 | 1 | 1 | stop |
| 9 | 11 | 1 / 1 | 17 | 1 | stop |
| 9 | 21 | 2 / 1 | 1 | 1 | stop |
| 9 | 31 | 3 / 1 | 3 | 10 | construct_objects(room=3,group_or_wave=1); set_switch(32); stop |
| 9 | 32 | 3 / 2 | 2 | 10 | construct_objects(room=3,group_or_wave=2); set_switch(33); stop |
| 9 | 33 | 3 / 3 | 3 | 10 | construct_objects(room=3,group_or_wave=3); set_switch(34); stop |
| 9 | 34 | 3 / 4 | 3 | 10 | construct_objects(room=3,group_or_wave=4); set_switch(35); stop |
| 9 | 35 | 3 / 5 | 2 | 10 | construct_objects(room=3,group_or_wave=5); set_switch(36); stop |
| 9 | 36 | 3 / 6 | 3 | 10 | construct_objects(room=3,group_or_wave=6); set_switch(37); stop |
| 9 | 37 | 3 / 7 | 4 | 10 | construct_objects(room=3,group_or_wave=7); set_switch(38); stop |
| 9 | 38 | 3 / 8 | 3 | 10 | construct_objects(room=3,group_or_wave=8); set_switch(39); stop |
| 9 | 39 | 3 / 9 | 1 | 10 | set_switch(2); set_switch(3); set_switch(12); stop |
| 9 | 71 | 7 / 1 | 4 | 10 | stop |
| 9 | 72 | 7 / 2 | 5 | 1 | set_switch(4); set_switch(5); stop |
| 9 | 91 | 9 / 1 | 5 | 1 | trigger_event(91011); trigger_event(91021); stop |
| 9 | 91011 | 9 / 2 | 2 | 100 | trigger_event(91012); stop |
| 9 | 91012 | 9 / 3 | 3 | 10 | set_switch(6); set_switch(8); stop |
| 9 | 91021 | 9 / 4 | 3 | 300 | stop |
| 9 | 101 | 10 / 1 | 1 | 1 | stop |
| 9 | 111 | 11 / 4 | 1 | 10 | set_switch(7); set_switch(9); set_switch(10); set_switch(11); set_switch(100); stop |
| 9 | 112 | 11 / 1 | 4 | 10 | trigger_event(1121); stop |
| 9 | 1121 | 11 / 2 | 3 | 100 | trigger_event(1122); stop |
| 9 | 1122 | 11 / 3 | 3 | 100 | trigger_event(1123); stop |
| 9 | 1123 | 11 / 4 | 1 | 100 | stop |
| 9 | 131 | 13 / 1 | 3 | 1 | stop |

## Review notes

- Floor 7: event 21021 targets absent event 221

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
