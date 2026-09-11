# 6-1:Test/Spaceship 1 — government-ep2/q456-bb-e

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/government-ep2/q456-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep2/q456-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep2/q456-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 456; language E. Static scan: **264 objects, 152 enemy/NPC records, 33 events, 80 script labels.** Script roundtrip: byte-identical.

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
0x00, 0x12, 0x00, 0x00, 0x00
0x03, 0x15, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 53 | 18 | 0 |
| 3 | 211 | 134 | 33 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 3 | 111 | 11 / 1 | 1 | 1 | trigger_event(1111); stop |
| 3 | 1111 | 11 / 2 | 4 | 60 | trigger_event(1112); stop |
| 3 | 1112 | 11 / 3 | 6 | 200 | set_switch(6); set_switch(7); stop |
| 3 | 201 | 20 / 1 | 1 | 1 | trigger_event(2011); stop |
| 3 | 2011 | 20 / 2 | 6 | 1 | trigger_event(2012); stop |
| 3 | 2012 | 20 / 3 | 2 | 1 | set_switch(34); stop |
| 3 | 211 | 21 / 1 | 3 | 1 | trigger_event(2111); stop |
| 3 | 2111 | 21 / 2 | 3 | 1 | set_switch(5); stop |
| 3 | 301 | 30 / 1 | 4 | 10 | trigger_event(3011); stop |
| 3 | 3011 | 30 / 2 | 5 | 10 | set_switch(10); set_switch(11); set_switch(20); set_switch(21); stop |
| 3 | 321 | 32 / 1 | 5 | 150 | trigger_event(3211); stop |
| 3 | 3211 | 32 / 2 | 3 | 10 | set_switch(31); set_switch(32); stop |
| 3 | 401 | 40 / 1 | 6 | 1 | trigger_event(4011); stop |
| 3 | 4011 | 40 / 2 | 6 | 1 | trigger_event(4012); stop |
| 3 | 4012 | 40 / 3 | 2 | 1 | trigger_event(4013); stop |
| 3 | 4013 | 40 / 4 | 6 | 1 | set_switch(10); set_switch(11); set_switch(12); set_switch(13); stop |
| 3 | 421 | 42 / 1 | 5 | 60 | trigger_event(4211); stop |
| 3 | 4211 | 42 / 2 | 6 | 1 | trigger_event(4212); stop |
| 3 | 4212 | 42 / 3 | 2 | 1 | set_switch(29); set_switch(30); set_switch(33); stop |
| 3 | 501 | 50 / 1 | 4 | 10 | trigger_event(5011); stop |
| 3 | 5011 | 50 / 2 | 6 | 10 | set_switch(14); set_switch(15); set_switch(16); set_switch(17); set_switch(18); set_switch(19); stop |
| 3 | 511 | 51 / 1 | 5 | 1 | trigger_event(5111); stop |
| 3 | 5111 | 51 / 2 | 6 | 1 | trigger_event(5112); stop |
| 3 | 5112 | 51 / 3 | 5 | 200 | set_switch(14); set_switch(17); set_switch(18); set_switch(19); set_switch(20); set_switch(21); set_switch(22); set_switch(23); set_switch(24); set_switch(25); set_switch(26); set_switch(27); set_switch(28); stop |
| 3 | 521 | 52 / 1 | 3 | 1 | trigger_event(5211); stop |
| 3 | 5211 | 52 / 2 | 6 | 1 | trigger_event(5212); stop |
| 3 | 5212 | 52 / 3 | 5 | 150 | trigger_event(5213); stop |
| 3 | 5213 | 52 / 4 | 4 | 90 | trigger_event(5214); stop |
| 3 | 5214 | 52 / 5 | 7 | 180 | stop |
| 3 | 522 | 52 / 6 | 2 | 60 | trigger_event(5221); stop |
| 3 | 5221 | 52 / 7 | 2 | 60 | trigger_event(5222); stop |
| 3 | 5222 | 52 / 8 | 2 | 60 | stop |
| 3 | 1601 | 160 / 1 | 1 | 1 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
