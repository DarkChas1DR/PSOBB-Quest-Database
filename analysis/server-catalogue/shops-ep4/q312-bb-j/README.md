# クレアの取引５ — shops-ep4/q312-bb-j

Episode4; header quest ID 312; language J. Static scan: **85 objects, 134 enemy/NPC records, 32 events, 334 script labels.** Script roundtrip: alignment-only.

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
0x00, 0x2D, 0x00, 0x00, 0x00
0x05, 0x28, 0x00, 0x00, 0x00
0x08, 0x2B, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 30 | 20 | 0 |
| 5 | 50 | 114 | 32 |
| 8 | 5 | 0 | 0 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 5 | 101 | 10 / 1 | 3 | 0 | trigger_event(102); stop |
| 5 | 102 | 10 / 2 | 3 | 0 | trigger_event(103); stop |
| 5 | 103 | 10 / 3 | 4 | 0 | trigger_event(104); stop |
| 5 | 104 | 10 / 4 | 4 | 0 | trigger_event(105); stop |
| 5 | 105 | 10 / 5 | 5 | 0 | set_switch(10); stop |
| 5 | 201 | 20 / 1 | 3 | 0 | trigger_event(202); stop |
| 5 | 202 | 20 / 2 | 4 | 0 | trigger_event(203); stop |
| 5 | 203 | 20 / 3 | 5 | 0 | trigger_event(204); stop |
| 5 | 204 | 20 / 4 | 3 | 0 | set_switch(20); stop |
| 5 | 301 | 30 / 1 | 4 | 0 | trigger_event(302); stop |
| 5 | 302 | 30 / 2 | 4 | 0 | trigger_event(303); stop |
| 5 | 303 | 30 / 3 | 4 | 0 | trigger_event(304); stop |
| 5 | 304 | 30 / 4 | 5 | 0 | trigger_event(305); stop |
| 5 | 305 | 30 / 5 | 3 | 0 | trigger_event(306); stop |
| 5 | 306 | 30 / 6 | 3 | 0 | trigger_event(307); stop |
| 5 | 307 | 30 / 7 | 2 | 0 | set_switch(30); stop |
| 5 | 401 | 40 / 1 | 3 | 0 | trigger_event(402); stop |
| 5 | 402 | 40 / 2 | 3 | 0 | trigger_event(403); stop |
| 5 | 403 | 40 / 3 | 3 | 0 | trigger_event(404); stop |
| 5 | 404 | 40 / 4 | 4 | 0 | trigger_event(405); stop |
| 5 | 405 | 40 / 5 | 3 | 0 | set_switch(40); stop |
| 5 | 501 | 50 / 1 | 3 | 0 | trigger_event(502); stop |
| 5 | 502 | 50 / 2 | 4 | 0 | trigger_event(503); stop |
| 5 | 503 | 50 / 3 | 3 | 0 | trigger_event(504); stop |
| 5 | 504 | 50 / 4 | 3 | 0 | set_switch(50); stop |
| 5 | 601 | 60 / 1 | 3 | 0 | trigger_event(602); stop |
| 5 | 602 | 60 / 2 | 2 | 0 | trigger_event(603); stop |
| 5 | 603 | 60 / 3 | 3 | 0 | trigger_event(604); stop |
| 5 | 604 | 60 / 4 | 3 | 0 | trigger_event(605); stop |
| 5 | 605 | 60 / 5 | 4 | 0 | trigger_event(606); stop |
| 5 | 606 | 60 / 6 | 5 | 0 | trigger_event(607); stop |
| 5 | 607 | 60 / 7 | 6 | 0 | set_switch(60); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
