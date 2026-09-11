# Maximum Attack 4th Stage -4A- — maximum-attack-ep4/q303-bb-e

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/maximum-attack-ep4/q303-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/maximum-attack-ep4/q303-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/maximum-attack-ep4/q303-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode4; header quest ID 303; language E. Static scan: **117 objects, 404 enemy/NPC records, 60 events, 222 script labels.** Script roundtrip: byte-identical.

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
0x08, 0x2B, 0x00, 0x01, 0x00
0x05, 0x28, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 29 | 20 | 0 |
| 5 | 37 | 184 | 30 |
| 8 | 51 | 200 | 30 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 5 | 601 | 60 / 1 | 6 | 3 | trigger_event(602); stop |
| 5 | 602 | 60 / 2 | 6 | 3 | trigger_event(603); stop |
| 5 | 603 | 60 / 3 | 8 | 3 | trigger_event(604); stop |
| 5 | 604 | 60 / 4 | 8 | 3 | trigger_event(605); stop |
| 5 | 605 | 60 / 5 | 8 | 3 | trigger_event(606); stop |
| 5 | 606 | 60 / 6 | 8 | 3 | trigger_event(607); stop |
| 5 | 607 | 60 / 7 | 8 | 3 | set_switch(61); trigger_event(608); stop |
| 5 | 608 | 60 / 8 | 8 | 3 | trigger_event(609); stop |
| 5 | 609 | 60 / 9 | 8 | 3 | trigger_event(610); stop |
| 5 | 610 | 60 / 10 | 3 | 3 | trigger_event(611); stop |
| 5 | 611 | 60 / 11 | 3 | 3 | trigger_event(612); stop |
| 5 | 612 | 60 / 12 | 5 | 3 | trigger_event(613); stop |
| 5 | 613 | 60 / 13 | 8 | 3 | trigger_event(614); stop |
| 5 | 614 | 60 / 14 | 2 | 3 | trigger_event(615); stop |
| 5 | 615 | 60 / 15 | 8 | 3 | trigger_event(616); stop |
| 5 | 616 | 60 / 16 | 3 | 3 | stop |
| 5 | 501 | 50 / 1 | 6 | 3 | trigger_event(502); stop |
| 5 | 502 | 50 / 2 | 6 | 3 | trigger_event(503); stop |
| 5 | 503 | 50 / 3 | 6 | 3 | set_switch(51); trigger_event(504); stop |
| 5 | 504 | 50 / 4 | 8 | 3 | trigger_event(505); stop |
| 5 | 505 | 50 / 5 | 5 | 3 | trigger_event(506); stop |
| 5 | 506 | 50 / 6 | 5 | 3 | trigger_event(507); stop |
| 5 | 507 | 50 / 7 | 7 | 3 | trigger_event(508); stop |
| 5 | 508 | 50 / 8 | 5 | 3 | set_switch(52); trigger_event(509); stop |
| 5 | 509 | 50 / 9 | 8 | 3 | trigger_event(510); stop |
| 5 | 510 | 50 / 10 | 5 | 3 | trigger_event(511); stop |
| 5 | 511 | 50 / 11 | 5 | 3 | trigger_event(512); stop |
| 5 | 512 | 50 / 12 | 8 | 3 | trigger_event(513); stop |
| 5 | 513 | 50 / 13 | 5 | 3 | trigger_event(514); stop |
| 5 | 514 | 50 / 14 | 5 | 3 | construct_objects(room=50,group_or_wave=1); stop |
| 8 | 901 | 90 / 1 | 6 | 3 | trigger_event(902); stop |
| 8 | 902 | 90 / 2 | 8 | 3 | trigger_event(903); stop |
| 8 | 903 | 90 / 3 | 7 | 3 | trigger_event(904); stop |
| 8 | 904 | 90 / 4 | 8 | 3 | trigger_event(905); stop |
| 8 | 905 | 90 / 5 | 7 | 3 | set_switch(90); stop |
| 8 | 701 | 70 / 1 | 8 | 3 | trigger_event(702); stop |
| 8 | 702 | 70 / 2 | 8 | 3 | trigger_event(703); stop |
| 8 | 703 | 70 / 3 | 8 | 90 | construct_objects(room=70,group_or_wave=1); stop |
| 8 | 704 | 70 / 4 | 8 | 3 | trigger_event(705); stop |
| 8 | 705 | 70 / 5 | 8 | 3 | trigger_event(706); stop |
| 8 | 706 | 70 / 6 | 7 | 3 | trigger_event(707); stop |
| 8 | 707 | 70 / 7 | 7 | 3 | set_switch(70); stop |
| 8 | 401 | 40 / 1 | 3 | 3 | trigger_event(402); stop |
| 8 | 402 | 40 / 2 | 6 | 3 | trigger_event(403); stop |
| 8 | 403 | 40 / 3 | 5 | 3 | trigger_event(404); stop |
| 8 | 404 | 40 / 4 | 6 | 3 | trigger_event(405); stop |
| 8 | 405 | 40 / 5 | 5 | 3 | set_switch(40); stop |
| 8 | 1001 | 100 / 1 | 8 | 3 | trigger_event(1002); stop |
| 8 | 1002 | 100 / 2 | 7 | 3 | trigger_event(1003); stop |
| 8 | 1003 | 100 / 3 | 6 | 3 | trigger_event(1004); stop |
| 8 | 1004 | 100 / 4 | 7 | 3 | trigger_event(1005); stop |
| 8 | 1005 | 100 / 5 | 7 | 3 | set_switch(100); stop |
| 8 | 501 | 50 / 1 | 5 | 3 | trigger_event(502); stop |
| 8 | 502 | 50 / 2 | 8 | 3 | trigger_event(503); stop |
| 8 | 503 | 50 / 3 | 8 | 3 | trigger_event(504); stop |
| 8 | 504 | 50 / 4 | 6 | 3 | trigger_event(505); stop |
| 8 | 505 | 50 / 5 | 6 | 3 | trigger_event(506); stop |
| 8 | 506 | 50 / 6 | 5 | 3 | trigger_event(507); stop |
| 8 | 507 | 50 / 7 | 5 | 3 | trigger_event(508); stop |
| 8 | 508 | 50 / 8 | 7 | 3 | set_switch(50); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

A backup is present; decompressed content identical: True. See [text differences](<backup-diff.txt>).

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
