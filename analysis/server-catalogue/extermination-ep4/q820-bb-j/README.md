# 新掃討作戦 第五号 — extermination-ep4/q820-bb-j

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/extermination-ep4/q820-bb-j.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/extermination-ep4/q820-bb-j.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/extermination-ep4/q820-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode4; header quest ID 820; language J. Static scan: **225 objects, 228 enemy/NPC records, 50 events, 149 script labels.** Script roundtrip: byte-identical.

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
0x08, 0x2B, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 17 | 0 |
| 8 | 199 | 211 | 50 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 8 | 201 | 20 / 99 | 0 | 3 | trigger_event(202); trigger_event(203); trigger_event(204); stop |
| 8 | 202 | 20 / 1 | 1 | 3 | trigger_event(205); stop |
| 8 | 203 | 20 / 2 | 1 | 3 | trigger_event(206); stop |
| 8 | 204 | 20 / 3 | 1 | 3 | trigger_event(207); stop |
| 8 | 205 | 20 / 4 | 2 | 3 | trigger_event(208); stop |
| 8 | 206 | 20 / 5 | 3 | 3 | trigger_event(209); stop |
| 8 | 207 | 20 / 6 | 3 | 3 | trigger_event(2010); stop |
| 8 | 208 | 20 / 7 | 3 | 3 | set_switch(22); stop |
| 8 | 209 | 20 / 8 | 1 | 3 | set_switch(23); stop |
| 8 | 2010 | 20 / 9 | 2 | 3 | set_switch(24); stop |
| 8 | 211 | 21 / 1 | 1 | 3 | trigger_event(212); stop |
| 8 | 212 | 21 / 2 | 8 | 3 | trigger_event(213); stop |
| 8 | 213 | 21 / 3 | 6 | 3 | set_switch(21); stop |
| 8 | 401 | 40 / 1 | 6 | 3 | trigger_event(402); stop |
| 8 | 402 | 40 / 2 | 7 | 3 | trigger_event(403); stop |
| 8 | 403 | 40 / 3 | 6 | 3 | set_switch(40); stop |
| 8 | 411 | 41 / 1 | 5 | 3 | trigger_event(412); stop |
| 8 | 412 | 41 / 2 | 5 | 3 | trigger_event(413); stop |
| 8 | 413 | 41 / 3 | 7 | 3 | set_switch(41); stop |
| 8 | 421 | 42 / 1 | 4 | 3 | trigger_event(422); stop |
| 8 | 422 | 42 / 2 | 6 | 3 | trigger_event(423); stop |
| 8 | 423 | 42 / 3 | 6 | 3 | set_switch(42); stop |
| 8 | 501 | 50 / 1 | 6 | 3 | trigger_event(502); stop |
| 8 | 502 | 50 / 2 | 1 | 3 | trigger_event(503); stop |
| 8 | 503 | 50 / 3 | 6 | 3 | set_switch(50); stop |
| 8 | 511 | 51 / 1 | 11 | 3 | trigger_event(512); stop |
| 8 | 512 | 51 / 2 | 8 | 3 | trigger_event(513); stop |
| 8 | 513 | 51 / 3 | 8 | 3 | set_switch(51); stop |
| 8 | 601 | 60 / 1 | 4 | 3 | trigger_event(602); stop |
| 8 | 602 | 60 / 2 | 5 | 3 | trigger_event(603); stop |
| 8 | 603 | 60 / 3 | 4 | 3 | set_switch(60); stop |
| 8 | 611 | 61 / 1 | 4 | 3 | trigger_event(612); stop |
| 8 | 612 | 61 / 2 | 5 | 3 | trigger_event(613); stop |
| 8 | 613 | 61 / 3 | 6 | 3 | set_switch(61); stop |
| 8 | 701 | 70 / 99 | 0 | 3 | trigger_event(702); trigger_event(703); trigger_event(704); stop |
| 8 | 702 | 70 / 1 | 3 | 3 | trigger_event(705); stop |
| 8 | 703 | 70 / 2 | 3 | 3 | trigger_event(706); stop |
| 8 | 704 | 70 / 3 | 1 | 3 | trigger_event(707); stop |
| 8 | 705 | 70 / 4 | 3 | 3 | trigger_event(708); stop |
| 8 | 706 | 70 / 5 | 2 | 3 | trigger_event(709); stop |
| 8 | 707 | 70 / 6 | 3 | 3 | trigger_event(7010); stop |
| 8 | 708 | 70 / 7 | 5 | 3 | set_switch(71); stop |
| 8 | 709 | 70 / 8 | 3 | 3 | set_switch(72); stop |
| 8 | 7010 | 70 / 9 | 5 | 3 | set_switch(73); stop |
| 8 | 801 | 80 / 1 | 4 | 3 | set_switch(81); stop |
| 8 | 802 | 80 / 2 | 4 | 3 | set_switch(82); stop |
| 8 | 803 | 80 / 3 | 5 | 3 | set_switch(83); stop |
| 8 | 1001 | 100 / 1 | 7 | 3 | trigger_event(1002); stop |
| 8 | 1002 | 100 / 2 | 6 | 3 | trigger_event(1003); stop |
| 8 | 1003 | 100 / 3 | 5 | 3 | set_switch(100); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
