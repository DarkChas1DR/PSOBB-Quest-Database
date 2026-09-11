# ２－１：灼熱の洞窟 — government-ep1/q404-bb-j

Episode1; header quest ID 404; language J. Static scan: **237 objects, 227 enemy/NPC records, 48 events, 72 script labels.** Script roundtrip: alignment-only.

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
0x03, 0x03, 0x00, 0x00, 0x00
0x04, 0x03, 0x00, 0x01, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 27 | 20 | 0 |
| 3 | 154 | 160 | 36 |
| 4 | 56 | 47 | 12 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 3 | 501 | 50 / 1 | 4 | 40 | stop |
| 3 | 502 | 50 / 2 | 6 | 10 | trigger_event(5021); stop |
| 3 | 5021 | 50 / 3 | 5 | 10 | trigger_event(5022); stop |
| 3 | 5022 | 50 / 4 | 4 | 10 | set_switch(2); set_switch(3); stop |
| 3 | 321 | 32 / 1 | 5 | 40 | trigger_event(3211); stop |
| 3 | 3211 | 32 / 2 | 4 | 40 | trigger_event(3212); stop |
| 3 | 3212 | 32 / 3 | 5 | 40 | set_switch(27); set_switch(5); set_switch(7); stop |
| 3 | 341 | 34 / 1 | 6 | 40 | trigger_event(3411); stop |
| 3 | 3411 | 34 / 2 | 6 | 40 | trigger_event(3412); stop |
| 3 | 3412 | 34 / 3 | 8 | 40 | set_switch(6); set_switch(10); stop |
| 3 | 531 | 53 / 1 | 5 | 10 | trigger_event(5311); stop |
| 3 | 5311 | 53 / 2 | 3 | 10 | trigger_event(5312); stop |
| 3 | 5312 | 53 / 3 | 4 | 10 | trigger_event(5313); stop |
| 3 | 5313 | 53 / 4 | 6 | 10 | set_switch(8); set_switch(11); set_switch(12); stop |
| 3 | 101 | 10 / 1 | 3 | 40 | trigger_event(1011); stop |
| 3 | 1011 | 10 / 2 | 4 | 40 | set_switch(8); set_switch(11); set_switch(12); stop |
| 3 | 601 | 60 / 1 | 6 | 40 | trigger_event(6011); stop |
| 3 | 6011 | 60 / 2 | 6 | 40 | trigger_event(6012); stop |
| 3 | 6012 | 60 / 3 | 6 | 40 | trigger_event(6013); stop |
| 3 | 6013 | 60 / 4 | 5 | 40 | set_switch(13); set_switch(14); stop |
| 3 | 113 | 11 / 1 | 1 | 40 | trigger_event(1111); stop |
| 3 | 1111 | 11 / 2 | 4 | 40 | set_switch(15); set_switch(16); set_switch(17); set_switch(18); stop |
| 3 | 112 | 11 / 3 | 3 | 40 | stop |
| 3 | 331 | 33 / 1 | 5 | 40 | trigger_event(3311); stop |
| 3 | 3311 | 33 / 2 | 8 | 40 | stop |
| 3 | 511 | 51 / 1 | 6 | 10 | trigger_event(5111); stop |
| 3 | 5111 | 51 / 2 | 7 | 10 | trigger_event(5112); stop |
| 3 | 5112 | 51 / 3 | 4 | 10 | trigger_event(5113); stop |
| 3 | 5113 | 51 / 4 | 1 | 10 | trigger_event(5114); stop |
| 3 | 5114 | 51 / 5 | 1 | 10 | set_switch(19); set_switch(20); set_switch(23); set_switch(25); set_switch(26); set_switch(24); set_switch(22); stop |
| 3 | 201 | 20 / 1 | 1 | 40 | stop |
| 3 | 202 | 20 / 2 | 2 | 40 | stop |
| 3 | 521 | 52 / 1 | 5 | 10 | trigger_event(5211); stop |
| 3 | 5211 | 52 / 2 | 2 | 10 | trigger_event(5212); stop |
| 3 | 5212 | 52 / 3 | 4 | 10 | trigger_event(5213); stop |
| 3 | 5213 | 52 / 4 | 5 | 10 | set_switch(21); stop |
| 4 | 111 | 11 / 1 | 5 | 30 | set_switch(29); set_switch(27); stop |
| 4 | 521 | 52 / 1 | 3 | 30 | trigger_event(5211); stop |
| 4 | 5211 | 52 / 2 | 3 | 120 | trigger_event(5212); stop |
| 4 | 5212 | 52 / 3 | 4 | 120 | trigger_event(5213); stop |
| 4 | 5213 | 52 / 4 | 3 | 120 | set_switch(101); stop |
| 4 | 522 | 52 / 5 | 3 | 120 | trigger_event(5221); stop |
| 4 | 5221 | 52 / 6 | 3 | 120 | trigger_event(5222); stop |
| 4 | 5222 | 52 / 7 | 3 | 120 | trigger_event(5223); stop |
| 4 | 5223 | 52 / 8 | 3 | 120 | set_switch(102); stop |
| 4 | 523 | 52 / 9 | 6 | 90 | trigger_event(5231); stop |
| 4 | 5231 | 52 / 10 | 5 | 60 | trigger_event(5232); stop |
| 4 | 5232 | 52 / 11 | 6 | 180 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
