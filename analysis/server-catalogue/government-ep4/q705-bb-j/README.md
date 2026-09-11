# ９－５：選ばれし者（前編） — government-ep4/q705-bb-j

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/government-ep4/q705-bb-j.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep4/q705-bb-j.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep4/q705-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode4; header quest ID 705; language J. Static scan: **364 objects, 290 enemy/NPC records, 54 events, 229 script labels.** Script roundtrip: byte-identical.

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
0x05, 0x28, 0x00, 0x00, 0x00
0x06, 0x29, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 27 | 20 | 0 |
| 5 | 124 | 51 | 10 |
| 6 | 213 | 219 | 44 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 5 | 501 | 50 / 1 | 5 | 10 | trigger_event(5011); stop |
| 5 | 5011 | 50 / 2 | 6 | 10 | trigger_event(5012); stop |
| 5 | 5012 | 50 / 3 | 6 | 90 | set_switch(50); stop |
| 5 | 502 | 50 / 4 | 4 | 10 | trigger_event(5021); stop |
| 5 | 5021 | 50 / 5 | 2 | 10 | stop |
| 5 | 601 | 60 / 1 | 2 | 10 | set_switch(60); stop |
| 5 | 602 | 60 / 2 | 6 | 10 | trigger_event(6021); stop |
| 5 | 6021 | 60 / 3 | 5 | 10 | trigger_event(6022); stop |
| 5 | 6022 | 60 / 4 | 6 | 10 | trigger_event(6023); stop |
| 5 | 6023 | 60 / 5 | 7 | 90 | set_switch(61); stop |
| 6 | 201 | 20 / 1 | 8 | 10 | trigger_event(2011); stop |
| 6 | 2011 | 20 / 2 | 5 | 10 | set_switch(20); stop |
| 6 | 301 | 30 / 1 | 3 | 10 | trigger_event(3011); stop |
| 6 | 3011 | 30 / 2 | 4 | 10 | set_switch(30); stop |
| 6 | 311 | 31 / 1 | 8 | 90 | set_switch(31); stop |
| 6 | 501 | 50 / 1 | 4 | 10 | trigger_event(5011); stop |
| 6 | 5011 | 50 / 2 | 6 | 10 | trigger_event(5012); stop |
| 6 | 5012 | 50 / 3 | 5 | 10 | trigger_event(5013); stop |
| 6 | 5013 | 50 / 4 | 9 | 60 | trigger_event(5014); stop |
| 6 | 5014 | 50 / 5 | 0 | 90 | set_switch(50); stop |
| 6 | 601 | 60 / 1 | 1 | 90 | trigger_event(6011); stop |
| 6 | 6011 | 60 / 2 | 3 | 90 | set_switch(60); stop |
| 6 | 611 | 61 / 1 | 3 | 120 | trigger_event(6111); stop |
| 6 | 6111 | 61 / 2 | 4 | 10 | set_switch(61); stop |
| 6 | 701 | 70 / 1 | 4 | 10 | trigger_event(7011); stop |
| 6 | 7011 | 70 / 2 | 5 | 10 | set_switch(70); stop |
| 6 | 702 | 70 / 3 | 4 | 10 | trigger_event(7021); stop |
| 6 | 7021 | 70 / 4 | 9 | 10 | set_switch(71); stop |
| 6 | 831 | 83 / 1 | 4 | 90 | stop |
| 6 | 832 | 83 / 100 | 1 | 90 | stop |
| 6 | 901 | 90 / 1 | 3 | 10 | trigger_event(9011); stop |
| 6 | 9011 | 90 / 2 | 7 | 10 | trigger_event(9012); stop |
| 6 | 9012 | 90 / 3 | 8 | 60 | set_switch(90); stop |
| 6 | 1001 | 100 / 1 | 6 | 10 | trigger_event(10011); stop |
| 6 | 10011 | 100 / 2 | 6 | 10 | trigger_event(10012); stop |
| 6 | 10012 | 100 / 3 | 11 | 10 | trigger_event(10013); stop |
| 6 | 10013 | 100 / 4 | 11 | 10 | set_switch(100); stop |
| 6 | 1101 | 110 / 1 | 1 | 10 | trigger_event(11011); stop |
| 6 | 11011 | 110 / 2 | 5 | 90 | trigger_event(11012); stop |
| 6 | 11012 | 110 / 3 | 3 | 90 | trigger_event(11013); stop |
| 6 | 11013 | 110 / 4 | 3 | 90 | trigger_event(11014); stop |
| 6 | 11014 | 110 / 5 | 1 | 90 | set_switch(110); stop |
| 6 | 1102 | 110 / 6 | 3 | 10 | trigger_event(11021); stop |
| 6 | 11021 | 110 / 7 | 1 | 10 | trigger_event(11022); stop |
| 6 | 11022 | 110 / 8 | 3 | 10 | trigger_event(11023); stop |
| 6 | 11023 | 110 / 9 | 3 | 10 | trigger_event(11024); stop |
| 6 | 11024 | 110 / 10 | 3 | 10 | stop |
| 6 | 1103 | 110 / 11 | 4 | 10 | trigger_event(11031); stop |
| 6 | 11031 | 110 / 12 | 3 | 10 | trigger_event(11032); stop |
| 6 | 11032 | 110 / 13 | 3 | 10 | trigger_event(11033); stop |
| 6 | 11033 | 110 / 14 | 2 | 14 | trigger_event(11034); stop |
| 6 | 11034 | 110 / 15 | 3 | 10 | stop |
| 6 | 1601 | 160 / 1 | 6 | 30 | set_switch(160); stop |
| 6 | 1611 | 161 / 1 | 6 | 30 | set_switch(161); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
