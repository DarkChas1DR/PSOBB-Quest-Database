# 7-1:From the Past — government-ep2/q461-bb-e

Episode2; header quest ID 461; language E. Static scan: **338 objects, 141 enemy/NPC records, 56 events, 98 script labels.** Script roundtrip: byte-identical.

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
0x05, 0x17, 0x00, 0x00, 0x00
0x06, 0x18, 0x00, 0x00, 0x00
0x07, 0x19, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 53 | 19 | 0 |
| 5 | 84 | 0 | 0 |
| 6 | 107 | 57 | 22 |
| 7 | 94 | 65 | 34 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 6 | 11 | 1 / 1 | 2 | 120 | set_switch(12); stop |
| 6 | 31 | 3 / 1 | 3 | 1 | trigger_event(311); stop |
| 6 | 311 | 3 / 2 | 3 | 60 | trigger_event(312); stop |
| 6 | 312 | 3 / 3 | 4 | 1 | set_switch(13); set_switch(16); stop |
| 6 | 32 | 3 / 4 | 3 | 100 | trigger_event(321); stop |
| 6 | 321 | 3 / 5 | 3 | 1 | stop |
| 6 | 41 | 4 / 1 | 3 | 60 | trigger_event(411); stop |
| 6 | 411 | 4 / 2 | 4 | 30 | trigger_event(412); stop |
| 6 | 412 | 4 / 3 | 4 | 60 | set_switch(7); set_switch(11); set_switch(14); set_switch(15); set_switch(10); set_switch(9); set_switch(6); stop |
| 6 | 42 | 4 / 4 | 2 | 30 | trigger_event(421); stop |
| 6 | 421 | 4 / 5 | 2 | 1 | stop |
| 6 | 43 | 4 / 6 | 2 | 100 | trigger_event(431); stop |
| 6 | 431 | 4 / 7 | 2 | 100 | stop |
| 6 | 61 | 6 / 1 | 1 | 60 | stop |
| 6 | 121 | 12 / 1 | 2 | 1 | stop |
| 6 | 151 | 15 / 1 | 2 | 1 | trigger_event(1511); stop |
| 6 | 1511 | 15 / 2 | 3 | 1 | trigger_event(1512); stop |
| 6 | 1512 | 15 / 3 | 4 | 200 | set_switch(3); set_switch(4); set_switch(5); set_switch(8); stop |
| 6 | 152 | 15 / 4 | 1 | 150 | stop |
| 6 | 153 | 15 / 5 | 2 | 200 | trigger_event(1531); stop |
| 6 | 1531 | 15 / 6 | 2 | 100 | trigger_event(1532); stop |
| 6 | 1532 | 15 / 7 | 2 | 100 | stop |
| 7 | 11 | 1 / 1 | 2 | 1 | set_switch(2); stop |
| 7 | 21 | 2 / 1 | 3 | 1 | trigger_event(211); stop |
| 7 | 211 | 2 / 2 | 3 | 30 | trigger_event(212); stop |
| 7 | 212 | 2 / 3 | 4 | 30 | trigger_event(213); stop |
| 7 | 213 | 2 / 6 | 3 | 60 | set_switch(3); set_switch(4); set_switch(5); stop |
| 7 | 22 | 2 / 4 | 2 | 60 | trigger_event(221); stop |
| 7 | 221 | 2 / 5 | 4 | 150 | stop |
| 7 | 33 | 3 / 1 | 4 | 100 | trigger_event(331); stop |
| 7 | 331 | 3 / 2 | 4 | 200 | stop |
| 7 | 32 | 3 / 3 | 4 | 30 | stop |
| 7 | 41 | 4 / 1 | 2 | 10 | stop |
| 7 | 42 | 4 / 2 | 1 | 1 | stop |
| 7 | 51 | 5 / 13 | 4 | 1 | construct_objects(room=5,group_or_wave=1); trigger_event(5101); trigger_event(5102); trigger_event(5103); trigger_event(5104); trigger_event(5105); stop |
| 7 | 5101 | 5 / 14 | 1 | 100 | trigger_event(51011); stop |
| 7 | 51011 | 5 / 19 | 3 | 120 | trigger_event(51012); stop |
| 7 | 51012 | 5 / 20 | 2 | 200 | set_switch(6); set_switch(7); set_switch(201); stop |
| 7 | 5102 | 5 / 1 | 1 | 30 | trigger_event(51021); stop |
| 7 | 51021 | 5 / 2 | 1 | 100 | trigger_event(51022); stop |
| 7 | 51022 | 5 / 3 | 1 | 60 | trigger_event(51023); stop |
| 7 | 51023 | 5 / 15 | 1 | 30 | stop |
| 7 | 5103 | 5 / 4 | 1 | 1 | trigger_event(51031); stop |
| 7 | 51031 | 5 / 5 | 1 | 30 | trigger_event(51032); stop |
| 7 | 51032 | 5 / 6 | 1 | 100 | trigger_event(51033); stop |
| 7 | 51033 | 5 / 16 | 1 | 60 | stop |
| 7 | 5104 | 5 / 7 | 1 | 100 | trigger_event(51041); stop |
| 7 | 51041 | 5 / 8 | 1 | 60 | trigger_event(51042); stop |
| 7 | 51042 | 5 / 9 | 1 | 30 | trigger_event(51043); stop |
| 7 | 51043 | 5 / 17 | 1 | 60 | stop |
| 7 | 5105 | 5 / 10 | 1 | 30 | trigger_event(51051); stop |
| 7 | 51051 | 5 / 11 | 1 | 1 | trigger_event(51052); stop |
| 7 | 51052 | 5 / 12 | 1 | 10 | trigger_event(51053); stop |
| 7 | 51053 | 5 / 18 | 1 | 60 | stop |
| 7 | 71 | 7 / 1 | 2 | 100 | set_switch(1); stop |
| 7 | 81 | 8 / 1 | 1 | 100 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
