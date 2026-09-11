# Requiem — tower-ep2/q75-bb-j

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/tower-ep2/q75-bb-j.zip?download=1)**

[Original QST](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/tower-ep2/q75-bb-j.qst?download=1) · [Extracted BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/tower-ep2/q75-bb-j/q75-bb-j.qst-quest0.bin?download=1) · [Extracted DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/tower-ep2/q75-bb-j/q75-bb-j.qst-quest0.dat?download=1)

QST is the preserved original package. BIN and DAT are its decoded payload files, not reassembled scripts. The ZIP contains all three formats.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 75; language J. Static scan: **254 objects, 81 enemy/NPC records, 22 events, 517 script labels.** Script roundtrip: alignment-only.

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
| 0 | 41 | 22 | 0 |
| 1 | 4 | 0 | 0 |
| 3 | 12 | 0 | 0 |
| 9 | 8 | 0 | 0 |
| 11 | 101 | 0 | 0 |
| 12 | 22 | 1 | 1 |
| 13 | 6 | 1 | 1 |
| 14 | 30 | 1 | 1 |
| 15 | 30 | 1 | 1 |
| 17 | 0 | 55 | 18 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 12 | 1 | 1 / 1 | 1 | 50 | construct_objects(room=1,group_or_wave=1); stop |
| 13 | 1 | 0 / 1 | 1 | 0 | construct_objects(room=1,group_or_wave=1); stop |
| 14 | 1 | 1 / 1 | 1 | 50 | construct_objects(room=1,group_or_wave=1); stop |
| 15 | 1 | 1 / 1 | 1 | 50 | construct_objects(room=1,group_or_wave=1); stop |
| 17 | 11 | 1 / 1 | 6 | 1 | stop |
| 17 | 21 | 2 / 1 | 2 | 100 | trigger_event(213); stop |
| 17 | 213 | 2 / 2 | 1 | 100 | set_switch(2); stop |
| 17 | 201 | 20 / 1 | 2 | 100 | set_switch(3); stop |
| 17 | 202 | 20 / 2 | 4 | 10 | stop |
| 17 | 101 | 10 / 1 | 7 | 10 | set_switch(4); stop |
| 17 | 102 | 10 / 2 | 3 | 10 | stop |
| 17 | 31 | 3 / 1 | 2 | 10 | trigger_event(311); stop |
| 17 | 311 | 3 / 2 | 3 | 100 | set_switch(5); stop |
| 17 | 41 | 4 / 1 | 1 | 150 | set_switch(6); stop |
| 17 | 211 | 21 / 1 | 1 | 150 | set_switch(7); stop |
| 17 | 212 | 21 / 2 | 6 | 10 | stop |
| 17 | 51 | 5 / 1 | 3 | 10 | trigger_event(511); stop |
| 17 | 511 | 5 / 2 | 3 | 100 | trigger_event(512); stop |
| 17 | 512 | 5 / 3 | 2 | 100 | set_switch(8); stop |
| 17 | 221 | 22 / 1 | 2 | 200 | set_switch(9); stop |
| 17 | 222 | 22 / 2 | 6 | 10 | stop |
| 17 | 301 | 30 / 1 | 1 | 200 | set_switch(1); construct_objects(room=30,group_or_wave=1); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
