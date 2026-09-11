# Malicious Uprising #4 — extermination-ep2/q99-bb-j

Episode2; header quest ID 99; language J. Static scan: **151 objects, 219 enemy/NPC records, 48 events, 153 script labels.** Script roundtrip: alignment-only.

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
| 10 | 107 | 200 | 48 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 10 | 1 | 80 / 1 | 4 | 60 | trigger_event(100); stop |
| 10 | 100 | 80 / 2 | 6 | 60 | trigger_event(1001); stop |
| 10 | 1001 | 80 / 3 | 6 | 60 | trigger_event(1002); stop |
| 10 | 1002 | 80 / 4 | 4 | 60 | set_switch(171); set_switch(172); set_switch(1); trigger_event(2); stop |
| 10 | 2 | 90 / 1 | 6 | 60 | trigger_event(21); stop |
| 10 | 21 | 90 / 2 | 6 | 60 | trigger_event(22); stop |
| 10 | 22 | 90 / 3 | 3 | 60 | trigger_event(23); stop |
| 10 | 23 | 90 / 4 | 6 | 60 | trigger_event(24); stop |
| 10 | 24 | 90 / 5 | 3 | 60 | set_switch(174); set_switch(175); set_switch(2); stop |
| 10 | 3 | 40 / 1 | 5 | 60 | trigger_event(31); stop |
| 10 | 31 | 40 / 2 | 5 | 60 | set_switch(177); set_switch(178); set_switch(3); stop |
| 10 | 4 | 20 / 1 | 5 | 30 | trigger_event(41); stop |
| 10 | 41 | 20 / 2 | 5 | 60 | trigger_event(42); stop |
| 10 | 42 | 20 / 3 | 2 | 60 | set_switch(180); set_switch(181); set_switch(4); stop |
| 10 | 5 | 81 / 1 | 7 | 60 | trigger_event(51); stop |
| 10 | 51 | 81 / 2 | 3 | 60 | trigger_event(52); stop |
| 10 | 52 | 81 / 3 | 7 | 60 | trigger_event(53); stop |
| 10 | 53 | 81 / 4 | 2 | 60 | set_switch(183); set_switch(184); set_switch(5); stop |
| 10 | 6 | 64 / 1 | 4 | 30 | trigger_event(62); stop |
| 10 | 62 | 64 / 2 | 4 | 60 | trigger_event(63); stop |
| 10 | 63 | 64 / 3 | 2 | 60 | set_switch(186); set_switch(187); set_switch(6); stop |
| 10 | 7 | 62 / 1 | 5 | 60 | trigger_event(71); stop |
| 10 | 71 | 62 / 2 | 5 | 60 | trigger_event(72); stop |
| 10 | 72 | 62 / 3 | 3 | 60 | set_switch(189); set_switch(190); set_switch(7); stop |
| 10 | 8 | 30 / 1 | 2 | 30 | trigger_event(81); stop |
| 10 | 81 | 30 / 2 | 2 | 60 | trigger_event(82); stop |
| 10 | 82 | 30 / 3 | 5 | 60 | trigger_event(83); stop |
| 10 | 83 | 30 / 4 | 1 | 60 | set_switch(192); set_switch(193); set_switch(8); stop |
| 10 | 9 | 21 / 1 | 2 | 60 | trigger_event(91); stop |
| 10 | 91 | 21 / 2 | 5 | 60 | trigger_event(92); stop |
| 10 | 92 | 21 / 3 | 3 | 60 | set_switch(195); set_switch(196); set_switch(9); trigger_event(10); stop |
| 10 | 10 | 61 / 1 | 5 | 180 | trigger_event(101); stop |
| 10 | 101 | 61 / 2 | 5 | 60 | set_switch(198); set_switch(199); set_switch(10); stop |
| 10 | 11 | 71 / 1 | 5 | 60 | trigger_event(110); stop |
| 10 | 110 | 71 / 2 | 5 | 60 | trigger_event(111); stop |
| 10 | 111 | 71 / 3 | 4 | 60 | trigger_event(112); stop |
| 10 | 112 | 71 / 4 | 4 | 60 | set_switch(201); set_switch(202); set_switch(11); stop |
| 10 | 12 | 63 / 1 | 5 | 30 | trigger_event(121); stop |
| 10 | 121 | 63 / 2 | 5 | 60 | set_switch(204); set_switch(205); set_switch(12); stop |
| 10 | 13 | 70 / 1 | 3 | 60 | trigger_event(131); stop |
| 10 | 131 | 70 / 2 | 6 | 60 | trigger_event(132); stop |
| 10 | 132 | 70 / 3 | 3 | 60 | trigger_event(133); stop |
| 10 | 133 | 70 / 4 | 6 | 60 | trigger_event(134); stop |
| 10 | 134 | 70 / 5 | 2 | 60 | set_switch(207); set_switch(208); set_switch(13); stop |
| 10 | 14 | 60 / 1 | 4 | 60 | trigger_event(141); stop |
| 10 | 141 | 60 / 2 | 4 | 60 | trigger_event(142); stop |
| 10 | 142 | 60 / 3 | 4 | 60 | trigger_event(143); stop |
| 10 | 143 | 60 / 4 | 2 | 120 | set_switch(14); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
