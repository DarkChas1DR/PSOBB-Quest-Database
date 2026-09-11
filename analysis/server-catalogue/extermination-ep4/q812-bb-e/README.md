# War of Limits 2 — extermination-ep4/q812-bb-e

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/extermination-ep4/q812-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/extermination-ep4/q812-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/extermination-ep4/q812-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode4; header quest ID 812; language E. Static scan: **115 objects, 340 enemy/NPC records, 56 events, 97 script labels.** Script roundtrip: byte-identical.

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
0x05, 0x28, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 17 | 0 |
| 5 | 89 | 323 | 56 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 5 | 101 | 10 / 1 | 5 | 3 | trigger_event(102); stop |
| 5 | 102 | 10 / 2 | 6 | 3 | construct_objects(room=10,group_or_wave=1); stop |
| 5 | 103 | 10 / 3 | 7 | 3 | trigger_event(104); stop |
| 5 | 104 | 10 / 4 | 5 | 3 | trigger_event(105); stop |
| 5 | 105 | 10 / 5 | 5 | 3 | trigger_event(106); stop |
| 5 | 106 | 10 / 6 | 7 | 3 | trigger_event(107); stop |
| 5 | 107 | 10 / 7 | 7 | 3 | set_switch(11); stop |
| 5 | 201 | 20 / 1 | 4 | 3 | trigger_event(202); stop |
| 5 | 202 | 20 / 2 | 5 | 3 | trigger_event(203); stop |
| 5 | 203 | 20 / 3 | 6 | 3 | trigger_event(204); stop |
| 5 | 204 | 20 / 4 | 5 | 3 | trigger_event(205); stop |
| 5 | 205 | 20 / 5 | 5 | 3 | trigger_event(206); stop |
| 5 | 206 | 20 / 6 | 6 | 3 | trigger_event(207); stop |
| 5 | 207 | 20 / 7 | 6 | 3 | trigger_event(208); stop |
| 5 | 208 | 20 / 8 | 7 | 3 | trigger_event(209); stop |
| 5 | 209 | 20 / 9 | 7 | 3 | construct_objects(room=20,group_or_wave=1); set_switch(102); stop |
| 5 | 301 | 30 / 1 | 5 | 3 | trigger_event(302); stop |
| 5 | 302 | 30 / 2 | 5 | 3 | trigger_event(303); stop |
| 5 | 303 | 30 / 3 | 5 | 3 | trigger_event(304); stop |
| 5 | 304 | 30 / 4 | 6 | 3 | trigger_event(305); stop |
| 5 | 305 | 30 / 5 | 6 | 3 | trigger_event(306); stop |
| 5 | 306 | 30 / 6 | 6 | 3 | trigger_event(307); stop |
| 5 | 307 | 30 / 7 | 6 | 3 | trigger_event(308); stop |
| 5 | 308 | 30 / 8 | 6 | 3 | construct_objects(room=30,group_or_wave=1); set_switch(103); stop |
| 5 | 401 | 40 / 1 | 5 | 3 | trigger_event(402); stop |
| 5 | 402 | 40 / 2 | 5 | 3 | trigger_event(403); stop |
| 5 | 403 | 40 / 3 | 5 | 3 | trigger_event(404); stop |
| 5 | 404 | 40 / 4 | 6 | 3 | trigger_event(405); stop |
| 5 | 405 | 40 / 5 | 6 | 3 | trigger_event(406); stop |
| 5 | 406 | 40 / 6 | 6 | 3 | trigger_event(407); stop |
| 5 | 407 | 40 / 7 | 6 | 3 | trigger_event(408); stop |
| 5 | 408 | 40 / 8 | 6 | 3 | trigger_event(409); stop |
| 5 | 409 | 40 / 9 | 6 | 3 | trigger_event(410); stop |
| 5 | 410 | 40 / 10 | 6 | 3 | trigger_event(411); stop |
| 5 | 411 | 40 / 11 | 6 | 3 | trigger_event(412); stop |
| 5 | 412 | 40 / 12 | 6 | 3 | trigger_event(413); stop |
| 5 | 413 | 40 / 13 | 6 | 3 | trigger_event(414); stop |
| 5 | 414 | 40 / 14 | 8 | 3 | construct_objects(room=40,group_or_wave=1); set_switch(104); stop |
| 5 | 501 | 50 / 1 | 5 | 3 | trigger_event(502); stop |
| 5 | 502 | 50 / 2 | 5 | 3 | trigger_event(503); stop |
| 5 | 503 | 50 / 3 | 6 | 3 | trigger_event(504); stop |
| 5 | 504 | 50 / 4 | 6 | 3 | trigger_event(505); stop |
| 5 | 505 | 50 / 5 | 6 | 3 | trigger_event(506); stop |
| 5 | 506 | 50 / 6 | 7 | 3 | trigger_event(507); stop |
| 5 | 507 | 50 / 7 | 7 | 3 | trigger_event(508); stop |
| 5 | 508 | 50 / 8 | 7 | 3 | trigger_event(509); stop |
| 5 | 509 | 50 / 9 | 7 | 3 | trigger_event(510); stop |
| 5 | 510 | 50 / 10 | 6 | 3 | construct_objects(room=50,group_or_wave=1); set_switch(105); stop |
| 5 | 601 | 60 / 1 | 4 | 3 | trigger_event(602); stop |
| 5 | 602 | 60 / 2 | 4 | 3 | trigger_event(603); stop |
| 5 | 603 | 60 / 3 | 5 | 3 | trigger_event(604); stop |
| 5 | 604 | 60 / 4 | 5 | 3 | trigger_event(605); stop |
| 5 | 605 | 60 / 5 | 5 | 3 | trigger_event(606); stop |
| 5 | 606 | 60 / 6 | 5 | 3 | trigger_event(607); stop |
| 5 | 607 | 60 / 7 | 6 | 3 | trigger_event(608); stop |
| 5 | 608 | 60 / 8 | 6 | 3 | construct_objects(room=60,group_or_wave=1); set_switch(106); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

A backup is present; decompressed content identical: True. See [text differences](<backup-diff.txt>).

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
