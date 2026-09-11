# Tian\'s Montreaux Final — events-ep2/q513-bb-e

Episode2; header quest ID 513; language E. Static scan: **705 objects, 330 enemy/NPC records, 76 events, 111 script labels.** Script roundtrip: byte-identical.

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
| 0 | 68 | 29 | 0 |
| 8 | 237 | 116 | 30 |
| 9 | 167 | 59 | 19 |
| 12 | 26 | 1 | 1 |
| 16 | 207 | 125 | 26 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 8 | 21 | 2 / 1 | 5 | 0 | trigger_event(22); stop |
| 8 | 22 | 2 / 2 | 5 | 70 | trigger_event(23); stop |
| 8 | 23 | 2 / 3 | 4 | 100 | set_switch(26); stop |
| 8 | 24 | 2 / 4 | 4 | 30 | trigger_event(25); stop |
| 8 | 25 | 2 / 5 | 7 | 70 | trigger_event(26); stop |
| 8 | 26 | 2 / 6 | 8 | 70 | stop |
| 8 | 27 | 2 / 7 | 2 | 0 | stop |
| 8 | 28 | 2 / 8 | 1 | 0 | stop |
| 8 | 31 | 3 / 1 | 1 | 100 | stop |
| 8 | 32 | 3 / 2 | 4 | 30 | trigger_event(33); stop |
| 8 | 33 | 3 / 3 | 6 | 70 | trigger_event(37); stop |
| 8 | 34 | 3 / 4 | 3 | 30 | trigger_event(35); stop |
| 8 | 35 | 3 / 5 | 3 | 70 | trigger_event(36); stop |
| 8 | 36 | 3 / 6 | 6 | 70 | set_switch(39); stop |
| 8 | 37 | 3 / 7 | 1 | 30 | stop |
| 8 | 81 | 8 / 1 | 4 | 30 | trigger_event(82); stop |
| 8 | 82 | 8 / 2 | 4 | 50 | trigger_event(83); stop |
| 8 | 83 | 8 / 3 | 5 | 70 | trigger_event(84); stop |
| 8 | 84 | 8 / 4 | 1 | 100 | set_switch(93); stop |
| 8 | 85 | 8 / 5 | 2 | 0 | stop |
| 8 | 86 | 8 / 6 | 1 | 0 | stop |
| 8 | 51 | 5 / 1 | 5 | 0 | trigger_event(52); stop |
| 8 | 52 | 5 / 2 | 10 | 30 | trigger_event(57); stop |
| 8 | 53 | 5 / 3 | 1 | 30 | trigger_event(57); stop |
| 8 | 54 | 5 / 4 | 7 | 30 | trigger_event(55); stop |
| 8 | 55 | 5 / 4 | 7 | 40 | trigger_event(58); stop |
| 8 | 56 | 5 / 6 | 1 | 40 | trigger_event(59); stop |
| 8 | 57 | 5 / 7 | 2 | 30 | trigger_event(53); stop |
| 8 | 58 | 5 / 8 | 8 | 30 | trigger_event(56); stop |
| 8 | 59 | 5 / 9 | 1 | 30 | set_switch(216); stop |
| 9 | 91 | 9 / 1 | 1 | 50 | trigger_event(92); stop |
| 9 | 92 | 9 / 2 | 2 | 30 | set_switch(83); stop |
| 9 | 111 | 11 / 1 | 1 | 90 | trigger_event(112); stop |
| 9 | 112 | 11 / 2 | 6 | 30 | trigger_event(113); stop |
| 9 | 113 | 11 / 3 | 7 | 40 | set_switch(44); stop |
| 9 | 93 | 9 / 3 | 4 | 50 | trigger_event(94); stop |
| 9 | 94 | 9 / 4 | 2 | 30 | stop |
| 9 | 71 | 7 / 1 | 5 | 0 | stop |
| 9 | 72 | 7 / 2 | 1 | 30 | stop |
| 9 | 31 | 3 / 1 | 3 | 30 | trigger_event(32); stop |
| 9 | 32 | 3 / 2 | 3 | 30 | stop |
| 9 | 33 | 3 / 3 | 5 | 30 | trigger_event(34); stop |
| 9 | 34 | 3 / 4 | 8 | 50 | trigger_event(35); stop |
| 9 | 35 | 3 / 5 | 3 | 100 | stop |
| 9 | 36 | 3 / 6 | 1 | 0 | stop |
| 9 | 37 | 3 / 7 | 3 | 0 | stop |
| 9 | 38 | 3 / 8 | 1 | 30 | stop |
| 9 | 73 | 7 / 3 | 1 | 20 | stop |
| 9 | 131 | 13 / 1 | 2 | 30 | stop |
| 12 | 1 | 1 / 1 | 1 | 50 | construct_objects(room=1,group_or_wave=1); stop |
| 16 | 91 | 9 / 1 | 8 | 0 | trigger_event(92); stop |
| 16 | 92 | 9 / 2 | 11 | 150 | trigger_event(93); stop |
| 16 | 93 | 9 / 3 | 7 | 70 | stop |
| 16 | 94 | 9 / 4 | 4 | 0 | stop |
| 16 | 95 | 9 / 5 | 5 | 0 | trigger_event(96); stop |
| 16 | 96 | 9 / 6 | 2 | 100 | stop |
| 16 | 97 | 9 / 7 | 2 | 50 | stop |
| 16 | 111 | 11 / 1 | 6 | 0 | trigger_event(113); stop |
| 16 | 112 | 11 / 2 | 3 | 300 | stop |
| 16 | 113 | 11 / 3 | 2 | 100 | stop |
| 16 | 114 | 11 / 4 | 3 | 0 | stop |
| 16 | 71 | 7 / 1 | 4 | 50 | trigger_event(72); construct_objects(room=7,group_or_wave=1); stop |
| 16 | 72 | 7 / 2 | 6 | 100 | stop |
| 16 | 73 | 7 / 3 | 4 | 30 | trigger_event(74); stop |
| 16 | 74 | 7 / 4 | 9 | 70 | stop |
| 16 | 75 | 7 / 5 | 6 | 0 | stop |
| 16 | 31 | 3 / 1 | 5 | 0 | trigger_event(35); stop |
| 16 | 32 | 3 / 2 | 1 | 100 | trigger_event(36); stop |
| 16 | 33 | 3 / 3 | 3 | 700 | trigger_event(39); stop |
| 16 | 34 | 3 / 4 | 3 | 700 | trigger_event(37); stop |
| 16 | 35 | 3 / 5 | 6 | 120 | stop |
| 16 | 36 | 3 / 6 | 3 | 50 | stop |
| 16 | 37 | 3 / 7 | 8 | 80 | trigger_event(38); stop |
| 16 | 38 | 3 / 8 | 5 | 50 | stop |
| 16 | 39 | 3 / 9 | 5 | 80 | trigger_event(310); stop |
| 16 | 310 | 3 / 10 | 4 | 100 | set_switch(85); set_switch(5); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

A backup is present; decompressed content identical: False. See [text differences](<backup-diff.txt>).

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
