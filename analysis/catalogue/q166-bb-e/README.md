# Sweep-up Operation #5 — q166-bb-e

Episode2; header quest ID 166; language E. Static scan: **149 objects, 206 enemy/NPC records, 57 events, 44 script labels.** Script roundtrip: alignment-only.

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
| 0 | 43 | 8 | 0 |
| 1 | 106 | 198 | 57 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 101 | 10 / 1 | 4 | 30 | trigger_event(102); stop |
| 1 | 102 | 10 / 2 | 3 | 20 | trigger_event(103); stop |
| 1 | 103 | 10 / 3 | 4 | 30 | set_switch(3); set_switch(4); stop |
| 1 | 601 | 60 / 1 | 5 | 45 | trigger_event(602); stop |
| 1 | 602 | 60 / 2 | 4 | 30 | set_switch(5); set_switch(6); stop |
| 1 | 931 | 93 / 1 | 3 | 30 | trigger_event(932); stop |
| 1 | 932 | 93 / 2 | 3 | 30 | set_switch(7); set_switch(8); stop |
| 1 | 1601 | 160 / 1 | 1 | 1 | stop |
| 1 | 941 | 94 / 1 | 3 | 30 | trigger_event(942); stop |
| 1 | 942 | 94 / 2 | 3 | 30 | set_switch(11); set_switch(12); stop |
| 1 | 401 | 40 / 1 | 5 | 30 | trigger_event(402); stop |
| 1 | 402 | 40 / 2 | 4 | 30 | trigger_event(403); stop |
| 1 | 403 | 40 / 3 | 6 | 30 | set_switch(21); set_switch(22); stop |
| 1 | 1401 | 140 / 1 | 1 | 1 | stop |
| 1 | 301 | 30 / 1 | 4 | 60 | trigger_event(302); stop |
| 1 | 302 | 30 / 2 | 5 | 30 | trigger_event(303); stop |
| 1 | 303 | 30 / 3 | 3 | 30 | set_switch(23); set_switch(24); trigger_event(415); stop |
| 1 | 415 | 41 / 5 | 1 | 1 | trigger_event(411); trigger_event(412); stop |
| 1 | 411 | 41 / 1 | 3 | 60 | trigger_event(413); stop |
| 1 | 413 | 41 / 3 | 3 | 60 | trigger_event(414); stop |
| 1 | 414 | 41 / 4 | 2 | 60 | stop |
| 1 | 412 | 41 / 2 | 3 | 60 | trigger_event(416); stop |
| 1 | 416 | 41 / 6 | 3 | 60 | trigger_event(417); stop |
| 1 | 417 | 41 / 7 | 2 | 60 | trigger_event(418); stop |
| 1 | 418 | 41 / 8 | 3 | 60 | stop |
| 1 | 410 | 41 / 0 | 0 | 1 | set_switch(25); set_switch(26); construct_objects(room=2,group_or_wave=1); stop |
| 1 | 801 | 80 / 1 | 5 | 30 | trigger_event(802); stop |
| 1 | 802 | 80 / 2 | 5 | 30 | trigger_event(803); stop |
| 1 | 803 | 80 / 3 | 6 | 30 | trigger_event(804); stop |
| 1 | 804 | 80 / 4 | 2 | 60 | set_switch(20); set_switch(99); trigger_event(501); stop |
| 1 | 501 | 50 / 1 | 1 | 1 | trigger_event(502); stop |
| 1 | 502 | 50 / 2 | 4 | 30 | trigger_event(503); stop |
| 1 | 503 | 50 / 3 | 4 | 30 | stop |
| 1 | 505 | 50 / 5 | 6 | 1 | trigger_event(506); stop |
| 1 | 506 | 50 / 6 | 2 | 30 | trigger_event(507); stop |
| 1 | 507 | 50 / 7 | 3 | 30 | stop |
| 1 | 500 | 50 / 0 | 0 | 1 | set_switch(18); set_switch(17); stop |
| 1 | 201 | 20 / 1 | 3 | 30 | trigger_event(202); stop |
| 1 | 202 | 20 / 2 | 4 | 30 | set_switch(32); set_switch(31); stop |
| 1 | 921 | 92 / 1 | 3 | 30 | trigger_event(922); stop |
| 1 | 922 | 92 / 2 | 3 | 30 | set_switch(33); set_switch(34); stop |
| 1 | 1001 | 100 / 1 | 3 | 1 | stop |
| 1 | 706 | 70 / 6 | 1 | 1 | stop |
| 1 | 701 | 70 / 1 | 4 | 30 | trigger_event(702); stop |
| 1 | 702 | 70 / 2 | 7 | 30 | stop |
| 1 | 703 | 70 / 3 | 3 | 30 | trigger_event(704); stop |
| 1 | 704 | 70 / 4 | 3 | 30 | trigger_event(705); stop |
| 1 | 705 | 70 / 5 | 5 | 30 | stop |
| 1 | 700 | 70 / 0 | 0 | 1 | set_switch(35); set_switch(36); set_switch(37); set_switch(38); stop |
| 1 | 111 | 11 / 1 | 3 | 30 | trigger_event(112); stop |
| 1 | 112 | 11 / 2 | 5 | 60 | trigger_event(113); stop |
| 1 | 113 | 11 / 3 | 3 | 60 | set_switch(39); set_switch(40); stop |
| 1 | 611 | 61 / 1 | 5 | 30 | trigger_event(612); stop |
| 1 | 612 | 61 / 2 | 5 | 30 | trigger_event(613); stop |
| 1 | 613 | 61 / 3 | 4 | 30 | trigger_event(614); stop |
| 1 | 614 | 61 / 4 | 5 | 30 | trigger_event(615); stop |
| 1 | 615 | 61 / 5 | 8 | 10 | set_switch(42); set_switch(41); stop |

## Review notes

- Nonzero data after terminal header
