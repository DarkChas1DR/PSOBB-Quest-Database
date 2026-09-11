# 8-2:Desire\'s End — government-ep2/q467-bb-e

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/government-ep2/q467-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep2/q467-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep2/q467-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 467; language E. Static scan: **485 objects, 184 enemy/NPC records, 75 events, 161 script labels.** Script roundtrip: byte-identical.

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
0x0B, 0x1D, 0x00, 0x00, 0x00
0x0C, 0x1D, 0x00, 0x01, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 53 | 19 | 0 |
| 11 | 242 | 90 | 32 |
| 12 | 190 | 75 | 43 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 11 | 201 | 20 / 1 | 2 | 1 | trigger_event(2011); stop |
| 11 | 2011 | 20 / 2 | 4 | 1 | set_switch(33); set_switch(34); set_switch(35); set_switch(36); set_switch(37); set_switch(38); stop |
| 11 | 303 | 30 / 1 | 2 | 1 | stop |
| 11 | 301 | 30 / 2 | 2 | 1 | set_switch(22); set_switch(23); stop |
| 11 | 504 | 50 / 1 | 3 | 1 | set_switch(7); set_switch(45); stop |
| 11 | 511 | 51 / 1 | 4 | 1 | set_switch(39); stop |
| 11 | 521 | 52 / 1 | 3 | 1 | set_switch(43); set_switch(44); stop |
| 11 | 702 | 70 / 1 | 4 | 60 | trigger_event(7021); stop |
| 11 | 7021 | 70 / 2 | 2 | 150 | trigger_event(7022); stop |
| 11 | 7022 | 70 / 3 | 4 | 1 | set_switch(4); set_switch(5); stop |
| 11 | 713 | 71 / 1 | 4 | 100 | trigger_event(7131); stop |
| 11 | 7131 | 71 / 2 | 2 | 150 | trigger_event(7132); stop |
| 11 | 7132 | 71 / 3 | 2 | 1 | trigger_event(7133); stop |
| 11 | 7133 | 71 / 4 | 3 | 1 | trigger_event(7134); stop |
| 11 | 7134 | 71 / 5 | 3 | 300 | set_switch(28); set_switch(29); set_switch(30); set_switch(31); set_switch(33); set_switch(34); stop |
| 11 | 711 | 71 / 6 | 4 | 1 | stop |
| 11 | 803 | 80 / 1 | 4 | 100 | trigger_event(8031); stop |
| 11 | 8031 | 80 / 2 | 2 | 200 | set_switch(10); set_switch(11); set_switch(12); set_switch(13); set_switch(14); set_switch(15); set_switch(16); set_switch(46); stop |
| 11 | 801 | 80 / 3 | 3 | 1 | stop |
| 11 | 811 | 81 / 1 | 2 | 100 | trigger_event(8111); stop |
| 11 | 8111 | 81 / 2 | 3 | 200 | set_switch(40); set_switch(41); set_switch(42); stop |
| 11 | 902 | 90 / 1 | 4 | 60 | trigger_event(9021); stop |
| 11 | 9021 | 90 / 2 | 5 | 1 | trigger_event(9022); stop |
| 11 | 9022 | 90 / 3 | 5 | 1 | set_switch(19); set_switch(20); set_switch(21); set_switch(24); set_switch(25); set_switch(26); set_switch(27); stop |
| 11 | 953 | 95 / 1 | 1 | 700 | set_switch(17); stop |
| 11 | 951 | 95 / 2 | 2 | 200 | stop |
| 11 | 2112 | 211 / 1 | 2 | 30 | trigger_event(21121); stop |
| 11 | 21121 | 211 / 2 | 1 | 150 | set_switch(32); stop |
| 11 | 2142 | 214 / 1 | 2 | 30 | stop |
| 11 | 2163 | 216 / 1 | 1 | 100 | stop |
| 11 | 2802 | 280 / 1 | 3 | 1 | stop |
| 11 | 2912 | 291 / 1 | 2 | 60 | set_switch(18); stop |
| 12 | 201 | 20 / 1 | 5 | 30 | trigger_event(2011); stop |
| 12 | 2011 | 20 / 2 | 4 | 30 | set_switch(19); stop |
| 12 | 301 | 30 / 1 | 4 | 0 | stop |
| 12 | 501 | 50 / 1 | 2 | 100 | set_switch(20); stop |
| 12 | 701 | 70 / 1 | 2 | 60 | trigger_event(7011); stop |
| 12 | 7011 | 70 / 2 | 2 | 150 | trigger_event(7012); stop |
| 12 | 7012 | 70 / 3 | 4 | 10 | set_switch(5); set_switch(8); set_switch(10); set_switch(42); stop |
| 12 | 711 | 71 / 1 | 2 | 120 | trigger_event(7111); stop |
| 12 | 7111 | 71 / 2 | 1 | 60 | trigger_event(7112); stop |
| 12 | 7112 | 71 / 3 | 1 | 60 | trigger_event(7113); stop |
| 12 | 7113 | 71 / 4 | 1 | 60 | trigger_event(7114); stop |
| 12 | 7114 | 71 / 5 | 1 | 60 | trigger_event(7115); stop |
| 12 | 7115 | 71 / 6 | 1 | 90 | stop |
| 12 | 712 | 71 / 7 | 1 | 120 | trigger_event(7121); stop |
| 12 | 7121 | 71 / 8 | 1 | 60 | trigger_event(7122); stop |
| 12 | 7122 | 71 / 9 | 1 | 60 | trigger_event(7123); stop |
| 12 | 7123 | 71 / 10 | 1 | 60 | trigger_event(7124); stop |
| 12 | 7124 | 71 / 11 | 1 | 60 | trigger_event(7125); stop |
| 12 | 7125 | 71 / 12 | 1 | 60 | stop |
| 12 | 713 | 71 / 13 | 1 | 120 | trigger_event(7131); stop |
| 12 | 7131 | 71 / 14 | 1 | 60 | trigger_event(7132); stop |
| 12 | 7132 | 71 / 15 | 1 | 60 | trigger_event(7133); stop |
| 12 | 7133 | 71 / 16 | 1 | 60 | trigger_event(7134); stop |
| 12 | 7134 | 71 / 17 | 1 | 60 | trigger_event(7135); stop |
| 12 | 7135 | 71 / 18 | 1 | 60 | stop |
| 12 | 714 | 71 / 19 | 1 | 120 | trigger_event(7141); stop |
| 12 | 7141 | 71 / 20 | 1 | 60 | trigger_event(7142); stop |
| 12 | 7142 | 71 / 21 | 1 | 60 | trigger_event(7143); stop |
| 12 | 7143 | 71 / 22 | 1 | 60 | trigger_event(7144); stop |
| 12 | 7144 | 71 / 23 | 1 | 60 | trigger_event(7145); stop |
| 12 | 7145 | 71 / 24 | 1 | 60 | stop |
| 12 | 715 | 71 / 25 | 2 | 600 | trigger_event(7151); stop |
| 12 | 7151 | 71 / 26 | 2 | 300 | trigger_event(7152); stop |
| 12 | 7152 | 71 / 27 | 3 | 900 | stop |
| 12 | 811 | 81 / 1 | 4 | 120 | trigger_event(8111); stop |
| 12 | 8111 | 81 / 2 | 2 | 60 | trigger_event(8112); stop |
| 12 | 8112 | 81 / 3 | 2 | 10 | trigger_event(8113); stop |
| 12 | 8113 | 81 / 4 | 1 | 300 | set_switch(9); set_switch(11); set_switch(12); set_switch(13); set_switch(14); set_switch(15); set_switch(16); stop |
| 12 | 812 | 81 / 5 | 1 | 0 | stop |
| 12 | 951 | 95 / 1 | 2 | 150 | trigger_event(9511); stop |
| 12 | 9511 | 95 / 2 | 1 | 300 | set_switch(17); set_switch(18); stop |
| 12 | 952 | 95 / 3 | 4 | 1 | stop |
| 12 | 2901 | 290 / 1 | 3 | 0 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
