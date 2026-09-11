# Malicious Uprising #5 — extermination-ep2/q100-bb-j

Episode2; header quest ID 100; language J. Static scan: **202 objects, 139 enemy/NPC records, 35 events, 141 script labels.** Script roundtrip: alignment-only.

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
| 17 | 158 | 120 | 35 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 17 | 1 | 1 / 1 | 2 | 60 | trigger_event(11); stop |
| 17 | 11 | 1 / 2 | 2 | 90 | trigger_event(12); stop |
| 17 | 12 | 1 / 3 | 3 | 60 | trigger_event(13); stop |
| 17 | 13 | 1 / 4 | 3 | 60 | set_switch(171); set_switch(172); set_switch(1); stop |
| 17 | 2 | 2 / 1 | 3 | 60 | trigger_event(21); stop |
| 17 | 21 | 2 / 2 | 4 | 60 | trigger_event(22); stop |
| 17 | 22 | 2 / 3 | 3 | 60 | set_switch(174); set_switch(175); set_switch(2); stop |
| 17 | 3 | 20 / 1 | 4 | 60 | trigger_event(31); stop |
| 17 | 31 | 20 / 2 | 1 | 60 | trigger_event(32); stop |
| 17 | 32 | 20 / 3 | 2 | 60 | trigger_event(33); stop |
| 17 | 33 | 20 / 4 | 3 | 60 | set_switch(177); set_switch(178); set_switch(3); stop |
| 17 | 4 | 10 / 1 | 2 | 60 | trigger_event(41); stop |
| 17 | 41 | 10 / 2 | 3 | 60 | construct_objects(room=10,group_or_wave=1); trigger_event(42); stop |
| 17 | 42 | 10 / 3 | 4 | 90 | set_switch(180); set_switch(181); set_switch(4); stop |
| 17 | 5 | 3 / 1 | 3 | 30 | trigger_event(51); stop |
| 17 | 51 | 3 / 2 | 4 | 60 | trigger_event(52); stop |
| 17 | 52 | 3 / 3 | 4 | 60 | set_switch(183); set_switch(184); set_switch(5); stop |
| 17 | 6 | 4 / 1 | 2 | 60 | trigger_event(61); stop |
| 17 | 61 | 4 / 2 | 4 | 120 | set_switch(186); set_switch(187); set_switch(6); stop |
| 17 | 7 | 21 / 1 | 2 | 60 | trigger_event(71); stop |
| 17 | 71 | 21 / 2 | 1 | 0 | set_switch(11); stop |
| 17 | 701 | 21 / 3 | 3 | 60 | trigger_event(7011); stop |
| 17 | 7011 | 21 / 4 | 1 | 0 | set_switch(12); stop |
| 17 | 702 | 21 / 5 | 2 | 60 | trigger_event(7022); stop |
| 17 | 7022 | 21 / 6 | 1 | 0 | set_switch(189); set_switch(190); set_switch(7); stop |
| 17 | 8 | 5 / 1 | 6 | 0 | trigger_event(81); stop |
| 17 | 81 | 5 / 2 | 4 | 90 | trigger_event(82); stop |
| 17 | 82 | 5 / 3 | 1 | 90 | set_switch(192); set_switch(193); set_switch(8); stop |
| 17 | 9 | 22 / 1 | 4 | 60 | trigger_event(91); stop |
| 17 | 91 | 22 / 2 | 4 | 60 | trigger_event(92); stop |
| 17 | 92 | 22 / 3 | 4 | 90 | set_switch(195); set_switch(196); set_switch(9); stop |
| 17 | 10 | 30 / 1 | 1 | 60 | trigger_event(1001); stop |
| 17 | 1001 | 30 / 2 | 3 | 90 | trigger_event(1002); stop |
| 17 | 1002 | 30 / 3 | 4 | 120 | trigger_event(1003); stop |
| 17 | 1003 | 30 / 4 | 5 | 180 | construct_objects(room=30,group_or_wave=1); set_switch(10); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
