# MAXIMUM ATTACK 3 Ver2 — maximum-attack-ep4/q314-bb-e

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/maximum-attack-ep4/q314-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/maximum-attack-ep4/q314-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/maximum-attack-ep4/q314-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode4; header quest ID 314; language E. Static scan: **807 objects, 921 enemy/NPC records, 189 events, 354 script labels.** Script roundtrip: byte-identical.

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
0x02, 0x25, 0x00, 0x00, 0x00
0x05, 0x28, 0x00, 0x00, 0x00
0x06, 0x29, 0x00, 0x02, 0x00
0x07, 0x2A, 0x00, 0x00, 0x00
0x08, 0x2B, 0x00, 0x01, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 54 | 21 | 0 |
| 2 | 193 | 241 | 59 |
| 5 | 169 | 129 | 20 |
| 6 | 115 | 148 | 34 |
| 7 | 146 | 209 | 43 |
| 8 | 130 | 173 | 33 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 2 | 101 | 10 / 1 | 5 | 30 | trigger_event(102); stop |
| 2 | 102 | 10 / 2 | 6 | 30 | trigger_event(103); stop |
| 2 | 103 | 10 / 3 | 8 | 30 | set_switch(10); stop |
| 2 | 111 | 11 / 1 | 2 | 30 | trigger_event(112); stop |
| 2 | 112 | 11 / 2 | 5 | 30 | trigger_event(113); stop |
| 2 | 113 | 11 / 3 | 6 | 30 | set_switch(11); set_switch(12); stop |
| 2 | 201 | 20 / 99 | 0 | 30 | trigger_event(2011); trigger_event(2021); stop |
| 2 | 2011 | 20 / 1 | 4 | 30 | trigger_event(2012); stop |
| 2 | 2012 | 20 / 2 | 4 | 30 | trigger_event(2013); stop |
| 2 | 2013 | 20 / 3 | 4 | 30 | set_switch(24); stop |
| 2 | 2021 | 20 / 4 | 2 | 30 | trigger_event(2022); stop |
| 2 | 2022 | 20 / 5 | 4 | 30 | trigger_event(2023); stop |
| 2 | 2023 | 20 / 6 | 4 | 30 | trigger_event(2024); stop |
| 2 | 2024 | 20 / 7 | 6 | 30 | set_switch(25); stop |
| 2 | 301 | 30 / 1 | 4 | 30 | trigger_event(302); stop |
| 2 | 302 | 30 / 2 | 6 | 30 | set_switch(31); stop |
| 2 | 303 | 30 / 99 | 0 | 30 | trigger_event(3011); trigger_event(3021); trigger_event(3031); stop |
| 2 | 3011 | 30 / 3 | 1 | 30 | trigger_event(3012); stop |
| 2 | 3012 | 30 / 4 | 2 | 30 | trigger_event(3013); stop |
| 2 | 3013 | 30 / 5 | 1 | 30 | trigger_event(3014); stop |
| 2 | 3014 | 30 / 6 | 2 | 30 | trigger_event(3015); stop |
| 2 | 3015 | 30 / 7 | 3 | 30 | set_switch(33); stop |
| 2 | 3021 | 30 / 8 | 1 | 30 | trigger_event(3022); stop |
| 2 | 3022 | 30 / 9 | 1 | 30 | trigger_event(3023); stop |
| 2 | 3023 | 30 / 10 | 1 | 30 | trigger_event(3024); stop |
| 2 | 3024 | 30 / 11 | 1 | 30 | trigger_event(3025); stop |
| 2 | 3025 | 30 / 12 | 3 | 30 | set_switch(34); stop |
| 2 | 3031 | 30 / 13 | 1 | 30 | trigger_event(3032); stop |
| 2 | 3032 | 30 / 14 | 1 | 30 | trigger_event(3033); stop |
| 2 | 3033 | 30 / 15 | 1 | 30 | trigger_event(3034); stop |
| 2 | 3034 | 30 / 16 | 3 | 30 | trigger_event(3035); stop |
| 2 | 3035 | 30 / 17 | 1 | 30 | set_switch(35); stop |
| 2 | 401 | 40 / 1 | 5 | 30 | trigger_event(402); stop |
| 2 | 402 | 40 / 2 | 5 | 30 | trigger_event(403); stop |
| 2 | 403 | 40 / 3 | 6 | 30 | set_switch(40); stop |
| 2 | 404 | 40 / 4 | 6 | 30 | trigger_event(405); stop |
| 2 | 405 | 40 / 5 | 6 | 30 | trigger_event(406); stop |
| 2 | 406 | 40 / 6 | 7 | 30 | set_switch(42); stop |
| 2 | 411 | 41 / 1 | 5 | 30 | trigger_event(412); stop |
| 2 | 412 | 41 / 2 | 6 | 30 | trigger_event(413); stop |
| 2 | 413 | 41 / 3 | 6 | 30 | set_switch(41); set_switch(54); stop |
| 2 | 414 | 41 / 4 | 5 | 30 | trigger_event(415); stop |
| 2 | 415 | 41 / 5 | 5 | 30 | trigger_event(416); stop |
| 2 | 416 | 41 / 6 | 6 | 30 | set_switch(43); stop |
| 2 | 501 | 50 / 1 | 6 | 30 | trigger_event(502); stop |
| 2 | 502 | 50 / 2 | 6 | 30 | trigger_event(503); stop |
| 2 | 503 | 50 / 3 | 7 | 30 | set_switch(51); set_switch(53); set_switch(12); stop |
| 2 | 504 | 50 / 4 | 5 | 30 | trigger_event(505); stop |
| 2 | 505 | 50 / 5 | 5 | 30 | set_switch(52); set_switch(53); set_switch(54); stop |
| 2 | 601 | 60 / 1 | 3 | 30 | trigger_event(602); stop |
| 2 | 602 | 60 / 2 | 5 | 30 | trigger_event(603); stop |
| 2 | 603 | 60 / 3 | 5 | 30 | trigger_event(604); stop |
| 2 | 604 | 60 / 4 | 8 | 30 | set_switch(60); stop |
| 2 | 610 | 60 / 4 | 8 | 30 | trigger_event(605); stop |
| 2 | 605 | 60 / 5 | 6 | 30 | trigger_event(606); stop |
| 2 | 606 | 60 / 6 | 6 | 30 | stop |
| 2 | 801 | 80 / 1 | 3 | 30 | trigger_event(802); stop |
| 2 | 802 | 80 / 2 | 6 | 30 | trigger_event(803); stop |
| 2 | 803 | 80 / 3 | 3 | 30 | set_switch(80); set_switch(52); set_switch(54); stop |
| 5 | 101 | 10 / 1 | 3 | 30 | trigger_event(102); stop |
| 5 | 102 | 10 / 2 | 5 | 30 | trigger_event(103); stop |
| 5 | 103 | 10 / 3 | 7 | 30 | set_switch(10); stop |
| 5 | 201 | 20 / 1 | 8 | 30 | trigger_event(202); stop |
| 5 | 202 | 20 / 2 | 7 | 30 | trigger_event(203); stop |
| 5 | 203 | 20 / 3 | 8 | 30 | trigger_event(204); stop |
| 5 | 204 | 20 / 4 | 9 | 30 | set_switch(20); stop |
| 5 | 301 | 30 / 1 | 6 | 30 | construct_objects(room=30,group_or_wave=1); stop |
| 5 | 306 | 30 / 2 | 5 | 30 | trigger_event(307); stop |
| 5 | 307 | 30 / 3 | 5 | 30 | set_switch(30); stop |
| 5 | 401 | 40 / 1 | 6 | 30 | trigger_event(402); stop |
| 5 | 402 | 40 / 2 | 7 | 30 | trigger_event(403); stop |
| 5 | 403 | 40 / 3 | 7 | 30 | trigger_event(404); stop |
| 5 | 404 | 40 / 4 | 8 | 30 | trigger_event(405); stop |
| 5 | 405 | 40 / 5 | 5 | 30 | set_switch(40); stop |
| 5 | 601 | 60 / 1 | 6 | 30 | trigger_event(602); stop |
| 5 | 602 | 60 / 2 | 8 | 30 | trigger_event(603); stop |
| 5 | 603 | 60 / 3 | 8 | 30 | set_switch(60); construct_objects(room=60,group_or_wave=1); stop |
| 5 | 604 | 60 / 4 | 8 | 30 | trigger_event(605); stop |
| 5 | 605 | 60 / 5 | 3 | 30 | construct_objects(room=60,group_or_wave=2); stop |
| 6 | 201 | 20 / 1 | 3 | 30 | trigger_event(202); stop |
| 6 | 202 | 20 / 2 | 5 | 30 | trigger_event(203); stop |
| 6 | 203 | 20 / 3 | 5 | 30 | set_switch(20); stop |
| 6 | 311 | 31 / 1 | 1 | 30 | set_switch(31); stop |
| 6 | 321 | 32 / 1 | 3 | 30 | set_switch(32); stop |
| 6 | 501 | 50 / 1 | 4 | 30 | trigger_event(502); stop |
| 6 | 502 | 50 / 2 | 5 | 30 | trigger_event(503); stop |
| 6 | 503 | 50 / 3 | 5 | 30 | set_switch(50); stop |
| 6 | 601 | 60 / 1 | 3 | 30 | trigger_event(602); stop |
| 6 | 602 | 60 / 2 | 5 | 30 | set_switch(60); stop |
| 6 | 611 | 61 / 1 | 4 | 30 | trigger_event(612); stop |
| 6 | 612 | 61 / 2 | 5 | 30 | set_switch(61); stop |
| 6 | 621 | 62 / 1 | 4 | 30 | trigger_event(622); stop |
| 6 | 622 | 62 / 2 | 4 | 30 | trigger_event(623); stop |
| 6 | 623 | 62 / 3 | 4 | 30 | set_switch(62); set_switch(71); stop |
| 6 | 631 | 63 / 1 | 1 | 30 | trigger_event(632); stop |
| 6 | 632 | 63 / 2 | 5 | 30 | set_switch(63); stop |
| 6 | 641 | 64 / 1 | 1 | 30 | trigger_event(642); stop |
| 6 | 642 | 64 / 2 | 5 | 30 | trigger_event(643); stop |
| 6 | 643 | 64 / 3 | 2 | 30 | set_switch(64); stop |
| 6 | 701 | 70 / 1 | 4 | 30 | trigger_event(702); stop |
| 6 | 702 | 70 / 2 | 5 | 30 | trigger_event(703); stop |
| 6 | 703 | 70 / 3 | 5 | 30 | set_switch(70); stop |
| 6 | 901 | 90 / 1 | 5 | 30 | trigger_event(902); stop |
| 6 | 902 | 90 / 2 | 5 | 30 | trigger_event(903); stop |
| 6 | 903 | 90 / 3 | 6 | 30 | set_switch(90); stop |
| 6 | 1001 | 100 / 1 | 4 | 30 | trigger_event(1002); stop |
| 6 | 1002 | 100 / 2 | 4 | 30 | trigger_event(1003); stop |
| 6 | 1003 | 100 / 3 | 5 | 30 | trigger_event(1004); stop |
| 6 | 1004 | 100 / 4 | 5 | 30 | trigger_event(1005); stop |
| 6 | 1005 | 100 / 5 | 6 | 30 | set_switch(100); stop |
| 6 | 1101 | 110 / 1 | 6 | 30 | trigger_event(1102); stop |
| 6 | 1102 | 110 / 2 | 7 | 30 | trigger_event(1103); stop |
| 6 | 1103 | 110 / 3 | 7 | 30 | set_switch(110); stop |
| 7 | 101 | 10 / 99 | 0 | 30 | trigger_event(1001); trigger_event(1002); trigger_event(1003); trigger_event(1004); stop |
| 7 | 1001 | 10 / 1 | 2 | 30 | trigger_event(105); stop |
| 7 | 1002 | 10 / 2 | 1 | 30 | trigger_event(106); stop |
| 7 | 1003 | 10 / 3 | 2 | 30 | trigger_event(107); stop |
| 7 | 1004 | 10 / 4 | 1 | 30 | trigger_event(108); stop |
| 7 | 105 | 10 / 5 | 2 | 30 | trigger_event(109); stop |
| 7 | 106 | 10 / 6 | 2 | 30 | trigger_event(1010); stop |
| 7 | 107 | 10 / 7 | 3 | 30 | trigger_event(1011); stop |
| 7 | 108 | 10 / 8 | 2 | 30 | trigger_event(1012); stop |
| 7 | 109 | 10 / 9 | 3 | 30 | set_switch(15); stop |
| 7 | 1010 | 10 / 10 | 3 | 30 | set_switch(16); stop |
| 7 | 1011 | 10 / 11 | 3 | 30 | set_switch(17); stop |
| 7 | 1012 | 10 / 12 | 2 | 30 | set_switch(18); stop |
| 7 | 211 | 21 / 1 | 5 | 30 | trigger_event(212); stop |
| 7 | 212 | 21 / 2 | 5 | 30 | trigger_event(213); stop |
| 7 | 213 | 21 / 3 | 8 | 30 | set_switch(21); stop |
| 7 | 221 | 22 / 1 | 5 | 30 | trigger_event(222); stop |
| 7 | 222 | 22 / 2 | 6 | 30 | trigger_event(223); stop |
| 7 | 223 | 22 / 3 | 6 | 30 | set_switch(22); stop |
| 7 | 231 | 23 / 1 | 5 | 30 | trigger_event(232); stop |
| 7 | 232 | 23 / 2 | 6 | 30 | trigger_event(233); stop |
| 7 | 233 | 23 / 3 | 7 | 30 | set_switch(23); stop |
| 7 | 241 | 24 / 1 | 5 | 30 | trigger_event(242); stop |
| 7 | 242 | 24 / 2 | 6 | 30 | trigger_event(243); stop |
| 7 | 243 | 24 / 3 | 6 | 30 | set_switch(24); stop |
| 7 | 251 | 25 / 1 | 6 | 30 | trigger_event(252); stop |
| 7 | 252 | 25 / 2 | 8 | 30 | trigger_event(253); stop |
| 7 | 253 | 25 / 3 | 8 | 30 | set_switch(25); stop |
| 7 | 271 | 27 / 1 | 6 | 30 | trigger_event(272); stop |
| 7 | 272 | 27 / 3 | 6 | 30 | trigger_event(273); stop |
| 7 | 273 | 27 / 3 | 6 | 30 | set_switch(27); stop |
| 7 | 401 | 40 / 1 | 6 | 30 | trigger_event(402); stop |
| 7 | 402 | 40 / 2 | 6 | 30 | trigger_event(403); stop |
| 7 | 403 | 40 / 3 | 6 | 30 | set_switch(40); stop |
| 7 | 411 | 41 / 1 | 6 | 30 | trigger_event(412); stop |
| 7 | 412 | 41 / 2 | 6 | 30 | trigger_event(413); stop |
| 7 | 413 | 41 / 3 | 7 | 30 | set_switch(41); stop |
| 7 | 421 | 42 / 1 | 6 | 30 | trigger_event(422); stop |
| 7 | 422 | 42 / 2 | 6 | 30 | trigger_event(423); stop |
| 7 | 423 | 42 / 3 | 6 | 30 | set_switch(42); stop |
| 7 | 501 | 50 / 1 | 5 | 30 | trigger_event(502); stop |
| 7 | 502 | 50 / 2 | 6 | 30 | trigger_event(503); stop |
| 7 | 503 | 50 / 3 | 7 | 30 | set_switch(50); stop |
| 8 | 201 | 20 / 1 | 4 | 30 | trigger_event(202); stop |
| 8 | 202 | 20 / 2 | 8 | 30 | trigger_event(203); stop |
| 8 | 203 | 20 / 3 | 3 | 30 | set_switch(20); stop |
| 8 | 401 | 40 / 1 | 3 | 30 | trigger_event(402); stop |
| 8 | 402 | 40 / 2 | 6 | 30 | set_switch(40); stop |
| 8 | 411 | 41 / 1 | 5 | 30 | trigger_event(412); stop |
| 8 | 412 | 41 / 2 | 6 | 30 | set_switch(41); stop |
| 8 | 501 | 50 / 1 | 4 | 30 | trigger_event(502); stop |
| 8 | 502 | 50 / 2 | 4 | 30 | trigger_event(503); stop |
| 8 | 503 | 50 / 3 | 5 | 30 | set_switch(50); stop |
| 8 | 511 | 51 / 1 | 6 | 30 | trigger_event(512); stop |
| 8 | 512 | 51 / 2 | 4 | 30 | trigger_event(513); stop |
| 8 | 513 | 51 / 3 | 4 | 30 | set_switch(51); stop |
| 8 | 601 | 60 / 1 | 6 | 30 | trigger_event(602); stop |
| 8 | 602 | 60 / 2 | 5 | 30 | set_switch(60); construct_objects(room=60,group_or_wave=1); stop |
| 8 | 701 | 70 / 1 | 6 | 30 | trigger_event(702); stop |
| 8 | 702 | 70 / 2 | 6 | 30 | trigger_event(703); stop |
| 8 | 703 | 70 / 3 | 8 | 30 | set_switch(70); stop |
| 8 | 801 | 80 / 1 | 3 | 30 | construct_objects(room=80,group_or_wave=1); stop |
| 8 | 802 | 80 / 2 | 2 | 30 | construct_objects(room=80,group_or_wave=2); stop |
| 8 | 803 | 80 / 3 | 4 | 30 | set_switch(80); stop |
| 8 | 1001 | 100 / 1 | 6 | 30 | trigger_event(1002); stop |
| 8 | 1002 | 100 / 2 | 6 | 30 | trigger_event(1003); stop |
| 8 | 1003 | 100 / 3 | 6 | 30 | set_switch(100); stop |
| 8 | 1011 | 101 / 1 | 6 | 30 | trigger_event(1012); stop |
| 8 | 1012 | 101 / 2 | 4 | 30 | trigger_event(1013); stop |
| 8 | 1013 | 101 / 3 | 6 | 30 | set_switch(101); stop |
| 8 | 1101 | 110 / 1 | 2 | 30 | trigger_event(1102); stop |
| 8 | 1102 | 110 / 2 | 8 | 30 | trigger_event(1103); stop |
| 8 | 1103 | 110 / 3 | 8 | 30 | trigger_event(1104); stop |
| 8 | 1104 | 110 / 4 | 8 | 30 | trigger_event(1105); stop |
| 8 | 1105 | 110 / 5 | 6 | 30 | trigger_event(1106); stop |
| 8 | 1106 | 110 / 6 | 5 | 90 | set_switch(111); set_switch(112); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
