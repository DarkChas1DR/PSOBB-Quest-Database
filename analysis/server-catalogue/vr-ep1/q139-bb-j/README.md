# Mine Offensive v1.02 — vr-ep1/q139-bb-j

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/vr-ep1/q139-bb-j.zip?download=1)**

[Original QST](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/vr-ep1/q139-bb-j.qst?download=1) · [Extracted BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/vr-ep1/q139-bb-j/q139-bb-j.qst-quest0.bin?download=1) · [Extracted DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/vr-ep1/q139-bb-j/q139-bb-j.qst-quest0.dat?download=1)

QST is the preserved original package. BIN and DAT are its decoded payload files, not reassembled scripts. The ZIP contains all three formats.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 139; language J. Static scan: **447 objects, 188 enemy/NPC records, 38 events, 134 script labels.** Script roundtrip: alignment-only.

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
| 6 | 248 | 84 | 22 |
| 7 | 173 | 85 | 16 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 6 | 100 | 50 / 1 | 1 | 5 | trigger_event(102); stop |
| 6 | 101 | 50 / 2 | 2 | 30 | stop |
| 6 | 102 | 50 / 3 | 8 | 50 | set_switch(2); set_switch(3); trigger_event(105); stop |
| 6 | 104 | 50 / 4 | 2 | 60 | stop |
| 6 | 105 | 60 / 1 | 2 | 50 | stop |
| 6 | 106 | 60 / 2 | 5 | 40 | set_switch(5); set_switch(6); set_switch(8); stop |
| 6 | 107 | 60 / 3 | 3 | 50 | stop |
| 6 | 108 | 51 / 1 | 6 | 1 | set_switch(11); stop |
| 6 | 109 | 51 / 2 | 3 | 1 | trigger_event(110); stop |
| 6 | 110 | 51 / 3 | 3 | 1 | construct_objects(room=51,group_or_wave=1); stop |
| 6 | 111 | 75 / 1 | 6 | 50 | set_switch(12); stop |
| 6 | 112 | 75 / 2 | 3 | 1 | stop |
| 6 | 113 | 75 / 3 | 3 | 50 | stop |
| 6 | 114 | 75 / 4 | 6 | 300 | set_switch(13); stop |
| 6 | 115 | 75 / 5 | 1 | 30 | stop |
| 6 | 116 | 30 / 1 | 3 | 20 | trigger_event(118); stop |
| 6 | 117 | 60 / 4 | 2 | 1 | stop |
| 6 | 118 | 30 / 2 | 4 | 50 | construct_objects(room=30,group_or_wave=1); stop |
| 6 | 119 | 52 / 1 | 5 | 1 | set_switch(14); stop |
| 6 | 120 | 75 / 6 | 2 | 30 | stop |
| 6 | 121 | 40 / 1 | 4 | 100 | stop |
| 6 | 122 | 220 / 1 | 3 | 60 | set_switch(16); stop |
| 7 | 100 | 50 / 1 | 4 | 200 | trigger_event(101); stop |
| 7 | 101 | 50 / 2 | 5 | 1 | trigger_event(102); stop |
| 7 | 102 | 50 / 3 | 4 | 1 | construct_objects(room=50,group_or_wave=1); stop |
| 7 | 103 | 40 / 1 | 6 | 1 | trigger_event(104); stop |
| 7 | 104 | 40 / 2 | 4 | 1 | construct_objects(room=40,group_or_wave=1); stop |
| 7 | 105 | 52 / 1 | 8 | 50 | stop |
| 7 | 106 | 220 / 1 | 5 | 50 | trigger_event(107); stop |
| 7 | 107 | 220 / 2 | 4 | 60 | construct_objects(room=220,group_or_wave=1); stop |
| 7 | 108 | 80 / 1 | 7 | 20 | set_switch(62); stop |
| 7 | 109 | 30 / 1 | 3 | 1 | trigger_event(110); stop |
| 7 | 110 | 30 / 2 | 6 | 1 | construct_objects(room=30,group_or_wave=1); stop |
| 7 | 111 | 61 / 1 | 6 | 1 | trigger_event(112); stop |
| 7 | 112 | 61 / 2 | 6 | 1 | trigger_event(113); stop |
| 7 | 113 | 61 / 3 | 6 | 1 | trigger_event(114); stop |
| 7 | 114 | 61 / 4 | 2 | 1 | trigger_event(115); stop |
| 7 | 115 | 61 / 5 | 9 | 1 | set_switch(120); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
