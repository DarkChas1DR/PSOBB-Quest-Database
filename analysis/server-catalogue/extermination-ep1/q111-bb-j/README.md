# 夢幻のごとく ４ — extermination-ep1/q111-bb-j

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/extermination-ep1/q111-bb-j.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/extermination-ep1/q111-bb-j.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/extermination-ep1/q111-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 111; language J. Static scan: **486 objects, 390 enemy/NPC records, 98 events, 40 script labels.** Script roundtrip: byte-identical.

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
0x08, 0x08, 0x00, 0x00, 0x00
0x09, 0x09, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 21 | 0 |
| 8 | 221 | 203 | 55 |
| 9 | 239 | 166 | 43 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 8 | 602 | 60 / 1 | 8 | 30 | set_switch(55); set_switch(56); set_switch(52); set_switch(51); stop |
| 8 | 201 | 20 / 1 | 6 | 30 | trigger_event(2011); stop |
| 8 | 2011 | 20 / 2 | 6 | 30 | trigger_event(2012); stop |
| 8 | 2012 | 20 / 3 | 6 | 30 | set_switch(50); set_switch(49); set_switch(45); set_switch(46); set_switch(47); set_switch(48); stop |
| 8 | 701 | 70 / 1 | 5 | 30 | trigger_event(7011); stop |
| 8 | 7011 | 70 / 2 | 7 | 30 | trigger_event(7012); stop |
| 8 | 7012 | 70 / 3 | 2 | 30 | set_switch(43); set_switch(44); stop |
| 8 | 311 | 31 / 1 | 2 | 30 | trigger_event(3111); stop |
| 8 | 3111 | 31 / 2 | 3 | 30 | trigger_event(3112); stop |
| 8 | 3112 | 31 / 3 | 6 | 30 | set_switch(34); set_switch(33); set_switch(36); set_switch(35); set_switch(39); set_switch(40); set_switch(37); set_switch(38); set_switch(31); set_switch(32); stop |
| 8 | 211 | 21 / 1 | 4 | 30 | set_switch(41); set_switch(42); stop |
| 8 | 212 | 21 / 2 | 4 | 30 | stop |
| 8 | 221 | 22 / 1 | 8 | 30 | trigger_event(2211); stop |
| 8 | 2211 | 22 / 2 | 5 | 30 | set_switch(28); set_switch(27); stop |
| 8 | 501 | 50 / 1 | 6 | 30 | set_switch(23); set_switch(24); stop |
| 8 | 502 | 50 / 2 | 4 | 30 | set_switch(29); set_switch(30); set_switch(31); set_switch(32); stop |
| 8 | 321 | 32 / 1 | 3 | 30 | trigger_event(3211); stop |
| 8 | 3211 | 32 / 2 | 3 | 30 | trigger_event(3212); stop |
| 8 | 3212 | 32 / 3 | 6 | 30 | set_switch(25); set_switch(26); set_switch(21); set_switch(22); set_switch(20); set_switch(19); set_switch(17); set_switch(18); set_switch(16); set_switch(15); set_switch(13); set_switch(14); set_switch(11); set_switch(12); set_switch(10); set_switch(9); set_switch(1); set_switch(2); set_switch(3); set_switch(4); stop |
| 8 | 241 | 24 / 1 | 3 | 30 | trigger_event(2411); stop |
| 8 | 2411 | 24 / 2 | 3 | 30 | trigger_event(2412); stop |
| 8 | 2412 | 24 / 3 | 5 | 30 | stop |
| 8 | 231 | 23 / 1 | 3 | 30 | trigger_event(2311); stop |
| 8 | 2311 | 23 / 2 | 3 | 30 | trigger_event(2312); stop |
| 8 | 2312 | 23 / 3 | 3 | 30 | trigger_event(2313); stop |
| 8 | 2313 | 23 / 4 | 5 | 30 | trigger_event(2314); stop |
| 8 | 2314 | 23 / 5 | 5 | 30 | trigger_event(2315); stop |
| 8 | 2315 | 23 / 6 | 3 | 30 | trigger_event(2316); stop |
| 8 | 2316 | 23 / 7 | 5 | 30 | set_switch(5); set_switch(6); set_switch(3); set_switch(4); stop |
| 8 | 331 | 33 / 1 | 3 | 30 | trigger_event(3311); stop |
| 8 | 3311 | 33 / 2 | 3 | 30 | trigger_event(3312); stop |
| 8 | 3312 | 33 / 3 | 3 | 30 | trigger_event(3313); stop |
| 8 | 3313 | 33 / 4 | 2 | 30 | trigger_event(3314); stop |
| 8 | 3314 | 33 / 5 | 2 | 30 | trigger_event(3315); stop |
| 8 | 3315 | 33 / 6 | 2 | 30 | trigger_event(3316); stop |
| 8 | 3316 | 33 / 7 | 3 | 30 | trigger_event(3317); stop |
| 8 | 3317 | 33 / 8 | 3 | 30 | trigger_event(3318); stop |
| 8 | 3318 | 33 / 9 | 3 | 30 | trigger_event(3319); stop |
| 8 | 3319 | 33 / 10 | 2 | 30 | trigger_event(3380); stop |
| 8 | 3380 | 33 / 11 | 2 | 30 | trigger_event(3381); stop |
| 8 | 3381 | 33 / 12 | 2 | 30 | trigger_event(3382); stop |
| 8 | 3382 | 33 / 13 | 2 | 30 | set_switch(7); set_switch(8); stop |
| 8 | 332 | 33 / 14 | 3 | 30 | trigger_event(3321); stop |
| 8 | 3321 | 33 / 15 | 3 | 30 | trigger_event(3322); stop |
| 8 | 3322 | 33 / 16 | 3 | 30 | trigger_event(3323); stop |
| 8 | 3323 | 33 / 17 | 4 | 30 | trigger_event(3324); stop |
| 8 | 3324 | 33 / 18 | 4 | 30 | trigger_event(3325); stop |
| 8 | 3325 | 33 / 19 | 4 | 30 | trigger_event(3326); stop |
| 8 | 3326 | 33 / 20 | 4 | 30 | trigger_event(3327); stop |
| 8 | 3327 | 33 / 21 | 3 | 30 | trigger_event(3328); stop |
| 8 | 3328 | 33 / 22 | 3 | 30 | trigger_event(3329); stop |
| 8 | 3329 | 33 / 23 | 1 | 30 | trigger_event(3390); stop |
| 8 | 3390 | 33 / 24 | 3 | 30 | trigger_event(3391); stop |
| 8 | 3391 | 33 / 25 | 1 | 30 | trigger_event(3392); stop |
| 8 | 3392 | 33 / 26 | 3 | 30 | stop |
| 9 | 201 | 20 / 1 | 4 | 30 | set_switch(37); set_switch(38); stop |
| 9 | 211 | 21 / 1 | 6 | 10 | trigger_event(2111); stop |
| 9 | 2111 | 21 / 2 | 4 | 1 | set_switch(7); set_switch(8); set_switch(35); set_switch(36); stop |
| 9 | 212 | 21 / 3 | 3 | 60 | stop |
| 9 | 301 | 30 / 1 | 9 | 30 | set_switch(31); set_switch(32); stop |
| 9 | 311 | 31 / 1 | 3 | 30 | trigger_event(3111); stop |
| 9 | 3111 | 31 / 2 | 8 | 60 | trigger_event(3112); stop |
| 9 | 3112 | 31 / 3 | 5 | 30 | set_switch(11); set_switch(12); set_switch(13); set_switch(14); set_switch(33); set_switch(34); stop |
| 9 | 312 | 31 / 4 | 5 | 120 | stop |
| 9 | 401 | 40 / 1 | 8 | 1 | trigger_event(4011); stop |
| 9 | 4011 | 40 / 2 | 8 | 30 | set_switch(5); set_switch(6); set_switch(9); set_switch(10); stop |
| 9 | 411 | 41 / 1 | 3 | 30 | trigger_event(4111); stop |
| 9 | 4111 | 41 / 2 | 4 | 60 | trigger_event(4112); stop |
| 9 | 4112 | 41 / 3 | 1 | 60 | set_switch(3); set_switch(4); set_switch(27); set_switch(28); set_switch(29); set_switch(30); stop |
| 9 | 431 | 43 / 1 | 8 | 1 | trigger_event(4311); stop |
| 9 | 4311 | 43 / 2 | 3 | 60 | trigger_event(4312); stop |
| 9 | 4312 | 43 / 3 | 3 | 60 | set_switch(15); set_switch(16); set_switch(17); set_switch(18); set_switch(19); set_switch(20); set_switch(21); set_switch(22); set_switch(23); set_switch(24); stop |
| 9 | 801 | 80 / 1 | 1 | 1 | trigger_event(8011); stop |
| 9 | 8011 | 80 / 2 | 3 | 35 | trigger_event(8012); stop |
| 9 | 8012 | 80 / 3 | 4 | 50 | trigger_event(8013); stop |
| 9 | 8013 | 80 / 4 | 4 | 15 | trigger_event(8014); stop |
| 9 | 8014 | 80 / 5 | 4 | 1 | trigger_event(8015); stop |
| 9 | 8015 | 80 / 6 | 4 | 60 | trigger_event(8016); stop |
| 9 | 8016 | 80 / 7 | 1 | 20 | trigger_event(8017); stop |
| 9 | 8017 | 80 / 8 | 3 | 15 | trigger_event(8018); stop |
| 9 | 8018 | 80 / 9 | 4 | 55 | trigger_event(8019); stop |
| 9 | 8019 | 80 / 10 | 1 | 55 | trigger_event(80191); stop |
| 9 | 80191 | 80 / 21 | 5 | 30 | trigger_event(80192); stop |
| 9 | 80192 | 80 / 23 | 4 | 23 | trigger_event(80193); stop |
| 9 | 80193 | 80 / 25 | 4 | 30 | trigger_event(80194); stop |
| 9 | 80194 | 80 / 26 | 4 | 30 | stop |
| 9 | 802 | 80 / 11 | 6 | 60 | trigger_event(8021); stop |
| 9 | 8021 | 80 / 12 | 1 | 35 | trigger_event(8022); stop |
| 9 | 8022 | 80 / 13 | 1 | 50 | trigger_event(8023); stop |
| 9 | 8023 | 80 / 14 | 4 | 15 | trigger_event(8024); stop |
| 9 | 8024 | 80 / 15 | 1 | 1 | trigger_event(8025); stop |
| 9 | 8025 | 80 / 16 | 4 | 60 | trigger_event(8026); stop |
| 9 | 8026 | 80 / 17 | 4 | 20 | trigger_event(8027); stop |
| 9 | 8027 | 80 / 18 | 4 | 15 | trigger_event(8028); stop |
| 9 | 8028 | 80 / 19 | 4 | 55 | trigger_event(8029); stop |
| 9 | 8029 | 80 / 20 | 2 | 35 | trigger_event(80291); stop |
| 9 | 80291 | 80 / 22 | 1 | 30 | trigger_event(80292); stop |
| 9 | 80292 | 80 / 24 | 3 | 30 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
