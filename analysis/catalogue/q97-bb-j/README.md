# Malicious Uprising #2 — q97-bb-j

Episode2; header quest ID 97; language J. Static scan: **137 objects, 212 enemy/NPC records, 35 events, 146 script labels.** Script roundtrip: alignment-only.

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
| 3 | 93 | 193 | 35 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 3 | 1 | 52 / 1 | 7 | 60 | trigger_event(101); stop |
| 3 | 101 | 52 / 2 | 7 | 60 | trigger_event(102); stop |
| 3 | 102 | 52 / 3 | 4 | 60 | set_switch(171); set_switch(172); set_switch(1); stop |
| 3 | 2 | 20 / 1 | 5 | 60 | trigger_event(21); stop |
| 3 | 21 | 20 / 2 | 6 | 60 | set_switch(174); set_switch(175); set_switch(2); stop |
| 3 | 3 | 42 / 1 | 4 | 60 | trigger_event(31); stop |
| 3 | 31 | 42 / 2 | 5 | 60 | trigger_event(32); stop |
| 3 | 32 | 42 / 3 | 4 | 60 | trigger_event(33); stop |
| 3 | 33 | 42 / 4 | 7 | 60 | set_switch(177); set_switch(178); set_switch(3); stop |
| 3 | 4 | 32 / 1 | 5 | 60 | trigger_event(41); stop |
| 3 | 41 | 32 / 2 | 5 | 60 | set_switch(180); set_switch(181); set_switch(4); stop |
| 3 | 5 | 10 / 1 | 6 | 60 | trigger_event(51); stop |
| 3 | 51 | 10 / 2 | 5 | 60 | trigger_event(52); stop |
| 3 | 52 | 10 / 3 | 2 | 60 | set_switch(183); set_switch(184); set_switch(5); stop |
| 3 | 6 | 51 / 1 | 7 | 60 | trigger_event(61); stop |
| 3 | 61 | 51 / 2 | 7 | 60 | trigger_event(62); stop |
| 3 | 62 | 51 / 3 | 3 | 60 | set_switch(186); set_switch(187); set_switch(6); stop |
| 3 | 7 | 41 / 1 | 5 | 60 | trigger_event(71); stop |
| 3 | 71 | 41 / 2 | 5 | 60 | trigger_event(72); stop |
| 3 | 72 | 41 / 3 | 4 | 60 | trigger_event(73); stop |
| 3 | 73 | 41 / 4 | 7 | 60 | set_switch(189); set_switch(190); set_switch(7); stop |
| 3 | 8 | 50 / 1 | 7 | 60 | trigger_event(81); stop |
| 3 | 81 | 50 / 2 | 6 | 60 | trigger_event(82); stop |
| 3 | 82 | 50 / 3 | 7 | 60 | set_switch(192); set_switch(193); set_switch(8); stop |
| 3 | 9 | 33 / 1 | 2 | 60 | trigger_event(91); stop |
| 3 | 91 | 33 / 2 | 5 | 60 | trigger_event(92); stop |
| 3 | 92 | 33 / 3 | 5 | 60 | set_switch(195); set_switch(196); set_switch(9); stop |
| 3 | 10 | 21 / 1 | 5 | 60 | trigger_event(100); stop |
| 3 | 100 | 21 / 2 | 5 | 60 | set_switch(198); set_switch(199); set_switch(10); stop |
| 3 | 11 | 11 / 1 | 5 | 60 | trigger_event(110); stop |
| 3 | 110 | 11 / 2 | 9 | 60 | set_switch(201); set_switch(202); set_switch(11); stop |
| 3 | 12 | 40 / 1 | 7 | 60 | trigger_event(121); stop |
| 3 | 121 | 40 / 2 | 6 | 60 | trigger_event(122); stop |
| 3 | 122 | 40 / 3 | 5 | 60 | trigger_event(123); stop |
| 3 | 123 | 40 / 4 | 9 | 60 | set_switch(12); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
