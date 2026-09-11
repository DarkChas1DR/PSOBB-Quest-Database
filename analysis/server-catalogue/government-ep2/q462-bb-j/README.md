# ７－２：手がかりを求めて — government-ep2/q462-bb-j

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/government-ep2/q462-bb-j.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep2/q462-bb-j.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep2/q462-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 462; language J. Static scan: **428 objects, 161 enemy/NPC records, 58 events, 99 script labels.** Script roundtrip: byte-identical.

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
0x07, 0x19, 0x00, 0x00, 0x01
0x08, 0x1A, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 53 | 19 | 0 |
| 7 | 121 | 49 | 25 |
| 8 | 254 | 93 | 33 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 7 | 11 | 1 / 1 | 3 | 20 | stop |
| 7 | 12 | 1 / 2 | 3 | 30 | set_switch(1); stop |
| 7 | 31 | 3 / 1 | 2 | 1 | trigger_event(311); stop |
| 7 | 311 | 3 / 2 | 3 | 100 | stop |
| 7 | 32 | 3 / 3 | 4 | 1 | stop |
| 7 | 51 | 5 / 13 | 4 | 1 | construct_objects(room=5,group_or_wave=1); trigger_event(5101); trigger_event(5102); trigger_event(5103); trigger_event(5104); trigger_event(5105); stop |
| 7 | 5101 | 5 / 14 | 1 | 300 | set_switch(4); set_switch(5); set_switch(102); stop |
| 7 | 5102 | 5 / 1 | 1 | 30 | trigger_event(51021); stop |
| 7 | 51021 | 5 / 2 | 1 | 100 | trigger_event(51022); stop |
| 7 | 51022 | 5 / 3 | 1 | 60 | stop |
| 7 | 5103 | 5 / 4 | 1 | 1 | trigger_event(51031); stop |
| 7 | 51031 | 5 / 5 | 1 | 30 | trigger_event(51032); stop |
| 7 | 51032 | 5 / 6 | 1 | 100 | stop |
| 7 | 5104 | 5 / 7 | 1 | 100 | trigger_event(51041); stop |
| 7 | 51041 | 5 / 8 | 1 | 60 | trigger_event(51042); stop |
| 7 | 51042 | 5 / 9 | 1 | 30 | stop |
| 7 | 5105 | 5 / 10 | 1 | 30 | trigger_event(51051); stop |
| 7 | 51051 | 5 / 11 | 1 | 1 | trigger_event(51052); stop |
| 7 | 51052 | 5 / 12 | 1 | 10 | stop |
| 7 | 61 | 6 / 1 | 2 | 1 | trigger_event(611); stop |
| 7 | 611 | 6 / 2 | 2 | 100 | set_switch(6); stop |
| 7 | 62 | 6 / 3 | 2 | 1 | stop |
| 7 | 63 | 6 / 4 | 2 | 1 | stop |
| 7 | 71 | 7 / 1 | 4 | 60 | set_switch(7); stop |
| 7 | 81 | 8 / 1 | 5 | 1 | stop |
| 8 | 25 | 2 / 1 | 1 | 240 | set_switch(1); set_switch(18); set_switch(102); stop |
| 8 | 28 | 2 / 7 | 6 | 1 | trigger_event(281); stop |
| 8 | 281 | 2 / 8 | 3 | 30 | stop |
| 8 | 24 | 2 / 2 | 4 | 1 | trigger_event(241); stop |
| 8 | 241 | 2 / 3 | 3 | 90 | trigger_event(242); construct_objects(room=2,group_or_wave=2); stop |
| 8 | 242 | 2 / 4 | 4 | 90 | trigger_event(243); stop |
| 8 | 243 | 2 / 5 | 4 | 90 | trigger_event(244); construct_objects(room=2,group_or_wave=1); stop |
| 8 | 244 | 2 / 6 | 4 | 90 | set_switch(103); set_switch(104); set_switch(105); stop |
| 8 | 31 | 3 / 1 | 2 | 1 | trigger_event(311); stop |
| 8 | 311 | 3 / 2 | 3 | 1 | trigger_event(312); stop |
| 8 | 312 | 3 / 3 | 4 | 1 | trigger_event(313); trigger_event(3110); stop |
| 8 | 313 | 3 / 4 | 3 | 90 | trigger_event(314); trigger_event(3111); stop |
| 8 | 314 | 3 / 5 | 3 | 60 | trigger_event(315); stop |
| 8 | 315 | 3 / 6 | 3 | 100 | set_switch(4); stop |
| 8 | 3110 | 3 / 7 | 3 | 100 | stop |
| 8 | 3111 | 3 / 8 | 3 | 1 | trigger_event(31111); stop |
| 8 | 31111 | 3 / 9 | 3 | 30 | stop |
| 8 | 32 | 3 / 10 | 3 | 100 | stop |
| 8 | 33 | 3 / 11 | 2 | 90 | stop |
| 8 | 34 | 3 / 12 | 1 | 1 | stop |
| 8 | 41 | 4 / 1 | 3 | 60 | set_switch(7); set_switch(8); set_switch(9); set_switch(10); stop |
| 8 | 42 | 4 / 2 | 3 | 1 | stop |
| 8 | 51 | 5 / 1 | 3 | 1 | trigger_event(511); stop |
| 8 | 511 | 5 / 2 | 3 | 60 | set_switch(11); stop |
| 8 | 52 | 5 / 3 | 2 | 200 | stop |
| 8 | 53 | 5 / 4 | 2 | 200 | trigger_event(531); stop |
| 8 | 531 | 5 / 5 | 3 | 1 | stop |
| 8 | 82 | 8 / 5 | 2 | 150 | trigger_event(811); trigger_event(8110); stop |
| 8 | 81 | 8 / 1 | 2 | 1 | stop |
| 8 | 811 | 8 / 2 | 2 | 60 | trigger_event(812); stop |
| 8 | 812 | 8 / 3 | 2 | 90 | set_switch(13); set_switch(14); set_switch(12); stop |
| 8 | 8110 | 8 / 4 | 1 | 300 | stop |
| 8 | 83 | 8 / 6 | 3 | 60 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
