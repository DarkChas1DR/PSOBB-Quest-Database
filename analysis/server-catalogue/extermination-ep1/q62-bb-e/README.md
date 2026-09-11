# Slime Anarchy — extermination-ep1/q62-bb-e

Episode1; header quest ID 62; language E. Static scan: **584 objects, 474 enemy/NPC records, 134 events, 88 script labels.** Script roundtrip: alignment-only.

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
| 0 | 33 | 23 | 0 |
| 3 | 172 | 186 | 47 |
| 4 | 166 | 164 | 46 |
| 5 | 197 | 100 | 40 |
| 12 | 16 | 1 | 1 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 3 | 101 | 10 / 1 | 1 | 20 | trigger_event(1011); stop |
| 3 | 1011 | 10 / 2 | 3 | 20 | trigger_event(1012); stop |
| 3 | 1012 | 10 / 3 | 3 | 20 | set_switch(8); set_switch(4); stop |
| 3 | 102 | 10 / 4 | 3 | 20 | trigger_event(1021); stop |
| 3 | 1021 | 10 / 5 | 3 | 20 | trigger_event(1022); stop |
| 3 | 1022 | 10 / 6 | 3 | 20 | set_switch(8); stop |
| 3 | 401 | 40 / 1 | 4 | 20 | trigger_event(4011); stop |
| 3 | 4011 | 40 / 2 | 3 | 20 | set_switch(2); stop |
| 3 | 402 | 40 / 3 | 3 | 20 | trigger_event(4021); stop |
| 3 | 4021 | 40 / 4 | 3 | 20 | trigger_event(4022); stop |
| 3 | 4022 | 40 / 5 | 4 | 20 | set_switch(5); set_switch(10); stop |
| 3 | 341 | 34 / 1 | 5 | 20 | trigger_event(3411); stop |
| 3 | 3411 | 34 / 2 | 5 | 20 | trigger_event(3412); stop |
| 3 | 3412 | 34 / 3 | 4 | 20 | set_switch(218); set_switch(1); set_switch(3); set_switch(7); stop |
| 3 | 121 | 12 / 1 | 6 | 20 | trigger_event(1211); stop |
| 3 | 1211 | 12 / 2 | 3 | 20 | trigger_event(1212); stop |
| 3 | 1212 | 12 / 3 | 6 | 20 | set_switch(6); stop |
| 3 | 501 | 50 / 1 | 6 | 20 | trigger_event(5011); stop |
| 3 | 5011 | 50 / 2 | 6 | 20 | trigger_event(5012); stop |
| 3 | 5012 | 50 / 3 | 6 | 20 | trigger_event(5013); stop |
| 3 | 5013 | 50 / 4 | 6 | 20 | set_switch(11); set_switch(12); set_switch(16); set_switch(13); set_switch(14); stop |
| 3 | 301 | 30 / 1 | 5 | 20 | trigger_event(3011); stop |
| 3 | 3011 | 30 / 2 | 4 | 20 | trigger_event(3012); stop |
| 3 | 3012 | 30 / 3 | 6 | 20 | set_switch(15); stop |
| 3 | 601 | 60 / 1 | 3 | 20 | trigger_event(6011); stop |
| 3 | 6011 | 60 / 2 | 3 | 20 | trigger_event(6012); stop |
| 3 | 6012 | 60 / 3 | 3 | 20 | trigger_event(6013); stop |
| 3 | 6013 | 60 / 4 | 3 | 20 | set_switch(17); set_switch(18); set_switch(19); set_switch(20); set_switch(21); stop |
| 3 | 311 | 31 / 1 | 4 | 20 | trigger_event(3111); stop |
| 3 | 3111 | 31 / 2 | 4 | 20 | trigger_event(3112); stop |
| 3 | 3112 | 31 / 3 | 4 | 20 | set_switch(21); set_switch(23); set_switch(24); set_switch(22); stop |
| 3 | 201 | 20 / 1 | 4 | 20 | stop |
| 3 | 511 | 51 / 1 | 2 | 20 | trigger_event(5111); stop |
| 3 | 5111 | 51 / 2 | 2 | 20 | trigger_event(5112); stop |
| 3 | 5112 | 51 / 3 | 1 | 20 | set_switch(26); stop |
| 3 | 512 | 51 / 4 | 4 | 20 | trigger_event(5121); stop |
| 3 | 5121 | 51 / 5 | 3 | 20 | trigger_event(5122); stop |
| 3 | 5122 | 51 / 6 | 3 | 20 | stop |
| 3 | 321 | 32 / 1 | 5 | 20 | trigger_event(3211); stop |
| 3 | 3211 | 32 / 2 | 5 | 20 | set_switch(20); set_switch(35); set_switch(28); set_switch(27); stop |
| 3 | 522 | 52 / 1 | 4 | 20 | trigger_event(5211); stop |
| 3 | 5211 | 52 / 2 | 6 | 20 | trigger_event(5212); stop |
| 3 | 5212 | 52 / 3 | 4 | 20 | trigger_event(5213); stop |
| 3 | 5213 | 52 / 4 | 6 | 20 | set_switch(232); set_switch(30); set_switch(31); set_switch(32); stop |
| 3 | 331 | 33 / 1 | 4 | 20 | trigger_event(3311); stop |
| 3 | 3311 | 33 / 2 | 3 | 20 | trigger_event(3312); stop |
| 3 | 3312 | 33 / 3 | 5 | 20 | set_switch(231); set_switch(33); set_switch(34); stop |
| 4 | 221 | 22 / 1 | 5 | 20 | trigger_event(2211); stop |
| 4 | 2211 | 22 / 2 | 6 | 20 | set_switch(235); set_switch(7); set_switch(4); set_switch(5); set_switch(9); set_switch(6); set_switch(3); stop |
| 4 | 161 | 16 / 1 | 3 | 20 | trigger_event(1611); stop |
| 4 | 1611 | 16 / 2 | 4 | 20 | trigger_event(1612); stop |
| 4 | 1612 | 16 / 3 | 3 | 20 | stop |
| 4 | 162 | 16 / 4 | 2 | 20 | trigger_event(1621); stop |
| 4 | 1621 | 16 / 5 | 3 | 20 | trigger_event(1622); stop |
| 4 | 1622 | 16 / 6 | 2 | 20 | set_switch(10); stop |
| 4 | 201 | 20 / 1 | 2 | 20 | trigger_event(2011); stop |
| 4 | 2011 | 20 / 2 | 3 | 20 | trigger_event(2012); stop |
| 4 | 2012 | 20 / 3 | 3 | 20 | stop |
| 4 | 202 | 20 / 4 | 3 | 20 | trigger_event(2021); stop |
| 4 | 2021 | 20 / 5 | 3 | 20 | trigger_event(2022); stop |
| 4 | 2022 | 20 / 6 | 2 | 20 | set_switch(2); stop |
| 4 | 151 | 15 / 1 | 5 | 20 | set_switch(1); stop |
| 4 | 211 | 21 / 1 | 5 | 20 | trigger_event(2111); stop |
| 4 | 2111 | 21 / 2 | 2 | 20 | trigger_event(2112); stop |
| 4 | 2112 | 21 / 3 | 5 | 20 | set_switch(11); stop |
| 4 | 111 | 11 / 1 | 3 | 20 | set_switch(12); set_switch(14); stop |
| 4 | 112 | 11 / 2 | 3 | 20 | stop |
| 4 | 601 | 60 / 1 | 2 | 20 | stop |
| 4 | 602 | 60 / 2 | 5 | 20 | trigger_event(6011); stop |
| 4 | 6011 | 60 / 3 | 2 | 20 | trigger_event(6012); stop |
| 4 | 6012 | 60 / 4 | 5 | 20 | set_switch(15); set_switch(16); set_switch(18); set_switch(21); set_switch(22); set_switch(35); stop |
| 4 | 453 | 45 / 1 | 6 | 20 | trigger_event(4511); stop |
| 4 | 4511 | 45 / 2 | 4 | 20 | trigger_event(4512); stop |
| 4 | 4512 | 45 / 3 | 3 | 20 | set_switch(17); set_switch(219); stop |
| 4 | 131 | 13 / 1 | 2 | 20 | trigger_event(1311); stop |
| 4 | 1311 | 13 / 2 | 4 | 20 | set_switch(19); set_switch(20); stop |
| 4 | 401 | 40 / 1 | 5 | 20 | trigger_event(4011); stop |
| 4 | 4011 | 40 / 2 | 3 | 20 | set_switch(23); set_switch(24); set_switch(25); stop |
| 4 | 351 | 35 / 1 | 2 | 20 | trigger_event(3511); stop |
| 4 | 352 | 35 / 2 | 4 | 20 | trigger_event(3512); stop |
| 4 | 3512 | 35 / 3 | 4 | 20 | trigger_event(3513); stop |
| 4 | 3513 | 35 / 4 | 4 | 20 | set_switch(29); set_switch(26); set_switch(28); stop |
| 4 | 122 | 12 / 1 | 7 | 20 | trigger_event(1211); stop |
| 4 | 1211 | 12 / 2 | 7 | 20 | stop |
| 4 | 301 | 30 / 1 | 4 | 20 | trigger_event(3011); stop |
| 4 | 3011 | 30 / 2 | 2 | 20 | trigger_event(3012); stop |
| 4 | 3012 | 30 / 3 | 3 | 20 | set_switch(30); set_switch(31); set_switch(27); set_switch(32); set_switch(33); stop |
| 4 | 302 | 30 / 4 | 4 | 20 | stop |
| 4 | 141 | 14 / 1 | 4 | 20 | trigger_event(1411); stop |
| 4 | 1411 | 14 / 2 | 3 | 20 | trigger_event(1412); stop |
| 4 | 1412 | 14 / 3 | 2 | 20 | trigger_event(1413); stop |
| 4 | 1413 | 14 / 4 | 4 | 20 | trigger_event(1414); stop |
| 4 | 1414 | 14 / 5 | 2 | 20 | set_switch(34); stop |
| 5 | 301 | 30 / 1 | 1 | 10 | stop |
| 5 | 302 | 30 / 2 | 1 | 10 | trigger_event(3021); stop |
| 5 | 3021 | 30 / 3 | 3 | 10 | trigger_event(3022); stop |
| 5 | 3022 | 30 / 4 | 2 | 10 | stop |
| 5 | 303 | 30 / 5 | 4 | 10 | trigger_event(3031); stop |
| 5 | 3031 | 30 / 6 | 3 | 10 | trigger_event(3032); stop |
| 5 | 3032 | 30 / 7 | 2 | 10 | set_switch(235); set_switch(4); set_switch(1); set_switch(5); set_switch(7); set_switch(8); set_switch(26); set_switch(32); set_switch(29); set_switch(27); set_switch(28); stop |
| 5 | 221 | 22 / 1 | 6 | 10 | trigger_event(2211); stop |
| 5 | 2211 | 22 / 2 | 3 | 10 | trigger_event(2212); stop |
| 5 | 2212 | 22 / 3 | 5 | 10 | trigger_event(2213); stop |
| 5 | 2213 | 22 / 4 | 6 | 10 | set_switch(38); set_switch(33); stop |
| 5 | 601 | 60 / 1 | 0 | 10 | trigger_event(6011); stop |
| 5 | 6011 | 60 / 2 | 0 | 10 | trigger_event(6012); stop |
| 5 | 6012 | 60 / 3 | 0 | 10 | set_switch(35); stop |
| 5 | 701 | 70 / 1 | 5 | 10 | trigger_event(7011); stop |
| 5 | 7011 | 70 / 2 | 5 | 10 | trigger_event(7012); stop |
| 5 | 7012 | 70 / 3 | 6 | 240 | trigger_event(7013); stop |
| 5 | 7013 | 70 / 4 | 6 | 10 | set_switch(36); set_switch(37); stop |
| 5 | 331 | 33 / 1 | 2 | 10 | trigger_event(3311); stop |
| 5 | 3311 | 33 / 2 | 2 | 10 | trigger_event(3312); stop |
| 5 | 3312 | 33 / 3 | 2 | 10 | set_switch(29); set_switch(30); stop |
| 5 | 201 | 20 / 1 | 1 | 10 | trigger_event(2011); stop |
| 5 | 2011 | 20 / 2 | 1 | 40 | trigger_event(2012); stop |
| 5 | 2012 | 20 / 3 | 1 | 10 | set_switch(30); set_switch(31); set_switch(22); set_switch(15); stop |
| 5 | 511 | 51 / 1 | 3 | 10 | trigger_event(5111); stop |
| 5 | 5111 | 51 / 2 | 2 | 10 | trigger_event(5112); stop |
| 5 | 5112 | 51 / 3 | 3 | 10 | trigger_event(5113); stop |
| 5 | 5113 | 51 / 4 | 1 | 10 | set_switch(23); set_switch(24); set_switch(25); stop |
| 5 | 211 | 21 / 1 | 2 | 10 | trigger_event(2111); stop |
| 5 | 2111 | 21 / 2 | 3 | 10 | set_switch(7); set_switch(8); set_switch(9); set_switch(10); stop |
| 5 | 321 | 32 / 1 | 2 | 10 | set_switch(11); set_switch(12); set_switch(13); stop |
| 5 | 322 | 32 / 2 | 2 | 10 | trigger_event(3211); stop |
| 5 | 3211 | 32 / 3 | 2 | 10 | set_switch(22); stop |
| 5 | 711 | 71 / 1 | 4 | 10 | trigger_event(7111); stop |
| 5 | 7111 | 71 / 2 | 2 | 10 | trigger_event(7112); stop |
| 5 | 7112 | 71 / 3 | 2 | 10 | trigger_event(7113); stop |
| 5 | 7113 | 71 / 4 | 2 | 360 | set_switch(19); set_switch(20); stop |
| 5 | 231 | 23 / 1 | 1 | 10 | trigger_event(2311); stop |
| 5 | 2311 | 23 / 2 | 1 | 10 | trigger_event(2312); stop |
| 5 | 2312 | 23 / 3 | 1 | 10 | set_switch(21); stop |
| 12 | 1 | 1 / 1 | 1 | 50 | construct_objects(room=1,group_or_wave=1); stop |

## Review notes

- Floor 4: event 351 targets absent event 3511
