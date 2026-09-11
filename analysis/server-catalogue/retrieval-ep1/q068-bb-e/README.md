# The Missing Maracas — retrieval-ep1/q068-bb-e

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/retrieval-ep1/q068-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/retrieval-ep1/q068-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/retrieval-ep1/q068-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 68; language E. Static scan: **378 objects, 296 enemy/NPC records, 84 events, 232 script labels.** Script roundtrip: byte-identical.

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
0x01, 0x01, 0x00, 0x00, 0x00
0x03, 0x03, 0x00, 0x00, 0x00
0x05, 0x05, 0x00, 0x00, 0x00
0x0C, 0x0C, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 23 | 0 |
| 1 | 110 | 67 | 18 |
| 3 | 213 | 205 | 65 |
| 5 | 13 | 0 | 0 |
| 12 | 16 | 1 | 1 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 111 | 11 / 1 | 3 | 50 | trigger_event(1111); stop |
| 1 | 1111 | 11 / 2 | 3 | 50 | trigger_event(1112); stop |
| 1 | 1112 | 11 / 3 | 3 | 50 | trigger_event(1113); stop |
| 1 | 1113 | 11 / 4 | 3 | 50 | set_switch(5); set_switch(6); stop |
| 1 | 101 | 10 / 1 | 3 | 30 | trigger_event(1011); stop |
| 1 | 1011 | 10 / 2 | 3 | 30 | trigger_event(1012); stop |
| 1 | 1012 | 10 / 3 | 3 | 30 | set_switch(7); set_switch(8); stop |
| 1 | 51 | 5 / 1 | 3 | 30 | trigger_event(511); stop |
| 1 | 511 | 5 / 2 | 6 | 30 | trigger_event(512); stop |
| 1 | 512 | 5 / 3 | 3 | 30 | set_switch(1); set_switch(2); stop |
| 1 | 52 | 5 / 4 | 3 | 30 | stop |
| 1 | 53 | 5 / 5 | 1 | 30 | stop |
| 1 | 71 | 7 / 1 | 5 | 30 | trigger_event(711); stop |
| 1 | 711 | 7 / 2 | 5 | 30 | trigger_event(712); stop |
| 1 | 712 | 7 / 3 | 5 | 30 | set_switch(3); stop |
| 1 | 41 | 4 / 1 | 5 | 30 | trigger_event(411); stop |
| 1 | 411 | 4 / 2 | 4 | 30 | trigger_event(412); stop |
| 1 | 412 | 4 / 3 | 6 | 30 | set_switch(9); stop |
| 3 | 502 | 50 / 1 | 6 | 30 | trigger_event(5021); stop |
| 3 | 5021 | 50 / 2 | 6 | 30 | trigger_event(5022); stop |
| 3 | 5022 | 50 / 3 | 6 | 30 | set_switch(2); set_switch(3); stop |
| 3 | 321 | 32 / 1 | 5 | 30 | trigger_event(3211); stop |
| 3 | 3211 | 32 / 2 | 2 | 30 | trigger_event(3212); stop |
| 3 | 3212 | 32 / 3 | 6 | 30 | set_switch(27); set_switch(5); set_switch(7); stop |
| 3 | 341 | 34 / 1 | 5 | 30 | trigger_event(3411); stop |
| 3 | 3411 | 34 / 2 | 8 | 30 | trigger_event(3412); stop |
| 3 | 3412 | 34 / 3 | 6 | 30 | set_switch(6); set_switch(10); stop |
| 3 | 531 | 53 / 1 | 4 | 30 | trigger_event(5311); stop |
| 3 | 5311 | 53 / 2 | 4 | 30 | trigger_event(5312); stop |
| 3 | 5312 | 53 / 3 | 5 | 30 | trigger_event(5313); stop |
| 3 | 5313 | 53 / 4 | 3 | 30 | set_switch(8); set_switch(11); set_switch(12); stop |
| 3 | 101 | 10 / 1 | 4 | 30 | trigger_event(1011); stop |
| 3 | 1011 | 10 / 2 | 5 | 30 | set_switch(8); set_switch(11); set_switch(12); stop |
| 3 | 301 | 30 / 1 | 4 | 30 | trigger_event(3011); stop |
| 3 | 3011 | 30 / 2 | 5 | 30 | trigger_event(3012); stop |
| 3 | 3012 | 30 / 3 | 5 | 30 | stop |
| 3 | 601 | 60 / 1 | 3 | 30 | trigger_event(6011); stop |
| 3 | 6011 | 60 / 2 | 4 | 30 | trigger_event(6012); stop |
| 3 | 6012 | 60 / 3 | 4 | 30 | trigger_event(6013); stop |
| 3 | 6013 | 60 / 4 | 3 | 30 | trigger_event(6014); stop |
| 3 | 6014 | 60 / 5 | 3 | 30 | trigger_event(6015); stop |
| 3 | 6015 | 60 / 6 | 4 | 30 | trigger_event(6016); stop |
| 3 | 6016 | 60 / 7 | 4 | 30 | trigger_event(6017); stop |
| 3 | 6017 | 60 / 8 | 4 | 30 | set_switch(13); set_switch(14); set_switch(15); set_switch(16); set_switch(17); set_switch(18); stop |
| 3 | 111 | 11 / 1 | 0 | 30 | stop |
| 3 | 112 | 11 / 2 | 0 | 30 | trigger_event(1121); stop |
| 3 | 1121 | 11 / 3 | 0 | 30 | stop |
| 3 | 331 | 33 / 1 | 3 | 30 | trigger_event(3311); stop |
| 3 | 3311 | 33 / 2 | 1 | 30 | trigger_event(3312); stop |
| 3 | 3312 | 33 / 3 | 2 | 30 | set_switch(208); stop |
| 3 | 332 | 33 / 4 | 2 | 30 | stop |
| 3 | 511 | 51 / 1 | 2 | 30 | trigger_event(5111); stop |
| 3 | 5111 | 51 / 2 | 4 | 30 | trigger_event(5112); stop |
| 3 | 5112 | 51 / 3 | 3 | 30 | trigger_event(5113); stop |
| 3 | 5113 | 51 / 4 | 6 | 30 | trigger_event(5114); stop |
| 3 | 5114 | 51 / 5 | 6 | 30 | set_switch(19); stop |
| 3 | 202 | 20 / 1 | 2 | 30 | trigger_event(2021); stop |
| 3 | 2021 | 20 / 2 | 3 | 30 | set_switch(20); set_switch(23); stop |
| 3 | 201 | 20 / 3 | 1 | 30 | stop |
| 3 | 311 | 31 / 1 | 4 | 30 | trigger_event(3111); stop |
| 3 | 3111 | 31 / 2 | 3 | 30 | trigger_event(3112); stop |
| 3 | 3112 | 31 / 3 | 5 | 30 | trigger_event(3113); stop |
| 3 | 3113 | 31 / 4 | 4 | 30 | trigger_event(3114); stop |
| 3 | 3114 | 31 / 5 | 6 | 30 | trigger_event(3115); stop |
| 3 | 3115 | 31 / 6 | 6 | 30 | trigger_event(3116); stop |
| 3 | 3116 | 31 / 7 | 5 | 30 | set_switch(25); set_switch(26); set_switch(24); set_switch(22); stop |
| 3 | 521 | 52 / 1 | 1 | 30 | trigger_event(5211); stop |
| 3 | 5211 | 52 / 2 | 1 | 30 | trigger_event(5212); stop |
| 3 | 5212 | 52 / 3 | 1 | 30 | trigger_event(5213); stop |
| 3 | 5213 | 52 / 4 | 1 | 30 | stop |
| 3 | 522 | 52 / 5 | 1 | 30 | trigger_event(5221); stop |
| 3 | 5221 | 52 / 6 | 1 | 30 | trigger_event(5222); stop |
| 3 | 5222 | 52 / 7 | 1 | 30 | trigger_event(5223); stop |
| 3 | 5223 | 52 / 8 | 1 | 30 | stop |
| 3 | 523 | 52 / 9 | 1 | 30 | trigger_event(5231); stop |
| 3 | 5231 | 52 / 10 | 1 | 30 | trigger_event(5232); stop |
| 3 | 5232 | 52 / 11 | 1 | 30 | trigger_event(5233); stop |
| 3 | 5233 | 52 / 12 | 1 | 30 | stop |
| 3 | 524 | 52 / 13 | 1 | 30 | trigger_event(5241); stop |
| 3 | 5241 | 52 / 14 | 1 | 30 | trigger_event(5242); stop |
| 3 | 5242 | 52 / 15 | 1 | 30 | trigger_event(5243); stop |
| 3 | 5243 | 52 / 16 | 1 | 30 | trigger_event(5244); stop |
| 3 | 5244 | 52 / 17 | 3 | 30 | stop |
| 12 | 1 | 1 / 1 | 1 | 50 | construct_objects(room=1,group_or_wave=1); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

A backup is present; decompressed content identical: True. See [text differences](<backup-diff.txt>).

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
