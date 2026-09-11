# ガロンの野望 — retrieval-ep1/q138-bb-j

Episode1; header quest ID 138; language J. Static scan: **743 objects, 137 enemy/NPC records, 45 events, 920 script labels.** Script roundtrip: byte-identical.

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
0x05, 0x05, 0x00, 0x01, 0x00
0x09, 0x09, 0x00, 0x02, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 21 | 0 |
| 5 | 371 | 78 | 33 |
| 9 | 346 | 38 | 12 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 5 | 211 | 21 / 1 | 1 | 0 | stop |
| 5 | 311 | 31 / 1 | 1 | 30 | stop |
| 5 | 321 | 32 / 1 | 2 | 0 | trigger_event(3211); stop |
| 5 | 3211 | 32 / 2 | 2 | 0 | trigger_event(3212); stop |
| 5 | 3212 | 32 / 3 | 2 | 120 | trigger_event(3213); stop |
| 5 | 3213 | 32 / 4 | 2 | 0 | trigger_event(3214); stop |
| 5 | 3214 | 32 / 5 | 2 | 180 | trigger_event(3215); stop |
| 5 | 3215 | 32 / 6 | 2 | 60 | trigger_event(3216); stop |
| 5 | 3216 | 32 / 7 | 2 | 60 | trigger_event(3217); stop |
| 5 | 3217 | 32 / 8 | 2 | 0 | trigger_event(3218); stop |
| 5 | 3218 | 32 / 9 | 2 | 120 | stop |
| 5 | 511 | 51 / 1 | 4 | 30 | trigger_event(5111); stop |
| 5 | 5111 | 51 / 2 | 2 | 60 | trigger_event(5112); stop |
| 5 | 5112 | 51 / 3 | 3 | 60 | set_switch(173); stop |
| 5 | 512 | 51 / 4 | 2 | 120 | stop |
| 5 | 541 | 54 / 1 | 4 | 150 | trigger_event(5411); stop |
| 5 | 5411 | 54 / 2 | 4 | 90 | trigger_event(5412); stop |
| 5 | 5412 | 54 / 3 | 2 | 150 | trigger_event(5413); stop |
| 5 | 5413 | 54 / 4 | 4 | 180 | trigger_event(5414); stop |
| 5 | 5414 | 54 / 5 | 3 | 90 | trigger_event(5415); stop |
| 5 | 5415 | 54 / 6 | 4 | 120 | stop |
| 5 | 601 | 60 / 1 | 1 | 30 | trigger_event(6011); stop |
| 5 | 6011 | 60 / 2 | 1 | 0 | trigger_event(6012); set_switch(101); stop |
| 5 | 711 | 71 / 1 | 3 | 90 | trigger_event(7111); stop |
| 5 | 7111 | 71 / 2 | 1 | 90 | trigger_event(7112); stop |
| 5 | 7112 | 71 / 3 | 3 | 30 | trigger_event(7113); stop |
| 5 | 7113 | 71 / 4 | 3 | 0 | trigger_event(7114); stop |
| 5 | 7114 | 71 / 5 | 2 | 180 | trigger_event(7115); stop |
| 5 | 7115 | 71 / 6 | 4 | 90 | trigger_event(7116); stop |
| 5 | 7116 | 71 / 7 | 3 | 0 | trigger_event(7117); stop |
| 5 | 7117 | 71 / 8 | 1 | 120 | trigger_event(7118); stop |
| 5 | 7118 | 71 / 9 | 3 | 30 | trigger_event(7119); stop |
| 5 | 7119 | 71 / 10 | 1 | 180 | stop |
| 9 | 211 | 21 / 1 | 4 | 60 | trigger_event(2111); stop |
| 9 | 2111 | 21 / 2 | 4 | 30 | trigger_event(2112); stop |
| 9 | 2112 | 21 / 3 | 1 | 90 | set_switch(126); stop |
| 9 | 311 | 31 / 1 | 3 | 90 | trigger_event(3111); stop |
| 9 | 3111 | 31 / 2 | 4 | 30 | trigger_event(3112); stop |
| 9 | 3112 | 31 / 3 | 2 | 120 | set_switch(129); stop |
| 9 | 341 | 34 / 1 | 2 | 30 | stop |
| 9 | 421 | 42 / 1 | 3 | 30 | trigger_event(4211); stop |
| 9 | 4211 | 42 / 2 | 4 | 30 | trigger_event(4212); stop |
| 9 | 4212 | 42 / 3 | 4 | 30 | set_switch(136); stop |
| 9 | 501 | 50 / 1 | 4 | 30 | trigger_event(5011); stop |
| 9 | 5011 | 50 / 2 | 3 | 30 | set_switch(125); stop |

## Review notes

- Floor 5: event 6011 targets absent event 6012

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
