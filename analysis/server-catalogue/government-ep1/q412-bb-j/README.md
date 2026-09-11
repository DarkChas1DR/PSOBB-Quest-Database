# ４－２：地底の石碑 — government-ep1/q412-bb-j

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/government-ep1/q412-bb-j.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep1/q412-bb-j.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep1/q412-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 412; language J. Static scan: **297 objects, 223 enemy/NPC records, 51 events, 125 script labels.** Script roundtrip: byte-identical.

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
0x09, 0x09, 0x00, 0x00, 0x00
0x0A, 0x09, 0x00, 0x01, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 27 | 20 | 0 |
| 9 | 223 | 151 | 34 |
| 10 | 47 | 52 | 17 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 9 | 201 | 20 / 1 | 2 | 30 | set_switch(37); set_switch(38); stop |
| 9 | 211 | 21 / 1 | 6 | 10 | trigger_event(2111); stop |
| 9 | 2111 | 21 / 2 | 4 | 1 | set_switch(7); set_switch(8); set_switch(35); set_switch(36); stop |
| 9 | 212 | 21 / 3 | 3 | 60 | stop |
| 9 | 241 | 24 / 1 | 4 | 1 | trigger_event(2411); stop |
| 9 | 2411 | 24 / 2 | 8 | 1 | set_switch(23); set_switch(24); set_switch(25); set_switch(26); set_switch(39); set_switch(40); stop |
| 9 | 242 | 24 / 3 | 3 | 60 | stop |
| 9 | 301 | 30 / 1 | 6 | 30 | set_switch(31); set_switch(32); stop |
| 9 | 311 | 31 / 1 | 3 | 30 | trigger_event(3111); stop |
| 9 | 3111 | 31 / 2 | 5 | 60 | trigger_event(3112); stop |
| 9 | 3112 | 31 / 3 | 5 | 30 | set_switch(11); set_switch(12); set_switch(13); set_switch(14); set_switch(33); set_switch(34); stop |
| 9 | 312 | 31 / 4 | 5 | 120 | stop |
| 9 | 321 | 32 / 1 | 5 | 30 | set_switch(63); set_switch(64); stop |
| 9 | 331 | 33 / 1 | 5 | 30 | trigger_event(3311); stop |
| 9 | 3311 | 33 / 2 | 3 | 60 | set_switch(43); set_switch(44); stop |
| 9 | 401 | 40 / 1 | 6 | 1 | trigger_event(4011); stop |
| 9 | 4011 | 40 / 2 | 4 | 30 | set_switch(5); set_switch(6); set_switch(9); set_switch(10); stop |
| 9 | 411 | 41 / 1 | 3 | 30 | trigger_event(4111); stop |
| 9 | 4111 | 41 / 2 | 2 | 60 | trigger_event(4112); stop |
| 9 | 4112 | 41 / 3 | 5 | 60 | set_switch(3); set_switch(4); set_switch(27); set_switch(28); set_switch(29); set_switch(30); stop |
| 9 | 421 | 42 / 1 | 4 | 1 | stop |
| 9 | 431 | 43 / 1 | 4 | 1 | trigger_event(4311); stop |
| 9 | 4311 | 43 / 2 | 5 | 60 | trigger_event(4312); stop |
| 9 | 4312 | 43 / 3 | 6 | 60 | set_switch(15); set_switch(16); set_switch(17); set_switch(18); set_switch(19); set_switch(20); set_switch(21); set_switch(22); stop |
| 9 | 441 | 44 / 1 | 6 | 1 | trigger_event(4411); stop |
| 9 | 4411 | 44 / 2 | 5 | 30 | trigger_event(4412); stop |
| 9 | 4412 | 44 / 3 | 6 | 30 | trigger_event(4413); stop |
| 9 | 4413 | 44 / 4 | 4 | 60 | set_switch(59); set_switch(60); set_switch(61); set_switch(62); stop |
| 9 | 601 | 60 / 1 | 5 | 1 | trigger_event(6011); stop |
| 9 | 6011 | 60 / 2 | 2 | 60 | set_switch(53); set_switch(54); set_switch(55); set_switch(56); set_switch(57); set_switch(58); stop |
| 9 | 801 | 80 / 1 | 1 | 1 | trigger_event(8011); stop |
| 9 | 8011 | 80 / 2 | 5 | 60 | trigger_event(8012); stop |
| 9 | 8012 | 80 / 3 | 5 | 60 | trigger_event(8013); stop |
| 9 | 8013 | 80 / 4 | 6 | 15 | set_switch(41); set_switch(42); set_switch(43); set_switch(44); set_switch(45); set_switch(46); set_switch(47); set_switch(48); set_switch(49); set_switch(50); set_switch(51); set_switch(52); stop |
| 10 | 431 | 43 / 1 | 4 | 30 | trigger_event(4311); stop |
| 10 | 4311 | 43 / 2 | 7 | 30 | set_switch(47); set_switch(48); set_switch(55); stop |
| 10 | 331 | 33 / 1 | 2 | 30 | trigger_event(3311); stop |
| 10 | 3311 | 33 / 2 | 2 | 90 | trigger_event(3312); stop |
| 10 | 3312 | 33 / 3 | 2 | 90 | trigger_event(3313); stop |
| 10 | 3313 | 33 / 4 | 2 | 90 | trigger_event(3314); stop |
| 10 | 3314 | 33 / 5 | 2 | 90 | set_switch(101); stop |
| 10 | 332 | 33 / 6 | 2 | 30 | trigger_event(3321); stop |
| 10 | 3321 | 33 / 7 | 2 | 90 | trigger_event(3322); stop |
| 10 | 3322 | 33 / 8 | 2 | 90 | trigger_event(3323); stop |
| 10 | 3323 | 33 / 9 | 2 | 90 | trigger_event(3324); stop |
| 10 | 3324 | 33 / 10 | 2 | 90 | set_switch(102); stop |
| 10 | 333 | 33 / 11 | 3 | 30 | trigger_event(3331); stop |
| 10 | 3331 | 33 / 12 | 4 | 90 | trigger_event(3332); stop |
| 10 | 3332 | 33 / 13 | 6 | 90 | trigger_event(3333); stop |
| 10 | 3333 | 33 / 14 | 5 | 90 | trigger_event(3334); stop |
| 10 | 3334 | 33 / 15 | 3 | 120 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
