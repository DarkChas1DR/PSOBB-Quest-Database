# 慟哭の森 — solo-story-ep1/q008-bb-j

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/solo-story-ep1/q008-bb-j.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/solo-story-ep1/q008-bb-j.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/solo-story-ep1/q008-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 8; language J. Static scan: **227 objects, 120 enemy/NPC records, 49 events, 48 script labels.** Script roundtrip: byte-identical.

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
0x02, 0x02, 0x00, 0x00, 0x02
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 17 | 0 |
| 1 | 111 | 59 | 22 |
| 2 | 90 | 44 | 27 |

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
| 2 | 31 | 3 / 1 | 3 | 1 | trigger_event(311); stop |
| 2 | 311 | 3 / 2 | 1 | 30 | set_switch(5); stop |
| 2 | 51 | 5 / 1 | 1 | 1 | stop |
| 2 | 52 | 5 / 2 | 1 | 1 | stop |
| 2 | 61 | 6 / 1 | 1 | 1 | trigger_event(611); stop |
| 2 | 611 | 6 / 2 | 3 | 30 | trigger_event(612); stop |
| 2 | 612 | 6 / 3 | 1 | 30 | set_switch(3); set_switch(9); stop |
| 2 | 101 | 10 / 1 | 2 | 1 | set_switch(11); stop |
| 2 | 111 | 11 / 1 | 1 | 1 | trigger_event(1111); stop |
| 2 | 1111 | 11 / 2 | 1 | 30 | trigger_event(1112); stop |
| 2 | 1112 | 11 / 3 | 4 | 30 | trigger_event(1113); stop |
| 2 | 1113 | 11 / 4 | 2 | 30 | set_switch(4); set_switch(5); set_switch(6); set_switch(7); set_switch(11); stop |
| 2 | 112 | 11 / 5 | 1 | 10 | trigger_event(1121); stop |
| 2 | 1121 | 11 / 6 | 2 | 20 | stop |
| 2 | 131 | 13 / 1 | 3 | 30 | trigger_event(1311); stop |
| 2 | 1311 | 13 / 2 | 3 | 60 | stop |
| 2 | 131 | 13 / 1 | 3 | 30 | trigger_event(1311); stop |
| 2 | 1311 | 13 / 2 | 3 | 60 | stop |
| 2 | 132 | 13 / 3 | 2 | 30 | trigger_event(1321); stop |
| 2 | 1321 | 13 / 4 | 3 | 30 | trigger_event(1322); stop |
| 2 | 1322 | 13 / 5 | 1 | 30 | set_switch(8); stop |
| 2 | 151 | 15 / 1 | 2 | 1 | trigger_event(1511); stop |
| 2 | 1511 | 15 / 2 | 1 | 60 | stop |
| 2 | 152 | 15 / 3 | 1 | 30 | trigger_event(1521); stop |
| 2 | 1521 | 15 / 4 | 1 | 60 | trigger_event(1522); stop |
| 2 | 1522 | 15 / 5 | 2 | 15 | stop |
| 2 | 161 | 16 / 1 | 1 | 1 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
