# Maximum Attack 4th Stage -A- — maximum-attack-ep1/q144-bb-j

Episode1; header quest ID 144; language J. Static scan: **206 objects, 626 enemy/NPC records, 109 events, 224 script labels.** Script roundtrip: byte-identical.

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
0x04, 0x04, 0x00, 0x02, 0x00
0x07, 0x07, 0x00, 0x02, 0x00
0x0A, 0x0A, 0x00, 0x01, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 20 | 0 |
| 4 | 48 | 210 | 33 |
| 7 | 60 | 166 | 35 |
| 10 | 72 | 230 | 41 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 4 | 101 | 10 / 1 | 7 | 3 | trigger_event(102); stop |
| 4 | 102 | 10 / 2 | 7 | 3 | trigger_event(103); stop |
| 4 | 103 | 10 / 3 | 6 | 3 | set_switch(10); stop |
| 4 | 201 | 20 / 1 | 7 | 3 | trigger_event(202); stop |
| 4 | 202 | 20 / 2 | 7 | 3 | trigger_event(203); stop |
| 4 | 203 | 20 / 3 | 7 | 3 | trigger_event(204); stop |
| 4 | 204 | 20 / 4 | 5 | 300 | trigger_event(205); stop |
| 4 | 205 | 20 / 5 | 7 | 3 | trigger_event(206); stop |
| 4 | 206 | 20 / 6 | 7 | 3 | set_switch(20); stop |
| 4 | 221 | 22 / 1 | 8 | 3 | trigger_event(222); stop |
| 4 | 222 | 22 / 2 | 8 | 3 | trigger_event(223); stop |
| 4 | 223 | 22 / 3 | 4 | 3 | set_switch(22); stop |
| 4 | 121 | 12 / 1 | 7 | 3 | trigger_event(122); stop |
| 4 | 122 | 12 / 2 | 7 | 3 | trigger_event(123); stop |
| 4 | 123 | 12 / 3 | 5 | 3 | trigger_event(124); stop |
| 4 | 124 | 12 / 4 | 6 | 3 | set_switch(12); stop |
| 4 | 211 | 21 / 1 | 5 | 3 | trigger_event(212); stop |
| 4 | 212 | 21 / 2 | 5 | 3 | trigger_event(213); stop |
| 4 | 213 | 21 / 3 | 7 | 3 | trigger_event(214); stop |
| 4 | 214 | 21 / 4 | 7 | 150 | trigger_event(215); stop |
| 4 | 215 | 21 / 5 | 6 | 3 | set_switch(21); stop |
| 4 | 111 | 11 / 1 | 6 | 3 | trigger_event(112); stop |
| 4 | 112 | 11 / 2 | 6 | 3 | trigger_event(113); stop |
| 4 | 113 | 11 / 3 | 3 | 3 | trigger_event(114); stop |
| 4 | 114 | 11 / 4 | 4 | 300 | trigger_event(115); stop |
| 4 | 115 | 11 / 5 | 8 | 3 | trigger_event(116); stop |
| 4 | 116 | 11 / 6 | 8 | 3 | set_switch(11); stop |
| 4 | 131 | 13 / 1 | 8 | 3 | trigger_event(132); stop |
| 4 | 132 | 13 / 2 | 8 | 3 | trigger_event(133); stop |
| 4 | 133 | 13 / 3 | 8 | 300 | trigger_event(134); stop |
| 4 | 134 | 13 / 4 | 5 | 3 | trigger_event(135); stop |
| 4 | 135 | 13 / 5 | 5 | 3 | trigger_event(136); stop |
| 4 | 136 | 13 / 6 | 6 | 3 | set_switch(13); stop |
| 7 | 201 | 20 / 1 | 5 | 3 | trigger_event(202); stop |
| 7 | 202 | 20 / 2 | 5 | 3 | trigger_event(203); stop |
| 7 | 203 | 20 / 3 | 1 | 150 | trigger_event(204); stop |
| 7 | 204 | 20 / 4 | 1 | 3 | set_switch(20); stop |
| 7 | 701 | 70 / 1 | 6 | 3 | trigger_event(702); stop |
| 7 | 702 | 70 / 2 | 6 | 3 | trigger_event(703); stop |
| 7 | 703 | 70 / 3 | 6 | 3 | trigger_event(704); stop |
| 7 | 704 | 70 / 4 | 3 | 3 | trigger_event(705); stop |
| 7 | 705 | 70 / 5 | 3 | 300 | trigger_event(706); stop |
| 7 | 706 | 70 / 6 | 3 | 3 | trigger_event(707); stop |
| 7 | 707 | 70 / 7 | 3 | 3 | set_switch(70); set_switch(71); stop |
| 7 | 501 | 50 / 1 | 8 | 3 | trigger_event(502); stop |
| 7 | 502 | 50 / 2 | 8 | 3 | trigger_event(503); stop |
| 7 | 503 | 50 / 3 | 7 | 3 | trigger_event(504); stop |
| 7 | 504 | 50 / 4 | 7 | 3 | set_switch(50); stop |
| 7 | 401 | 40 / 1 | 6 | 3 | trigger_event(402); stop |
| 7 | 402 | 40 / 2 | 6 | 3 | trigger_event(403); stop |
| 7 | 403 | 40 / 3 | 4 | 3 | trigger_event(404); stop |
| 7 | 404 | 40 / 4 | 4 | 300 | trigger_event(405); stop |
| 7 | 405 | 40 / 5 | 1 | 3 | trigger_event(406); stop |
| 7 | 406 | 40 / 6 | 1 | 3 | set_switch(40); stop |
| 7 | 511 | 51 / 1 | 8 | 3 | trigger_event(512); stop |
| 7 | 512 | 51 / 2 | 8 | 3 | trigger_event(513); stop |
| 7 | 513 | 51 / 3 | 8 | 3 | trigger_event(514); stop |
| 7 | 514 | 51 / 4 | 4 | 150 | trigger_event(515); stop |
| 7 | 515 | 51 / 5 | 2 | 3 | set_switch(51); stop |
| 7 | 601 | 60 / 1 | 4 | 3 | trigger_event(602); stop |
| 7 | 602 | 60 / 2 | 8 | 3 | trigger_event(603); stop |
| 7 | 603 | 60 / 3 | 1 | 3 | trigger_event(604); stop |
| 7 | 604 | 60 / 4 | 8 | 3 | trigger_event(605); stop |
| 7 | 605 | 60 / 5 | 4 | 300 | trigger_event(606); stop |
| 7 | 606 | 60 / 6 | 4 | 15 | trigger_event(607); stop |
| 7 | 607 | 60 / 7 | 5 | 3 | trigger_event(608); stop |
| 7 | 608 | 60 / 8 | 2 | 3 | trigger_event(609); stop |
| 7 | 609 | 60 / 9 | 6 | 3 | set_switch(60); stop |
| 10 | 421 | 42 / 1 | 7 | 3 | trigger_event(422); stop |
| 10 | 422 | 42 / 2 | 7 | 3 | trigger_event(423); stop |
| 10 | 423 | 42 / 3 | 6 | 3 | set_switch(42); stop |
| 10 | 651 | 65 / 1 | 6 | 3 | trigger_event(652); stop |
| 10 | 652 | 65 / 2 | 2 | 3 | trigger_event(653); stop |
| 10 | 653 | 65 / 3 | 4 | 3 | trigger_event(654); stop |
| 10 | 654 | 65 / 4 | 3 | 3 | set_switch(65); stop |
| 10 | 331 | 33 / 1 | 7 | 3 | trigger_event(332); stop |
| 10 | 332 | 33 / 2 | 7 | 3 | trigger_event(333); stop |
| 10 | 333 | 33 / 3 | 5 | 150 | trigger_event(334); stop |
| 10 | 334 | 33 / 4 | 6 | 3 | trigger_event(335); stop |
| 10 | 335 | 33 / 5 | 7 | 3 | set_switch(33); stop |
| 10 | 201 | 20 / 1 | 4 | 3 | trigger_event(202); stop |
| 10 | 202 | 20 / 2 | 4 | 3 | trigger_event(203); stop |
| 10 | 203 | 20 / 3 | 4 | 150 | trigger_event(204); stop |
| 10 | 204 | 20 / 4 | 9 | 3 | trigger_event(205); stop |
| 10 | 205 | 20 / 5 | 4 | 3 | set_switch(20); stop |
| 10 | 411 | 41 / 1 | 1 | 3 | trigger_event(412); stop |
| 10 | 412 | 41 / 2 | 8 | 3 | trigger_event(413); stop |
| 10 | 413 | 41 / 3 | 8 | 3 | trigger_event(414); stop |
| 10 | 414 | 41 / 4 | 10 | 3 | trigger_event(415); stop |
| 10 | 415 | 41 / 5 | 4 | 300 | trigger_event(416); stop |
| 10 | 416 | 41 / 6 | 2 | 3 | trigger_event(417); stop |
| 10 | 417 | 41 / 7 | 3 | 3 | set_switch(41); stop |
| 10 | 211 | 21 / 1 | 7 | 3 | trigger_event(212); stop |
| 10 | 212 | 21 / 2 | 9 | 3 | trigger_event(213); stop |
| 10 | 213 | 21 / 3 | 5 | 3 | trigger_event(214); stop |
| 10 | 214 | 21 / 4 | 4 | 150 | trigger_event(215); stop |
| 10 | 215 | 21 / 5 | 5 | 3 | set_switch(21); set_switch(41); stop |
| 10 | 221 | 22 / 1 | 8 | 3 | trigger_event(222); stop |
| 10 | 222 | 22 / 2 | 7 | 3 | trigger_event(223); stop |
| 10 | 223 | 22 / 3 | 6 | 3 | trigger_event(224); stop |
| 10 | 224 | 22 / 4 | 9 | 150 | trigger_event(225); stop |
| 10 | 225 | 22 / 5 | 1 | 3 | set_switch(22); set_switch(65); set_switch(21); stop |
| 10 | 311 | 31 / 1 | 9 | 3 | trigger_event(312); stop |
| 10 | 312 | 31 / 2 | 2 | 3 | trigger_event(313); stop |
| 10 | 313 | 31 / 3 | 8 | 3 | trigger_event(314); stop |
| 10 | 314 | 31 / 4 | 8 | 3 | trigger_event(315); stop |
| 10 | 315 | 31 / 5 | 4 | 300 | trigger_event(316); stop |
| 10 | 316 | 31 / 6 | 9 | 3 | trigger_event(317); stop |
| 10 | 317 | 31 / 7 | 1 | 3 | set_switch(31); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
