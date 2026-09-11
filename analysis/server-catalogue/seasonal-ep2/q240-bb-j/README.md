# パイオニア クリスマス — seasonal-ep2/q240-bb-j

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/seasonal-ep2/q240-bb-j.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/seasonal-ep2/q240-bb-j.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/seasonal-ep2/q240-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 240; language J. Static scan: **172 objects, 39 enemy/NPC records, 7 events, 791 script labels.** Script roundtrip: byte-identical.

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
0x08, 0x1A, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 49 | 15 | 0 |
| 8 | 123 | 24 | 7 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 8 | 21 | 2 / 1 | 3 | 30 | stop |
| 8 | 22 | 2 / 2 | 3 | 45 | stop |
| 8 | 31 | 3 / 1 | 6 | 30 | stop |
| 8 | 32 | 3 / 2 | 3 | 45 | stop |
| 8 | 41 | 4 / 1 | 5 | 30 | stop |
| 8 | 42 | 4 / 2 | 3 | 45 | stop |
| 8 | 101 | 10 / 1 | 1 | 30 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
