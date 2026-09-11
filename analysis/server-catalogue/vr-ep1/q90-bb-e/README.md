# Simulator v1.01 — vr-ep1/q90-bb-e

Episode1; header quest ID 90; language E. Static scan: **223 objects, 279 enemy/NPC records, 26 events, 119 script labels.** Script roundtrip: alignment-only.

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
| 0 | 25 | 24 | 0 |
| 1 | 61 | 34 | 4 |
| 2 | 24 | 38 | 3 |
| 3 | 24 | 78 | 4 |
| 4 | 14 | 18 | 3 |
| 5 | 47 | 34 | 4 |
| 6 | 10 | 52 | 7 |
| 7 | 18 | 1 | 1 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 501 | 11 / 1 | 7 | 1 | trigger_event(502); stop |
| 1 | 502 | 11 / 2 | 8 | 1 | trigger_event(503); stop |
| 1 | 503 | 11 / 3 | 8 | 1 | trigger_event(504); stop |
| 1 | 504 | 11 / 4 | 11 | 1 | construct_objects(room=11,group_or_wave=1); stop |
| 2 | 601 | 60 / 1 | 6 | 1 | trigger_event(602); stop |
| 2 | 602 | 60 / 2 | 11 | 30 | trigger_event(603); set_switch(5); stop |
| 2 | 603 | 60 / 3 | 19 | 25 | construct_objects(room=60,group_or_wave=1); stop |
| 3 | 701 | 80 / 1 | 13 | 100 | trigger_event(702); stop |
| 3 | 702 | 80 / 2 | 11 | 50 | trigger_event(703); stop |
| 3 | 703 | 80 / 3 | 27 | 50 | trigger_event(704); stop |
| 3 | 704 | 80 / 4 | 25 | 40 | construct_objects(room=80,group_or_wave=1); stop |
| 4 | 801 | 50 / 1 | 6 | 40 | trigger_event(802); stop |
| 4 | 802 | 50 / 2 | 6 | 50 | trigger_event(803); stop |
| 4 | 803 | 50 / 3 | 6 | 50 | construct_objects(room=50,group_or_wave=1); stop |
| 5 | 730 | 80 / 1 | 6 | 100 | trigger_event(731); stop |
| 5 | 731 | 80 / 2 | 4 | 50 | trigger_event(732); stop |
| 5 | 732 | 80 / 3 | 10 | 75 | set_switch(5); trigger_event(733); stop |
| 5 | 733 | 80 / 4 | 14 | 75 | construct_objects(room=80,group_or_wave=1); stop |
| 6 | 530 | 40 / 1 | 4 | 20 | trigger_event(533); stop |
| 6 | 533 | 40 / 4 | 4 | 45 | trigger_event(534); stop |
| 6 | 534 | 40 / 5 | 4 | 50 | trigger_event(535); stop |
| 6 | 535 | 40 / 6 | 6 | 50 | trigger_event(536); stop |
| 6 | 536 | 40 / 7 | 6 | 50 | trigger_event(537); stop |
| 6 | 537 | 40 / 8 | 15 | 50 | trigger_event(538); stop |
| 6 | 538 | 40 / 9 | 12 | 50 | construct_objects(room=40,group_or_wave=1); stop |
| 7 | 1 | 1 / 1 | 1 | 50 | construct_objects(room=1,group_or_wave=1); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
