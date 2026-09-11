# Gran Squall — solo-story-ep1/q009-bb-e

Episode1; header quest ID 9; language E. Static scan: **249 objects, 111 enemy/NPC records, 36 events, 53 script labels.** Script roundtrip: byte-identical.

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
0x01, 0x01, 0x00, 0x00, 0x04
0x02, 0x02, 0x00, 0x00, 0x04
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 19 | 0 |
| 1 | 103 | 26 | 15 |
| 2 | 120 | 66 | 21 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 111 | 11 / 1 | 3 | 50 | trigger_event(1111); stop |
| 1 | 1111 | 11 / 2 | 2 | 50 | trigger_event(1112); stop |
| 1 | 1112 | 11 / 3 | 2 | 50 | set_switch(5); set_switch(6); set_switch(7); set_switch(8); set_switch(10); stop |
| 1 | 51 | 5 / 1 | 2 | 60 | trigger_event(511); stop |
| 1 | 511 | 5 / 2 | 2 | 60 | trigger_event(512); stop |
| 1 | 512 | 5 / 3 | 2 | 60 | set_switch(1); stop |
| 1 | 21 | 2 / 1 | 1 | 60 | trigger_event(211); stop |
| 1 | 211 | 2 / 2 | 1 | 60 | trigger_event(212); stop |
| 1 | 212 | 2 / 3 | 1 | 60 | trigger_event(213); stop |
| 1 | 213 | 2 / 4 | 2 | 60 | stop |
| 1 | 71 | 7 / 1 | 1 | 60 | trigger_event(711); stop |
| 1 | 711 | 7 / 2 | 2 | 60 | trigger_event(712); stop |
| 1 | 712 | 7 / 3 | 2 | 60 | set_switch(4); stop |
| 1 | 41 | 4 / 1 | 1 | 60 | trigger_event(411); stop |
| 1 | 411 | 4 / 2 | 2 | 60 | set_switch(3); stop |
| 2 | 11 | 1 / 1 | 6 | 70 | set_switch(1); stop |
| 2 | 21 | 2 / 1 | 2 | 1 | trigger_event(211); stop |
| 2 | 211 | 2 / 2 | 3 | 30 | stop |
| 2 | 22 | 2 / 3 | 2 | 90 | trigger_event(221); stop |
| 2 | 221 | 2 / 4 | 2 | 30 | set_switch(3); set_switch(4); set_switch(5); set_switch(6); stop |
| 2 | 31 | 3 / 1 | 5 | 60 | stop |
| 2 | 41 | 4 / 1 | 3 | 1 | stop |
| 2 | 42 | 4 / 2 | 1 | 10 | stop |
| 2 | 61 | 6 / 1 | 1 | 1 | trigger_event(611); stop |
| 2 | 611 | 6 / 2 | 3 | 1 | set_switch(2); stop |
| 2 | 101 | 10 / 1 | 5 | 1 | stop |
| 2 | 111 | 11 / 1 | 2 | 1 | trigger_event(1111); stop |
| 2 | 1111 | 11 / 2 | 4 | 1 | trigger_event(1112); stop |
| 2 | 1112 | 11 / 3 | 1 | 60 | set_switch(7); set_switch(8); set_switch(11); stop |
| 2 | 121 | 12 / 1 | 3 | 10 | trigger_event(1211); stop |
| 2 | 1211 | 12 / 2 | 4 | 30 | trigger_event(1212); stop |
| 2 | 1212 | 12 / 3 | 4 | 1 | trigger_event(1213); stop |
| 2 | 1213 | 12 / 4 | 6 | 30 | trigger_event(1214); stop |
| 2 | 1214 | 12 / 5 | 2 | 30 | set_switch(10); stop |
| 2 | 131 | 13 / 1 | 4 | 90 | set_switch(9); stop |
| 2 | 132 | 13 / 2 | 3 | 30 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
