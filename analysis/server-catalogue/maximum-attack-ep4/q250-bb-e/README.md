# Maximum Attack S — maximum-attack-ep4/q250-bb-e

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/maximum-attack-ep4/q250-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/maximum-attack-ep4/q250-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/maximum-attack-ep4/q250-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode4; header quest ID 250; language E. Static scan: **68 objects, 607 enemy/NPC records, 71 events, 194 script labels.** Script roundtrip: byte-identical.

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
0x06, 0x29, 0x00, 0x00, 0x00
0x05, 0x28, 0x00, 0x00, 0x00
0x08, 0x2B, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 25 | 12 | 0 |
| 5 | 24 | 189 | 32 |
| 6 | 13 | 205 | 17 |
| 8 | 6 | 201 | 22 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 5 | 601 | 60 / 1 | 5 | 0 | trigger_event(602); stop |
| 5 | 602 | 60 / 2 | 5 | 0 | trigger_event(603); stop |
| 5 | 603 | 60 / 3 | 5 | 0 | trigger_event(604); stop |
| 5 | 604 | 60 / 4 | 5 | 0 | trigger_event(605); stop |
| 5 | 605 | 60 / 5 | 5 | 0 | trigger_event(606); stop |
| 5 | 606 | 60 / 6 | 5 | 0 | trigger_event(607); stop |
| 5 | 607 | 60 / 7 | 5 | 0 | trigger_event(608); stop |
| 5 | 608 | 60 / 8 | 5 | 0 | trigger_event(609); stop |
| 5 | 609 | 60 / 9 | 5 | 0 | trigger_event(610); stop |
| 5 | 610 | 60 / 10 | 5 | 0 | trigger_event(611); stop |
| 5 | 611 | 60 / 11 | 6 | 0 | trigger_event(612); stop |
| 5 | 612 | 60 / 12 | 6 | 0 | trigger_event(613); stop |
| 5 | 613 | 60 / 13 | 6 | 0 | trigger_event(614); stop |
| 5 | 614 | 60 / 14 | 6 | 0 | trigger_event(615); stop |
| 5 | 615 | 60 / 15 | 6 | 0 | trigger_event(616); set_switch(10); stop |
| 5 | 616 | 60 / 16 | 6 | 0 | trigger_event(617); stop |
| 5 | 617 | 60 / 17 | 6 | 0 | trigger_event(618); stop |
| 5 | 618 | 60 / 18 | 6 | 0 | trigger_event(619); stop |
| 5 | 619 | 60 / 19 | 6 | 0 | trigger_event(620); stop |
| 5 | 620 | 60 / 20 | 6 | 0 | trigger_event(621); stop |
| 5 | 621 | 60 / 21 | 7 | 0 | trigger_event(622); stop |
| 5 | 622 | 60 / 22 | 7 | 0 | trigger_event(623); stop |
| 5 | 623 | 60 / 23 | 7 | 0 | trigger_event(624); stop |
| 5 | 624 | 60 / 24 | 7 | 0 | trigger_event(625); stop |
| 5 | 625 | 60 / 25 | 7 | 0 | trigger_event(626); stop |
| 5 | 626 | 60 / 26 | 7 | 0 | trigger_event(627); stop |
| 5 | 627 | 60 / 27 | 7 | 0 | trigger_event(628); stop |
| 5 | 628 | 60 / 28 | 7 | 0 | trigger_event(629); stop |
| 5 | 629 | 60 / 29 | 7 | 0 | trigger_event(630); stop |
| 5 | 630 | 60 / 30 | 7 | 0 | trigger_event(640); stop |
| 5 | 640 | 60 / 31 | 4 | 0 | trigger_event(641); stop |
| 5 | 641 | 60 / 32 | 5 | 0 | set_switch(40); stop |
| 6 | 1 | 0 / 0 | 0 | 0 | trigger_event(100); stop |
| 6 | 100 | 100 / 1 | 15 | 50 | trigger_event(101); trigger_event(102); stop |
| 6 | 101 | 100 / 2 | 9 | 50 | stop |
| 6 | 102 | 100 / 3 | 14 | 700 | trigger_event(103); trigger_event(104); set_switch(10); stop |
| 6 | 103 | 100 / 4 | 16 | 50 | stop |
| 6 | 104 | 100 / 5 | 14 | 800 | trigger_event(105); trigger_event(106); trigger_event(107); stop |
| 6 | 105 | 100 / 6 | 10 | 50 | stop |
| 6 | 106 | 100 / 7 | 7 | 700 | trigger_event(108); stop |
| 6 | 107 | 100 / 8 | 11 | 1000 | trigger_event(109); stop |
| 6 | 108 | 100 / 9 | 10 | 50 | stop |
| 6 | 109 | 100 / 10 | 16 | 50 | trigger_event(110); trigger_event(111); stop |
| 6 | 110 | 100 / 11 | 18 | 50 | stop |
| 6 | 111 | 100 / 12 | 17 | 800 | trigger_event(112); stop |
| 6 | 112 | 100 / 13 | 13 | 50 | trigger_event(113); stop |
| 6 | 113 | 100 / 14 | 21 | 60 | trigger_event(114); trigger_event(115); stop |
| 6 | 114 | 100 / 15 | 11 | 50 | stop |
| 6 | 115 | 100 / 16 | 3 | 700 | stop |
| 8 | 101 | 110 / 1 | 10 | 300 | trigger_event(102); trigger_event(203); trigger_event(104); stop |
| 8 | 102 | 110 / 2 | 11 | 50 | trigger_event(105); stop |
| 8 | 203 | 110 / 3 | 10 | 50 | trigger_event(206); stop |
| 8 | 104 | 110 / 4 | 4 | 3000 | stop |
| 8 | 105 | 110 / 5 | 8 | 500 | trigger_event(107); stop |
| 8 | 206 | 110 / 6 | 12 | 500 | trigger_event(208); stop |
| 8 | 107 | 110 / 7 | 4 | 50 | trigger_event(109); trigger_event(110); stop |
| 8 | 208 | 110 / 8 | 7 | 50 | trigger_event(211); stop |
| 8 | 109 | 110 / 9 | 11 | 100 | trigger_event(112); stop |
| 8 | 110 | 110 / 10 | 4 | 1000 | stop |
| 8 | 211 | 110 / 11 | 4 | 100 | trigger_event(213); stop |
| 8 | 112 | 110 / 12 | 8 | 70 | trigger_event(314); stop |
| 8 | 213 | 110 / 13 | 8 | 70 | trigger_event(314); stop |
| 8 | 314 | 110 / 14 | 12 | 400 | trigger_event(315); trigger_event(316); stop |
| 8 | 315 | 110 / 15 | 12 | 100 | stop |
| 8 | 316 | 110 / 16 | 13 | 800 | trigger_event(317); stop |
| 8 | 317 | 110 / 17 | 13 | 50 | trigger_event(318); trigger_event(319); stop |
| 8 | 318 | 110 / 18 | 5 | 50 | stop |
| 8 | 319 | 110 / 19 | 4 | 900 | trigger_event(320); stop |
| 8 | 320 | 110 / 20 | 12 | 60 | trigger_event(321); stop |
| 8 | 321 | 110 / 21 | 10 | 50 | trigger_event(322); stop |
| 8 | 322 | 110 / 22 | 19 | 50 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

A backup is present; decompressed content identical: False. See [text differences](<backup-diff.txt>).

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
