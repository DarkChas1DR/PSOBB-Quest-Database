# ステージ１ — challenge-ep2/d88201-bb-j

Episode2; header quest ID 65535; language J. Static scan: **1150 objects, 431 enemy/NPC records, 130 events, 56 script labels.** Script roundtrip: alignment-only.

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
0x01, 0x13, 0x00, 0x00, 0x00
0x02, 0x13, 0x00, 0x02, 0x00
0x03, 0x13, 0x00, 0x01, 0x00
0x04, 0x14, 0x00, 0x00, 0x00
0x05, 0x14, 0x00, 0x02, 0x00
0x06, 0x14, 0x00, 0x01, 0x00
0x0E, 0x20, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 40 | 12 | 0 |
| 1 | 199 | 58 | 21 |
| 2 | 95 | 66 | 23 |
| 3 | 251 | 77 | 22 |
| 4 | 220 | 70 | 21 |
| 5 | 94 | 46 | 17 |
| 6 | 235 | 101 | 25 |
| 14 | 16 | 1 | 1 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 101 | 10 / 1 | 1 | 10 | set_switch(5); set_switch(6); set_switch(11); set_switch(12); stop |
| 1 | 111 | 11 / 1 | 3 | 200 | trigger_event(1111); stop |
| 1 | 1111 | 11 / 2 | 4 | 10 | set_switch(28); set_switch(29); stop |
| 1 | 201 | 20 / 1 | 4 | 10 | trigger_event(2021); stop |
| 1 | 2021 | 20 / 2 | 5 | 10 | set_switch(3); set_switch(4); set_switch(9); set_switch(10); stop |
| 1 | 301 | 30 / 1 | 4 | 1 | set_switch(23); set_switch(24); set_switch(25); set_switch(26); set_switch(27); stop |
| 1 | 411 | 41 / 1 | 2 | 30 | trigger_event(4111); stop |
| 1 | 4111 | 41 / 2 | 3 | 100 | set_switch(42); set_switch(43); stop |
| 1 | 601 | 60 / 1 | 3 | 250 | trigger_event(6011); stop |
| 1 | 6011 | 60 / 2 | 4 | 10 | set_switch(9); set_switch(10); set_switch(17); set_switch(18); stop |
| 1 | 611 | 61 / 1 | 2 | 100 | set_switch(30); set_switch(31); stop |
| 1 | 701 | 70 / 1 | 4 | 10 | trigger_event(7011); stop |
| 1 | 7011 | 70 / 2 | 3 | 10 | trigger_event(7012); stop |
| 1 | 7012 | 70 / 3 | 1 | 200 | set_switch(32); set_switch(33); stop |
| 1 | 703 | 70 / 4 | 2 | 1 | set_switch(11); set_switch(12); stop |
| 1 | 901 | 90 / 1 | 1 | 10 | set_switch(38); set_switch(39); stop |
| 1 | 911 | 91 / 1 | 2 | 150 | set_switch(34); set_switch(35); set_switch(36); set_switch(37); set_switch(40); set_switch(41); stop |
| 1 | 921 | 92 / 1 | 3 | 150 | set_switch(1); set_switch(2); set_switch(7); set_switch(8); set_switch(3); set_switch(4); set_switch(5); set_switch(6); stop |
| 1 | 931 | 93 / 1 | 3 | 10 | set_switch(13); set_switch(14); set_switch(15); set_switch(16); set_switch(19); set_switch(20); set_switch(21); set_switch(22); stop |
| 1 | 1011 | 101 / 1 | 2 | 1 | stop |
| 1 | 1021 | 102 / 1 | 2 | 1 | stop |
| 2 | 101 | 10 / 1 | 4 | 1 | trigger_event(10101); stop |
| 2 | 10101 | 10 / 2 | 4 | 100 | trigger_event(10102); stop |
| 2 | 10102 | 10 / 3 | 0 | 10 | set_switch(3); set_switch(4); stop |
| 2 | 402 | 40 / 5 | 1 | 10 | stop |
| 2 | 403 | 40 / 6 | 1 | 40 | stop |
| 2 | 404 | 40 / 7 | 1 | 70 | stop |
| 2 | 401 | 40 / 1 | 1 | 130 | trigger_event(4011); stop |
| 2 | 4011 | 40 / 2 | 5 | 10 | trigger_event(4012); stop |
| 2 | 4012 | 40 / 3 | 3 | 10 | trigger_event(4013); stop |
| 2 | 4013 | 40 / 4 | 2 | 150 | set_switch(7); set_switch(8); set_switch(9); set_switch(10); set_switch(17); set_switch(18); set_switch(22); stop |
| 2 | 411 | 41 / 1 | 5 | 10 | trigger_event(4111); stop |
| 2 | 4111 | 41 / 2 | 5 | 10 | trigger_event(4112); stop |
| 2 | 4112 | 41 / 3 | 6 | 60 | trigger_event(4113); stop |
| 2 | 4113 | 41 / 4 | 5 | 100 | trigger_event(4114); stop |
| 2 | 4114 | 41 / 5 | 5 | 10 | set_switch(11); set_switch(12); stop |
| 2 | 601 | 60 / 1 | 4 | 30 | trigger_event(6011); stop |
| 2 | 6011 | 60 / 2 | 4 | 100 | trigger_event(6012); stop |
| 2 | 6012 | 60 / 3 | 0 | 10 | set_switch(23); set_switch(24); set_switch(25); set_switch(13); set_switch(14); stop |
| 2 | 602 | 60 / 4 | 0 | 100 | stop |
| 2 | 901 | 90 / 1 | 4 | 1 | set_switch(15); set_switch(16); stop |
| 2 | 911 | 91 / 1 | 3 | 1 | set_switch(5); set_switch(6); stop |
| 2 | 1011 | 101 / 1 | 1 | 1 | stop |
| 2 | 1601 | 160 / 1 | 2 | 1 | stop |
| 3 | 101 | 10 / 1 | 3 | 150 | set_switch(1); set_switch(2); stop |
| 3 | 111 | 11 / 1 | 1 | 150 | set_switch(37); set_switch(38); stop |
| 3 | 201 | 20 / 1 | 1 | 150 | set_switch(17); set_switch(18); set_switch(19); set_switch(20); stop |
| 3 | 301 | 30 / 1 | 4 | 300 | set_switch(21); set_switch(22); stop |
| 3 | 401 | 40 / 1 | 6 | 10 | trigger_event(4011); stop |
| 3 | 4011 | 40 / 2 | 6 | 10 | set_switch(11); set_switch(12); stop |
| 3 | 411 | 41 / 1 | 6 | 10 | trigger_event(4111); stop |
| 3 | 4111 | 41 / 2 | 6 | 150 | set_switch(25); set_switch(26); set_switch(23); set_switch(24); stop |
| 3 | 611 | 61 / 1 | 4 | 1 | trigger_event(6111); stop |
| 3 | 6111 | 61 / 2 | 3 | 150 | set_switch(40); set_switch(39); stop |
| 3 | 501 | 50 / 1 | 1 | 60 | trigger_event(5011); stop |
| 3 | 5011 | 50 / 2 | 2 | 150 | set_switch(13); set_switch(14); set_switch(15); set_switch(16); stop |
| 3 | 701 | 70 / 1 | 4 | 100 | trigger_event(7011); stop |
| 3 | 7011 | 70 / 2 | 4 | 10 | trigger_event(7012); stop |
| 3 | 7012 | 70 / 3 | 4 | 10 | set_switch(29); set_switch(30); set_switch(31); set_switch(32); set_switch(33); set_switch(34); set_switch(35); set_switch(36); stop |
| 3 | 901 | 90 / 1 | 4 | 1 | set_switch(43); set_switch(44); stop |
| 3 | 911 | 91 / 1 | 4 | 1 | set_switch(27); set_switch(28); stop |
| 3 | 931 | 93 / 1 | 4 | 1 | set_switch(3); set_switch(4); set_switch(5); set_switch(6); stop |
| 3 | 941 | 94 / 1 | 4 | 1 | set_switch(7); set_switch(8); set_switch(9); set_switch(10); stop |
| 3 | 1001 | 100 / 1 | 2 | 1 | stop |
| 3 | 1011 | 101 / 1 | 1 | 1 | stop |
| 3 | 1031 | 103 / 1 | 3 | 1 | stop |
| 4 | 101 | 10 / 1 | 1 | 10 | trigger_event(1011); stop |
| 4 | 1011 | 10 / 2 | 2 | 10 | trigger_event(1012); stop |
| 4 | 1012 | 10 / 3 | 3 | 10 | set_switch(40); set_switch(41); set_switch(42); stop |
| 4 | 111 | 11 / 1 | 4 | 10 | set_switch(3); set_switch(4); stop |
| 4 | 301 | 30 / 1 | 3 | 10 | set_switch(34); set_switch(35); stop |
| 4 | 401 | 40 / 1 | 4 | 10 | trigger_event(4011); stop |
| 4 | 4011 | 40 / 2 | 4 | 150 | set_switch(1); set_switch(2); stop |
| 4 | 501 | 50 / 1 | 4 | 10 | trigger_event(5011); stop |
| 4 | 5011 | 50 / 2 | 5 | 10 | trigger_event(5012); stop |
| 4 | 5012 | 50 / 3 | 5 | 200 | set_switch(12); set_switch(13); stop |
| 4 | 601 | 60 / 1 | 5 | 10 | trigger_event(6011); stop |
| 4 | 6011 | 60 / 2 | 4 | 10 | set_switch(36); set_switch(37); set_switch(38); set_switch(39); stop |
| 4 | 701 | 70 / 1 | 5 | 10 | set_switch(46); set_switch(47); stop |
| 4 | 702 | 70 / 2 | 3 | 10 | trigger_event(7021); stop |
| 4 | 7021 | 70 / 3 | 2 | 200 | set_switch(43); set_switch(44); stop |
| 4 | 951 | 95 / 1 | 2 | 100 | set_switch(32); set_switch(33); stop |
| 4 | 961 | 96 / 1 | 3 | 150 | set_switch(5); set_switch(6); set_switch(50); set_switch(51); stop |
| 4 | 971 | 97 / 1 | 4 | 100 | set_switch(26); set_switch(45); stop |
| 4 | 981 | 98 / 1 | 5 | 10 | set_switch(10); set_switch(11); stop |
| 4 | 1051 | 105 / 1 | 1 | 1 | stop |
| 4 | 1641 | 164 / 1 | 1 | 1 | stop |
| 5 | 201 | 20 / 1 | 1 | 10 | trigger_event(2011); stop |
| 5 | 2011 | 20 / 2 | 2 | 70 | set_switch(3); set_switch(4); stop |
| 5 | 202 | 20 / 3 | 1 | 100 | stop |
| 5 | 501 | 50 / 1 | 3 | 10 | trigger_event(5011); stop |
| 5 | 5011 | 50 / 2 | 5 | 150 | trigger_event(5012); stop |
| 5 | 5012 | 50 / 3 | 3 | 200 | set_switch(9); set_switch(10); set_switch(11); set_switch(12); set_switch(15); set_switch(16); stop |
| 5 | 301 | 30 / 1 | 4 | 10 | trigger_event(3011); stop |
| 5 | 3011 | 30 / 2 | 3 | 150 | set_switch(1); set_switch(2); set_switch(8); set_switch(7); stop |
| 5 | 701 | 70 / 1 | 5 | 10 | trigger_event(7011); stop |
| 5 | 7011 | 70 / 2 | 3 | 10 | trigger_event(7012); stop |
| 5 | 7012 | 70 / 3 | 5 | 150 | trigger_event(7013); stop |
| 5 | 7013 | 70 / 4 | 2 | 200 | set_switch(19); set_switch(20); stop |
| 5 | 901 | 90 / 1 | 2 | 10 | set_switch(13); set_switch(14); set_switch(17); set_switch(18); stop |
| 5 | 911 | 91 / 1 | 3 | 10 | stop |
| 5 | 1001 | 100 / 1 | 2 | 1 | stop |
| 5 | 1011 | 101 / 1 | 1 | 1 | stop |
| 5 | 1601 | 160 / 1 | 1 | 1 | stop |
| 6 | 101 | 10 / 1 | 6 | 100 | trigger_event(1011); stop |
| 6 | 1011 | 10 / 2 | 6 | 100 | trigger_event(1012); stop |
| 6 | 1012 | 10 / 3 | 6 | 100 | set_switch(35); set_switch(36); stop |
| 6 | 111 | 11 / 1 | 3 | 1 | set_switch(39); set_switch(40); stop |
| 6 | 201 | 20 / 1 | 2 | 300 | set_switch(13); set_switch(14); set_switch(15); set_switch(16); set_switch(17); set_switch(18); set_switch(21); set_switch(22); set_switch(23); set_switch(24); stop |
| 6 | 401 | 40 / 1 | 5 | 100 | trigger_event(4011); stop |
| 6 | 4011 | 40 / 2 | 4 | 10 | trigger_event(4012); stop |
| 6 | 4012 | 40 / 3 | 3 | 300 | set_switch(3); set_switch(4); set_switch(5); set_switch(6); stop |
| 6 | 411 | 41 / 1 | 6 | 10 | trigger_event(4111); stop |
| 6 | 4111 | 41 / 2 | 5 | 10 | trigger_event(4112); stop |
| 6 | 4112 | 41 / 3 | 5 | 150 | trigger_event(4113); stop |
| 6 | 4113 | 41 / 4 | 5 | 300 | set_switch(11); set_switch(12); stop |
| 6 | 501 | 50 / 1 | 4 | 1 | trigger_event(5011); stop |
| 6 | 5011 | 50 / 2 | 4 | 10 | trigger_event(5012); stop |
| 6 | 5012 | 50 / 3 | 4 | 10 | set_switch(7); set_switch(8); set_switch(9); set_switch(10); stop |
| 6 | 701 | 70 / 1 | 4 | 150 | trigger_event(7011); stop |
| 6 | 7011 | 70 / 2 | 2 | 10 | set_switch(25); stop |
| 6 | 702 | 70 / 3 | 4 | 150 | trigger_event(7021); stop |
| 6 | 7021 | 70 / 4 | 2 | 10 | set_switch(29); set_switch(30); set_switch(31); set_switch(32); set_switch(33); set_switch(34); stop |
| 6 | 901 | 90 / 1 | 4 | 10 | set_switch(1); set_switch(2); set_switch(27); set_switch(28); stop |
| 6 | 911 | 91 / 1 | 6 | 10 | stop |
| 6 | 921 | 92 / 1 | 4 | 10 | stop |
| 6 | 931 | 93 / 1 | 5 | 10 | set_switch(37); set_switch(38); stop |
| 6 | 1611 | 161 / 1 | 1 | 1 | stop |
| 6 | 1641 | 164 / 1 | 1 | 1 | stop |
| 14 | 1 | 1 / 1 | 1 | 50 | construct_objects(room=1,group_or_wave=1); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
