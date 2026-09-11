# Mop-up Operation #2 — extermination-ep1/q102-bb-e

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/extermination-ep1/q102-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/extermination-ep1/q102-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/extermination-ep1/q102-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 102; language E. Static scan: **182 objects, 172 enemy/NPC records, 37 events, 103 script labels.** Script roundtrip: byte-identical.

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
0x03, 0x03, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 28 | 18 | 0 |
| 3 | 154 | 154 | 37 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 3 | 502 | 50 / 2 | 5 | 1 | trigger_event(5021); stop |
| 3 | 5021 | 50 / 3 | 6 | 1 | trigger_event(5022); stop |
| 3 | 5022 | 50 / 4 | 3 | 1 | trigger_event(5023); stop |
| 3 | 5023 | 50 / 1 | 4 | 1 | set_switch(2); set_switch(3); stop |
| 3 | 321 | 32 / 1 | 6 | 1 | trigger_event(3211); stop |
| 3 | 3211 | 32 / 2 | 6 | 1 | trigger_event(3212); stop |
| 3 | 3212 | 32 / 3 | 5 | 1 | set_switch(27); set_switch(5); set_switch(7); set_switch(8); set_switch(11); set_switch(12); stop |
| 3 | 341 | 34 / 1 | 3 | 1 | trigger_event(3411); stop |
| 3 | 3411 | 34 / 2 | 3 | 1 | trigger_event(3412); stop |
| 3 | 3412 | 34 / 3 | 3 | 1 | stop |
| 3 | 342 | 34 / 4 | 1 | 1 | trigger_event(3421); stop |
| 3 | 3421 | 34 / 5 | 3 | 1 | trigger_event(3422); stop |
| 3 | 3422 | 34 / 6 | 2 | 1 | set_switch(10); stop |
| 3 | 531 | 53 / 1 | 6 | 1 | trigger_event(5311); stop |
| 3 | 5311 | 53 / 2 | 4 | 1 | trigger_event(5312); stop |
| 3 | 5312 | 53 / 3 | 5 | 1 | trigger_event(5313); stop |
| 3 | 5313 | 53 / 4 | 5 | 1 | set_switch(8); set_switch(11); set_switch(12); set_switch(9); stop |
| 3 | 601 | 60 / 1 | 5 | 1 | trigger_event(6011); stop |
| 3 | 6011 | 60 / 2 | 6 | 1 | trigger_event(6012); stop |
| 3 | 6012 | 60 / 3 | 7 | 1 | trigger_event(6013); stop |
| 3 | 6013 | 60 / 4 | 6 | 1 | set_switch(13); set_switch(14); stop |
| 3 | 113 | 11 / 1 | 4 | 1 | trigger_event(1111); stop |
| 3 | 1111 | 11 / 2 | 5 | 1 | trigger_event(1112); stop |
| 3 | 1112 | 11 / 3 | 3 | 1 | set_switch(17); set_switch(18); stop |
| 3 | 511 | 51 / 1 | 4 | 1 | trigger_event(5111); stop |
| 3 | 5111 | 51 / 2 | 4 | 1 | trigger_event(5112); stop |
| 3 | 5112 | 51 / 3 | 6 | 1 | trigger_event(5113); stop |
| 3 | 5113 | 51 / 4 | 6 | 1 | trigger_event(5114); stop |
| 3 | 5114 | 51 / 5 | 6 | 1 | set_switch(19); set_switch(20); set_switch(23); set_switch(25); set_switch(26); set_switch(24); set_switch(22); stop |
| 3 | 521 | 52 / 1 | 2 | 1 | trigger_event(5211); stop |
| 3 | 5211 | 52 / 2 | 3 | 1 | trigger_event(5212); stop |
| 3 | 5212 | 52 / 3 | 3 | 1 | trigger_event(5213); stop |
| 3 | 5213 | 52 / 4 | 3 | 1 | stop |
| 3 | 522 | 52 / 5 | 2 | 1 | trigger_event(5221); stop |
| 3 | 5221 | 52 / 6 | 4 | 1 | trigger_event(5222); stop |
| 3 | 5222 | 52 / 7 | 3 | 1 | trigger_event(5223); stop |
| 3 | 5223 | 52 / 8 | 2 | 1 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

A backup is present; decompressed content identical: True. See [text differences](<backup-diff.txt>).

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
