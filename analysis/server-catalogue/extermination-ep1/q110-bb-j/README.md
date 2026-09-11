# 夢幻のごとく ３ — extermination-ep1/q110-bb-j

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/extermination-ep1/q110-bb-j.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/extermination-ep1/q110-bb-j.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/extermination-ep1/q110-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 110; language J. Static scan: **328 objects, 316 enemy/NPC records, 74 events, 43 script labels.** Script roundtrip: byte-identical.

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
0x06, 0x06, 0x00, 0x01, 0x00
0x07, 0x07, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 21 | 0 |
| 6 | 205 | 125 | 32 |
| 7 | 97 | 170 | 42 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 6 | 201 | 20 / 1 | 2 | 1 | stop |
| 6 | 211 | 21 / 1 | 2 | 1 | trigger_event(2111); stop |
| 6 | 2111 | 21 / 2 | 4 | 1 | set_switch(23); stop |
| 6 | 301 | 30 / 1 | 6 | 1 | trigger_event(3011); stop |
| 6 | 3011 | 30 / 2 | 6 | 45 | trigger_event(3012); stop |
| 6 | 3013 | 30 / 3 | 4 | 30 | set_switch(23); set_switch(19); set_switch(20); stop |
| 6 | 501 | 50 / 1 | 1 | 1 | trigger_event(5011); stop |
| 6 | 5011 | 50 / 2 | 7 | 60 | set_switch(8); set_switch(9); set_switch(10); set_switch(11); set_switch(12); stop |
| 6 | 511 | 51 / 1 | 5 | 1 | set_switch(15); set_switch(16); set_switch(17); set_switch(18); stop |
| 6 | 531 | 53 / 1 | 2 | 61 | trigger_event(5311); stop |
| 6 | 5311 | 53 / 2 | 2 | 90 | trigger_event(5312); stop |
| 6 | 5312 | 53 / 3 | 2 | 90 | stop |
| 6 | 532 | 53 / 4 | 2 | 81 | trigger_event(5321); stop |
| 6 | 5321 | 53 / 5 | 1 | 20 | trigger_event(5322); stop |
| 6 | 5322 | 53 / 6 | 2 | 80 | stop |
| 6 | 534 | 53 / 10 | 2 | 121 | trigger_event(5341); stop |
| 6 | 5341 | 53 / 11 | 2 | 1 | trigger_event(5342); stop |
| 6 | 5342 | 53 / 12 | 3 | 1 | trigger_event(5343); stop |
| 6 | 5343 | 53 / 13 | 4 | 70 | set_switch(32); set_switch(33); set_switch(34); stop |
| 6 | 601 | 60 / 1 | 6 | 1 | trigger_event(6011); stop |
| 6 | 6011 | 60 / 2 | 8 | 45 | trigger_event(6012); stop |
| 6 | 6012 | 60 / 3 | 8 | 60 | trigger_event(6013); stop |
| 6 | 6013 | 60 / 4 | 9 | 45 | set_switch(3); set_switch(4); set_switch(5); set_switch(6); set_switch(7); stop |
| 6 | 611 | 61 / 1 | 1 | 1 | trigger_event(6111); stop |
| 6 | 6111 | 61 / 2 | 6 | 45 | trigger_event(6112); stop |
| 6 | 6112 | 61 / 3 | 6 | 60 | set_switch(22); set_switch(24); set_switch(25); set_switch(26); set_switch(27); set_switch(28); stop |
| 6 | 751 | 75 / 1 | 2 | 1 | trigger_event(7511); stop |
| 6 | 7511 | 75 / 2 | 2 | 45 | stop |
| 6 | 752 | 75 / 3 | 4 | 60 | trigger_event(7521); stop |
| 6 | 7521 | 75 / 4 | 3 | 45 | set_switch(31); stop |
| 6 | 753 | 75 / 5 | 3 | 1 | stop |
| 6 | 754 | 75 / 6 | 4 | 30 | set_switch(29); stop |
| 7 | 211 | 21 / 1 | 1 | 1 | set_switch(17); stop |
| 7 | 301 | 30 / 1 | 6 | 1 | trigger_event(3011); stop |
| 7 | 3011 | 30 / 2 | 6 | 45 | trigger_event(3012); stop |
| 7 | 3012 | 30 / 3 | 4 | 20 | trigger_event(3013); stop |
| 7 | 3013 | 30 / 4 | 9 | 20 | trigger_event(3014); stop |
| 7 | 3015 | 30 / 5 | 1 | 20 | set_switch(215); stop |
| 7 | 401 | 40 / 1 | 2 | 1 | set_switch(1); set_switch(2); stop |
| 7 | 501 | 50 / 1 | 5 | 1 | trigger_event(5011); stop |
| 7 | 5011 | 50 / 2 | 8 | 40 | trigger_event(5012); stop |
| 7 | 5012 | 50 / 3 | 4 | 1 | set_switch(5); stop |
| 7 | 531 | 53 / 1 | 5 | 1 | trigger_event(5311); stop |
| 7 | 5311 | 53 / 2 | 6 | 60 | trigger_event(5312); stop |
| 7 | 5312 | 53 / 3 | 4 | 60 | trigger_event(5313); stop |
| 7 | 5313 | 53 / 4 | 4 | 60 | trigger_event(5314); stop |
| 7 | 5314 | 53 / 5 | 3 | 19 | trigger_event(5315); stop |
| 7 | 5315 | 53 / 6 | 1 | 1 | trigger_event(5316); stop |
| 7 | 5316 | 53 / 7 | 2 | 1 | trigger_event(5317); stop |
| 7 | 5317 | 53 / 8 | 4 | 60 | trigger_event(5318); stop |
| 7 | 5318 | 53 / 9 | 2 | 30 | trigger_event(5319); stop |
| 7 | 5319 | 53 / 10 | 2 | 30 | stop |
| 7 | 532 | 53 / 11 | 2 | 1 | trigger_event(5321); stop |
| 7 | 5321 | 53 / 12 | 5 | 20 | trigger_event(5322); stop |
| 7 | 5322 | 53 / 13 | 4 | 60 | trigger_event(5323); stop |
| 7 | 5323 | 53 / 14 | 1 | 45 | trigger_event(5324); stop |
| 7 | 5324 | 53 / 15 | 4 | 22 | trigger_event(5325); stop |
| 7 | 5325 | 53 / 16 | 5 | 20 | trigger_event(5326); stop |
| 7 | 5326 | 53 / 17 | 2 | 15 | trigger_event(5327); stop |
| 7 | 5327 | 53 / 18 | 4 | 60 | trigger_event(5328); stop |
| 7 | 5328 | 53 / 19 | 4 | 30 | trigger_event(5329); stop |
| 7 | 5329 | 53 / 20 | 2 | 40 | stop |
| 7 | 601 | 60 / 1 | 3 | 1 | trigger_event(6011); stop |
| 7 | 6011 | 60 / 2 | 4 | 30 | trigger_event(6012); stop |
| 7 | 6012 | 60 / 3 | 4 | 1 | stop |
| 7 | 602 | 60 / 4 | 2 | 1 | trigger_event(6021); stop |
| 7 | 6021 | 60 / 5 | 4 | 60 | trigger_event(6022); stop |
| 7 | 6022 | 60 / 6 | 2 | 60 | set_switch(5); set_switch(6); set_switch(7); set_switch(8); set_switch(9); set_switch(11); set_switch(12); stop |
| 7 | 801 | 80 / 1 | 4 | 1 | trigger_event(8011); stop |
| 7 | 8011 | 80 / 2 | 4 | 1 | trigger_event(8012); stop |
| 7 | 8012 | 80 / 3 | 4 | 1 | trigger_event(8013); stop |
| 7 | 8013 | 80 / 4 | 5 | 1 | trigger_event(8014); stop |
| 7 | 8014 | 80 / 5 | 5 | 1 | trigger_event(8015); stop |
| 7 | 8015 | 80 / 6 | 4 | 1 | set_switch(13); set_switch(14); stop |

## Review notes

- Floor 6: event 3011 targets absent event 3012
- Floor 7: event 3013 targets absent event 3014

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
