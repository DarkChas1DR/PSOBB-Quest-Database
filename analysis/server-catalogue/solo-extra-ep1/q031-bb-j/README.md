# ブラックペーパーの危険な取引 — solo-extra-ep1/q031-bb-j

Episode4; header quest ID 31; language J. Static scan: **200 objects, 95 enemy/NPC records, 18 events, 168 script labels.** Script roundtrip: byte-identical.

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
0x03, 0x26, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 18 | 0 |
| 3 | 174 | 77 | 18 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 3 | 201 | 20 / 1 | 3 | 30 | trigger_event(202); stop |
| 3 | 202 | 20 / 2 | 9 | 30 | trigger_event(203); stop |
| 3 | 203 | 20 / 3 | 9 | 30 | trigger_event(204); stop |
| 3 | 204 | 20 / 4 | 9 | 30 | trigger_event(205); stop |
| 3 | 205 | 20 / 5 | 9 | 30 | trigger_event(206); stop |
| 3 | 206 | 20 / 6 | 9 | 30 | set_switch(20); construct_objects(room=20,group_or_wave=1); stop |
| 3 | 301 | 30 / 1 | 1 | 30 | trigger_event(302); stop |
| 3 | 302 | 30 / 2 | 1 | 30 | trigger_event(303); stop |
| 3 | 303 | 30 / 3 | 3 | 30 | trigger_event(304); stop |
| 3 | 304 | 30 / 4 | 2 | 30 | trigger_event(305); stop |
| 3 | 305 | 30 / 5 | 3 | 30 | trigger_event(306); stop |
| 3 | 306 | 30 / 6 | 2 | 30 | set_switch(30); construct_objects(room=30,group_or_wave=1); stop |
| 3 | 901 | 90 / 1 | 1 | 30 | trigger_event(902); stop |
| 3 | 902 | 90 / 2 | 2 | 30 | trigger_event(903); stop |
| 3 | 903 | 90 / 3 | 3 | 30 | trigger_event(904); stop |
| 3 | 904 | 90 / 4 | 4 | 30 | trigger_event(905); stop |
| 3 | 905 | 90 / 5 | 2 | 30 | trigger_event(906); stop |
| 3 | 906 | 90 / 6 | 3 | 30 | set_switch(90); construct_objects(room=90,group_or_wave=1); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
