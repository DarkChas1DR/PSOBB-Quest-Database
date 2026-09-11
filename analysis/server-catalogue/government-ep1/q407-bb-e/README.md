# 2-4:Waterway Shadow — government-ep1/q407-bb-e

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/government-ep1/q407-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep1/q407-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep1/q407-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 407; language E. Static scan: **619 objects, 382 enemy/NPC records, 109 events, 108 script labels.** Script roundtrip: byte-identical.

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
0x03, 0x03, 0x00, 0x02, 0x01
0x04, 0x04, 0x00, 0x02, 0x01
0x05, 0x05, 0x00, 0x02, 0x01
0x0C, 0x0C, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 27 | 20 | 0 |
| 3 | 173 | 169 | 43 |
| 4 | 189 | 118 | 31 |
| 5 | 214 | 74 | 34 |
| 12 | 16 | 1 | 1 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 3 | 331 | 33 / 1 | 1 | 60 | trigger_event(3311); stop |
| 3 | 3311 | 33 / 2 | 3 | 60 | set_switch(31); set_switch(32); stop |
| 3 | 521 | 52 / 1 | 3 | 60 | trigger_event(5211); stop |
| 3 | 5211 | 52 / 2 | 3 | 60 | trigger_event(5212); stop |
| 3 | 5212 | 52 / 3 | 3 | 60 | set_switch(29); set_switch(30); stop |
| 3 | 522 | 52 / 4 | 3 | 60 | trigger_event(5221); stop |
| 3 | 5221 | 52 / 5 | 2 | 60 | trigger_event(5222); stop |
| 3 | 5222 | 52 / 6 | 3 | 60 | stop |
| 3 | 523 | 52 / 7 | 4 | 60 | stop |
| 3 | 321 | 32 / 1 | 3 | 60 | trigger_event(3211); stop |
| 3 | 3211 | 32 / 2 | 4 | 60 | set_switch(20); set_switch(27); set_switch(28); set_switch(23); set_switch(24); stop |
| 3 | 322 | 32 / 3 | 1 | 60 | trigger_event(3221); stop |
| 3 | 3221 | 32 / 4 | 3 | 60 | stop |
| 3 | 111 | 11 / 1 | 4 | 60 | set_switch(17); set_switch(18); set_switch(19); set_switch(21); set_switch(20); stop |
| 3 | 311 | 31 / 1 | 6 | 60 | trigger_event(3111); stop |
| 3 | 3111 | 31 / 2 | 4 | 60 | trigger_event(3112); stop |
| 3 | 3112 | 31 / 3 | 5 | 60 | set_switch(23); set_switch(24); set_switch(27); set_switch(28); set_switch(19); set_switch(21); set_switch(22); set_switch(26); stop |
| 3 | 511 | 51 / 1 | 5 | 60 | trigger_event(5111); stop |
| 3 | 5111 | 51 / 2 | 4 | 60 | set_switch(25); stop |
| 3 | 512 | 51 / 3 | 5 | 60 | stop |
| 3 | 601 | 60 / 1 | 6 | 60 | trigger_event(6011); stop |
| 3 | 6011 | 60 / 2 | 6 | 60 | trigger_event(6012); stop |
| 3 | 6012 | 60 / 3 | 4 | 60 | trigger_event(6013); stop |
| 3 | 6013 | 60 / 4 | 7 | 60 | trigger_event(6014); stop |
| 3 | 6014 | 60 / 5 | 6 | 60 | set_switch(12); set_switch(16); stop |
| 3 | 501 | 50 / 1 | 4 | 60 | trigger_event(5011); stop |
| 3 | 5011 | 50 / 2 | 7 | 60 | trigger_event(5012); stop |
| 3 | 5012 | 50 / 3 | 4 | 60 | set_switch(13); set_switch(14); set_switch(11); set_switch(10); set_switch(5); stop |
| 3 | 502 | 50 / 4 | 6 | 60 | stop |
| 3 | 301 | 30 / 1 | 5 | 60 | trigger_event(3011); stop |
| 3 | 3011 | 30 / 2 | 5 | 60 | trigger_event(3012); stop |
| 3 | 3012 | 30 / 3 | 6 | 60 | set_switch(15); stop |
| 3 | 401 | 40 / 1 | 6 | 60 | set_switch(6); set_switch(7); set_switch(3); stop |
| 3 | 402 | 40 / 2 | 3 | 60 | set_switch(4); set_switch(8); stop |
| 3 | 341 | 34 / 1 | 1 | 60 | trigger_event(3411); stop |
| 3 | 3411 | 34 / 2 | 1 | 60 | trigger_event(3412); stop |
| 3 | 3412 | 34 / 3 | 3 | 60 | trigger_event(3413); stop |
| 3 | 3413 | 34 / 4 | 4 | 60 | set_switch(1); set_switch(2); stop |
| 3 | 342 | 34 / 5 | 3 | 60 | trigger_event(3421); stop |
| 3 | 3421 | 34 / 6 | 4 | 60 | trigger_event(3422); stop |
| 3 | 3422 | 34 / 7 | 1 | 60 | stop |
| 3 | 101 | 10 / 1 | 4 | 60 | trigger_event(1011); stop |
| 3 | 1011 | 10 / 2 | 4 | 60 | set_switch(9); stop |
| 4 | 151 | 15 / 1 | 7 | 10 | trigger_event(1511); stop |
| 4 | 1511 | 15 / 2 | 3 | 10 | set_switch(34); set_switch(35); stop |
| 4 | 401 | 40 / 1 | 4 | 10 | set_switch(33); set_switch(32); set_switch(25); stop |
| 4 | 351 | 35 / 1 | 4 | 10 | set_switch(26); set_switch(27); stop |
| 4 | 352 | 35 / 2 | 3 | 10 | stop |
| 4 | 301 | 30 / 1 | 5 | 10 | set_switch(28); set_switch(29); set_switch(30); set_switch(17); set_switch(15); set_switch(16); set_switch(18); set_switch(19); set_switch(22); stop |
| 4 | 231 | 23 / 1 | 3 | 10 | trigger_event(2311); stop |
| 4 | 2311 | 23 / 2 | 3 | 10 | set_switch(31); stop |
| 4 | 141 | 14 / 1 | 6 | 10 | set_switch(20); set_switch(21); set_switch(23); set_switch(24); stop |
| 4 | 452 | 14 / 2 | 5 | 10 | stop |
| 4 | 601 | 60 / 1 | 6 | 10 | trigger_event(6011); stop |
| 4 | 6011 | 60 / 2 | 2 | 10 | set_switch(14); set_switch(10); set_switch(9); set_switch(8); set_switch(11); set_switch(12); stop |
| 4 | 221 | 22 / 1 | 3 | 10 | trigger_event(2211); stop |
| 4 | 2211 | 22 / 2 | 3 | 10 | trigger_event(2212); stop |
| 4 | 2212 | 22 / 3 | 2 | 10 | set_switch(13); stop |
| 4 | 222 | 22 / 4 | 3 | 10 | trigger_event(2221); stop |
| 4 | 2221 | 22 / 5 | 3 | 10 | trigger_event(2222); stop |
| 4 | 2222 | 22 / 6 | 3 | 10 | stop |
| 4 | 211 | 21 / 1 | 5 | 10 | trigger_event(2111); stop |
| 4 | 2111 | 21 / 2 | 2 | 10 | set_switch(7); stop |
| 4 | 101 | 10 / 1 | 5 | 10 | set_switch(4); stop |
| 4 | 201 | 20 / 1 | 1 | 10 | trigger_event(2011); stop |
| 4 | 2011 | 20 / 2 | 3 | 10 | trigger_event(2012); stop |
| 4 | 2012 | 20 / 3 | 3 | 10 | trigger_event(2013); stop |
| 4 | 2013 | 20 / 4 | 2 | 10 | set_switch(2); set_switch(3); set_switch(5); set_switch(6); stop |
| 4 | 202 | 20 / 5 | 3 | 10 | trigger_event(2021); stop |
| 4 | 2021 | 20 / 6 | 2 | 10 | trigger_event(2022); stop |
| 4 | 2022 | 20 / 7 | 3 | 10 | stop |
| 4 | 111 | 11 / 1 | 6 | 10 | trigger_event(1111); stop |
| 4 | 1111 | 11 / 2 | 5 | 10 | trigger_event(1112); stop |
| 4 | 1112 | 11 / 3 | 6 | 10 | set_switch(1); stop |
| 5 | 201 | 20 / 1 | 3 | 30 | set_switch(2); stop |
| 5 | 501 | 50 / 1 | 2 | 30 | trigger_event(5011); stop |
| 5 | 5011 | 50 / 2 | 1 | 30 | trigger_event(5012); stop |
| 5 | 5012 | 50 / 3 | 3 | 30 | set_switch(3); set_switch(4); set_switch(5); set_switch(6); set_switch(7); set_switch(9); stop |
| 5 | 502 | 50 / 4 | 2 | 30 | stop |
| 5 | 301 | 30 / 1 | 2 | 30 | trigger_event(3011); stop |
| 5 | 3011 | 30 / 2 | 2 | 30 | trigger_event(3012); stop |
| 5 | 3012 | 30 / 3 | 2 | 30 | set_switch(10); stop |
| 5 | 211 | 21 / 1 | 2 | 30 | trigger_event(2111); stop |
| 5 | 2111 | 21 / 2 | 3 | 30 | set_switch(11); set_switch(32); stop |
| 5 | 411 | 41 / 1 | 3 | 30 | set_switch(13); set_switch(14); set_switch(15); set_switch(12); set_switch(18); set_switch(19); stop |
| 5 | 711 | 71 / 1 | 2 | 1 | trigger_event(7111); stop |
| 5 | 7111 | 71 / 2 | 2 | 1 | trigger_event(7112); stop |
| 5 | 7112 | 71 / 3 | 2 | 1 | set_switch(16); stop |
| 5 | 712 | 71 / 4 | 2 | 1 | stop |
| 5 | 231 | 23 / 1 | 2 | 30 | set_switch(17); stop |
| 5 | 701 | 70 / 1 | 3 | 30 | trigger_event(7011); stop |
| 5 | 7011 | 70 / 2 | 3 | 30 | trigger_event(7012); stop |
| 5 | 7012 | 70 / 3 | 2 | 1 | trigger_event(7013); stop |
| 5 | 7013 | 70 / 4 | 2 | 1 | trigger_event(7014); stop |
| 5 | 7014 | 70 / 5 | 3 | 1 | set_switch(24); set_switch(25); set_switch(23); set_switch(27); set_switch(22); set_switch(21); set_switch(20); set_switch(8); set_switch(33); stop |
| 5 | 531 | 53 / 1 | 1 | 30 | trigger_event(5311); stop |
| 5 | 5311 | 53 / 2 | 3 | 30 | trigger_event(5312); stop |
| 5 | 5312 | 53 / 3 | 2 | 30 | trigger_event(5313); stop |
| 5 | 5313 | 53 / 4 | 1 | 30 | set_switch(26); stop |
| 5 | 532 | 53 / 5 | 1 | 30 | trigger_event(5321); stop |
| 5 | 5321 | 53 / 6 | 1 | 30 | trigger_event(5322); stop |
| 5 | 5322 | 53 / 7 | 2 | 30 | stop |
| 5 | 311 | 31 / 1 | 3 | 30 | trigger_event(3111); stop |
| 5 | 3111 | 31 / 2 | 2 | 30 | set_switch(28); set_switch(29); set_switch(31); stop |
| 5 | 521 | 52 / 1 | 3 | 30 | trigger_event(5211); stop |
| 5 | 5211 | 52 / 2 | 2 | 30 | trigger_event(5212); stop |
| 5 | 5212 | 52 / 3 | 2 | 30 | set_switch(30); stop |
| 5 | 522 | 52 / 4 | 3 | 30 | stop |
| 12 | 1 | 1 / 1 | 1 | 50 | construct_objects(room=1,group_or_wave=1); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
