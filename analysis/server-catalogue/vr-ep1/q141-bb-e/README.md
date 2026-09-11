# Labyrinthine Trial — vr-ep1/q141-bb-e

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/vr-ep1/q141-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/vr-ep1/q141-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/vr-ep1/q141-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 141; language E. Static scan: **230 objects, 134 enemy/NPC records, 20 events, 379 script labels.** Script roundtrip: byte-identical.

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
0x00, 0x00, 0x00, 0x00, 0x00
0x03, 0x03, 0x00, 0x05, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 27 | 21 | 0 |
| 3 | 203 | 113 | 20 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 3 | 101 | 10 / 1 | 5 | 30 | set_switch(6); stop |
| 3 | 111 | 11 / 1 | 5 | 30 | set_switch(27); stop |
| 3 | 121 | 12 / 1 | 4 | 30 | set_switch(21); set_switch(22); stop |
| 3 | 131 | 13 / 1 | 3 | 30 | set_switch(33); set_switch(34); set_switch(135); stop |
| 3 | 141 | 14 / 1 | 5 | 30 | set_switch(49); stop |
| 3 | 151 | 15 / 1 | 5 | 30 | set_switch(45); set_switch(46); stop |
| 3 | 301 | 30 / 1 | 5 | 30 | set_switch(11); stop |
| 3 | 311 | 31 / 1 | 6 | 30 | set_switch(17); stop |
| 3 | 321 | 32 / 1 | 5 | 30 | set_switch(25); set_switch(26); stop |
| 3 | 331 | 33 / 1 | 5 | 30 | set_switch(36); stop |
| 3 | 341 | 34 / 1 | 5 | 30 | set_switch(43); stop |
| 3 | 501 | 50 / 1 | 8 | 30 | trigger_event(5011); stop |
| 3 | 5011 | 50 / 2 | 6 | 120 | trigger_event(5012); stop |
| 3 | 5012 | 50 / 3 | 5 | 90 | set_switch(12); set_switch(136); stop |
| 3 | 511 | 51 / 1 | 9 | 30 | trigger_event(5111); stop |
| 3 | 5111 | 51 / 2 | 8 | 120 | trigger_event(5112); stop |
| 3 | 5112 | 51 / 3 | 6 | 90 | trigger_event(5113); stop |
| 3 | 5113 | 51 / 4 | 4 | 240 | set_switch(50); stop |
| 3 | 521 | 52 / 1 | 7 | 30 | trigger_event(5211); stop |
| 3 | 5211 | 52 / 2 | 7 | 120 | set_switch(1); set_switch(134); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
