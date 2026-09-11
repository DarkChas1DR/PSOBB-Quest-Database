# The Lost Bride — solo-story-ep1/q011-bb-e

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/solo-story-ep1/q011-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/solo-story-ep1/q011-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/solo-story-ep1/q011-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 11; language E. Static scan: **337 objects, 93 enemy/NPC records, 39 events, 42 script labels.** Script roundtrip: byte-identical.

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
0x03, 0x03, 0x00, 0x01, 0x01
0x04, 0x04, 0x00, 0x01, 0x01
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 18 | 0 |
| 3 | 148 | 42 | 19 |
| 4 | 163 | 33 | 20 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 3 | 111 | 11 / 1 | 2 | 40 | set_switch(29); set_switch(27); stop |
| 3 | 341 | 34 / 1 | 2 | 40 | trigger_event(3411); stop |
| 3 | 3411 | 34 / 2 | 2 | 40 | set_switch(28); set_switch(31); set_switch(26); stop |
| 3 | 331 | 33 / 1 | 2 | 40 | set_switch(32); set_switch(33); stop |
| 3 | 332 | 33 / 2 | 2 | 40 | stop |
| 3 | 521 | 52 / 1 | 3 | 40 | trigger_event(5211); stop |
| 3 | 5211 | 52 / 2 | 3 | 40 | set_switch(19); set_switch(18); set_switch(20); set_switch(23); set_switch(24); set_switch(25); set_switch(21); set_switch(22); stop |
| 3 | 321 | 32 / 1 | 1 | 40 | trigger_event(3211); stop |
| 3 | 3211 | 32 / 2 | 2 | 40 | stop |
| 3 | 601 | 60 / 1 | 2 | 40 | trigger_event(6011); stop |
| 3 | 6011 | 60 / 2 | 2 | 40 | set_switch(16); set_switch(17); stop |
| 3 | 501 | 50 / 1 | 1 | 40 | set_switch(14); set_switch(15); set_switch(9); stop |
| 3 | 311 | 311 / 1 | 0 | 40 | set_switch(2); set_switch(4); set_switch(5); set_switch(6); set_switch(8); set_switch(10); set_switch(13); stop |
| 3 | 101 | 10 / 1 | 2 | 40 | stop |
| 3 | 511 | 51 / 1 | 2 | 40 | trigger_event(5111); stop |
| 3 | 5111 | 51 / 2 | 4 | 40 | trigger_event(5112); stop |
| 3 | 5112 | 51 / 3 | 3 | 40 | set_switch(1); set_switch(3); set_switch(7); stop |
| 3 | 301 | 30 / 1 | 2 | 40 | trigger_event(3011); stop |
| 3 | 3011 | 30 / 2 | 2 | 40 | set_switch(11); set_switch(12); stop |
| 4 | 351 | 35 / 1 | 2 | 30 | set_switch(28); set_switch(29); stop |
| 4 | 352 | 35 / 2 | 2 | 30 | stop |
| 4 | 301 | 30 / 1 | 2 | 30 | trigger_event(3011); stop |
| 4 | 3011 | 30 / 2 | 3 | 30 | set_switch(26); set_switch(27); set_switch(24); set_switch(33); set_switch(32); set_switch(31); stop |
| 4 | 401 | 40 / 1 | 0 | 30 | trigger_event(4011); stop |
| 4 | 4011 | 40 / 2 | 0 | 30 | set_switch(20); set_switch(23); set_switch(25); set_switch(22); set_switch(21); set_switch(20); set_switch(17); set_switch(18); stop |
| 4 | 141 | 14 / 1 | 2 | 30 | stop |
| 4 | 451 | 45 / 1 | 2 | 30 | set_switch(19); stop |
| 4 | 452 | 45 / 2 | 2 | 30 | stop |
| 4 | 101 | 10 / 1 | 2 | 30 | trigger_event(1011); stop |
| 4 | 1011 | 10 / 2 | 2 | 30 | set_switch(11); stop |
| 4 | 211 | 20 / 1 | 1 | 30 | trigger_event(2111); stop |
| 4 | 2111 | 20 / 2 | 1 | 30 | trigger_event(2112); stop |
| 4 | 2112 | 20 / 3 | 1 | 30 | set_switch(9); set_switch(10); set_switch(3); set_switch(12); stop |
| 4 | 131 | 13 / 1 | 1 | 30 | set_switch(13); set_switch(1); stop |
| 4 | 221 | 22 / 1 | 3 | 30 | trigger_event(2211); stop |
| 4 | 2211 | 22 / 2 | 0 | 30 | set_switch(2); stop |
| 4 | 111 | 11 / 1 | 2 | 30 | trigger_event(1111); stop |
| 4 | 1111 | 11 / 2 | 2 | 30 | set_switch(4); set_switch(5); stop |
| 4 | 121 | 12 / 1 | 3 | 30 | set_switch(6); set_switch(7); set_switch(8); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
