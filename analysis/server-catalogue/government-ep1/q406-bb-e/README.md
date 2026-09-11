# 2-3:The Mutation — government-ep1/q406-bb-e

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/government-ep1/q406-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep1/q406-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep1/q406-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 406; language E. Static scan: **441 objects, 260 enemy/NPC records, 85 events, 102 script labels.** Script roundtrip: byte-identical.

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
0x04, 0x04, 0x00, 0x02, 0x00
0x05, 0x05, 0x00, 0x00, 0x00
0x06, 0x05, 0x00, 0x01, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 27 | 20 | 0 |
| 4 | 176 | 116 | 32 |
| 5 | 190 | 88 | 42 |
| 6 | 48 | 36 | 11 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 4 | 131 | 13 / 1 | 4 | 10 | set_switch(5); stop |
| 4 | 201 | 20 / 1 | 6 | 10 | trigger_event(2011); stop |
| 4 | 2011 | 20 / 2 | 4 | 10 | trigger_event(2012); stop |
| 4 | 2012 | 20 / 3 | 2 | 10 | set_switch(3); set_switch(2); set_switch(4); set_switch(7); stop |
| 4 | 111 | 11 / 1 | 4 | 10 | set_switch(1); stop |
| 4 | 211 | 21 / 1 | 3 | 10 | trigger_event(2111); stop |
| 4 | 2111 | 21 / 2 | 3 | 10 | trigger_event(2112); stop |
| 4 | 2112 | 21 / 3 | 3 | 10 | set_switch(8); set_switch(9); set_switch(11); set_switch(12); set_switch(10); set_switch(14); stop |
| 4 | 212 | 21 / 4 | 3 | 10 | trigger_event(2121); stop |
| 4 | 2121 | 21 / 5 | 2 | 10 | trigger_event(2122); stop |
| 4 | 2122 | 21 / 6 | 1 | 10 | stop |
| 4 | 221 | 22 / 1 | 3 | 10 | trigger_event(2211); stop |
| 4 | 2211 | 22 / 2 | 2 | 10 | trigger_event(2212); stop |
| 4 | 2212 | 22 / 3 | 3 | 10 | set_switch(13); stop |
| 4 | 601 | 60 / 1 | 2 | 10 | trigger_event(6011); stop |
| 4 | 6011 | 60 / 2 | 2 | 10 | trigger_event(6012); stop |
| 4 | 6012 | 60 / 3 | 5 | 10 | set_switch(15); set_switch(16); stop |
| 4 | 451 | 45 / 1 | 6 | 10 | set_switch(17); set_switch(18); set_switch(19); set_switch(22); stop |
| 4 | 452 | 45 / 2 | 1 | 10 | stop |
| 4 | 141 | 14 / 1 | 6 | 10 | trigger_event(1411); stop |
| 4 | 1411 | 14 / 2 | 5 | 10 | set_switch(20); set_switch(21); set_switch(23); set_switch(24); stop |
| 4 | 301 | 30 / 1 | 4 | 10 | set_switch(28); set_switch(29); set_switch(30); set_switch(26); set_switch(27); set_switch(25); set_switch(32); stop |
| 4 | 231 | 23 / 1 | 5 | 10 | trigger_event(2311); stop |
| 4 | 2311 | 23 / 2 | 6 | 10 | set_switch(31); stop |
| 4 | 232 | 23 / 3 | 6 | 10 | stop |
| 4 | 401 | 40 / 1 | 3 | 10 | trigger_event(4011); stop |
| 4 | 4011 | 40 / 2 | 3 | 10 | trigger_event(4012); stop |
| 4 | 4012 | 40 / 3 | 5 | 10 | set_switch(33); set_switch(34); set_switch(35); stop |
| 4 | 402 | 40 / 4 | 3 | 10 | stop |
| 4 | 151 | 15 / 1 | 3 | 10 | trigger_event(1511); stop |
| 4 | 1511 | 15 / 2 | 3 | 10 | trigger_event(1512); stop |
| 4 | 1512 | 15 / 3 | 5 | 10 | set_switch(36); stop |
| 5 | 301 | 30 / 1 | 3 | 30 | trigger_event(3011); stop |
| 5 | 3011 | 30 / 2 | 3 | 30 | trigger_event(3012); stop |
| 5 | 3012 | 30 / 3 | 1 | 240 | set_switch(4); stop |
| 5 | 501 | 50 / 1 | 3 | 30 | trigger_event(5011); stop |
| 5 | 5011 | 50 / 2 | 3 | 30 | trigger_event(5012); stop |
| 5 | 5012 | 50 / 3 | 1 | 30 | set_switch(1); set_switch(5); set_switch(7); set_switch(8); set_switch(26); set_switch(32); set_switch(29); set_switch(27); set_switch(28); stop |
| 5 | 221 | 22 / 1 | 1 | 30 | trigger_event(2211); stop |
| 5 | 2211 | 22 / 2 | 2 | 30 | trigger_event(2212); stop |
| 5 | 2212 | 22 / 3 | 2 | 30 | set_switch(38); set_switch(33); stop |
| 5 | 521 | 52 / 1 | 2 | 1 | trigger_event(5211); stop |
| 5 | 5211 | 52 / 2 | 2 | 30 | trigger_event(5212); stop |
| 5 | 5212 | 52 / 3 | 2 | 30 | trigger_event(5213); stop |
| 5 | 5213 | 52 / 4 | 2 | 30 | set_switch(34); set_switch(35); stop |
| 5 | 701 | 70 / 1 | 1 | 30 | trigger_event(7011); stop |
| 5 | 7011 | 70 / 2 | 1 | 30 | trigger_event(7012); stop |
| 5 | 7012 | 70 / 3 | 4 | 240 | trigger_event(7013); stop |
| 5 | 7013 | 70 / 4 | 1 | 30 | set_switch(36); set_switch(37); stop |
| 5 | 331 | 33 / 1 | 2 | 30 | trigger_event(3311); stop |
| 5 | 3311 | 33 / 2 | 2 | 30 | trigger_event(3312); stop |
| 5 | 3312 | 33 / 3 | 2 | 30 | set_switch(29); set_switch(30); stop |
| 5 | 201 | 20 / 1 | 2 | 30 | trigger_event(2011); stop |
| 5 | 2011 | 20 / 2 | 1 | 40 | trigger_event(2012); stop |
| 5 | 2012 | 20 / 3 | 3 | 30 | set_switch(30); set_switch(31); set_switch(22); set_switch(15); stop |
| 5 | 511 | 51 / 1 | 2 | 30 | trigger_event(5111); stop |
| 5 | 5111 | 51 / 2 | 3 | 30 | trigger_event(5112); stop |
| 5 | 5112 | 51 / 3 | 1 | 30 | trigger_event(5113); stop |
| 5 | 5113 | 51 / 4 | 3 | 30 | set_switch(23); set_switch(24); set_switch(25); stop |
| 5 | 211 | 21 / 1 | 1 | 30 | trigger_event(2111); stop |
| 5 | 2111 | 21 / 2 | 1 | 30 | set_switch(7); set_switch(8); set_switch(9); set_switch(10); stop |
| 5 | 321 | 32 / 1 | 2 | 30 | set_switch(11); set_switch(12); set_switch(13); stop |
| 5 | 322 | 32 / 2 | 3 | 30 | trigger_event(3211); stop |
| 5 | 3211 | 32 / 3 | 3 | 30 | stop |
| 5 | 401 | 40 / 1 | 2 | 30 | trigger_event(4011); stop |
| 5 | 4011 | 40 / 2 | 2 | 30 | trigger_event(4012); stop |
| 5 | 4012 | 40 / 3 | 2 | 30 | set_switch(15); set_switch(16); set_switch(31); set_switch(22); set_switch(17); set_switch(18); stop |
| 5 | 711 | 71 / 1 | 3 | 30 | trigger_event(7111); stop |
| 5 | 7111 | 71 / 2 | 2 | 30 | trigger_event(7112); stop |
| 5 | 7112 | 71 / 3 | 2 | 30 | trigger_event(7113); stop |
| 5 | 7113 | 71 / 4 | 2 | 360 | set_switch(19); set_switch(20); stop |
| 5 | 231 | 23 / 1 | 2 | 30 | trigger_event(2311); stop |
| 5 | 2311 | 23 / 2 | 3 | 30 | trigger_event(2312); stop |
| 5 | 2312 | 23 / 3 | 3 | 30 | set_switch(21); stop |
| 6 | 311 | 31 / 1 | 3 | 30 | set_switch(23); set_switch(25); stop |
| 6 | 701 | 70 / 1 | 2 | 30 | trigger_event(7011); stop |
| 6 | 7011 | 70 / 2 | 1 | 30 | set_switch(101); stop |
| 6 | 702 | 70 / 3 | 3 | 180 | trigger_event(7021); stop |
| 6 | 7021 | 70 / 4 | 3 | 180 | trigger_event(7022); stop |
| 6 | 7022 | 70 / 5 | 3 | 180 | trigger_event(7023); stop |
| 6 | 7023 | 70 / 6 | 4 | 180 | set_switch(102); stop |
| 6 | 703 | 70 / 7 | 1 | 30 | trigger_event(7031); stop |
| 6 | 7031 | 70 / 8 | 2 | 30 | set_switch(103); stop |
| 6 | 704 | 70 / 9 | 8 | 90 | trigger_event(7041); stop |
| 6 | 7041 | 70 / 10 | 6 | 90 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
