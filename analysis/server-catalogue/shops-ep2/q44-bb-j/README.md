# Gallon\'s Shop -Val- — shops-ep2/q44-bb-j

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/shops-ep2/q44-bb-j.zip?download=1)**

[Original QST](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/shops-ep2/q44-bb-j.qst?download=1) · [Extracted BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/shops-ep2/q44-bb-j/q44-bb-j.qst-quest0.bin?download=1) · [Extracted DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/shops-ep2/q44-bb-j/q44-bb-j.qst-quest0.dat?download=1)

QST is the preserved original package. BIN and DAT are its decoded payload files, not reassembled scripts. The ZIP contains all three formats.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 44; language J. Static scan: **217 objects, 100 enemy/NPC records, 18 events, 528 script labels.** Script roundtrip: alignment-only.

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
| 0 | 89 | 26 | 0 |
| 5 | 128 | 74 | 18 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 5 | 21 | 2 / 1 | 2 | 1 | trigger_event(211); stop |
| 5 | 211 | 2 / 2 | 4 | 1 | trigger_event(212); stop |
| 5 | 212 | 2 / 2 | 4 | 1 | set_switch(2); stop |
| 5 | 31 | 3 / 1 | 4 | 1 | trigger_event(311); stop |
| 5 | 311 | 3 / 2 | 5 | 60 | set_switch(3); stop |
| 5 | 41 | 4 / 1 | 5 | 1 | trigger_event(411); stop |
| 5 | 411 | 4 / 2 | 5 | 60 | trigger_event(412); stop |
| 5 | 412 | 4 / 3 | 1 | 1 | set_switch(4); stop |
| 5 | 51 | 5 / 1 | 4 | 30 | trigger_event(511); stop |
| 5 | 511 | 5 / 2 | 5 | 30 | trigger_event(512); stop |
| 5 | 512 | 5 / 3 | 2 | 30 | set_switch(5); stop |
| 5 | 81 | 8 / 1 | 4 | 30 | trigger_event(811); stop |
| 5 | 811 | 8 / 2 | 7 | 30 | trigger_event(812); stop |
| 5 | 812 | 8 / 3 | 5 | 30 | set_switch(7); stop |
| 5 | 91 | 9 / 1 | 2 | 30 | trigger_event(911); stop |
| 5 | 911 | 9 / 2 | 4 | 30 | trigger_event(912); stop |
| 5 | 912 | 9 / 3 | 5 | 30 | trigger_event(913); stop |
| 5 | 913 | 9 / 4 | 5 | 30 | set_switch(8); construct_objects(room=9,group_or_wave=8); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
