# Lost BIND ASSAULT — retrieval-ep2/q154-bb-e

Episode2; header quest ID 154; language E. Static scan: **372 objects, 425 enemy/NPC records, 78 events, 51 script labels.** Script roundtrip: alignment-only.

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
| 3 | 161 | 202 | 39 |
| 4 | 143 | 214 | 38 |
| 15 | 30 | 1 | 1 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 3 | 521 | 52 / 1 | 5 | 30 | trigger_event(522); stop |
| 3 | 522 | 52 / 2 | 8 | 60 | trigger_event(523); stop |
| 3 | 523 | 52 / 3 | 6 | 60 | trigger_event(524); stop |
| 3 | 524 | 52 / 4 | 2 | 30 | set_switch(1); stop |
| 3 | 201 | 20 / 1 | 5 | 1 | trigger_event(202); stop |
| 3 | 202 | 20 / 2 | 8 | 30 | set_switch(2); stop |
| 3 | 421 | 42 / 1 | 2 | 1 | trigger_event(422); stop |
| 3 | 422 | 42 / 2 | 5 | 60 | set_switch(3); trigger_event(321); stop |
| 3 | 321 | 32 / 1 | 2 | 60 | trigger_event(322); stop |
| 3 | 322 | 32 / 2 | 7 | 30 | set_switch(4); stop |
| 3 | 423 | 42 / 3 | 4 | 1 | trigger_event(424); stop |
| 3 | 424 | 42 / 4 | 6 | 30 | trigger_event(425); stop |
| 3 | 425 | 42 / 5 | 6 | 60 | set_switch(5); stop |
| 3 | 101 | 10 / 1 | 7 | 60 | set_switch(6); stop |
| 3 | 511 | 51 / 1 | 6 | 1 | trigger_event(512); stop |
| 3 | 512 | 51 / 2 | 10 | 60 | trigger_event(513); stop |
| 3 | 513 | 51 / 3 | 3 | 60 | set_switch(7); stop |
| 3 | 411 | 41 / 1 | 3 | 60 | trigger_event(412); stop |
| 3 | 412 | 41 / 2 | 7 | 60 | trigger_event(413); stop |
| 3 | 413 | 41 / 3 | 4 | 60 | set_switch(8); stop |
| 3 | 501 | 50 / 1 | 5 | 30 | trigger_event(502); stop |
| 3 | 502 | 50 / 2 | 3 | 60 | trigger_event(503); stop |
| 3 | 503 | 50 / 3 | 7 | 60 | trigger_event(504); stop |
| 3 | 504 | 50 / 4 | 5 | 60 | trigger_event(505); stop |
| 3 | 505 | 50 / 5 | 5 | 60 | set_switch(9); trigger_event(1921); stop |
| 3 | 1921 | 192 / 1 | 1 | 60 | stop |
| 3 | 1922 | 192 / 2 | 1 | 30 | stop |
| 3 | 401 | 40 / 1 | 4 | 30 | trigger_event(402); stop |
| 3 | 402 | 40 / 2 | 9 | 30 | trigger_event(403); stop |
| 3 | 403 | 40 / 3 | 7 | 60 | trigger_event(404); stop |
| 3 | 404 | 40 / 4 | 3 | 60 | set_switch(10); stop |
| 3 | 301 | 30 / 1 | 6 | 30 | set_switch(11); stop |
| 3 | 311 | 31 / 1 | 4 | 90 | construct_objects(room=31,group_or_wave=1); stop |
| 3 | 111 | 11 / 1 | 3 | 30 | trigger_event(112); stop |
| 3 | 112 | 11 / 2 | 4 | 30 | trigger_event(113); stop |
| 3 | 113 | 11 / 3 | 7 | 60 | set_switch(12); stop |
| 3 | 211 | 21 / 1 | 5 | 60 | trigger_event(212); stop |
| 3 | 212 | 21 / 2 | 8 | 60 | trigger_event(213); stop |
| 3 | 213 | 21 / 3 | 9 | 60 | set_switch(13); stop |
| 4 | 301 | 30 / 1 | 5 | 30 | trigger_event(302); stop |
| 4 | 302 | 30 / 2 | 7 | 30 | trigger_event(303); stop |
| 4 | 303 | 30 / 3 | 2 | 30 | set_switch(1); stop |
| 4 | 421 | 42 / 1 | 3 | 1 | trigger_event(422); stop |
| 4 | 422 | 42 / 2 | 2 | 60 | trigger_event(423); stop |
| 4 | 423 | 42 / 3 | 2 | 60 | set_switch(100); trigger_event(424); stop |
| 4 | 424 | 42 / 4 | 8 | 60 | trigger_event(425); stop |
| 4 | 425 | 42 / 5 | 10 | 60 | trigger_event(426); stop |
| 4 | 426 | 42 / 6 | 11 | 0 | set_switch(101); set_switch(2); stop |
| 4 | 501 | 50 / 1 | 4 | 60 | trigger_event(502); stop |
| 4 | 502 | 50 / 2 | 8 | 60 | trigger_event(503); stop |
| 4 | 503 | 50 / 3 | 7 | 60 | set_switch(3); stop |
| 4 | 401 | 40 / 1 | 8 | 90 | trigger_event(402); stop |
| 4 | 402 | 40 / 2 | 8 | 60 | trigger_event(403); stop |
| 4 | 403 | 40 / 3 | 5 | 60 | set_switch(4); stop |
| 4 | 201 | 20 / 1 | 1 | 90 | trigger_event(202); stop |
| 4 | 202 | 20 / 2 | 3 | 30 | trigger_event(203); stop |
| 4 | 203 | 20 / 3 | 5 | 30 | set_switch(5); stop |
| 4 | 111 | 11 / 1 | 2 | 60 | trigger_event(112); stop |
| 4 | 112 | 11 / 2 | 7 | 60 | set_switch(6); stop |
| 4 | 511 | 51 / 1 | 6 | 30 | trigger_event(512); stop |
| 4 | 512 | 51 / 2 | 6 | 60 | trigger_event(513); stop |
| 4 | 513 | 51 / 3 | 4 | 30 | set_switch(7); stop |
| 4 | 331 | 33 / 1 | 5 | 60 | trigger_event(332); stop |
| 4 | 332 | 33 / 2 | 9 | 60 | construct_objects(room=33,group_or_wave=1); stop |
| 4 | 411 | 41 / 1 | 3 | 30 | trigger_event(412); stop |
| 4 | 412 | 41 / 2 | 4 | 30 | trigger_event(413); stop |
| 4 | 413 | 41 / 3 | 8 | 60 | set_switch(8); stop |
| 4 | 101 | 10 / 1 | 5 | 60 | set_switch(9); stop |
| 4 | 321 | 32 / 1 | 3 | 30 | set_switch(10); stop |
| 4 | 211 | 21 / 1 | 6 | 1 | trigger_event(212); stop |
| 4 | 212 | 21 / 2 | 4 | 30 | set_switch(11); stop |
| 4 | 525 | 52 / 5 | 7 | 90 | construct_objects(room=52,group_or_wave=1); stop |
| 4 | 521 | 52 / 1 | 5 | 60 | trigger_event(522); set_switch(221); stop |
| 4 | 522 | 52 / 2 | 6 | 60 | trigger_event(523); stop |
| 4 | 523 | 52 / 3 | 11 | 60 | set_switch(12); stop |
| 4 | 311 | 31 / 1 | 6 | 10 | trigger_event(312); stop |
| 4 | 312 | 31 / 2 | 8 | 60 | set_switch(13); stop |
| 15 | 1 | 1 / 1 | 1 | 50 | construct_objects(room=1,group_or_wave=1); stop |

## Review notes

- Nonzero data after terminal header
