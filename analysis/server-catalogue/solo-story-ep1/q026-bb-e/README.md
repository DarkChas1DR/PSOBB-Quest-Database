# Central Dome Fire Swirl — solo-story-ep1/q026-bb-e

Episode1; header quest ID 26; language E. Static scan: **283 objects, 136 enemy/NPC records, 25 events, 326 script labels.** Script roundtrip: byte-identical.

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
0x02, 0x02, 0x00, 0x00, 0x02
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 18 | 0 |
| 2 | 257 | 118 | 25 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 2 | 21 | 2 / 1 | 4 | 1 | trigger_event(211); stop |
| 2 | 211 | 2 / 2 | 4 | 15 | trigger_event(212); stop |
| 2 | 212 | 2 / 3 | 4 | 10 | stop |
| 2 | 131 | 13 / 1 | 4 | 1 | trigger_event(1311); stop |
| 2 | 1311 | 13 / 2 | 4 | 20 | trigger_event(1312); stop |
| 2 | 1312 | 13 / 3 | 4 | 40 | trigger_event(1313); stop |
| 2 | 1313 | 13 / 4 | 5 | 10 | set_switch(22); stop |
| 2 | 111 | 11 / 1 | 6 | 45 | trigger_event(1111); stop |
| 2 | 1111 | 11 / 2 | 4 | 30 | trigger_event(1112); stop |
| 2 | 1112 | 11 / 3 | 7 | 1 | set_switch(11); stop |
| 2 | 151 | 15 / 1 | 5 | 1 | trigger_event(1511); stop |
| 2 | 1511 | 15 / 2 | 5 | 1 | trigger_event(1512); stop |
| 2 | 1512 | 15 / 3 | 6 | 1 | set_switch(23); stop |
| 2 | 121 | 12 / 1 | 6 | 30 | trigger_event(1211); stop |
| 2 | 1211 | 12 / 2 | 6 | 15 | trigger_event(1212); stop |
| 2 | 1212 | 12 / 3 | 8 | 30 | trigger_event(1213); stop |
| 2 | 1213 | 12 / 4 | 8 | 1 | trigger_event(1214); stop |
| 2 | 1214 | 12 / 5 | 8 | 10 | trigger_event(1215); stop |
| 2 | 1215 | 12 / 6 | 8 | 45 | trigger_event(1216); stop |
| 2 | 1216 | 12 / 7 | 8 | 15 | set_switch(10); stop |
| 2 | 152 | 15 / 1 | 5 | 1 | set_switch(7); stop |
| 2 | 132 | 13 / 5 | 1 | 1 | stop |
| 2 | 133 | 13 / 6 | 1 | 1 | stop |
| 2 | 134 | 13 / 7 | 1 | 1 | stop |
| 2 | 135 | 13 / 8 | 1 | 1 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
