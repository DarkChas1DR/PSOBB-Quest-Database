# Journalistic Pursuit — solo-story-ep1/q005-bb-e

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/solo-story-ep1/q005-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/solo-story-ep1/q005-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/solo-story-ep1/q005-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 5; language E. Static scan: **217 objects, 81 enemy/NPC records, 27 events, 44 script labels.** Script roundtrip: byte-identical.

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
0x02, 0x02, 0x00, 0x00, 0x03
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 17 | 0 |
| 1 | 98 | 27 | 16 |
| 2 | 93 | 37 | 11 |

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
| 1 | 51 | 5 / 1 | 2 | 60 | set_switch(2); stop |
| 1 | 54 | 5 / 2 | 3 | 60 | stop |
| 1 | 71 | 7 / 1 | 2 | 60 | trigger_event(711); stop |
| 1 | 711 | 7 / 2 | 2 | 60 | trigger_event(712); stop |
| 1 | 712 | 7 / 3 | 2 | 60 | set_switch(3); stop |
| 1 | 41 | 4 / 1 | 2 | 60 | trigger_event(411); stop |
| 1 | 411 | 4 / 2 | 1 | 60 | set_switch(9); stop |
| 1 | 81 | 8 / 1 | 1 | 60 | stop |
| 1 | 82 | 8 / 2 | 1 | 60 | stop |
| 2 | 11 | 1 / 1 | 4 | 1 | set_switch(1); set_switch(2); stop |
| 2 | 31 | 3 / 1 | 1 | 1 | set_switch(5); stop |
| 2 | 61 | 6 / 1 | 1 | 1 | trigger_event(611); stop |
| 2 | 611 | 6 / 2 | 4 | 30 | trigger_event(612); stop |
| 2 | 612 | 6 / 3 | 4 | 30 | trigger_event(613); stop |
| 2 | 613 | 6 / 4 | 4 | 30 | trigger_event(614); stop |
| 2 | 614 | 6 / 5 | 1 | 60 | set_switch(2); stop |
| 2 | 111 | 11 / 1 | 5 | 1 | set_switch(7); stop |
| 2 | 112 | 11 / 2 | 3 | 1 | set_switch(1); set_switch(4); set_switch(5); set_switch(6); stop |
| 2 | 151 | 15 / 1 | 4 | 1 | set_switch(7); stop |
| 2 | 152 | 15 / 2 | 6 | 30 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
