# Monster Bash 3 R — extermination-ep1/q130-bb-j

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/extermination-ep1/q130-bb-j.zip?download=1)**

[Original QST](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/extermination-ep1/q130-bb-j.qst?download=1) · [Extracted BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/extermination-ep1/q130-bb-j/q130-bb-j.qst-quest0.bin?download=1) · [Extracted DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/extermination-ep1/q130-bb-j/q130-bb-j.qst-quest0.dat?download=1)

QST is the preserved original package. BIN and DAT are its decoded payload files, not reassembled scripts. The ZIP contains all three formats.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 130; language J. Static scan: **107 objects, 281 enemy/NPC records, 18 events, 63 script labels.** Script roundtrip: alignment-only.

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
| 0 | 26 | 23 | 0 |
| 6 | 29 | 88 | 8 |
| 7 | 23 | 168 | 10 |
| 13 | 29 | 2 | 0 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 6 | 501 | 50 / 1 | 15 | 1 | trigger_event(5011); stop |
| 6 | 5011 | 50 / 2 | 14 | 15 | trigger_event(5012); stop |
| 6 | 5012 | 50 / 3 | 15 | 15 | trigger_event(5013); stop |
| 6 | 5013 | 50 / 4 | 14 | 15 | trigger_event(5014); stop |
| 6 | 5014 | 50 / 5 | 14 | 15 | trigger_event(5015); stop |
| 6 | 5015 | 50 / 6 | 16 | 15 | trigger_event(5016); stop |
| 6 | 5016 | 50 / 7 | 0 | 15 | trigger_event(5017); stop |
| 6 | 5017 | 50 / 8 | 0 | 15 | set_switch(2); set_switch(3); set_switch(235); stop |
| 7 | 5 | 0 / 0 | 0 | 0 | set_switch(206); trigger_event(611); stop |
| 7 | 611 | 61 / 1 | 38 | 1 | trigger_event(6111); stop |
| 7 | 6111 | 61 / 2 | 30 | 1 | trigger_event(6112); stop |
| 7 | 6112 | 61 / 3 | 26 | 1 | trigger_event(6113); stop |
| 7 | 6113 | 61 / 4 | 11 | 60 | trigger_event(6114); stop |
| 7 | 6114 | 61 / 5 | 12 | 60 | trigger_event(6115); stop |
| 7 | 6115 | 61 / 6 | 4 | 60 | set_switch(6); clear_switch(206); trigger_event(6116); stop |
| 7 | 6116 | 61 / 7 | 15 | 60 | trigger_event(6117); stop |
| 7 | 6117 | 61 / 8 | 18 | 60 | trigger_event(6118); stop |
| 7 | 6118 | 61 / 9 | 13 | 60 | set_switch(206); set_switch(23); set_switch(26); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
