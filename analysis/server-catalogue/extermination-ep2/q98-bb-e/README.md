# Malicious Uprising #3 — extermination-ep2/q98-bb-e

Episode2; header quest ID 98; language E. Static scan: **143 objects, 179 enemy/NPC records, 37 events, 141 script labels.** Script roundtrip: byte-identical.

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
| 0 | 44 | 19 | 0 |
| 8 | 99 | 160 | 37 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 8 | 1 | 8 / 1 | 5 | 30 | trigger_event(100); stop |
| 8 | 100 | 8 / 2 | 5 | 60 | trigger_event(101); stop |
| 8 | 101 | 8 / 3 | 5 | 60 | trigger_event(102); stop |
| 8 | 102 | 8 / 4 | 3 | 60 | set_switch(172); set_switch(173); set_switch(1); stop |
| 8 | 2 | 6 / 15 | 5 | 30 | trigger_event(21); stop |
| 8 | 21 | 6 / 1 | 5 | 60 | trigger_event(22); stop |
| 8 | 22 | 6 / 5 | 2 | 60 | set_switch(175); set_switch(176); set_switch(2); stop |
| 8 | 3 | 6 / 2 | 6 | 30 | trigger_event(31); set_switch(3); stop |
| 8 | 31 | 6 / 3 | 7 | 60 | trigger_event(32); stop |
| 8 | 32 | 6 / 4 | 1 | 60 | set_switch(177); set_switch(178); construct_objects(room=6,group_or_wave=1); set_switch(4); stop |
| 8 | 4 | 7 / 1 | 4 | 60 | trigger_event(41); stop |
| 8 | 41 | 7 / 2 | 5 | 60 | set_switch(180); set_switch(181); set_switch(5); stop |
| 8 | 5 | 5 / 1 | 6 | 60 | trigger_event(51); stop |
| 8 | 51 | 5 / 2 | 3 | 30 | trigger_event(52); stop |
| 8 | 52 | 5 / 3 | 7 | 60 | trigger_event(53); stop |
| 8 | 53 | 5 / 4 | 3 | 30 | trigger_event(54); stop |
| 8 | 54 | 5 / 5 | 1 | 60 | set_switch(183); set_switch(184); set_switch(6); stop |
| 8 | 6 | 4 / 1 | 4 | 60 | trigger_event(61); stop |
| 8 | 61 | 4 / 2 | 6 | 60 | set_switch(186); set_switch(187); set_switch(7); stop |
| 8 | 7 | 10 / 1 | 5 | 60 | trigger_event(71); stop |
| 8 | 71 | 10 / 2 | 4 | 60 | trigger_event(72); stop |
| 8 | 72 | 10 / 3 | 1 | 60 | set_switch(189); set_switch(190); set_switch(8); stop |
| 8 | 8 | 2 / 8 | 5 | 60 | trigger_event(81); stop |
| 8 | 81 | 2 / 9 | 6 | 60 | trigger_event(82); stop |
| 8 | 82 | 2 / 10 | 1 | 60 | set_switch(192); set_switch(193); set_switch(9); stop |
| 8 | 9 | 3 / 1 | 6 | 60 | trigger_event(91); stop |
| 8 | 91 | 3 / 2 | 6 | 60 | trigger_event(92); stop |
| 8 | 92 | 3 / 3 | 5 | 60 | trigger_event(93); stop |
| 8 | 93 | 3 / 4 | 1 | 60 | set_switch(195); set_switch(196); set_switch(10); stop |
| 8 | 10 | 3 / 5 | 5 | 60 | trigger_event(1000); stop |
| 8 | 1000 | 3 / 6 | 6 | 60 | trigger_event(1001); stop |
| 8 | 1001 | 3 / 7 | 1 | 60 | construct_objects(room=3,group_or_wave=1); stop |
| 8 | 11 | 2 / 1 | 6 | 0 | trigger_event(110); stop |
| 8 | 110 | 2 / 2 | 6 | 60 | trigger_event(111); stop |
| 8 | 111 | 2 / 3 | 4 | 60 | trigger_event(112); stop |
| 8 | 112 | 2 / 4 | 3 | 120 | trigger_event(113); stop |
| 8 | 113 | 2 / 5 | 6 | 90 | set_switch(11); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
