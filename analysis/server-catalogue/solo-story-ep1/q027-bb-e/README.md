# Seat of the Heart — solo-story-ep1/q027-bb-e

Episode2; header quest ID 27; language E. Static scan: **756 objects, 239 enemy/NPC records, 57 events, 2313 script labels.** Script roundtrip: byte-identical.

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
0x02, 0x14, 0x00, 0x01, 0x00
0x04, 0x16, 0x00, 0x00, 0x00
0x05, 0x17, 0x00, 0x00, 0x00
0x10, 0x22, 0x00, 0x00, 0x00
0x11, 0x23, 0x00, 0x00, 0x00
0x0F, 0x21, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 67 | 26 | 0 |
| 2 | 156 | 61 | 21 |
| 4 | 143 | 64 | 16 |
| 5 | 131 | 47 | 15 |
| 15 | 6 | 1 | 1 |
| 16 | 29 | 0 | 0 |
| 17 | 224 | 40 | 4 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 2 | 101 | 10 / 1 | 4 | 10 | trigger_event(1011); stop |
| 2 | 1011 | 10 / 2 | 4 | 10 | trigger_event(1012); stop |
| 2 | 1012 | 10 / 3 | 4 | 10 | set_switch(35); set_switch(36); stop |
| 2 | 111 | 11 / 1 | 3 | 150 | trigger_event(1111); stop |
| 2 | 1111 | 11 / 2 | 5 | 10 | trigger_event(1112); stop |
| 2 | 1112 | 11 / 3 | 1 | 150 | set_switch(39); set_switch(40); stop |
| 2 | 301 | 30 / 1 | 1 | 10 | set_switch(31); set_switch(32); set_switch(33); set_switch(34); stop |
| 2 | 411 | 41 / 1 | 3 | 10 | trigger_event(4111); stop |
| 2 | 4111 | 41 / 2 | 5 | 10 | trigger_event(4112); stop |
| 2 | 4112 | 41 / 3 | 2 | 100 | set_switch(13); set_switch(14); stop |
| 2 | 501 | 50 / 1 | 2 | 10 | trigger_event(5011); stop |
| 2 | 5011 | 50 / 2 | 3 | 10 | trigger_event(5012); stop |
| 2 | 5012 | 50 / 3 | 3 | 10 | set_switch(150); stop |
| 2 | 502 | 50 / 4 | 0 | 1 | set_switch(9); set_switch(10); set_switch(11); set_switch(12); stop |
| 2 | 611 | 61 / 1 | 2 | 300 | set_switch(15); set_switch(16); set_switch(21); set_switch(22); stop |
| 2 | 701 | 70 / 1 | 4 | 10 | trigger_event(7011); stop |
| 2 | 7011 | 70 / 2 | 3 | 100 | set_switch(26); stop |
| 2 | 702 | 70 / 3 | 1 | 10 | set_switch(27); set_switch(28); set_switch(29); set_switch(30); stop |
| 2 | 911 | 91 / 1 | 4 | 10 | set_switch(23); set_switch(24); stop |
| 2 | 921 | 92 / 1 | 3 | 1 | stop |
| 2 | 931 | 93 / 1 | 4 | 1 | set_switch(37); set_switch(38); stop |
| 4 | 101 | 10 / 1 | 1 | 10 | trigger_event(1011); stop |
| 4 | 1011 | 10 / 2 | 4 | 10 | set_switch(39); set_switch(40); stop |
| 4 | 121 | 12 / 1 | 1 | 60 | set_switch(31); set_switch(32); stop |
| 4 | 301 | 30 / 1 | 3 | 10 | trigger_event(3011); stop |
| 4 | 3011 | 30 / 2 | 3 | 10 | trigger_event(3012); stop |
| 4 | 3012 | 30 / 3 | 4 | 10 | trigger_event(3013); stop |
| 4 | 3013 | 30 / 4 | 5 | 10 | trigger_event(3014); stop |
| 4 | 3014 | 30 / 5 | 5 | 10 | set_switch(19); stop |
| 4 | 401 | 40 / 1 | 5 | 10 | trigger_event(4011); stop |
| 4 | 4011 | 40 / 2 | 4 | 10 | set_switch(34); set_switch(37); set_switch(38); stop |
| 4 | 411 | 41 / 1 | 9 | 1 | stop |
| 4 | 501 | 50 / 1 | 5 | 10 | set_switch(20); set_switch(21); set_switch(22); set_switch(23); set_switch(24); set_switch(27); set_switch(28); stop |
| 4 | 521 | 52 / 1 | 5 | 10 | trigger_event(5211); stop |
| 4 | 5211 | 52 / 2 | 6 | 100 | set_switch(25); set_switch(26); set_switch(29); set_switch(30); stop |
| 4 | 1611 | 161 / 1 | 2 | 1 | set_switch(33); stop |
| 4 | 1811 | 181 / 1 | 2 | 1 | stop |
| 15 | 1 | 1 / 1 | 1 | 50 | construct_objects(room=1,group_or_wave=1); stop |
| 5 | 21 | 2 / 1 | 3 | 10 | trigger_event(211); stop |
| 5 | 211 | 2 / 2 | 2 | 60 | set_switch(2); stop |
| 5 | 31 | 3 / 1 | 3 | 1 | trigger_event(311); stop |
| 5 | 311 | 3 / 2 | 5 | 10 | set_switch(3); stop |
| 5 | 41 | 4 / 1 | 5 | 1 | trigger_event(411); stop |
| 5 | 411 | 4 / 2 | 2 | 60 | trigger_event(412); stop |
| 5 | 412 | 4 / 3 | 5 | 10 | set_switch(4); stop |
| 5 | 61 | 6 / 1 | 2 | 10 | stop |
| 5 | 81 | 8 / 1 | 2 | 10 | trigger_event(811); stop |
| 5 | 811 | 8 / 2 | 4 | 150 | trigger_event(812); stop |
| 5 | 812 | 8 / 3 | 4 | 10 | set_switch(8); stop |
| 5 | 91 | 9 / 1 | 4 | 1 | trigger_event(911); stop |
| 5 | 911 | 9 / 2 | 5 | 10 | trigger_event(912); stop |
| 5 | 912 | 9 / 3 | 0 | 100 | set_switch(9); stop |
| 5 | 101 | 10 / 1 | 1 | 45 | set_switch(5); set_switch(6); set_switch(10); stop |
| 17 | 201 | 20 / 4 | 4 | 1 | stop |
| 17 | 301 | 30 / 1 | 1 | 60 | set_switch(10); stop |
| 17 | 303 | 30 / 2 | 3 | 60 | set_switch(10); stop |
| 17 | 302 | 30 / 3 | 1 | 1 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
