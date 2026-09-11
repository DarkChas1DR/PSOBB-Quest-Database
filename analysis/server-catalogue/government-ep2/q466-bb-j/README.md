# ８－１：水底で眠るモノ — government-ep2/q466-bb-j

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/government-ep2/q466-bb-j.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep2/q466-bb-j.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep2/q466-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 466; language J. Static scan: **491 objects, 135 enemy/NPC records, 45 events, 115 script labels.** Script roundtrip: byte-identical.

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
0x0A, 0x1C, 0x00, 0x00, 0x00
0x0B, 0x1C, 0x00, 0x01, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 53 | 19 | 0 |
| 10 | 249 | 97 | 38 |
| 11 | 189 | 19 | 7 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 10 | 201 | 20 / 1 | 3 | 30 | trigger_event(2011); stop |
| 10 | 2011 | 20 / 2 | 3 | 60 | set_switch(3); set_switch(4); set_switch(5); set_switch(8); stop |
| 10 | 212 | 21 / 1 | 4 | 30 | trigger_event(21201); stop |
| 10 | 21201 | 21 / 2 | 4 | 1 | trigger_event(21202); stop |
| 10 | 21202 | 21 / 3 | 4 | 60 | set_switch(40); set_switch(41); set_switch(42); stop |
| 10 | 301 | 30 / 1 | 3 | 1 | set_switch(11); set_switch(12); stop |
| 10 | 601 | 60 / 1 | 3 | 60 | set_switch(6); set_switch(7); set_switch(9); set_switch(10); stop |
| 10 | 603 | 60 / 2 | 3 | 150 | stop |
| 10 | 621 | 62 / 1 | 3 | 1 | set_switch(32); stop |
| 10 | 622 | 62 / 2 | 2 | 1 | trigger_event(6221); stop |
| 10 | 6221 | 62 / 3 | 0 | 1 | stop |
| 10 | 623 | 62 / 4 | 0 | 1 | trigger_event(6231); stop |
| 10 | 6231 | 62 / 5 | 0 | 1 | stop |
| 10 | 624 | 62 / 6 | 0 | 1 | stop |
| 10 | 631 | 63 / 1 | 5 | 1 | set_switch(45); set_switch(46); stop |
| 10 | 644 | 64 / 1 | 3 | 1 | stop |
| 10 | 645 | 64 / 2 | 1 | 150 | stop |
| 10 | 701 | 70 / 1 | 3 | 150 | trigger_event(7011); stop |
| 10 | 7011 | 70 / 2 | 4 | 1 | set_switch(23); set_switch(24); set_switch(25); set_switch(26); stop |
| 10 | 703 | 70 / 3 | 1 | 200 | stop |
| 10 | 712 | 71 / 1 | 2 | 1 | trigger_event(7121); stop |
| 10 | 7121 | 71 / 2 | 4 | 100 | trigger_event(7122); stop |
| 10 | 7122 | 71 / 3 | 3 | 1 | trigger_event(7123); stop |
| 10 | 7123 | 71 / 4 | 4 | 1 | trigger_event(7124); stop |
| 10 | 7124 | 71 / 5 | 3 | 200 | set_switch(34); set_switch(35); set_switch(36); set_switch(37); set_switch(47); set_switch(48); stop |
| 10 | 711 | 71 / 6 | 4 | 1 | stop |
| 10 | 801 | 80 / 1 | 2 | 1 | trigger_event(8011); stop |
| 10 | 8011 | 80 / 2 | 1 | 100 | set_switch(15); set_switch(16); stop |
| 10 | 804 | 80 / 3 | 1 | 200 | stop |
| 10 | 811 | 81 / 1 | 1 | 1 | set_switch(38); set_switch(39); stop |
| 10 | 902 | 90 / 1 | 4 | 30 | trigger_event(9021); stop |
| 10 | 9021 | 90 / 2 | 4 | 100 | set_switch(13); set_switch(14); set_switch(17); set_switch(18); set_switch(19); set_switch(20); set_switch(21); set_switch(22); set_switch(27); set_switch(28); set_switch(29); stop |
| 10 | 901 | 90 / 3 | 3 | 1 | stop |
| 10 | 2123 | 212 / 1 | 1 | 200 | stop |
| 10 | 2131 | 213 / 1 | 3 | 30 | trigger_event(21311); stop |
| 10 | 21311 | 213 / 2 | 2 | 1 | set_switch(33); stop |
| 10 | 2211 | 221 / 1 | 3 | 200 | stop |
| 10 | 2812 | 281 / 1 | 3 | 10 | stop |
| 11 | 611 | 61 / 1 | 3 | 1 | set_switch(3); set_switch(4); set_switch(5); stop |
| 11 | 801 | 80 / 1 | 4 | 120 | trigger_event(8011); stop |
| 11 | 8011 | 80 / 2 | 3 | 30 | trigger_event(8012); stop |
| 11 | 8012 | 80 / 3 | 2 | 30 | trigger_event(8013); stop |
| 11 | 8013 | 80 / 4 | 2 | 60 | trigger_event(8014); stop |
| 11 | 8014 | 80 / 5 | 2 | 60 | trigger_event(8015); stop |
| 11 | 8015 | 80 / 6 | 3 | 180 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
