# 1-2:Torrential Woods — government-ep1/q402-bb-e

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/government-ep1/q402-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep1/q402-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep1/q402-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 402; language E. Static scan: **268 objects, 153 enemy/NPC records, 47 events, 80 script labels.** Script roundtrip: byte-identical.

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
0x01, 0x01, 0x00, 0x00, 0x02
0x02, 0x02, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 27 | 20 | 0 |
| 1 | 111 | 59 | 22 |
| 2 | 130 | 74 | 25 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 51 | 5 / 1 | 3 | 1 | trigger_event(511); stop |
| 1 | 511 | 5 / 2 | 3 | 1 | trigger_event(512); stop |
| 1 | 512 | 5 / 3 | 1 | 1 | set_switch(1); stop |
| 1 | 52 | 5 / 4 | 4 | 1 | stop |
| 1 | 21 | 2 / 1 | 2 | 1 | trigger_event(211); stop |
| 1 | 211 | 2 / 2 | 2 | 1 | trigger_event(212); stop |
| 1 | 212 | 2 / 3 | 2 | 1 | set_switch(2); stop |
| 1 | 22 | 2 / 4 | 2 | 1 | trigger_event(221); stop |
| 1 | 221 | 2 / 5 | 2 | 1 | trigger_event(222); stop |
| 1 | 222 | 2 / 6 | 2 | 1 | stop |
| 1 | 71 | 7 / 1 | 3 | 60 | trigger_event(711); stop |
| 1 | 711 | 7 / 2 | 3 | 60 | trigger_event(712); stop |
| 1 | 712 | 7 / 3 | 3 | 60 | set_switch(3); set_switch(4); stop |
| 1 | 72 | 7 / 4 | 1 | 1 | stop |
| 1 | 111 | 11 / 1 | 4 | 50 | trigger_event(1111); stop |
| 1 | 1111 | 11 / 2 | 4 | 50 | trigger_event(1112); stop |
| 1 | 1112 | 11 / 3 | 3 | 50 | set_switch(5); set_switch(6); set_switch(10); stop |
| 1 | 161 | 16 / 1 | 3 | 60 | stop |
| 1 | 41 | 4 / 1 | 1 | 60 | trigger_event(411); stop |
| 1 | 411 | 4 / 2 | 4 | 60 | trigger_event(412); stop |
| 1 | 412 | 4 / 3 | 4 | 60 | set_switch(9); stop |
| 1 | 83 | 8 / 1 | 3 | 1 | stop |
| 2 | 11 | 1 / 1 | 3 | 30 | stop |
| 2 | 21 | 2 / 1 | 3 | 30 | trigger_event(211); stop |
| 2 | 211 | 2 / 2 | 3 | 30 | trigger_event(212); stop |
| 2 | 212 | 2 / 3 | 4 | 30 | set_switch(4); set_switch(5); set_switch(6); stop |
| 2 | 31 | 3 / 1 | 4 | 30 | stop |
| 2 | 61 | 6 / 1 | 3 | 30 | stop |
| 2 | 111 | 11 / 1 | 3 | 10 | stop |
| 2 | 112 | 11 / 2 | 3 | 30 | trigger_event(1121); stop |
| 2 | 1121 | 11 / 3 | 5 | 30 | set_switch(11); set_switch(7); set_switch(8); stop |
| 2 | 113 | 11 / 4 | 3 | 30 | stop |
| 2 | 131 | 13 / 1 | 5 | 30 | trigger_event(1311); stop |
| 2 | 1311 | 13 / 2 | 4 | 30 | trigger_event(1312); stop |
| 2 | 1312 | 13 / 3 | 3 | 30 | set_switch(9); stop |
| 2 | 101 | 10 / 1 | 3 | 30 | stop |
| 2 | 121 | 12 / 1 | 2 | 30 | trigger_event(1211); stop |
| 2 | 1211 | 12 / 2 | 2 | 90 | trigger_event(1212); stop |
| 2 | 1212 | 12 / 3 | 2 | 90 | trigger_event(1213); stop |
| 2 | 1213 | 12 / 7 | 3 | 90 | set_switch(101); stop |
| 2 | 122 | 12 / 4 | 2 | 30 | trigger_event(1221); stop |
| 2 | 1221 | 12 / 5 | 2 | 90 | trigger_event(1222); stop |
| 2 | 1222 | 12 / 6 | 2 | 90 | trigger_event(1223); stop |
| 2 | 1223 | 12 / 8 | 3 | 90 | set_switch(102); stop |
| 2 | 123 | 12 / 9 | 3 | 30 | trigger_event(1231); stop |
| 2 | 1231 | 12 / 10 | 2 | 90 | trigger_event(1232); stop |
| 2 | 1232 | 12 / 11 | 2 | 90 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
