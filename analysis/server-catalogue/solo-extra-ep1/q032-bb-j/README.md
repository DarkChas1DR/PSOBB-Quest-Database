# 蠢動の獅子 — solo-extra-ep1/q032-bb-j

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/solo-extra-ep1/q032-bb-j.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/solo-extra-ep1/q032-bb-j.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/solo-extra-ep1/q032-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode4; header quest ID 32; language J. Static scan: **155 objects, 106 enemy/NPC records, 22 events, 354 script labels.** Script roundtrip: byte-identical.

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
0x06, 0x29, 0x00, 0x01, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 23 | 0 |
| 6 | 129 | 83 | 22 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 6 | 201 | 20 / 1 | 3 | 3 | trigger_event(202); set_switch(6); stop |
| 6 | 202 | 20 / 2 | 4 | 3 | trigger_event(203); stop |
| 6 | 203 | 20 / 3 | 5 | 3 | set_switch(20); set_switch(21); stop |
| 6 | 321 | 32 / 1 | 3 | 3 | set_switch(32); stop |
| 6 | 501 | 50 / 1 | 4 | 3 | trigger_event(502); stop |
| 6 | 502 | 50 / 2 | 5 | 3 | trigger_event(503); stop |
| 6 | 503 | 50 / 3 | 6 | 3 | set_switch(50); trigger_event(504); stop |
| 6 | 504 | 50 / 4 | 1 | 3 | stop |
| 6 | 641 | 64 / 1 | 3 | 3 | set_switch(64); stop |
| 6 | 701 | 70 / 1 | 4 | 3 | trigger_event(702); stop |
| 6 | 702 | 70 / 2 | 5 | 3 | trigger_event(703); stop |
| 6 | 703 | 70 / 3 | 6 | 3 | set_switch(80); stop |
| 6 | 851 | 85 / 1 | 0 | 3 | stop |
| 6 | 901 | 90 / 1 | 3 | 3 | trigger_event(902); stop |
| 6 | 902 | 90 / 2 | 3 | 3 | set_switch(5); trigger_event(903); stop |
| 6 | 903 | 90 / 3 | 4 | 3 | trigger_event(904); stop |
| 6 | 904 | 90 / 4 | 4 | 3 | set_switch(90); set_switch(9); stop |
| 6 | 1002 | 100 / 1 | 3 | 3 | set_switch(7); stop |
| 6 | 1004 | 100 / 2 | 4 | 3 | set_switch(8); stop |
| 6 | 1101 | 110 / 1 | 3 | 3 | trigger_event(1102); stop |
| 6 | 1102 | 110 / 2 | 3 | 3 | trigger_event(1103); stop |
| 6 | 1103 | 110 / 3 | 3 | 3 | set_switch(110); set_switch(10); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
