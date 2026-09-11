# ８－３：紫紺の灯火 — government-ep2/q468-bb-j

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/government-ep2/q468-bb-j.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep2/q468-bb-j.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep2/q468-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 468; language J. Static scan: **552 objects, 198 enemy/NPC records, 74 events, 104 script labels.** Script roundtrip: byte-identical.

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
0x0A, 0x1C, 0x00, 0x01, 0x01
0x0B, 0x1D, 0x00, 0x01, 0x01
0x0D, 0x1F, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 53 | 19 | 0 |
| 10 | 222 | 81 | 33 |
| 11 | 250 | 97 | 40 |
| 13 | 27 | 1 | 1 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 10 | 201 | 20 / 2 | 4 | 1 | stop |
| 10 | 202 | 20 / 1 | 1 | 200 | set_switch(13); set_switch(14); set_switch(15); set_switch(16); set_switch(17); set_switch(18); set_switch(19); stop |
| 10 | 211 | 21 / 1 | 1 | 300 | set_switch(3); set_switch(4); set_switch(44); stop |
| 10 | 601 | 60 / 1 | 2 | 1 | set_switch(21); stop |
| 10 | 612 | 61 / 1 | 2 | 10 | set_switch(2); set_switch(1); stop |
| 10 | 622 | 62 / 1 | 3 | 100 | trigger_event(6221); stop |
| 10 | 6221 | 62 / 2 | 3 | 30 | set_switch(42); set_switch(43); stop |
| 10 | 621 | 62 / 3 | 3 | 1 | stop |
| 10 | 623 | 62 / 4 | 1 | 150 | stop |
| 10 | 632 | 63 / 1 | 3 | 60 | trigger_event(6321); stop |
| 10 | 6321 | 63 / 2 | 3 | 10 | set_switch(33); set_switch(34); set_switch(37); stop |
| 10 | 633 | 63 / 3 | 1 | 60 | stop |
| 10 | 641 | 64 / 1 | 6 | 1 | set_switch(8); set_switch(9); set_switch(10); stop |
| 10 | 703 | 70 / 1 | 3 | 60 | trigger_event(7031); stop |
| 10 | 7031 | 70 / 2 | 1 | 300 | set_switch(22); set_switch(23); set_switch(24); stop |
| 10 | 711 | 71 / 1 | 4 | 150 | trigger_event(7111); stop |
| 10 | 7111 | 71 / 2 | 2 | 10 | trigger_event(7112); stop |
| 10 | 7112 | 71 / 3 | 2 | 100 | trigger_event(7113); stop |
| 10 | 7113 | 71 / 4 | 4 | 60 | trigger_event(7114); stop |
| 10 | 7114 | 71 / 5 | 3 | 150 | set_switch(25); set_switch(26); set_switch(38); set_switch(39); set_switch(40); set_switch(41); stop |
| 10 | 803 | 80 / 1 | 4 | 150 | trigger_event(8031); stop |
| 10 | 8031 | 80 / 2 | 3 | 60 | set_switch(5); set_switch(6); set_switch(45); set_switch(7); stop |
| 10 | 813 | 81 / 1 | 3 | 60 | trigger_event(8131); stop |
| 10 | 8131 | 81 / 2 | 1 | 60 | set_switch(29); set_switch(30); set_switch(31); set_switch(32); set_switch(28); set_switch(35); set_switch(36); stop |
| 10 | 814 | 81 / 3 | 2 | 100 | stop |
| 10 | 903 | 90 / 1 | 2 | 200 | trigger_event(9031); stop |
| 10 | 9031 | 90 / 2 | 1 | 100 | set_switch(11); set_switch(12); stop |
| 10 | 2111 | 211 / 1 | 2 | 1 | stop |
| 10 | 2131 | 213 / 1 | 1 | 1 | trigger_event(21311); stop |
| 10 | 21311 | 213 / 2 | 4 | 30 | set_switch(20); stop |
| 10 | 2602 | 260 / 1 | 1 | 1 | stop |
| 10 | 2801 | 280 / 1 | 3 | 1 | stop |
| 10 | 2812 | 281 / 1 | 2 | 300 | stop |
| 11 | 201 | 20 / 1 | 2 | 10 | trigger_event(2011); stop |
| 11 | 2011 | 20 / 2 | 5 | 10 | set_switch(18); stop |
| 11 | 301 | 30 / 1 | 4 | 1 | set_switch(42); set_switch(10); set_switch(11); set_switch(12); stop |
| 11 | 302 | 30 / 2 | 2 | 30 | stop |
| 11 | 503 | 50 / 1 | 2 | 1 | trigger_event(5031); stop |
| 11 | 5031 | 50 / 2 | 1 | 350 | set_switch(19); stop |
| 11 | 501 | 50 / 3 | 2 | 1 | stop |
| 11 | 512 | 51 / 1 | 4 | 100 | trigger_event(5121); stop |
| 11 | 5121 | 51 / 2 | 4 | 10 | set_switch(24); set_switch(25); set_switch(26); stop |
| 11 | 513 | 51 / 3 | 2 | 100 | stop |
| 11 | 521 | 52 / 1 | 5 | 1 | set_switch(27); set_switch(29); stop |
| 11 | 523 | 52 / 2 | 1 | 100 | stop |
| 11 | 531 | 53 / 1 | 2 | 1 | set_switch(38); stop |
| 11 | 702 | 70 / 1 | 2 | 100 | trigger_event(7021); stop |
| 11 | 7021 | 70 / 2 | 4 | 10 | trigger_event(7022); stop |
| 11 | 7022 | 70 / 3 | 2 | 100 | trigger_event(7023); stop |
| 11 | 7023 | 70 / 4 | 2 | 200 | trigger_event(7024); stop |
| 11 | 7024 | 70 / 5 | 0 | 300 | set_switch(6); set_switch(7); set_switch(5); set_switch(8); set_switch(39); stop |
| 11 | 712 | 71 / 1 | 6 | 90 | trigger_event(7121); stop |
| 11 | 7121 | 71 / 2 | 2 | 150 | trigger_event(7122); stop |
| 11 | 7122 | 71 / 3 | 2 | 30 | trigger_event(7123); stop |
| 11 | 7123 | 71 / 4 | 3 | 30 | trigger_event(7124); stop |
| 11 | 7124 | 71 / 5 | 0 | 200 | set_switch(20); set_switch(21); set_switch(22); set_switch(23); stop |
| 11 | 803 | 80 / 2 | 2 | 100 | trigger_event(8031); stop |
| 11 | 8031 | 80 / 3 | 2 | 600 | stop |
| 11 | 802 | 80 / 1 | 1 | 500 | set_switch(40); set_switch(41); set_switch(42); set_switch(43); stop |
| 11 | 801 | 80 / 4 | 4 | 1 | stop |
| 11 | 814 | 81 / 1 | 3 | 10 | set_switch(13); stop |
| 11 | 903 | 90 / 1 | 4 | 60 | trigger_event(9031); stop |
| 11 | 9031 | 90 / 2 | 5 | 30 | set_switch(36); set_switch(37); set_switch(28); set_switch(30); set_switch(31); set_switch(32); set_switch(33); stop |
| 11 | 901 | 90 / 3 | 2 | 1 | stop |
| 11 | 904 | 90 / 4 | 0 | 100 | stop |
| 11 | 952 | 95 / 1 | 1 | 300 | set_switch(14); set_switch(9); set_switch(3); set_switch(2); set_switch(1); set_switch(4); stop |
| 11 | 951 | 95 / 2 | 2 | 100 | trigger_event(9511); stop |
| 11 | 9511 | 95 / 3 | 2 | 600 | stop |
| 11 | 953 | 95 / 4 | 3 | 1 | stop |
| 11 | 2123 | 212 / 1 | 1 | 30 | stop |
| 11 | 2132 | 213 / 1 | 2 | 1 | stop |
| 11 | 2903 | 290 / 1 | 1 | 150 | set_switch(15); set_switch(16); set_switch(17); stop |
| 11 | 2901 | 290 / 2 | 3 | 1 | stop |
| 13 | 1 | 0 / 1 | 1 | 0 | construct_objects(room=1,group_or_wave=1); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
