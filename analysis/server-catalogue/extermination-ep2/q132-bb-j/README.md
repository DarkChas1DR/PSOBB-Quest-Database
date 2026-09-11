# Monster Bash 6 — extermination-ep2/q132-bb-j

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/extermination-ep2/q132-bb-j.zip?download=1)**

[Original QST](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/extermination-ep2/q132-bb-j.qst?download=1) · [Extracted BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/extermination-ep2/q132-bb-j/q132-bb-j.qst-quest0.bin?download=1) · [Extracted DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/extermination-ep2/q132-bb-j/q132-bb-j.qst-quest0.dat?download=1)

QST is the preserved original package. BIN and DAT are its decoded payload files, not reassembled scripts. The ZIP contains all three formats.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 132; language J. Static scan: **82 objects, 194 enemy/NPC records, 14 events, 103 script labels.** Script roundtrip: alignment-only.

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
| 0 | 53 | 18 | 0 |
| 3 | 23 | 175 | 13 |
| 15 | 6 | 1 | 1 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 3 | 8 | 0 / 0 | 0 | 0 | set_switch(8); trigger_event(41); stop |
| 3 | 41 | 41 / 1 | 29 | 5 | trigger_event(411); stop |
| 3 | 411 | 41 / 2 | 10 | 5 | trigger_event(412); stop |
| 3 | 412 | 41 / 3 | 17 | 5 | set_switch(41); stop |
| 3 | 51 | 51 / 1 | 24 | 5 | trigger_event(511); stop |
| 3 | 511 | 51 / 2 | 12 | 5 | trigger_event(512); stop |
| 3 | 512 | 51 / 3 | 5 | 5 | trigger_event(513); stop |
| 3 | 513 | 51 / 4 | 18 | 5 | trigger_event(515); stop |
| 3 | 515 | 51 / 5 | 12 | 5 | trigger_event(516); stop |
| 3 | 516 | 51 / 6 | 9 | 5 | trigger_event(517); stop |
| 3 | 517 | 51 / 7 | 10 | 5 | trigger_event(518); stop |
| 3 | 518 | 51 / 8 | 6 | 5 | trigger_event(519); stop |
| 3 | 519 | 51 / 9 | 11 | 5 | set_switch(51); set_switch(1); stop |
| 15 | 1 | 1 / 1 | 1 | 50 | construct_objects(room=1,group_or_wave=1); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
