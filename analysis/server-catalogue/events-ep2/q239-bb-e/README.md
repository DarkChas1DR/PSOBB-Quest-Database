# Beach Laughter — events-ep2/q239-bb-e

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/events-ep2/q239-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/events-ep2/q239-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/events-ep2/q239-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 239; language E. Static scan: **163 objects, 155 enemy/NPC records, 20 events, 371 script labels.** Script roundtrip: byte-identical.

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
0x05, 0x1A, 0x00, 0x00, 0x00
0x06, 0x1A, 0x00, 0x00, 0x00
0x07, 0x1A, 0x00, 0x00, 0x00
0x08, 0x1A, 0x00, 0x00, 0x00
0x10, 0x22, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 54 | 20 | 0 |
| 5 | 14 | 30 | 4 |
| 6 | 14 | 30 | 4 |
| 7 | 14 | 30 | 4 |
| 8 | 14 | 30 | 4 |
| 16 | 53 | 15 | 4 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 5 | 41 | 4 / 1 | 1 | 0 | stop |
| 5 | 42 | 4 / 2 | 1 | 960 | stop |
| 5 | 43 | 4 / 3 | 17 | 1260 | stop |
| 5 | 44 | 4 / 4 | 11 | 1710 | stop |
| 6 | 41 | 4 / 1 | 1 | 0 | stop |
| 6 | 42 | 4 / 2 | 1 | 960 | stop |
| 6 | 43 | 4 / 3 | 17 | 1260 | stop |
| 6 | 44 | 4 / 4 | 11 | 1710 | stop |
| 7 | 41 | 4 / 1 | 1 | 0 | stop |
| 7 | 42 | 4 / 2 | 1 | 960 | stop |
| 7 | 43 | 4 / 3 | 17 | 1260 | stop |
| 7 | 44 | 4 / 4 | 11 | 1710 | stop |
| 8 | 41 | 4 / 1 | 1 | 0 | stop |
| 8 | 42 | 4 / 2 | 1 | 960 | stop |
| 8 | 43 | 4 / 3 | 17 | 1260 | stop |
| 8 | 44 | 4 / 4 | 11 | 1710 | stop |
| 16 | 61 | 6 / 1 | 3 | 30 | stop |
| 16 | 71 | 7 / 1 | 1 | 30 | stop |
| 16 | 91 | 9 / 1 | 7 | 30 | stop |
| 16 | 111 | 11 / 1 | 4 | 30 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
