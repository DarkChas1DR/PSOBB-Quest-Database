# 隠居ハンター — solo-story-ep1/q019-bb-j

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/solo-story-ep1/q019-bb-j.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/solo-story-ep1/q019-bb-j.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/solo-story-ep1/q019-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 19; language J. Static scan: **331 objects, 154 enemy/NPC records, 33 events, 156 script labels.** Script roundtrip: byte-identical.

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
0x02, 0x02, 0x00, 0x00, 0x03
0x0A, 0x0A, 0x00, 0x02, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 18 | 0 |
| 2 | 93 | 37 | 11 |
| 10 | 212 | 99 | 22 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 2 | 11 | 1 / 1 | 4 | 1 | set_switch(1); set_switch(2); stop |
| 2 | 31 | 3 / 1 | 1 | 1 | set_switch(5); stop |
| 2 | 61 | 6 / 1 | 1 | 1 | trigger_event(611); stop |
| 2 | 611 | 6 / 2 | 4 | 30 | trigger_event(612); stop |
| 2 | 612 | 6 / 3 | 4 | 30 | trigger_event(613); stop |
| 2 | 613 | 6 / 4 | 4 | 30 | trigger_event(614); stop |
| 2 | 614 | 6 / 5 | 1 | 60 | set_switch(2); stop |
| 2 | 111 | 11 / 1 | 5 | 1 | set_switch(7); stop |
| 2 | 112 | 11 / 2 | 3 | 1 | set_switch(1); set_switch(4); set_switch(5); set_switch(6); stop |
| 2 | 151 | 15 / 1 | 4 | 1 | set_switch(7); stop |
| 2 | 152 | 15 / 2 | 6 | 30 | stop |
| 10 | 301 | 30 / 1 | 6 | 20 | set_switch(9); set_switch(10); set_switch(17); set_switch(18); set_switch(15); set_switch(16); set_switch(13); set_switch(14); set_switch(12); set_switch(11); stop |
| 10 | 551 | 55 / 1 | 4 | 20 | trigger_event(5511); stop |
| 10 | 5511 | 55 / 2 | 4 | 20 | set_switch(23); set_switch(24); stop |
| 10 | 201 | 20 / 1 | 4 | 20 | set_switch(25); set_switch(26); set_switch(22); set_switch(21); stop |
| 10 | 411 | 41 / 1 | 6 | 20 | trigger_event(4111); stop |
| 10 | 4111 | 41 / 2 | 6 | 20 | trigger_event(4112); stop |
| 10 | 4112 | 41 / 3 | 5 | 20 | set_switch(36); set_switch(35); set_switch(37); set_switch(38); set_switch(20); set_switch(19); stop |
| 10 | 221 | 22 / 1 | 7 | 20 | set_switch(31); set_switch(32); set_switch(29); set_switch(30); set_switch(33); set_switch(34); set_switch(39); set_switch(40); stop |
| 10 | 231 | 23 / 1 | 6 | 20 | set_switch(41); set_switch(42); stop |
| 10 | 311 | 31 / 1 | 5 | 20 | set_switch(45); set_switch(46); set_switch(43); set_switch(44); stop |
| 10 | 421 | 42 / 1 | 3 | 20 | trigger_event(4211); stop |
| 10 | 4211 | 42 / 2 | 3 | 20 | trigger_event(4212); stop |
| 10 | 4212 | 42 / 3 | 3 | 20 | trigger_event(4213); stop |
| 10 | 4213 | 42 / 4 | 3 | 20 | set_switch(47); set_switch(48); set_switch(38); set_switch(37); set_switch(36); set_switch(35); stop |
| 10 | 801 | 80 / 1 | 6 | 20 | trigger_event(8011); stop |
| 10 | 8011 | 80 / 2 | 4 | 20 | trigger_event(8012); stop |
| 10 | 8012 | 80 / 3 | 8 | 20 | trigger_event(8013); stop |
| 10 | 8013 | 80 / 4 | 3 | 20 | trigger_event(8014); stop |
| 10 | 8014 | 80 / 5 | 4 | 20 | trigger_event(8015); stop |
| 10 | 8015 | 80 / 6 | 4 | 20 | trigger_event(8016); stop |
| 10 | 8016 | 80 / 7 | 3 | 20 | trigger_event(8017); stop |
| 10 | 8017 | 80 / 8 | 2 | 20 | set_switch(54); set_switch(55); set_switch(56); set_switch(57); set_switch(58); set_switch(59); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
