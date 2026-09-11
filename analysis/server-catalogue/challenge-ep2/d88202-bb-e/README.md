# Stage2 — challenge-ep2/d88202-bb-e

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/challenge-ep2/d88202-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/challenge-ep2/d88202-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/challenge-ep2/d88202-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 65535; language E. Static scan: **985 objects, 429 enemy/NPC records, 117 events, 56 script labels.** Script roundtrip: byte-identical.

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
0x01, 0x15, 0x00, 0x00, 0x00
0x02, 0x15, 0x00, 0x02, 0x00
0x03, 0x15, 0x00, 0x01, 0x00
0x04, 0x16, 0x00, 0x00, 0x00
0x05, 0x16, 0x00, 0x02, 0x00
0x06, 0x16, 0x00, 0x01, 0x00
0x0F, 0x21, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 40 | 12 | 0 |
| 1 | 186 | 51 | 17 |
| 2 | 91 | 40 | 12 |
| 3 | 184 | 48 | 18 |
| 4 | 197 | 106 | 25 |
| 5 | 88 | 59 | 19 |
| 6 | 193 | 112 | 25 |
| 15 | 6 | 1 | 1 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 111 | 11 / 1 | 3 | 1 | set_switch(5); stop |
| 1 | 201 | 20 / 1 | 4 | 1 | trigger_event(2011); stop |
| 1 | 2011 | 20 / 2 | 4 | 60 | set_switch(33); stop |
| 1 | 211 | 21 / 1 | 3 | 1 | set_switch(1); set_switch(2); set_switch(3); set_switch(4); set_switch(38); set_switch(39); stop |
| 1 | 301 | 30 / 1 | 1 | 1 | set_switch(10); set_switch(11); stop |
| 1 | 311 | 31 / 1 | 2 | 1 | set_switch(20); stop |
| 1 | 321 | 32 / 1 | 2 | 1 | set_switch(31); set_switch(32); stop |
| 1 | 401 | 40 / 1 | 3 | 60 | trigger_event(4011); stop |
| 1 | 4011 | 40 / 2 | 4 | 100 | trigger_event(4012); stop |
| 1 | 4012 | 40 / 3 | 1 | 200 | set_switch(6); set_switch(7); set_switch(8); set_switch(9); stop |
| 1 | 411 | 41 / 1 | 3 | 10 | set_switch(14); set_switch(17); stop |
| 1 | 421 | 42 / 1 | 5 | 10 | set_switch(26); set_switch(27); set_switch(28); set_switch(29); set_switch(30); stop |
| 1 | 501 | 50 / 1 | 4 | 10 | set_switch(12); set_switch(13); set_switch(15); set_switch(16); stop |
| 1 | 511 | 51 / 1 | 2 | 1 | trigger_event(5111); stop |
| 1 | 5111 | 51 / 2 | 2 | 60 | set_switch(18); set_switch(19); set_switch(21); stop |
| 1 | 521 | 52 / 1 | 5 | 1 | set_switch(34); set_switch(35); set_switch(36); set_switch(37); stop |
| 1 | 1401 | 140 / 1 | 1 | 1 | stop |
| 2 | 101 | 10 / 1 | 1 | 10 | set_switch(13); set_switch(14); set_switch(15); set_switch(16); set_switch(17); set_switch(18); set_switch(24); set_switch(25); stop |
| 2 | 102 | 10 / 2 | 5 | 100 | stop |
| 2 | 201 | 20 / 1 | 1 | 60 | set_switch(5); set_switch(6); stop |
| 2 | 202 | 20 / 2 | 3 | 60 | stop |
| 2 | 401 | 40 / 1 | 1 | 30 | set_switch(7); set_switch(8); set_switch(9); set_switch(10); stop |
| 2 | 402 | 40 / 2 | 6 | 30 | stop |
| 2 | 411 | 41 / 1 | 1 | 200 | set_switch(21); set_switch(22); set_switch(23); stop |
| 2 | 412 | 41 / 2 | 7 | 1 | stop |
| 2 | 501 | 50 / 1 | 1 | 1 | set_switch(11); set_switch(12); set_switch(13); set_switch(14); stop |
| 2 | 502 | 50 / 2 | 6 | 60 | stop |
| 2 | 511 | 51 / 1 | 1 | 200 | set_switch(19); set_switch(20); stop |
| 2 | 512 | 51 / 2 | 7 | 10 | stop |
| 3 | 201 | 20 / 1 | 3 | 30 | set_switch(1); set_switch(2); set_switch(5); set_switch(6); set_switch(43); stop |
| 3 | 211 | 21 / 1 | 1 | 10 | set_switch(20); set_switch(24); set_switch(26); stop |
| 3 | 311 | 31 / 1 | 3 | 30 | set_switch(38); stop |
| 3 | 321 | 32 / 1 | 1 | 10 | set_switch(19); set_switch(23); set_switch(25); stop |
| 3 | 401 | 40 / 1 | 1 | 100 | set_switch(7); set_switch(8); set_switch(9); set_switch(10); stop |
| 3 | 411 | 41 / 1 | 5 | 10 | trigger_event(4111); stop |
| 3 | 4111 | 41 / 2 | 6 | 10 | set_switch(3); set_switch(4); set_switch(35); set_switch(36); stop |
| 3 | 421 | 42 / 1 | 4 | 100 | trigger_event(4211); stop |
| 3 | 4211 | 42 / 2 | 0 | 100 | set_switch(33); set_switch(34); stop |
| 3 | 501 | 50 / 1 | 4 | 1 | trigger_event(5011); stop |
| 3 | 5011 | 50 / 2 | 3 | 100 | set_switch(3); set_switch(4); set_switch(37); stop |
| 3 | 511 | 51 / 1 | 4 | 10 | trigger_event(5111); stop |
| 3 | 5111 | 51 / 2 | 2 | 10 | set_switch(11); set_switch(12); set_switch(13); set_switch(14); set_switch(15); set_switch(16); stop |
| 3 | 521 | 52 / 1 | 6 | 10 | trigger_event(5211); stop |
| 3 | 5211 | 52 / 2 | 1 | 10 | set_switch(17); set_switch(18); set_switch(21); set_switch(22); stop |
| 3 | 1811 | 181 / 1 | 1 | 1 | stop |
| 3 | 1901 | 190 / 1 | 2 | 1 | stop |
| 3 | 1921 | 192 / 1 | 1 | 1 | stop |
| 4 | 111 | 11 / 1 | 5 | 1 | construct_objects(room=11,group_or_wave=27); set_switch(27); stop |
| 4 | 121 | 12 / 1 | 3 | 100 | trigger_event(1211); stop |
| 4 | 1211 | 12 / 2 | 3 | 1 | trigger_event(1212); stop |
| 4 | 1212 | 12 / 3 | 3 | 10 | construct_objects(room=12,group_or_wave=32); set_switch(32); stop |
| 4 | 201 | 20 / 1 | 4 | 60 | set_switch(13); set_switch(14); stop |
| 4 | 211 | 21 / 1 | 2 | 60 | set_switch(9); set_switch(10); stop |
| 4 | 301 | 30 / 1 | 3 | 100 | set_switch(15); set_switch(16); set_switch(17); set_switch(18); set_switch(25); set_switch(39); set_switch(40); stop |
| 4 | 311 | 31 / 1 | 5 | 60 | set_switch(11); set_switch(12); stop |
| 4 | 401 | 40 / 1 | 4 | 1 | trigger_event(4011); stop |
| 4 | 4011 | 40 / 2 | 4 | 1 | construct_objects(room=40,group_or_wave=34); set_switch(34); stop |
| 4 | 411 | 41 / 1 | 5 | 1 | trigger_event(4111); stop |
| 4 | 4111 | 41 / 2 | 5 | 150 | trigger_event(4112); stop |
| 4 | 4112 | 41 / 3 | 2 | 1 | construct_objects(room=41,group_or_wave=28); set_switch(28); stop |
| 4 | 421 | 42 / 1 | 6 | 120 | trigger_event(4211); stop |
| 4 | 4211 | 42 / 2 | 3 | 1 | set_switch(1); set_switch(2); set_switch(3); set_switch(4); set_switch(5); set_switch(6); set_switch(7); set_switch(8); stop |
| 4 | 501 | 50 / 1 | 9 | 1 | trigger_event(5011); stop |
| 4 | 5011 | 50 / 2 | 6 | 1 | trigger_event(5012); stop |
| 4 | 5012 | 50 / 3 | 5 | 100 | trigger_event(5013); stop |
| 4 | 5013 | 50 / 4 | 2 | 1 | trigger_event(5014); stop |
| 4 | 5014 | 50 / 5 | 1 | 200 | set_switch(19); set_switch(20); set_switch(21); set_switch(22); set_switch(23); stop |
| 4 | 511 | 51 / 1 | 9 | 100 | stop |
| 4 | 521 | 52 / 1 | 4 | 150 | trigger_event(5211); stop |
| 4 | 5211 | 52 / 2 | 4 | 1 | trigger_event(5212); stop |
| 4 | 5212 | 52 / 3 | 3 | 1 | construct_objects(room=52,group_or_wave=30); set_switch(30); stop |
| 4 | 1811 | 181 / 1 | 6 | 1 | stop |
| 5 | 101 | 10 / 1 | 5 | 1 | set_switch(20); set_switch(21); stop |
| 5 | 111 | 11 / 1 | 2 | 1 | stop |
| 5 | 112 | 11 / 2 | 1 | 100 | stop |
| 5 | 113 | 11 / 3 | 1 | 200 | stop |
| 5 | 114 | 11 / 4 | 1 | 300 | stop |
| 5 | 115 | 11 / 5 | 1 | 400 | stop |
| 5 | 116 | 11 / 6 | 1 | 500 | set_switch(1); set_switch(2); set_switch(3); set_switch(4); stop |
| 5 | 201 | 20 / 1 | 2 | 1 | set_switch(13); set_switch(14); set_switch(15); set_switch(30); stop |
| 5 | 202 | 20 / 2 | 5 | 60 | stop |
| 5 | 211 | 21 / 1 | 1 | 1 | set_switch(9); set_switch(10); set_switch(11); set_switch(12); stop |
| 5 | 212 | 21 / 2 | 9 | 120 | stop |
| 5 | 301 | 30 / 1 | 2 | 10 | set_switch(18); set_switch(19); stop |
| 5 | 302 | 30 / 2 | 5 | 10 | stop |
| 5 | 311 | 31 / 1 | 1 | 10 | set_switch(6); set_switch(5); stop |
| 5 | 312 | 31 / 2 | 5 | 10 | stop |
| 5 | 401 | 40 / 1 | 3 | 10 | set_switch(16); set_switch(17); stop |
| 5 | 402 | 40 / 2 | 5 | 100 | stop |
| 5 | 501 | 50 / 1 | 2 | 10 | set_switch(8); set_switch(7); stop |
| 5 | 502 | 50 / 2 | 7 | 10 | stop |
| 6 | 211 | 21 / 1 | 8 | 1 | set_switch(36); set_switch(37); stop |
| 6 | 212 | 21 / 2 | 0 | 60 | stop |
| 6 | 301 | 30 / 1 | 4 | 30 | trigger_event(3011); stop |
| 6 | 3011 | 30 / 2 | 4 | 30 | trigger_event(3012); stop |
| 6 | 3012 | 30 / 3 | 5 | 30 | set_switch(1); set_switch(2); set_switch(3); set_switch(4); set_switch(9); set_switch(10); stop |
| 6 | 322 | 32 / 1 | 2 | 150 | set_switch(31); set_switch(32); set_switch(33); set_switch(34); set_switch(35); stop |
| 6 | 331 | 33 / 1 | 2 | 150 | set_switch(9); set_switch(10); set_switch(15); stop |
| 6 | 401 | 40 / 1 | 2 | 150 | set_switch(13); set_switch(14); set_switch(17); set_switch(18); set_switch(19); set_switch(20); set_switch(21); set_switch(22); set_switch(39); set_switch(40); set_switch(41); set_switch(42); set_switch(43); stop |
| 6 | 411 | 41 / 1 | 6 | 10 | trigger_event(4111); stop |
| 6 | 4111 | 41 / 2 | 7 | 10 | trigger_event(4112); stop |
| 6 | 4112 | 41 / 3 | 6 | 10 | set_switch(28); set_switch(29); set_switch(30); stop |
| 6 | 421 | 42 / 1 | 6 | 10 | trigger_event(4211); stop |
| 6 | 4211 | 42 / 2 | 5 | 10 | trigger_event(4212); stop |
| 6 | 4212 | 42 / 3 | 6 | 10 | set_switch(5); set_switch(6); set_switch(18); set_switch(19); set_switch(20); set_switch(21); set_switch(22); set_switch(39); set_switch(40); set_switch(41); set_switch(42); set_switch(43); stop |
| 6 | 501 | 50 / 1 | 8 | 1 | stop |
| 6 | 511 | 51 / 1 | 3 | 10 | trigger_event(5111); stop |
| 6 | 5111 | 51 / 2 | 6 | 10 | trigger_event(5112); stop |
| 6 | 5112 | 51 / 3 | 3 | 100 | set_switch(24); set_switch(25); set_switch(26); set_switch(27); stop |
| 6 | 521 | 52 / 1 | 8 | 1 | trigger_event(5211); stop |
| 6 | 5211 | 52 / 2 | 6 | 10 | set_switch(38); stop |
| 6 | 1401 | 140 / 1 | 4 | 1 | stop |
| 6 | 1411 | 141 / 1 | 2 | 1 | stop |
| 6 | 1601 | 160 / 1 | 1 | 90 | stop |
| 6 | 1821 | 182 / 1 | 4 | 1 | stop |
| 6 | 1901 | 190 / 1 | 4 | 1 | stop |
| 15 | 1 | 1 / 1 | 1 | 50 | construct_objects(room=1,group_or_wave=1); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
