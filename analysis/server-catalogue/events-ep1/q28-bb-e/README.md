# AOL Cup Sunset Base — events-ep1/q28-bb-e

Episode1; header quest ID 28; language E. Static scan: **366 objects, 150 enemy/NPC records, 20 events, 320 script labels.** Script roundtrip: byte-identical.

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

```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 54 | 20 | 0 |
| 1 | 146 | 34 | 7 |
| 2 | 159 | 87 | 13 |
| 8 | 7 | 9 | 0 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 11 | 1 / 1 | 1 | 1 | stop |
| 1 | 21 | 2 / 1 | 1 | 1 | stop |
| 1 | 51 | 5 / 1 | 8 | 1 | stop |
| 1 | 81 | 8 / 1 | 21 | 1 | stop |
| 1 | 101 | 10 / 1 | 1 | 1 | stop |
| 1 | 111 | 11 / 1 | 1 | 1 | stop |
| 1 | 161 | 16 / 1 | 1 | 1 | stop |
| 2 | 11 | 1 / 1 | 2 | 1 | stop |
| 2 | 21 | 2 / 1 | 5 | 1 | stop |
| 2 | 31 | 3 / 1 | 40 | 1 | stop |
| 2 | 41 | 4 / 1 | 11 | 1 | stop |
| 2 | 51 | 5 / 1 | 2 | 1 | stop |
| 2 | 61 | 6 / 1 | 4 | 1 | stop |
| 2 | 71 | 7 / 1 | 1 | 1 | stop |
| 2 | 101 | 10 / 1 | 7 | 1 | stop |
| 2 | 111 | 11 / 1 | 2 | 1 | stop |
| 2 | 121 | 12 / 1 | 3 | 1 | stop |
| 2 | 131 | 13 / 1 | 3 | 1 | stop |
| 2 | 151 | 15 / 1 | 6 | 1 | stop |
| 2 | 161 | 16 / 1 | 1 | 1 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
