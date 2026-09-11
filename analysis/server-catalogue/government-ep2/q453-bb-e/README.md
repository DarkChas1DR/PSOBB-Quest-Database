# 5-3:Test/VR Temple 3 — government-ep2/q453-bb-e

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/government-ep2/q453-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep2/q453-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep2/q453-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 453; language E. Static scan: **238 objects, 137 enemy/NPC records, 32 events, 139 script labels.** Script roundtrip: byte-identical.

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
0x01, 0x13, 0x00, 0x02, 0x00
0x02, 0x14, 0x00, 0x02, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 53 | 18 | 0 |
| 1 | 74 | 46 | 14 |
| 2 | 111 | 73 | 18 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 401 | 40 / 1 | 4 | 0 | trigger_event(4011); stop |
| 1 | 4011 | 40 / 2 | 4 | 10 | trigger_event(4012); stop |
| 1 | 4012 | 40 / 3 | 4 | 30 | trigger_event(4013); stop |
| 1 | 4013 | 40 / 4 | 2 | 90 | set_switch(7); stop |
| 1 | 402 | 40 / 5 | 1 | 0 | trigger_event(4021); stop |
| 1 | 4021 | 40 / 6 | 1 | 0 | set_switch(8); stop |
| 1 | 411 | 41 / 1 | 4 | 0 | trigger_event(4111); stop |
| 1 | 4111 | 41 / 2 | 4 | 10 | trigger_event(4112); stop |
| 1 | 4112 | 41 / 3 | 6 | 30 | set_switch(11); set_switch(12); stop |
| 1 | 601 | 60 / 1 | 3 | 0 | set_switch(13); set_switch(14); stop |
| 1 | 602 | 60 / 2 | 2 | 0 | trigger_event(6021); stop |
| 1 | 6021 | 60 / 3 | 4 | 30 | trigger_event(6022); stop |
| 1 | 6022 | 60 / 4 | 3 | 60 | set_switch(18); stop |
| 1 | 901 | 90 / 1 | 4 | 30 | set_switch(23); set_switch(24); stop |
| 2 | 201 | 20 / 1 | 6 | 30 | trigger_event(2011); stop |
| 2 | 2011 | 20 / 2 | 5 | 30 | set_switch(3); set_switch(4); stop |
| 2 | 301 | 30 / 1 | 5 | 30 | set_switch(1); set_switch(2); set_switch(7); set_switch(8); set_switch(9); set_switch(10); stop |
| 2 | 501 | 50 / 1 | 7 | 60 | trigger_event(5011); stop |
| 2 | 5011 | 50 / 2 | 6 | 10 | trigger_event(5012); stop |
| 2 | 5012 | 50 / 3 | 5 | 60 | set_switch(11); set_switch(12); stop |
| 2 | 701 | 70 / 1 | 4 | 0 | trigger_event(7011); stop |
| 2 | 7011 | 70 / 2 | 4 | 10 | trigger_event(7012); stop |
| 2 | 7012 | 70 / 3 | 6 | 30 | trigger_event(7013); stop |
| 2 | 7013 | 70 / 4 | 3 | 30 | trigger_event(7014); stop |
| 2 | 7014 | 70 / 5 | 5 | 90 | stop |
| 2 | 702 | 70 / 6 | 2 | 0 | trigger_event(7021); stop |
| 2 | 7021 | 70 / 7 | 2 | 0 | trigger_event(7022); stop |
| 2 | 7022 | 70 / 8 | 3 | 0 | stop |
| 2 | 901 | 90 / 1 | 1 | 0 | set_switch(13); set_switch(14); stop |
| 2 | 911 | 91 / 1 | 6 | 0 | set_switch(26); stop |
| 2 | 1501 | 150 / 1 | 1 | 0 | stop |
| 2 | 1611 | 161 / 1 | 2 | 0 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
