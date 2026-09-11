# ９－１：調査部隊を追って — government-ep4/q701-bb-j

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/government-ep4/q701-bb-j.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep4/q701-bb-j.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep4/q701-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode4; header quest ID 701; language J. Static scan: **293 objects, 261 enemy/NPC records, 46 events, 166 script labels.** Script roundtrip: byte-identical.

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
| 0 | 27 | 21 | 0 |
| 1 | 266 | 240 | 46 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 101 | 10 / 1 | 3 | 10 | trigger_event(102); stop |
| 1 | 102 | 10 / 2 | 4 | 10 | trigger_event(103); stop |
| 1 | 103 | 10 / 3 | 4 | 10 | set_switch(10); stop |
| 1 | 111 | 11 / 1 | 4 | 10 | trigger_event(112); stop |
| 1 | 112 | 11 / 2 | 4 | 10 | trigger_event(113); stop |
| 1 | 113 | 11 / 3 | 4 | 10 | set_switch(11); stop |
| 1 | 801 | 80 / 1 | 6 | 10 | construct_objects(room=80,group_or_wave=1); stop |
| 1 | 802 | 80 / 2 | 6 | 120 | trigger_event(803); stop |
| 1 | 803 | 80 / 3 | 2 | 10 | set_switch(80); stop |
| 1 | 201 | 20 / 1 | 3 | 10 | trigger_event(202); stop |
| 1 | 202 | 20 / 2 | 4 | 10 | trigger_event(203); stop |
| 1 | 203 | 20 / 3 | 3 | 60 | trigger_event(204); stop |
| 1 | 204 | 20 / 4 | 4 | 10 | trigger_event(205); stop |
| 1 | 205 | 20 / 5 | 5 | 10 | trigger_event(206); stop |
| 1 | 206 | 20 / 6 | 9 | 90 | set_switch(20); stop |
| 1 | 211 | 21 / 1 | 5 | 10 | trigger_event(212); stop |
| 1 | 212 | 21 / 2 | 6 | 10 | trigger_event(213); stop |
| 1 | 213 | 21 / 3 | 10 | 10 | trigger_event(214); stop |
| 1 | 214 | 21 / 4 | 9 | 10 | set_switch(21); stop |
| 1 | 301 | 10 / 1 | 3 | 10 | trigger_event(302); stop |
| 1 | 302 | 30 / 2 | 6 | 10 | construct_objects(room=30,group_or_wave=2); stop |
| 1 | 303 | 30 / 3 | 6 | 10 | trigger_event(304); stop |
| 1 | 304 | 30 / 4 | 4 | 10 | trigger_event(305); stop |
| 1 | 305 | 30 / 5 | 6 | 10 | trigger_event(306); stop |
| 1 | 306 | 30 / 6 | 7 | 10 | set_switch(30); stop |
| 1 | 401 | 40 / 1 | 4 | 30 | trigger_event(402); stop |
| 1 | 402 | 40 / 2 | 5 | 10 | trigger_event(403); stop |
| 1 | 403 | 40 / 3 | 6 | 10 | set_switch(41); construct_objects(room=40,group_or_wave=3); stop |
| 1 | 404 | 40 / 4 | 5 | 10 | trigger_event(405); stop |
| 1 | 405 | 40 / 5 | 5 | 10 | trigger_event(406); stop |
| 1 | 406 | 40 / 6 | 4 | 10 | set_switch(40); stop |
| 1 | 501 | 50 / 1 | 1 | 10 | trigger_event(502); stop |
| 1 | 502 | 50 / 2 | 2 | 10 | trigger_event(503); stop |
| 1 | 503 | 50 / 3 | 3 | 10 | trigger_event(504); stop |
| 1 | 504 | 50 / 4 | 4 | 60 | trigger_event(505); stop |
| 1 | 505 | 50 / 5 | 5 | 10 | trigger_event(506); stop |
| 1 | 506 | 50 / 6 | 6 | 60 | set_switch(51); construct_objects(room=50,group_or_wave=6); stop |
| 1 | 507 | 50 / 7 | 4 | 10 | trigger_event(508); stop |
| 1 | 508 | 50 / 8 | 3 | 10 | construct_objects(room=50,group_or_wave=8); stop |
| 1 | 509 | 50 / 9 | 5 | 90 | trigger_event(510); stop |
| 1 | 510 | 50 / 10 | 5 | 10 | set_switch(50); stop |
| 1 | 601 | 60 / 1 | 6 | 10 | construct_objects(room=60,group_or_wave=1); stop |
| 1 | 602 | 60 / 2 | 6 | 10 | construct_objects(room=60,group_or_wave=2); stop |
| 1 | 603 | 60 / 3 | 10 | 10 | trigger_event(604); stop |
| 1 | 604 | 60 / 4 | 5 | 90 | trigger_event(605); stop |
| 1 | 605 | 60 / 5 | 9 | 180 | set_switch(60); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
