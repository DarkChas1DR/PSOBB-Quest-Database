# 9-3:Reality & Truth — government-ep4/q703-bb-e

Episode4; header quest ID 703; language E. Static scan: **209 objects, 203 enemy/NPC records, 34 events, 173 script labels.** Script roundtrip: byte-identical.

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
0x00, 0x2D, 0x00, 0x00, 0x00
0x03, 0x26, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 27 | 20 | 0 |
| 3 | 182 | 183 | 34 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 3 | 801 | 80 / 1 | 3 | 30 | set_switch(81); stop |
| 3 | 802 | 80 / 2 | 3 | 30 | set_switch(82); stop |
| 3 | 901 | 90 / 1 | 5 | 30 | trigger_event(9011); stop |
| 3 | 9011 | 90 / 2 | 4 | 30 | set_switch(91); stop |
| 3 | 902 | 90 / 3 | 5 | 30 | trigger_event(9021); stop |
| 3 | 9021 | 90 / 4 | 6 | 60 | trigger_event(9022); stop |
| 3 | 9022 | 90 / 5 | 5 | 30 | trigger_event(9023); stop |
| 3 | 9023 | 90 / 6 | 6 | 60 | trigger_event(9024); stop |
| 3 | 9024 | 90 / 7 | 5 | 30 | trigger_event(9025); stop |
| 3 | 9025 | 90 / 8 | 6 | 30 | set_switch(92); stop |
| 3 | 301 | 30 / 1 | 5 | 30 | trigger_event(3011); stop |
| 3 | 3011 | 30 / 2 | 4 | 30 | set_switch(31); stop |
| 3 | 302 | 30 / 3 | 5 | 30 | trigger_event(3021); stop |
| 3 | 3021 | 30 / 4 | 5 | 60 | trigger_event(3022); stop |
| 3 | 3022 | 30 / 5 | 5 | 30 | trigger_event(3023); stop |
| 3 | 3023 | 30 / 6 | 6 | 60 | trigger_event(3024); stop |
| 3 | 3024 | 30 / 7 | 5 | 30 | trigger_event(3025); stop |
| 3 | 3025 | 30 / 8 | 6 | 30 | set_switch(32); stop |
| 3 | 201 | 20 / 1 | 4 | 30 | trigger_event(2011); stop |
| 3 | 2011 | 20 / 2 | 5 | 90 | trigger_event(2012); stop |
| 3 | 2012 | 20 / 3 | 5 | 60 | trigger_event(2013); stop |
| 3 | 2013 | 20 / 4 | 5 | 60 | trigger_event(2014); stop |
| 3 | 2014 | 20 / 5 | 4 | 30 | trigger_event(2015); stop |
| 3 | 2015 | 20 / 6 | 5 | 60 | trigger_event(2016); stop |
| 3 | 2016 | 20 / 7 | 7 | 90 | set_switch(201); set_switch(202); set_switch(90); set_switch(30); stop |
| 3 | 601 | 60 / 1 | 6 | 30 | trigger_event(6011); stop |
| 3 | 6011 | 60 / 2 | 6 | 30 | trigger_event(6012); stop |
| 3 | 6012 | 60 / 3 | 6 | 90 | trigger_event(6013); stop |
| 3 | 6013 | 60 / 4 | 5 | 30 | trigger_event(6014); stop |
| 3 | 6014 | 60 / 5 | 6 | 60 | trigger_event(6015); stop |
| 3 | 6015 | 60 / 6 | 6 | 30 | trigger_event(6016); stop |
| 3 | 6016 | 60 / 7 | 5 | 90 | trigger_event(6017); stop |
| 3 | 6017 | 60 / 8 | 6 | 30 | trigger_event(6018); stop |
| 3 | 6018 | 60 / 9 | 5 | 90 | set_switch(60); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
