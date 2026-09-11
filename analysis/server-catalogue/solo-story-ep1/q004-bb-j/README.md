# 戦いのいしずえ — solo-story-ep1/q004-bb-j

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/solo-story-ep1/q004-bb-j.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/solo-story-ep1/q004-bb-j.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/solo-story-ep1/q004-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 4; language J. Static scan: **117 objects, 53 enemy/NPC records, 19 events, 76 script labels.** Script roundtrip: byte-identical.

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
0x01, 0x01, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 18 | 0 |
| 1 | 91 | 35 | 19 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 111 | 11 / 1 | 2 | 50 | trigger_event(1111); stop |
| 1 | 1111 | 11 / 2 | 2 | 50 | trigger_event(1112); stop |
| 1 | 1112 | 11 / 3 | 2 | 50 | trigger_event(1113); stop |
| 1 | 1113 | 11 / 4 | 2 | 50 | set_switch(5); set_switch(6); stop |
| 1 | 101 | 10 / 1 | 1 | 60 | trigger_event(1011); stop |
| 1 | 1011 | 10 / 2 | 1 | 60 | trigger_event(1012); stop |
| 1 | 1012 | 10 / 3 | 1 | 60 | set_switch(7); set_switch(8); stop |
| 1 | 51 | 5 / 1 | 1 | 60 | trigger_event(511); stop |
| 1 | 511 | 5 / 2 | 2 | 60 | trigger_event(512); stop |
| 1 | 512 | 5 / 3 | 1 | 60 | set_switch(1); stop |
| 1 | 21 | 2 / 1 | 1 | 60 | trigger_event(211); stop |
| 1 | 211 | 2 / 2 | 2 | 60 | trigger_event(212); stop |
| 1 | 212 | 2 / 3 | 4 | 60 | set_switch(2); stop |
| 1 | 71 | 7 / 1 | 2 | 60 | trigger_event(711); stop |
| 1 | 711 | 7 / 2 | 2 | 60 | trigger_event(712); stop |
| 1 | 712 | 7 / 3 | 2 | 60 | set_switch(3); stop |
| 1 | 41 | 4 / 1 | 2 | 60 | trigger_event(411); stop |
| 1 | 411 | 4 / 2 | 1 | 60 | set_switch(9); stop |
| 1 | 84 | 8 / 1 | 4 | 60 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
