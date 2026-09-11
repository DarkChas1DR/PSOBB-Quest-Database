# ３－２：襲いくる機械 — government-ep1/q409-bb-j

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/government-ep1/q409-bb-j.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep1/q409-bb-j.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep1/q409-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 409; language J. Static scan: **330 objects, 179 enemy/NPC records, 45 events, 147 script labels.** Script roundtrip: byte-identical.

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
0x07, 0x07, 0x00, 0x00, 0x00
0x08, 0x07, 0x00, 0x01, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 27 | 20 | 0 |
| 7 | 156 | 112 | 27 |
| 8 | 147 | 47 | 18 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 7 | 211 | 21 / 1 | 1 | 1 | set_switch(17); stop |
| 7 | 301 | 30 / 1 | 6 | 1 | trigger_event(3011); stop |
| 7 | 3011 | 30 / 2 | 6 | 45 | trigger_event(3012); stop |
| 7 | 3012 | 30 / 3 | 4 | 20 | set_switch(15); set_switch(16); stop |
| 7 | 401 | 40 / 1 | 2 | 1 | set_switch(1); set_switch(2); stop |
| 7 | 501 | 50 / 1 | 4 | 1 | trigger_event(5011); stop |
| 7 | 5011 | 50 / 2 | 5 | 1 | set_switch(5); stop |
| 7 | 511 | 51 / 1 | 6 | 1 | set_switch(21); stop |
| 7 | 521 | 52 / 1 | 8 | 1 | trigger_event(5211); stop |
| 7 | 5211 | 52 / 2 | 5 | 45 | set_switch(10); stop |
| 7 | 531 | 53 / 1 | 5 | 1 | trigger_event(5311); stop |
| 7 | 5311 | 53 / 2 | 4 | 60 | set_switch(17); set_switch(18); set_switch(19); set_switch(20); set_switch(21); stop |
| 7 | 601 | 60 / 1 | 1 | 1 | trigger_event(6011); stop |
| 7 | 6011 | 60 / 2 | 3 | 30 | trigger_event(6012); stop |
| 7 | 6012 | 60 / 3 | 6 | 1 | set_switch(5); set_switch(6); set_switch(7); set_switch(8); set_switch(9); set_switch(11); set_switch(12); stop |
| 7 | 602 | 60 / 4 | 5 | 1 | stop |
| 7 | 611 | 61 / 1 | 1 | 1 | trigger_event(6111); stop |
| 7 | 6111 | 61 / 2 | 7 | 1 | trigger_event(6112); stop |
| 7 | 6112 | 61 / 3 | 5 | 1 | trigger_event(6113); stop |
| 7 | 6113 | 61 / 4 | 2 | 60 | set_switch(23); set_switch(24); set_switch(25); set_switch(26); stop |
| 7 | 701 | 70 / 1 | 3 | 1 | set_switch(22); stop |
| 7 | 702 | 70 / 2 | 5 | 1 | trigger_event(7021); stop |
| 7 | 7021 | 70 / 3 | 5 | 60 | trigger_event(7022); stop |
| 7 | 7022 | 70 / 3 | 5 | 1 | set_switch(28); set_switch(29); set_switch(30); stop |
| 7 | 801 | 80 / 1 | 3 | 1 | set_switch(11); set_switch(13); stop |
| 7 | 802 | 80 / 2 | 3 | 1 | set_switch(11); set_switch(13); stop |
| 7 | 803 | 80 / 3 | 2 | 1 | set_switch(13); set_switch(14); stop |
| 8 | 511 | 51 / 1 | 3 | 30 | stop |
| 8 | 531 | 53 / 1 | 6 | 30 | trigger_event(5311); stop |
| 8 | 5311 | 53 / 2 | 6 | 30 | set_switch(28); stop |
| 8 | 801 | 80 / 1 | 5 | 30 | trigger_event(8011); stop |
| 8 | 8011 | 80 / 2 | 2 | 180 | trigger_event(8012); stop |
| 8 | 8012 | 80 / 3 | 2 | 180 | trigger_event(8013); stop |
| 8 | 8013 | 80 / 4 | 2 | 30 | stop |
| 8 | 802 | 80 / 5 | 2 | 30 | trigger_event(8021); stop |
| 8 | 8021 | 80 / 6 | 1 | 180 | trigger_event(8022); stop |
| 8 | 8022 | 80 / 7 | 1 | 180 | trigger_event(8023); stop |
| 8 | 803 | 80 / 8 | 1 | 30 | trigger_event(8031); stop |
| 8 | 8031 | 80 / 9 | 3 | 120 | trigger_event(8032); stop |
| 8 | 8032 | 80 / 10 | 3 | 90 | trigger_event(8033); stop |
| 8 | 8033 | 80 / 11 | 3 | 120 | trigger_event(8034); stop |
| 8 | 8034 | 80 / 12 | 1 | 30 | trigger_event(8035); stop |
| 8 | 8035 | 80 / 13 | 3 | 90 | trigger_event(8036); stop |
| 8 | 8036 | 80 / 14 | 1 | 120 | trigger_event(8037); stop |
| 8 | 8037 | 80 / 15 | 2 | 120 | stop |

## Review notes

- Floor 8: event 8022 targets absent event 8023
