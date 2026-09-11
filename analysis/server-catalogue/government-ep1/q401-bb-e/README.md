# 1-1:Planet Ragol — government-ep1/q401-bb-e

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/government-ep1/q401-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep1/q401-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep1/q401-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 401; language E. Static scan: **196 objects, 119 enemy/NPC records, 34 events, 79 script labels.** Script roundtrip: byte-identical.

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
0x01, 0x01, 0x00, 0x00, 0x00
0x02, 0x02, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 27 | 20 | 0 |
| 1 | 105 | 67 | 19 |
| 2 | 64 | 32 | 15 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 111 | 11 / 1 | 4 | 50 | trigger_event(1111); stop |
| 1 | 1111 | 11 / 2 | 4 | 50 | trigger_event(1112); stop |
| 1 | 1112 | 11 / 3 | 6 | 50 | trigger_event(1113); stop |
| 1 | 1113 | 11 / 4 | 3 | 50 | set_switch(5); set_switch(6); stop |
| 1 | 101 | 10 / 1 | 1 | 60 | trigger_event(1011); stop |
| 1 | 1011 | 10 / 2 | 3 | 60 | trigger_event(1012); stop |
| 1 | 1012 | 10 / 3 | 3 | 60 | set_switch(7); set_switch(8); stop |
| 1 | 51 | 5 / 1 | 3 | 60 | trigger_event(511); stop |
| 1 | 511 | 5 / 2 | 4 | 60 | trigger_event(512); stop |
| 1 | 512 | 5 / 3 | 3 | 60 | set_switch(1); stop |
| 1 | 21 | 2 / 1 | 3 | 60 | trigger_event(211); stop |
| 1 | 211 | 2 / 2 | 3 | 60 | trigger_event(212); stop |
| 1 | 212 | 2 / 3 | 4 | 60 | set_switch(2); stop |
| 1 | 71 | 7 / 1 | 4 | 60 | trigger_event(711); stop |
| 1 | 711 | 7 / 2 | 4 | 60 | trigger_event(712); stop |
| 1 | 712 | 7 / 3 | 3 | 60 | set_switch(3); stop |
| 1 | 41 | 4 / 1 | 5 | 60 | trigger_event(411); stop |
| 1 | 411 | 4 / 2 | 4 | 60 | set_switch(9); stop |
| 1 | 82 | 8 / 1 | 3 | 60 | stop |
| 2 | 61 | 6 / 1 | 3 | 30 | trigger_event(611); stop |
| 2 | 611 | 6 / 2 | 4 | 30 | set_switch(62); stop |
| 2 | 21 | 2 / 1 | 1 | 30 | trigger_event(211); stop |
| 2 | 211 | 2 / 2 | 1 | 180 | trigger_event(212); stop |
| 2 | 212 | 2 / 3 | 1 | 180 | trigger_event(213); stop |
| 2 | 213 | 2 / 4 | 1 | 180 | set_switch(101); stop |
| 2 | 22 | 2 / 5 | 2 | 30 | trigger_event(221); stop |
| 2 | 221 | 2 / 6 | 2 | 60 | trigger_event(222); stop |
| 2 | 222 | 2 / 7 | 2 | 90 | trigger_event(223); stop |
| 2 | 223 | 2 / 8 | 2 | 90 | set_switch(102); stop |
| 2 | 23 | 2 / 9 | 2 | 30 | trigger_event(231); stop |
| 2 | 231 | 2 / 10 | 2 | 60 | trigger_event(232); stop |
| 2 | 232 | 2 / 11 | 2 | 90 | trigger_event(233); stop |
| 2 | 233 | 2 / 12 | 2 | 90 | set_switch(103); stop |
| 2 | 24 | 2 / 13 | 5 | 90 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
