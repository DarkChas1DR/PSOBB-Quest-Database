# 新掃討作戦 第三号 — extermination-ep4/q818-bb-j

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/extermination-ep4/q818-bb-j.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/extermination-ep4/q818-bb-j.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/extermination-ep4/q818-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode4; header quest ID 818; language J. Static scan: **216 objects, 356 enemy/NPC records, 45 events, 120 script labels.** Script roundtrip: byte-identical.

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
0x00, 0x2D, 0x00, 0x00, 0x00
0x06, 0x29, 0x00, 0x02, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 17 | 0 |
| 6 | 190 | 339 | 45 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 6 | 201 | 20 / 1 | 11 | 30 | trigger_event(202); stop |
| 6 | 202 | 20 / 2 | 10 | 30 | trigger_event(203); stop |
| 6 | 203 | 20 / 3 | 6 | 30 | trigger_event(204); stop |
| 6 | 204 | 20 / 4 | 7 | 30 | trigger_event(205); stop |
| 6 | 205 | 20 / 5 | 9 | 30 | set_switch(20); stop |
| 6 | 501 | 50 / 1 | 8 | 30 | trigger_event(502); stop |
| 6 | 502 | 50 / 2 | 8 | 30 | trigger_event(503); stop |
| 6 | 503 | 50 / 3 | 5 | 30 | trigger_event(504); stop |
| 6 | 504 | 50 / 4 | 10 | 30 | trigger_event(505); stop |
| 6 | 505 | 50 / 5 | 10 | 30 | set_switch(50); stop |
| 6 | 601 | 60 / 1 | 7 | 30 | trigger_event(602); stop |
| 6 | 602 | 60 / 2 | 8 | 30 | trigger_event(603); stop |
| 6 | 603 | 60 / 3 | 7 | 30 | set_switch(60); stop |
| 6 | 611 | 61 / 1 | 4 | 30 | trigger_event(612); stop |
| 6 | 612 | 61 / 2 | 9 | 30 | trigger_event(613); stop |
| 6 | 613 | 61 / 3 | 7 | 30 | set_switch(61); stop |
| 6 | 621 | 62 / 1 | 6 | 30 | trigger_event(622); stop |
| 6 | 622 | 62 / 2 | 6 | 30 | trigger_event(623); stop |
| 6 | 623 | 62 / 3 | 7 | 30 | set_switch(62); stop |
| 6 | 701 | 70 / 1 | 5 | 30 | trigger_event(702); stop |
| 6 | 702 | 70 / 2 | 5 | 30 | trigger_event(703); stop |
| 6 | 703 | 70 / 3 | 6 | 30 | trigger_event(704); stop |
| 6 | 704 | 70 / 4 | 7 | 30 | trigger_event(705); stop |
| 6 | 705 | 70 / 5 | 8 | 30 | set_switch(70); stop |
| 6 | 901 | 90 / 1 | 7 | 30 | trigger_event(902); stop |
| 6 | 902 | 90 / 2 | 6 | 30 | trigger_event(903); stop |
| 6 | 903 | 90 / 3 | 6 | 30 | trigger_event(904); stop |
| 6 | 904 | 90 / 4 | 8 | 30 | trigger_event(905); stop |
| 6 | 905 | 90 / 5 | 5 | 30 | set_switch(90); stop |
| 6 | 101 | 100 / 1 | 8 | 30 | trigger_event(1002); stop |
| 6 | 1002 | 100 / 2 | 9 | 30 | trigger_event(1003); stop |
| 6 | 1003 | 100 / 3 | 9 | 30 | trigger_event(1004); stop |
| 6 | 1004 | 100 / 4 | 10 | 30 | trigger_event(1005); stop |
| 6 | 1005 | 100 / 5 | 11 | 30 | trigger_event(1006); stop |
| 6 | 1006 | 100 / 6 | 12 | 30 | set_switch(100); stop |
| 6 | 111 | 110 / 1 | 8 | 30 | trigger_event(1102); stop |
| 6 | 1102 | 110 / 2 | 7 | 30 | trigger_event(1103); stop |
| 6 | 1103 | 110 / 3 | 7 | 30 | trigger_event(1104); stop |
| 6 | 1104 | 110 / 4 | 9 | 30 | trigger_event(1105); stop |
| 6 | 1105 | 110 / 5 | 11 | 30 | trigger_event(1106); stop |
| 6 | 1106 | 110 / 6 | 10 | 30 | set_switch(110); stop |
| 6 | 641 | 64 / 1 | 4 | 30 | trigger_event(1202); stop |
| 6 | 1202 | 64 / 2 | 4 | 30 | trigger_event(1203); stop |
| 6 | 1203 | 64 / 3 | 6 | 30 | trigger_event(1204); stop |
| 6 | 1204 | 64 / 4 | 6 | 30 | set_switch(64); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
