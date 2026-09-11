# Stage5  — challenge-ep1/c88105-bb-e

Episode1; header quest ID 65535; language E. Static scan: **640 objects, 11 enemy/NPC records, 0 events, 45 script labels.** Script roundtrip: byte-identical.

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
0x07, 0x06, 0x00, 0x03, 0x00
0x08, 0x06, 0x00, 0x01, 0x00
0x09, 0x06, 0x00, 0x04, 0x00
0x0A, 0x06, 0x00, 0x02, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 21 | 11 | 0 |
| 6 | 183 | 0 | 0 |
| 7 | 57 | 0 | 0 |
| 8 | 170 | 0 | 0 |
| 9 | 55 | 0 | 0 |
| 10 | 154 | 0 | 0 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|

## Review notes

- Floor 6: random-format events require separate interpretation
- Floor 7: random-format events require separate interpretation
- Floor 8: random-format events require separate interpretation
- Floor 9: random-format events require separate interpretation
- Floor 10: random-format events require separate interpretation

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
