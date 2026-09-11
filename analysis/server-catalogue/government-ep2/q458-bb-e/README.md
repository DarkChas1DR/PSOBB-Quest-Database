# 6-3:Test/Spaceship 3 — government-ep2/q458-bb-e

Episode2; header quest ID 458; language E. Static scan: **196 objects, 199 enemy/NPC records, 51 events, 146 script labels.** Script roundtrip: byte-identical.

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
0x00, 0x12, 0x00, 0x00, 0x00
0x03, 0x15, 0x00, 0x02, 0x00
0x04, 0x16, 0x00, 0x02, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 53 | 18 | 0 |
| 3 | 55 | 89 | 19 |
| 4 | 88 | 92 | 32 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 3 | 101 | 10 / 1 | 6 | 0 | set_switch(13); stop |
| 3 | 401 | 40 / 1 | 5 | 120 | trigger_event(4011); stop |
| 3 | 4011 | 40 / 2 | 7 | 10 | trigger_event(4012); stop |
| 3 | 4012 | 40 / 3 | 4 | 150 | set_switch(1); set_switch(2); set_switch(3); set_switch(4); set_switch(5); set_switch(6); stop |
| 3 | 411 | 41 / 1 | 6 | 30 | trigger_event(4111); stop |
| 3 | 4111 | 41 / 2 | 6 | 10 | trigger_event(4112); stop |
| 3 | 4112 | 41 / 3 | 7 | 10 | set_switch(21); set_switch(22); set_switch(23); stop |
| 3 | 501 | 50 / 1 | 6 | 90 | trigger_event(5011); stop |
| 3 | 5011 | 50 / 2 | 6 | 10 | trigger_event(5012); stop |
| 3 | 5012 | 50 / 3 | 6 | 10 | trigger_event(5013); stop |
| 3 | 5013 | 50 / 4 | 7 | 10 | set_switch(9); set_switch(10); stop |
| 3 | 511 | 51 / 1 | 5 | 120 | trigger_event(5111); stop |
| 3 | 5111 | 51 / 2 | 4 | 60 | trigger_event(5112); stop |
| 3 | 5112 | 51 / 3 | 6 | 60 | trigger_event(5113); stop |
| 3 | 5113 | 51 / 4 | 4 | 120 | stop |
| 3 | 512 | 51 / 5 | 1 | 120 | trigger_event(5121); stop |
| 3 | 5121 | 51 / 6 | 1 | 60 | trigger_event(5122); stop |
| 3 | 5122 | 51 / 7 | 1 | 60 | trigger_event(5123); stop |
| 3 | 5123 | 51 / 8 | 1 | 60 | stop |
| 4 | 101 | 10 / 1 | 4 | 60 | trigger_event(1011); stop |
| 4 | 1011 | 10 / 2 | 4 | 10 | set_switch(22); set_switch(23); set_switch(24); set_switch(25); stop |
| 4 | 111 | 11 / 1 | 4 | 30 | set_switch(5); set_switch(6); stop |
| 4 | 201 | 20 / 1 | 5 | 10 | trigger_event(2011); stop |
| 4 | 2011 | 20 / 2 | 6 | 30 | set_switch(14); set_switch(15); set_switch(16); set_switch(17); stop |
| 4 | 211 | 21 / 1 | 3 | 10 | trigger_event(2111); stop |
| 4 | 2111 | 21 / 2 | 3 | 30 | set_switch(11); set_switch(12); set_switch(13); set_switch(30); stop |
| 4 | 301 | 30 / 1 | 3 | 120 | set_switch(20); set_switch(21); stop |
| 4 | 311 | 31 / 1 | 3 | 30 | trigger_event(3111); stop |
| 4 | 3111 | 31 / 2 | 4 | 30 | set_switch(7); set_switch(8); stop |
| 4 | 401 | 40 / 1 | 6 | 10 | trigger_event(4011); stop |
| 4 | 4011 | 40 / 2 | 3 | 90 | set_switch(18); set_switch(19); stop |
| 4 | 501 | 50 / 1 | 7 | 10 | trigger_event(5011); stop |
| 4 | 5011 | 50 / 2 | 6 | 10 | trigger_event(5012); stop |
| 4 | 5012 | 50 / 3 | 6 | 30 | set_switch(9); set_switch(10); stop |
| 4 | 511 | 51 / 1 | 1 | 120 | trigger_event(5111); stop |
| 4 | 5111 | 51 / 2 | 1 | 30 | stop |
| 4 | 512 | 51 / 3 | 1 | 120 | trigger_event(5121); stop |
| 4 | 5121 | 51 / 4 | 1 | 30 | stop |
| 4 | 513 | 51 / 5 | 1 | 120 | trigger_event(5131); stop |
| 4 | 5131 | 51 / 6 | 1 | 30 | trigger_event(5132); stop |
| 4 | 5132 | 51 / 7 | 1 | 60 | stop |
| 4 | 514 | 51 / 8 | 1 | 120 | trigger_event(5141); stop |
| 4 | 5141 | 51 / 9 | 1 | 30 | trigger_event(5142); stop |
| 4 | 5142 | 51 / 10 | 1 | 60 | stop |
| 4 | 515 | 51 / 11 | 2 | 90 | trigger_event(5151); stop |
| 4 | 5151 | 51 / 12 | 2 | 30 | trigger_event(5152); stop |
| 4 | 5152 | 51 / 13 | 2 | 30 | trigger_event(5153); stop |
| 4 | 5153 | 51 / 14 | 2 | 60 | trigger_event(5154); stop |
| 4 | 5154 | 51 / 15 | 3 | 120 | stop |
| 4 | 1601 | 160 / 1 | 1 | 0 | stop |
| 4 | 1901 | 190 / 1 | 3 | 30 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
