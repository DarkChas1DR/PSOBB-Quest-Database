# Endless Forest Brawl 1 — extermination-ep1/q140-bb-j

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/extermination-ep1/q140-bb-j.zip?download=1)**

[Original QST](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/extermination-ep1/q140-bb-j.qst?download=1) · [Extracted BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/extermination-ep1/q140-bb-j/q140-bb-j.qst-quest0.bin?download=1) · [Extracted DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/extermination-ep1/q140-bb-j/q140-bb-j.qst-quest0.dat?download=1)

QST is the preserved original package. BIN and DAT are its decoded payload files, not reassembled scripts. The ZIP contains all three formats.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 140; language J. Static scan: **208 objects, 305 enemy/NPC records, 44 events, 38 script labels.** Script roundtrip: alignment-only.

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
| 0 | 33 | 23 | 0 |
| 1 | 128 | 185 | 29 |
| 2 | 27 | 94 | 12 |
| 11 | 20 | 3 | 3 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 111 | 11 / 1 | 5 | 50 | trigger_event(1111); stop |
| 1 | 1111 | 11 / 2 | 5 | 50 | trigger_event(1112); stop |
| 1 | 1112 | 11 / 3 | 4 | 50 | trigger_event(1113); stop |
| 1 | 1113 | 11 / 4 | 6 | 50 | trigger_event(1114); stop |
| 1 | 1114 | 11 / 5 | 16 | 50 | trigger_event(1115); stop |
| 1 | 1115 | 11 / 6 | 8 | 50 | trigger_event(1116); stop |
| 1 | 1116 | 11 / 7 | 7 | 50 | trigger_event(1117); stop |
| 1 | 1117 | 11 / 6 | 8 | 50 | trigger_event(1118); stop |
| 1 | 1118 | 11 / 7 | 7 | 50 | set_switch(5); set_switch(6); stop |
| 1 | 101 | 10 / 1 | 8 | 1 | trigger_event(1011); stop |
| 1 | 1011 | 10 / 2 | 3 | 1 | trigger_event(1012); stop |
| 1 | 1012 | 10 / 3 | 19 | 1 | set_switch(7); set_switch(8); stop |
| 1 | 51 | 5 / 1 | 3 | 1 | trigger_event(511); stop |
| 1 | 511 | 5 / 2 | 5 | 1 | trigger_event(512); stop |
| 1 | 512 | 5 / 3 | 4 | 1 | trigger_event(513); stop |
| 1 | 513 | 5 / 3 | 4 | 1 | set_switch(1); stop |
| 1 | 52 | 5 / 4 | 6 | 1 | stop |
| 1 | 53 | 5 / 5 | 1 | 1 | stop |
| 1 | 22 | 2 / 1 | 0 | 1 | trigger_event(211); stop |
| 1 | 211 | 2 / 2 | 5 | 1 | trigger_event(212); stop |
| 1 | 212 | 2 / 3 | 3 | 1 | set_switch(2); stop |
| 1 | 71 | 7 / 1 | 3 | 1 | trigger_event(711); stop |
| 1 | 711 | 7 / 2 | 9 | 1 | trigger_event(7111); stop |
| 1 | 7111 | 7 / 2 | 9 | 1 | trigger_event(7112); stop |
| 1 | 7112 | 7 / 1 | 3 | 1 | trigger_event(712); stop |
| 1 | 712 | 7 / 3 | 6 | 1 | set_switch(3); stop |
| 1 | 41 | 4 / 1 | 9 | 1 | trigger_event(411); stop |
| 1 | 411 | 4 / 2 | 9 | 1 | set_switch(9); stop |
| 1 | 82 | 8 / 1 | 11 | 1 | stop |
| 2 | 41 | 4 / 1 | 8 | 1 | trigger_event(411); stop |
| 2 | 411 | 4 / 2 | 4 | 1 | trigger_event(412); stop |
| 2 | 412 | 4 / 3 | 7 | 1 | set_switch(90); stop |
| 2 | 42 | 4 / 4 | 0 | 300 | set_switch(90); stop |
| 2 | 121 | 12 / 1 | 9 | 100 | trigger_event(1211); stop |
| 2 | 1211 | 12 / 2 | 6 | 30 | trigger_event(12111); stop |
| 2 | 12111 | 12 / 2 | 6 | 30 | trigger_event(12112); stop |
| 2 | 12112 | 12 / 2 | 6 | 30 | trigger_event(12113); stop |
| 2 | 12113 | 12 / 2 | 6 | 30 | trigger_event(1212); stop |
| 2 | 1212 | 12 / 4 | 5 | 30 | trigger_event(12121); stop |
| 2 | 12121 | 12 / 5 | 9 | 30 | set_switch(10); stop |
| 2 | 122 | 12 / 4 | 5 | 1 | set_switch(10); stop |
| 11 | 1 | 1 / 1 | 1 | 0 | trigger_event(2); stop |
| 11 | 2 | 1 / 2 | 1 | 600 | trigger_event(3); stop |
| 11 | 3 | 1 / 3 | 1 | 600 | construct_objects(room=1,group_or_wave=1); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
