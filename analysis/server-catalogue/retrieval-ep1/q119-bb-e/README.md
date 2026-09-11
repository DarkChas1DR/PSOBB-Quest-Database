# Fragments of a Memory — retrieval-ep1/q119-bb-e

Episode1; header quest ID 119; language E. Static scan: **558 objects, 871 enemy/NPC records, 178 events, 160 script labels.** Script roundtrip: alignment-only.

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
0x08, 0x08, 0x00, 0x01, 0x00
0x09, 0x09, 0x00, 0x01, 0x00
0x0A, 0x0A, 0x00, 0x01, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 17 | 0 |
| 8 | 239 | 263 | 57 |
| 9 | 126 | 331 | 64 |
| 10 | 132 | 259 | 56 |
| 14 | 35 | 1 | 1 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 8 | 101 | 10 / 1 | 3 | 3 | trigger_event(102); stop |
| 8 | 102 | 10 / 2 | 4 | 3 | trigger_event(103); stop |
| 8 | 103 | 10 / 3 | 6 | 3 | set_switch(6); set_switch(30); stop |
| 8 | 111 | 11 / 1 | 4 | 3 | trigger_event(112); stop |
| 8 | 112 | 11 / 2 | 5 | 3 | trigger_event(113); stop |
| 8 | 113 | 11 / 3 | 5 | 3 | set_switch(144); set_switch(1); stop |
| 8 | 121 | 12 / 1 | 2 | 3 | trigger_event(122); stop |
| 8 | 122 | 12 / 2 | 5 | 3 | trigger_event(123); stop |
| 8 | 123 | 12 / 3 | 6 | 3 | set_switch(12); stop |
| 8 | 201 | 20 / 1 | 4 | 3 | trigger_event(202); stop |
| 8 | 202 | 20 / 2 | 4 | 3 | trigger_event(203); stop |
| 8 | 203 | 20 / 3 | 4 | 3 | set_switch(5); set_switch(20); stop |
| 8 | 211 | 21 / 1 | 6 | 3 | trigger_event(212); stop |
| 8 | 212 | 21 / 2 | 5 | 3 | trigger_event(213); stop |
| 8 | 213 | 21 / 3 | 6 | 3 | set_switch(21); stop |
| 8 | 221 | 22 / 1 | 3 | 3 | trigger_event(222); stop |
| 8 | 222 | 22 / 2 | 4 | 3 | trigger_event(223); stop |
| 8 | 223 | 22 / 3 | 6 | 3 | set_switch(3); set_switch(22); stop |
| 8 | 301 | 30 / 1 | 4 | 3 | trigger_event(302); stop |
| 8 | 302 | 30 / 2 | 5 | 3 | trigger_event(303); stop |
| 8 | 303 | 30 / 3 | 5 | 3 | trigger_event(304); stop |
| 8 | 304 | 30 / 4 | 6 | 3 | set_switch(22); set_switch(30); set_switch(50); set_switch(51); stop |
| 8 | 311 | 31 / 1 | 3 | 3 | trigger_event(312); stop |
| 8 | 312 | 31 / 2 | 4 | 3 | trigger_event(313); stop |
| 8 | 313 | 31 / 3 | 5 | 3 | trigger_event(314); stop |
| 8 | 314 | 31 / 4 | 6 | 3 | set_switch(31); stop |
| 8 | 321 | 32 / 1 | 3 | 3 | trigger_event(322); stop |
| 8 | 322 | 32 / 2 | 4 | 3 | trigger_event(323); stop |
| 8 | 323 | 32 / 3 | 5 | 3 | trigger_event(324); stop |
| 8 | 324 | 32 / 4 | 5 | 3 | stop |
| 8 | 331 | 33 / 1 | 4 | 3 | trigger_event(332); stop |
| 8 | 332 | 33 / 2 | 5 | 3 | trigger_event(333); stop |
| 8 | 333 | 33 / 3 | 5 | 3 | trigger_event(334); stop |
| 8 | 334 | 33 / 4 | 6 | 3 | set_switch(20); set_switch(33); stop |
| 8 | 401 | 40 / 1 | 2 | 3 | trigger_event(402); stop |
| 8 | 402 | 40 / 2 | 4 | 3 | trigger_event(403); stop |
| 8 | 403 | 40 / 3 | 5 | 3 | set_switch(141); set_switch(142); stop |
| 8 | 404 | 40 / 4 | 3 | 3 | trigger_event(405); stop |
| 8 | 405 | 40 / 5 | 2 | 3 | set_switch(143); set_switch(144); set_switch(40); stop |
| 8 | 451 | 45 / 1 | 4 | 3 | trigger_event(452); stop |
| 8 | 452 | 45 / 2 | 4 | 3 | trigger_event(453); stop |
| 8 | 453 | 45 / 3 | 5 | 3 | trigger_event(454); stop |
| 8 | 454 | 45 / 4 | 5 | 3 | stop |
| 8 | 501 | 50 / 1 | 4 | 3 | trigger_event(502); stop |
| 8 | 502 | 50 / 2 | 5 | 3 | trigger_event(503); stop |
| 8 | 503 | 50 / 3 | 6 | 3 | set_switch(50); set_switch(141); stop |
| 8 | 504 | 50 / 4 | 5 | 3 | trigger_event(505); stop |
| 8 | 505 | 50 / 5 | 6 | 3 | set_switch(51); set_switch(143); stop |
| 8 | 551 | 55 / 1 | 4 | 3 | trigger_event(552); stop |
| 8 | 552 | 55 / 2 | 4 | 3 | construct_objects(room=55,group_or_wave=1); trigger_event(553); stop |
| 8 | 553 | 55 / 3 | 5 | 3 | trigger_event(554); stop |
| 8 | 554 | 55 / 4 | 5 | 3 | set_switch(55); stop |
| 8 | 701 | 70 / 1 | 5 | 3 | trigger_event(702); stop |
| 8 | 702 | 70 / 2 | 6 | 3 | trigger_event(703); stop |
| 8 | 703 | 70 / 3 | 6 | 3 | trigger_event(704); stop |
| 8 | 704 | 70 / 4 | 5 | 3 | trigger_event(705); stop |
| 8 | 705 | 70 / 5 | 6 | 3 | set_switch(70); stop |
| 9 | 201 | 20 / 1 | 5 | 3 | trigger_event(202); stop |
| 9 | 202 | 20 / 2 | 6 | 3 | trigger_event(203); stop |
| 9 | 203 | 20 / 3 | 4 | 3 | set_switch(20); stop |
| 9 | 211 | 21 / 1 | 6 | 3 | trigger_event(212); stop |
| 9 | 212 | 21 / 2 | 6 | 3 | set_switch(21); stop |
| 9 | 221 | 22 / 1 | 5 | 3 | trigger_event(222); stop |
| 9 | 222 | 22 / 2 | 5 | 3 | trigger_event(223); stop |
| 9 | 223 | 22 / 3 | 5 | 3 | set_switch(22); stop |
| 9 | 231 | 23 / 1 | 4 | 3 | trigger_event(232); stop |
| 9 | 232 | 23 / 2 | 4 | 3 | trigger_event(233); stop |
| 9 | 233 | 23 / 3 | 5 | 3 | set_switch(23); stop |
| 9 | 241 | 24 / 1 | 3 | 3 | trigger_event(242); stop |
| 9 | 242 | 24 / 2 | 4 | 3 | trigger_event(243); stop |
| 9 | 243 | 24 / 3 | 2 | 3 | set_switch(24); stop |
| 9 | 301 | 30 / 1 | 3 | 3 | trigger_event(302); stop |
| 9 | 302 | 30 / 2 | 3 | 3 | trigger_event(303); stop |
| 9 | 303 | 30 / 3 | 6 | 3 | set_switch(30); stop |
| 9 | 311 | 31 / 1 | 1 | 3 | trigger_event(312); stop |
| 9 | 312 | 31 / 2 | 4 | 3 | trigger_event(313); stop |
| 9 | 313 | 31 / 3 | 6 | 3 | trigger_event(314); stop |
| 9 | 314 | 31 / 4 | 8 | 3 | set_switch(31); set_switch(131); stop |
| 9 | 321 | 32 / 1 | 2 | 3 | trigger_event(322); stop |
| 9 | 322 | 32 / 2 | 8 | 3 | trigger_event(323); stop |
| 9 | 323 | 32 / 3 | 6 | 3 | set_switch(32); stop |
| 9 | 331 | 33 / 1 | 4 | 3 | trigger_event(332); stop |
| 9 | 332 | 33 / 2 | 6 | 3 | trigger_event(333); stop |
| 9 | 333 | 33 / 3 | 5 | 3 | set_switch(33); stop |
| 9 | 341 | 34 / 1 | 5 | 3 | trigger_event(342); stop |
| 9 | 342 | 34 / 2 | 5 | 3 | trigger_event(343); stop |
| 9 | 343 | 34 / 3 | 6 | 3 | set_switch(34); stop |
| 9 | 401 | 40 / 1 | 5 | 3 | trigger_event(402); stop |
| 9 | 402 | 40 / 2 | 6 | 3 | trigger_event(403); stop |
| 9 | 403 | 40 / 3 | 6 | 3 | set_switch(40); stop |
| 9 | 411 | 41 / 1 | 2 | 3 | trigger_event(412); stop |
| 9 | 412 | 41 / 2 | 4 | 3 | trigger_event(413); stop |
| 9 | 413 | 41 / 3 | 5 | 3 | trigger_event(414); stop |
| 9 | 414 | 41 / 4 | 6 | 3 | set_switch(41); stop |
| 9 | 421 | 42 / 1 | 6 | 3 | trigger_event(422); stop |
| 9 | 422 | 42 / 2 | 7 | 3 | trigger_event(423); stop |
| 9 | 423 | 42 / 3 | 6 | 3 | trigger_event(424); stop |
| 9 | 424 | 42 / 4 | 8 | 3 | set_switch(42); stop |
| 9 | 431 | 43 / 1 | 3 | 3 | trigger_event(432); stop |
| 9 | 432 | 43 / 2 | 5 | 3 | trigger_event(433); stop |
| 9 | 433 | 43 / 3 | 6 | 3 | set_switch(43); stop |
| 9 | 601 | 60 / 1 | 2 | 3 | trigger_event(602); stop |
| 9 | 602 | 60 / 2 | 6 | 3 | trigger_event(603); stop |
| 9 | 603 | 60 / 3 | 4 | 3 | trigger_event(604); stop |
| 9 | 604 | 60 / 4 | 5 | 3 | set_switch(60); stop |
| 9 | 651 | 65 / 1 | 6 | 3 | trigger_event(652); stop |
| 9 | 652 | 65 / 2 | 7 | 3 | trigger_event(653); stop |
| 9 | 653 | 65 / 3 | 8 | 3 | trigger_event(654); stop |
| 9 | 654 | 65 / 4 | 8 | 3 | trigger_event(655); stop |
| 9 | 655 | 65 / 5 | 8 | 3 | set_switch(131); stop |
| 9 | 701 | 70 / 1 | 6 | 3 | trigger_event(702); stop |
| 9 | 702 | 70 / 2 | 5 | 3 | trigger_event(703); stop |
| 9 | 703 | 70 / 3 | 6 | 3 | set_switch(70); stop |
| 9 | 751 | 75 / 1 | 5 | 3 | trigger_event(752); stop |
| 9 | 752 | 75 / 2 | 6 | 3 | trigger_event(753); stop |
| 9 | 753 | 75 / 3 | 4 | 3 | set_switch(75); stop |
| 9 | 801 | 80 / 1 | 4 | 3 | trigger_event(802); stop |
| 9 | 802 | 80 / 2 | 2 | 3 | trigger_event(803); stop |
| 9 | 803 | 80 / 3 | 7 | 3 | trigger_event(804); stop |
| 9 | 804 | 80 / 4 | 7 | 3 | trigger_event(805); stop |
| 9 | 805 | 80 / 5 | 8 | 3 | set_switch(80); stop |
| 10 | 201 | 20 / 1 | 6 | 3 | trigger_event(202); stop |
| 10 | 202 | 20 / 2 | 6 | 3 | set_switch(20); stop |
| 10 | 211 | 21 / 1 | 3 | 3 | trigger_event(212); stop |
| 10 | 212 | 21 / 2 | 2 | 3 | set_switch(21); stop |
| 10 | 231 | 23 / 1 | 3 | 3 | trigger_event(232); stop |
| 10 | 232 | 23 / 2 | 4 | 3 | trigger_event(233); stop |
| 10 | 233 | 23 / 3 | 0 | 3 | set_switch(23); stop |
| 10 | 301 | 30 / 1 | 3 | 3 | trigger_event(302); stop |
| 10 | 302 | 30 / 2 | 5 | 3 | trigger_event(303); stop |
| 10 | 303 | 30 / 3 | 7 | 3 | set_switch(30); stop |
| 10 | 311 | 31 / 1 | 4 | 3 | trigger_event(312); stop |
| 10 | 312 | 31 / 2 | 5 | 3 | trigger_event(313); stop |
| 10 | 313 | 31 / 3 | 5 | 3 | trigger_event(314); stop |
| 10 | 314 | 31 / 4 | 6 | 3 | trigger_event(315); stop |
| 10 | 315 | 31 / 5 | 6 | 3 | set_switch(31); stop |
| 10 | 321 | 32 / 1 | 6 | 3 | trigger_event(322); stop |
| 10 | 322 | 32 / 2 | 4 | 3 | trigger_event(323); stop |
| 10 | 323 | 32 / 3 | 6 | 3 | set_switch(32); stop |
| 10 | 331 | 33 / 1 | 5 | 3 | trigger_event(332); stop |
| 10 | 332 | 33 / 2 | 6 | 3 | trigger_event(333); stop |
| 10 | 333 | 33 / 3 | 7 | 3 | set_switch(33); stop |
| 10 | 401 | 40 / 1 | 4 | 3 | trigger_event(402); stop |
| 10 | 402 | 40 / 2 | 4 | 3 | trigger_event(403); stop |
| 10 | 403 | 40 / 3 | 5 | 3 | set_switch(40); stop |
| 10 | 411 | 41 / 1 | 4 | 3 | trigger_event(412); stop |
| 10 | 412 | 41 / 2 | 5 | 3 | trigger_event(413); stop |
| 10 | 413 | 41 / 3 | 5 | 3 | trigger_event(414); stop |
| 10 | 414 | 41 / 4 | 6 | 3 | trigger_event(415); stop |
| 10 | 415 | 41 / 5 | 7 | 3 | set_switch(41); stop |
| 10 | 421 | 42 / 1 | 3 | 3 | trigger_event(422); stop |
| 10 | 422 | 42 / 2 | 5 | 3 | trigger_event(423); stop |
| 10 | 423 | 42 / 3 | 5 | 3 | trigger_event(424); stop |
| 10 | 424 | 42 / 4 | 6 | 3 | trigger_event(425); stop |
| 10 | 425 | 42 / 5 | 7 | 3 | set_switch(42); stop |
| 10 | 431 | 43 / 1 | 4 | 3 | trigger_event(432); stop |
| 10 | 432 | 43 / 2 | 4 | 3 | trigger_event(433); stop |
| 10 | 433 | 43 / 3 | 6 | 3 | set_switch(43); stop |
| 10 | 501 | 50 / 1 | 2 | 3 | trigger_event(502); stop |
| 10 | 502 | 50 / 2 | 4 | 3 | trigger_event(503); stop |
| 10 | 503 | 50 / 3 | 5 | 3 | set_switch(50); stop |
| 10 | 551 | 55 / 1 | 3 | 3 | trigger_event(552); stop |
| 10 | 552 | 55 / 2 | 4 | 3 | trigger_event(553); stop |
| 10 | 553 | 55 / 3 | 3 | 3 | set_switch(55); stop |
| 10 | 651 | 65 / 1 | 3 | 3 | trigger_event(652); stop |
| 10 | 652 | 65 / 2 | 4 | 3 | trigger_event(653); stop |
| 10 | 653 | 65 / 3 | 3 | 3 | set_switch(65); stop |
| 10 | 701 | 70 / 1 | 5 | 3 | trigger_event(702); stop |
| 10 | 702 | 70 / 2 | 6 | 3 | trigger_event(703); stop |
| 10 | 703 | 70 / 3 | 3 | 3 | set_switch(70); stop |
| 10 | 801 | 80 / 1 | 6 | 3 | trigger_event(802); stop |
| 10 | 802 | 80 / 2 | 4 | 3 | trigger_event(803); stop |
| 10 | 803 | 80 / 3 | 5 | 3 | trigger_event(804); stop |
| 10 | 804 | 80 / 4 | 6 | 3 | trigger_event(805); stop |
| 10 | 805 | 80 / 5 | 8 | 3 | set_switch(80); stop |
| 10 | 851 | 85 / 1 | 2 | 3 | trigger_event(852); stop |
| 10 | 852 | 85 / 2 | 4 | 3 | set_switch(85); stop |
| 14 | 1 | 0 / 1 | 1 | 50 | construct_objects(room=0,group_or_wave=1); construct_objects(room=1,group_or_wave=1); construct_objects(room=2,group_or_wave=1); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

A backup is present; decompressed content identical: True. See [text differences](<backup-diff.txt>).

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
