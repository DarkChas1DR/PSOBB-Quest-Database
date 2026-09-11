# Addicting Food — solo-story-ep1/q010-bb-e

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/solo-story-ep1/q010-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/solo-story-ep1/q010-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/solo-story-ep1/q010-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 10; language E. Static scan: **497 objects, 393 enemy/NPC records, 110 events, 40 script labels.** Script roundtrip: byte-identical.

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
0x03, 0x03, 0x00, 0x00, 0x00
0x04, 0x04, 0x00, 0x00, 0x00
0x05, 0x05, 0x00, 0x00, 0x01
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 20 | 0 |
| 3 | 154 | 183 | 36 |
| 4 | 155 | 93 | 29 |
| 5 | 162 | 97 | 45 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 3 | 501 | 50 / 1 | 4 | 60 | stop |
| 3 | 502 | 50 / 2 | 6 | 60 | trigger_event(5021); stop |
| 3 | 5021 | 50 / 3 | 5 | 60 | trigger_event(5022); stop |
| 3 | 5022 | 50 / 4 | 4 | 60 | set_switch(2); set_switch(3); stop |
| 3 | 321 | 32 / 1 | 5 | 60 | trigger_event(3211); stop |
| 3 | 3211 | 32 / 2 | 4 | 60 | trigger_event(3212); stop |
| 3 | 3212 | 32 / 3 | 5 | 60 | set_switch(27); set_switch(5); set_switch(7); stop |
| 3 | 341 | 34 / 1 | 6 | 60 | trigger_event(3411); stop |
| 3 | 3411 | 34 / 2 | 6 | 60 | trigger_event(3412); stop |
| 3 | 3412 | 34 / 3 | 8 | 60 | set_switch(6); set_switch(10); stop |
| 3 | 531 | 53 / 1 | 6 | 60 | trigger_event(5311); stop |
| 3 | 5311 | 53 / 2 | 3 | 60 | trigger_event(5312); stop |
| 3 | 5312 | 53 / 3 | 4 | 60 | trigger_event(5313); stop |
| 3 | 5313 | 53 / 4 | 6 | 60 | set_switch(8); set_switch(11); set_switch(12); stop |
| 3 | 101 | 10 / 1 | 3 | 60 | trigger_event(1011); stop |
| 3 | 1011 | 10 / 2 | 4 | 60 | set_switch(8); set_switch(11); set_switch(12); stop |
| 3 | 601 | 60 / 1 | 6 | 60 | trigger_event(6011); stop |
| 3 | 6011 | 60 / 2 | 6 | 60 | trigger_event(6012); stop |
| 3 | 6012 | 60 / 3 | 6 | 60 | trigger_event(6013); stop |
| 3 | 6013 | 60 / 4 | 5 | 60 | set_switch(13); set_switch(14); stop |
| 3 | 113 | 11 / 1 | 1 | 60 | trigger_event(1111); stop |
| 3 | 1111 | 11 / 2 | 4 | 60 | set_switch(15); set_switch(16); set_switch(17); set_switch(18); stop |
| 3 | 112 | 11 / 3 | 3 | 60 | stop |
| 3 | 331 | 33 / 1 | 5 | 60 | trigger_event(3311); stop |
| 3 | 3311 | 33 / 2 | 8 | 60 | stop |
| 3 | 511 | 51 / 1 | 6 | 60 | trigger_event(5111); stop |
| 3 | 5111 | 51 / 2 | 7 | 60 | trigger_event(5112); stop |
| 3 | 5112 | 51 / 3 | 4 | 60 | trigger_event(5113); stop |
| 3 | 5113 | 51 / 4 | 1 | 60 | trigger_event(5114); stop |
| 3 | 5114 | 51 / 5 | 1 | 60 | set_switch(19); set_switch(20); set_switch(23); set_switch(25); set_switch(26); set_switch(24); set_switch(22); stop |
| 3 | 201 | 20 / 1 | 1 | 60 | stop |
| 3 | 202 | 20 / 2 | 2 | 60 | stop |
| 3 | 521 | 52 / 1 | 5 | 60 | trigger_event(5211); stop |
| 3 | 5211 | 52 / 2 | 2 | 60 | trigger_event(5212); stop |
| 3 | 5212 | 52 / 3 | 4 | 60 | trigger_event(5213); stop |
| 3 | 5213 | 52 / 4 | 5 | 60 | set_switch(21); stop |
| 4 | 141 | 14 / 1 | 3 | 60 | trigger_event(1411); stop |
| 4 | 1411 | 14 / 2 | 3 | 60 | set_switch(33); stop |
| 4 | 231 | 23 / 1 | 3 | 60 | trigger_event(2311); stop |
| 4 | 2311 | 23 / 2 | 4 | 60 | set_switch(32); set_switch(31); stop |
| 4 | 302 | 30 / 1 | 4 | 60 | set_switch(25); set_switch(30); set_switch(27); set_switch(24); stop |
| 4 | 303 | 30 / 2 | 7 | 60 | stop |
| 4 | 351 | 35 / 1 | 3 | 60 | set_switch(26); set_switch(28); stop |
| 4 | 352 | 35 / 2 | 0 | 60 | stop |
| 4 | 402 | 40 / 1 | 0 | 60 | set_switch(22); set_switch(23); set_switch(17); set_switch(18); set_switch(21); set_switch(35); set_switch(20); set_switch(19); set_switch(15); stop |
| 4 | 121 | 12 / 1 | 7 | 60 | stop |
| 4 | 122 | 12 / 2 | 1 | 60 | trigger_event(1221); stop |
| 4 | 1221 | 12 / 3 | 3 | 60 | set_switch(29); stop |
| 4 | 131 | 13 / 1 | 5 | 60 | set_switch(20); set_switch(19); set_switch(15); stop |
| 4 | 132 | 13 / 2 | 1 | 60 | stop |
| 4 | 601 | 60 / 1 | 2 | 60 | trigger_event(6011); stop |
| 4 | 6011 | 60 / 2 | 2 | 60 | trigger_event(6012); stop |
| 4 | 6012 | 60 / 3 | 5 | 60 | set_switch(13); set_switch(14); stop |
| 4 | 111 | 11 / 1 | 1 | 60 | trigger_event(1111); stop |
| 4 | 1111 | 11 / 2 | 4 | 60 | set_switch(12); stop |
| 4 | 211 | 21 / 1 | 3 | 60 | trigger_event(2111); stop |
| 4 | 2111 | 21 / 2 | 5 | 60 | trigger_event(2112); stop |
| 4 | 2112 | 21 / 3 | 2 | 60 | set_switch(6); set_switch(5); set_switch(9); set_switch(4); set_switch(7); set_switch(3); stop |
| 4 | 161 | 16 / 1 | 3 | 60 | trigger_event(1611); stop |
| 4 | 1611 | 16 / 2 | 6 | 60 | set_switch(10); stop |
| 4 | 221 | 22 / 1 | 2 | 60 | set_switch(8); stop |
| 4 | 201 | 20 / 1 | 6 | 60 | trigger_event(2011); stop |
| 4 | 2011 | 20 / 2 | 1 | 60 | trigger_event(2012); stop |
| 4 | 2012 | 20 / 3 | 6 | 60 | set_switch(2); stop |
| 4 | 151 | 15 / 1 | 1 | 60 | set_switch(1); stop |
| 5 | 501 | 50 / 1 | 3 | 30 | trigger_event(5011); stop |
| 5 | 5011 | 50 / 2 | 2 | 30 | trigger_event(5012); stop |
| 5 | 5012 | 50 / 3 | 1 | 30 | set_switch(4); set_switch(6); set_switch(26); set_switch(28); set_switch(32); set_switch(26); set_switch(27); set_switch(29); stop |
| 5 | 301 | 30 / 1 | 3 | 30 | trigger_event(3011); stop |
| 5 | 3011 | 30 / 2 | 2 | 30 | trigger_event(3012); stop |
| 5 | 3012 | 30 / 3 | 3 | 240 | set_switch(1); set_switch(2); set_switch(3); set_switch(13); stop |
| 5 | 221 | 22 / 1 | 2 | 30 | trigger_event(2211); stop |
| 5 | 2211 | 22 / 2 | 3 | 30 | set_switch(33); set_switch(38); stop |
| 5 | 521 | 52 / 1 | 3 | 1 | trigger_event(5211); stop |
| 5 | 5211 | 52 / 2 | 3 | 30 | trigger_event(5212); stop |
| 5 | 5212 | 52 / 3 | 3 | 30 | trigger_event(5213); stop |
| 5 | 5213 | 52 / 4 | 2 | 30 | set_switch(34); set_switch(35); stop |
| 5 | 701 | 70 / 1 | 2 | 10 | trigger_event(7011); stop |
| 5 | 7011 | 70 / 2 | 2 | 10 | trigger_event(7012); stop |
| 5 | 7012 | 70 / 3 | 1 | 30 | trigger_event(7013); stop |
| 5 | 7013 | 70 / 4 | 2 | 10 | set_switch(36); set_switch(37); stop |
| 5 | 331 | 33 / 1 | 2 | 30 | trigger_event(3311); stop |
| 5 | 3311 | 33 / 2 | 1 | 30 | set_switch(30); set_switch(29); stop |
| 5 | 201 | 20 / 1 | 1 | 30 | trigger_event(2011); stop |
| 5 | 2011 | 20 / 2 | 1 | 40 | trigger_event(2012); stop |
| 5 | 2012 | 20 / 3 | 2 | 30 | set_switch(30); set_switch(31); set_switch(22); set_switch(15); set_switch(16); set_switch(17); set_switch(14); stop |
| 5 | 511 | 51 / 1 | 1 | 30 | trigger_event(5111); stop |
| 5 | 5111 | 51 / 2 | 3 | 30 | trigger_event(5112); stop |
| 5 | 5112 | 51 / 3 | 2 | 30 | set_switch(23); stop |
| 5 | 311 | 31 / 1 | 3 | 30 | trigger_event(3111); stop |
| 5 | 3111 | 31 / 2 | 2 | 30 | trigger_event(3112); stop |
| 5 | 3112 | 31 / 3 | 2 | 30 | set_switch(24); set_switch(25); stop |
| 5 | 211 | 21 / 1 | 3 | 30 | trigger_event(2111); stop |
| 5 | 2111 | 21 / 2 | 2 | 30 | set_switch(8); set_switch(7); set_switch(9); set_switch(10); stop |
| 5 | 321 | 32 / 1 | 2 | 30 | trigger_event(3211); stop |
| 5 | 3211 | 32 / 2 | 1 | 30 | trigger_event(3212); stop |
| 5 | 3212 | 32 / 3 | 3 | 30 | set_switch(10); set_switch(9); set_switch(14); set_switch(15); set_switch(31); set_switch(22); set_switch(16); set_switch(17); stop |
| 5 | 241 | 24 / 1 | 1 | 30 | trigger_event(2411); stop |
| 5 | 2411 | 24 / 2 | 1 | 30 | set_switch(12); set_switch(11); stop |
| 5 | 611 | 61 / 1 | 1 | 10 | stop |
| 5 | 612 | 61 / 2 | 2 | 1 | trigger_event(6121); stop |
| 5 | 6121 | 61 / 3 | 3 | 1 | set_switch(18); stop |
| 5 | 711 | 71 / 1 | 3 | 30 | trigger_event(7111); stop |
| 5 | 7111 | 71 / 2 | 3 | 30 | trigger_event(7112); stop |
| 5 | 7112 | 71 / 3 | 3 | 30 | trigger_event(7113); stop |
| 5 | 7113 | 71 / 4 | 2 | 30 | trigger_event(7114); stop |
| 5 | 7114 | 71 / 5 | 1 | 10 | set_switch(19); set_switch(20); stop |
| 5 | 231 | 23 / 1 | 2 | 30 | trigger_event(2311); stop |
| 5 | 2311 | 23 / 2 | 3 | 30 | trigger_event(2312); stop |
| 5 | 2312 | 23 / 3 | 1 | 30 | set_switch(21); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
