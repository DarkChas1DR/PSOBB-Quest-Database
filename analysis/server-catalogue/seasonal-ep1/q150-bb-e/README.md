# Christmas Fiasco — seasonal-ep1/q150-bb-e

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/seasonal-ep1/q150-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/seasonal-ep1/q150-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/seasonal-ep1/q150-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 150; language E. Static scan: **122 objects, 637 enemy/NPC records, 106 events, 76 script labels.** Script roundtrip: byte-identical.

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
| 0 | 26 | 15 | 0 |
| 4 | 61 | 231 | 43 |
| 7 | 17 | 170 | 30 |
| 10 | 18 | 221 | 33 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 4 | 101 | 10 / 1 | 4 | 0 | trigger_event(102); stop |
| 4 | 102 | 10 / 2 | 4 | 0 | trigger_event(103); stop |
| 4 | 103 | 10 / 3 | 4 | 0 | trigger_event(104); stop |
| 4 | 104 | 10 / 4 | 4 | 0 | trigger_event(105); stop |
| 4 | 105 | 10 / 5 | 2 | 0 | trigger_event(106); stop |
| 4 | 106 | 10 / 6 | 5 | 0 | trigger_event(107); stop |
| 4 | 107 | 10 / 7 | 8 | 0 | trigger_event(108); stop |
| 4 | 108 | 10 / 8 | 6 | 0 | trigger_event(109); stop |
| 4 | 109 | 10 / 9 | 4 | 0 | trigger_event(110); stop |
| 4 | 110 | 10 / 10 | 5 | 0 | trigger_event(111); stop |
| 4 | 111 | 10 / 11 | 12 | 0 | trigger_event(112); stop |
| 4 | 112 | 10 / 12 | 4 | 0 | trigger_event(113); stop |
| 4 | 113 | 10 / 13 | 4 | 0 | trigger_event(114); stop |
| 4 | 114 | 10 / 14 | 5 | 0 | trigger_event(115); stop |
| 4 | 115 | 10 / 15 | 6 | 0 | set_switch(1); stop |
| 4 | 201 | 11 / 1 | 4 | 0 | trigger_event(202); stop |
| 4 | 202 | 11 / 2 | 6 | 0 | trigger_event(203); stop |
| 4 | 203 | 11 / 3 | 6 | 0 | trigger_event(204); stop |
| 4 | 204 | 11 / 4 | 6 | 0 | trigger_event(205); stop |
| 4 | 205 | 11 / 5 | 6 | 0 | trigger_event(206); stop |
| 4 | 206 | 11 / 6 | 8 | 0 | trigger_event(207); stop |
| 4 | 207 | 11 / 7 | 6 | 0 | trigger_event(208); stop |
| 4 | 208 | 11 / 8 | 5 | 0 | set_switch(2); stop |
| 4 | 301 | 20 / 1 | 6 | 0 | trigger_event(302); stop |
| 4 | 302 | 20 / 2 | 6 | 0 | trigger_event(303); stop |
| 4 | 303 | 20 / 3 | 3 | 0 | trigger_event(304); stop |
| 4 | 304 | 20 / 4 | 6 | 0 | trigger_event(305); stop |
| 4 | 305 | 20 / 5 | 6 | 0 | trigger_event(306); stop |
| 4 | 306 | 20 / 6 | 10 | 0 | trigger_event(307); set_switch(201); stop |
| 4 | 307 | 20 / 7 | 3 | 0 | trigger_event(308); stop |
| 4 | 308 | 20 / 8 | 5 | 0 | trigger_event(309); stop |
| 4 | 309 | 20 / 9 | 4 | 0 | trigger_event(310); stop |
| 4 | 310 | 20 / 10 | 6 | 0 | trigger_event(311); stop |
| 4 | 311 | 20 / 11 | 5 | 0 | trigger_event(312); stop |
| 4 | 312 | 20 / 12 | 5 | 0 | set_switch(3); stop |
| 4 | 401 | 12 / 1 | 3 | 0 | trigger_event(402); stop |
| 4 | 402 | 12 / 2 | 4 | 0 | trigger_event(403); set_switch(4); stop |
| 4 | 403 | 12 / 3 | 5 | 0 | trigger_event(404); stop |
| 4 | 404 | 12 / 4 | 5 | 0 | trigger_event(405); set_switch(5); stop |
| 4 | 405 | 12 / 5 | 6 | 0 | trigger_event(406); stop |
| 4 | 406 | 12 / 6 | 3 | 0 | trigger_event(407); set_switch(6); stop |
| 4 | 407 | 12 / 7 | 8 | 0 | trigger_event(408); stop |
| 4 | 408 | 12 / 8 | 8 | 0 | set_switch(7); stop |
| 7 | 101 | 40 / 1 | 5 | 0 | trigger_event(102); stop |
| 7 | 102 | 40 / 2 | 6 | 0 | trigger_event(103); stop |
| 7 | 103 | 40 / 3 | 4 | 0 | trigger_event(104); stop |
| 7 | 104 | 40 / 4 | 1 | 0 | trigger_event(105); stop |
| 7 | 105 | 40 / 5 | 4 | 0 | trigger_event(106); stop |
| 7 | 106 | 40 / 6 | 3 | 0 | trigger_event(107); stop |
| 7 | 107 | 40 / 7 | 3 | 0 | trigger_event(108); stop |
| 7 | 108 | 40 / 8 | 8 | 0 | trigger_event(109); stop |
| 7 | 109 | 40 / 9 | 4 | 0 | trigger_event(110); stop |
| 7 | 110 | 40 / 10 | 9 | 0 | set_switch(1); set_switch(10); stop |
| 7 | 201 | 50 / 1 | 5 | 0 | trigger_event(202); stop |
| 7 | 202 | 50 / 2 | 2 | 0 | trigger_event(203); stop |
| 7 | 203 | 50 / 3 | 2 | 0 | trigger_event(204); stop |
| 7 | 204 | 50 / 4 | 4 | 0 | trigger_event(205); stop |
| 7 | 205 | 50 / 5 | 4 | 0 | trigger_event(206); stop |
| 7 | 206 | 50 / 6 | 11 | 0 | trigger_event(207); stop |
| 7 | 207 | 50 / 7 | 5 | 0 | trigger_event(208); stop |
| 7 | 208 | 50 / 8 | 6 | 0 | trigger_event(209); stop |
| 7 | 209 | 50 / 9 | 7 | 0 | trigger_event(210); stop |
| 7 | 210 | 50 / 10 | 11 | 0 | trigger_event(211); stop |
| 7 | 211 | 50 / 11 | 6 | 0 | trigger_event(212); stop |
| 7 | 212 | 50 / 12 | 6 | 0 | set_switch(2); stop |
| 7 | 301 | 51 / 1 | 3 | 0 | trigger_event(302); stop |
| 7 | 302 | 51 / 2 | 6 | 0 | trigger_event(303); stop |
| 7 | 303 | 51 / 3 | 5 | 0 | trigger_event(304); stop |
| 7 | 304 | 51 / 4 | 7 | 0 | trigger_event(305); stop |
| 7 | 305 | 51 / 5 | 5 | 0 | trigger_event(306); stop |
| 7 | 306 | 51 / 6 | 6 | 0 | trigger_event(307); stop |
| 7 | 307 | 51 / 7 | 14 | 0 | trigger_event(308); stop |
| 7 | 308 | 51 / 8 | 8 | 0 | set_switch(3); stop |
| 10 | 101 | 20 / 1 | 3 | 0 | trigger_event(102); stop |
| 10 | 102 | 20 / 2 | 5 | 0 | trigger_event(103); stop |
| 10 | 103 | 20 / 3 | 5 | 0 | trigger_event(104); stop |
| 10 | 104 | 20 / 4 | 5 | 0 | trigger_event(105); stop |
| 10 | 105 | 20 / 5 | 5 | 0 | trigger_event(106); stop |
| 10 | 106 | 20 / 6 | 2 | 0 | trigger_event(107); stop |
| 10 | 107 | 20 / 7 | 2 | 0 | trigger_event(108); stop |
| 10 | 108 | 20 / 8 | 6 | 0 | trigger_event(109); stop |
| 10 | 109 | 20 / 9 | 5 | 0 | trigger_event(110); stop |
| 10 | 110 | 20 / 10 | 7 | 0 | trigger_event(111); stop |
| 10 | 111 | 20 / 11 | 7 | 0 | trigger_event(112); stop |
| 10 | 112 | 20 / 12 | 7 | 0 | set_switch(1); stop |
| 10 | 201 | 30 / 1 | 6 | 0 | trigger_event(202); stop |
| 10 | 202 | 30 / 2 | 6 | 0 | trigger_event(203); stop |
| 10 | 203 | 30 / 3 | 5 | 0 | trigger_event(204); stop |
| 10 | 204 | 30 / 4 | 5 | 0 | trigger_event(205); stop |
| 10 | 205 | 30 / 5 | 5 | 0 | trigger_event(206); stop |
| 10 | 206 | 30 / 6 | 6 | 0 | set_switch(2); stop |
| 10 | 301 | 40 / 1 | 5 | 0 | trigger_event(302); stop |
| 10 | 302 | 40 / 2 | 6 | 0 | trigger_event(303); stop |
| 10 | 303 | 40 / 3 | 9 | 0 | trigger_event(304); stop |
| 10 | 304 | 40 / 4 | 10 | 0 | trigger_event(305); stop |
| 10 | 305 | 40 / 5 | 8 | 0 | trigger_event(306); stop |
| 10 | 306 | 40 / 6 | 10 | 0 | trigger_event(307); stop |
| 10 | 307 | 40 / 7 | 11 | 0 | trigger_event(308); stop |
| 10 | 308 | 40 / 8 | 15 | 0 | trigger_event(309); stop |
| 10 | 309 | 40 / 9 | 8 | 0 | trigger_event(310); stop |
| 10 | 310 | 40 / 10 | 6 | 0 | trigger_event(311); stop |
| 10 | 311 | 40 / 11 | 6 | 0 | trigger_event(312); stop |
| 10 | 312 | 40 / 12 | 12 | 0 | trigger_event(313); stop |
| 10 | 313 | 40 / 13 | 10 | 0 | trigger_event(314); stop |
| 10 | 314 | 40 / 14 | 4 | 0 | trigger_event(315); stop |
| 10 | 315 | 40 / 15 | 9 | 0 | set_switch(3); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

A backup is present; decompressed content identical: False. See [text differences](<backup-diff.txt>).

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
