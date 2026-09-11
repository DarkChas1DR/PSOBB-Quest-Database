# Lost RIOT Raygun — retrieval-ep2/q921-bb-e

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/retrieval-ep2/q921-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/retrieval-ep2/q921-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/retrieval-ep2/q921-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 921; language E. Static scan: **410 objects, 421 enemy/NPC records, 74 events, 69 script labels.** Script roundtrip: byte-identical.

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
0x00, 0x12, 0x00, 0x00, 0x00
0x03, 0x15, 0x00, 0x00, 0x00
0x04, 0x16, 0x00, 0x00, 0x00
0x0F, 0x21, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 57 | 16 | 0 |
| 3 | 159 | 206 | 39 |
| 4 | 172 | 198 | 34 |
| 15 | 22 | 1 | 1 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 3 | 101 | 10 / 1 | 5 | 10 | trigger_event(1011); stop |
| 3 | 1011 | 10 / 2 | 5 | 10 | set_switch(28); stop |
| 3 | 111 | 11 / 1 | 6 | 10 | trigger_event(1111); stop |
| 3 | 1111 | 11 / 2 | 6 | 10 | trigger_event(1112); stop |
| 3 | 1112 | 11 / 3 | 6 | 10 | set_switch(6); set_switch(7); stop |
| 3 | 201 | 20 / 1 | 6 | 10 | trigger_event(2011); stop |
| 3 | 2011 | 20 / 2 | 11 | 10 | trigger_event(2012); stop |
| 3 | 2012 | 20 / 3 | 4 | 10 | set_switch(35); stop |
| 3 | 211 | 21 / 1 | 4 | 10 | trigger_event(2111); stop |
| 3 | 2111 | 21 / 2 | 4 | 10 | trigger_event(2112); stop |
| 3 | 2112 | 21 / 3 | 6 | 10 | trigger_event(2113); stop |
| 3 | 2113 | 21 / 4 | 0 | 10 | set_switch(5); stop |
| 3 | 301 | 30 / 1 | 1 | 10 | trigger_event(3011); stop |
| 3 | 3011 | 30 / 2 | 9 | 10 | construct_objects(room=30,group_or_wave=1); stop |
| 3 | 311 | 31 / 1 | 2 | 0 | stop |
| 3 | 321 | 32 / 1 | 7 | 150 | set_switch(31); set_switch(32); stop |
| 3 | 330 | 33 / 1 | 1 | 0 | stop |
| 3 | 401 | 40 / 1 | 3 | 10 | trigger_event(4011); stop |
| 3 | 4011 | 40 / 2 | 4 | 10 | set_switch(8); set_switch(9); stop |
| 3 | 402 | 40 / 4 | 4 | 10 | trigger_event(4100); stop |
| 3 | 4100 | 40 / 5 | 2 | 10 | set_switch(10); set_switch(11); stop |
| 3 | 411 | 41 / 1 | 8 | 10 | trigger_event(4111); stop |
| 3 | 4111 | 41 / 2 | 4 | 10 | trigger_event(4112); stop |
| 3 | 4112 | 41 / 3 | 3 | 10 | set_switch(18); set_switch(19); stop |
| 3 | 421 | 42 / 1 | 5 | 0 | trigger_event(4211); stop |
| 3 | 4211 | 42 / 2 | 5 | 10 | trigger_event(4212); stop |
| 3 | 4212 | 42 / 3 | 10 | 10 | trigger_event(4213); stop |
| 3 | 4213 | 42 / 4 | 3 | 10 | set_switch(29); set_switch(30); stop |
| 3 | 501 | 50 / 1 | 6 | 10 | trigger_event(5011); stop |
| 3 | 5011 | 50 / 2 | 6 | 10 | set_switch(17); set_switch(104); stop |
| 3 | 511 | 51 / 1 | 12 | 10 | trigger_event(5111); stop |
| 3 | 5111 | 51 / 2 | 5 | 10 | set_switch(22); set_switch(23); set_switch(24); set_switch(25); stop |
| 3 | 521 | 52 / 1 | 9 | 10 | trigger_event(5211); stop |
| 3 | 5211 | 52 / 2 | 8 | 1 | trigger_event(5212); stop |
| 3 | 5212 | 52 / 3 | 8 | 1 | trigger_event(5213); stop |
| 3 | 5213 | 52 / 4 | 5 | 60 | trigger_event(5214); stop |
| 3 | 5214 | 52 / 5 | 11 | 10 | set_switch(36); set_switch(37); set_switch(38); set_switch(39); stop |
| 3 | 4101 | 101 / 1 | 1 | 0 | stop |
| 3 | 5102 | 102 / 1 | 1 | 0 | stop |
| 4 | 101 | 10 / 1 | 7 | 10 | trigger_event(1011); stop |
| 4 | 1011 | 10 / 2 | 4 | 10 | set_switch(17); set_switch(18); set_switch(39); set_switch(40); stop |
| 4 | 121 | 12 / 1 | 6 | 10 | trigger_event(1211); stop |
| 4 | 1211 | 12 / 2 | 8 | 10 | set_switch(33); stop |
| 4 | 201 | 20 / 1 | 6 | 10 | trigger_event(2011); stop |
| 4 | 2011 | 20 / 2 | 4 | 10 | set_switch(15); set_switch(16); stop |
| 4 | 211 | 21 / 1 | 14 | 10 | trigger_event(2111); stop |
| 4 | 2111 | 21 / 2 | 4 | 250 | set_switch(9); set_switch(10); stop |
| 4 | 301 | 30 / 1 | 9 | 10 | set_switch(25); stop |
| 4 | 311 | 31 / 1 | 4 | 10 | trigger_event(3111); stop |
| 4 | 3111 | 31 / 2 | 4 | 10 | set_switch(13); set_switch(14); stop |
| 4 | 401 | 40 / 1 | 9 | 10 | trigger_event(4011); stop |
| 4 | 4011 | 40 / 2 | 7 | 10 | trigger_event(4012); stop |
| 4 | 4012 | 40 / 3 | 6 | 10 | trigger_event(4013); stop |
| 4 | 4013 | 40 / 4 | 9 | 10 | set_switch(35); set_switch(36); set_switch(37); set_switch(38); stop |
| 4 | 411 | 41 / 1 | 1 | 10 | trigger_event(4111); stop |
| 4 | 4111 | 41 / 2 | 2 | 10 | trigger_event(4112); stop |
| 4 | 4112 | 41 / 3 | 3 | 10 | trigger_event(4113); stop |
| 4 | 4113 | 41 / 4 | 4 | 10 | trigger_event(4114); stop |
| 4 | 4114 | 41 / 5 | 5 | 10 | trigger_event(4115); stop |
| 4 | 4115 | 41 / 6 | 6 | 10 | trigger_event(4116); stop |
| 4 | 4116 | 41 / 7 | 7 | 10 | set_switch(101); set_switch(27); set_switch(30); stop |
| 4 | 421 | 42 / 1 | 9 | 10 | trigger_event(4211); stop |
| 4 | 4211 | 42 / 2 | 0 | 10 | set_switch(12); stop |
| 4 | 422 | 42 / 3 | 0 | 10 | stop |
| 4 | 501 | 50 / 1 | 2 | 10 | set_switch(20); set_switch(22); set_switch(23); stop |
| 4 | 502 | 50 / 2 | 5 | 10 | stop |
| 4 | 511 | 51 / 1 | 9 | 10 | trigger_event(5111); stop |
| 4 | 5111 | 51 / 2 | 8 | 10 | trigger_event(5112); stop |
| 4 | 5112 | 51 / 3 | 7 | 10 | set_switch(5); stop |
| 4 | 521 | 52 / 1 | 10 | 10 | trigger_event(5211); stop |
| 4 | 5211 | 52 / 2 | 8 | 10 | trigger_event(5212); stop |
| 4 | 5212 | 52 / 3 | 7 | 10 | set_switch(31); set_switch(32); stop |
| 4 | 1611 | 161 / 1 | 4 | 0 | set_switch(34); stop |
| 15 | 1 | 1 / 1 | 1 | 50 | construct_objects(room=1,group_or_wave=1); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

A backup is present; decompressed content identical: False. See [text differences](<backup-diff.txt>).

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
