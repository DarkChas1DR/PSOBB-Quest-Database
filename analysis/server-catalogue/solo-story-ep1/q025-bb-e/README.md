# From the Depths — solo-story-ep1/q025-bb-e

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/solo-story-ep1/q025-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/solo-story-ep1/q025-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/solo-story-ep1/q025-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 25; language E. Static scan: **454 objects, 216 enemy/NPC records, 47 events, 231 script labels.** Script roundtrip: byte-identical.

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
0x09, 0x09, 0x00, 0x01, 0x00
0x0A, 0x0A, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 17 | 0 |
| 9 | 227 | 132 | 32 |
| 10 | 201 | 67 | 15 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 9 | 211 | 21 / 1 | 6 | 1 | set_switch(27); set_switch(28); stop |
| 9 | 212 | 21 / 2 | 3 | 120 | stop |
| 9 | 231 | 23 / 1 | 1 | 1 | set_switch(65); set_switch(66); stop |
| 9 | 249 | 24 / 1 | 8 | 1 | trigger_event(2411); stop |
| 9 | 2411 | 24 / 2 | 6 | 30 | set_switch(33); set_switch(34); stop |
| 9 | 311 | 31 / 1 | 2 | 1 | trigger_event(3111); stop |
| 9 | 3111 | 31 / 2 | 3 | 60 | set_switch(13); set_switch(14); set_switch(15); set_switch(16); stop |
| 9 | 312 | 31 / 3 | 3 | 60 | stop |
| 9 | 321 | 32 / 1 | 5 | 1 | set_switch(37); set_switch(38); set_switch(39); set_switch(40); stop |
| 9 | 331 | 33 / 1 | 2 | 1 | trigger_event(3311); stop |
| 9 | 3311 | 33 / 2 | 6 | 60 | trigger_event(3312); stop |
| 9 | 3312 | 33 / 3 | 8 | 30 | set_switch(57); set_switch(58); set_switch(59); set_switch(60); set_switch(61); set_switch(62); set_switch(63); set_switch(64); stop |
| 9 | 341 | 34 / 1 | 6 | 1 | set_switch(53); set_switch(54); stop |
| 9 | 342 | 34 / 2 | 4 | 30 | stop |
| 9 | 401 | 40 / 1 | 4 | 1 | trigger_event(4011); stop |
| 9 | 4011 | 40 / 2 | 4 | 60 | set_switch(7); set_switch(8); set_switch(17); set_switch(18); set_switch(19); set_switch(20); set_switch(21); set_switch(22); set_switch(23); set_switch(24); set_switch(25); set_switch(26); set_switch(31); set_switch(32); stop |
| 9 | 402 | 40 / 3 | 3 | 60 | stop |
| 9 | 411 | 41 / 1 | 2 | 1 | trigger_event(4111); stop |
| 9 | 4111 | 41 / 2 | 2 | 30 | trigger_event(4112); stop |
| 9 | 4112 | 41 / 3 | 3 | 60 | set_switch(29); set_switch(30); stop |
| 9 | 421 | 42 / 1 | 5 | 1 | trigger_event(4211); stop |
| 9 | 4211 | 42 / 2 | 5 | 60 | trigger_event(4212); stop |
| 9 | 4212 | 42 / 3 | 3 | 60 | set_switch(35); set_switch(36); stop |
| 9 | 431 | 43 / 1 | 3 | 1 | trigger_event(4311); stop |
| 9 | 4311 | 43 / 2 | 4 | 30 | set_switch(49); set_switch(50); set_switch(51); set_switch(52); stop |
| 9 | 651 | 65 / 1 | 5 | 1 | trigger_event(6511); stop |
| 9 | 6511 | 65 / 2 | 4 | 45 | set_switch(11); set_switch(12); stop |
| 9 | 701 | 70 / 1 | 4 | 1 | set_switch(43); set_switch(44); set_switch(45); set_switch(46); set_switch(47); set_switch(48); set_switch(55); set_switch(56); stop |
| 9 | 702 | 70 / 2 | 3 | 100 | stop |
| 9 | 809 | 80 / 1 | 8 | 30 | trigger_event(8011); stop |
| 9 | 8011 | 80 / 2 | 6 | 90 | trigger_event(8012); stop |
| 9 | 8012 | 80 / 3 | 1 | 60 | set_switch(41); set_switch(42); stop |
| 10 | 400 | 40 / 1 | 5 | 10 | trigger_event(4011); stop |
| 10 | 4011 | 40 / 2 | 6 | 10 | set_switch(3); set_switch(4); stop |
| 10 | 301 | 30 / 1 | 1 | 10 | set_switch(11); set_switch(12); set_switch(13); set_switch(14); set_switch(23); set_switch(24); set_switch(15); set_switch(16); set_switch(19); set_switch(20); set_switch(21); set_switch(22); set_switch(23); set_switch(24); set_switch(9); set_switch(10); set_switch(27); set_switch(28); stop |
| 10 | 201 | 20 / 1 | 4 | 10 | trigger_event(2011); stop |
| 10 | 2011 | 20 / 2 | 2 | 10 | trigger_event(2012); stop |
| 10 | 2012 | 20 / 3 | 5 | 10 | set_switch(5); set_switch(6); stop |
| 10 | 411 | 41 / 1 | 6 | 10 | trigger_event(4111); stop |
| 10 | 4111 | 41 / 2 | 3 | 10 | set_switch(7); set_switch(8); stop |
| 10 | 311 | 31 / 1 | 5 | 10 | set_switch(17); set_switch(18); stop |
| 10 | 431 | 43 / 1 | 5 | 10 | trigger_event(4311); stop |
| 10 | 4311 | 43 / 2 | 2 | 10 | trigger_event(4312); stop |
| 10 | 4312 | 43 / 3 | 5 | 10 | trigger_event(4313); stop |
| 10 | 4313 | 43 / 4 | 6 | 10 | set_switch(25); set_switch(26); set_switch(29); set_switch(30); set_switch(31); set_switch(32); set_switch(23); set_switch(24); stop |
| 10 | 421 | 42 / 1 | 7 | 10 | set_switch(25); set_switch(26); set_switch(27); set_switch(28); stop |
| 10 | 601 | 60 / 1 | 5 | 10 | set_switch(33); set_switch(34); set_switch(35); set_switch(36); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
