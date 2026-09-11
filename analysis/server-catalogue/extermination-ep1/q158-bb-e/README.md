# Sweep-up Operation #2 — extermination-ep1/q158-bb-e

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/extermination-ep1/q158-bb-e.zip?download=1)**

[Original QST](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/extermination-ep1/q158-bb-e.qst?download=1) · [Extracted BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/extermination-ep1/q158-bb-e/q158-bb-e.qst-quest0.bin?download=1) · [Extracted DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/extermination-ep1/q158-bb-e/q158-bb-e.qst-quest0.dat?download=1)

QST is the preserved original package. BIN and DAT are its decoded payload files, not reassembled scripts. The ZIP contains all three formats.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 158; language E. Static scan: **138 objects, 185 enemy/NPC records, 59 events, 44 script labels.** Script roundtrip: alignment-only.

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
| 0 | 28 | 10 | 0 |
| 5 | 110 | 175 | 59 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 5 | 501 | 50 / 1 | 4 | 5 | trigger_event(502); stop |
| 5 | 502 | 50 / 2 | 4 | 5 | trigger_event(503); stop |
| 5 | 503 | 50 / 3 | 4 | 10 | set_switch(7); stop |
| 5 | 401 | 40 / 1 | 5 | 10 | trigger_event(402); stop |
| 5 | 402 | 40 / 2 | 6 | 10 | trigger_event(403); stop |
| 5 | 403 | 40 / 3 | 6 | 10 | set_switch(203); stop |
| 5 | 311 | 31 / 1 | 5 | 5 | trigger_event(312); stop |
| 5 | 312 | 31 / 2 | 4 | 15 | trigger_event(313); stop |
| 5 | 313 | 31 / 3 | 6 | 15 | set_switch(24); stop |
| 5 | 1502 | 150 / 2 | 1 | 1 | stop |
| 5 | 1501 | 150 / 1 | 2 | 1 | stop |
| 5 | 221 | 22 / 1 | 4 | 1 | trigger_event(222); stop |
| 5 | 222 | 22 / 2 | 4 | 1 | trigger_event(223); stop |
| 5 | 223 | 22 / 3 | 6 | 1 | trigger_event(224); stop |
| 5 | 224 | 22 / 4 | 1 | 1 | set_switch(28); stop |
| 5 | 511 | 51 / 1 | 5 | 5 | trigger_event(512); stop |
| 5 | 512 | 51 / 2 | 1 | 5 | trigger_event(513); trigger_event(516); trigger_event(519); trigger_event(5112); trigger_event(5115); stop |
| 5 | 513 | 51 / 3 | 2 | 10 | trigger_event(514); stop |
| 5 | 514 | 51 / 4 | 2 | 20 | stop |
| 5 | 516 | 51 / 6 | 1 | 10 | trigger_event(517); stop |
| 5 | 517 | 51 / 7 | 1 | 10 | trigger_event(518); stop |
| 5 | 518 | 51 / 8 | 1 | 10 | stop |
| 5 | 519 | 51 / 9 | 1 | 10 | trigger_event(5110); stop |
| 5 | 5110 | 51 / 10 | 1 | 10 | trigger_event(5111); stop |
| 5 | 5111 | 51 / 11 | 1 | 10 | stop |
| 5 | 5112 | 51 / 12 | 1 | 10 | trigger_event(5113); stop |
| 5 | 5113 | 51 / 13 | 1 | 10 | trigger_event(5114); stop |
| 5 | 5114 | 51 / 14 | 1 | 10 | stop |
| 5 | 5115 | 51 / 15 | 1 | 10 | trigger_event(5116); stop |
| 5 | 5116 | 51 / 16 | 1 | 10 | trigger_event(5117); stop |
| 5 | 5117 | 51 / 17 | 1 | 10 | stop |
| 5 | 510 | 51 / 0 | 0 | 0 | set_switch(15); set_switch(13); stop |
| 5 | 211 | 21 / 1 | 6 | 30 | trigger_event(212); stop |
| 5 | 212 | 21 / 2 | 4 | 10 | trigger_event(213); stop |
| 5 | 213 | 21 / 3 | 5 | 15 | set_switch(16); stop |
| 5 | 611 | 61 / 1 | 1 | 1 | trigger_event(612); stop |
| 5 | 612 | 61 / 2 | 5 | 5 | trigger_event(613); stop |
| 5 | 613 | 61 / 3 | 5 | 5 | set_switch(205); stop |
| 5 | 711 | 71 / 1 | 6 | 30 | trigger_event(712); stop |
| 5 | 712 | 71 / 2 | 5 | 30 | trigger_event(713); stop |
| 5 | 713 | 71 / 3 | 8 | 15 | trigger_event(714); stop |
| 5 | 714 | 71 / 4 | 7 | 5 | set_switch(18); stop |
| 5 | 1101 | 110 / 1 | 1 | 5 | stop |
| 5 | 1102 | 110 / 2 | 4 | 5 | stop |
| 5 | 541 | 54 / 1 | 6 | 30 | trigger_event(542); trigger_event(547); stop |
| 5 | 542 | 54 / 2 | 2 | 60 | trigger_event(543); stop |
| 5 | 543 | 54 / 3 | 2 | 15 | trigger_event(544); stop |
| 5 | 544 | 54 / 4 | 2 | 1 | trigger_event(545); stop |
| 5 | 545 | 54 / 5 | 2 | 1 | trigger_event(546); stop |
| 5 | 546 | 54 / 6 | 2 | 1 | stop |
| 5 | 547 | 54 / 7 | 4 | 5 | trigger_event(548); stop |
| 5 | 548 | 54 / 8 | 1 | 1 | trigger_event(549); stop |
| 5 | 549 | 54 / 9 | 4 | 10 | trigger_event(5410); stop |
| 5 | 5410 | 54 / 10 | 4 | 10 | trigger_event(5411); stop |
| 5 | 5411 | 54 / 11 | 5 | 10 | stop |
| 5 | 540 | 54 / 0 | 0 | 0 | set_switch(20); stop |
| 5 | 6111 | 61 / 1 | 1 | 1 | trigger_event(6112); stop |
| 5 | 6112 | 61 / 2 | 5 | 10 | trigger_event(6113); stop |
| 5 | 6113 | 61 / 3 | 5 | 10 | set_switch(205); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
