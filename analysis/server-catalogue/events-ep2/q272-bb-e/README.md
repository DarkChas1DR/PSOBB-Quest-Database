# Weather Effects — events-ep2/q272-bb-e

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/events-ep2/q272-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/events-ep2/q272-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/events-ep2/q272-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 272; language E. Static scan: **382 objects, 119 enemy/NPC records, 31 events, 203 script labels.** Script roundtrip: differs.

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
| 0 | 71 | 21 | 0 |
| 5 | 78 | 43 | 9 |
| 17 | 233 | 55 | 22 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 5 | 21 | 2 / 1 | 6 | 10 | trigger_event(211); stop |
| 5 | 211 | 2 / 2 | 5 | 60 | set_switch(2); stop |
| 5 | 31 | 3 / 1 | 3 | 1 | trigger_event(311); stop |
| 5 | 311 | 3 / 2 | 5 | 10 | set_switch(3); stop |
| 5 | 41 | 4 / 1 | 5 | 1 | set_switch(4); stop |
| 5 | 51 | 5 / 1 | 4 | 10 | stop |
| 5 | 81 | 8 / 1 | 5 | 10 | construct_objects(room=8,group_or_wave=1); stop |
| 5 | 91 | 9 / 1 | 5 | 1 | set_switch(8); stop |
| 5 | 101 | 10 / 1 | 5 | 45 | set_switch(7); stop |
| 17 | 11 | 1 / 1 | 1 | 180 | set_switch(1); stop |
| 17 | 21 | 2 / 1 | 4 | 10 | set_switch(2); stop |
| 17 | 31 | 3 / 1 | 2 | 10 | trigger_event(311); stop |
| 17 | 311 | 3 / 2 | 3 | 120 | set_switch(5); stop |
| 17 | 41 | 4 / 1 | 3 | 10 | trigger_event(411); stop |
| 17 | 411 | 4 / 2 | 4 | 42 | set_switch(6); stop |
| 17 | 51 | 5 / 1 | 5 | 10 | set_switch(8); stop |
| 17 | 101 | 10 / 1 | 5 | 10 | set_switch(4); stop |
| 17 | 201 | 20 / 1 | 5 | 10 | set_switch(3); stop |
| 17 | 2011 | 20 / 5 | 0 | 10 | stop |
| 17 | 202 | 20 / 2 | 0 | 10 | trigger_event(2021); stop |
| 17 | 2021 | 20 / 6 | 0 | 10 | stop |
| 17 | 203 | 20 / 3 | 0 | 10 | stop |
| 17 | 204 | 20 / 4 | 0 | 10 | trigger_event(2041); stop |
| 17 | 2041 | 20 / 7 | 0 | 10 | set_switch(3); stop |
| 17 | 211 | 21 / 1 | 4 | 10 | trigger_event(2111); stop |
| 17 | 2111 | 21 / 2 | 2 | 90 | set_switch(7); stop |
| 17 | 221 | 22 / 1 | 6 | 10 | trigger_event(2211); stop |
| 17 | 2211 | 22 / 2 | 3 | 10 | trigger_event(2212); stop |
| 17 | 2212 | 22 / 3 | 3 | 10 | trigger_event(2213); stop |
| 17 | 2213 | 22 / 4 | 3 | 240 | set_switch(9); stop |
| 17 | 301 | 30 / 1 | 2 | 10 | set_switch(10); stop |

## Review notes

- Reassembled bytes differ beyond recognized alignment; inspect before rebuilding

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
