# Maximum Attack 4th Stage -1C- — maximum-attack-ep1/q146-bb-e

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/maximum-attack-ep1/q146-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/maximum-attack-ep1/q146-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/maximum-attack-ep1/q146-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 146; language E. Static scan: **168 objects, 471 enemy/NPC records, 90 events, 237 script labels.** Script roundtrip: alignment-only.

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
0x00, 0x00, 0x00, 0x00, 0x00
0x04, 0x04, 0x00, 0x02, 0x00
0x07, 0x07, 0x00, 0x02, 0x00
0x0A, 0x0A, 0x00, 0x01, 0x00
0x0E, 0x0E, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 20 | 0 |
| 4 | 67 | 218 | 41 |
| 7 | 47 | 118 | 28 |
| 10 | 22 | 114 | 20 |
| 14 | 6 | 1 | 1 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 4 | 121 | 12 / 1 | 7 | 3 | trigger_event(122); stop |
| 4 | 122 | 12 / 2 | 7 | 3 | trigger_event(123); stop |
| 4 | 123 | 12 / 3 | 5 | 3 | trigger_event(124); stop |
| 4 | 124 | 12 / 4 | 6 | 3 | set_switch(121); stop |
| 4 | 221 | 22 / 1 | 8 | 3 | trigger_event(222); stop |
| 4 | 222 | 22 / 2 | 8 | 3 | trigger_event(223); stop |
| 4 | 223 | 22 / 3 | 4 | 3 | set_switch(22); stop |
| 4 | 601 | 60 / 1 | 7 | 3 | trigger_event(602); stop |
| 4 | 602 | 60 / 2 | 7 | 3 | trigger_event(603); stop |
| 4 | 603 | 60 / 3 | 7 | 3 | trigger_event(604); set_switch(60); stop |
| 4 | 604 | 60 / 4 | 1 | 450 | stop |
| 4 | 451 | 45 / 1 | 6 | 3 | trigger_event(452); stop |
| 4 | 452 | 45 / 2 | 6 | 3 | trigger_event(453); stop |
| 4 | 453 | 45 / 3 | 5 | 3 | trigger_event(454); stop |
| 4 | 454 | 45 / 4 | 3 | 3 | set_switch(45); stop |
| 4 | 301 | 30 / 1 | 5 | 3 | trigger_event(302); stop |
| 4 | 302 | 30 / 2 | 5 | 3 | trigger_event(303); stop |
| 4 | 303 | 30 / 3 | 5 | 3 | trigger_event(304); stop |
| 4 | 304 | 30 / 4 | 5 | 3 | set_switch(30); stop |
| 4 | 351 | 35 / 1 | 8 | 3 | trigger_event(352); stop |
| 4 | 352 | 35 / 2 | 8 | 3 | trigger_event(353); stop |
| 4 | 353 | 35 / 3 | 8 | 3 | set_switch(35); trigger_event(354); stop |
| 4 | 354 | 35 / 4 | 3 | 3 | trigger_event(355); stop |
| 4 | 355 | 35 / 5 | 2 | 3 | trigger_event(356); stop |
| 4 | 356 | 35 / 6 | 1 | 3 | construct_objects(room=35,group_or_wave=1); stop |
| 4 | 401 | 40 / 1 | 2 | 3 | trigger_event(402); stop |
| 4 | 402 | 40 / 2 | 8 | 3 | trigger_event(403); stop |
| 4 | 403 | 40 / 3 | 7 | 3 | trigger_event(404); stop |
| 4 | 404 | 40 / 4 | 7 | 3 | trigger_event(405); stop |
| 4 | 405 | 40 / 5 | 3 | 3 | trigger_event(406); stop |
| 4 | 406 | 40 / 6 | 3 | 3 | set_switch(41); stop |
| 4 | 161 | 16 / 1 | 4 | 3 | trigger_event(162); stop |
| 4 | 162 | 16 / 2 | 6 | 3 | trigger_event(163); stop |
| 4 | 163 | 16 / 3 | 4 | 3 | trigger_event(164); stop |
| 4 | 164 | 16 / 4 | 6 | 3 | set_switch(16); stop |
| 4 | 231 | 23 / 1 | 8 | 3 | trigger_event(232); stop |
| 4 | 232 | 23 / 2 | 8 | 3 | trigger_event(233); stop |
| 4 | 233 | 23 / 3 | 4 | 3 | set_switch(23); set_switch(15); stop |
| 4 | 151 | 15 / 1 | 5 | 3 | trigger_event(152); stop |
| 4 | 152 | 15 / 2 | 5 | 3 | trigger_event(153); set_switch(40); stop |
| 4 | 153 | 15 / 3 | 1 | 300 | stop |
| 7 | 2201 | 220 / 1 | 3 | 3 | trigger_event(222); stop |
| 7 | 222 | 220 / 2 | 2 | 3 | trigger_event(223); stop |
| 7 | 223 | 220 / 3 | 8 | 3 | trigger_event(224); stop |
| 7 | 224 | 220 / 4 | 2 | 3 | set_switch(220); stop |
| 7 | 531 | 53 / 1 | 1 | 3 | trigger_event(532); stop |
| 7 | 532 | 53 / 2 | 1 | 3 | trigger_event(533); stop |
| 7 | 533 | 53 / 3 | 2 | 3 | trigger_event(534); stop |
| 7 | 534 | 53 / 4 | 9 | 3 | trigger_event(535); stop |
| 7 | 535 | 53 / 5 | 9 | 3 | trigger_event(536); stop |
| 7 | 536 | 53 / 6 | 2 | 3 | trigger_event(537); stop |
| 7 | 537 | 53 / 7 | 2 | 3 | set_switch(8); stop |
| 7 | 538 | 53 / 8 | 5 | 3 | trigger_event(539); stop |
| 7 | 539 | 53 / 9 | 3 | 3 | set_switch(53); stop |
| 7 | 521 | 52 / 1 | 9 | 3 | trigger_event(522); stop |
| 7 | 522 | 52 / 2 | 1 | 3 | trigger_event(523); stop |
| 7 | 523 | 52 / 3 | 4 | 3 | trigger_event(524); stop |
| 7 | 524 | 52 / 4 | 4 | 3 | trigger_event(525); stop |
| 7 | 525 | 52 / 5 | 4 | 3 | trigger_event(526); stop |
| 7 | 526 | 52 / 6 | 2 | 3 | trigger_event(527); stop |
| 7 | 527 | 52 / 7 | 3 | 3 | set_switch(52); stop |
| 7 | 611 | 61 / 1 | 5 | 3 | trigger_event(612); stop |
| 7 | 612 | 61 / 2 | 8 | 3 | trigger_event(613); stop |
| 7 | 613 | 61 / 3 | 5 | 3 | trigger_event(614); stop |
| 7 | 614 | 61 / 4 | 6 | 300 | trigger_event(615); stop |
| 7 | 615 | 61 / 5 | 1 | 3 | trigger_event(616); stop |
| 7 | 616 | 61 / 6 | 9 | 3 | trigger_event(617); stop |
| 7 | 617 | 61 / 7 | 4 | 3 | trigger_event(618); stop |
| 7 | 618 | 61 / 8 | 4 | 600 | set_switch(61); stop |
| 10 | 431 | 43 / 1 | 4 | 3 | trigger_event(432); stop |
| 10 | 432 | 43 / 2 | 8 | 3 | trigger_event(433); stop |
| 10 | 433 | 43 / 3 | 8 | 3 | trigger_event(434); stop |
| 10 | 434 | 43 / 4 | 3 | 3 | trigger_event(435); stop |
| 10 | 435 | 43 / 5 | 2 | 3 | set_switch(43); stop |
| 10 | 801 | 80 / 1 | 3 | 3 | trigger_event(802); stop |
| 10 | 802 | 80 / 2 | 6 | 3 | trigger_event(803); stop |
| 10 | 803 | 80 / 3 | 7 | 3 | trigger_event(804); stop |
| 10 | 804 | 80 / 4 | 8 | 3 | trigger_event(805); stop |
| 10 | 805 | 80 / 5 | 6 | 3 | set_switch(3); stop |
| 10 | 806 | 80 / 6 | 7 | 3 | trigger_event(807); stop |
| 10 | 807 | 80 / 7 | 5 | 3 | trigger_event(808); stop |
| 10 | 808 | 80 / 8 | 8 | 3 | trigger_event(809); stop |
| 10 | 809 | 80 / 9 | 3 | 3 | trigger_event(810); stop |
| 10 | 810 | 80 / 10 | 8 | 3 | trigger_event(811); stop |
| 10 | 811 | 80 / 11 | 9 | 3 | set_switch(2); stop |
| 10 | 812 | 80 / 12 | 3 | 3 | trigger_event(813); stop |
| 10 | 813 | 80 / 13 | 6 | 3 | trigger_event(814); stop |
| 10 | 814 | 80 / 14 | 6 | 3 | trigger_event(815); stop |
| 10 | 815 | 80 / 15 | 4 | 3 | set_switch(80); stop |
| 14 | 1 | 0 / 1 | 1 | 50 | construct_objects(room=0,group_or_wave=1); construct_objects(room=1,group_or_wave=1); construct_objects(room=2,group_or_wave=1); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

A backup is present; decompressed content identical: True. See [text differences](<backup-diff.txt>).

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
