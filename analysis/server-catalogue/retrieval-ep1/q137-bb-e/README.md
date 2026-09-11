# Rappy\'s Holiday — retrieval-ep1/q137-bb-e

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/retrieval-ep1/q137-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/retrieval-ep1/q137-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/retrieval-ep1/q137-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 137; language E. Static scan: **351 objects, 247 enemy/NPC records, 75 events, 828 script labels.** Script roundtrip: byte-identical.

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
0x01, 0x01, 0x00, 0x00, 0x04
0x02, 0x02, 0x00, 0x00, 0x02
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 28 | 19 | 0 |
| 1 | 160 | 91 | 17 |
| 2 | 163 | 137 | 58 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 11 | 1 / 1 | 11 | 0 | stop |
| 1 | 41 | 4 / 1 | 3 | 0 | stop |
| 1 | 51 | 5 / 1 | 4 | 0 | stop |
| 1 | 71 | 7 / 1 | 18 | 0 | stop |
| 1 | 101 | 10 / 1 | 7 | 0 | stop |
| 1 | 111 | 11 / 1 | 6 | 0 | stop |
| 1 | 161 | 16 / 1 | 7 | 0 | stop |
| 1 | 52 | 5 / 2 | 4 | 0 | trigger_event(521); stop |
| 1 | 521 | 5 / 3 | 3 | 0 | trigger_event(522); stop |
| 1 | 522 | 5 / 4 | 3 | 0 | trigger_event(523); stop |
| 1 | 523 | 5 / 5 | 6 | 0 | trigger_event(524); stop |
| 1 | 524 | 5 / 6 | 3 | 0 | trigger_event(525); stop |
| 1 | 525 | 5 / 7 | 3 | 0 | trigger_event(528); stop |
| 1 | 527 | 5 / 9 | 4 | 0 | stop |
| 1 | 528 | 5 / 10 | 4 | 0 | trigger_event(529); stop |
| 1 | 529 | 5 / 11 | 4 | 0 | trigger_event(5291); stop |
| 1 | 5291 | 5 / 12 | 0 | 0 | set_switch(101); stop |
| 2 | 21 | 2 / 1 | 6 | 0 | trigger_event(211); trigger_event(212); stop |
| 2 | 211 | 2 / 2 | 1 | 0 | stop |
| 2 | 212 | 2 / 3 | 2 | 0 | trigger_event(213); stop |
| 2 | 213 | 2 / 4 | 2 | 0 | trigger_event(214); stop |
| 2 | 214 | 2 / 5 | 1 | 0 | trigger_event(216); stop |
| 2 | 215 | 2 / 6 | 3 | 0 | set_switch(4); set_switch(61); stop |
| 2 | 216 | 2 / 7 | 2 | 0 | trigger_event(217); stop |
| 2 | 217 | 2 / 8 | 2 | 0 | trigger_event(215); stop |
| 2 | 31 | 3 / 1 | 6 | 0 | stop |
| 2 | 41 | 4 / 1 | 3 | 0 | stop |
| 2 | 43 | 4 / 2 | 1 | 45 | set_switch(172); stop |
| 2 | 42 | 4 / 3 | 1 | 15 | set_switch(173); stop |
| 2 | 44 | 4 / 4 | 1 | 0 | trigger_event(423); stop |
| 2 | 423 | 4 / 5 | 1 | 120 | trigger_event(424); stop |
| 2 | 424 | 4 / 6 | 3 | 0 | trigger_event(425); stop |
| 2 | 425 | 4 / 7 | 2 | 0 | trigger_event(426); stop |
| 2 | 426 | 4 / 8 | 1 | 0 | trigger_event(427); stop |
| 2 | 427 | 4 / 9 | 3 | 60 | trigger_event(428); stop |
| 2 | 428 | 4 / 10 | 3 | 0 | trigger_event(429); stop |
| 2 | 429 | 4 / 11 | 3 | 0 | trigger_event(4291); stop |
| 2 | 4291 | 4 / 12 | 3 | 0 | set_switch(171); stop |
| 2 | 61 | 6 / 1 | 1 | 0 | stop |
| 2 | 61 | 6 / 2 | 2 | 0 | trigger_event(612); stop |
| 2 | 612 | 6 / 3 | 2 | 0 | trigger_event(613); stop |
| 2 | 613 | 6 / 4 | 1 | 0 | trigger_event(614); trigger_event(616); stop |
| 2 | 614 | 6 / 5 | 2 | 0 | trigger_event(615); stop |
| 2 | 615 | 6 / 6 | 2 | 0 | stop |
| 2 | 616 | 6 / 7 | 1 | 0 | trigger_event(617); stop |
| 2 | 617 | 6 / 8 | 2 | 0 | trigger_event(618); stop |
| 2 | 618 | 6 / 9 | 2 | 0 | set_switch(9); set_switch(62); stop |
| 2 | 81 | 8 / 1 | 1 | 0 | stop |
| 2 | 91 | 9 / 1 | 1 | 0 | stop |
| 2 | 101 | 10 / 1 | 4 | 0 | trigger_event(1011); stop |
| 2 | 1011 | 10 / 2 | 3 | 0 | set_switch(37); trigger_event(1521); stop |
| 2 | 1521 | 15 / 4 | 2 | 0 | trigger_event(1522); stop |
| 2 | 1522 | 15 / 5 | 3 | 0 | trigger_event(1231); stop |
| 2 | 1231 | 12 / 5 | 3 | 0 | stop |
| 2 | 102 | 10 / 3 | 1 | 0 | stop |
| 2 | 111 | 11 / 1 | 6 | 0 | trigger_event(1111); stop |
| 2 | 1111 | 11 / 2 | 3 | 0 | trigger_event(1112); stop |
| 2 | 1112 | 11 / 3 | 3 | 0 | set_switch(6); set_switch(7); set_switch(8); stop |
| 2 | 121 | 12 / 1 | 3 | 0 | trigger_event(1211); stop |
| 2 | 1211 | 12 / 2 | 3 | 0 | trigger_event(1212); stop |
| 2 | 1212 | 12 / 3 | 3 | 0 | set_switch(175); stop |
| 2 | 122 | 12 / 4 | 3 | 0 | set_switch(176); stop |
| 2 | 131 | 13 / 1 | 1 | 0 | trigger_event(1311); stop |
| 2 | 1311 | 13 / 2 | 2 | 0 | trigger_event(1312); stop |
| 2 | 1312 | 13 / 3 | 2 | 0 | trigger_event(1313); stop |
| 2 | 1313 | 13 / 4 | 3 | 0 | trigger_event(1314); stop |
| 2 | 1314 | 13 / 5 | 1 | 0 | trigger_event(1315); stop |
| 2 | 1315 | 13 / 6 | 2 | 0 | trigger_event(1316); stop |
| 2 | 1316 | 13 / 7 | 3 | 0 | trigger_event(1317); stop |
| 2 | 1317 | 13 / 8 | 1 | 0 | trigger_event(1318); stop |
| 2 | 1318 | 13 / 9 | 2 | 0 | set_switch(50); set_switch(56); stop |
| 2 | 151 | 15 / 1 | 3 | 0 | trigger_event(1511); stop |
| 2 | 1511 | 15 / 2 | 3 | 0 | trigger_event(1512); stop |
| 2 | 1512 | 15 / 3 | 6 | 0 | set_switch(30); trigger_event(1513); stop |
| 2 | 161 | 16 / 1 | 1 | 0 | stop |

## Review notes

- Floor 2: event 1512 targets absent event 1513

A backup is present; decompressed content identical: True. See [text differences](<backup-diff.txt>).

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
