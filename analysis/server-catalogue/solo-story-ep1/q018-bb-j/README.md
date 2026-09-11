# 心のかたち — solo-story-ep1/q018-bb-j

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/solo-story-ep1/q018-bb-j.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/solo-story-ep1/q018-bb-j.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/solo-story-ep1/q018-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 18; language J. Static scan: **184 objects, 69 enemy/NPC records, 17 events, 52 script labels.** Script roundtrip: byte-identical.

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
0x06, 0x06, 0x00, 0x02, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 18 | 0 |
| 6 | 158 | 51 | 17 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 6 | 301 | 30 / 1 | 2 | 60 | set_switch(16); set_switch(17); stop |
| 6 | 411 | 41 / 1 | 1 | 1 | set_switch(24); stop |
| 6 | 511 | 51 / 1 | 4 | 1 | trigger_event(5111); stop |
| 6 | 5111 | 51 / 2 | 4 | 60 | set_switch(12); set_switch(13); set_switch(14); set_switch(15); stop |
| 6 | 521 | 52 / 1 | 3 | 1 | trigger_event(5211); stop |
| 6 | 5211 | 52 / 2 | 3 | 60 | trigger_event(5212); stop |
| 6 | 5212 | 52 / 3 | 1 | 60 | set_switch(18); set_switch(19); set_switch(20); set_switch(21); set_switch(23); stop |
| 6 | 522 | 52 / 4 | 2 | 1 | trigger_event(5221); stop |
| 6 | 5221 | 52 / 5 | 2 | 60 | stop |
| 6 | 531 | 53 / 1 | 1 | 61 | trigger_event(5311); stop |
| 6 | 5311 | 53 / 2 | 3 | 90 | set_switch(25); set_switch(26); stop |
| 6 | 601 | 60 / 1 | 4 | 1 | trigger_event(6011); stop |
| 6 | 6011 | 60 / 2 | 4 | 60 | set_switch(4); set_switch(6); set_switch(7); set_switch(8); set_switch(9); set_switch(10); set_switch(11); stop |
| 6 | 611 | 61 / 1 | 5 | 1 | trigger_event(6111); stop |
| 6 | 6111 | 61 / 2 | 5 | 45 | trigger_event(6112); stop |
| 6 | 6112 | 61 / 3 | 2 | 45 | trigger_event(6113); stop |
| 6 | 6113 | 61 / 4 | 5 | 60 | set_switch(22); set_switch(27); set_switch(30); set_switch(31); set_switch(32); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
