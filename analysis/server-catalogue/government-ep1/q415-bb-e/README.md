# 4-5:Dark Inheritance — government-ep1/q415-bb-e

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/government-ep1/q415-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep1/q415-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep1/q415-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 415; language E. Static scan: **774 objects, 507 enemy/NPC records, 131 events, 74 script labels.** Script roundtrip: byte-identical.

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
0x08, 0x08, 0x00, 0x02, 0x01
0x09, 0x09, 0x00, 0x02, 0x01
0x0A, 0x0A, 0x00, 0x02, 0x01
0x0E, 0x0E, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 27 | 20 | 0 |
| 8 | 246 | 160 | 42 |
| 9 | 248 | 157 | 39 |
| 10 | 221 | 169 | 49 |
| 14 | 32 | 1 | 1 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 8 | 101 | 10 / 1 | 3 | 1 | trigger_event(1011); stop |
| 8 | 1011 | 10 / 2 | 4 | 10 | trigger_event(1012); stop |
| 8 | 1012 | 10 / 3 | 4 | 10 | trigger_event(1013); stop |
| 8 | 1013 | 10 / 4 | 7 | 10 | set_switch(45); set_switch(46); set_switch(49); set_switch(50); set_switch(43); set_switch(44); stop |
| 8 | 201 | 20 / 1 | 4 | 1 | trigger_event(2011); stop |
| 8 | 2011 | 20 / 2 | 5 | 10 | set_switch(51); set_switch(52); stop |
| 8 | 202 | 20 / 3 | 4 | 10 | stop |
| 8 | 701 | 70 / 1 | 7 | 1 | trigger_event(7011); stop |
| 8 | 7011 | 70 / 2 | 4 | 1 | trigger_event(7012); stop |
| 8 | 7012 | 70 / 3 | 4 | 1 | trigger_event(7013); stop |
| 8 | 7013 | 70 / 4 | 5 | 1 | set_switch(41); set_switch(42); stop |
| 8 | 301 | 30 / 1 | 5 | 1 | trigger_event(3011); stop |
| 8 | 3011 | 30 / 2 | 3 | 1 | trigger_event(3012); stop |
| 8 | 3012 | 30 / 3 | 4 | 1 | trigger_event(3013); stop |
| 8 | 3013 | 30 / 4 | 3 | 1 | trigger_event(3014); stop |
| 8 | 3014 | 30 / 5 | 8 | 1 | set_switch(39); set_switch(40); set_switch(37); set_switch(38); set_switch(33); set_switch(34); set_switch(35); set_switch(36); set_switch(31); set_switch(32); stop |
| 8 | 501 | 55 / 1 | 2 | 1 | trigger_event(5511); stop |
| 8 | 5511 | 55 / 2 | 6 | 1 | trigger_event(5512); stop |
| 8 | 5512 | 55 / 3 | 4 | 1 | set_switch(30); set_switch(29); set_switch(27); set_switch(28); set_switch(26); set_switch(25); stop |
| 8 | 331 | 33 / 1 | 3 | 10 | trigger_event(3311); stop |
| 8 | 3311 | 33 / 2 | 2 | 1 | trigger_event(3312); stop |
| 8 | 3312 | 33 / 3 | 3 | 1 | set_switch(21); set_switch(22); set_switch(15); set_switch(16); set_switch(23); set_switch(24); stop |
| 8 | 121 | 12 / 1 | 2 | 10 | trigger_event(1211); stop |
| 8 | 1211 | 12 / 2 | 5 | 10 | set_switch(19); set_switch(20); set_switch(17); set_switch(18); set_switch(9); set_switch(10); set_switch(23); set_switch(24); stop |
| 8 | 111 | 11 / 1 | 7 | 10 | trigger_event(1111); stop |
| 8 | 1111 | 11 / 2 | 5 | 10 | set_switch(14); set_switch(13); stop |
| 8 | 311 | 31 / 1 | 3 | 10 | trigger_event(3111); stop |
| 8 | 3111 | 31 / 2 | 3 | 10 | trigger_event(3112); stop |
| 8 | 3112 | 31 / 3 | 3 | 10 | set_switch(11); set_switch(12); stop |
| 8 | 312 | 31 / 4 | 1 | 10 | trigger_event(3121); stop |
| 8 | 3121 | 31 / 5 | 2 | 10 | trigger_event(3122); stop |
| 8 | 3122 | 31 / 6 | 4 | 10 | stop |
| 8 | 221 | 22 / 1 | 3 | 10 | trigger_event(2211); stop |
| 8 | 2211 | 22 / 2 | 3 | 10 | trigger_event(2212); stop |
| 8 | 2212 | 22 / 3 | 6 | 10 | trigger_event(2213); stop |
| 8 | 2213 | 22 / 4 | 5 | 10 | set_switch(9); set_switch(10); set_switch(8); set_switch(3); set_switch(17); set_switch(18); set_switch(19); set_switch(20); stop |
| 8 | 321 | 32 / 1 | 2 | 10 | trigger_event(3211); stop |
| 8 | 3211 | 32 / 2 | 3 | 10 | trigger_event(3212); stop |
| 8 | 3212 | 32 / 3 | 2 | 10 | set_switch(4); set_switch(5); set_switch(6); set_switch(7); set_switch(1); set_switch(2); stop |
| 8 | 322 | 32 / 4 | 3 | 10 | trigger_event(3221); stop |
| 8 | 3221 | 32 / 5 | 3 | 10 | trigger_event(3222); stop |
| 8 | 3222 | 32 / 6 | 1 | 10 | stop |
| 9 | 301 | 30 / 1 | 4 | 1 | trigger_event(3011); stop |
| 9 | 3011 | 30 / 2 | 7 | 45 | set_switch(1); set_switch(2); set_switch(3); set_switch(4); stop |
| 9 | 311 | 31 / 1 | 6 | 1 | trigger_event(3111); stop |
| 9 | 3111 | 31 / 2 | 6 | 45 | set_switch(33); set_switch(34); set_switch(35); set_switch(36); set_switch(37); set_switch(38); stop |
| 9 | 321 | 32 / 1 | 3 | 1 | trigger_event(3211); stop |
| 9 | 3211 | 32 / 2 | 6 | 30 | set_switch(23); set_switch(24); set_switch(25); set_switch(26); set_switch(27); set_switch(28); set_switch(41); set_switch(42); stop |
| 9 | 331 | 33 / 1 | 6 | 1 | set_switch(45); set_switch(46); set_switch(47); set_switch(48); set_switch(49); set_switch(50); set_switch(53); set_switch(54); stop |
| 9 | 341 | 34 / 1 | 6 | 1 | trigger_event(3411); stop |
| 9 | 3411 | 34 / 2 | 6 | 1 | set_switch(51); set_switch(52); stop |
| 9 | 401 | 40 / 1 | 6 | 1 | trigger_event(4011); stop |
| 9 | 4011 | 40 / 2 | 4 | 45 | set_switch(5); set_switch(6); set_switch(7); set_switch(8); set_switch(9); set_switch(10); set_switch(11); set_switch(12); stop |
| 9 | 403 | 40 / 3 | 4 | 60 | stop |
| 9 | 411 | 41 / 1 | 7 | 1 | trigger_event(4111); stop |
| 9 | 4111 | 41 / 2 | 8 | 60 | set_switch(15); set_switch(16); set_switch(17); set_switch(18); set_switch(19); set_switch(20); set_switch(21); set_switch(22); stop |
| 9 | 412 | 41 / 3 | 3 | 100 | stop |
| 9 | 421 | 42 / 1 | 1 | 1 | trigger_event(4211); stop |
| 9 | 4211 | 42 / 2 | 4 | 60 | trigger_event(4212); stop |
| 9 | 4212 | 42 / 3 | 2 | 55 | stop |
| 9 | 422 | 42 / 4 | 3 | 60 | trigger_event(4221); stop |
| 9 | 4221 | 42 / 5 | 4 | 40 | trigger_event(4222); stop |
| 9 | 4222 | 42 / 6 | 1 | 45 | set_switch(55); set_switch(56); stop |
| 9 | 431 | 43 / 1 | 2 | 1 | trigger_event(4311); stop |
| 9 | 4311 | 43 / 2 | 4 | 90 | trigger_event(4312); stop |
| 9 | 4312 | 42 / 3 | 2 | 45 | stop |
| 9 | 432 | 43 / 4 | 2 | 60 | trigger_event(4321); stop |
| 9 | 4321 | 43 / 5 | 4 | 80 | trigger_event(4322); stop |
| 9 | 4322 | 43 / 6 | 4 | 100 | trigger_event(4323); stop |
| 9 | 4323 | 43 / 7 | 1 | 120 | set_switch(61); set_switch(62); set_switch(63); set_switch(64); set_switch(65); set_switch(66); stop |
| 9 | 501 | 50 / 1 | 6 | 1 | trigger_event(5011); stop |
| 9 | 5011 | 50 / 2 | 6 | 45 | set_switch(29); set_switch(30); set_switch(31); set_switch(32); stop |
| 9 | 651 | 65 / 1 | 5 | 1 | trigger_event(6511); stop |
| 9 | 6511 | 65 / 2 | 3 | 60 | set_switch(13); set_switch(14); stop |
| 9 | 701 | 70 / 1 | 3 | 1 | set_switch(57); set_switch(58); set_switch(59); set_switch(60); stop |
| 9 | 801 | 80 / 1 | 6 | 30 | trigger_event(8011); stop |
| 9 | 8011 | 80 / 2 | 3 | 90 | trigger_event(8012); stop |
| 9 | 8012 | 80 / 3 | 4 | 60 | stop |
| 9 | 802 | 80 / 4 | 1 | 50 | trigger_event(8021); stop |
| 9 | 8021 | 80 / 5 | 2 | 90 | trigger_event(8022); stop |
| 9 | 8022 | 80 / 6 | 3 | 190 | set_switch(43); set_switch(44); stop |
| 10 | 211 | 21 / 1 | 3 | 20 | trigger_event(2111); stop |
| 10 | 2111 | 21 / 2 | 2 | 20 | set_switch(7); set_switch(8); set_switch(4); set_switch(3); stop |
| 10 | 401 | 40 / 1 | 2 | 20 | trigger_event(4011); stop |
| 10 | 4011 | 40 / 2 | 3 | 20 | trigger_event(4012); stop |
| 10 | 4012 | 40 / 3 | 1 | 20 | set_switch(1); set_switch(2); stop |
| 10 | 402 | 40 / 4 | 3 | 20 | trigger_event(4021); stop |
| 10 | 4021 | 40 / 5 | 3 | 20 | trigger_event(4022); stop |
| 10 | 4022 | 40 / 6 | 4 | 20 | stop |
| 10 | 301 | 30 / 1 | 5 | 20 | trigger_event(3011); stop |
| 10 | 3011 | 30 / 2 | 6 | 20 | set_switch(9); set_switch(10); set_switch(15); set_switch(16); set_switch(12); set_switch(11); stop |
| 10 | 651 | 65 / 1 | 7 | 20 | set_switch(13); set_switch(14); set_switch(23); set_switch(24); stop |
| 10 | 652 | 65 / 2 | 2 | 20 | stop |
| 10 | 653 | 65 / 3 | 1 | 20 | stop |
| 10 | 201 | 20 / 1 | 4 | 20 | set_switch(25); set_switch(26); set_switch(22); set_switch(21); stop |
| 10 | 202 | 20 / 2 | 3 | 20 | stop |
| 10 | 411 | 41 / 1 | 5 | 20 | trigger_event(4111); stop |
| 10 | 4111 | 41 / 2 | 4 | 20 | trigger_event(4112); stop |
| 10 | 4112 | 41 / 3 | 5 | 20 | set_switch(20); set_switch(19); stop |
| 10 | 321 | 32 / 1 | 3 | 20 | trigger_event(3211); stop |
| 10 | 3211 | 32 / 2 | 5 | 20 | set_switch(17); set_switch(18); set_switch(27); set_switch(28); stop |
| 10 | 221 | 22 / 1 | 4 | 20 | trigger_event(2211); stop |
| 10 | 2211 | 22 / 2 | 6 | 20 | set_switch(31); set_switch(32); set_switch(29); set_switch(30); set_switch(33); set_switch(34); set_switch(39); set_switch(40); stop |
| 10 | 231 | 23 / 1 | 1 | 20 | trigger_event(2311); stop |
| 10 | 2311 | 23 / 2 | 7 | 20 | trigger_event(2312); stop |
| 10 | 2312 | 23 / 3 | 3 | 20 | set_switch(41); set_switch(42); set_switch(40); set_switch(39); set_switch(34); set_switch(33); stop |
| 10 | 311 | 31 / 1 | 3 | 20 | trigger_event(3111); stop |
| 10 | 3111 | 31 / 2 | 3 | 20 | trigger_event(3112); stop |
| 10 | 3112 | 31 / 3 | 4 | 20 | set_switch(45); set_switch(46); set_switch(43); set_switch(44); set_switch(41); set_switch(40); stop |
| 10 | 312 | 31 / 4 | 3 | 20 | trigger_event(3121); stop |
| 10 | 3121 | 31 / 5 | 3 | 20 | trigger_event(3122); stop |
| 10 | 3122 | 31 / 6 | 3 | 20 | stop |
| 10 | 421 | 42 / 1 | 3 | 20 | trigger_event(4211); stop |
| 10 | 4211 | 42 / 2 | 4 | 20 | trigger_event(4212); stop |
| 10 | 4212 | 42 / 3 | 2 | 20 | set_switch(47); set_switch(48); set_switch(38); set_switch(37); set_switch(36); set_switch(35); set_switch(43); set_switch(44); stop |
| 10 | 422 | 42 / 4 | 3 | 20 | trigger_event(4221); stop |
| 10 | 4221 | 42 / 5 | 3 | 20 | trigger_event(4221); stop |
| 10 | 4221 | 42 / 6 | 3 | 20 | stop |
| 10 | 331 | 33 / 1 | 4 | 20 | trigger_event(3311); stop |
| 10 | 3311 | 33 / 2 | 3 | 20 | trigger_event(3312); stop |
| 10 | 3312 | 33 / 3 | 5 | 20 | trigger_event(3313); stop |
| 10 | 3313 | 33 / 4 | 6 | 20 | set_switch(49); set_switch(50); set_switch(51); set_switch(52); set_switch(53); set_switch(47); set_switch(48); stop |
| 10 | 801 | 80 / 1 | 4 | 20 | trigger_event(8011); stop |
| 10 | 8011 | 80 / 2 | 2 | 20 | trigger_event(8012); stop |
| 10 | 8012 | 80 / 3 | 3 | 20 | trigger_event(8013); stop |
| 10 | 8013 | 80 / 4 | 2 | 20 | set_switch(54); set_switch(55); set_switch(56); set_switch(57); set_switch(58); set_switch(59); stop |
| 10 | 802 | 80 / 5 | 3 | 20 | trigger_event(8021); stop |
| 10 | 8021 | 80 / 6 | 3 | 20 | trigger_event(8022); stop |
| 10 | 8022 | 80 / 7 | 3 | 20 | trigger_event(8023); stop |
| 10 | 8023 | 80 / 8 | 2 | 20 | stop |
| 14 | 1 | 0 / 1 | 1 | 50 | construct_objects(room=0,group_or_wave=1); construct_objects(room=1,group_or_wave=1); construct_objects(room=2,group_or_wave=1); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
