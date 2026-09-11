# ライオネルのメール — solo-story-ep1/q016-bb-j

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/solo-story-ep1/q016-bb-j.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/solo-story-ep1/q016-bb-j.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/solo-story-ep1/q016-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 16; language J. Static scan: **498 objects, 274 enemy/NPC records, 87 events, 67 script labels.** Script roundtrip: byte-identical.

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
0x01, 0x01, 0x00, 0x00, 0x03
0x02, 0x02, 0x00, 0x00, 0x04
0x03, 0x03, 0x00, 0x01, 0x01
0x04, 0x04, 0x00, 0x01, 0x01
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 17 | 0 |
| 1 | 103 | 38 | 20 |
| 2 | 129 | 63 | 25 |
| 3 | 157 | 45 | 21 |
| 4 | 83 | 111 | 21 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 111 | 11 / 1 | 2 | 30 | trigger_event(1111); stop |
| 1 | 1111 | 11 / 2 | 4 | 30 | set_switch(4); stop |
| 1 | 71 | 7 / 1 | 2 | 30 | trigger_event(711); stop |
| 1 | 711 | 7 / 2 | 2 | 30 | trigger_event(712); stop |
| 1 | 712 | 7 / 3 | 2 | 30 | set_switch(2); set_switch(3); stop |
| 1 | 41 | 4 / 1 | 1 | 30 | trigger_event(411); stop |
| 1 | 411 | 4 / 2 | 4 | 30 | trigger_event(412); stop |
| 1 | 412 | 4 / 3 | 1 | 30 | trigger_event(413); stop |
| 1 | 413 | 4 / 4 | 2 | 30 | set_switch(9); stop |
| 1 | 81 | 8 / 1 | 1 | 30 | trigger_event(82); stop |
| 1 | 82 | 8 / 2 | 1 | 30 | stop |
| 1 | 21 | 2 / 1 | 1 | 30 | trigger_event(211); stop |
| 1 | 211 | 2 / 2 | 1 | 30 | trigger_event(212); stop |
| 1 | 212 | 2 / 3 | 3 | 30 | set_switch(1); stop |
| 1 | 22 | 2 / 4 | 2 | 30 | stop |
| 1 | 51 | 5 / 1 | 2 | 30 | trigger_event(511); stop |
| 1 | 511 | 5 / 2 | 2 | 30 | trigger_event(512); stop |
| 1 | 512 | 5 / 3 | 2 | 30 | trigger_event(513); stop |
| 1 | 513 | 5 / 4 | 2 | 30 | set_switch(7); set_switch(8); set_switch(6); set_switch(5); stop |
| 1 | 52 | 5 / 5 | 1 | 30 | stop |
| 2 | 11 | 1 / 1 | 3 | 30 | stop |
| 2 | 12 | 1 / 2 | 2 | 15 | set_switch(1); stop |
| 2 | 21 | 2 / 1 | 2 | 1 | trigger_event(211); stop |
| 2 | 211 | 2 / 2 | 2 | 30 | stop |
| 2 | 22 | 2 / 3 | 1 | 50 | trigger_event(221); stop |
| 2 | 221 | 2 / 4 | 2 | 30 | set_switch(4); set_switch(5); set_switch(6); stop |
| 2 | 31 | 3 / 1 | 1 | 15 | stop |
| 2 | 41 | 4 / 1 | 3 | 50 | trigger_event(411); stop |
| 2 | 411 | 4 / 2 | 3 | 20 | set_switch(31); stop |
| 2 | 61 | 6 / 1 | 2 | 1 | trigger_event(611); stop |
| 2 | 611 | 6 / 2 | 1 | 55 | stop |
| 2 | 62 | 6 / 3 | 2 | 30 | trigger_event(621); stop |
| 2 | 621 | 6 / 4 | 1 | 90 | set_switch(2); stop |
| 2 | 101 | 10 / 1 | 4 | 1 | stop |
| 2 | 111 | 11 / 1 | 3 | 5 | trigger_event(1111); stop |
| 2 | 1111 | 11 / 2 | 3 | 120 | trigger_event(1112); stop |
| 2 | 1112 | 11 / 3 | 4 | 30 | trigger_event(1113); stop |
| 2 | 1113 | 11 / 4 | 3 | 30 | set_switch(7); set_switch(8); set_switch(11); stop |
| 2 | 121 | 12 / 1 | 1 | 1 | trigger_event(1211); stop |
| 2 | 1211 | 12 / 2 | 5 | 30 | set_switch(10); stop |
| 2 | 131 | 13 / 1 | 2 | 1 | trigger_event(1311); stop |
| 2 | 1311 | 13 / 2 | 2 | 15 | trigger_event(1312); stop |
| 2 | 1312 | 13 / 3 | 2 | 15 | set_switch(9); stop |
| 2 | 132 | 13 / 4 | 1 | 80 | trigger_event(1321); stop |
| 2 | 1321 | 13 / 5 | 3 | 15 | stop |
| 3 | 111 | 11 / 1 | 2 | 60 | set_switch(29); set_switch(27); stop |
| 3 | 341 | 34 / 1 | 2 | 60 | trigger_event(3411); stop |
| 3 | 3411 | 34 / 2 | 2 | 60 | set_switch(28); set_switch(31); set_switch(26); stop |
| 3 | 331 | 33 / 1 | 2 | 60 | set_switch(32); set_switch(33); stop |
| 3 | 332 | 33 / 2 | 2 | 60 | stop |
| 3 | 521 | 52 / 1 | 3 | 60 | trigger_event(5211); stop |
| 3 | 5211 | 52 / 2 | 3 | 60 | set_switch(19); set_switch(18); set_switch(20); set_switch(23); set_switch(24); set_switch(25); set_switch(21); set_switch(22); stop |
| 3 | 321 | 32 / 1 | 1 | 60 | stop |
| 3 | 601 | 60 / 1 | 2 | 60 | trigger_event(6011); stop |
| 3 | 6011 | 60 / 2 | 2 | 60 | set_switch(16); set_switch(17); stop |
| 3 | 501 | 50 / 1 | 1 | 60 | set_switch(14); set_switch(15); set_switch(9); stop |
| 3 | 311 | 311 / 1 | 0 | 60 | trigger_event(3111); stop |
| 3 | 3111 | 31 / 2 | 2 | 60 | trigger_event(3112); stop |
| 3 | 3112 | 53 / 3 | 0 | 60 | set_switch(2); set_switch(4); set_switch(5); set_switch(6); set_switch(8); set_switch(10); set_switch(13); stop |
| 3 | 101 | 10 / 1 | 2 | 60 | stop |
| 3 | 511 | 51 / 1 | 2 | 60 | trigger_event(5111); stop |
| 3 | 5111 | 51 / 2 | 4 | 60 | trigger_event(5112); stop |
| 3 | 5112 | 51 / 3 | 3 | 60 | set_switch(1); set_switch(3); set_switch(7); stop |
| 3 | 301 | 30 / 1 | 2 | 60 | trigger_event(3011); stop |
| 3 | 3011 | 30 / 2 | 2 | 60 | set_switch(11); set_switch(12); stop |
| 3 | 302 | 30 / 3 | 1 | 60 | stop |
| 4 | 351 | 35 / 1 | 4 | 1 | set_switch(28); set_switch(29); stop |
| 4 | 301 | 30 / 1 | 2 | 1 | set_switch(26); set_switch(27); set_switch(24); set_switch(33); set_switch(32); set_switch(31); stop |
| 4 | 401 | 40 / 1 | 0 | 1 | trigger_event(4011); stop |
| 4 | 4011 | 40 / 2 | 0 | 1 | set_switch(20); set_switch(23); set_switch(25); set_switch(22); set_switch(21); set_switch(20); set_switch(17); set_switch(18); stop |
| 4 | 141 | 14 / 1 | 3 | 1 | stop |
| 4 | 451 | 45 / 1 | 2 | 1 | set_switch(19); stop |
| 4 | 602 | 60 / 1 | 3 | 1 | trigger_event(6021); stop |
| 4 | 6021 | 60 / 2 | 2 | 1 | set_switch(16); set_switch(15); set_switch(14); stop |
| 4 | 101 | 10 / 1 | 3 | 1 | trigger_event(1011); stop |
| 4 | 1011 | 10 / 2 | 3 | 1 | set_switch(11); stop |
| 4 | 211 | 20 / 1 | 4 | 1 | trigger_event(2111); stop |
| 4 | 2111 | 20 / 2 | 3 | 1 | trigger_event(2112); stop |
| 4 | 2112 | 20 / 3 | 2 | 1 | set_switch(9); set_switch(10); set_switch(3); set_switch(12); stop |
| 4 | 131 | 13 / 1 | 1 | 1 | set_switch(13); set_switch(1); stop |
| 4 | 221 | 22 / 1 | 7 | 1 | trigger_event(2211); stop |
| 4 | 2211 | 22 / 2 | 5 | 1 | set_switch(2); stop |
| 4 | 111 | 11 / 1 | 4 | 1 | trigger_event(1111); stop |
| 4 | 1111 | 11 / 2 | 2 | 1 | set_switch(4); set_switch(5); stop |
| 4 | 121 | 12 / 1 | 7 | 1 | set_switch(6); set_switch(7); set_switch(8); stop |
| 4 | 122 | 12 / 2 | 1 | 1 | stop |
| 4 | 123 | 12 / 3 | 6 | 1 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
