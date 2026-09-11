# ヒミツの届け物 — solo-story-ep1/q014-bb-j

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/solo-story-ep1/q014-bb-j.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/solo-story-ep1/q014-bb-j.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/solo-story-ep1/q014-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 14; language J. Static scan: **328 objects, 131 enemy/NPC records, 57 events, 93 script labels.** Script roundtrip: byte-identical.

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
0x03, 0x03, 0x00, 0x00, 0x01
0x04, 0x04, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 21 | 0 |
| 3 | 156 | 71 | 33 |
| 4 | 146 | 39 | 24 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 3 | 311 | 31 / 1 | 2 | 60 | trigger_event(3111); stop |
| 3 | 3111 | 31 / 2 | 2 | 60 | trigger_event(3112); stop |
| 3 | 3112 | 31 / 3 | 2 | 60 | set_switch(23); set_switch(24); set_switch(20); set_switch(19); set_switch(22); stop |
| 3 | 521 | 52 / 1 | 2 | 60 | trigger_event(5211); stop |
| 3 | 5211 | 52 / 2 | 2 | 60 | trigger_event(5212); stop |
| 3 | 5212 | 52 / 3 | 1 | 60 | trigger_event(5213); stop |
| 3 | 5213 | 52 / 4 | 2 | 60 | set_switch(21); stop |
| 3 | 201 | 20 / 1 | 2 | 60 | trigger_event(2011); stop |
| 3 | 2011 | 20 / 2 | 1 | 60 | stop |
| 3 | 511 | 51 / 1 | 3 | 60 | trigger_event(5111); stop |
| 3 | 5111 | 51 / 2 | 1 | 60 | trigger_event(5112); stop |
| 3 | 5112 | 51 / 3 | 2 | 60 | trigger_event(5113); stop |
| 3 | 5113 | 51 / 4 | 2 | 60 | trigger_event(5114); stop |
| 3 | 5114 | 51 / 5 | 2 | 60 | set_switch(16); set_switch(17); set_switch(15); set_switch(18); set_switch(14); set_switch(13); stop |
| 3 | 331 | 33 / 1 | 2 | 60 | trigger_event(3311); stop |
| 3 | 3311 | 33 / 2 | 2 | 60 | stop |
| 3 | 601 | 60 / 1 | 2 | 60 | trigger_event(6011); stop |
| 3 | 6011 | 60 / 2 | 3 | 60 | trigger_event(6012); stop |
| 3 | 6012 | 60 / 3 | 3 | 60 | trigger_event(6013); stop |
| 3 | 6013 | 60 / 4 | 2 | 60 | set_switch(11); set_switch(12); set_switch(8); set_switch(9); stop |
| 3 | 531 | 53 / 1 | 2 | 60 | trigger_event(5311); stop |
| 3 | 5311 | 53 / 2 | 2 | 60 | trigger_event(5312); stop |
| 3 | 5312 | 53 / 3 | 4 | 60 | trigger_event(5313); stop |
| 3 | 5313 | 53 / 4 | 3 | 60 | set_switch(10); set_switch(6); stop |
| 3 | 101 | 10 / 1 | 2 | 60 | trigger_event(1011); stop |
| 3 | 1011 | 10 / 2 | 2 | 60 | set_switch(7); set_switch(8); set_switch(4); stop |
| 3 | 341 | 34 / 1 | 2 | 60 | trigger_event(3411); stop |
| 3 | 3411 | 34 / 2 | 1 | 60 | trigger_event(3412); stop |
| 3 | 3412 | 34 / 3 | 3 | 60 | set_switch(4); set_switch(5); set_switch(7); stop |
| 3 | 501 | 50 / 1 | 2 | 60 | set_switch(2); set_switch(3); stop |
| 3 | 502 | 50 / 2 | 3 | 60 | trigger_event(5021); stop |
| 3 | 5021 | 50 / 3 | 2 | 60 | trigger_event(5022); stop |
| 3 | 5022 | 50 / 4 | 3 | 60 | set_switch(1); stop |
| 4 | 141 | 14 / 1 | 2 | 60 | trigger_event(1411); stop |
| 4 | 1411 | 14 / 2 | 2 | 60 | set_switch(33); stop |
| 4 | 231 | 23 / 1 | 2 | 60 | trigger_event(2311); stop |
| 4 | 2311 | 23 / 2 | 1 | 60 | set_switch(32); set_switch(31); stop |
| 4 | 302 | 30 / 1 | 2 | 60 | set_switch(25); set_switch(30); set_switch(27); set_switch(24); stop |
| 4 | 303 | 30 / 2 | 2 | 60 | stop |
| 4 | 351 | 35 / 1 | 3 | 60 | set_switch(26); set_switch(28); stop |
| 4 | 352 | 35 / 2 | 0 | 60 | stop |
| 4 | 402 | 40 / 1 | 0 | 60 | set_switch(22); set_switch(23); set_switch(17); set_switch(18); set_switch(21); set_switch(35); set_switch(20); set_switch(19); set_switch(15); stop |
| 4 | 121 | 12 / 1 | 3 | 60 | stop |
| 4 | 122 | 12 / 2 | 1 | 60 | trigger_event(1221); stop |
| 4 | 1221 | 12 / 3 | 2 | 60 | set_switch(29); stop |
| 4 | 601 | 60 / 1 | 2 | 60 | trigger_event(6011); stop |
| 4 | 6011 | 60 / 2 | 1 | 60 | trigger_event(6012); stop |
| 4 | 6012 | 60 / 3 | 2 | 60 | set_switch(13); set_switch(14); stop |
| 4 | 111 | 11 / 1 | 1 | 60 | trigger_event(1111); stop |
| 4 | 1111 | 11 / 2 | 2 | 60 | set_switch(12); stop |
| 4 | 211 | 21 / 1 | 1 | 60 | trigger_event(2111); stop |
| 4 | 2111 | 21 / 2 | 2 | 60 | trigger_event(2112); stop |
| 4 | 2112 | 21 / 3 | 1 | 60 | set_switch(6); set_switch(5); set_switch(9); set_switch(4); set_switch(7); set_switch(3); stop |
| 4 | 201 | 20 / 1 | 3 | 60 | trigger_event(2011); stop |
| 4 | 2011 | 20 / 2 | 1 | 60 | trigger_event(2012); stop |
| 4 | 2012 | 20 / 3 | 2 | 60 | set_switch(2); stop |
| 4 | 151 | 15 / 1 | 1 | 60 | set_switch(1); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
