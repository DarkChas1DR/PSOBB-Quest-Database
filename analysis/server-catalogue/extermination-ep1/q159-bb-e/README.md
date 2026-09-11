# Sweep-up Operation #3 — extermination-ep1/q159-bb-e

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/extermination-ep1/q159-bb-e.zip?download=1)**

[Original QST](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/extermination-ep1/q159-bb-e.qst?download=1) · [Extracted BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/extermination-ep1/q159-bb-e/q159-bb-e.qst-quest0.bin?download=1) · [Extracted DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/extermination-ep1/q159-bb-e/q159-bb-e.qst-quest0.dat?download=1)

QST is the preserved original package. BIN and DAT are its decoded payload files, not reassembled scripts. The ZIP contains all three formats.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 159; language E. Static scan: **135 objects, 192 enemy/NPC records, 56 events, 51 script labels.** Script roundtrip: alignment-only.

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
| 7 | 107 | 182 | 56 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 7 | 611 | 61 / 1 | 1 | 60 | trigger_event(612); stop |
| 7 | 612 | 61 / 2 | 7 | 10 | trigger_event(613); stop |
| 7 | 613 | 61 / 3 | 7 | 10 | set_switch(26); stop |
| 7 | 211 | 21 / 1 | 4 | 5 | trigger_event(212); stop |
| 7 | 212 | 21 / 2 | 4 | 15 | set_switch(25); stop |
| 7 | 2211 | 221 / 1 | 6 | 10 | trigger_event(2212); stop |
| 7 | 2212 | 221 / 2 | 6 | 10 | set_switch(27); set_switch(28); stop |
| 7 | 531 | 53 / 1 | 1 | 10 | trigger_event(532); trigger_event(536); stop |
| 7 | 532 | 53 / 2 | 2 | 60 | trigger_event(533); stop |
| 7 | 533 | 53 / 3 | 4 | 10 | trigger_event(534); stop |
| 7 | 534 | 53 / 4 | 6 | 10 | stop |
| 7 | 536 | 53 / 6 | 1 | 30 | trigger_event(537); stop |
| 7 | 537 | 53 / 7 | 4 | 30 | stop |
| 7 | 530 | 53 / 0 | 0 | 0 | set_switch(30); stop |
| 7 | 801 | 80 / 1 | 4 | 60 | set_switch(110); stop |
| 7 | 802 | 80 / 2 | 8 | 30 | trigger_event(803); stop |
| 7 | 803 | 80 / 3 | 2 | 10 | trigger_event(804); stop |
| 7 | 804 | 80 / 4 | 9 | 10 | set_switch(21); stop |
| 7 | 521 | 52 / 1 | 1 | 10 | trigger_event(522); stop |
| 7 | 522 | 52 / 2 | 6 | 10 | trigger_event(523); stop |
| 7 | 523 | 52 / 3 | 6 | 20 | trigger_event(524); stop |
| 7 | 524 | 52 / 4 | 2 | 30 | set_switch(18); set_switch(17); stop |
| 7 | 301 | 30 / 1 | 1 | 1 | trigger_event(302); trigger_event(306); stop |
| 7 | 302 | 30 / 2 | 1 | 1 | trigger_event(303); stop |
| 7 | 303 | 30 / 3 | 2 | 1 | trigger_event(304); stop |
| 7 | 304 | 30 / 4 | 2 | 1 | stop |
| 7 | 306 | 30 / 6 | 2 | 1 | trigger_event(307); stop |
| 7 | 307 | 30 / 7 | 4 | 10 | trigger_event(308); stop |
| 7 | 308 | 30 / 8 | 4 | 10 | stop |
| 7 | 300 | 30 / 0 | 0 | 0 | set_switch(16); stop |
| 7 | 601 | 60 / 1 | 9 | 20 | trigger_event(602); stop |
| 7 | 602 | 60 / 2 | 1 | 20 | trigger_event(603); stop |
| 7 | 603 | 60 / 3 | 4 | 15 | set_switch(12); set_switch(14); stop |
| 7 | 501 | 50 / 1 | 5 | 1 | trigger_event(502); stop |
| 7 | 502 | 50 / 2 | 8 | 10 | trigger_event(503); stop |
| 7 | 503 | 50 / 3 | 4 | 10 | set_switch(9); stop |
| 7 | 2201 | 220 / 1 | 4 | 1 | trigger_event(2202); stop |
| 7 | 2202 | 220 / 2 | 9 | 15 | set_switch(7); stop |
| 7 | 511 | 51 / 1 | 6 | 5 | trigger_event(512); stop |
| 7 | 512 | 51 / 2 | 1 | 10 | trigger_event(513); stop |
| 7 | 513 | 51 / 3 | 2 | 10 | trigger_event(514); trigger_event(518); trigger_event(5112); trigger_event(5116); stop |
| 7 | 514 | 51 / 4 | 1 | 5 | trigger_event(515); stop |
| 7 | 515 | 51 / 5 | 1 | 1 | trigger_event(516); stop |
| 7 | 516 | 51 / 6 | 2 | 10 | set_switch(100); stop |
| 7 | 518 | 51 / 8 | 1 | 5 | trigger_event(519); stop |
| 7 | 519 | 51 / 9 | 1 | 1 | trigger_event(5110); stop |
| 7 | 5110 | 51 / 10 | 2 | 10 | set_switch(101); stop |
| 7 | 5112 | 51 / 12 | 1 | 5 | trigger_event(5113); stop |
| 7 | 5113 | 51 / 13 | 1 | 1 | trigger_event(5114); stop |
| 7 | 5114 | 51 / 14 | 2 | 10 | set_switch(102); stop |
| 7 | 5116 | 51 / 16 | 1 | 5 | trigger_event(5117); stop |
| 7 | 5117 | 51 / 17 | 1 | 1 | trigger_event(5118); stop |
| 7 | 5118 | 51 / 18 | 2 | 10 | set_switch(103); stop |
| 7 | 5120 | 51 / 20 | 1 | 1 | trigger_event(5121); stop |
| 7 | 5121 | 51 / 21 | 5 | 15 | stop |
| 7 | 510 | 51 / 0 | 0 | 0 | set_switch(1); stop |

## Review notes

- Nonzero data after terminal header
