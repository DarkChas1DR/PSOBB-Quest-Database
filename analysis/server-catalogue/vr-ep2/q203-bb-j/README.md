# 届け、この想い — vr-ep2/q203-bb-j

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/vr-ep2/q203-bb-j.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/vr-ep2/q203-bb-j.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/vr-ep2/q203-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 203; language J. Static scan: **168 objects, 73 enemy/NPC records, 19 events, 936 script labels.** Script roundtrip: byte-identical.

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
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 46 | 16 | 0 |
| 3 | 122 | 57 | 19 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 3 | 111 | 11 / 1 | 1 | 1 | stop |
| 3 | 112 | 11 / 2 | 4 | 1 | set_switch(6); set_switch(7); set_switch(8); set_switch(9); set_switch(170); stop |
| 3 | 401 | 40 / 1 | 1 | 1 | stop |
| 3 | 402 | 40 / 2 | 2 | 1 | set_switch(12); set_switch(13); set_switch(171); stop |
| 3 | 412 | 41 / 2 | 2 | 10 | trigger_event(4121); stop |
| 3 | 4121 | 41 / 3 | 2 | 10 | trigger_event(4122); stop |
| 3 | 4122 | 41 / 4 | 3 | 10 | set_switch(18); set_switch(19); set_switch(172); stop |
| 3 | 411 | 41 / 1 | 1 | 1 | stop |
| 3 | 422 | 42 / 2 | 4 | 10 | trigger_event(4221); stop |
| 3 | 4221 | 42 / 3 | 4 | 10 | trigger_event(4222); stop |
| 3 | 4222 | 42 / 4 | 5 | 10 | trigger_event(4223); stop |
| 3 | 4223 | 42 / 5 | 6 | 10 | trigger_event(4224); stop |
| 3 | 4224 | 42 / 6 | 7 | 100 | set_switch(31); set_switch(32); set_switch(33); set_switch(34); set_switch(35); set_switch(36); set_switch(37); set_switch(38); set_switch(39); set_switch(174); stop |
| 3 | 421 | 42 / 1 | 1 | 1 | stop |
| 3 | 501 | 50 / 1 | 10 | 10 | stop |
| 3 | 512 | 51 / 2 | 1 | 10 | trigger_event(5121); stop |
| 3 | 5121 | 51 / 3 | 2 | 10 | trigger_event(5122); stop |
| 3 | 5122 | 51 / 4 | 0 | 10 | set_switch(22); set_switch(23); set_switch(24); set_switch(25); set_switch(26); set_switch(27); set_switch(28); set_switch(173); stop |
| 3 | 511 | 51 / 1 | 1 | 1 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
