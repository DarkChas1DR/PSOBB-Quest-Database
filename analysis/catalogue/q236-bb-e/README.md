# Phantasmal World #4 — q236-bb-e

Episode2; header quest ID 236; language E. Static scan: **526 objects, 262 enemy/NPC records, 100 events, 897 script labels.** Script roundtrip: byte-identical.

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
0x11, 0x23, 0x00, 0x00, 0x00
0x10, 0x23, 0x00, 0x01, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 44 | 20 | 0 |
| 16 | 230 | 139 | 58 |
| 17 | 252 | 103 | 42 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 17 | 11 | 1 / 1 | 1 | 60 | trigger_event(111); stop |
| 17 | 111 | 1 / 2 | 2 | 120 | trigger_event(112); stop |
| 17 | 112 | 1 / 3 | 1 | 30 | trigger_event(113); stop |
| 17 | 113 | 1 / 4 | 1 | 30 | set_switch(1); stop |
| 17 | 21 | 2 / 1 | 2 | 60 | trigger_event(215); stop |
| 17 | 215 | 2 / 2 | 3 | 30 | set_switch(2); stop |
| 17 | 201 | 20 / 1 | 7 | 30 | set_switch(3); stop |
| 17 | 101 | 10 / 1 | 4 | 60 | trigger_event(1011); stop |
| 17 | 1011 | 10 / 2 | 2 | 30 | trigger_event(1012); stop |
| 17 | 1012 | 10 / 3 | 3 | 60 | set_switch(4); stop |
| 17 | 31 | 3 / 1 | 2 | 60 | trigger_event(311); stop |
| 17 | 311 | 3 / 2 | 4 | 30 | trigger_event(312); stop |
| 17 | 312 | 3 / 3 | 3 | 150 | set_switch(5); stop |
| 17 | 41 | 4 / 1 | 3 | 30 | stop |
| 17 | 42 | 4 / 2 | 2 | 30 | set_switch(6); stop |
| 17 | 211 | 21 / 1 | 4 | 30 | trigger_event(2111); stop |
| 17 | 2111 | 21 / 2 | 4 | 90 | set_switch(7); stop |
| 17 | 51 | 5 / 1 | 1 | 45 | construct_objects(room=5,group_or_wave=1); stop |
| 17 | 52 | 5 / 2 | 2 | 60 | construct_objects(room=5,group_or_wave=2); stop |
| 17 | 53 | 5 / 3 | 2 | 90 | construct_objects(room=5,group_or_wave=3); set_switch(8); stop |
| 17 | 221 | 22 / 1 | 4 | 30 | trigger_event(2211); stop |
| 17 | 2211 | 22 / 2 | 2 | 30 | set_switch(9); stop |
| 17 | 301 | 30 / 1 | 4 | 30 | trigger_event(3011); stop |
| 17 | 3011 | 30 / 2 | 2 | 150 | trigger_event(3012); stop |
| 17 | 3012 | 30 / 3 | 1 | 30 | trigger_event(3013); stop |
| 17 | 3013 | 30 / 4 | 2 | 120 | trigger_event(3014); stop |
| 17 | 3014 | 30 / 5 | 2 | 90 | trigger_event(3015); stop |
| 17 | 3015 | 30 / 6 | 2 | 60 | trigger_event(3016); stop |
| 17 | 3016 | 30 / 7 | 1 | 120 | trigger_event(3017); stop |
| 17 | 3017 | 30 / 8 | 2 | 30 | set_switch(100); stop |
| 17 | 302 | 30 / 9 | 3 | 60 | trigger_event(3021); stop |
| 17 | 3021 | 30 / 10 | 1 | 120 | trigger_event(3022); stop |
| 17 | 3022 | 30 / 11 | 2 | 150 | trigger_event(3023); stop |
| 17 | 3023 | 30 / 12 | 1 | 90 | trigger_event(3024); stop |
| 17 | 3024 | 30 / 13 | 2 | 120 | trigger_event(3025); stop |
| 17 | 3025 | 30 / 14 | 2 | 30 | trigger_event(3026); stop |
| 17 | 3026 | 30 / 15 | 2 | 90 | trigger_event(3027); stop |
| 17 | 3027 | 30 / 16 | 1 | 30 | set_switch(101); stop |
| 17 | 303 | 30 / 17 | 1 | 120 | trigger_event(3031); stop |
| 17 | 3031 | 30 / 18 | 5 | 60 | trigger_event(3032); stop |
| 17 | 3032 | 30 / 19 | 5 | 30 | trigger_event(3033); stop |
| 17 | 3033 | 30 / 20 | 3 | 150 | set_switch(120); stop |
| 16 | 11 | 1 / 1 | 2 | 60 | trigger_event(111); stop |
| 16 | 111 | 1 / 2 | 3 | 60 | set_switch(1); stop |
| 16 | 21 | 2 / 1 | 7 | 30 | set_switch(2); stop |
| 16 | 201 | 20 / 1 | 2 | 30 | trigger_event(2011); stop |
| 16 | 2011 | 20 / 2 | 2 | 30 | set_switch(3); stop |
| 16 | 202 | 20 / 3 | 1 | 15 | stop |
| 16 | 203 | 20 / 4 | 2 | 15 | stop |
| 16 | 101 | 10 / 1 | 5 | 60 | trigger_event(1011); stop |
| 16 | 1011 | 10 / 2 | 3 | 30 | trigger_event(1012); stop |
| 16 | 1012 | 10 / 3 | 3 | 30 | trigger_event(1013); stop |
| 16 | 1013 | 10 / 4 | 2 | 60 | set_switch(4); stop |
| 16 | 33 | 3 / 1 | 4 | 60 | trigger_event(331); stop |
| 16 | 331 | 3 / 2 | 3 | 30 | trigger_event(332); stop |
| 16 | 332 | 3 / 3 | 3 | 150 | set_switch(5); stop |
| 16 | 41 | 4 / 1 | 6 | 30 | trigger_event(411); stop |
| 16 | 411 | 4 / 2 | 4 | 30 | set_switch(6); stop |
| 16 | 211 | 21 / 1 | 2 | 30 | trigger_event(2111); stop |
| 16 | 2111 | 21 / 2 | 2 | 30 | trigger_event(2112); stop |
| 16 | 2112 | 21 / 3 | 4 | 30 | set_switch(7); stop |
| 16 | 51 | 5 / 1 | 2 | 60 | trigger_event(511); stop |
| 16 | 511 | 5 / 2 | 2 | 60 | trigger_event(512); stop |
| 16 | 512 | 5 / 3 | 4 | 60 | trigger_event(513); stop |
| 16 | 513 | 5 / 4 | 4 | 60 | set_switch(8); construct_objects(room=5,group_or_wave=6); stop |
| 16 | 52 | 5 / 5 | 1 | 30 | stop |
| 16 | 221 | 22 / 1 | 1 | 90 | trigger_event(2211); stop |
| 16 | 2211 | 22 / 2 | 1 | 120 | trigger_event(2212); stop |
| 16 | 2212 | 22 / 3 | 1 | 120 | trigger_event(2213); stop |
| 16 | 2213 | 22 / 4 | 4 | 30 | set_switch(9); stop |
| 16 | 301 | 30 / 1 | 2 | 30 | trigger_event(3011); stop |
| 16 | 3011 | 30 / 2 | 1 | 150 | trigger_event(3012); stop |
| 16 | 3012 | 30 / 3 | 2 | 30 | trigger_event(3013); stop |
| 16 | 3013 | 30 / 4 | 2 | 120 | trigger_event(3014); stop |
| 16 | 3014 | 30 / 5 | 1 | 90 | trigger_event(3015); stop |
| 16 | 3015 | 30 / 6 | 1 | 60 | trigger_event(3016); stop |
| 16 | 3016 | 30 / 7 | 1 | 120 | trigger_event(3017); stop |
| 16 | 3017 | 30 / 8 | 2 | 30 | trigger_event(3018); stop |
| 16 | 3018 | 30 / 9 | 1 | 30 | trigger_event(3019); stop |
| 16 | 3019 | 30 / 10 | 1 | 30 | trigger_event(30111); stop |
| 16 | 30111 | 30 / 11 | 1 | 30 | trigger_event(30112); stop |
| 16 | 30112 | 30 / 12 | 2 | 30 | set_switch(100); stop |
| 16 | 302 | 30 / 13 | 2 | 60 | trigger_event(3021); stop |
| 16 | 3021 | 30 / 14 | 1 | 120 | trigger_event(3022); stop |
| 16 | 3022 | 30 / 15 | 1 | 150 | trigger_event(3023); stop |
| 16 | 3023 | 30 / 16 | 1 | 90 | trigger_event(3024); stop |
| 16 | 3024 | 30 / 17 | 1 | 120 | trigger_event(3025); stop |
| 16 | 3025 | 30 / 18 | 1 | 30 | trigger_event(3026); stop |
| 16 | 3026 | 30 / 19 | 2 | 90 | trigger_event(3027); stop |
| 16 | 3027 | 30 / 20 | 1 | 30 | trigger_event(3028); stop |
| 16 | 3028 | 30 / 21 | 1 | 30 | trigger_event(3029); stop |
| 16 | 3029 | 30 / 22 | 2 | 30 | trigger_event(30211); stop |
| 16 | 30211 | 30 / 23 | 1 | 30 | trigger_event(30212); stop |
| 16 | 30212 | 30 / 24 | 2 | 30 | set_switch(101); stop |
| 16 | 303 | 30 / 25 | 4 | 120 | trigger_event(3031); stop |
| 16 | 3031 | 30 / 26 | 4 | 60 | trigger_event(3032); stop |
| 16 | 3032 | 30 / 27 | 3 | 30 | trigger_event(3033); stop |
| 16 | 3033 | 30 / 28 | 3 | 150 | trigger_event(3034); stop |
| 16 | 3034 | 30 / 29 | 4 | 30 | trigger_event(3035); stop |
| 16 | 3035 | 30 / 30 | 8 | 150 | set_switch(120); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
