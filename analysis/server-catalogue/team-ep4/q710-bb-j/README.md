# 黄昏る遊具達 — team-ep4/q710-bb-j

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/team-ep4/q710-bb-j.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/team-ep4/q710-bb-j.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/team-ep4/q710-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode4; header quest ID 710; language J. Static scan: **496 objects, 461 enemy/NPC records, 99 events, 316 script labels.** Script roundtrip: byte-identical.

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
0x07, 0x2A, 0x00, 0x00, 0x00
0x08, 0x2B, 0x00, 0x00, 0x00
0x03, 0x26, 0x00, 0x00, 0x00
0x05, 0x28, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 22 | 0 |
| 3 | 149 | 89 | 22 |
| 5 | 33 | 131 | 17 |
| 6 | 90 | 101 | 33 |
| 7 | 136 | 47 | 8 |
| 8 | 62 | 71 | 19 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 3 | 201 | 20 / 1 | 4 | 3 | trigger_event(203); stop |
| 3 | 203 | 20 / 2 | 6 | 3 | set_switch(21); trigger_event(202); stop |
| 3 | 202 | 20 / 4 | 7 | 3 | set_switch(22); stop |
| 3 | 301 | 30 / 99 | 0 | 3 | trigger_event(302); trigger_event(303); stop |
| 3 | 302 | 30 / 1 | 1 | 3 | trigger_event(304); stop |
| 3 | 304 | 30 / 3 | 3 | 3 | trigger_event(305); stop |
| 3 | 305 | 30 / 5 | 4 | 3 | set_switch(32); stop |
| 3 | 303 | 30 / 2 | 2 | 3 | trigger_event(306); stop |
| 3 | 306 | 30 / 4 | 4 | 3 | trigger_event(307); stop |
| 3 | 307 | 30 / 6 | 5 | 3 | set_switch(33); stop |
| 3 | 601 | 60 / 1 | 1 | 3 | trigger_event(602); stop |
| 3 | 602 | 60 / 2 | 1 | 3 | trigger_event(603); stop |
| 3 | 603 | 60 / 3 | 1 | 3 | trigger_event(604); stop |
| 3 | 604 | 60 / 4 | 1 | 3 | trigger_event(605); stop |
| 3 | 605 | 60 / 4 | 1 | 3 | set_switch(63); stop |
| 3 | 606 | 60 / 6 | 3 | 3 | trigger_event(607); stop |
| 3 | 607 | 60 / 7 | 6 | 3 | trigger_event(608); stop |
| 3 | 608 | 60 / 6 | 3 | 3 | set_switch(64); stop |
| 3 | 901 | 90 / 1 | 4 | 3 | trigger_event(902); stop |
| 3 | 902 | 90 / 2 | 6 | 3 | trigger_event(903); stop |
| 3 | 903 | 90 / 3 | 5 | 3 | trigger_event(904); stop |
| 3 | 904 | 90 / 4 | 6 | 3 | set_switch(94); stop |
| 5 | 101 | 10 / 1 | 10 | 3 | trigger_event(102); stop |
| 5 | 102 | 10 / 2 | 8 | 3 | trigger_event(103); stop |
| 5 | 103 | 10 / 3 | 6 | 3 | set_switch(10); stop |
| 5 | 201 | 20 / 1 | 6 | 3 | trigger_event(202); stop |
| 5 | 202 | 20 / 2 | 5 | 3 | trigger_event(203); stop |
| 5 | 203 | 20 / 3 | 9 | 3 | set_switch(20); stop |
| 5 | 301 | 30 / 1 | 10 | 3 | trigger_event(302); stop |
| 5 | 302 | 30 / 2 | 10 | 3 | set_switch(31); stop |
| 5 | 401 | 40 / 1 | 7 | 3 | trigger_event(402); stop |
| 5 | 402 | 40 / 2 | 8 | 3 | trigger_event(403); stop |
| 5 | 403 | 40 / 3 | 8 | 3 | set_switch(43); stop |
| 5 | 501 | 50 / 1 | 7 | 3 | trigger_event(502); stop |
| 5 | 502 | 50 / 2 | 7 | 3 | trigger_event(503); stop |
| 5 | 503 | 50 / 3 | 8 | 3 | set_switch(50); stop |
| 5 | 601 | 60 / 1 | 4 | 3 | trigger_event(602); stop |
| 5 | 602 | 60 / 2 | 7 | 3 | trigger_event(603); stop |
| 5 | 603 | 60 / 3 | 10 | 3 | set_switch(60); stop |
| 6 | 611 | 61 / 1 | 4 | 3 | trigger_event(612); stop |
| 6 | 612 | 61 / 2 | 6 | 3 | set_switch(61); stop |
| 6 | 621 | 62 / 1 | 6 | 3 | trigger_event(622); stop |
| 6 | 622 | 62 / 2 | 6 | 3 | set_switch(62); stop |
| 6 | 901 | 90 / 1 | 6 | 3 | trigger_event(902); stop |
| 6 | 902 | 90 / 2 | 5 | 3 | trigger_event(903); stop |
| 6 | 903 | 90 / 3 | 4 | 3 | trigger_event(904); stop |
| 6 | 904 | 90 / 4 | 6 | 3 | set_switch(90); stop |
| 6 | 1001 | 100 / 1 | 5 | 3 | trigger_event(1002); stop |
| 6 | 1002 | 100 / 2 | 5 | 3 | trigger_event(1003); stop |
| 6 | 1003 | 100 / 3 | 7 | 3 | trigger_event(1004); stop |
| 6 | 1004 | 100 / 4 | 5 | 3 | set_switch(101); stop |
| 6 | 1101 | 110 / 99 | 0 | 3 | trigger_event(1102); trigger_event(1103); trigger_event(1104); stop |
| 6 | 1102 | 110 / 1 | 3 | 3 | trigger_event(1105); stop |
| 6 | 1105 | 110 / 4 | 3 | 3 | set_switch(111); stop |
| 6 | 1103 | 110 / 2 | 3 | 3 | trigger_event(1106); stop |
| 6 | 1106 | 110 / 5 | 2 | 3 | set_switch(112); stop |
| 6 | 1104 | 110 / 3 | 2 | 3 | trigger_event(1107); stop |
| 6 | 1107 | 110 / 6 | 2 | 3 | set_switch(113); stop |
| 6 | 1611 | 161 / 99 | 0 | 30 | trigger_event(1612); trigger_event(1613); stop |
| 6 | 1612 | 161 / 1 | 1 | 3 | trigger_event(1614); stop |
| 6 | 1614 | 161 / 3 | 1 | 3 | trigger_event(1615); stop |
| 6 | 1615 | 161 / 5 | 3 | 3 | set_switch(166); stop |
| 6 | 1613 | 161 / 2 | 1 | 3 | trigger_event(1616); stop |
| 6 | 1616 | 161 / 4 | 1 | 3 | trigger_event(1617); stop |
| 6 | 1617 | 161 / 6 | 3 | 3 | set_switch(163); stop |
| 6 | 1621 | 162 / 99 | 0 | 3 | trigger_event(1622); trigger_event(1623); stop |
| 6 | 1622 | 162 / 1 | 1 | 3 | trigger_event(1624); stop |
| 6 | 1624 | 162 / 3 | 2 | 3 | trigger_event(1625); stop |
| 6 | 1625 | 162 / 5 | 3 | 3 | set_switch(164); stop |
| 6 | 1623 | 162 / 2 | 1 | 3 | trigger_event(1626); stop |
| 6 | 1626 | 162 / 4 | 1 | 3 | trigger_event(1627); stop |
| 6 | 1627 | 162 / 6 | 3 | 3 | set_switch(165); stop |
| 7 | 231 | 23 / 1 | 3 | 3 | trigger_event(232); stop |
| 7 | 232 | 23 / 2 | 3 | 3 | trigger_event(233); stop |
| 7 | 233 | 23 / 3 | 5 | 3 | set_switch(23); set_switch(27); stop |
| 7 | 401 | 40 / 1 | 3 | 3 | trigger_event(402); stop |
| 7 | 402 | 40 / 2 | 5 | 3 | set_switch(40); stop |
| 7 | 501 | 50 / 1 | 3 | 3 | trigger_event(502); stop |
| 7 | 502 | 50 / 2 | 4 | 3 | trigger_event(503); stop |
| 7 | 503 | 50 / 3 | 5 | 3 | set_switch(50); stop |
| 8 | 201 | 20 / 99 | 0 | 3 | trigger_event(202); trigger_event(203); stop |
| 8 | 202 | 20 / 1 | 2 | 3 | trigger_event(204); stop |
| 8 | 204 | 20 / 3 | 4 | 3 | trigger_event(205); stop |
| 8 | 205 | 20 / 5 | 4 | 3 | set_switch(21); stop |
| 8 | 203 | 20 / 2 | 1 | 3 | trigger_event(206); stop |
| 8 | 206 | 20 / 4 | 4 | 3 | trigger_event(207); stop |
| 8 | 207 | 20 / 6 | 4 | 3 | set_switch(22); stop |
| 8 | 601 | 60 / 1 | 6 | 3 | trigger_event(602); stop |
| 8 | 602 | 60 / 2 | 3 | 3 | set_switch(60); stop |
| 8 | 611 | 61 / 1 | 4 | 3 | trigger_event(612); stop |
| 8 | 612 | 61 / 2 | 7 | 3 | trigger_event(613); stop |
| 8 | 613 | 61 / 2 | 7 | 3 | set_switch(61); stop |
| 8 | 701 | 70 / 99 | 0 | 3 | trigger_event(702); trigger_event(703); stop |
| 8 | 702 | 70 / 1 | 6 | 3 | trigger_event(704); stop |
| 8 | 704 | 70 / 3 | 3 | 3 | trigger_event(705); stop |
| 8 | 705 | 70 / 5 | 5 | 3 | set_switch(73); stop |
| 8 | 703 | 70 / 2 | 4 | 3 | trigger_event(706); stop |
| 8 | 706 | 70 / 4 | 4 | 3 | trigger_event(707); stop |
| 8 | 707 | 70 / 6 | 4 | 3 | set_switch(72); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
