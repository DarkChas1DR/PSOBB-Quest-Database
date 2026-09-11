# Sweep-up Operation #4 — extermination-ep1/q160-bb-e

Episode1; header quest ID 160; language E. Static scan: **166 objects, 212 enemy/NPC records, 62 events, 50 script labels.** Script roundtrip: byte-identical.

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
| 0 | 28 | 10 | 0 |
| 9 | 138 | 202 | 62 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 9 | 651 | 65 / 1 | 7 | 45 | trigger_event(652); stop |
| 9 | 652 | 65 / 2 | 6 | 10 | trigger_event(653); stop |
| 9 | 653 | 65 / 3 | 0 | 10 | set_switch(13); set_switch(14); stop |
| 9 | 311 | 31 / 1 | 6 | 40 | trigger_event(312); stop |
| 9 | 312 | 31 / 2 | 7 | 10 | trigger_event(313); stop |
| 9 | 313 | 31 / 3 | 5 | 10 | set_switch(15); set_switch(16); set_switch(17); set_switch(18); set_switch(7); set_switch(8); stop |
| 9 | 401 | 40 / 1 | 1 | 30 | trigger_event(402); trigger_event(405); stop |
| 9 | 402 | 40 / 2 | 4 | 10 | trigger_event(403); stop |
| 9 | 403 | 40 / 3 | 2 | 10 | trigger_event(404); stop |
| 9 | 404 | 40 / 4 | 1 | 10 | stop |
| 9 | 405 | 40 / 5 | 5 | 10 | trigger_event(406); stop |
| 9 | 406 | 40 / 6 | 2 | 20 | stop |
| 9 | 400 | 40 / 0 | 0 | 0 | set_switch(19); stop |
| 9 | 201 | 20 / 1 | 5 | 40 | set_switch(21); set_switch(22); set_switch(23); set_switch(24); stop |
| 9 | 601 | 60 / 1 | 1 | 30 | trigger_event(602); stop |
| 9 | 602 | 60 / 2 | 3 | 30 | trigger_event(603); stop |
| 9 | 603 | 60 / 3 | 6 | 1 | set_switch(31); set_switch(32); stop |
| 9 | 241 | 24 / 1 | 4 | 30 | trigger_event(242); stop |
| 9 | 242 | 24 / 2 | 2 | 20 | set_switch(33); set_switch(34); stop |
| 9 | 421 | 42 / 1 | 5 | 30 | trigger_event(423); trigger_event(427); stop |
| 9 | 423 | 42 / 3 | 3 | 20 | trigger_event(424); stop |
| 9 | 424 | 42 / 4 | 4 | 5 | trigger_event(425); stop |
| 9 | 425 | 42 / 5 | 1 | 30 | stop |
| 9 | 427 | 42 / 7 | 4 | 10 | trigger_event(428); stop |
| 9 | 428 | 42 / 8 | 1 | 10 | trigger_event(429); stop |
| 9 | 429 | 42 / 9 | 1 | 30 | stop |
| 9 | 420 | 42 / 0 | 0 | 0 | set_switch(35); stop |
| 9 | 321 | 32 / 1 | 5 | 60 | set_switch(102); stop |
| 9 | 323 | 32 / 3 | 4 | 30 | set_switch(39); set_switch(40); stop |
| 9 | 801 | 80 / 1 | 2 | 60 | trigger_event(802); stop |
| 9 | 802 | 80 / 2 | 4 | 30 | trigger_event(803); stop |
| 9 | 803 | 80 / 3 | 2 | 30 | trigger_event(804); stop |
| 9 | 804 | 80 / 4 | 2 | 30 | trigger_event(805); stop |
| 9 | 805 | 80 / 5 | 3 | 5 | trigger_event(807); stop |
| 9 | 807 | 80 / 7 | 4 | 50 | trigger_event(808); stop |
| 9 | 808 | 80 / 8 | 4 | 10 | stop |
| 9 | 800 | 80 / 0 | 0 | 0 | set_switch(41); set_switch(42); stop |
| 9 | 701 | 70 / 1 | 3 | 45 | set_switch(43); stop |
| 9 | 702 | 70 / 2 | 2 | 10 | set_switch(45); set_switch(46); stop |
| 9 | 221 | 22 / 1 | 3 | 10 | trigger_event(222); stop |
| 9 | 222 | 22 / 2 | 5 | 10 | set_switch(47); set_switch(48); stop |
| 9 | 431 | 43 / 1 | 4 | 30 | trigger_event(433); stop |
| 9 | 433 | 43 / 3 | 7 | 15 | trigger_event(434); stop |
| 9 | 434 | 43 / 4 | 6 | 10 | set_switch(49); set_switch(50); set_switch(51); set_switch(52); stop |
| 9 | 341 | 34 / 1 | 4 | 30 | trigger_event(342); stop |
| 9 | 342 | 34 / 2 | 4 | 15 | trigger_event(343); stop |
| 9 | 343 | 34 / 3 | 6 | 15 | trigger_event(344); stop |
| 9 | 344 | 34 / 4 | 6 | 30 | set_switch(53); set_switch(54); set_switch(56); stop |
| 9 | 331 | 33 / 1 | 3 | 10 | trigger_event(332); stop |
| 9 | 332 | 33 / 2 | 3 | 10 | trigger_event(333); stop |
| 9 | 333 | 33 / 3 | 4 | 10 | trigger_event(334); stop |
| 9 | 334 | 33 / 4 | 1 | 10 | trigger_event(335); trigger_event(3310); stop |
| 9 | 335 | 33 / 5 | 1 | 10 | trigger_event(336); stop |
| 9 | 336 | 33 / 6 | 2 | 10 | trigger_event(337); stop |
| 9 | 337 | 33 / 7 | 2 | 10 | set_switch(101); stop |
| 9 | 3310 | 33 / 10 | 1 | 10 | trigger_event(3311); stop |
| 9 | 3311 | 33 / 11 | 2 | 10 | trigger_event(3312); stop |
| 9 | 3312 | 33 / 12 | 2 | 10 | set_switch(100); stop |
| 9 | 3313 | 33 / 13 | 5 | 10 | trigger_event(3314); stop |
| 9 | 3314 | 33 / 14 | 3 | 10 | trigger_event(3315); stop |
| 9 | 3315 | 33 / 15 | 7 | 10 | stop |
| 9 | 330 | 33 / 0 | 0 | 0 | set_switch(57); set_switch(58); set_switch(9); construct_objects(room=378,group_or_wave=1); stop |

## Review notes

- Nonzero data after terminal header
