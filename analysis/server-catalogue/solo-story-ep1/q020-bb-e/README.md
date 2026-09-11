# Dr. Osto\'s Research — solo-story-ep1/q020-bb-e

Episode1; header quest ID 20; language E. Static scan: **190 objects, 83 enemy/NPC records, 20 events, 120 script labels.** Script roundtrip: byte-identical.

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
0x07, 0x07, 0x00, 0x01, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 20 | 0 |
| 7 | 164 | 63 | 20 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 7 | 201 | 20 / 1 | 4 | 1 | set_switch(2); set_switch(4); set_switch(5); set_switch(6); set_switch(7); set_switch(8); set_switch(9); stop |
| 7 | 301 | 30 / 1 | 5 | 1 | trigger_event(3011); stop |
| 7 | 3011 | 30 / 2 | 4 | 60 | trigger_event(3012); stop |
| 7 | 3012 | 30 / 3 | 2 | 60 | set_switch(17); set_switch(18); stop |
| 7 | 501 | 50 / 1 | 8 | 1 | set_switch(10); set_switch(12); stop |
| 7 | 521 | 52 / 1 | 3 | 1 | trigger_event(5211); stop |
| 7 | 5211 | 52 / 2 | 3 | 30 | trigger_event(5212); stop |
| 7 | 5212 | 52 / 3 | 1 | 1 | set_switch(19); set_switch(21); set_switch(22); stop |
| 7 | 601 | 60 / 1 | 2 | 1 | trigger_event(6011); stop |
| 7 | 6011 | 60 / 2 | 2 | 30 | trigger_event(6012); stop |
| 7 | 6012 | 60 / 3 | 1 | 100 | set_switch(14); set_switch(15); set_switch(16); stop |
| 7 | 602 | 60 / 4 | 2 | 90 | trigger_event(6021); stop |
| 7 | 6021 | 60 / 5 | 2 | 45 | stop |
| 7 | 611 | 61 / 1 | 1 | 1 | trigger_event(6111); stop |
| 7 | 6111 | 61 / 2 | 6 | 60 | trigger_event(6112); stop |
| 7 | 6112 | 61 / 3 | 2 | 30 | set_switch(31); stop |
| 7 | 801 | 80 / 1 | 5 | 1 | set_switch(23); set_switch(24); set_switch(25); set_switch(27); set_switch(28); set_switch(30); stop |
| 7 | 802 | 80 / 2 | 5 | 1 | stop |
| 7 | 901 | 90 / 1 | 3 | 1 | trigger_event(9011); stop |
| 7 | 9011 | 90 / 2 | 2 | 60 | set_switch(1); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
