# Simulator 2.0 — events-ep1/q399-bb-e

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/events-ep1/q399-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/events-ep1/q399-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/events-ep1/q399-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 399; language E. Static scan: **233 objects, 268 enemy/NPC records, 48 events, 100 script labels.** Script roundtrip: differs.

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
0x02, 0x02, 0x00, 0x00, 0x00
0x04, 0x04, 0x00, 0x00, 0x00
0x07, 0x07, 0x00, 0x00, 0x00
0x0A, 0x0A, 0x00, 0x00, 0x00
0x0C, 0x0C, 0x00, 0x00, 0x00
0x10, 0x10, 0x00, 0x00, 0x00
0x11, 0x11, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 25 | 20 | 0 |
| 2 | 56 | 35 | 8 |
| 4 | 23 | 38 | 3 |
| 7 | 32 | 47 | 12 |
| 10 | 45 | 34 | 5 |
| 12 | 17 | 1 | 1 |
| 16 | 17 | 40 | 12 |
| 17 | 18 | 53 | 7 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 2 | 501 | 11 / 1 | 3 | 100 | trigger_event(502); stop |
| 2 | 502 | 11 / 2 | 6 | 60 | trigger_event(503); stop |
| 2 | 503 | 11 / 3 | 5 | 60 | trigger_event(504); stop |
| 2 | 504 | 11 / 4 | 4 | 60 | trigger_event(505); trigger_event(506); construct_objects(room=11,group_or_wave=1); stop |
| 2 | 505 | 11 / 5 | 3 | 10 | stop |
| 2 | 506 | 11 / 6 | 6 | 500 | set_switch(5); trigger_event(507); stop |
| 2 | 507 | 11 / 7 | 4 | 50 | trigger_event(508); stop |
| 2 | 508 | 11 / 8 | 4 | 40 | stop |
| 4 | 601 | 60 / 1 | 6 | 1 | trigger_event(602); stop |
| 4 | 602 | 60 / 2 | 12 | 30 | trigger_event(603); set_switch(5); stop |
| 4 | 603 | 60 / 3 | 20 | 25 | stop |
| 7 | 700 | 0 / 0 | 0 | 0 | set_switch(4); trigger_event(701); stop |
| 7 | 701 | 80 / 1 | 8 | 100 | trigger_event(702); trigger_event(703); stop |
| 7 | 702 | 80 / 2 | 4 | 50 | stop |
| 7 | 703 | 80 / 3 | 5 | 500 | trigger_event(704); stop |
| 7 | 704 | 80 / 4 | 2 | 50 | set_switch(5); set_switch(6); trigger_event(705); clear_switch(4); trigger_event(706); stop |
| 7 | 705 | 80 / 5 | 4 | 100 | trigger_event(707); trigger_event(708); stop |
| 7 | 706 | 80 / 6 | 2 | 500 | stop |
| 7 | 707 | 80 / 7 | 2 | 50 | stop |
| 7 | 708 | 80 / 8 | 5 | 500 | clear_switch(6); set_switch(10); trigger_event(709); set_switch(7); stop |
| 7 | 709 | 80 / 9 | 7 | 50 | trigger_event(710); stop |
| 7 | 710 | 80 / 10 | 3 | 40 | trigger_event(711); stop |
| 7 | 711 | 80 / 11 | 5 | 50 | clear_switch(7); stop |
| 10 | 729 | 0 / 0 | 0 | 0 | set_switch(10); trigger_event(730); stop |
| 10 | 730 | 80 / 1 | 6 | 100 | trigger_event(731); stop |
| 10 | 731 | 80 / 2 | 4 | 50 | trigger_event(732); stop |
| 10 | 732 | 80 / 3 | 10 | 75 | set_switch(5); trigger_event(733); stop |
| 10 | 733 | 80 / 4 | 14 | 75 | clear_switch(10); stop |
| 12 | 1 | 1 / 1 | 1 | 50 | set_switch(40); construct_objects(room=1,group_or_wave=1); stop |
| 16 | 801 | 50 / 1 | 4 | 40 | trigger_event(802); stop |
| 16 | 802 | 50 / 2 | 4 | 50 | trigger_event(803); stop |
| 16 | 803 | 50 / 3 | 3 | 50 | trigger_event(804); trigger_event(805); trigger_event(806); trigger_event(807); trigger_event(812); stop |
| 16 | 804 | 50 / 4 | 1 | 1 | trigger_event(808); stop |
| 16 | 805 | 50 / 5 | 1 | 50 | trigger_event(809); stop |
| 16 | 806 | 50 / 6 | 1 | 100 | trigger_event(810); stop |
| 16 | 807 | 50 / 7 | 1 | 150 | trigger_event(811); stop |
| 16 | 808 | 50 / 8 | 5 | 100 | stop |
| 16 | 809 | 50 / 9 | 5 | 100 | stop |
| 16 | 810 | 50 / 10 | 5 | 100 | stop |
| 16 | 811 | 50 / 11 | 5 | 100 | stop |
| 16 | 812 | 50 / 12 | 5 | 800 | set_switch(40); stop |
| 17 | 530 | 40 / 1 | 4 | 20 | trigger_event(533); stop |
| 17 | 533 | 40 / 4 | 5 | 45 | trigger_event(534); stop |
| 17 | 534 | 40 / 5 | 4 | 50 | trigger_event(535); stop |
| 17 | 535 | 40 / 6 | 6 | 50 | trigger_event(536); stop |
| 17 | 536 | 40 / 7 | 6 | 50 | trigger_event(537); stop |
| 17 | 537 | 40 / 8 | 15 | 50 | trigger_event(538); stop |
| 17 | 538 | 40 / 9 | 13 | 50 | stop |

## Review notes

- Reassembled bytes differ beyond recognized alignment; inspect before rebuilding

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
