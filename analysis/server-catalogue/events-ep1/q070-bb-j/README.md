# ＰＳＯファミ通ＣＵＰｖｅｒ.２ — events-ep1/q070-bb-j

Episode1; header quest ID 70; language J. Static scan: **807 objects, 277 enemy/NPC records, 74 events, 560 script labels.** Script roundtrip: differs.

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
0x01, 0x01, 0x00, 0x00, 0x04
0x04, 0x04, 0x00, 0x01, 0x01
0x06, 0x06, 0x00, 0x02, 0x00
0x09, 0x09, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 52 | 13 | 0 |
| 1 | 134 | 15 | 1 |
| 4 | 193 | 98 | 31 |
| 6 | 234 | 34 | 16 |
| 9 | 194 | 117 | 26 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 51 | 5 / 1 | 15 | 1 | stop |
| 4 | 202 | 20 / 1 | 1 | 20 | stop |
| 4 | 203 | 20 / 2 | 1 | 20 | stop |
| 4 | 204 | 20 / 3 | 1 | 20 | stop |
| 4 | 205 | 20 / 4 | 1 | 20 | set_switch(11); stop |
| 4 | 206 | 20 / 5 | 1 | 20 | stop |
| 4 | 211 | 21 / 1 | 4 | 20 | trigger_event(2111); stop |
| 4 | 2111 | 21 / 2 | 4 | 20 | trigger_event(2112); stop |
| 4 | 2112 | 21 / 3 | 4 | 20 | set_switch(15); stop |
| 4 | 451 | 45 / 1 | 2 | 20 | trigger_event(4511); stop |
| 4 | 4511 | 45 / 2 | 2 | 20 | trigger_event(4512); stop |
| 4 | 4512 | 45 / 3 | 4 | 20 | trigger_event(4513); stop |
| 4 | 4513 | 45 / 4 | 2 | 20 | trigger_event(4514); stop |
| 4 | 4514 | 45 / 5 | 2 | 20 | stop |
| 4 | 452 | 45 / 6 | 3 | 20 | set_switch(19); stop |
| 4 | 301 | 30 / 1 | 1 | 20 | set_switch(203); stop |
| 4 | 302 | 30 / 2 | 1 | 20 | set_switch(204); stop |
| 4 | 303 | 30 / 3 | 1 | 20 | set_switch(205); stop |
| 4 | 304 | 30 / 4 | 1 | 20 | set_switch(206); stop |
| 4 | 141 | 14 / 1 | 6 | 20 | stop |
| 4 | 351 | 35 / 1 | 5 | 20 | trigger_event(3511); stop |
| 4 | 3511 | 35 / 2 | 4 | 20 | trigger_event(3512); stop |
| 4 | 3512 | 35 / 3 | 3 | 20 | trigger_event(3513); stop |
| 4 | 3513 | 35 / 4 | 5 | 20 | trigger_event(3514); stop |
| 4 | 3514 | 35 / 5 | 2 | 20 | trigger_event(3515); stop |
| 4 | 3515 | 35 / 6 | 8 | 20 | trigger_event(3516); stop |
| 4 | 3516 | 35 / 7 | 5 | 20 | trigger_event(3517); stop |
| 4 | 3517 | 35 / 8 | 5 | 20 | trigger_event(3518); stop |
| 4 | 3518 | 35 / 9 | 4 | 20 | trigger_event(3519); stop |
| 4 | 3519 | 35 / 10 | 8 | 20 | trigger_event(3590); stop |
| 4 | 3590 | 35 / 11 | 4 | 20 | set_switch(30); stop |
| 4 | 601 | 60 / 1 | 3 | 20 | stop |
| 6 | 301 | 30 / 1 | 2 | 60 | set_switch(16); set_switch(17); stop |
| 6 | 411 | 41 / 1 | 1 | 1 | set_switch(24); stop |
| 6 | 511 | 51 / 1 | 4 | 1 | trigger_event(5111); stop |
| 6 | 5111 | 51 / 2 | 4 | 60 | set_switch(12); set_switch(13); set_switch(14); set_switch(15); stop |
| 6 | 521 | 52 / 1 | 3 | 1 | trigger_event(5211); stop |
| 6 | 5211 | 52 / 2 | 3 | 60 | trigger_event(5212); stop |
| 6 | 5212 | 52 / 3 | 1 | 60 | set_switch(18); set_switch(19); set_switch(20); set_switch(21); set_switch(23); stop |
| 6 | 522 | 52 / 4 | 2 | 1 | trigger_event(5221); stop |
| 6 | 5221 | 52 / 5 | 2 | 60 | stop |
| 6 | 531 | 53 / 1 | 1 | 61 | trigger_event(5311); stop |
| 6 | 5311 | 53 / 2 | 3 | 90 | set_switch(22); set_switch(25); set_switch(26); set_switch(27); set_switch(30); set_switch(31); stop |
| 6 | 601 | 60 / 1 | 4 | 1 | trigger_event(6011); stop |
| 6 | 6011 | 60 / 2 | 4 | 60 | set_switch(4); set_switch(6); set_switch(7); set_switch(8); set_switch(9); set_switch(11); stop |
| 6 | 611 | 61 / 1 | 0 | 1 | trigger_event(6111); stop |
| 6 | 6111 | 61 / 2 | 0 | 45 | trigger_event(6112); stop |
| 6 | 6112 | 61 / 3 | 0 | 45 | trigger_event(6113); stop |
| 9 | 201 | 20 / 1 | 2 | 30 | set_switch(37); set_switch(38); stop |
| 9 | 211 | 21 / 1 | 6 | 10 | set_switch(7); set_switch(8); set_switch(35); set_switch(36); stop |
| 9 | 212 | 21 / 2 | 3 | 60 | stop |
| 9 | 231 | 23 / 1 | 6 | 1 | trigger_event(2311); stop |
| 9 | 2311 | 23 / 2 | 5 | 1 | trigger_event(2312); stop |
| 9 | 2312 | 23 / 3 | 4 | 1 | set_switch(17); set_switch(18); set_switch(19); set_switch(20); set_switch(21); set_switch(22); stop |
| 9 | 241 | 24 / 1 | 5 | 1 | trigger_event(2411); stop |
| 9 | 2411 | 24 / 2 | 4 | 1 | set_switch(23); set_switch(24); set_switch(25); set_switch(26); set_switch(39); set_switch(40); stop |
| 9 | 301 | 30 / 1 | 6 | 30 | set_switch(31); set_switch(32); stop |
| 9 | 311 | 31 / 1 | 2 | 30 | trigger_event(3111); stop |
| 9 | 3111 | 31 / 2 | 5 | 60 | set_switch(11); set_switch(12); set_switch(13); set_switch(14); set_switch(15); set_switch(16); set_switch(33); set_switch(34); stop |
| 9 | 312 | 31 / 3 | 5 | 120 | stop |
| 9 | 331 | 33 / 1 | 5 | 30 | trigger_event(3311); stop |
| 9 | 3311 | 33 / 2 | 3 | 60 | set_switch(43); set_switch(44); stop |
| 9 | 401 | 40 / 1 | 4 | 1 | trigger_event(4011); stop |
| 9 | 4011 | 40 / 2 | 4 | 30 | set_switch(5); set_switch(6); set_switch(9); set_switch(10); stop |
| 9 | 411 | 41 / 1 | 2 | 30 | trigger_event(4111); stop |
| 9 | 4111 | 41 / 2 | 1 | 60 | set_switch(3); set_switch(4); set_switch(27); set_switch(28); set_switch(29); set_switch(30); stop |
| 9 | 421 | 42 / 1 | 4 | 1 | stop |
| 9 | 441 | 44 / 1 | 6 | 1 | trigger_event(4411); stop |
| 9 | 4411 | 44 / 2 | 5 | 30 | set_switch(59); set_switch(60); set_switch(61); set_switch(62); set_switch(63); set_switch(64); stop |
| 9 | 601 | 60 / 1 | 5 | 1 | set_switch(53); set_switch(54); set_switch(55); set_switch(56); set_switch(57); set_switch(58); stop |
| 9 | 801 | 80 / 1 | 7 | 30 | trigger_event(8011); stop |
| 9 | 8011 | 80 / 2 | 6 | 60 | trigger_event(8012); stop |
| 9 | 8012 | 80 / 3 | 9 | 1 | trigger_event(8013); stop |
| 9 | 8013 | 80 / 4 | 3 | 15 | set_switch(41); set_switch(42); set_switch(43); set_switch(44); set_switch(45); set_switch(46); set_switch(47); set_switch(48); set_switch(49); set_switch(50); set_switch(51); set_switch(52); stop |

## Review notes

- Floor 6: event 6112 targets absent event 6113
- Reassembled bytes differ beyond recognized alignment; inspect before rebuilding

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
