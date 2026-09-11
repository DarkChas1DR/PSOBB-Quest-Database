# ７－４：中央管理区 — government-ep2/q464-bb-j

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/government-ep2/q464-bb-j.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep2/q464-bb-j.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep2/q464-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 464; language J. Static scan: **144 objects, 144 enemy/NPC records, 54 events, 98 script labels.** Script roundtrip: byte-identical.

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
0x05, 0x17, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 53 | 19 | 0 |
| 5 | 91 | 125 | 54 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 5 | 21 | 2 / 1 | 2 | 1 | set_switch(2); stop |
| 5 | 31 | 3 / 1 | 2 | 1 | trigger_event(311); stop |
| 5 | 311 | 3 / 2 | 4 | 60 | set_switch(3); stop |
| 5 | 41 | 4 / 1 | 3 | 1 | trigger_event(411); stop |
| 5 | 411 | 4 / 3 | 2 | 60 | set_switch(4); stop |
| 5 | 42 | 4 / 2 | 2 | 1 | stop |
| 5 | 51 | 5 / 1 | 3 | 30 | trigger_event(511); stop |
| 5 | 511 | 5 / 3 | 3 | 60 | set_switch(5); stop |
| 5 | 52 | 5 / 2 | 2 | 1 | stop |
| 5 | 111 | 11 / 1 | 6 | 60 | trigger_event(1111); trigger_event(112); trigger_event(113); trigger_event(114); stop |
| 5 | 1111 | 11 / 2 | 1 | 400 | trigger_event(1112); stop |
| 5 | 1112 | 11 / 3 | 1 | 400 | trigger_event(1113); stop |
| 5 | 1113 | 11 / 4 | 2 | 400 | stop |
| 5 | 112 | 11 / 5 | 2 | 30 | trigger_event(1121); stop |
| 5 | 1121 | 11 / 6 | 2 | 90 | trigger_event(1122); stop |
| 5 | 1122 | 11 / 7 | 2 | 120 | trigger_event(1123); stop |
| 5 | 1123 | 11 / 8 | 2 | 120 | stop |
| 5 | 113 | 11 / 9 | 2 | 30 | trigger_event(1131); stop |
| 5 | 1131 | 11 / 10 | 2 | 90 | trigger_event(1132); stop |
| 5 | 1132 | 11 / 11 | 2 | 120 | trigger_event(1133); stop |
| 5 | 1133 | 11 / 12 | 2 | 120 | stop |
| 5 | 114 | 11 / 13 | 2 | 30 | trigger_event(1141); stop |
| 5 | 1141 | 11 / 14 | 1 | 30 | trigger_event(1142); stop |
| 5 | 1142 | 11 / 15 | 1 | 90 | trigger_event(1143); stop |
| 5 | 1143 | 11 / 16 | 1 | 90 | stop |
| 5 | 121 | 12 / 1 | 4 | 60 | trigger_event(1211); trigger_event(122); trigger_event(123); trigger_event(124); stop |
| 5 | 1211 | 12 / 2 | 1 | 200 | trigger_event(1212); stop |
| 5 | 1212 | 12 / 3 | 3 | 90 | trigger_event(1213); stop |
| 5 | 1213 | 12 / 4 | 2 | 200 | trigger_event(1214); stop |
| 5 | 1214 | 12 / 17 | 3 | 300 | stop |
| 5 | 122 | 12 / 5 | 1 | 60 | trigger_event(1221); stop |
| 5 | 1221 | 12 / 6 | 1 | 90 | trigger_event(1222); stop |
| 5 | 1222 | 12 / 7 | 1 | 120 | trigger_event(1223); stop |
| 5 | 1223 | 12 / 8 | 1 | 120 | stop |
| 5 | 123 | 12 / 9 | 1 | 60 | trigger_event(1231); stop |
| 5 | 1231 | 12 / 10 | 1 | 90 | trigger_event(1232); stop |
| 5 | 1232 | 12 / 11 | 1 | 120 | trigger_event(1233); stop |
| 5 | 1233 | 12 / 12 | 1 | 120 | stop |
| 5 | 124 | 12 / 13 | 2 | 60 | trigger_event(1241); stop |
| 5 | 1241 | 12 / 14 | 2 | 90 | trigger_event(1242); stop |
| 5 | 1242 | 12 / 15 | 2 | 90 | trigger_event(1243); stop |
| 5 | 1243 | 12 / 16 | 2 | 60 | stop |
| 5 | 131 | 13 / 1 | 6 | 60 | trigger_event(1311); trigger_event(132); stop |
| 5 | 1311 | 13 / 2 | 4 | 30 | trigger_event(1312); stop |
| 5 | 1312 | 13 / 3 | 4 | 30 | trigger_event(1313); stop |
| 5 | 1313 | 13 / 4 | 5 | 200 | trigger_event(1314); trigger_event(133); stop |
| 5 | 1314 | 13 / 5 | 3 | 90 | trigger_event(1315); stop |
| 5 | 1315 | 13 / 6 | 4 | 120 | trigger_event(1316); stop |
| 5 | 1316 | 13 / 11 | 4 | 120 | trigger_event(1317); stop |
| 5 | 1317 | 13 / 12 | 4 | 400 | stop |
| 5 | 132 | 13 / 7 | 2 | 60 | trigger_event(1321); stop |
| 5 | 1321 | 13 / 8 | 2 | 120 | stop |
| 5 | 133 | 13 / 9 | 2 | 90 | trigger_event(1331); stop |
| 5 | 1331 | 13 / 10 | 2 | 120 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
