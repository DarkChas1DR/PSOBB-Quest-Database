# 掃討作戦 第四号 — extermination-ep1/q104-bb-j

Episode1; header quest ID 104; language J. Static scan: **219 objects, 201 enemy/NPC records, 50 events, 133 script labels.** Script roundtrip: byte-identical.

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
0x08, 0x08, 0x00, 0x01, 0x01
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 28 | 19 | 0 |
| 8 | 191 | 182 | 50 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 8 | 101 | 10 / 1 | 5 | 1 | trigger_event(1011); stop |
| 8 | 1011 | 10 / 2 | 5 | 1 | trigger_event(1012); stop |
| 8 | 1012 | 10 / 3 | 7 | 1 | trigger_event(1013); stop |
| 8 | 1013 | 10 / 4 | 4 | 1 | trigger_event(1014); stop |
| 8 | 1014 | 10 / 5 | 7 | 1 | trigger_event(1015); stop |
| 8 | 1015 | 10 / 6 | 5 | 1 | set_switch(43); set_switch(44); stop |
| 8 | 301 | 30 / 1 | 2 | 1 | trigger_event(3011); stop |
| 8 | 3011 | 30 / 2 | 2 | 1 | trigger_event(3012); stop |
| 8 | 3012 | 30 / 3 | 3 | 1 | set_switch(37); set_switch(35); set_switch(40); set_switch(33); set_switch(34); set_switch(27); set_switch(28); set_switch(31); set_switch(32); stop |
| 8 | 303 | 30 / 4 | 1 | 1 | trigger_event(3031); stop |
| 8 | 3031 | 30 / 5 | 3 | 1 | trigger_event(3032); stop |
| 8 | 3032 | 30 / 6 | 3 | 1 | stop |
| 8 | 221 | 22 / 1 | 6 | 1 | trigger_event(2211); stop |
| 8 | 2211 | 22 / 2 | 6 | 1 | trigger_event(2212); stop |
| 8 | 2212 | 22 / 3 | 3 | 1 | set_switch(41); set_switch(42); stop |
| 8 | 111 | 11 / 1 | 4 | 1 | trigger_event(1111); stop |
| 8 | 1111 | 11 / 2 | 5 | 1 | trigger_event(1112); stop |
| 8 | 1112 | 11 / 3 | 3 | 1 | set_switch(30); set_switch(29); set_switch(26); set_switch(25); set_switch(31); set_switch(32); stop |
| 8 | 401 | 40 / 1 | 3 | 1 | trigger_event(4011); stop |
| 8 | 4011 | 40 / 2 | 3 | 1 | set_switch(23); set_switch(24); stop |
| 8 | 121 | 12 / 1 | 4 | 1 | trigger_event(1211); stop |
| 8 | 1211 | 12 / 2 | 4 | 1 | trigger_event(1212); stop |
| 8 | 1212 | 12 / 3 | 7 | 1 | set_switch(19); set_switch(20); set_switch(21); set_switch(22); stop |
| 8 | 311 | 31 / 1 | 3 | 1 | trigger_event(3111); stop |
| 8 | 3111 | 31 / 2 | 3 | 1 | trigger_event(3112); stop |
| 8 | 3112 | 31 / 3 | 3 | 1 | set_switch(15); set_switch(18); set_switch(14); set_switch(13); stop |
| 8 | 313 | 31 / 4 | 3 | 1 | trigger_event(3131); stop |
| 8 | 3131 | 31 / 5 | 3 | 1 | trigger_event(3132); stop |
| 8 | 3132 | 31 / 6 | 3 | 1 | stop |
| 8 | 701 | 70 / 1 | 2 | 1 | trigger_event(7011); stop |
| 8 | 7011 | 70 / 2 | 2 | 1 | trigger_event(7012); stop |
| 8 | 7012 | 70 / 3 | 2 | 1 | set_switch(11); stop |
| 8 | 702 | 70 / 4 | 5 | 1 | trigger_event(7021); stop |
| 8 | 7021 | 70 / 5 | 4 | 1 | trigger_event(7022); stop |
| 8 | 7022 | 70 / 6 | 4 | 1 | stop |
| 8 | 551 | 55 / 1 | 2 | 1 | trigger_event(5511); stop |
| 8 | 5511 | 55 / 2 | 4 | 1 | set_switch(9); set_switch(10); stop |
| 8 | 321 | 32 / 1 | 5 | 1 | trigger_event(3211); stop |
| 8 | 3211 | 32 / 2 | 6 | 1 | trigger_event(3212); stop |
| 8 | 3212 | 32 / 3 | 5 | 1 | set_switch(7); set_switch(8); stop |
| 8 | 201 | 20 / 1 | 3 | 1 | trigger_event(2011); stop |
| 8 | 2011 | 20 / 2 | 3 | 1 | trigger_event(2012); stop |
| 8 | 2012 | 20 / 3 | 3 | 1 | trigger_event(2013); stop |
| 8 | 2013 | 20 / 4 | 2 | 1 | trigger_event(2014); stop |
| 8 | 2014 | 20 / 5 | 3 | 1 | stop |
| 8 | 202 | 20 / 6 | 3 | 1 | trigger_event(2021); stop |
| 8 | 2021 | 20 / 7 | 4 | 1 | trigger_event(2022); stop |
| 8 | 2022 | 20 / 8 | 3 | 1 | trigger_event(2023); stop |
| 8 | 2023 | 20 / 9 | 2 | 1 | trigger_event(2024); stop |
| 8 | 2024 | 20 / 10 | 2 | 1 | set_switch(1); set_switch(2); set_switch(3); set_switch(5); set_switch(47); set_switch(48); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
