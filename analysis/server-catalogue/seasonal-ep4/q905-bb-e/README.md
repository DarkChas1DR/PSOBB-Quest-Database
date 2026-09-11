# Christmas Fiasco — seasonal-ep4/q905-bb-e

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/seasonal-ep4/q905-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/seasonal-ep4/q905-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/seasonal-ep4/q905-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode4; header quest ID 905; language E. Static scan: **143 objects, 602 enemy/NPC records, 90 events, 82 script labels.** Script roundtrip: byte-identical.

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
0x01, 0x24, 0x00, 0x00, 0x00
0x07, 0x2A, 0x00, 0x00, 0x00
0x08, 0x2B, 0x00, 0x02, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 15 | 0 |
| 1 | 51 | 184 | 28 |
| 7 | 20 | 201 | 32 |
| 8 | 46 | 202 | 30 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 101 | 10 / 1 | 4 | 0 | trigger_event(102); stop |
| 1 | 102 | 10 / 2 | 3 | 0 | trigger_event(103); stop |
| 1 | 103 | 10 / 3 | 6 | 0 | trigger_event(104); stop |
| 1 | 104 | 10 / 4 | 7 | 0 | trigger_event(105); stop |
| 1 | 105 | 10 / 5 | 7 | 0 | trigger_event(106); stop |
| 1 | 106 | 10 / 6 | 7 | 0 | trigger_event(107); stop |
| 1 | 107 | 10 / 7 | 12 | 0 | trigger_event(108); stop |
| 1 | 108 | 10 / 8 | 5 | 0 | trigger_event(109); stop |
| 1 | 109 | 10 / 9 | 4 | 0 | trigger_event(110); stop |
| 1 | 110 | 10 / 10 | 4 | 0 | set_switch(1); stop |
| 1 | 201 | 30 / 1 | 5 | 0 | trigger_event(202); stop |
| 1 | 202 | 30 / 2 | 7 | 0 | trigger_event(203); stop |
| 1 | 203 | 30 / 3 | 6 | 0 | trigger_event(204); stop |
| 1 | 204 | 30 / 4 | 10 | 0 | trigger_event(205); stop |
| 1 | 205 | 30 / 5 | 4 | 0 | trigger_event(206); stop |
| 1 | 206 | 30 / 6 | 9 | 0 | trigger_event(207); stop |
| 1 | 207 | 30 / 7 | 5 | 0 | trigger_event(208); stop |
| 1 | 208 | 30 / 8 | 4 | 0 | set_switch(2); stop |
| 1 | 301 | 60 / 1 | 5 | 0 | trigger_event(302); stop |
| 1 | 302 | 60 / 2 | 5 | 0 | trigger_event(303); stop |
| 1 | 303 | 60 / 3 | 6 | 0 | trigger_event(304); stop |
| 1 | 304 | 60 / 4 | 9 | 0 | trigger_event(305); stop |
| 1 | 305 | 60 / 5 | 12 | 0 | trigger_event(306); stop |
| 1 | 306 | 60 / 6 | 9 | 0 | trigger_event(307); stop |
| 1 | 307 | 60 / 7 | 8 | 0 | trigger_event(308); stop |
| 1 | 308 | 60 / 8 | 7 | 0 | trigger_event(309); stop |
| 1 | 309 | 60 / 9 | 8 | 0 | trigger_event(310); stop |
| 1 | 310 | 60 / 10 | 6 | 0 | set_switch(3); stop |
| 7 | 101 | 40 / 1 | 4 | 0 | trigger_event(102); stop |
| 7 | 102 | 40 / 2 | 7 | 0 | trigger_event(103); stop |
| 7 | 103 | 40 / 3 | 2 | 0 | trigger_event(104); stop |
| 7 | 104 | 40 / 4 | 7 | 0 | trigger_event(105); stop |
| 7 | 105 | 40 / 5 | 6 | 0 | trigger_event(106); stop |
| 7 | 106 | 40 / 6 | 4 | 0 | trigger_event(107); stop |
| 7 | 107 | 40 / 7 | 5 | 0 | trigger_event(108); stop |
| 7 | 108 | 40 / 8 | 8 | 0 | trigger_event(109); stop |
| 7 | 109 | 40 / 9 | 8 | 0 | trigger_event(110); stop |
| 7 | 110 | 40 / 10 | 4 | 0 | trigger_event(111); stop |
| 7 | 111 | 40 / 11 | 8 | 0 | trigger_event(112); stop |
| 7 | 112 | 40 / 12 | 2 | 0 | set_switch(1); stop |
| 7 | 201 | 20 / 1 | 3 | 0 | trigger_event(202); stop |
| 7 | 202 | 20 / 2 | 5 | 0 | trigger_event(203); stop |
| 7 | 203 | 20 / 3 | 9 | 0 | trigger_event(204); stop |
| 7 | 204 | 20 / 4 | 8 | 0 | trigger_event(205); stop |
| 7 | 205 | 20 / 5 | 7 | 0 | trigger_event(206); stop |
| 7 | 206 | 20 / 6 | 8 | 0 | trigger_event(207); stop |
| 7 | 207 | 20 / 7 | 4 | 0 | trigger_event(208); stop |
| 7 | 208 | 20 / 8 | 7 | 0 | trigger_event(209); stop |
| 7 | 209 | 20 / 9 | 11 | 0 | trigger_event(210); stop |
| 7 | 210 | 20 / 10 | 4 | 0 | set_switch(2); stop |
| 7 | 301 | 42 / 1 | 1 | 0 | trigger_event(302); stop |
| 7 | 302 | 42 / 2 | 9 | 0 | trigger_event(303); stop |
| 7 | 303 | 42 / 3 | 10 | 0 | trigger_event(304); stop |
| 7 | 304 | 42 / 4 | 9 | 0 | trigger_event(305); stop |
| 7 | 305 | 42 / 5 | 9 | 0 | trigger_event(306); stop |
| 7 | 306 | 42 / 6 | 4 | 0 | trigger_event(307); stop |
| 7 | 307 | 42 / 7 | 10 | 0 | trigger_event(308); stop |
| 7 | 308 | 42 / 8 | 3 | 0 | trigger_event(309); stop |
| 7 | 309 | 42 / 9 | 13 | 0 | trigger_event(310); stop |
| 7 | 310 | 42 / 10 | 2 | 0 | set_switch(3); stop |
| 8 | 101 | 40 / 1 | 4 | 0 | trigger_event(102); stop |
| 8 | 102 | 40 / 2 | 9 | 0 | trigger_event(103); stop |
| 8 | 103 | 40 / 3 | 6 | 0 | trigger_event(104); stop |
| 8 | 104 | 40 / 4 | 6 | 0 | trigger_event(105); stop |
| 8 | 105 | 40 / 5 | 5 | 0 | trigger_event(106); stop |
| 8 | 106 | 40 / 6 | 10 | 0 | trigger_event(107); stop |
| 8 | 107 | 40 / 7 | 8 | 0 | trigger_event(108); stop |
| 8 | 108 | 40 / 8 | 8 | 0 | trigger_event(109); stop |
| 8 | 109 | 40 / 9 | 8 | 0 | trigger_event(110); stop |
| 8 | 110 | 40 / 10 | 1 | 0 | set_switch(1); construct_objects(room=40,group_or_wave=1); stop |
| 8 | 201 | 20 / 1 | 7 | 0 | trigger_event(202); stop |
| 8 | 202 | 20 / 2 | 7 | 0 | trigger_event(203); stop |
| 8 | 203 | 20 / 3 | 10 | 0 | trigger_event(204); stop |
| 8 | 204 | 20 / 4 | 4 | 0 | trigger_event(205); stop |
| 8 | 205 | 20 / 5 | 14 | 0 | trigger_event(206); stop |
| 8 | 206 | 20 / 6 | 10 | 0 | trigger_event(207); stop |
| 8 | 207 | 20 / 7 | 4 | 0 | trigger_event(208); stop |
| 8 | 208 | 20 / 8 | 10 | 0 | trigger_event(209); stop |
| 8 | 209 | 20 / 9 | 8 | 0 | trigger_event(210); stop |
| 8 | 210 | 20 / 10 | 1 | 0 | set_switch(2); construct_objects(room=20,group_or_wave=1); stop |
| 8 | 301 | 70 / 1 | 6 | 0 | trigger_event(302); stop |
| 8 | 302 | 70 / 2 | 10 | 0 | trigger_event(303); stop |
| 8 | 303 | 70 / 3 | 6 | 0 | trigger_event(304); stop |
| 8 | 304 | 70 / 4 | 4 | 0 | trigger_event(305); stop |
| 8 | 305 | 70 / 5 | 5 | 0 | trigger_event(306); stop |
| 8 | 306 | 70 / 6 | 5 | 0 | trigger_event(307); stop |
| 8 | 307 | 70 / 7 | 5 | 0 | trigger_event(308); stop |
| 8 | 308 | 70 / 8 | 5 | 0 | trigger_event(309); stop |
| 8 | 309 | 70 / 9 | 12 | 0 | trigger_event(310); stop |
| 8 | 310 | 70 / 10 | 4 | 0 | set_switch(3); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

A backup is present; decompressed content identical: False. See [text differences](<backup-diff.txt>).

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
