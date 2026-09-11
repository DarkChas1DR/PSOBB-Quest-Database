# Stage5 — challenge-ep2/d88205-bb-e

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/challenge-ep2/d88205-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/challenge-ep2/d88205-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/challenge-ep2/d88205-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 65535; language E. Static scan: **453 objects, 125 enemy/NPC records, 37 events, 47 script labels.** Script roundtrip: byte-identical.

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
0x01, 0x23, 0x00, 0x00, 0x00
0x02, 0x23, 0x00, 0x01, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 40 | 12 | 0 |
| 1 | 194 | 55 | 18 |
| 2 | 219 | 58 | 19 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 11 | 1 / 1 | 6 | 1 | stop |
| 1 | 21 | 2 / 1 | 2 | 100 | trigger_event(213); stop |
| 1 | 213 | 2 / 2 | 1 | 100 | set_switch(2); stop |
| 1 | 201 | 20 / 1 | 2 | 100 | set_switch(3); stop |
| 1 | 202 | 20 / 2 | 4 | 10 | stop |
| 1 | 101 | 10 / 1 | 7 | 10 | set_switch(4); stop |
| 1 | 102 | 10 / 2 | 3 | 10 | stop |
| 1 | 31 | 3 / 1 | 2 | 10 | trigger_event(311); stop |
| 1 | 311 | 3 / 2 | 3 | 100 | set_switch(5); stop |
| 1 | 41 | 4 / 1 | 1 | 150 | set_switch(6); stop |
| 1 | 211 | 21 / 1 | 1 | 150 | set_switch(7); stop |
| 1 | 212 | 21 / 2 | 6 | 10 | stop |
| 1 | 51 | 5 / 1 | 3 | 10 | trigger_event(511); stop |
| 1 | 511 | 5 / 2 | 3 | 100 | trigger_event(512); stop |
| 1 | 512 | 5 / 3 | 2 | 100 | set_switch(8); stop |
| 1 | 221 | 22 / 1 | 2 | 200 | set_switch(9); stop |
| 1 | 222 | 22 / 2 | 6 | 10 | stop |
| 1 | 301 | 30 / 1 | 1 | 200 | construct_objects(room=30,group_or_wave=1); set_switch(1); stop |
| 2 | 11 | 1 / 1 | 1 | 300 | construct_objects(room=1,group_or_wave=1); set_switch(1); stop |
| 2 | 21 | 2 / 1 | 3 | 200 | trigger_event(2101); stop |
| 2 | 2101 | 2 / 2 | 2 | 10 | trigger_event(2102); stop |
| 2 | 2102 | 2 / 3 | 1 | 100 | set_switch(2); stop |
| 2 | 22 | 2 / 4 | 2 | 10 | stop |
| 2 | 201 | 20 / 1 | 2 | 100 | set_switch(3); stop |
| 2 | 101 | 10 / 1 | 8 | 10 | set_switch(4); stop |
| 2 | 102 | 10 / 2 | 4 | 10 | stop |
| 2 | 31 | 3 / 1 | 2 | 100 | set_switch(5); stop |
| 2 | 41 | 4 / 1 | 1 | 100 | trigger_event(411); stop |
| 2 | 411 | 4 / 2 | 2 | 100 | trigger_event(412); stop |
| 2 | 412 | 4 / 3 | 3 | 100 | set_switch(6); stop |
| 2 | 42 | 4 / 4 | 8 | 10 | stop |
| 2 | 211 | 21 / 1 | 2 | 100 | set_switch(7); stop |
| 2 | 212 | 21 / 2 | 6 | 10 | stop |
| 2 | 51 | 5 / 1 | 2 | 100 | trigger_event(511); stop |
| 2 | 511 | 5 / 2 | 4 | 100 | set_switch(8); stop |
| 2 | 221 | 22 / 1 | 4 | 10 | set_switch(9); stop |
| 2 | 222 | 22 / 2 | 1 | 10 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
