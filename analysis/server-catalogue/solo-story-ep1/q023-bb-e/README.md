# Doc\'s Secret Plan — solo-story-ep1/q023-bb-e

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/solo-story-ep1/q023-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/solo-story-ep1/q023-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/solo-story-ep1/q023-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 23; language E. Static scan: **234 objects, 136 enemy/NPC records, 26 events, 51 script labels.** Script roundtrip: byte-identical.

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
0x08, 0x08, 0x00, 0x01, 0x01
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 19 | 0 |
| 8 | 208 | 117 | 26 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 8 | 300 | 30 / 1 | 5 | 10 | trigger_event(3011); stop |
| 8 | 3011 | 30 / 2 | 7 | 10 | trigger_event(3012); stop |
| 8 | 3012 | 30 / 3 | 5 | 10 | trigger_event(3013); stop |
| 8 | 3013 | 30 / 4 | 6 | 10 | set_switch(37); set_switch(38); set_switch(35); set_switch(36); set_switch(39); set_switch(40); set_switch(33); set_switch(34); set_switch(27); set_switch(28); set_switch(31); set_switch(32); stop |
| 8 | 221 | 22 / 1 | 5 | 10 | set_switch(41); set_switch(42); stop |
| 8 | 111 | 11 / 1 | 5 | 10 | trigger_event(1111); stop |
| 8 | 1111 | 11 / 2 | 5 | 10 | set_switch(30); set_switch(29); set_switch(26); set_switch(25); set_switch(31); set_switch(32); stop |
| 8 | 121 | 12 / 1 | 1 | 10 | set_switch(19); set_switch(20); set_switch(21); set_switch(22); stop |
| 8 | 310 | 31 / 1 | 2 | 10 | trigger_event(3111); stop |
| 8 | 3111 | 31 / 2 | 3 | 10 | trigger_event(3112); stop |
| 8 | 3112 | 31 / 3 | 4 | 10 | set_switch(15); set_switch(16); set_switch(17); set_switch(18); set_switch(14); set_switch(13); stop |
| 8 | 700 | 70 / 1 | 6 | 10 | trigger_event(7011); stop |
| 8 | 7011 | 70 / 2 | 5 | 10 | trigger_event(7012); stop |
| 8 | 7012 | 70 / 3 | 2 | 10 | trigger_event(7013); stop |
| 8 | 7013 | 70 / 4 | 4 | 10 | trigger_event(7014); stop |
| 8 | 7014 | 70 / 5 | 3 | 10 | trigger_event(7015); stop |
| 8 | 7015 | 70 / 6 | 3 | 10 | set_switch(11); set_switch(12); stop |
| 8 | 551 | 55 / 1 | 4 | 10 | set_switch(9); set_switch(10); stop |
| 8 | 552 | 55 / 2 | 4 | 10 | stop |
| 8 | 321 | 32 / 1 | 2 | 10 | trigger_event(3211); stop |
| 8 | 3211 | 32 / 2 | 8 | 10 | set_switch(7); set_switch(8); stop |
| 8 | 201 | 20 / 1 | 5 | 10 | trigger_event(2011); stop |
| 8 | 2011 | 20 / 2 | 4 | 10 | set_switch(3); set_switch(4); set_switch(5); set_switch(6); set_switch(47); set_switch(48); stop |
| 8 | 331 | 33 / 1 | 4 | 10 | trigger_event(3311); stop |
| 8 | 3311 | 33 / 2 | 3 | 10 | trigger_event(3312); stop |
| 8 | 3312 | 33 / 3 | 4 | 10 | set_switch(1); set_switch(2); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
