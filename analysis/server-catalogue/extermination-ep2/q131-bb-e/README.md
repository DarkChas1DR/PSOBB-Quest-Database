# Monster Bash 5 — extermination-ep2/q131-bb-e

Episode2; header quest ID 131; language E. Static scan: **476 objects, 378 enemy/NPC records, 55 events, 103 script labels.** Script roundtrip: alignment-only.

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
| 0 | 53 | 18 | 0 |
| 1 | 202 | 208 | 27 |
| 2 | 193 | 151 | 27 |
| 14 | 28 | 1 | 1 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 101 | 10 / 1 | 23 | 10 | set_switch(11); set_switch(12); stop |
| 1 | 111 | 11 / 1 | 5 | 100 | trigger_event(1111); stop |
| 1 | 1111 | 11 / 2 | 4 | 100 | set_switch(32); set_switch(33); stop |
| 1 | 201 | 20 / 1 | 16 | 10 | set_switch(9); set_switch(10); stop |
| 1 | 301 | 30 / 1 | 3 | 200 | trigger_event(3011); stop |
| 1 | 3011 | 30 / 2 | 3 | 10 | set_switch(21); set_switch(22); set_switch(23); set_switch(24); set_switch(25); set_switch(26); set_switch(27); set_switch(30); set_switch(31); stop |
| 1 | 401 | 40 / 1 | 6 | 1 | trigger_event(4011); stop |
| 1 | 4011 | 40 / 2 | 9 | 1 | trigger_event(4012); stop |
| 1 | 4012 | 40 / 3 | 0 | 200 | set_switch(36); set_switch(37); set_switch(38); set_switch(39); set_switch(40); set_switch(41); stop |
| 1 | 411 | 41 / 1 | 5 | 10 | trigger_event(4111); stop |
| 1 | 4111 | 41 / 2 | 6 | 10 | set_switch(44); set_switch(45); stop |
| 1 | 501 | 50 / 1 | 6 | 10 | set_switch(13); set_switch(14); set_switch(15); set_switch(16); stop |
| 1 | 502 | 50 / 2 | 3 | 10 | trigger_event(5021); stop |
| 1 | 5021 | 50 / 3 | 8 | 200 | set_switch(19); set_switch(20); stop |
| 1 | 601 | 60 / 1 | 10 | 10 | trigger_event(6011); stop |
| 1 | 6011 | 60 / 2 | 20 | 100 | set_switch(9); set_switch(10); set_switch(15); set_switch(16); set_switch(17); set_switch(18); stop |
| 1 | 611 | 61 / 1 | 6 | 10 | trigger_event(6111); stop |
| 1 | 6111 | 61 / 2 | 3 | 10 | set_switch(25); set_switch(26); set_switch(30); set_switch(31); stop |
| 1 | 701 | 70 / 1 | 7 | 10 | trigger_event(7011); stop |
| 1 | 7011 | 70 / 2 | 9 | 100 | set_switch(11); set_switch(12); set_switch(13); set_switch(14); stop |
| 1 | 702 | 70 / 3 | 3 | 10 | set_switch(34); set_switch(35); stop |
| 1 | 703 | 70 / 4 | 5 | 10 | stop |
| 1 | 911 | 91 / 1 | 4 | 250 | set_switch(42); set_switch(43); stop |
| 1 | 931 | 93 / 1 | 4 | 10 | trigger_event(9311); stop |
| 1 | 9311 | 93 / 2 | 5 | 10 | set_switch(21); set_switch(22); set_switch(28); set_switch(29); stop |
| 1 | 1401 | 140 / 1 | 13 | 1 | stop |
| 1 | 5201 | 520 / 1 | 1 | 1 | stop |
| 2 | 101 | 10 / 1 | 5 | 200 | set_switch(35); set_switch(36); stop |
| 2 | 111 | 11 / 1 | 5 | 1 | trigger_event(1111); stop |
| 2 | 1111 | 11 / 2 | 6 | 1 | trigger_event(1112); stop |
| 2 | 1112 | 11 / 3 | 19 | 100 | set_switch(39); set_switch(40); stop |
| 2 | 201 | 20 / 1 | 5 | 10 | set_switch(19); set_switch(20); stop |
| 2 | 301 | 30 / 1 | 4 | 200 | trigger_event(3011); stop |
| 2 | 3011 | 30 / 2 | 4 | 10 | set_switch(31); set_switch(32); set_switch(33); set_switch(34); stop |
| 2 | 401 | 40 / 1 | 5 | 1 | trigger_event(4011); stop |
| 2 | 4011 | 40 / 2 | 6 | 200 | set_switch(7); set_switch(8); set_switch(9); set_switch(10); stop |
| 2 | 411 | 41 / 1 | 6 | 10 | trigger_event(4111); stop |
| 2 | 4111 | 41 / 2 | 3 | 10 | trigger_event(4112); stop |
| 2 | 4112 | 41 / 3 | 6 | 10 | set_switch(13); set_switch(14); stop |
| 2 | 501 | 50 / 1 | 3 | 10 | stop |
| 2 | 502 | 50 / 2 | 5 | 10 | trigger_event(5021); stop |
| 2 | 5021 | 50 / 3 | 4 | 200 | set_switch(11); set_switch(12); stop |
| 2 | 601 | 60 / 1 | 5 | 10 | trigger_event(6011); stop |
| 2 | 6011 | 60 / 2 | 4 | 10 | set_switch(5); set_switch(6); stop |
| 2 | 611 | 61 / 1 | 6 | 10 | trigger_event(6111); stop |
| 2 | 6111 | 61 / 2 | 6 | 10 | trigger_event(6112); stop |
| 2 | 6112 | 61 / 3 | 6 | 200 | set_switch(15); set_switch(16); set_switch(17); set_switch(18); set_switch(21); set_switch(22); stop |
| 2 | 701 | 70 / 1 | 9 | 10 | set_switch(25); set_switch(26); stop |
| 2 | 702 | 70 / 2 | 5 | 10 | trigger_event(7021); stop |
| 2 | 7021 | 70 / 3 | 5 | 10 | set_switch(27); set_switch(28); set_switch(29); set_switch(30); stop |
| 2 | 911 | 91 / 1 | 3 | 250 | set_switch(23); set_switch(24); set_switch(25); set_switch(26); stop |
| 2 | 931 | 93 / 1 | 9 | 250 | set_switch(37); set_switch(38); stop |
| 2 | 1031 | 103 / 1 | 2 | 1 | stop |
| 2 | 1641 | 164 / 1 | 1 | 1 | stop |
| 14 | 1 | 1 / 1 | 1 | 50 | construct_objects(room=1,group_or_wave=1); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
