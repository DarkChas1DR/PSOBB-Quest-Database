# Sweep-up Operation #6 — extermination-ep2/q167-bb-e

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/extermination-ep2/q167-bb-e.zip?download=1)**

[Original QST](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/extermination-ep2/q167-bb-e.qst?download=1) · [Extracted BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/extermination-ep2/q167-bb-e/q167-bb-e.qst-quest0.bin?download=1) · [Extracted DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/extermination-ep2/q167-bb-e/q167-bb-e.qst-quest0.dat?download=1)

QST is the preserved original package. BIN and DAT are its decoded payload files, not reassembled scripts. The ZIP contains all three formats.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 167; language E. Static scan: **192 objects, 213 enemy/NPC records, 50 events, 52 script labels.** Script roundtrip: alignment-only.

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
| 0 | 43 | 8 | 0 |
| 3 | 149 | 205 | 50 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 3 | 101 | 10 / 1 | 3 | 30 | trigger_event(102); stop |
| 3 | 102 | 10 / 2 | 5 | 30 | set_switch(5); set_switch(6); stop |
| 3 | 201 | 20 / 1 | 3 | 30 | trigger_event(202); stop |
| 3 | 202 | 20 / 2 | 5 | 30 | set_switch(7); set_switch(8); stop |
| 3 | 401 | 40 / 1 | 7 | 30 | trigger_event(402); stop |
| 3 | 402 | 40 / 2 | 3 | 10 | trigger_event(403); stop |
| 3 | 403 | 40 / 3 | 5 | 10 | trigger_event(404); stop |
| 3 | 404 | 40 / 4 | 5 | 50 | set_switch(9); set_switch(10); stop |
| 3 | 511 | 51 / 1 | 4 | 60 | trigger_event(512); stop |
| 3 | 512 | 51 / 2 | 4 | 30 | trigger_event(513); stop |
| 3 | 513 | 51 / 3 | 6 | 10 | set_switch(15); set_switch(16); stop |
| 3 | 1601 | 160 / 1 | 3 | 1 | stop |
| 3 | 521 | 52 / 1 | 9 | 40 | trigger_event(522); stop |
| 3 | 522 | 52 / 2 | 5 | 30 | trigger_event(523); stop |
| 3 | 523 | 52 / 3 | 7 | 30 | set_switch(18); set_switch(19); set_switch(201); set_switch(21); stop |
| 3 | 520 | 52 / 0 | 0 | 1 | set_switch(21); stop |
| 3 | 211 | 21 / 1 | 1 | 1 | trigger_event(212); stop |
| 3 | 212 | 21 / 2 | 1 | 30 | set_switch(20); set_switch(26); stop |
| 3 | 1911 | 191 / 1 | 2 | 1 | stop |
| 3 | 302 | 30 / 2 | 4 | 60 | trigger_event(301); stop |
| 3 | 301 | 30 / 1 | 8 | 20 | construct_objects(room=30,group_or_wave=1); stop |
| 3 | 300 | 30 / 0 | 0 | 3 | set_switch(27); construct_objects(room=30,group_or_wave=2); stop |
| 3 | 321 | 32 / 1 | 5 | 30 | trigger_event(322); stop |
| 3 | 322 | 32 / 2 | 7 | 30 | set_switch(23); set_switch(25); stop |
| 3 | 1821 | 182 / 1 | 5 | 40 | stop |
| 3 | 121 | 12 / 1 | 2 | 60 | set_switch(221); stop |
| 3 | 122 | 12 / 2 | 1 | 120 | set_switch(222); stop |
| 3 | 123 | 12 / 3 | 1 | 180 | set_switch(223); stop |
| 3 | 124 | 12 / 4 | 1 | 240 | set_switch(224); stop |
| 3 | 125 | 12 / 5 | 1 | 300 | set_switch(225); stop |
| 3 | 126 | 12 / 6 | 6 | 30 | construct_objects(room=12,group_or_wave=1); stop |
| 3 | 120 | 12 / 0 | 0 | 1 | set_switch(28); construct_objects(room=12,group_or_wave=2); stop |
| 3 | 420 | 42 / 0 | 0 | 1 | set_switch(27); set_switch(28); stop |
| 3 | 421 | 42 / 1 | 1 | 1 | trigger_event(423); stop |
| 3 | 423 | 42 / 3 | 6 | 20 | trigger_event(424); stop |
| 3 | 424 | 42 / 4 | 8 | 20 | trigger_event(425); stop |
| 3 | 425 | 42 / 5 | 7 | 10 | set_switch(29); set_switch(30); set_switch(33); set_switch(34); set_switch(36); stop |
| 3 | 1401 | 140 / 0 | 0 | 1 | construct_objects(room=1,group_or_wave=1); stop |
| 3 | 1611 | 161 / 1 | 2 | 1 | stop |
| 3 | 1612 | 161 / 2 | 2 | 1 | stop |
| 3 | 111 | 11 / 1 | 5 | 30 | trigger_event(112); stop |
| 3 | 112 | 11 / 2 | 4 | 30 | set_switch(37); stop |
| 3 | 311 | 31 / 1 | 7 | 1 | trigger_event(312); stop |
| 3 | 501 | 50 / 1 | 6 | 1 | trigger_event(502); stop |
| 3 | 502 | 50 / 2 | 2 | 30 | trigger_event(503); stop |
| 3 | 503 | 50 / 3 | 8 | 30 | trigger_event(504); stop |
| 3 | 504 | 50 / 4 | 6 | 10 | trigger_event(505); stop |
| 3 | 505 | 50 / 5 | 0 | 10 | set_switch(38); stop |
| 3 | 312 | 31 / 2 | 6 | 30 | trigger_event(313); stop |
| 3 | 313 | 31 / 3 | 9 | 30 | set_switch(39); set_switch(40); set_switch(41); set_switch(42); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
