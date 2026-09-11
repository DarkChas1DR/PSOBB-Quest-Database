# ９－４：追跡 — government-ep4/q704-bb-j

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/government-ep4/q704-bb-j.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep4/q704-bb-j.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep4/q704-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode4; header quest ID 704; language J. Static scan: **283 objects, 279 enemy/NPC records, 44 events, 296 script labels.** Script roundtrip: byte-identical.

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
0x00, 0x2D, 0x00, 0x00, 0x00
0x04, 0x27, 0x00, 0x00, 0x00
0x05, 0x28, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 27 | 20 | 0 |
| 4 | 142 | 111 | 21 |
| 5 | 114 | 148 | 23 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 4 | 811 | 81 / 1 | 1 | 30 | set_switch(81); stop |
| 4 | 221 | 22 / 1 | 5 | 30 | trigger_event(2211); stop |
| 4 | 2211 | 22 / 2 | 5 | 60 | trigger_event(2212); stop |
| 4 | 2212 | 22 / 3 | 5 | 30 | trigger_event(2213); stop |
| 4 | 2213 | 22 / 4 | 4 | 60 | set_switch(1); stop |
| 4 | 222 | 22 / 5 | 6 | 30 | trigger_event(2221); stop |
| 4 | 2221 | 22 / 6 | 5 | 60 | trigger_event(2222); stop |
| 4 | 2222 | 22 / 7 | 6 | 30 | set_switch(22); set_switch(2); stop |
| 4 | 601 | 60 / 1 | 5 | 30 | trigger_event(6011); stop |
| 4 | 6011 | 60 / 2 | 5 | 30 | trigger_event(6012); stop |
| 4 | 6012 | 60 / 3 | 7 | 90 | trigger_event(6013); stop |
| 4 | 6013 | 60 / 4 | 5 | 30 | trigger_event(6014); stop |
| 4 | 6014 | 60 / 5 | 5 | 60 | trigger_event(6015); stop |
| 4 | 6015 | 60 / 6 | 6 | 30 | trigger_event(6016); stop |
| 4 | 6016 | 60 / 7 | 6 | 90 | set_switch(60); set_switch(6); set_switch(8); stop |
| 4 | 411 | 41 / 1 | 5 | 30 | trigger_event(4111); stop |
| 4 | 4111 | 41 / 2 | 5 | 60 | trigger_event(4112); stop |
| 4 | 4112 | 41 / 3 | 6 | 30 | set_switch(3); set_switch(4); stop |
| 4 | 412 | 41 / 4 | 5 | 30 | trigger_event(4121); stop |
| 4 | 4121 | 41 / 5 | 6 | 60 | trigger_event(4122); stop |
| 4 | 4122 | 41 / 6 | 4 | 30 | set_switch(41); set_switch(5); stop |
| 5 | 101 | 10 / 1 | 6 | 30 | trigger_event(1011); stop |
| 5 | 1011 | 10 / 2 | 6 | 60 | trigger_event(1012); stop |
| 5 | 1012 | 10 / 3 | 5 | 30 | set_switch(10); set_switch(21); stop |
| 5 | 201 | 20 / 1 | 7 | 30 | trigger_event(2011); stop |
| 5 | 2011 | 20 / 2 | 7 | 60 | trigger_event(2012); stop |
| 5 | 2012 | 20 / 3 | 7 | 30 | set_switch(20); set_switch(31); stop |
| 5 | 301 | 30 / 1 | 6 | 30 | trigger_event(3011); stop |
| 5 | 3011 | 30 / 2 | 6 | 60 | trigger_event(3012); stop |
| 5 | 3012 | 30 / 3 | 7 | 60 | trigger_event(3013); stop |
| 5 | 3013 | 30 / 4 | 6 | 30 | set_switch(30); set_switch(41); stop |
| 5 | 401 | 40 / 1 | 6 | 30 | trigger_event(4011); stop |
| 5 | 4011 | 40 / 2 | 6 | 60 | trigger_event(4012); stop |
| 5 | 4012 | 40 / 3 | 7 | 30 | set_switch(40); set_switch(51); stop |
| 5 | 501 | 50 / 1 | 5 | 30 | trigger_event(5011); stop |
| 5 | 5011 | 50 / 2 | 5 | 60 | trigger_event(5012); stop |
| 5 | 5012 | 50 / 3 | 6 | 60 | trigger_event(5013); stop |
| 5 | 5013 | 50 / 4 | 5 | 30 | set_switch(50); set_switch(61); stop |
| 5 | 601 | 60 / 1 | 5 | 30 | trigger_event(6011); stop |
| 5 | 6011 | 60 / 2 | 7 | 60 | trigger_event(6012); stop |
| 5 | 6012 | 60 / 3 | 5 | 60 | trigger_event(6013); stop |
| 5 | 6013 | 60 / 4 | 5 | 30 | trigger_event(6014); stop |
| 5 | 6014 | 60 / 5 | 5 | 30 | trigger_event(6015); stop |
| 5 | 6015 | 60 / 6 | 0 | 30 | set_switch(60); set_switch(11); set_switch(62); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
