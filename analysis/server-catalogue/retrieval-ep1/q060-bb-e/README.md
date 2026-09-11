# Lost SOUL BLADE — retrieval-ep1/q060-bb-e

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/retrieval-ep1/q060-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/retrieval-ep1/q060-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/retrieval-ep1/q060-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 107; language E. Static scan: **461 objects, 344 enemy/NPC records, 76 events, 68 script labels.** Script roundtrip: byte-identical.

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
0x06, 0x06, 0x00, 0x00, 0x00
0x07, 0x07, 0x00, 0x00, 0x00
0x0D, 0x0D, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 19 | 0 |
| 6 | 194 | 157 | 37 |
| 7 | 212 | 166 | 39 |
| 13 | 29 | 2 | 0 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 6 | 211 | 21 / 1 | 1 | 1 | set_switch(26); set_switch(27); set_switch(28); set_switch(29); set_switch(30); stop |
| 6 | 301 | 30 / 1 | 4 | 1 | trigger_event(3011); stop |
| 6 | 3011 | 30 / 2 | 4 | 60 | trigger_event(3012); stop |
| 6 | 3012 | 30 / 3 | 4 | 20 | trigger_event(3013); stop |
| 6 | 3013 | 30 / 4 | 4 | 1 | set_switch(17); set_switch(18); stop |
| 6 | 501 | 50 / 1 | 4 | 1 | trigger_event(5011); stop |
| 6 | 5011 | 50 / 2 | 4 | 15 | set_switch(2); set_switch(3); set_switch(235); stop |
| 6 | 511 | 51 / 1 | 8 | 1 | trigger_event(5111); stop |
| 6 | 5111 | 51 / 2 | 6 | 1 | trigger_event(5112); stop |
| 6 | 5112 | 51 / 3 | 6 | 30 | trigger_event(5113); stop |
| 6 | 5113 | 51 / 4 | 8 | 15 | trigger_event(5114); stop |
| 6 | 5114 | 51 / 5 | 8 | 60 | set_switch(9); set_switch(11); set_switch(12); set_switch(13); set_switch(38); set_switch(217); set_switch(219); stop |
| 6 | 521 | 52 / 1 | 1 | 1 | trigger_event(5211); stop |
| 6 | 5211 | 52 / 2 | 6 | 30 | trigger_event(5212); stop |
| 6 | 5212 | 52 / 3 | 6 | 10 | set_switch(21); set_switch(22); set_switch(23); stop |
| 6 | 531 | 53 / 1 | 1 | 1 | set_switch(34); set_switch(37); stop |
| 6 | 532 | 53 / 2 | 4 | 1 | set_switch(37); stop |
| 6 | 541 | 54 / 1 | 5 | 1 | trigger_event(5411); stop |
| 6 | 5411 | 54 / 2 | 3 | 15 | trigger_event(5412); stop |
| 6 | 5412 | 54 / 3 | 4 | 30 | trigger_event(5413); stop |
| 6 | 5413 | 54 / 4 | 7 | 45 | set_switch(33); set_switch(34); set_switch(35); set_switch(36); stop |
| 6 | 601 | 60 / 1 | 1 | 1 | trigger_event(6011); stop |
| 6 | 6011 | 60 / 2 | 6 | 1 | set_switch(3); set_switch(5); set_switch(6); set_switch(7); set_switch(8); stop |
| 6 | 611 | 61 / 1 | 1 | 1 | trigger_event(6111); stop |
| 6 | 6111 | 61 / 2 | 4 | 20 | trigger_event(6112); stop |
| 6 | 6112 | 61 / 3 | 6 | 20 | trigger_event(6113); stop |
| 6 | 6113 | 61 / 4 | 4 | 1 | trigger_event(6114); stop |
| 6 | 6114 | 61 / 5 | 2 | 1 | set_switch(31); set_switch(32); set_switch(215); set_switch(220); stop |
| 6 | 752 | 75 / 1 | 4 | 60 | set_switch(14); stop |
| 6 | 753 | 75 / 2 | 4 | 1 | stop |
| 6 | 751 | 75 / 3 | 5 | 1 | trigger_event(7511); stop |
| 6 | 7511 | 75 / 4 | 5 | 1 | set_switch(15); set_switch(16); stop |
| 6 | 901 | 90 / 1 | 3 | 1 | trigger_event(9011); stop |
| 6 | 9011 | 90 / 2 | 3 | 10 | trigger_event(9012); stop |
| 6 | 9012 | 90 / 3 | 3 | 10 | set_switch(19); set_switch(20); set_switch(21); set_switch(22); set_switch(24); set_switch(215); set_switch(220); stop |
| 6 | 902 | 90 / 4 | 3 | 1 | stop |
| 6 | 903 | 90 / 5 | 5 | 1 | set_switch(19); set_switch(20); set_switch(21); set_switch(22); set_switch(24); stop |
| 7 | 211 | 21 / 1 | 1 | 1 | set_switch(17); stop |
| 7 | 301 | 30 / 1 | 6 | 1 | trigger_event(3011); stop |
| 7 | 3011 | 30 / 2 | 6 | 45 | trigger_event(3012); stop |
| 7 | 3012 | 30 / 3 | 8 | 20 | set_switch(15); set_switch(16); stop |
| 7 | 401 | 40 / 1 | 2 | 1 | set_switch(1); set_switch(2); stop |
| 7 | 501 | 50 / 1 | 4 | 1 | trigger_event(5011); stop |
| 7 | 5011 | 50 / 2 | 5 | 1 | set_switch(5); set_switch(235); stop |
| 7 | 511 | 51 / 1 | 5 | 1 | trigger_event(5111); stop |
| 7 | 5111 | 51 / 2 | 3 | 30 | trigger_event(5112); stop |
| 7 | 5112 | 51 / 3 | 2 | 40 | trigger_event(5113); stop |
| 7 | 5113 | 51 / 4 | 5 | 45 | trigger_event(5114); stop |
| 7 | 5114 | 51 / 5 | 3 | 30 | set_switch(21); stop |
| 7 | 521 | 52 / 1 | 8 | 1 | trigger_event(5211); stop |
| 7 | 5211 | 52 / 2 | 5 | 45 | set_switch(10); stop |
| 7 | 531 | 53 / 1 | 8 | 1 | trigger_event(5311); stop |
| 7 | 5311 | 53 / 2 | 8 | 10 | trigger_event(5312); stop |
| 7 | 5312 | 53 / 3 | 2 | 10 | trigger_event(5313); stop |
| 7 | 5313 | 53 / 4 | 2 | 10 | trigger_event(5314); stop |
| 7 | 5314 | 53 / 5 | 2 | 60 | set_switch(17); set_switch(18); set_switch(19); set_switch(20); set_switch(21); set_switch(220); stop |
| 7 | 601 | 60 / 1 | 8 | 1 | trigger_event(6011); stop |
| 7 | 6011 | 60 / 2 | 4 | 30 | trigger_event(6012); stop |
| 7 | 6012 | 60 / 3 | 7 | 30 | trigger_event(6013); stop |
| 7 | 6013 | 60 / 4 | 1 | 1 | trigger_event(6014); stop |
| 7 | 6014 | 60 / 5 | 8 | 60 | trigger_event(6015); stop |
| 7 | 6015 | 60 / 6 | 1 | 30 | trigger_event(6016); stop |
| 7 | 6016 | 60 / 7 | 8 | 1 | trigger_event(6017); stop |
| 7 | 6017 | 60 / 8 | 2 | 1 | set_switch(5); set_switch(6); set_switch(7); set_switch(8); set_switch(9); set_switch(11); set_switch(12); set_switch(215); set_switch(219); stop |
| 7 | 611 | 61 / 1 | 1 | 1 | trigger_event(6111); stop |
| 7 | 6111 | 61 / 2 | 7 | 1 | trigger_event(6112); stop |
| 7 | 6112 | 61 / 3 | 5 | 1 | trigger_event(6113); stop |
| 7 | 6113 | 61 / 4 | 2 | 60 | set_switch(23); set_switch(24); set_switch(25); set_switch(26); stop |
| 7 | 701 | 70 / 1 | 3 | 1 | set_switch(22); stop |
| 7 | 702 | 70 / 2 | 5 | 1 | trigger_event(7021); stop |
| 7 | 7021 | 70 / 3 | 5 | 60 | trigger_event(7022); stop |
| 7 | 7022 | 70 / 4 | 5 | 1 | set_switch(28); set_switch(29); set_switch(30); stop |
| 7 | 801 | 80 / 1 | 3 | 1 | set_switch(11); set_switch(13); stop |
| 7 | 802 | 80 / 2 | 2 | 1 | trigger_event(8021); stop |
| 7 | 8021 | 80 / 3 | 2 | 1 | trigger_event(8022); stop |
| 7 | 8022 | 80 / 4 | 2 | 1 | set_switch(11); set_switch(13); set_switch(14); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

A backup is present; decompressed content identical: True. See [text differences](<backup-diff.txt>).

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
