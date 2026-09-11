# 荒野の果てに — solo-extra-ep1/q036-bb-j

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/solo-extra-ep1/q036-bb-j.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/solo-extra-ep1/q036-bb-j.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/solo-extra-ep1/q036-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode4; header quest ID 36; language J. Static scan: **479 objects, 342 enemy/NPC records, 86 events, 378 script labels.** Script roundtrip: byte-identical.

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
0x01, 0x24, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 23 | 0 |
| 1 | 243 | 157 | 43 |
| 2 | 210 | 162 | 43 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 301 | 30 / 1 | 3 | 3 | trigger_event(302); stop |
| 1 | 302 | 30 / 2 | 3 | 3 | trigger_event(303); stop |
| 1 | 303 | 30 / 3 | 4 | 3 | trigger_event(304); stop |
| 1 | 304 | 30 / 4 | 4 | 3 | set_switch(30); trigger_event(305); stop |
| 1 | 305 | 30 / 5 | 5 | 3 | trigger_event(306); stop |
| 1 | 306 | 30 / 6 | 4 | 3 | set_switch(31); set_switch(32); stop |
| 1 | 201 | 20 / 1 | 4 | 3 | trigger_event(202); stop |
| 1 | 202 | 20 / 2 | 3 | 3 | set_switch(21); set_switch(22); trigger_event(203); stop |
| 1 | 203 | 20 / 3 | 4 | 3 | set_switch(20); trigger_event(204); stop |
| 1 | 204 | 20 / 4 | 3 | 3 | trigger_event(205); stop |
| 1 | 205 | 20 / 5 | 3 | 3 | set_switch(23); trigger_event(206); stop |
| 1 | 206 | 20 / 6 | 4 | 3 | trigger_event(207); stop |
| 1 | 207 | 20 / 7 | 4 | 3 | trigger_event(208); stop |
| 1 | 208 | 20 / 8 | 4 | 3 | set_switch(24); set_switch(25); stop |
| 1 | 101 | 10 / 1 | 4 | 3 | trigger_event(102); stop |
| 1 | 102 | 10 / 2 | 4 | 3 | trigger_event(103); stop |
| 1 | 103 | 10 / 3 | 3 | 3 | set_switch(10); set_switch(11); set_switch(12); stop |
| 1 | 501 | 50 / 1 | 3 | 3 | trigger_event(502); stop |
| 1 | 502 | 50 / 2 | 4 | 3 | trigger_event(503); stop |
| 1 | 503 | 50 / 3 | 4 | 3 | trigger_event(504); stop |
| 1 | 504 | 50 / 4 | 3 | 3 | trigger_event(505); stop |
| 1 | 505 | 50 / 5 | 4 | 3 | set_switch(50); set_switch(51); trigger_event(506); stop |
| 1 | 506 | 50 / 6 | 3 | 3 | set_switch(52); trigger_event(507); stop |
| 1 | 507 | 50 / 7 | 3 | 3 | trigger_event(508); stop |
| 1 | 508 | 50 / 8 | 3 | 3 | set_switch(53); stop |
| 1 | 601 | 60 / 1 | 4 | 3 | trigger_event(602); stop |
| 1 | 602 | 60 / 2 | 4 | 3 | trigger_event(603); stop |
| 1 | 603 | 60 / 3 | 3 | 3 | set_switch(60); set_switch(62); set_switch(63); stop |
| 1 | 111 | 11 / 1 | 4 | 3 | trigger_event(112); stop |
| 1 | 112 | 11 / 2 | 4 | 3 | trigger_event(113); stop |
| 1 | 113 | 11 / 3 | 4 | 3 | set_switch(110); set_switch(111); set_switch(112); stop |
| 1 | 401 | 40 / 1 | 3 | 3 | trigger_event(402); stop |
| 1 | 402 | 40 / 2 | 4 | 3 | trigger_event(403); stop |
| 1 | 403 | 40 / 3 | 4 | 3 | set_switch(40); set_switch(41); set_switch(42); set_switch(43); stop |
| 1 | 211 | 21 / 1 | 3 | 3 | trigger_event(212); stop |
| 1 | 212 | 21 / 2 | 4 | 3 | set_switch(210); set_switch(211); trigger_event(213); stop |
| 1 | 213 | 21 / 3 | 7 | 3 | trigger_event(214); stop |
| 1 | 214 | 21 / 4 | 3 | 3 | trigger_event(215); stop |
| 1 | 215 | 21 / 5 | 4 | 3 | trigger_event(216); stop |
| 1 | 216 | 21 / 6 | 3 | 3 | set_switch(212); set_switch(213); set_switch(214); stop |
| 1 | 801 | 80 / 1 | 3 | 3 | trigger_event(802); stop |
| 1 | 802 | 80 / 2 | 3 | 3 | trigger_event(803); stop |
| 1 | 803 | 80 / 3 | 3 | 3 | set_switch(80); set_switch(81); stop |
| 2 | 101 | 10 / 1 | 3 | 3 | trigger_event(102); stop |
| 2 | 102 | 10 / 2 | 3 | 3 | trigger_event(103); stop |
| 2 | 103 | 10 / 3 | 3 | 3 | set_switch(10); set_switch(11); set_switch(12); stop |
| 2 | 401 | 40 / 1 | 3 | 3 | trigger_event(402); stop |
| 2 | 402 | 40 / 2 | 4 | 3 | set_switch(40); set_switch(41); trigger_event(403); stop |
| 2 | 403 | 40 / 3 | 4 | 3 | trigger_event(404); stop |
| 2 | 404 | 40 / 4 | 4 | 3 | set_switch(42); stop |
| 2 | 201 | 20 / 1 | 4 | 3 | trigger_event(202); stop |
| 2 | 202 | 20 / 2 | 4 | 3 | trigger_event(203); stop |
| 2 | 203 | 20 / 3 | 4 | 3 | set_switch(20); set_switch(21); trigger_event(204); stop |
| 2 | 204 | 20 / 4 | 3 | 3 | trigger_event(205); stop |
| 2 | 205 | 20 / 5 | 4 | 3 | trigger_event(206); stop |
| 2 | 206 | 20 / 6 | 4 | 3 | set_switch(22); set_switch(23); stop |
| 2 | 411 | 41 / 1 | 3 | 3 | trigger_event(412); stop |
| 2 | 412 | 41 / 2 | 4 | 3 | set_switch(43); set_switch(44); trigger_event(413); stop |
| 2 | 413 | 41 / 3 | 3 | 3 | trigger_event(414); stop |
| 2 | 414 | 41 / 4 | 5 | 3 | set_switch(45); set_switch(46); stop |
| 2 | 301 | 30 / 1 | 5 | 3 | trigger_event(302); stop |
| 2 | 302 | 30 / 2 | 5 | 3 | set_switch(30); set_switch(31); trigger_event(303); stop |
| 2 | 303 | 30 / 3 | 3 | 3 | trigger_event(304); stop |
| 2 | 304 | 30 / 4 | 5 | 3 | trigger_event(305); stop |
| 2 | 305 | 30 / 5 | 4 | 3 | trigger_event(306); stop |
| 2 | 306 | 30 / 6 | 3 | 3 | set_switch(32); stop |
| 2 | 601 | 60 / 1 | 6 | 3 | trigger_event(602); stop |
| 2 | 602 | 60 / 2 | 6 | 3 | trigger_event(603); stop |
| 2 | 603 | 60 / 3 | 5 | 3 | set_switch(60); set_switch(61); set_switch(62); set_switch(63); stop |
| 2 | 111 | 11 / 1 | 3 | 3 | trigger_event(112); stop |
| 2 | 112 | 11 / 2 | 4 | 3 | set_switch(110); trigger_event(113); stop |
| 2 | 801 | 80 / 1 | 4 | 3 | trigger_event(802); stop |
| 2 | 802 | 80 / 2 | 3 | 3 | trigger_event(803); stop |
| 2 | 803 | 80 / 3 | 4 | 3 | trigger_event(804); stop |
| 2 | 804 | 80 / 4 | 4 | 3 | trigger_event(805); stop |
| 2 | 805 | 80 / 5 | 2 | 3 | set_switch(80); set_switch(81); set_switch(82); stop |
| 2 | 501 | 50 / 1 | 3 | 3 | trigger_event(502); stop |
| 2 | 502 | 50 / 2 | 4 | 3 | trigger_event(503); stop |
| 2 | 503 | 50 / 3 | 3 | 3 | set_switch(50); trigger_event(504); stop |
| 2 | 504 | 50 / 4 | 3 | 3 | trigger_event(505); stop |
| 2 | 505 | 50 / 5 | 3 | 3 | trigger_event(506); stop |
| 2 | 506 | 50 / 6 | 3 | 3 | trigger_event(507); stop |
| 2 | 507 | 50 / 7 | 4 | 3 | trigger_event(508); stop |
| 2 | 508 | 50 / 8 | 3 | 3 | set_switch(51); set_switch(52); set_switch(53); stop |
| 2 | 113 | 11 / 3 | 4 | 3 | trigger_event(114); stop |
| 2 | 114 | 11 / 4 | 4 | 3 | set_switch(111); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

A backup is present; decompressed content identical: True. See [text differences](<backup-diff.txt>).

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
