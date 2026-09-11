# War of Limits 1 — extermination-ep4/q811-bb-e

Episode4; header quest ID 811; language E. Static scan: **331 objects, 263 enemy/NPC records, 74 events, 92 script labels.** Script roundtrip: byte-identical.

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
| 1 | 305 | 246 | 74 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 101 | 10 / 1 | 6 | 30 | trigger_event(102); stop |
| 1 | 102 | 10 / 2 | 6 | 30 | trigger_event(103); stop |
| 1 | 103 | 10 / 3 | 6 | 30 | trigger_event(104); stop |
| 1 | 104 | 10 / 4 | 7 | 30 | trigger_event(105); stop |
| 1 | 105 | 10 / 5 | 8 | 30 | trigger_event(106); stop |
| 1 | 106 | 10 / 6 | 7 | 30 | trigger_event(107); stop |
| 1 | 107 | 10 / 7 | 4 | 30 | set_switch(10); stop |
| 1 | 111 | 11 / 1 | 4 | 30 | trigger_event(112); stop |
| 1 | 112 | 11 / 2 | 5 | 30 | trigger_event(113); stop |
| 1 | 113 | 11 / 3 | 4 | 30 | set_switch(11); stop |
| 1 | 201 | 20 / 1 | 3 | 30 | trigger_event(202); stop |
| 1 | 202 | 20 / 2 | 4 | 30 | trigger_event(203); stop |
| 1 | 203 | 20 / 3 | 6 | 30 | set_switch(21); construct_objects(room=20,group_or_wave=1); stop |
| 1 | 204 | 20 / 4 | 5 | 30 | trigger_event(205); stop |
| 1 | 205 | 20 / 5 | 6 | 30 | trigger_event(206); stop |
| 1 | 206 | 20 / 6 | 6 | 30 | trigger_event(207); stop |
| 1 | 207 | 20 / 7 | 6 | 30 | trigger_event(208); stop |
| 1 | 208 | 20 / 8 | 1 | 30 | trigger_event(209); trigger_event(2010); stop |
| 1 | 209 | 20 / 9 | 1 | 30 | trigger_event(2011); stop |
| 1 | 2010 | 20 / 10 | 1 | 30 | trigger_event(2012); stop |
| 1 | 2011 | 20 / 11 | 1 | 30 | trigger_event(2013); stop |
| 1 | 2012 | 20 / 12 | 2 | 30 | trigger_event(2014); stop |
| 1 | 2013 | 20 / 13 | 1 | 30 | set_switch(23); stop |
| 1 | 2014 | 20 / 14 | 1 | 30 | set_switch(24); stop |
| 1 | 211 | 21 / 1 | 4 | 30 | trigger_event(212); stop |
| 1 | 212 | 21 / 2 | 5 | 30 | trigger_event(213); stop |
| 1 | 213 | 21 / 3 | 5 | 30 | set_switch(211); construct_objects(room=21,group_or_wave=1); stop |
| 1 | 214 | 21 / 4 | 1 | 30 | trigger_event(215); stop |
| 1 | 215 | 21 / 5 | 5 | 30 | trigger_event(216); stop |
| 1 | 216 | 21 / 6 | 6 | 30 | set_switch(212); stop |
| 1 | 301 | 30 / 1 | 1 | 30 | trigger_event(302); trigger_event(303); stop |
| 1 | 302 | 30 / 2 | 1 | 30 | trigger_event(304); stop |
| 1 | 303 | 30 / 3 | 1 | 30 | trigger_event(305); stop |
| 1 | 304 | 30 / 4 | 1 | 30 | trigger_event(306); stop |
| 1 | 305 | 30 / 5 | 2 | 30 | trigger_event(317); stop |
| 1 | 306 | 30 / 6 | 2 | 30 | trigger_event(308); stop |
| 1 | 317 | 30 / 7 | 1 | 30 | trigger_event(309); stop |
| 1 | 308 | 30 / 8 | 1 | 30 | trigger_event(310); stop |
| 1 | 309 | 30 / 9 | 2 | 30 | trigger_event(311); stop |
| 1 | 310 | 30 / 10 | 2 | 30 | trigger_event(312); stop |
| 1 | 311 | 30 / 11 | 2 | 30 | trigger_event(313); stop |
| 1 | 312 | 30 / 12 | 1 | 30 | trigger_event(314); stop |
| 1 | 313 | 30 / 13 | 3 | 30 | trigger_event(315); stop |
| 1 | 314 | 30 / 14 | 1 | 30 | trigger_event(316); stop |
| 1 | 315 | 30 / 15 | 1 | 30 | set_switch(35); stop |
| 1 | 316 | 30 / 16 | 2 | 30 | set_switch(34); stop |
| 1 | 307 | 30 / 17 | 8 | 30 | set_switch(32); stop |
| 1 | 401 | 40 / 1 | 5 | 30 | trigger_event(402); stop |
| 1 | 402 | 40 / 2 | 6 | 30 | trigger_event(403); stop |
| 1 | 403 | 40 / 3 | 6 | 30 | construct_objects(room=40,group_or_wave=1); set_switch(41); stop |
| 1 | 404 | 40 / 4 | 3 | 30 | trigger_event(405); stop |
| 1 | 405 | 40 / 5 | 4 | 30 | trigger_event(406); stop |
| 1 | 406 | 40 / 6 | 6 | 30 | set_switch(42); stop |
| 1 | 501 | 50 / 99 | 0 | 30 | trigger_event(511); trigger_event(512); trigger_event(513); stop |
| 1 | 511 | 50 / 1 | 1 | 30 | trigger_event(521); stop |
| 1 | 512 | 50 / 2 | 1 | 30 | trigger_event(522); stop |
| 1 | 513 | 50 / 3 | 1 | 30 | trigger_event(523); stop |
| 1 | 521 | 50 / 4 | 1 | 30 | trigger_event(531); stop |
| 1 | 522 | 50 / 5 | 2 | 30 | trigger_event(532); stop |
| 1 | 523 | 50 / 6 | 2 | 30 | trigger_event(533); stop |
| 1 | 531 | 50 / 7 | 1 | 30 | trigger_event(541); stop |
| 1 | 532 | 50 / 8 | 1 | 30 | trigger_event(542); stop |
| 1 | 533 | 50 / 9 | 2 | 30 | trigger_event(543); stop |
| 1 | 541 | 50 / 10 | 1 | 30 | set_switch(55); stop |
| 1 | 542 | 50 / 11 | 1 | 30 | set_switch(56); stop |
| 1 | 543 | 50 / 12 | 4 | 30 | set_switch(57); stop |
| 1 | 551 | 50 / 13 | 4 | 30 | set_switch(52); stop |
| 1 | 561 | 50 / 14 | 3 | 30 | set_switch(53); stop |
| 1 | 601 | 60 / 1 | 4 | 30 | trigger_event(602); stop |
| 1 | 602 | 60 / 2 | 6 | 30 | trigger_event(603); stop |
| 1 | 603 | 60 / 3 | 6 | 30 | set_switch(60); stop |
| 1 | 801 | 80 / 1 | 4 | 30 | trigger_event(802); stop |
| 1 | 802 | 80 / 2 | 6 | 30 | trigger_event(803); stop |
| 1 | 803 | 80 / 3 | 6 | 30 | set_switch(80); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

A backup is present; decompressed content identical: True. See [text differences](<backup-diff.txt>).

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
