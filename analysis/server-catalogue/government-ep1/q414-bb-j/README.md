# ４－４：胎動する墓 — government-ep1/q414-bb-j

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/government-ep1/q414-bb-j.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep1/q414-bb-j.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep1/q414-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 414; language J. Static scan: **317 objects, 305 enemy/NPC records, 71 events, 73 script labels.** Script roundtrip: byte-identical.

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
0x0A, 0x0A, 0x00, 0x00, 0x00
0x0B, 0x0A, 0x00, 0x01, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 27 | 20 | 0 |
| 10 | 223 | 170 | 37 |
| 11 | 67 | 115 | 34 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 10 | 401 | 40 / 1 | 4 | 10 | trigger_event(4011); stop |
| 10 | 4011 | 40 / 2 | 6 | 10 | trigger_event(4012); stop |
| 10 | 4012 | 40 / 3 | 6 | 10 | trigger_event(4013); stop |
| 10 | 4013 | 40 / 4 | 5 | 10 | trigger_event(4014); stop |
| 10 | 4014 | 40 / 5 | 3 | 10 | set_switch(3); set_switch(4); stop |
| 10 | 301 | 30 / 1 | 1 | 10 | trigger_event(3011); stop |
| 10 | 3011 | 30 / 2 | 6 | 10 | trigger_event(3012); stop |
| 10 | 3012 | 30 / 3 | 2 | 10 | set_switch(11); set_switch(12); set_switch(13); set_switch(14); set_switch(23); set_switch(24); set_switch(15); set_switch(16); set_switch(19); set_switch(20); set_switch(21); set_switch(22); set_switch(23); set_switch(24); set_switch(9); set_switch(10); set_switch(27); set_switch(28); stop |
| 10 | 201 | 20 / 1 | 4 | 10 | trigger_event(2011); stop |
| 10 | 2011 | 20 / 2 | 2 | 10 | trigger_event(2012); stop |
| 10 | 2012 | 20 / 3 | 5 | 10 | set_switch(5); set_switch(6); stop |
| 10 | 411 | 41 / 1 | 6 | 10 | trigger_event(4111); stop |
| 10 | 4111 | 41 / 2 | 3 | 10 | trigger_event(4112); stop |
| 10 | 4112 | 41 / 3 | 4 | 10 | set_switch(7); set_switch(8); stop |
| 10 | 311 | 31 / 1 | 5 | 10 | set_switch(17); set_switch(18); stop |
| 10 | 431 | 43 / 1 | 5 | 10 | trigger_event(4311); stop |
| 10 | 4311 | 43 / 2 | 2 | 10 | trigger_event(4312); stop |
| 10 | 4312 | 43 / 3 | 5 | 10 | trigger_event(4313); stop |
| 10 | 4313 | 43 / 4 | 6 | 10 | set_switch(25); set_switch(26); set_switch(29); set_switch(30); set_switch(31); set_switch(32); set_switch(23); set_switch(24); stop |
| 10 | 421 | 42 / 1 | 7 | 10 | trigger_event(4211); stop |
| 10 | 4211 | 42 / 2 | 6 | 10 | trigger_event(4212); stop |
| 10 | 4212 | 42 / 3 | 4 | 10 | set_switch(25); set_switch(26); set_switch(27); set_switch(28); stop |
| 10 | 601 | 60 / 1 | 5 | 10 | set_switch(33); set_switch(34); set_switch(35); set_switch(36); stop |
| 10 | 602 | 60 / 2 | 5 | 10 | trigger_event(6021); stop |
| 10 | 6021 | 60 / 3 | 6 | 10 | set_switch(43); set_switch(44); stop |
| 10 | 321 | 32 / 1 | 5 | 10 | trigger_event(3211); stop |
| 10 | 3211 | 32 / 2 | 5 | 10 | trigger_event(3212); stop |
| 10 | 3212 | 32 / 3 | 7 | 10 | set_switch(37); set_switch(38); set_switch(39); set_switch(40); stop |
| 10 | 211 | 21 / 1 | 5 | 10 | trigger_event(2111); stop |
| 10 | 2111 | 21 / 2 | 7 | 10 | set_switch(41); set_switch(42); stop |
| 10 | 441 | 44 / 1 | 1 | 10 | trigger_event(4411); stop |
| 10 | 4411 | 44 / 2 | 6 | 10 | trigger_event(4412); stop |
| 10 | 4412 | 44 / 3 | 3 | 10 | trigger_event(4413); stop |
| 10 | 4413 | 44 / 4 | 5 | 10 | set_switch(45); set_switch(46); set_switch(47); set_switch(48); set_switch(49); stop |
| 10 | 801 | 80 / 1 | 3 | 10 | set_switch(50); set_switch(51); set_switch(52); set_switch(53); set_switch(54); set_switch(55); stop |
| 10 | 802 | 80 / 2 | 6 | 10 | stop |
| 10 | 803 | 80 / 3 | 4 | 10 | stop |
| 11 | 401 | 40 / 1 | 5 | 30 | trigger_event(4011); stop |
| 11 | 4011 | 40 / 2 | 8 | 30 | set_switch(17); set_switch(18); set_switch(26); stop |
| 11 | 411 | 41 / 1 | 3 | 30 | trigger_event(4111); stop |
| 11 | 4111 | 41 / 2 | 3 | 120 | trigger_event(4112); stop |
| 11 | 4112 | 41 / 3 | 3 | 120 | trigger_event(4113); stop |
| 11 | 4113 | 41 / 4 | 3 | 120 | set_switch(101); stop |
| 11 | 412 | 41 / 5 | 3 | 30 | trigger_event(4121); stop |
| 11 | 4121 | 41 / 6 | 3 | 120 | trigger_event(4122); stop |
| 11 | 4122 | 41 / 7 | 3 | 120 | trigger_event(4123); stop |
| 11 | 4123 | 41 / 8 | 3 | 120 | set_switch(102); stop |
| 11 | 413 | 41 / 12 | 3 | 120 | trigger_event(4131); stop |
| 11 | 4131 | 41 / 13 | 3 | 120 | trigger_event(4132); stop |
| 11 | 4132 | 41 / 14 | 3 | 120 | trigger_event(4133); stop |
| 11 | 4133 | 41 / 15 | 3 | 120 | set_switch(104); stop |
| 11 | 414 | 41 / 16 | 3 | 120 | trigger_event(4141); stop |
| 11 | 4141 | 41 / 17 | 3 | 120 | trigger_event(4142); stop |
| 11 | 4142 | 41 / 18 | 3 | 120 | trigger_event(4143); stop |
| 11 | 4143 | 41 / 19 | 3 | 120 | set_switch(105); stop |
| 11 | 415 | 41 / 22 | 3 | 120 | trigger_event(4151); stop |
| 11 | 4151 | 41 / 23 | 3 | 120 | trigger_event(4152); stop |
| 11 | 4152 | 41 / 24 | 3 | 120 | trigger_event(4153); stop |
| 11 | 4153 | 41 / 25 | 3 | 120 | set_switch(107); stop |
| 11 | 416 | 41 / 26 | 3 | 120 | trigger_event(4161); stop |
| 11 | 4161 | 41 / 27 | 3 | 120 | trigger_event(4162); stop |
| 11 | 4162 | 41 / 28 | 3 | 120 | trigger_event(4163); stop |
| 11 | 4163 | 41 / 29 | 3 | 120 | set_switch(108); stop |
| 11 | 417 | 41 / 9 | 7 | 120 | trigger_event(4171); stop |
| 11 | 4171 | 41 / 10 | 4 | 90 | trigger_event(4172); stop |
| 11 | 4172 | 41 / 11 | 3 | 90 | set_switch(103); stop |
| 11 | 418 | 41 / 20 | 3 | 120 | trigger_event(4181); stop |
| 11 | 4181 | 41 / 21 | 4 | 90 | set_switch(106); stop |
| 11 | 419 | 41 / 30 | 3 | 120 | trigger_event(4191); stop |
| 11 | 4191 | 41 / 31 | 3 | 90 | trigger_event(4192); stop |
| 11 | 4192 | 41 / 32 | 3 | 120 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
