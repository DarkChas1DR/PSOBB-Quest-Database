# New Mop-Up Operation #1 — extermination-ep4/q816-bb-e

Episode4; header quest ID 816; language E. Static scan: **229 objects, 168 enemy/NPC records, 61 events, 132 script labels.** Script roundtrip: byte-identical.

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
0x01, 0x24, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 17 | 0 |
| 1 | 203 | 151 | 61 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 101 | 10 / 1 | 5 | 30 | trigger_event(102); stop |
| 1 | 102 | 10 / 2 | 5 | 30 | trigger_event(103); trigger_event(104); stop |
| 1 | 103 | 10 / 3 | 4 | 30 | set_switch(101); stop |
| 1 | 104 | 10 / 4 | 1 | 30 | trigger_event(105); trigger_event(106); trigger_event(107); stop |
| 1 | 105 | 10 / 5 | 1 | 30 | set_switch(102); stop |
| 1 | 106 | 10 / 6 | 2 | 30 | trigger_event(108); stop |
| 1 | 107 | 10 / 7 | 2 | 30 | trigger_event(109); stop |
| 1 | 108 | 10 / 8 | 3 | 30 | set_switch(103); stop |
| 1 | 109 | 10 / 9 | 1 | 30 | set_switch(104); stop |
| 1 | 111 | 11 / 1 | 1 | 30 | trigger_event(112); stop |
| 1 | 112 | 11 / 2 | 6 | 30 | trigger_event(113); stop |
| 1 | 113 | 11 / 3 | 3 | 30 | set_switch(11); stop |
| 1 | 201 | 20 / 1 | 3 | 30 | trigger_event(202); trigger_event(203); stop |
| 1 | 202 | 20 / 2 | 2 | 30 | trigger_event(204); stop |
| 1 | 203 | 20 / 3 | 3 | 30 | trigger_event(205); stop |
| 1 | 204 | 20 / 4 | 1 | 30 | trigger_event(206); stop |
| 1 | 205 | 20 / 5 | 1 | 30 | trigger_event(207); stop |
| 1 | 206 | 20 / 6 | 3 | 30 | trigger_event(208); stop |
| 1 | 207 | 20 / 7 | 3 | 30 | trigger_event(209); stop |
| 1 | 208 | 20 / 8 | 3 | 30 | trigger_event(2010); stop |
| 1 | 209 | 20 / 9 | 5 | 30 | set_switch(201); stop |
| 1 | 2010 | 20 / 10 | 3 | 30 | set_switch(202); stop |
| 1 | 301 | 30 / 1 | 5 | 30 | set_switch(30); stop |
| 1 | 302 | 30 / 2 | 3 | 30 | trigger_event(303); trigger_event(304); stop |
| 1 | 303 | 30 / 3 | 1 | 30 | trigger_event(305); stop |
| 1 | 304 | 30 / 4 | 2 | 30 | trigger_event(306); stop |
| 1 | 305 | 30 / 5 | 1 | 30 | trigger_event(307); stop |
| 1 | 306 | 30 / 6 | 1 | 30 | trigger_event(308); stop |
| 1 | 307 | 30 / 7 | 1 | 30 | trigger_event(309); stop |
| 1 | 308 | 30 / 8 | 4 | 30 | set_switch(32); stop |
| 1 | 309 | 30 / 9 | 3 | 30 | trigger_event(3010); stop |
| 1 | 3010 | 30 / 10 | 4 | 30 | set_switch(33); stop |
| 1 | 401 | 40 / 1 | 6 | 30 | trigger_event(4011); stop |
| 1 | 4011 | 40 / 2 | 5 | 30 | trigger_event(4012); stop |
| 1 | 4012 | 40 / 3 | 5 | 30 | set_switch(40); stop |
| 1 | 402 | 40 / 4 | 4 | 30 | trigger_event(4021); stop |
| 1 | 4021 | 40 / 5 | 5 | 30 | trigger_event(4022); stop |
| 1 | 4022 | 40 / 6 | 5 | 30 | set_switch(41); stop |
| 1 | 501 | 50 / 99 | 0 | 30 | trigger_event(5001); trigger_event(5002); trigger_event(5003); stop |
| 1 | 5001 | 50 / 1 | 1 | 30 | trigger_event(5011); stop |
| 1 | 5002 | 50 / 2 | 1 | 30 | trigger_event(5012); stop |
| 1 | 5003 | 50 / 3 | 1 | 30 | trigger_event(5013); stop |
| 1 | 5011 | 50 / 4 | 1 | 30 | trigger_event(5021); stop |
| 1 | 5012 | 50 / 5 | 1 | 30 | trigger_event(5022); stop |
| 1 | 5013 | 50 / 6 | 1 | 30 | trigger_event(5023); stop |
| 1 | 5021 | 50 / 7 | 1 | 30 | trigger_event(5031); stop |
| 1 | 5022 | 50 / 8 | 1 | 30 | trigger_event(5032); stop |
| 1 | 5023 | 50 / 9 | 1 | 30 | trigger_event(5033); stop |
| 1 | 5031 | 50 / 10 | 1 | 30 | trigger_event(5041); stop |
| 1 | 5032 | 50 / 11 | 1 | 30 | trigger_event(5042); stop |
| 1 | 5033 | 50 / 12 | 2 | 30 | trigger_event(5043); stop |
| 1 | 5041 | 50 / 13 | 2 | 30 | set_switch(52); stop |
| 1 | 5042 | 50 / 14 | 2 | 30 | set_switch(53); stop |
| 1 | 5043 | 50 / 15 | 4 | 30 | set_switch(54); stop |
| 1 | 601 | 60 / 99 | 0 | 30 | trigger_event(6011); trigger_event(6012); stop |
| 1 | 6011 | 60 / 1 | 1 | 30 | trigger_event(603); stop |
| 1 | 6012 | 60 / 2 | 1 | 30 | trigger_event(604); stop |
| 1 | 603 | 60 / 3 | 2 | 30 | trigger_event(605); stop |
| 1 | 604 | 60 / 4 | 2 | 30 | set_switch(62); stop |
| 1 | 605 | 60 / 5 | 1 | 30 | set_switch(63); stop |
| 1 | 602 | 60 / 6 | 7 | 30 | set_switch(61); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

A backup is present; decompressed content identical: True. See [text differences](<backup-diff.txt>).

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
