# Lost SHOCK RIFLE — retrieval-ep2/q155-bb-e

Episode2; header quest ID 155; language E. Static scan: **443 objects, 453 enemy/NPC records, 87 events, 51 script labels.** Script roundtrip: byte-identical.

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
| 0 | 38 | 8 | 0 |
| 1 | 195 | 220 | 45 |
| 2 | 180 | 224 | 41 |
| 14 | 30 | 1 | 1 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 921 | 92 / 1 | 3 | 30 | trigger_event(922); stop |
| 1 | 922 | 92 / 2 | 4 | 30 | set_switch(1); stop |
| 1 | 101 | 10 / 1 | 5 | 30 | trigger_event(102); stop |
| 1 | 102 | 10 / 2 | 5 | 30 | trigger_event(103); stop |
| 1 | 103 | 10 / 3 | 5 | 30 | trigger_event(104); stop |
| 1 | 104 | 10 / 4 | 5 | 30 | set_switch(4); stop |
| 1 | 701 | 70 / 1 | 6 | 30 | trigger_event(702); stop |
| 1 | 702 | 70 / 2 | 5 | 30 | stop |
| 1 | 703 | 70 / 3 | 5 | 30 | set_switch(5); trigger_event(501); stop |
| 1 | 501 | 50 / 1 | 5 | 30 | trigger_event(502); stop |
| 1 | 502 | 50 / 2 | 3 | 30 | trigger_event(503); stop |
| 1 | 503 | 50 / 3 | 4 | 30 | set_switch(6); stop |
| 1 | 601 | 60 / 1 | 6 | 1 | trigger_event(602); stop |
| 1 | 602 | 60 / 2 | 6 | 30 | trigger_event(603); stop |
| 1 | 603 | 60 / 3 | 6 | 30 | construct_objects(room=60,group_or_wave=1); stop |
| 1 | 201 | 20 / 1 | 4 | 30 | set_switch(85); construct_objects(room=20,group_or_wave=1); stop |
| 1 | 504 | 50 / 4 | 4 | 30 | set_switch(7); stop |
| 1 | 931 | 93 / 1 | 4 | 30 | trigger_event(932); stop |
| 1 | 932 | 93 / 2 | 3 | 30 | set_switch(103); stop |
| 1 | 301 | 30 / 1 | 4 | 90 | trigger_event(302); stop |
| 1 | 302 | 30 / 2 | 4 | 30 | trigger_event(303); stop |
| 1 | 303 | 30 / 3 | 5 | 30 | set_switch(8); stop |
| 1 | 801 | 80 / 1 | 2 | 60 | trigger_event(802); stop |
| 1 | 802 | 80 / 2 | 4 | 30 | trigger_event(803); stop |
| 1 | 803 | 80 / 3 | 5 | 30 | set_switch(9); construct_objects(room=80,group_or_wave=1); trigger_event(611); stop |
| 1 | 611 | 61 / 1 | 4 | 1 | trigger_event(612); stop |
| 1 | 612 | 61 / 2 | 6 | 30 | trigger_event(613); stop |
| 1 | 613 | 61 / 3 | 6 | 30 | set_switch(10); stop |
| 1 | 111 | 11 / 1 | 4 | 30 | trigger_event(112); stop |
| 1 | 112 | 11 / 2 | 6 | 30 | set_switch(11); stop |
| 1 | 704 | 70 / 4 | 3 | 90 | trigger_event(705); stop |
| 1 | 705 | 70 / 5 | 4 | 60 | trigger_event(706); stop |
| 1 | 706 | 70 / 6 | 5 | 30 | set_switch(12); stop |
| 1 | 401 | 40 / 1 | 7 | 1 | trigger_event(402); stop |
| 1 | 402 | 40 / 2 | 7 | 60 | trigger_event(403); stop |
| 1 | 403 | 40 / 3 | 6 | 30 | trigger_event(404); stop |
| 1 | 404 | 40 / 4 | 6 | 30 | set_switch(13); stop |
| 1 | 911 | 91 / 1 | 4 | 30 | trigger_event(912); stop |
| 1 | 912 | 91 / 2 | 4 | 30 | set_switch(14); stop |
| 1 | 411 | 41 / 1 | 5 | 90 | trigger_event(412); stop |
| 1 | 412 | 41 / 2 | 5 | 60 | trigger_event(413); stop |
| 1 | 413 | 41 / 3 | 5 | 60 | trigger_event(414); stop |
| 1 | 414 | 41 / 4 | 6 | 60 | trigger_event(415); stop |
| 1 | 415 | 41 / 5 | 8 | 60 | trigger_event(416); stop |
| 1 | 416 | 41 / 6 | 6 | 90 | set_switch(15); stop |
| 2 | 401 | 40 / 1 | 3 | 1 | trigger_event(402); stop |
| 2 | 402 | 40 / 2 | 7 | 60 | trigger_event(403); stop |
| 2 | 403 | 40 / 3 | 8 | 60 | trigger_event(404); stop |
| 2 | 404 | 40 / 4 | 8 | 60 | trigger_event(406); stop |
| 2 | 406 | 40 / 6 | 11 | 60 | trigger_event(405); stop |
| 2 | 405 | 40 / 5 | 8 | 60 | set_switch(1); trigger_event(111); stop |
| 2 | 111 | 11 / 1 | 2 | 1 | trigger_event(112); stop |
| 2 | 112 | 11 / 2 | 4 | 60 | trigger_event(113); stop |
| 2 | 113 | 11 / 3 | 7 | 60 | trigger_event(114); stop |
| 2 | 114 | 11 / 4 | 3 | 60 | set_switch(2); stop |
| 2 | 961 | 96 / 1 | 2 | 90 | trigger_event(962); stop |
| 2 | 962 | 96 / 2 | 5 | 30 | set_switch(3); stop |
| 2 | 921 | 92 / 1 | 3 | 30 | trigger_event(922); stop |
| 2 | 922 | 92 / 2 | 3 | 60 | set_switch(4); stop |
| 2 | 981 | 98 / 1 | 3 | 90 | set_switch(5); set_switch(120); trigger_event(501); stop |
| 2 | 501 | 50 / 1 | 2 | 1 | trigger_event(502); stop |
| 2 | 502 | 50 / 2 | 8 | 30 | trigger_event(503); stop |
| 2 | 503 | 50 / 3 | 8 | 30 | trigger_event(504); stop |
| 2 | 504 | 50 / 4 | 7 | 30 | trigger_event(505); stop |
| 2 | 505 | 50 / 5 | 7 | 90 | set_switch(6); stop |
| 2 | 801 | 80 / 1 | 9 | 90 | construct_objects(room=80,group_or_wave=1); set_switch(7); set_switch(102); stop |
| 2 | 971 | 97 / 1 | 3 | 60 | trigger_event(972); stop |
| 2 | 972 | 97 / 2 | 5 | 60 | set_switch(8); stop |
| 2 | 931 | 93 / 1 | 4 | 60 | set_switch(16); stop |
| 2 | 941 | 94 / 1 | 3 | 60 | set_switch(9); stop |
| 2 | 701 | 70 / 1 | 8 | 1 | trigger_event(702); stop |
| 2 | 702 | 70 / 2 | 5 | 60 | trigger_event(703); stop |
| 2 | 703 | 70 / 3 | 6 | 60 | trigger_event(704); stop |
| 2 | 704 | 70 / 4 | 8 | 60 | set_switch(10); stop |
| 2 | 301 | 30 / 1 | 4 | 60 | trigger_event(302); stop |
| 2 | 302 | 30 / 2 | 5 | 60 | set_switch(11); stop |
| 2 | 601 | 60 / 1 | 2 | 60 | set_switch(104); stop |
| 2 | 602 | 60 / 2 | 5 | 30 | set_switch(105); stop |
| 2 | 603 | 60 / 3 | 4 | 30 | trigger_event(604); stop |
| 2 | 604 | 60 / 4 | 6 | 60 | set_switch(12); stop |
| 2 | 101 | 10 / 1 | 8 | 30 | trigger_event(102); stop |
| 2 | 102 | 10 / 2 | 8 | 60 | set_switch(13); stop |
| 2 | 201 | 20 / 1 | 4 | 30 | set_switch(14); stop |
| 2 | 705 | 70 / 5 | 5 | 120 | trigger_event(706); stop |
| 2 | 706 | 70 / 6 | 6 | 60 | trigger_event(707); stop |
| 2 | 707 | 70 / 7 | 6 | 120 | set_switch(15); stop |
| 14 | 11 | 1 / 1 | 1 | 50 | construct_objects(room=1,group_or_wave=1); stop |

## Review notes

- Nonzero data after terminal header
