# Monster Bash 1: Encore — extermination-ep1/q122-bb-e

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/extermination-ep1/q122-bb-e.zip?download=1)**

[Original QST](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/extermination-ep1/q122-bb-e.qst?download=1) · [Extracted BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/extermination-ep1/q122-bb-e/q122-bb-e.qst-quest122.bin?download=1) · [Extracted DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/extermination-ep1/q122-bb-e/q122-bb-e.qst-quest122.dat?download=1)

QST is the preserved original package. BIN and DAT are its decoded payload files, not reassembled scripts. The ZIP contains all three formats.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 122; language E. Static scan: **141 objects, 460 enemy/NPC records, 27 events, 37 script labels.** Script roundtrip: alignment-only.

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
| 0 | 26 | 25 | 0 |
| 1 | 62 | 144 | 7 |
| 2 | 53 | 291 | 20 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 2 | 0 / 0 | 0 | 0 | set_switch(2); stop |
| 1 | 7 | 7 / 1 | 34 | 30 | trigger_event(71); stop |
| 1 | 71 | 7 / 2 | 25 | 5 | trigger_event(72); stop |
| 1 | 72 | 7 / 3 | 31 | 5 | trigger_event(73); stop |
| 1 | 73 | 7 / 4 | 17 | 5 | trigger_event(74); stop |
| 1 | 74 | 7 / 5 | 6 | 5 | trigger_event(75); stop |
| 1 | 75 | 7 / 6 | 26 | 5 | set_switch(11); stop |
| 2 | 121 | 12 / 1 | 21 | 1 | trigger_event(1211); stop |
| 2 | 1211 | 12 / 2 | 23 | 1 | trigger_event(1212); stop |
| 2 | 1212 | 12 / 3 | 28 | 30 | trigger_event(1213); stop |
| 2 | 1213 | 12 / 4 | 23 | 30 | trigger_event(1214); stop |
| 2 | 1214 | 12 / 5 | 20 | 60 | trigger_event(1215); stop |
| 2 | 1215 | 12 / 6 | 5 | 45 | trigger_event(1216); stop |
| 2 | 1216 | 12 / 7 | 13 | 45 | trigger_event(1217); stop |
| 2 | 1217 | 12 / 8 | 9 | 45 | trigger_event(1218); stop |
| 2 | 1218 | 12 / 9 | 14 | 45 | trigger_event(1219); stop |
| 2 | 1219 | 12 / 10 | 17 | 45 | trigger_event(122); stop |
| 2 | 122 | 12 / 11 | 16 | 1 | trigger_event(1221); stop |
| 2 | 1221 | 12 / 12 | 17 | 1 | trigger_event(1222); stop |
| 2 | 1222 | 12 / 13 | 22 | 30 | trigger_event(1223); stop |
| 2 | 1223 | 12 / 14 | 24 | 30 | trigger_event(1224); stop |
| 2 | 1224 | 12 / 15 | 0 | 60 | trigger_event(1225); stop |
| 2 | 1225 | 12 / 16 | 0 | 45 | trigger_event(1226); stop |
| 2 | 1226 | 12 / 17 | 0 | 45 | trigger_event(1227); stop |
| 2 | 1227 | 12 / 18 | 0 | 45 | trigger_event(1228); stop |
| 2 | 1228 | 12 / 19 | 0 | 45 | trigger_event(1229); stop |
| 2 | 1229 | 12 / 20 | 0 | 45 | set_switch(12); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
