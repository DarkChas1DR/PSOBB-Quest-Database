# Towards the Future — vr-ep1/q118-bb-e

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/vr-ep1/q118-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/vr-ep1/q118-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/vr-ep1/q118-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 118; language E. Static scan: **277 objects, 216 enemy/NPC records, 69 events, 361 script labels.** Script roundtrip: byte-identical.

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
0x02, 0x02, 0x00, 0x00, 0x00
0x0B, 0x0B, 0x00, 0x00, 0x00
0x05, 0x05, 0x00, 0x04, 0x00
0x0C, 0x0C, 0x00, 0x00, 0x00
0x07, 0x07, 0x00, 0x04, 0x00
0x0D, 0x0D, 0x00, 0x00, 0x00
0x08, 0x08, 0x00, 0x04, 0x00
0x0A, 0x0A, 0x00, 0x04, 0x00
0x0E, 0x0E, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 19 | 0 |
| 2 | 29 | 33 | 8 |
| 5 | 42 | 52 | 18 |
| 7 | 37 | 62 | 28 |
| 10 | 39 | 45 | 12 |
| 11 | 23 | 1 | 1 |
| 12 | 16 | 1 | 1 |
| 13 | 30 | 2 | 0 |
| 14 | 35 | 1 | 1 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 2 | 41 | 4 / 1 | 6 | 1 | trigger_event(411); stop |
| 2 | 411 | 4 / 2 | 3 | 1 | trigger_event(412); stop |
| 2 | 412 | 4 / 3 | 4 | 1 | set_switch(90); stop |
| 2 | 42 | 4 / 4 | 1 | 300 | set_switch(90); stop |
| 2 | 121 | 12 / 1 | 6 | 100 | trigger_event(1211); stop |
| 2 | 1211 | 12 / 2 | 6 | 30 | trigger_event(1212); stop |
| 2 | 1212 | 12 / 3 | 6 | 30 | set_switch(10); stop |
| 2 | 122 | 12 / 4 | 1 | 1 | set_switch(10); stop |
| 5 | 501 | 50 / 5 | 1 | 200 | trigger_event(5011); stop |
| 5 | 5011 | 50 / 1 | 6 | 100 | trigger_event(5012); stop |
| 5 | 5012 | 50 / 2 | 4 | 100 | trigger_event(5013); stop |
| 5 | 5013 | 50 / 3 | 3 | 100 | set_switch(1); set_switch(2); set_switch(3); stop |
| 5 | 502 | 50 / 4 | 1 | 1 | set_switch(1); set_switch(2); set_switch(3); stop |
| 5 | 511 | 51 / 1 | 4 | 10 | trigger_event(5111); stop |
| 5 | 5111 | 51 / 2 | 6 | 500 | trigger_event(5112); stop |
| 5 | 5112 | 51 / 3 | 3 | 200 | set_switch(8); set_switch(9); set_switch(90); stop |
| 5 | 512 | 51 / 4 | 1 | 1000 | set_switch(8); set_switch(9); set_switch(90); stop |
| 5 | 601 | 60 / 1 | 5 | 30 | trigger_event(6011); stop |
| 5 | 6011 | 60 / 2 | 5 | 100 | trigger_event(6012); stop |
| 5 | 6012 | 60 / 3 | 2 | 100 | set_switch(4); set_switch(5); stop |
| 5 | 602 | 60 / 4 | 1 | 1 | set_switch(4); set_switch(5); stop |
| 5 | 611 | 61 / 1 | 2 | 1 | trigger_event(6111); stop |
| 5 | 6111 | 61 / 2 | 3 | 10 | trigger_event(6112); stop |
| 5 | 6112 | 61 / 3 | 3 | 10 | set_switch(6); set_switch(7); stop |
| 5 | 612 | 61 / 4 | 1 | 1 | trigger_event(6121); set_switch(6); set_switch(7); stop |
| 5 | 6121 | 61 / 5 | 1 | 1000 | set_switch(8); set_switch(9); set_switch(90); stop |
| 7 | 201 | 20 / 1 | 4 | 400 | trigger_event(2011); stop |
| 7 | 2011 | 20 / 2 | 4 | 10 | trigger_event(2012); stop |
| 7 | 2012 | 20 / 3 | 4 | 10 | set_switch(2); set_switch(3); stop |
| 7 | 202 | 20 / 4 | 1 | 1 | set_switch(2); set_switch(3); stop |
| 7 | 501 | 50 / 1 | 1 | 1 | trigger_event(5011); stop |
| 7 | 5011 | 50 / 2 | 1 | 1 | trigger_event(5012); stop |
| 7 | 5012 | 50 / 3 | 1 | 1 | stop |
| 7 | 502 | 50 / 4 | 1 | 1 | trigger_event(5021); stop |
| 7 | 5021 | 50 / 5 | 1 | 1 | trigger_event(5022); stop |
| 7 | 5022 | 50 / 6 | 1 | 1 | stop |
| 7 | 503 | 50 / 7 | 1 | 1 | trigger_event(5031); stop |
| 7 | 5031 | 50 / 8 | 1 | 1 | trigger_event(5032); stop |
| 7 | 5032 | 50 / 9 | 1 | 1 | stop |
| 7 | 504 | 50 / 10 | 1 | 1 | trigger_event(5041); stop |
| 7 | 5041 | 50 / 11 | 1 | 1 | trigger_event(5042); stop |
| 7 | 5042 | 50 / 12 | 1 | 1 | stop |
| 7 | 505 | 50 / 13 | 1 | 1 | trigger_event(5051); stop |
| 7 | 5051 | 50 / 14 | 1 | 1 | trigger_event(5052); stop |
| 7 | 5052 | 50 / 15 | 1 | 1 | set_switch(4); set_switch(5); stop |
| 7 | 506 | 50 / 16 | 1 | 1 | set_switch(4); set_switch(5); stop |
| 7 | 511 | 51 / 1 | 6 | 1 | trigger_event(5111); stop |
| 7 | 5111 | 51 / 2 | 6 | 1 | trigger_event(5112); stop |
| 7 | 5112 | 51 / 3 | 6 | 1 | set_switch(6); set_switch(7); set_switch(8); set_switch(9); set_switch(10); stop |
| 7 | 512 | 51 / 4 | 1 | 1 | set_switch(6); set_switch(7); set_switch(8); set_switch(9); set_switch(10); stop |
| 7 | 601 | 60 / 1 | 3 | 100 | trigger_event(6011); stop |
| 7 | 6011 | 60 / 2 | 8 | 60 | trigger_event(6012); stop |
| 7 | 6012 | 60 / 3 | 1 | 1 | set_switch(1); set_switch(90); stop |
| 7 | 602 | 60 / 4 | 2 | 30 | set_switch(1); set_switch(90); stop |
| 10 | 221 | 22 / 1 | 6 | 1 | trigger_event(2211); stop |
| 10 | 2211 | 22 / 2 | 4 | 100 | trigger_event(2212); stop |
| 10 | 2212 | 22 / 3 | 2 | 100 | set_switch(16); set_switch(17); set_switch(18); set_switch(19); stop |
| 10 | 222 | 22 / 4 | 1 | 60 | set_switch(16); set_switch(17); set_switch(18); set_switch(19); stop |
| 10 | 401 | 40 / 1 | 2 | 30 | trigger_event(4011); stop |
| 10 | 4011 | 40 / 2 | 5 | 100 | trigger_event(4012); stop |
| 10 | 4012 | 40 / 3 | 3 | 100 | set_switch(24); set_switch(25); set_switch(90); stop |
| 10 | 402 | 40 / 4 | 1 | 30 | set_switch(24); set_switch(25); set_switch(90); stop |
| 10 | 701 | 70 / 1 | 4 | 30 | trigger_event(7011); stop |
| 10 | 7011 | 70 / 2 | 8 | 60 | trigger_event(7012); stop |
| 10 | 7012 | 70 / 3 | 8 | 60 | set_switch(22); set_switch(23); stop |
| 10 | 702 | 70 / 4 | 1 | 100 | set_switch(22); set_switch(23); stop |
| 11 | 1 | 1 / 1 | 1 | 50 | construct_objects(room=1,group_or_wave=1); stop |
| 12 | 1 | 1 / 1 | 1 | 50 | construct_objects(room=1,group_or_wave=1); stop |
| 14 | 1 | 0 / 1 | 1 | 50 | construct_objects(room=0,group_or_wave=1); construct_objects(room=1,group_or_wave=1); construct_objects(room=2,group_or_wave=1); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
