# ステージ9 — challenge-ep1/c88109-bb-j

Episode1; header quest ID 65535; language J. Static scan: **970 objects, 12 enemy/NPC records, 1 events, 46 script labels.** Script roundtrip: byte-identical.

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
0x01, 0x0A, 0x00, 0x00, 0x00
0x02, 0x0A, 0x00, 0x03, 0x00
0x03, 0x0A, 0x00, 0x01, 0x00
0x04, 0x0A, 0x00, 0x04, 0x00
0x05, 0x0A, 0x00, 0x02, 0x00
0x0E, 0x0E, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 21 | 11 | 0 |
| 1 | 201 | 0 | 0 |
| 2 | 145 | 0 | 0 |
| 3 | 223 | 0 | 0 |
| 4 | 126 | 0 | 0 |
| 5 | 246 | 0 | 0 |
| 14 | 8 | 1 | 1 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 14 | 1 | 0 / 1 | 1 | 50 | construct_objects(room=0,group_or_wave=1); construct_objects(room=1,group_or_wave=1); construct_objects(room=2,group_or_wave=1); stop |

## Review notes

- Floor 1: random-format events require separate interpretation
- Floor 2: random-format events require separate interpretation
- Floor 3: random-format events require separate interpretation
- Floor 4: random-format events require separate interpretation
- Floor 5: random-format events require separate interpretation

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
