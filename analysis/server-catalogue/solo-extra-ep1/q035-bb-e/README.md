# Gallon\'s Plan — solo-extra-ep1/q035-bb-e

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/solo-extra-ep1/q035-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/solo-extra-ep1/q035-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/solo-extra-ep1/q035-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 35; language E. Static scan: **228 objects, 152 enemy/NPC records, 47 events, 162 script labels.** Script roundtrip: byte-identical.

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
0x01, 0x01, 0x00, 0x00, 0x00
0x02, 0x02, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 19 | 0 |
| 1 | 96 | 51 | 18 |
| 2 | 106 | 82 | 29 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 101 | 10 / 1 | 4 | 3 | trigger_event(102); stop |
| 1 | 102 | 10 / 2 | 2 | 3 | set_switch(6); set_switch(5); stop |
| 1 | 111 | 11 / 1 | 2 | 3 | trigger_event(112); stop |
| 1 | 112 | 11 / 2 | 3 | 3 | trigger_event(113); stop |
| 1 | 113 | 11 / 3 | 3 | 3 | set_switch(60); stop |
| 1 | 21 | 2 / 1 | 3 | 3 | trigger_event(22); stop |
| 1 | 22 | 2 / 2 | 3 | 3 | trigger_event(23); stop |
| 1 | 23 | 2 / 3 | 3 | 3 | set_switch(23); stop |
| 1 | 41 | 4 / 1 | 2 | 3 | trigger_event(42); stop |
| 1 | 42 | 4 / 2 | 3 | 3 | set_switch(9); stop |
| 1 | 51 | 5 / 1 | 2 | 3 | trigger_event(52); stop |
| 1 | 52 | 5 / 2 | 1 | 3 | trigger_event(53); stop |
| 1 | 53 | 5 / 3 | 4 | 3 | set_switch(8); set_switch(7); stop |
| 1 | 71 | 7 / 1 | 3 | 3 | trigger_event(72); stop |
| 1 | 72 | 7 / 2 | 3 | 3 | trigger_event(73); stop |
| 1 | 73 | 7 / 3 | 4 | 3 | set_switch(2); set_switch(3); stop |
| 1 | 81 | 8 / 1 | 2 | 3 | trigger_event(82); stop |
| 1 | 82 | 8 / 2 | 4 | 3 | stop |
| 2 | 101 | 10 / 1 | 3 | 3 | trigger_event(102); stop |
| 2 | 102 | 10 / 2 | 1 | 3 | trigger_event(111); stop |
| 2 | 111 | 11 / 1 | 3 | 3 | trigger_event(112); stop |
| 2 | 112 | 11 / 2 | 3 | 3 | set_switch(4); set_switch(5); set_switch(6); stop |
| 2 | 113 | 11 / 3 | 1 | 3 | trigger_event(114); stop |
| 2 | 114 | 11 / 4 | 1 | 3 | set_switch(7); stop |
| 2 | 21 | 2 / 1 | 3 | 3 | trigger_event(22); stop |
| 2 | 22 | 2 / 2 | 3 | 3 | trigger_event(23); stop |
| 2 | 23 | 2 / 3 | 4 | 3 | set_switch(63); stop |
| 2 | 11 | 1 / 1 | 3 | 3 | trigger_event(12); stop |
| 2 | 12 | 1 / 2 | 3 | 3 | set_switch(62); stop |
| 2 | 61 | 6 / 1 | 3 | 3 | trigger_event(62); stop |
| 2 | 62 | 6 / 2 | 3 | 3 | trigger_event(63); stop |
| 2 | 63 | 6 / 3 | 1 | 3 | set_switch(9); set_switch(61); stop |
| 2 | 131 | 13 / 1 | 1 | 3 | trigger_event(132); stop |
| 2 | 132 | 13 / 2 | 1 | 3 | trigger_event(133); stop |
| 2 | 133 | 13 / 3 | 4 | 3 | set_switch(8); set_switch(13); set_switch(7); stop |
| 2 | 121 | 12 / 1 | 3 | 3 | trigger_event(122); stop |
| 2 | 122 | 12 / 2 | 3 | 3 | trigger_event(123); stop |
| 2 | 123 | 12 / 3 | 3 | 3 | set_switch(10); stop |
| 2 | 81 | 8 / 1 | 0 | 3 | trigger_event(82); stop |
| 2 | 41 | 4 / 1 | 3 | 3 | trigger_event(42); stop |
| 2 | 42 | 4 / 2 | 5 | 3 | trigger_event(43); stop |
| 2 | 43 | 4 / 3 | 5 | 3 | set_switch(111); stop |
| 2 | 31 | 3 / 1 | 3 | 3 | trigger_event(32); stop |
| 2 | 32 | 3 / 2 | 4 | 3 | stop |
| 2 | 151 | 15 / 1 | 5 | 3 | trigger_event(152); stop |
| 2 | 152 | 15 / 2 | 5 | 3 | stop |
| 2 | 51 | 5 / 1 | 2 | 3 | stop |

## Review notes

- Floor 2: event 81 targets absent event 82

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
