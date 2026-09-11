# The Fake in Yellow — solo-story-ep1/q006-bb-e

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/solo-story-ep1/q006-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/solo-story-ep1/q006-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/solo-story-ep1/q006-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 6; language E. Static scan: **129 objects, 79 enemy/NPC records, 14 events, 161 script labels.** Script roundtrip: byte-identical.

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
0x01, 0x01, 0x00, 0x00, 0x04
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 27 | 24 | 0 |
| 1 | 102 | 55 | 14 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 111 | 11 / 1 | 3 | 50 | trigger_event(1111); stop |
| 1 | 1111 | 11 / 2 | 6 | 50 | trigger_event(1112); stop |
| 1 | 1112 | 11 / 3 | 4 | 50 | set_switch(5); set_switch(6); set_switch(10); stop |
| 1 | 101 | 10 / 1 | 8 | 60 | set_switch(7); set_switch(8); stop |
| 1 | 51 | 5 / 1 | 7 | 60 | trigger_event(511); stop |
| 1 | 511 | 5 / 2 | 7 | 60 | set_switch(1); stop |
| 1 | 21 | 2 / 1 | 0 | 60 | stop |
| 1 | 71 | 7 / 1 | 1 | 10 | trigger_event(711); stop |
| 1 | 711 | 7 / 2 | 1 | 10 | trigger_event(712); stop |
| 1 | 712 | 7 / 3 | 1 | 10 | trigger_event(713); stop |
| 1 | 713 | 7 / 4 | 1 | 10 | set_switch(4); stop |
| 1 | 41 | 4 / 1 | 2 | 60 | trigger_event(411); stop |
| 1 | 411 | 4 / 2 | 3 | 60 | trigger_event(412); stop |
| 1 | 412 | 4 / 3 | 3 | 60 | set_switch(3); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
