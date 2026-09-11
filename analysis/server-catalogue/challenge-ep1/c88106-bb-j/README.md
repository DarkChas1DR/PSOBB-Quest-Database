# ステージ6 — challenge-ep1/c88106-bb-j

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/challenge-ep1/c88106-bb-j.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/challenge-ep1/c88106-bb-j.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/challenge-ep1/c88106-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 65535; language J. Static scan: **690 objects, 13 enemy/NPC records, 0 events, 46 script labels.** Script roundtrip: alignment-only.

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
0x07, 0x07, 0x00, 0x00, 0x00
0x08, 0x07, 0x00, 0x03, 0x00
0x09, 0x07, 0x00, 0x01, 0x00
0x0A, 0x07, 0x00, 0x04, 0x00
0x0B, 0x07, 0x00, 0x02, 0x00
0x0D, 0x0D, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 21 | 11 | 0 |
| 7 | 147 | 0 | 0 |
| 8 | 73 | 0 | 0 |
| 9 | 157 | 0 | 0 |
| 10 | 107 | 0 | 0 |
| 11 | 173 | 0 | 0 |
| 13 | 12 | 2 | 0 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|

## Review notes

- Floor 7: random-format events require separate interpretation
- Floor 8: random-format events require separate interpretation
- Floor 9: random-format events require separate interpretation
- Floor 10: random-format events require separate interpretation
- Floor 11: random-format events require separate interpretation

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
