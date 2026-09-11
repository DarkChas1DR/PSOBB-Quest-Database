# 9-7:Sacred Ground — government-ep4/q707-bb-e

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/government-ep4/q707-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep4/q707-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep4/q707-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode4; header quest ID 707; language E. Static scan: **180 objects, 246 enemy/NPC records, 52 events, 194 script labels.** Script roundtrip: byte-identical.

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
| 0 | 27 | 20 | 0 |
| 8 | 153 | 226 | 52 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 8 | 201 | 20 / 1 | 4 | 10 | trigger_event(2011); stop |
| 8 | 2011 | 20 / 2 | 6 | 10 | trigger_event(2012); stop |
| 8 | 2012 | 20 / 3 | 6 | 10 | set_switch(20); stop |
| 8 | 211 | 21 / 1 | 7 | 90 | trigger_event(2111); stop |
| 8 | 2111 | 21 / 2 | 8 | 10 | trigger_event(2112); stop |
| 8 | 2112 | 21 / 3 | 6 | 10 | trigger_event(2113); stop |
| 8 | 2113 | 21 / 4 | 10 | 60 | set_switch(21); stop |
| 8 | 401 | 40 / 1 | 5 | 10 | trigger_event(4011); stop |
| 8 | 4011 | 40 / 2 | 8 | 10 | set_switch(40); stop |
| 8 | 411 | 41 / 1 | 0 | 10 | trigger_event(4111); stop |
| 8 | 4111 | 41 / 2 | 0 | 10 | set_switch(41); stop |
| 8 | 501 | 50 / 1 | 7 | 120 | trigger_event(5011); stop |
| 8 | 5011 | 50 / 2 | 7 | 10 | trigger_event(5012); stop |
| 8 | 5012 | 50 / 3 | 8 | 60 | trigger_event(5013); stop |
| 8 | 5013 | 50 / 4 | 5 | 10 | set_switch(50); stop |
| 8 | 511 | 51 / 1 | 4 | 120 | trigger_event(5111); stop |
| 8 | 5111 | 51 / 2 | 7 | 10 | set_switch(51); stop |
| 8 | 601 | 60 / 1 | 10 | 150 | trigger_event(6011); stop |
| 8 | 6011 | 60 / 2 | 4 | 10 | set_switch(60); stop |
| 8 | 611 | 61 / 1 | 3 | 30 | trigger_event(6111); stop |
| 8 | 6111 | 61 / 2 | 2 | 10 | trigger_event(6112); stop |
| 8 | 6112 | 61 / 3 | 1 | 10 | set_switch(61); stop |
| 8 | 701 | 70 / 1 | 3 | 10 | trigger_event(7011); stop |
| 8 | 7011 | 70 / 2 | 9 | 10 | trigger_event(7012); stop |
| 8 | 7012 | 70 / 3 | 6 | 10 | set_switch(70); stop |
| 8 | 801 | 80 / 1 | 5 | 10 | construct_objects(room=10,group_or_wave=1); stop |
| 8 | 802 | 80 / 2 | 8 | 10 | trigger_event(8021); stop |
| 8 | 8021 | 80 / 3 | 1 | 60 | set_switch(80); stop |
| 8 | 1001 | 100 / 1 | 4 | 10 | trigger_event(10011); stop |
| 8 | 10011 | 100 / 2 | 5 | 10 | trigger_event(10012); stop |
| 8 | 10012 | 100 / 3 | 7 | 10 | set_switch(100); stop |
| 8 | 1002 | 100 / 4 | 4 | 240 | stop |
| 8 | 1101 | 110 / 1 | 1 | 10 | trigger_event(11011); stop |
| 8 | 11011 | 110 / 2 | 3 | 10 | trigger_event(11012); stop |
| 8 | 11012 | 110 / 3 | 1 | 10 | trigger_event(11013); stop |
| 8 | 11013 | 110 / 4 | 4 | 60 | trigger_event(11014); stop |
| 8 | 11014 | 110 / 5 | 3 | 90 | trigger_event(11015); stop |
| 8 | 11015 | 110 / 6 | 4 | 120 | set_switch(110); stop |
| 8 | 1102 | 110 / 7 | 1 | 10 | trigger_event(11021); stop |
| 8 | 11021 | 110 / 8 | 3 | 10 | trigger_event(11022); stop |
| 8 | 11022 | 110 / 9 | 3 | 10 | trigger_event(11023); stop |
| 8 | 11023 | 110 / 10 | 2 | 10 | trigger_event(11024); stop |
| 8 | 11024 | 110 / 11 | 1 | 10 | trigger_event(11025); stop |
| 8 | 11025 | 110 / 12 | 1 | 10 | set_switch(111); stop |
| 8 | 1103 | 110 / 13 | 1 | 10 | trigger_event(11031); stop |
| 8 | 11031 | 110 / 14 | 3 | 10 | trigger_event(11032); stop |
| 8 | 11032 | 110 / 15 | 3 | 10 | trigger_event(11033); stop |
| 8 | 11033 | 110 / 16 | 1 | 10 | trigger_event(11034); stop |
| 8 | 11034 | 110 / 17 | 3 | 10 | trigger_event(11035); stop |
| 8 | 11035 | 110 / 18 | 2 | 10 | set_switch(112); stop |
| 8 | 1811 | 181 / 1 | 4 | 60 | trigger_event(18111); stop |
| 8 | 18111 | 181 / 2 | 2 | 10 | set_switch(181); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
