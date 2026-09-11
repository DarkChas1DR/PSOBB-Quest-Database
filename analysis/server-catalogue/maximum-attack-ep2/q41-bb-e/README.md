# Maximum Attack E -VR- — maximum-attack-ep2/q41-bb-e

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/maximum-attack-ep2/q41-bb-e.zip?download=1)**

[Original QST](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/maximum-attack-ep2/q41-bb-e.qst?download=1) · [Extracted BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/maximum-attack-ep2/q41-bb-e/q41-bb-e.qst-quest0.bin?download=1) · [Extracted DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/maximum-attack-ep2/q41-bb-e/q41-bb-e.qst-quest0.dat?download=1)

QST is the preserved original package. BIN and DAT are its decoded payload files, not reassembled scripts. The ZIP contains all three formats.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 41; language E. Static scan: **166 objects, 353 enemy/NPC records, 68 events, 44 script labels.** Script roundtrip: byte-identical.

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
| 0 | 41 | 8 | 0 |
| 1 | 39 | 174 | 30 |
| 3 | 26 | 169 | 36 |
| 14 | 30 | 1 | 1 |
| 15 | 30 | 1 | 1 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 101 | 10 / 1 | 5 | 20 | trigger_event(102); stop |
| 1 | 102 | 10 / 2 | 5 | 20 | trigger_event(103); stop |
| 1 | 103 | 10 / 3 | 6 | 20 | trigger_event(104); stop |
| 1 | 104 | 10 / 4 | 6 | 20 | trigger_event(105); stop |
| 1 | 105 | 10 / 5 | 6 | 20 | trigger_event(106); stop |
| 1 | 106 | 10 / 6 | 5 | 20 | set_switch(1); stop |
| 1 | 401 | 40 / 1 | 3 | 20 | trigger_event(402); stop |
| 1 | 402 | 40 / 2 | 7 | 20 | trigger_event(403); stop |
| 1 | 403 | 40 / 3 | 6 | 20 | trigger_event(404); stop |
| 1 | 404 | 40 / 4 | 5 | 20 | trigger_event(405); stop |
| 1 | 405 | 40 / 5 | 10 | 20 | trigger_event(406); stop |
| 1 | 406 | 40 / 6 | 7 | 20 | trigger_event(407); stop |
| 1 | 407 | 40 / 7 | 5 | 20 | set_switch(2); stop |
| 1 | 411 | 41 / 1 | 4 | 20 | trigger_event(412); stop |
| 1 | 412 | 41 / 2 | 6 | 20 | trigger_event(413); stop |
| 1 | 413 | 41 / 3 | 6 | 20 | trigger_event(414); stop |
| 1 | 414 | 41 / 4 | 7 | 20 | trigger_event(415); stop |
| 1 | 415 | 41 / 5 | 10 | 20 | trigger_event(416); stop |
| 1 | 416 | 41 / 6 | 10 | 20 | trigger_event(417); stop |
| 1 | 417 | 41 / 7 | 5 | 20 | set_switch(3); stop |
| 1 | 601 | 60 / 1 | 4 | 20 | trigger_event(602); stop |
| 1 | 602 | 60 / 2 | 4 | 20 | trigger_event(603); stop |
| 1 | 603 | 60 / 3 | 6 | 20 | trigger_event(604); stop |
| 1 | 604 | 60 / 4 | 3 | 20 | trigger_event(605); stop |
| 1 | 605 | 60 / 5 | 5 | 20 | trigger_event(606); stop |
| 1 | 606 | 60 / 6 | 6 | 20 | trigger_event(607); stop |
| 1 | 607 | 60 / 7 | 6 | 20 | trigger_event(608); stop |
| 1 | 608 | 60 / 8 | 8 | 20 | trigger_event(609); stop |
| 1 | 609 | 60 / 9 | 4 | 20 | trigger_event(6010); stop |
| 1 | 6010 | 60 / 10 | 4 | 20 | set_switch(4); stop |
| 3 | 111 | 11 / 1 | 3 | 20 | trigger_event(112); stop |
| 3 | 112 | 11 / 2 | 6 | 20 | trigger_event(113); stop |
| 3 | 113 | 11 / 3 | 4 | 20 | trigger_event(114); stop |
| 3 | 114 | 11 / 4 | 5 | 20 | trigger_event(115); stop |
| 3 | 115 | 11 / 5 | 3 | 20 | trigger_event(116); stop |
| 3 | 116 | 11 / 6 | 6 | 20 | trigger_event(117); stop |
| 3 | 117 | 11 / 7 | 9 | 20 | trigger_event(118); stop |
| 3 | 118 | 11 / 8 | 3 | 20 | set_switch(3); stop |
| 3 | 311 | 31 / 1 | 5 | 20 | trigger_event(312); stop |
| 3 | 312 | 31 / 2 | 5 | 20 | trigger_event(313); stop |
| 3 | 313 | 31 / 3 | 4 | 20 | trigger_event(314); stop |
| 3 | 314 | 31 / 4 | 2 | 20 | trigger_event(315); stop |
| 3 | 315 | 31 / 5 | 5 | 20 | trigger_event(316); stop |
| 3 | 316 | 31 / 6 | 6 | 20 | trigger_event(317); stop |
| 3 | 317 | 31 / 7 | 3 | 20 | trigger_event(318); stop |
| 3 | 318 | 31 / 8 | 7 | 20 | trigger_event(319); stop |
| 3 | 319 | 31 / 9 | 4 | 20 | set_switch(1); stop |
| 3 | 411 | 41 / 1 | 2 | 20 | trigger_event(412); stop |
| 3 | 412 | 41 / 2 | 2 | 20 | trigger_event(413); stop |
| 3 | 413 | 41 / 3 | 3 | 20 | trigger_event(414); stop |
| 3 | 414 | 41 / 4 | 5 | 20 | trigger_event(415); stop |
| 3 | 415 | 41 / 5 | 6 | 20 | trigger_event(416); stop |
| 3 | 416 | 41 / 6 | 5 | 20 | trigger_event(417); stop |
| 3 | 417 | 41 / 7 | 3 | 20 | trigger_event(418); stop |
| 3 | 418 | 41 / 8 | 6 | 20 | trigger_event(419); stop |
| 3 | 419 | 41 / 9 | 7 | 20 | trigger_event(4010); stop |
| 3 | 4010 | 41 / 10 | 6 | 20 | trigger_event(4011); stop |
| 3 | 4011 | 41 / 11 | 6 | 20 | trigger_event(4012); stop |
| 3 | 4012 | 41 / 12 | 10 | 20 | trigger_event(4013); stop |
| 3 | 4013 | 41 / 13 | 4 | 20 | set_switch(4); stop |
| 3 | 501 | 50 / 1 | 3 | 20 | trigger_event(502); stop |
| 3 | 502 | 50 / 2 | 5 | 20 | trigger_event(503); stop |
| 3 | 503 | 50 / 3 | 6 | 20 | trigger_event(504); stop |
| 3 | 504 | 50 / 4 | 2 | 20 | trigger_event(505); stop |
| 3 | 505 | 50 / 5 | 3 | 20 | trigger_event(507); stop |
| 3 | 507 | 50 / 7 | 5 | 20 | set_switch(2); stop |
| 14 | 1 | 1 / 1 | 1 | 50 | construct_objects(room=1,group_or_wave=1); stop |
| 15 | 1 | 1 / 1 | 1 | 50 | construct_objects(room=1,group_or_wave=1); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
