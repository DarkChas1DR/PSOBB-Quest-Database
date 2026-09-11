# 明日の代価 — extermination-ep1/q117-bb-j

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/extermination-ep1/q117-bb-j.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/extermination-ep1/q117-bb-j.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/extermination-ep1/q117-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 117; language J. Static scan: **527 objects, 274 enemy/NPC records, 90 events, 284 script labels.** Script roundtrip: byte-identical.

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
0x05, 0x05, 0x00, 0x02, 0x00
0x06, 0x06, 0x00, 0x01, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 20 | 0 |
| 4 | 66 | 29 | 9 |
| 5 | 178 | 101 | 35 |
| 6 | 257 | 124 | 46 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 4 | 301 | 30 / 1 | 3 | 120 | trigger_event(3011); stop |
| 4 | 3011 | 30 / 2 | 3 | 10 | trigger_event(3012); stop |
| 4 | 3012 | 30 / 3 | 3 | 10 | stop |
| 4 | 302 | 30 / 4 | 2 | 10 | trigger_event(3021); stop |
| 4 | 3021 | 30 / 5 | 3 | 10 | stop |
| 4 | 451 | 45 / 1 | 4 | 10 | set_switch(20); set_switch(21); stop |
| 4 | 601 | 60 / 1 | 4 | 10 | trigger_event(6011); stop |
| 4 | 6011 | 60 / 2 | 3 | 60 | trigger_event(6012); stop |
| 4 | 6012 | 60 / 3 | 4 | 90 | set_switch(9); set_switch(10); set_switch(14); stop |
| 5 | 201 | 20 / 1 | 4 | 1 | trigger_event(2011); stop |
| 5 | 2011 | 20 / 2 | 2 | 1 | trigger_event(2012); stop |
| 5 | 2012 | 20 / 3 | 4 | 1 | trigger_event(2013); stop |
| 5 | 2013 | 20 / 4 | 1 | 1 | trigger_event(2014); stop |
| 5 | 2014 | 20 / 5 | 4 | 1 | set_switch(1); set_switch(2); stop |
| 5 | 211 | 21 / 1 | 4 | 60 | trigger_event(2111); stop |
| 5 | 2111 | 21 / 2 | 3 | 1 | trigger_event(2112); stop |
| 5 | 2112 | 21 / 3 | 3 | 1 | trigger_event(2113); stop |
| 5 | 2113 | 21 / 4 | 1 | 1 | trigger_event(2114); stop |
| 5 | 2114 | 21 / 5 | 1 | 1 | trigger_event(2115); stop |
| 5 | 2115 | 21 / 6 | 1 | 1 | set_switch(11); set_switch(12); set_switch(18); set_switch(19); stop |
| 5 | 301 | 30 / 1 | 1 | 1 | stop |
| 5 | 302 | 30 / 2 | 5 | 60 | trigger_event(3021); stop |
| 5 | 3021 | 30 / 3 | 4 | 1 | trigger_event(3022); stop |
| 5 | 3022 | 30 / 4 | 3 | 1 | set_switch(10); stop |
| 5 | 311 | 31 / 2 | 5 | 60 | trigger_event(3111); trigger_event(3112); stop |
| 5 | 3111 | 31 / 3 | 5 | 1 | trigger_event(3113); stop |
| 5 | 3113 | 31 / 5 | 2 | 1 | stop |
| 5 | 3112 | 31 / 4 | 2 | 1 | trigger_event(3114); stop |
| 5 | 3114 | 31 / 6 | 4 | 1 | set_switch(28); stop |
| 5 | 312 | 31 / 1 | 4 | 1 | stop |
| 5 | 501 | 50 / 1 | 4 | 150 | trigger_event(5011); stop |
| 5 | 5011 | 50 / 2 | 4 | 1 | trigger_event(5012); stop |
| 5 | 5012 | 50 / 3 | 4 | 1 | set_switch(4); set_switch(5); set_switch(6); set_switch(7); set_switch(8); set_switch(9); set_switch(20); stop |
| 5 | 701 | 70 / 1 | 4 | 1 | trigger_event(7011); stop |
| 5 | 7011 | 70 / 2 | 3 | 1 | trigger_event(7012); stop |
| 5 | 7012 | 70 / 3 | 4 | 1 | trigger_event(7013); stop |
| 5 | 7013 | 70 / 4 | 2 | 1 | trigger_event(7014); stop |
| 5 | 7014 | 70 / 5 | 4 | 1 | trigger_event(7015); stop |
| 5 | 7015 | 70 / 6 | 4 | 1 | set_switch(21); set_switch(22); set_switch(23); set_switch(24); set_switch(25); set_switch(26); set_switch(27); stop |
| 5 | 131 | 13 / 1 | 1 | 1 | stop |
| 5 | 11 | 1 / 1 | 1 | 1 | stop |
| 5 | 401 | 40 / 1 | 1 | 1 | stop |
| 5 | 411 | 41 / 1 | 1 | 1 | stop |
| 5 | 601 | 60 / 1 | 1 | 1 | stop |
| 6 | 511 | 51 / 1 | 4 | 1 | trigger_event(5111); stop |
| 6 | 5111 | 51 / 2 | 2 | 1 | trigger_event(5112); stop |
| 6 | 5112 | 51 / 3 | 4 | 1 | set_switch(13); set_switch(12); set_switch(11); set_switch(10); set_switch(4); set_switch(3); stop |
| 6 | 521 | 52 / 1 | 3 | 1 | trigger_event(5211); stop |
| 6 | 5211 | 52 / 2 | 4 | 1 | trigger_event(5212); stop |
| 6 | 5212 | 52 / 3 | 1 | 1 | trigger_event(5213); stop |
| 6 | 5213 | 52 / 4 | 6 | 1 | set_switch(21); set_switch(22); set_switch(23); set_switch(24); stop |
| 6 | 531 | 53 / 1 | 1 | 30 | trigger_event(5311); stop |
| 6 | 532 | 53 / 2 | 1 | 60 | stop |
| 6 | 533 | 53 / 3 | 1 | 90 | stop |
| 6 | 534 | 53 / 4 | 1 | 120 | stop |
| 6 | 5311 | 53 / 7 | 4 | 1 | trigger_event(5312); stop |
| 6 | 5312 | 53 / 8 | 4 | 1 | set_switch(25); set_switch(27); set_switch(29); set_switch(30); set_switch(31); set_switch(32); set_switch(33); stop |
| 6 | 601 | 60 / 1 | 5 | 300 | trigger_event(6011); stop |
| 6 | 6011 | 60 / 2 | 6 | 1 | trigger_event(6012); stop |
| 6 | 6012 | 60 / 3 | 6 | 1 | trigger_event(6013); stop |
| 6 | 6013 | 60 / 4 | 6 | 1 | trigger_event(6014); stop |
| 6 | 6014 | 60 / 5 | 6 | 1 | trigger_event(6015); stop |
| 6 | 6015 | 60 / 6 | 2 | 1 | trigger_event(6016); stop |
| 6 | 6016 | 60 / 7 | 4 | 1 | trigger_event(6017); stop |
| 6 | 6017 | 60 / 8 | 3 | 1 | trigger_event(6018); stop |
| 6 | 6018 | 60 / 9 | 3 | 1 | trigger_event(6019); stop |
| 6 | 6019 | 60 / 10 | 4 | 1 | set_switch(1); set_switch(5); set_switch(6); set_switch(7); set_switch(8); set_switch(9); stop |
| 6 | 611 | 61 / 1 | 2 | 1 | trigger_event(6113); stop |
| 6 | 6113 | 61 / 3 | 4 | 1 | trigger_event(6115); stop |
| 6 | 6115 | 61 / 7 | 2 | 1 | stop |
| 6 | 612 | 61 / 2 | 3 | 120 | trigger_event(6122); stop |
| 6 | 6122 | 61 / 4 | 2 | 1 | trigger_event(6124); stop |
| 6 | 6124 | 61 / 6 | 2 | 1 | trigger_event(6126); stop |
| 6 | 6126 | 61 / 8 | 2 | 1 | trigger_event(6127); stop |
| 6 | 6127 | 61 / 9 | 2 | 1 | trigger_event(6128); trigger_event(6129); trigger_event(61210); trigger_event(61211); stop |
| 6 | 6128 | 61 / 10 | 1 | 150 | trigger_event(61212); stop |
| 6 | 61212 | 61 / 14 | 1 | 10 | trigger_event(61213); stop |
| 6 | 61213 | 61 / 18 | 1 | 10 | stop |
| 6 | 6129 | 61 / 11 | 1 | 210 | trigger_event(61214); stop |
| 6 | 61214 | 61 / 15 | 1 | 10 | trigger_event(61215); stop |
| 6 | 61215 | 61 / 19 | 1 | 10 | stop |
| 6 | 61210 | 61 / 12 | 1 | 270 | trigger_event(61216); stop |
| 6 | 61216 | 61 / 16 | 1 | 10 | trigger_event(61217); stop |
| 6 | 61217 | 61 / 20 | 1 | 10 | stop |
| 6 | 61211 | 61 / 13 | 1 | 330 | trigger_event(61218); stop |
| 6 | 61218 | 61 / 17 | 1 | 10 | trigger_event(61219); stop |
| 6 | 61219 | 61 / 21 | 1 | 10 | set_switch(14); set_switch(15); set_switch(16); set_switch(17); set_switch(18); set_switch(19); set_switch(20); stop |
| 6 | 751 | 75 / 1 | 5 | 1 | trigger_event(7511); stop |
| 6 | 7511 | 75 / 2 | 3 | 1 | trigger_event(7512); stop |
| 6 | 7512 | 75 / 3 | 0 | 1 | set_switch(26); set_switch(28); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
