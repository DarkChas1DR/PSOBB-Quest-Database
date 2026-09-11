# Forest Offensive v1.10 — vr-ep1/q114-bb-e

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/vr-ep1/q114-bb-e.zip?download=1)**

[Original QST](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/vr-ep1/q114-bb-e.qst?download=1) · [Extracted BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/vr-ep1/q114-bb-e/q114-bb-e.qst-quest114.bin?download=1) · [Extracted DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/vr-ep1/q114-bb-e/q114-bb-e.qst-quest114.dat?download=1)

QST is the preserved original package. BIN and DAT are its decoded payload files, not reassembled scripts. The ZIP contains all three formats.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 114; language E. Static scan: **187 objects, 122 enemy/NPC records, 28 events, 72 script labels.** Script roundtrip: alignment-only.

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
| 0 | 26 | 19 | 0 |
| 2 | 113 | 50 | 14 |
| 11 | 24 | 1 | 1 |
| 16 | 24 | 52 | 13 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 2 | 1 | 2 / 1 | 1 | 1 | trigger_event(2); stop |
| 2 | 2 | 2 / 2 | 3 | 1 | trigger_event(3); stop |
| 2 | 3 | 2 / 3 | 3 | 3 | set_switch(7); stop |
| 2 | 120 | 11 / 1 | 3 | 1 | trigger_event(121); trigger_event(122); trigger_event(123); stop |
| 2 | 121 | 11 / 2 | 2 | 20 | stop |
| 2 | 122 | 11 / 3 | 6 | 250 | trigger_event(124); stop |
| 2 | 220 | 11 / 4 | 3 | 30 | stop |
| 2 | 123 | 11 / 5 | 2 | 30 | trigger_event(125); stop |
| 2 | 124 | 11 / 6 | 3 | 40 | set_switch(8); stop |
| 2 | 330 | 15 / 1 | 5 | 1 | trigger_event(332); stop |
| 2 | 331 | 15 / 2 | 5 | 1 | stop |
| 2 | 332 | 15 / 3 | 3 | 50 | trigger_event(333); set_switch(39); set_switch(40); stop |
| 2 | 333 | 15 / 4 | 3 | 200 | stop |
| 2 | 125 | 11 / 7 | 8 | 25 | stop |
| 11 | 1 | 1 / 1 | 1 | 50 | construct_objects(room=1,group_or_wave=1); stop |
| 16 | 100 | 10 / 1 | 0 | 30 | stop |
| 16 | 110 | 11 / 1 | 0 | 30 | stop |
| 16 | 300 | 30 / 1 | 0 | 30 | stop |
| 16 | 310 | 31 / 1 | 0 | 30 | stop |
| 16 | 530 | 50 / 1 | 4 | 20 | trigger_event(533); stop |
| 16 | 531 | 50 / 2 | 0 | 30 | stop |
| 16 | 532 | 50 / 3 | 0 | 30 | stop |
| 16 | 533 | 50 / 4 | 5 | 45 | trigger_event(534); stop |
| 16 | 534 | 50 / 5 | 3 | 50 | trigger_event(535); stop |
| 16 | 535 | 50 / 6 | 4 | 50 | trigger_event(536); stop |
| 16 | 536 | 50 / 7 | 5 | 50 | trigger_event(537); stop |
| 16 | 537 | 50 / 8 | 14 | 50 | trigger_event(538); stop |
| 16 | 538 | 50 / 9 | 12 | 50 | set_switch(50); construct_objects(room=32,group_or_wave=1); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
