# ５－２：適合試験２ ＶＲ神殿２ — government-ep2/q452-bb-j

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/government-ep2/q452-bb-j.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep2/q452-bb-j.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep2/q452-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 452; language J. Static scan: **446 objects, 195 enemy/NPC records, 48 events, 81 script labels.** Script roundtrip: byte-identical.

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
0x02, 0x14, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 53 | 18 | 0 |
| 1 | 181 | 94 | 26 |
| 2 | 212 | 83 | 22 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 101 | 10 / 1 | 4 | 10 | set_switch(3); set_switch(4); stop |
| 1 | 111 | 11 / 1 | 5 | 1 | set_switch(39); set_switch(40); stop |
| 1 | 201 | 20 / 1 | 4 | 10 | set_switch(13); set_switch(14); set_switch(15); set_switch(16); set_switch(17); set_switch(18); set_switch(19); set_switch(20); set_switch(31); set_switch(32); stop |
| 1 | 301 | 30 / 1 | 5 | 1 | set_switch(23); set_switch(24); stop |
| 1 | 401 | 40 / 1 | 6 | 1 | trigger_event(4011); stop |
| 1 | 4011 | 40 / 2 | 6 | 60 | trigger_event(4012); stop |
| 1 | 4012 | 40 / 3 | 5 | 150 | set_switch(21); set_switch(22); stop |
| 1 | 411 | 41 / 1 | 4 | 60 | trigger_event(4111); stop |
| 1 | 4111 | 41 / 2 | 5 | 100 | trigger_event(4112); stop |
| 1 | 4112 | 41 / 3 | 6 | 1 | set_switch(25); set_switch(26); set_switch(27); set_switch(28); stop |
| 1 | 601 | 60 / 1 | 5 | 1 | trigger_event(6011); stop |
| 1 | 6011 | 60 / 2 | 5 | 60 | set_switch(5); set_switch(6); stop |
| 1 | 611 | 61 / 1 | 4 | 10 | trigger_event(6111); stop |
| 1 | 6111 | 61 / 2 | 3 | 300 | set_switch(41); set_switch(42); set_switch(43); set_switch(44); stop |
| 1 | 701 | 70 / 1 | 3 | 10 | set_switch(35); set_switch(36); set_switch(37); set_switch(38); stop |
| 1 | 702 | 70 / 2 | 4 | 10 | stop |
| 1 | 703 | 70 / 3 | 2 | 100 | stop |
| 1 | 704 | 70 / 4 | 1 | 1 | stop |
| 1 | 911 | 91 / 1 | 1 | 1 | set_switch(29); set_switch(30); stop |
| 1 | 921 | 92 / 1 | 6 | 200 | set_switch(29); set_switch(30); set_switch(31); set_switch(32); set_switch(33); set_switch(34); stop |
| 1 | 931 | 93 / 1 | 4 | 10 | set_switch(7); set_switch(8); stop |
| 1 | 941 | 94 / 1 | 3 | 100 | trigger_event(9411); stop |
| 1 | 9411 | 94 / 2 | 0 | 100 | set_switch(7); set_switch(8); set_switch(9); set_switch(10); set_switch(11); set_switch(12); set_switch(13); set_switch(14); set_switch(15); set_switch(16); set_switch(17); set_switch(18); stop |
| 1 | 1021 | 102 / 1 | 1 | 1 | stop |
| 1 | 1401 | 140 / 1 | 1 | 1 | stop |
| 1 | 1641 | 100 / 1 | 0 | 1 | stop |
| 2 | 111 | 11 / 1 | 5 | 1 | trigger_event(1111); stop |
| 2 | 1111 | 11 / 2 | 6 | 10 | trigger_event(1112); stop |
| 2 | 1112 | 11 / 3 | 4 | 200 | set_switch(5); set_switch(6); set_switch(7); set_switch(8); set_switch(9); set_switch(10); set_switch(11); set_switch(14); set_switch(15); set_switch(16); set_switch(17); set_switch(18); set_switch(19); set_switch(20); set_switch(21); set_switch(22); set_switch(30); set_switch(31); set_switch(32); set_switch(33); set_switch(50); set_switch(51); stop |
| 2 | 301 | 30 / 1 | 5 | 300 | set_switch(34); set_switch(35); stop |
| 2 | 401 | 40 / 1 | 5 | 10 | trigger_event(4011); stop |
| 2 | 4011 | 40 / 2 | 6 | 10 | set_switch(3); set_switch(4); stop |
| 2 | 501 | 50 / 1 | 5 | 10 | trigger_event(5011); stop |
| 2 | 5011 | 50 / 2 | 6 | 10 | trigger_event(5012); stop |
| 2 | 5012 | 50 / 3 | 6 | 1 | set_switch(12); set_switch(13); stop |
| 2 | 502 | 50 / 4 | 1 | 10 | stop |
| 2 | 601 | 60 / 1 | 5 | 120 | trigger_event(6011); stop |
| 2 | 6011 | 60 / 2 | 4 | 10 | trigger_event(6012); stop |
| 2 | 6012 | 60 / 3 | 3 | 10 | trigger_event(6013); stop |
| 2 | 6013 | 60 / 4 | 4 | 10 | stop |
| 2 | 602 | 60 / 5 | 2 | 120 | trigger_event(6021); stop |
| 2 | 6021 | 60 / 6 | 2 | 10 | trigger_event(6022); stop |
| 2 | 6022 | 60 / 7 | 3 | 10 | stop |
| 2 | 921 | 92 / 1 | 2 | 1 | stop |
| 2 | 931 | 93 / 1 | 3 | 1 | stop |
| 2 | 941 | 94 / 1 | 4 | 1 | stop |
| 2 | 981 | 98 / 1 | 1 | 1 | stop |
| 2 | 1001 | 100 / 1 | 1 | 1 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
