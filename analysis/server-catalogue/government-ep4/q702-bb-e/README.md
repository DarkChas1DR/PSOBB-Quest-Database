# 9-2:Data Retrieval — government-ep4/q702-bb-e

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/government-ep4/q702-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep4/q702-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep4/q702-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode4; header quest ID 702; language E. Static scan: **312 objects, 227 enemy/NPC records, 37 events, 233 script labels.** Script roundtrip: byte-identical.

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
0x02, 0x25, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 27 | 20 | 0 |
| 2 | 285 | 207 | 37 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 2 | 101 | 10 / 1 | 6 | 10 | construct_objects(room=10,group_or_wave=2); stop |
| 2 | 102 | 10 / 2 | 7 | 10 | trigger_event(103); stop |
| 2 | 103 | 10 / 3 | 2 | 90 | set_switch(10); stop |
| 2 | 201 | 20 / 1 | 8 | 10 | trigger_event(2011); stop |
| 2 | 2011 | 20 / 2 | 8 | 10 | trigger_event(2012); stop |
| 2 | 2012 | 20 / 3 | 8 | 10 | trigger_event(2013); stop |
| 2 | 2013 | 20 / 4 | 5 | 10 | trigger_event(2014); stop |
| 2 | 2014 | 20 / 5 | 7 | 10 | trigger_event(2015); stop |
| 2 | 2015 | 20 / 6 | 10 | 90 | trigger_event(2016); stop |
| 2 | 2016 | 20 / 7 | 3 | 90 | trigger_event(2017); stop |
| 2 | 2017 | 20 / 8 | 2 | 150 | set_switch(21); stop |
| 2 | 301 | 30 / 1 | 5 | 210 | trigger_event(302); stop |
| 2 | 302 | 30 / 2 | 5 | 10 | trigger_event(303); stop |
| 2 | 303 | 30 / 3 | 3 | 10 | set_switch(31); construct_objects(room=30,group_or_wave=4); stop |
| 2 | 304 | 30 / 4 | 3 | 10 | trigger_event(305); stop |
| 2 | 305 | 30 / 5 | 8 | 90 | construct_objects(room=30,group_or_wave=6); stop |
| 2 | 306 | 30 / 6 | 7 | 10 | trigger_event(307); stop |
| 2 | 307 | 30 / 7 | 7 | 90 | set_switch(30); stop |
| 2 | 401 | 40 / 1 | 6 | 10 | trigger_event(402); stop |
| 2 | 402 | 40 / 2 | 6 | 10 | construct_objects(room=40,group_or_wave=3); stop |
| 2 | 403 | 40 / 3 | 6 | 10 | set_switch(41); construct_objects(room=40,group_or_wave=4); stop |
| 2 | 404 | 40 / 4 | 2 | 10 | construct_objects(room=40,group_or_wave=5); stop |
| 2 | 405 | 40 / 5 | 6 | 10 | trigger_event(406); stop |
| 2 | 406 | 40 / 6 | 5 | 10 | set_switch(42); stop |
| 2 | 501 | 50 / 1 | 6 | 10 | construct_objects(room=50,group_or_wave=2); stop |
| 2 | 502 | 50 / 2 | 6 | 10 | construct_objects(room=50,group_or_wave=3); stop |
| 2 | 503 | 50 / 3 | 6 | 10 | set_switch(51); construct_objects(room=50,group_or_wave=4); stop |
| 2 | 504 | 50 / 4 | 3 | 10 | construct_objects(room=50,group_or_wave=5); stop |
| 2 | 505 | 50 / 5 | 8 | 10 | construct_objects(room=50,group_or_wave=6); stop |
| 2 | 506 | 50 / 6 | 6 | 10 | construct_objects(room=50,group_or_wave=7); stop |
| 2 | 507 | 50 / 7 | 5 | 10 | construct_objects(room=50,group_or_wave=8); stop |
| 2 | 508 | 50 / 8 | 4 | 10 | set_switch(50); stop |
| 2 | 601 | 60 / 1 | 4 | 10 | trigger_event(602); stop |
| 2 | 602 | 60 / 2 | 5 | 10 | trigger_event(603); stop |
| 2 | 603 | 60 / 3 | 6 | 10 | trigger_event(604); stop |
| 2 | 604 | 60 / 4 | 4 | 10 | trigger_event(605); stop |
| 2 | 605 | 60 / 5 | 5 | 10 | set_switch(60); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
