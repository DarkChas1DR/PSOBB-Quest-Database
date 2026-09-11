# Dream Messenger — vr-ep2/q49-bb-e

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/vr-ep2/q49-bb-e.zip?download=1)**

[Original QST](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/vr-ep2/q49-bb-e.qst?download=1) · [Extracted BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/vr-ep2/q49-bb-e/q49-bb-e.qst-quest0.bin?download=1) · [Extracted DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/vr-ep2/q49-bb-e/q49-bb-e.qst-quest0.dat?download=1)

QST is the preserved original package. BIN and DAT are its decoded payload files, not reassembled scripts. The ZIP contains all three formats.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 49; language E. Static scan: **255 objects, 87 enemy/NPC records, 15 events, 912 script labels.** Script roundtrip: alignment-only.

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
| 0 | 44 | 19 | 0 |
| 16 | 211 | 68 | 15 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 16 | 31 | 3 / 1 | 6 | 0 | set_switch(190); stop |
| 16 | 71 | 7 / 1 | 6 | 0 | trigger_event(711); stop |
| 16 | 711 | 7 / 2 | 6 | 120 | set_switch(4); set_switch(5); stop |
| 16 | 91 | 9 / 1 | 6 | 60 | set_switch(120); trigger_event(911); stop |
| 16 | 911 | 9 / 2 | 3 | 0 | set_switch(121); trigger_event(912); stop |
| 16 | 912 | 9 / 3 | 4 | 0 | set_switch(6); stop |
| 16 | 111 | 11 / 1 | 6 | 0 | trigger_event(1111); stop |
| 16 | 1111 | 11 / 2 | 6 | 0 | trigger_event(1112); stop |
| 16 | 1112 | 11 / 3 | 6 | 0 | trigger_event(1113); stop |
| 16 | 1113 | 11 / 4 | 6 | 0 | set_switch(9); set_switch(10); stop |
| 16 | 81 | 8 / 1 | 1 | 160 | stop |
| 16 | 131 | 13 / 1 | 2 | 90 | set_switch(155); stop |
| 16 | 141 | 14 / 1 | 2 | 150 | stop |
| 16 | 61 | 6 / 1 | 3 | 60 | trigger_event(611); stop |
| 16 | 611 | 6 / 2 | 3 | 0 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
