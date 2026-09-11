# Rappy Attack — events-ep2/q134-bb-e

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/events-ep2/q134-bb-e.zip?download=1)**

[Original QST](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/events-ep2/q134-bb-e.qst?download=1) · [Extracted BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/events-ep2/q134-bb-e/q134-bb-e.qst-quest134.bin?download=1) · [Extracted DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/events-ep2/q134-bb-e/q134-bb-e.qst-quest134.dat?download=1)

QST is the preserved original package. BIN and DAT are its decoded payload files, not reassembled scripts. The ZIP contains all three formats.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 134; language E. Static scan: **127 objects, 151 enemy/NPC records, 23 events, 517 script labels.** Script roundtrip: alignment-only.

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

```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 44 | 11 | 0 |
| 1 | 83 | 140 | 23 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 101 | 10 / 1 | 4 | 1 | trigger_event(10101); stop |
| 1 | 10101 | 10 / 2 | 4 | 100 | trigger_event(10102); stop |
| 1 | 10102 | 10 / 3 | 0 | 10 | set_switch(3); set_switch(4); stop |
| 1 | 402 | 40 / 5 | 1 | 10 | stop |
| 1 | 403 | 40 / 6 | 1 | 40 | stop |
| 1 | 404 | 40 / 7 | 1 | 70 | stop |
| 1 | 401 | 40 / 1 | 1 | 130 | trigger_event(4011); stop |
| 1 | 4011 | 40 / 2 | 5 | 10 | trigger_event(4012); stop |
| 1 | 4012 | 40 / 3 | 3 | 10 | trigger_event(4013); stop |
| 1 | 4013 | 40 / 4 | 2 | 150 | set_switch(7); set_switch(8); set_switch(9); set_switch(10); set_switch(17); set_switch(18); set_switch(22); stop |
| 1 | 411 | 41 / 1 | 5 | 10 | trigger_event(4111); stop |
| 1 | 4111 | 41 / 2 | 5 | 10 | trigger_event(4112); stop |
| 1 | 4112 | 41 / 3 | 6 | 60 | trigger_event(4113); stop |
| 1 | 4113 | 41 / 4 | 5 | 100 | trigger_event(4114); stop |
| 1 | 4114 | 41 / 5 | 5 | 10 | set_switch(11); set_switch(12); stop |
| 1 | 601 | 60 / 1 | 4 | 30 | trigger_event(6011); stop |
| 1 | 6011 | 60 / 2 | 4 | 100 | trigger_event(6012); stop |
| 1 | 6012 | 60 / 3 | 0 | 10 | set_switch(23); set_switch(24); set_switch(25); set_switch(13); set_switch(14); stop |
| 1 | 602 | 60 / 4 | 0 | 100 | stop |
| 1 | 901 | 90 / 1 | 4 | 1 | set_switch(15); set_switch(16); stop |
| 1 | 911 | 91 / 1 | 3 | 1 | set_switch(5); set_switch(6); stop |
| 1 | 1011 | 101 / 1 | 1 | 1 | stop |
| 1 | 1601 | 160 / 1 | 2 | 1 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
