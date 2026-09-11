# ６－５：適合試験１０ ＶＲ宇宙船５ — government-ep2/q460-bb-j

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/government-ep2/q460-bb-j.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep2/q460-bb-j.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep2/q460-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 460; language J. Static scan: **456 objects, 251 enemy/NPC records, 54 events, 115 script labels.** Script roundtrip: byte-identical.

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
0x03, 0x15, 0x00, 0x01, 0x00
0x04, 0x16, 0x00, 0x01, 0x00
0x0F, 0x21, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 53 | 19 | 0 |
| 3 | 184 | 121 | 26 |
| 4 | 196 | 110 | 27 |
| 15 | 23 | 1 | 1 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 3 | 101 | 10 / 1 | 4 | 1 | set_switch(5); set_switch(6); stop |
| 3 | 111 | 11 / 1 | 6 | 150 | set_switch(37); stop |
| 3 | 201 | 20 / 1 | 4 | 1 | set_switch(43); set_switch(7); set_switch(8); stop |
| 3 | 301 | 30 / 1 | 5 | 100 | set_switch(27); stop |
| 3 | 311 | 31 / 1 | 5 | 10 | trigger_event(3111); stop |
| 3 | 3111 | 31 / 2 | 5 | 60 | set_switch(39); set_switch(40); set_switch(41); set_switch(42); stop |
| 3 | 321 | 32 / 1 | 4 | 10 | trigger_event(3211); stop |
| 3 | 3211 | 32 / 2 | 6 | 60 | set_switch(19); set_switch(23); set_switch(25); set_switch(28); stop |
| 3 | 401 | 40 / 1 | 6 | 10 | trigger_event(4011); stop |
| 3 | 4011 | 40 / 2 | 5 | 10 | trigger_event(4012); stop |
| 3 | 4012 | 40 / 3 | 5 | 90 | set_switch(5); set_switch(6); set_switch(7); set_switch(8); set_switch(9); set_switch(10); stop |
| 3 | 411 | 41 / 1 | 6 | 1 | trigger_event(4111); stop |
| 3 | 4111 | 41 / 2 | 6 | 1 | trigger_event(4112); stop |
| 3 | 4112 | 41 / 3 | 6 | 1 | set_switch(35); set_switch(36); stop |
| 3 | 421 | 42 / 1 | 2 | 60 | trigger_event(4211); stop |
| 3 | 4211 | 42 / 2 | 5 | 10 | set_switch(29); set_switch(30); set_switch(31); set_switch(32); set_switch(33); set_switch(34); stop |
| 3 | 501 | 50 / 1 | 6 | 1 | trigger_event(5011); stop |
| 3 | 5011 | 50 / 2 | 5 | 150 | set_switch(38); stop |
| 3 | 511 | 51 / 1 | 5 | 1 | trigger_event(5111); stop |
| 3 | 5111 | 51 / 2 | 6 | 30 | trigger_event(5112); stop |
| 3 | 5112 | 51 / 3 | 5 | 90 | trigger_event(5113); stop |
| 3 | 5113 | 51 / 4 | 3 | 100 | set_switch(11); set_switch(12); set_switch(13); set_switch(14); set_switch(15); set_switch(16); stop |
| 3 | 521 | 52 / 1 | 2 | 1 | trigger_event(5211); stop |
| 3 | 5211 | 52 / 2 | 4 | 1 | set_switch(17); set_switch(18); set_switch(20); set_switch(21); set_switch(22); set_switch(24); set_switch(26); stop |
| 3 | 522 | 52 / 3 | 3 | 1 | stop |
| 3 | 1921 | 192 / 1 | 2 | 1 | stop |
| 4 | 111 | 11 / 1 | 5 | 10 | set_switch(23); stop |
| 4 | 201 | 20 / 1 | 4 | 100 | set_switch(19); set_switch(20); set_switch(21); set_switch(22); stop |
| 4 | 211 | 21 / 1 | 4 | 100 | set_switch(38); stop |
| 4 | 311 | 31 / 1 | 3 | 100 | trigger_event(3111); stop |
| 4 | 3111 | 31 / 2 | 0 | 1 | set_switch(40); set_switch(41); set_switch(42); set_switch(43); stop |
| 4 | 321 | 32 / 1 | 3 | 60 | set_switch(36); set_switch(37); stop |
| 4 | 331 | 33 / 1 | 2 | 10 | trigger_event(3311); stop |
| 4 | 3311 | 33 / 2 | 4 | 10 | set_switch(15); set_switch(16); stop |
| 4 | 401 | 40 / 1 | 7 | 60 | trigger_event(4011); stop |
| 4 | 4011 | 40 / 2 | 5 | 30 | set_switch(13); set_switch(14); set_switch(17); set_switch(18); stop |
| 4 | 411 | 41 / 1 | 5 | 60 | trigger_event(4111); stop |
| 4 | 4111 | 41 / 2 | 5 | 30 | trigger_event(4112); stop |
| 4 | 4112 | 41 / 3 | 5 | 30 | trigger_event(4113); stop |
| 4 | 4113 | 41 / 4 | 4 | 150 | set_switch(31); set_switch(32); set_switch(33); set_switch(34); set_switch(35); stop |
| 4 | 421 | 42 / 1 | 5 | 1 | trigger_event(4211); stop |
| 4 | 4211 | 42 / 2 | 4 | 1 | set_switch(7); set_switch(8); stop |
| 4 | 501 | 50 / 1 | 5 | 60 | trigger_event(5011); stop |
| 4 | 5011 | 50 / 2 | 6 | 30 | trigger_event(5012); stop |
| 4 | 5012 | 50 / 3 | 5 | 150 | set_switch(9); set_switch(10); set_switch(11); set_switch(12); stop |
| 4 | 502 | 50 / 4 | 5 | 1 | stop |
| 4 | 511 | 51 / 1 | 5 | 1 | trigger_event(5111); stop |
| 4 | 5111 | 51 / 2 | 6 | 1 | set_switch(24); set_switch(25); set_switch(26); set_switch(27); set_switch(28); set_switch(29); set_switch(30); stop |
| 4 | 521 | 52 / 1 | 6 | 1 | trigger_event(5211); stop |
| 4 | 5211 | 52 / 2 | 3 | 60 | set_switch(39); stop |
| 4 | 1401 | 140 / 1 | 1 | 1 | stop |
| 4 | 1901 | 190 / 1 | 1 | 1 | stop |
| 4 | 1911 | 191 / 1 | 2 | 1 | stop |
| 15 | 1 | 1 / 1 | 1 | 50 | construct_objects(room=1,group_or_wave=1); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
