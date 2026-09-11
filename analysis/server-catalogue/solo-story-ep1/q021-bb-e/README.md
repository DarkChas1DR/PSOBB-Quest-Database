# Unsealed Door — solo-story-ep1/q021-bb-e

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/solo-story-ep1/q021-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/solo-story-ep1/q021-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/solo-story-ep1/q021-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 21; language E. Static scan: **373 objects, 182 enemy/NPC records, 46 events, 116 script labels.** Script roundtrip: byte-identical.

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
0x07, 0x07, 0x00, 0x01, 0x00
0x06, 0x06, 0x00, 0x00, 0x01
0x0C, 0x0C, 0x02, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 19 | 0 |
| 6 | 171 | 89 | 25 |
| 7 | 161 | 73 | 20 |
| 12 | 15 | 1 | 1 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 12 | 1 | 1 / 1 | 1 | 50 | construct_objects(room=1,group_or_wave=1); stop |
| 6 | 211 | 21 / 1 | 3 | 1 | set_switch(24); stop |
| 6 | 301 | 30 / 1 | 1 | 60 | trigger_event(3011); stop |
| 6 | 3011 | 30 / 2 | 4 | 60 | trigger_event(3012); stop |
| 6 | 3012 | 30 / 3 | 4 | 30 | set_switch(15); set_switch(16); stop |
| 6 | 501 | 50 / 1 | 4 | 1 | trigger_event(5011); stop |
| 6 | 5011 | 50 / 2 | 4 | 1 | set_switch(1); set_switch(2); set_switch(3); stop |
| 6 | 502 | 50 / 3 | 1 | 1 | stop |
| 6 | 511 | 51 / 1 | 1 | 1 | trigger_event(5111); stop |
| 6 | 5111 | 51 / 2 | 3 | 60 | set_switch(7); set_switch(8); set_switch(9); set_switch(11); stop |
| 6 | 521 | 52 / 1 | 5 | 1 | set_switch(23); stop |
| 6 | 531 | 53 / 1 | 4 | 1 | trigger_event(5311); stop |
| 6 | 5311 | 53 / 2 | 4 | 60 | set_switch(33); set_switch(34); set_switch(35); set_switch(36); stop |
| 6 | 541 | 54 / 1 | 4 | 1 | trigger_event(5411); stop |
| 6 | 5411 | 54 / 2 | 4 | 1 | set_switch(31); set_switch(32); stop |
| 6 | 601 | 60 / 1 | 4 | 1 | trigger_event(6011); stop |
| 6 | 6011 | 60 / 2 | 6 | 60 | trigger_event(6012); stop |
| 6 | 6012 | 60 / 3 | 1 | 30 | trigger_event(6013); stop |
| 6 | 6013 | 60 / 4 | 2 | 60 | set_switch(3); set_switch(5); set_switch(6); set_switch(7); stop |
| 6 | 611 | 61 / 1 | 3 | 1 | trigger_event(6111); stop |
| 6 | 6111 | 61 / 2 | 4 | 1 | trigger_event(6112); stop |
| 6 | 6112 | 61 / 3 | 4 | 60 | set_switch(26); set_switch(27); set_switch(28); set_switch(29); set_switch(30); stop |
| 6 | 751 | 75 / 1 | 5 | 1 | set_switch(11); set_switch(12); set_switch(13); set_switch(38); stop |
| 6 | 752 | 75 / 2 | 4 | 1 | set_switch(14); stop |
| 6 | 901 | 90 / 1 | 6 | 1 | set_switch(17); set_switch(18); set_switch(19); set_switch(20); set_switch(21); set_switch(22); stop |
| 6 | 902 | 90 / 2 | 4 | 1 | stop |
| 7 | 201 | 20 / 1 | 4 | 1 | set_switch(2); set_switch(4); set_switch(5); stop |
| 7 | 301 | 30 / 1 | 5 | 1 | trigger_event(3011); stop |
| 7 | 3011 | 30 / 2 | 4 | 60 | trigger_event(3012); stop |
| 7 | 3012 | 30 / 3 | 2 | 60 | set_switch(17); set_switch(18); stop |
| 7 | 501 | 50 / 1 | 8 | 1 | set_switch(10); set_switch(12); stop |
| 7 | 511 | 51 / 1 | 6 | 1 | trigger_event(5111); stop |
| 7 | 5111 | 51 / 2 | 5 | 60 | set_switch(6); set_switch(7); set_switch(8); set_switch(9); stop |
| 7 | 521 | 52 / 1 | 3 | 1 | trigger_event(5211); stop |
| 7 | 5211 | 52 / 2 | 3 | 30 | trigger_event(5212); stop |
| 7 | 5212 | 52 / 3 | 1 | 1 | set_switch(19); set_switch(21); set_switch(22); stop |
| 7 | 601 | 60 / 1 | 2 | 1 | trigger_event(6011); stop |
| 7 | 6011 | 60 / 2 | 2 | 30 | trigger_event(6012); stop |
| 7 | 6012 | 60 / 3 | 1 | 100 | set_switch(14); set_switch(15); set_switch(16); stop |
| 7 | 602 | 60 / 4 | 2 | 90 | trigger_event(6021); stop |
| 7 | 6021 | 60 / 5 | 2 | 45 | stop |
| 7 | 611 | 61 / 1 | 2 | 1 | trigger_event(6111); stop |
| 7 | 6111 | 61 / 2 | 6 | 60 | trigger_event(6112); stop |
| 7 | 6112 | 61 / 3 | 5 | 30 | set_switch(31); stop |
| 7 | 801 | 80 / 1 | 5 | 1 | set_switch(23); set_switch(24); set_switch(25); set_switch(27); set_switch(28); set_switch(30); stop |
| 7 | 802 | 80 / 2 | 5 | 1 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
