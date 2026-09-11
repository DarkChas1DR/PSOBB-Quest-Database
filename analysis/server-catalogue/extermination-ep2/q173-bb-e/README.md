# Penumbral Surge #3 — extermination-ep2/q173-bb-e

Episode2; header quest ID 173; language E. Static scan: **800 objects, 442 enemy/NPC records, 145 events, 81 script labels.** Script roundtrip: alignment-only.

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
| 0 | 53 | 11 | 0 |
| 6 | 134 | 117 | 42 |
| 8 | 315 | 150 | 49 |
| 9 | 298 | 164 | 54 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 6 | 2 | 15 / 2 | 5 | 30 | trigger_event(3); stop |
| 6 | 3 | 15 / 3 | 4 | 35 | trigger_event(4); stop |
| 6 | 4 | 15 / 4 | 4 | 30 | set_switch(2); trigger_event(5); stop |
| 6 | 5 | 9 / 4 | 1 | 5 | set_switch(10); stop |
| 6 | 6 | 9 / 1 | 4 | 10 | set_switch(3); trigger_event(7); stop |
| 6 | 7 | 3 / 1 | 6 | 50 | trigger_event(8); stop |
| 6 | 8 | 3 / 3 | 6 | 35 | set_switch(4); construct_objects(room=2,group_or_wave=10); stop |
| 6 | 9 | 2 / 1 | 3 | 15 | set_switch(5); stop |
| 6 | 10 | 1 / 1 | 4 | 30 | trigger_event(11); stop |
| 6 | 11 | 1 / 2 | 4 | 35 | trigger_event(12); stop |
| 6 | 12 | 1 / 3 | 4 | 35 | trigger_event(13); stop |
| 6 | 13 | 1 / 4 | 4 | 20 | trigger_event(14); stop |
| 6 | 14 | 1 / 5 | 1 | 40 | set_switch(6); trigger_event(15); stop |
| 6 | 15 | 6 / 1 | 1 | 1 | set_switch(7); stop |
| 6 | 16 | 4 / 1 | 5 | 25 | trigger_event(17); stop |
| 6 | 17 | 4 / 2 | 4 | 30 | trigger_event(18); stop |
| 6 | 18 | 4 / 3 | 4 | 50 | trigger_event(19); stop |
| 6 | 19 | 4 / 4 | 5 | 35 | trigger_event(20); stop |
| 6 | 20 | 4 / 5 | 3 | 40 | trigger_event(21); stop |
| 6 | 21 | 4 / 6 | 1 | 35 | set_switch(67); construct_objects(room=4,group_or_wave=1); stop |
| 6 | 22 | 4 / 7 | 1 | 40 | set_switch(8); trigger_event(23); stop |
| 6 | 23 | 4 / 8 | 3 | 30 | trigger_event(24); stop |
| 6 | 24 | 4 / 9 | 1 | 10 | set_switch(9); stop |
| 6 | 25 | 8 / 1 | 1 | 5 | set_switch(11); stop |
| 6 | 26 | 8 / 2 | 3 | 5 | trigger_event(27); stop |
| 6 | 27 | 8 / 3 | 3 | 30 | set_switch(12); stop |
| 6 | 28 | 8 / 4 | 2 | 5 | set_switch(13); trigger_event(29); stop |
| 6 | 29 | 8 / 5 | 1 | 30 | set_switch(1); construct_objects(room=8,group_or_wave=11); trigger_event(30); stop |
| 6 | 30 | 7 / 1 | 2 | 5 | set_switch(14); stop |
| 6 | 31 | 11 / 1 | 1 | 40 | trigger_event(33); stop |
| 6 | 32 | 11 / 2 | 2 | 40 | trigger_event(34); stop |
| 6 | 33 | 11 / 3 | 2 | 30 | trigger_event(35); stop |
| 6 | 34 | 11 / 4 | 2 | 30 | trigger_event(36); stop |
| 6 | 35 | 11 / 5 | 3 | 30 | trigger_event(37); stop |
| 6 | 36 | 11 / 6 | 2 | 30 | trigger_event(38); stop |
| 6 | 37 | 11 / 7 | 4 | 30 | trigger_event(39); stop |
| 6 | 38 | 11 / 8 | 1 | 30 | trigger_event(40); stop |
| 6 | 39 | 11 / 9 | 1 | 30 | set_switch(15); stop |
| 6 | 40 | 11 / 10 | 1 | 30 | set_switch(16); stop |
| 6 | 41 | 12 / 1 | 1 | 60 | trigger_event(42); stop |
| 6 | 42 | 12 / 2 | 1 | 30 | set_switch(17); stop |
| 6 | 43 | 15 / 5 | 6 | 30 | set_switch(18); stop |
| 8 | 2 | 2 / 1 | 3 | 30 | set_switch(2); stop |
| 8 | 3 | 2 / 2 | 2 | 40 | trigger_event(4); stop |
| 8 | 4 | 2 / 3 | 4 | 35 | trigger_event(5); stop |
| 8 | 5 | 2 / 4 | 6 | 30 | trigger_event(6); stop |
| 8 | 6 | 2 / 5 | 3 | 35 | set_switch(3); stop |
| 8 | 7 | 2 / 30 | 1 | 30 | set_switch(4); construct_objects(room=2,group_or_wave=14); stop |
| 8 | 8 | 2 / 6 | 3 | 40 | trigger_event(9); stop |
| 8 | 9 | 2 / 7 | 5 | 30 | trigger_event(10); stop |
| 8 | 10 | 2 / 8 | 3 | 30 | trigger_event(11); stop |
| 8 | 11 | 2 / 9 | 1 | 40 | set_switch(5); stop |
| 8 | 12 | 2 / 10 | 2 | 40 | trigger_event(13); stop |
| 8 | 13 | 2 / 11 | 3 | 45 | trigger_event(14); stop |
| 8 | 14 | 2 / 12 | 3 | 35 | trigger_event(15); stop |
| 8 | 15 | 2 / 13 | 5 | 30 | set_switch(6); construct_objects(room=2,group_or_wave=13); construct_objects(room=2,group_or_wave=40); stop |
| 8 | 16 | 3 / 1 | 2 | 20 | set_switch(7); construct_objects(room=3,group_or_wave=15); stop |
| 8 | 17 | 3 / 2 | 4 | 40 | set_switch(8); construct_objects(room=3,group_or_wave=16); stop |
| 8 | 18 | 3 / 3 | 4 | 40 | set_switch(9); construct_objects(room=3,group_or_wave=17); stop |
| 8 | 19 | 3 / 4 | 5 | 35 | set_switch(10); stop |
| 8 | 20 | 4 / 1 | 4 | 30 | trigger_event(21); stop |
| 8 | 21 | 4 / 2 | 3 | 40 | trigger_event(23); stop |
| 8 | 23 | 4 / 3 | 6 | 35 | set_switch(11); trigger_event(24); stop |
| 8 | 24 | 6 / 1 | 1 | 1 | set_switch(12); stop |
| 8 | 25 | 8 / 1 | 4 | 35 | trigger_event(26); stop |
| 8 | 26 | 8 / 2 | 3 | 30 | trigger_event(27); stop |
| 8 | 27 | 8 / 3 | 4 | 40 | trigger_event(28); stop |
| 8 | 28 | 8 / 4 | 5 | 35 | trigger_event(29); stop |
| 8 | 29 | 8 / 5 | 3 | 40 | trigger_event(30); stop |
| 8 | 30 | 8 / 6 | 4 | 30 | set_switch(13); construct_objects(room=9,group_or_wave=18); stop |
| 8 | 31 | 9 / 1 | 1 | 5 | trigger_event(32); stop |
| 8 | 32 | 9 / 2 | 1 | 45 | set_switch(14); stop |
| 8 | 33 | 5 / 1 | 3 | 35 | set_switch(160); trigger_event(34); stop |
| 8 | 34 | 5 / 2 | 3 | 30 | set_switch(161); trigger_event(35); stop |
| 8 | 35 | 5 / 3 | 3 | 30 | set_switch(162); trigger_event(36); stop |
| 8 | 36 | 5 / 4 | 3 | 30 | set_switch(163); trigger_event(37); stop |
| 8 | 37 | 5 / 5 | 3 | 30 | set_switch(164); trigger_event(38); stop |
| 8 | 38 | 5 / 6 | 3 | 30 | set_switch(165); trigger_event(39); stop |
| 8 | 39 | 5 / 7 | 2 | 30 | set_switch(166); trigger_event(40); stop |
| 8 | 40 | 5 / 8 | 2 | 30 | set_switch(167); trigger_event(41); stop |
| 8 | 41 | 5 / 9 | 2 | 30 | set_switch(168); trigger_event(42); stop |
| 8 | 42 | 5 / 10 | 1 | 30 | set_switch(15); stop |
| 8 | 43 | 5 / 11 | 5 | 10 | set_switch(19); stop |
| 8 | 44 | 5 / 12 | 3 | 45 | set_switch(16); construct_objects(room=4,group_or_wave=1); trigger_event(45); stop |
| 8 | 45 | 4 / 4 | 3 | 25 | trigger_event(47); stop |
| 8 | 46 | 4 / 5 | 2 | 30 | trigger_event(48); stop |
| 8 | 47 | 4 / 6 | 3 | 35 | trigger_event(49); stop |
| 8 | 48 | 4 / 7 | 3 | 35 | trigger_event(50); stop |
| 8 | 49 | 4 / 8 | 3 | 35 | trigger_event(51); stop |
| 8 | 50 | 4 / 9 | 3 | 35 | set_switch(17); stop |
| 8 | 51 | 4 / 10 | 2 | 30 | set_switch(18); stop |
| 9 | 1 | 3 / 1 | 3 | 10 | trigger_event(2); stop |
| 9 | 2 | 3 / 2 | 4 | 50 | trigger_event(3); stop |
| 9 | 3 | 3 / 3 | 2 | 50 | trigger_event(4); stop |
| 9 | 4 | 3 / 4 | 4 | 40 | set_switch(1); trigger_event(5); stop |
| 9 | 5 | 3 / 5 | 1 | 40 | trigger_event(6); stop |
| 9 | 6 | 3 / 6 | 4 | 45 | trigger_event(7); stop |
| 9 | 7 | 3 / 7 | 2 | 40 | trigger_event(8); stop |
| 9 | 8 | 3 / 8 | 5 | 50 | trigger_event(9); stop |
| 9 | 9 | 3 / 9 | 4 | 40 | trigger_event(10); stop |
| 9 | 10 | 3 / 10 | 4 | 35 | trigger_event(11); stop |
| 9 | 11 | 3 / 11 | 5 | 50 | trigger_event(12); stop |
| 9 | 12 | 3 / 12 | 3 | 40 | set_switch(3); stop |
| 9 | 13 | 6 / 1 | 3 | 60 | trigger_event(14); stop |
| 9 | 14 | 6 / 2 | 1 | 35 | trigger_event(15); stop |
| 9 | 15 | 6 / 3 | 5 | 30 | trigger_event(16); stop |
| 9 | 16 | 6 / 4 | 1 | 35 | set_switch(1); construct_objects(room=6,group_or_wave=200); stop |
| 9 | 17 | 13 / 2 | 0 | 1 | construct_objects(room=1,group_or_wave=25); construct_objects(room=7,group_or_wave=25); clear_switch(179); stop |
| 9 | 1000 | 13 / 111 | 0 | 1 | set_switch(210); stop |
| 9 | 1001 | 13 / 110 | 0 | 1 | set_switch(211); stop |
| 9 | 18 | 3 / 13 | 9 | 20 | trigger_event(19); stop |
| 9 | 19 | 3 / 14 | 6 | 30 | trigger_event(20); stop |
| 9 | 20 | 3 / 15 | 10 | 35 | trigger_event(21); stop |
| 9 | 21 | 3 / 16 | 3 | 50 | set_switch(2); construct_objects(room=7,group_or_wave=33); trigger_event(22); stop |
| 9 | 22 | 7 / 1 | 6 | 5 | set_switch(1); trigger_event(23); trigger_event(24); stop |
| 9 | 23 | 7 / 2 | 2 | 60 | trigger_event(25); stop |
| 9 | 24 | 7 / 3 | 3 | 90 | trigger_event(26); stop |
| 9 | 25 | 7 / 4 | 3 | 30 | trigger_event(27); stop |
| 9 | 26 | 7 / 5 | 1 | 30 | trigger_event(28); stop |
| 9 | 27 | 7 / 6 | 2 | 30 | trigger_event(29); stop |
| 9 | 28 | 7 / 7 | 3 | 30 | trigger_event(30); stop |
| 9 | 29 | 7 / 8 | 3 | 30 | trigger_event(31); stop |
| 9 | 30 | 7 / 9 | 1 | 30 | trigger_event(32); stop |
| 9 | 31 | 7 / 10 | 2 | 30 | trigger_event(33); stop |
| 9 | 32 | 7 / 11 | 3 | 30 | trigger_event(34); stop |
| 9 | 33 | 7 / 12 | 4 | 30 | trigger_event(35); stop |
| 9 | 34 | 7 / 13 | 1 | 30 | trigger_event(36); stop |
| 9 | 35 | 7 / 14 | 2 | 30 | trigger_event(37); stop |
| 9 | 36 | 7 / 15 | 3 | 30 | trigger_event(38); stop |
| 9 | 37 | 7 / 16 | 3 | 30 | trigger_event(39); stop |
| 9 | 38 | 7 / 17 | 1 | 30 | trigger_event(40); stop |
| 9 | 39 | 7 / 18 | 2 | 30 | trigger_event(41); stop |
| 9 | 40 | 7 / 19 | 4 | 30 | trigger_event(42); stop |
| 9 | 41 | 7 / 20 | 3 | 30 | trigger_event(43); stop |
| 9 | 42 | 7 / 21 | 2 | 30 | trigger_event(44); stop |
| 9 | 43 | 7 / 22 | 3 | 30 | trigger_event(45); stop |
| 9 | 44 | 7 / 23 | 1 | 30 | trigger_event(46); stop |
| 9 | 45 | 7 / 24 | 2 | 30 | set_switch(1); trigger_event(47); stop |
| 9 | 46 | 7 / 25 | 3 | 30 | set_switch(1); trigger_event(48); stop |
| 9 | 47 | 7 / 26 | 5 | 30 | trigger_event(49); stop |
| 9 | 48 | 7 / 27 | 2 | 30 | trigger_event(50); stop |
| 9 | 49 | 7 / 28 | 4 | 30 | trigger_event(51); stop |
| 9 | 50 | 7 / 29 | 1 | 30 | set_switch(53); stop |
| 9 | 51 | 7 / 30 | 2 | 30 | set_switch(54); stop |
| 9 | 52 | 7 / 31 | 8 | 60 | set_switch(51); stop |

## Review notes

- Nonzero data after terminal header
