# Mop-up Operation #1 — q101-bb-e

Episode1; header quest ID 101; language E. Static scan: **127 objects, 109 enemy/NPC records, 28 events, 90 script labels.** Script roundtrip: byte-identical.

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
0x00, 0x00, 0x00, 0x00, 0x00
0x01, 0x01, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 28 | 19 | 0 |
| 1 | 99 | 90 | 28 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 111 | 11 / 1 | 3 | 10 | trigger_event(1111); stop |
| 1 | 1111 | 11 / 2 | 3 | 10 | trigger_event(1112); stop |
| 1 | 1112 | 11 / 3 | 3 | 10 | set_switch(6); stop |
| 1 | 101 | 10 / 1 | 3 | 10 | trigger_event(1011); stop |
| 1 | 1011 | 10 / 2 | 3 | 10 | trigger_event(1012); stop |
| 1 | 1012 | 10 / 3 | 1 | 10 | trigger_event(1013); stop |
| 1 | 1013 | 10 / 4 | 4 | 10 | set_switch(7); set_switch(8); stop |
| 1 | 51 | 5 / 1 | 5 | 10 | trigger_event(511); stop |
| 1 | 511 | 5 / 2 | 4 | 10 | trigger_event(512); stop |
| 1 | 512 | 5 / 3 | 6 | 10 | set_switch(1); stop |
| 1 | 21 | 2 / 1 | 4 | 10 | trigger_event(211); stop |
| 1 | 211 | 2 / 2 | 5 | 10 | set_switch(2); stop |
| 1 | 71 | 7 / 1 | 4 | 10 | trigger_event(711); stop |
| 1 | 711 | 7 / 2 | 4 | 10 | trigger_event(712); stop |
| 1 | 712 | 7 / 3 | 4 | 10 | trigger_event(713); stop |
| 1 | 713 | 7 / 4 | 3 | 10 | trigger_event(714); stop |
| 1 | 714 | 7 / 5 | 4 | 10 | trigger_event(715); stop |
| 1 | 715 | 7 / 6 | 3 | 10 | set_switch(3); stop |
| 1 | 41 | 4 / 1 | 2 | 10 | trigger_event(411); stop |
| 1 | 411 | 4 / 2 | 2 | 10 | trigger_event(412); stop |
| 1 | 412 | 4 / 3 | 2 | 10 | trigger_event(413); stop |
| 1 | 413 | 4 / 4 | 3 | 10 | trigger_event(414); stop |
| 1 | 414 | 4 / 5 | 3 | 10 | stop |
| 1 | 42 | 4 / 6 | 2 | 10 | trigger_event(421); stop |
| 1 | 421 | 4 / 7 | 2 | 10 | trigger_event(422); stop |
| 1 | 422 | 4 / 8 | 2 | 10 | trigger_event(423); stop |
| 1 | 423 | 4 / 9 | 3 | 10 | trigger_event(424); stop |
| 1 | 424 | 4 / 10 | 3 | 10 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

A backup is present; decompressed content identical: True. See [text differences](<backup-diff.txt>).
