# 大地の呼び声 — solo-story-ep1/q007-bb-j

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/solo-story-ep1/q007-bb-j.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/solo-story-ep1/q007-bb-j.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/solo-story-ep1/q007-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 7; language J. Static scan: **243 objects, 102 enemy/NPC records, 32 events, 52 script labels.** Script roundtrip: byte-identical.

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
| 0 | 26 | 19 | 0 |
| 1 | 112 | 41 | 14 |
| 2 | 105 | 42 | 18 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 111 | 11 / 1 | 3 | 50 | trigger_event(1111); stop |
| 1 | 1111 | 11 / 2 | 4 | 50 | trigger_event(1112); stop |
| 1 | 1112 | 11 / 3 | 3 | 50 | set_switch(5); set_switch(10); stop |
| 1 | 51 | 2 / 1 | 3 | 60 | set_switch(1); trigger_event(211); stop |
| 1 | 211 | 2 / 2 | 3 | 60 | trigger_event(212); stop |
| 1 | 212 | 2 / 3 | 2 | 60 | set_switch(2); stop |
| 1 | 41 | 4 / 1 | 2 | 60 | trigger_event(411); stop |
| 1 | 411 | 4 / 2 | 3 | 60 | trigger_event(412); stop |
| 1 | 412 | 4 / 3 | 4 | 60 | trigger_event(413); stop |
| 1 | 413 | 4 / 4 | 5 | 60 | set_switch(9); stop |
| 1 | 81 | 8 / 1 | 3 | 60 | stop |
| 1 | 161 | 16 / 1 | 1 | 60 | trigger_event(1611); stop |
| 1 | 1611 | 16 / 2 | 1 | 60 | trigger_event(1612); stop |
| 1 | 1612 | 16 / 3 | 1 | 60 | stop |
| 2 | 21 | 2 / 1 | 2 | 1 | trigger_event(211); stop |
| 2 | 211 | 2 / 2 | 1 | 30 | stop |
| 2 | 22 | 2 / 3 | 1 | 30 | trigger_event(221); stop |
| 2 | 221 | 2 / 4 | 2 | 30 | set_switch(3); set_switch(4); set_switch(5); set_switch(6); stop |
| 2 | 31 | 3 / 1 | 1 | 1 | stop |
| 2 | 61 | 6 / 1 | 4 | 55 | trigger_event(611); stop |
| 2 | 611 | 6 / 2 | 4 | 20 | trigger_event(612); stop |
| 2 | 612 | 6 / 3 | 6 | 10 | set_switch(9); stop |
| 2 | 101 | 10 / 1 | 1 | 1 | stop |
| 2 | 111 | 11 / 1 | 3 | 1 | trigger_event(1111); stop |
| 2 | 1111 | 11 / 2 | 3 | 40 | trigger_event(1112); stop |
| 2 | 1112 | 11 / 3 | 3 | 25 | set_switch(7); set_switch(8); set_switch(11); stop |
| 2 | 131 | 13 / 1 | 3 | 1 | trigger_event(1311); stop |
| 2 | 1311 | 13 / 2 | 2 | 30 | trigger_event(1312); stop |
| 2 | 1312 | 13 / 3 | 2 | 20 | stop |
| 2 | 132 | 13 / 4 | 1 | 30 | trigger_event(1321); stop |
| 2 | 1321 | 13 / 5 | 2 | 20 | stop |
| 2 | 151 | 15 / 1 | 1 | 1 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
