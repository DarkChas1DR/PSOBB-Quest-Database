# 総督の贈り物 — events-ep1/q220-bb-j

Episode1; header quest ID 220; language J. Static scan: **118 objects, 140 enemy/NPC records, 38 events, 250 script labels.** Script roundtrip: byte-identical.

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
0x06, 0x06, 0x00, 0x05, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 18 | 0 |
| 6 | 92 | 122 | 38 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 6 | 201 | 20 / 1 | 2 | 10 | trigger_event(2011); stop |
| 6 | 2011 | 20 / 2 | 3 | 10 | set_switch(5); stop |
| 6 | 401 | 40 / 1 | 2 | 10 | trigger_event(4011); stop |
| 6 | 4011 | 40 / 2 | 3 | 10 | set_switch(6); stop |
| 6 | 501 | 50 / 1 | 3 | 10 | trigger_event(5011); stop |
| 6 | 5011 | 50 / 4 | 3 | 10 | trigger_event(5012); stop |
| 6 | 5012 | 50 / 2 | 4 | 10 | trigger_event(5013); stop |
| 6 | 5013 | 50 / 5 | 4 | 10 | trigger_event(5014); stop |
| 6 | 5014 | 50 / 3 | 1 | 10 | trigger_event(5015); stop |
| 6 | 5015 | 50 / 6 | 1 | 10 | set_switch(10); set_switch(9); stop |
| 6 | 601 | 60 / 1 | 3 | 10 | trigger_event(6011); stop |
| 6 | 6011 | 60 / 5 | 3 | 10 | trigger_event(6012); stop |
| 6 | 6012 | 60 / 2 | 3 | 10 | trigger_event(6013); stop |
| 6 | 6013 | 60 / 6 | 3 | 10 | trigger_event(6014); stop |
| 6 | 6014 | 60 / 3 | 4 | 10 | trigger_event(6015); stop |
| 6 | 6015 | 60 / 7 | 4 | 10 | trigger_event(6016); stop |
| 6 | 6016 | 60 / 4 | 4 | 10 | trigger_event(6017); stop |
| 6 | 6017 | 60 / 8 | 4 | 10 | set_switch(7); set_switch(18); set_switch(19); stop |
| 6 | 761 | 76 / 1 | 7 | 10 | trigger_event(7611); stop |
| 6 | 7611 | 76 / 2 | 2 | 10 | trigger_event(7612); stop |
| 6 | 7612 | 76 / 3 | 6 | 10 | trigger_event(7613); stop |
| 6 | 7613 | 76 / 4 | 3 | 10 | set_switch(21); set_switch(22); stop |
| 6 | 911 | 91 / 1 | 3 | 10 | trigger_event(9111); stop |
| 6 | 9111 | 91 / 2 | 4 | 10 | trigger_event(9112); stop |
| 6 | 9112 | 91 / 3 | 2 | 10 | stop |
| 6 | 912 | 91 / 4 | 3 | 10 | trigger_event(9121); stop |
| 6 | 9121 | 91 / 5 | 4 | 10 | trigger_event(9122); stop |
| 6 | 9122 | 91 / 6 | 2 | 10 | stop |
| 6 | 521 | 52 / 1 | 3 | 10 | trigger_event(5211); stop |
| 6 | 5211 | 52 / 6 | 3 | 10 | trigger_event(5212); stop |
| 6 | 5212 | 52 / 2 | 4 | 10 | trigger_event(5213); stop |
| 6 | 5213 | 52 / 7 | 4 | 10 | trigger_event(5214); stop |
| 6 | 5214 | 52 / 3 | 3 | 10 | trigger_event(5215); stop |
| 6 | 5215 | 52 / 8 | 3 | 10 | trigger_event(5216); stop |
| 6 | 5216 | 52 / 4 | 3 | 10 | trigger_event(5217); stop |
| 6 | 5217 | 52 / 9 | 3 | 10 | trigger_event(5218); stop |
| 6 | 5218 | 52 / 5 | 3 | 10 | trigger_event(5219); stop |
| 6 | 5219 | 52 / 10 | 3 | 10 | set_switch(28); set_switch(29); set_switch(32); set_switch(33); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
