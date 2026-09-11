# Malicious Uprising #1 — extermination-ep2/q96-bb-e

Episode2; header quest ID 96; language E. Static scan: **143 objects, 200 enemy/NPC records, 42 events, 155 script labels.** Script roundtrip: alignment-only.

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
| 2 | 99 | 181 | 42 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 2 | 1 | 70 / 1 | 5 | 60 | trigger_event(11); stop |
| 2 | 11 | 70 / 2 | 5 | 60 | set_switch(1); stop |
| 2 | 2 | 70 / 3 | 4 | 60 | trigger_event(21); stop |
| 2 | 21 | 70 / 4 | 5 | 60 | set_switch(172); set_switch(173); set_switch(2); stop |
| 2 | 3 | 20 / 1 | 5 | 60 | trigger_event(31); stop |
| 2 | 31 | 20 / 2 | 3 | 60 | set_switch(174); set_switch(175); set_switch(3); stop |
| 2 | 4 | 10 / 1 | 4 | 60 | trigger_event(41); stop |
| 2 | 41 | 10 / 2 | 4 | 60 | trigger_event(42); stop |
| 2 | 42 | 10 / 3 | 2 | 60 | set_switch(177); set_switch(178); set_switch(4); stop |
| 2 | 5 | 60 / 1 | 5 | 60 | trigger_event(51); stop |
| 2 | 51 | 60 / 2 | 5 | 60 | trigger_event(52); stop |
| 2 | 52 | 60 / 3 | 6 | 60 | trigger_event(53); stop |
| 2 | 53 | 60 / 4 | 2 | 60 | set_switch(180); set_switch(181); set_switch(5); stop |
| 2 | 6 | 30 / 1 | 5 | 60 | trigger_event(61); stop |
| 2 | 61 | 30 / 2 | 5 | 60 | set_switch(183); set_switch(184); set_switch(6); stop |
| 2 | 7 | 95 / 1 | 4 | 60 | trigger_event(71); stop |
| 2 | 71 | 95 / 2 | 4 | 60 | set_switch(186); set_switch(187); set_switch(7); stop |
| 2 | 8 | 94 / 1 | 3 | 0 | trigger_event(81); stop |
| 2 | 81 | 94 / 2 | 5 | 0 | set_switch(189); set_switch(190); set_switch(8); stop |
| 2 | 9 | 97 / 1 | 4 | 60 | trigger_event(91); stop |
| 2 | 91 | 97 / 2 | 4 | 60 | set_switch(192); set_switch(193); set_switch(9); stop |
| 2 | 10 | 80 / 1 | 3 | 60 | trigger_event(101); construct_objects(room=80,group_or_wave=1); stop |
| 2 | 101 | 80 / 2 | 6 | 90 | set_switch(195); set_switch(196); construct_objects(room=80,group_or_wave=2); stop |
| 2 | 30 | 40 / 1 | 4 | 30 | trigger_event(300); stop |
| 2 | 300 | 40 / 2 | 4 | 60 | trigger_event(301); stop |
| 2 | 301 | 40 / 3 | 2 | 60 | trigger_event(302); stop |
| 2 | 302 | 40 / 4 | 6 | 60 | set_switch(198); set_switch(199); set_switch(11); stop |
| 2 | 12 | 11 / 1 | 4 | 60 | trigger_event(121); stop |
| 2 | 121 | 11 / 2 | 4 | 60 | trigger_event(122); stop |
| 2 | 122 | 11 / 3 | 4 | 60 | set_switch(201); set_switch(202); set_switch(12); stop |
| 2 | 13 | 96 / 1 | 4 | 60 | trigger_event(131); stop |
| 2 | 131 | 96 / 2 | 4 | 60 | set_switch(204); set_switch(205); set_switch(13); stop |
| 2 | 14 | 92 / 1 | 5 | 60 | trigger_event(141); trigger_event(142); stop |
| 2 | 141 | 92 / 2 | 5 | 60 | set_switch(207); set_switch(208); set_switch(14); stop |
| 2 | 15 | 98 / 1 | 2 | 60 | trigger_event(151); stop |
| 2 | 151 | 98 / 2 | 5 | 60 | trigger_event(152); stop |
| 2 | 152 | 98 / 3 | 5 | 60 | set_switch(210); set_switch(211); set_switch(15); stop |
| 2 | 16 | 50 / 1 | 3 | 60 | trigger_event(161); stop |
| 2 | 161 | 50 / 2 | 7 | 60 | trigger_event(162); stop |
| 2 | 162 | 50 / 3 | 6 | 60 | trigger_event(163); stop |
| 2 | 163 | 50 / 4 | 9 | 60 | trigger_event(164); stop |
| 2 | 164 | 50 / 5 | 0 | 120 | set_switch(16); stop |

## Review notes

- Floor 2: event 14 targets absent event 142
