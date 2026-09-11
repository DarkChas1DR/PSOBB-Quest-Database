# Lost DEVIL\'S SCEPTER — retrieval-ep2/q54-bb-j

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/retrieval-ep2/q54-bb-j.zip?download=1)**

[Original QST](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/retrieval-ep2/q54-bb-j.qst?download=1) · [Extracted BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/retrieval-ep2/q54-bb-j/q54-bb-j.qst-quest0.bin?download=1) · [Extracted DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/retrieval-ep2/q54-bb-j/q54-bb-j.qst-quest0.dat?download=1)

QST is the preserved original package. BIN and DAT are its decoded payload files, not reassembled scripts. The ZIP contains all three formats.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 54; language J. Static scan: **696 objects, 663 enemy/NPC records, 142 events, 60 script labels.** Script roundtrip: alignment-only.

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
| 0 | 54 | 17 | 0 |
| 5 | 72 | 158 | 33 |
| 6 | 104 | 99 | 33 |
| 7 | 97 | 98 | 24 |
| 8 | 243 | 144 | 28 |
| 9 | 104 | 146 | 23 |
| 12 | 22 | 1 | 1 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 5 | 21 | 2 / 1 | 8 | 10 | trigger_event(2110); stop |
| 5 | 2110 | 2 / 2 | 8 | 10 | trigger_event(2111); stop |
| 5 | 2111 | 2 / 3 | 10 | 10 | trigger_event(2112); stop |
| 5 | 2112 | 2 / 4 | 2 | 10 | trigger_event(2113); stop |
| 5 | 2113 | 2 / 5 | 2 | 10 | trigger_event(2114); stop |
| 5 | 2114 | 2 / 6 | 2 | 10 | trigger_event(2115); stop |
| 5 | 2115 | 2 / 7 | 3 | 10 | set_switch(2); stop |
| 5 | 31 | 3 / 1 | 8 | 10 | trigger_event(3110); stop |
| 5 | 3110 | 3 / 2 | 8 | 10 | trigger_event(3111); stop |
| 5 | 3111 | 3 / 2 | 8 | 10 | trigger_event(3112); stop |
| 5 | 3112 | 3 / 3 | 10 | 10 | trigger_event(3113); stop |
| 5 | 3113 | 3 / 4 | 5 | 10 | trigger_event(3114); stop |
| 5 | 3114 | 3 / 5 | 4 | 10 | set_switch(3); stop |
| 5 | 41 | 4 / 1 | 8 | 10 | trigger_event(4110); stop |
| 5 | 4110 | 4 / 2 | 8 | 10 | trigger_event(4111); stop |
| 5 | 4111 | 4 / 3 | 10 | 10 | trigger_event(4112); stop |
| 5 | 4112 | 4 / 4 | 5 | 10 | trigger_event(4113); stop |
| 5 | 4113 | 4 / 5 | 4 | 10 | set_switch(4); stop |
| 5 | 51 | 5 / 1 | 4 | 10 | trigger_event(5110); stop |
| 5 | 5110 | 5 / 2 | 5 | 10 | trigger_event(5111); stop |
| 5 | 5111 | 5 / 3 | 4 | 10 | trigger_event(5112); stop |
| 5 | 5112 | 5 / 4 | 5 | 10 | trigger_event(5113); stop |
| 5 | 5113 | 5 / 5 | 6 | 10 | construct_objects(room=5,group_or_wave=1); stop |
| 5 | 9 | 9 / 1 | 3 | 10 | trigger_event(910); stop |
| 5 | 910 | 9 / 2 | 3 | 10 | trigger_event(911); stop |
| 5 | 911 | 9 / 3 | 2 | 10 | set_switch(7); set_switch(8); stop |
| 5 | 10 | 10 / 1 | 3 | 10 | trigger_event(1010); stop |
| 5 | 1010 | 10 / 2 | 3 | 10 | trigger_event(1011); stop |
| 5 | 1011 | 10 / 3 | 3 | 10 | trigger_event(1012); stop |
| 5 | 1012 | 10 / 4 | 3 | 10 | construct_objects(room=10,group_or_wave=1); stop |
| 5 | 11 | 11 / 1 | 3 | 180 | construct_objects(room=11,group_or_wave=1); stop |
| 5 | 12 | 12 / 1 | 3 | 60 | construct_objects(room=12,group_or_wave=1); stop |
| 5 | 13 | 13 / 1 | 3 | 30 | construct_objects(room=13,group_or_wave=1); stop |
| 6 | 11 | 1 / 1 | 5 | 10 | construct_objects(room=1,group_or_wave=1); stop |
| 6 | 111 | 11 / 1 | 5 | 10 | trigger_event(112); stop |
| 6 | 112 | 11 / 2 | 8 | 10 | trigger_event(113); stop |
| 6 | 113 | 11 / 3 | 1 | 10 | trigger_event(114); stop |
| 6 | 114 | 11 / 4 | 6 | 10 | trigger_event(115); stop |
| 6 | 115 | 11 / 5 | 8 | 10 | trigger_event(116); stop |
| 6 | 116 | 11 / 6 | 2 | 10 | set_switch(40); stop |
| 6 | 13 | 13 / 1 | 4 | 10 | trigger_event(131); stop |
| 6 | 131 | 13 / 2 | 1 | 10 | set_switch(3); stop |
| 6 | 132 | 13 / 3 | 0 | 0 | construct_objects(room=13,group_or_wave=1); trigger_event(1321); stop |
| 6 | 1321 | 13 / 4 | 3 | 0 | set_switch(20); stop |
| 6 | 31 | 3 / 1 | 6 | 10 | trigger_event(311); stop |
| 6 | 311 | 3 / 2 | 1 | 10 | trigger_event(312); stop |
| 6 | 312 | 3 / 3 | 8 | 10 | trigger_event(314); stop |
| 6 | 314 | 3 / 4 | 6 | 10 | set_switch(13); stop |
| 6 | 32 | 3 / 4 | 6 | 100 | trigger_event(321); stop |
| 6 | 321 | 3 / 5 | 0 | 1 | stop |
| 6 | 41 | 4 / 1 | 3 | 10 | trigger_event(411); stop |
| 6 | 411 | 4 / 2 | 6 | 10 | trigger_event(412); stop |
| 6 | 412 | 4 / 3 | 1 | 10 | trigger_event(413); stop |
| 6 | 413 | 4 / 4 | 6 | 10 | trigger_event(414); stop |
| 6 | 414 | 4 / 5 | 7 | 10 | trigger_event(415); stop |
| 6 | 415 | 4 / 6 | 3 | 10 | construct_objects(room=4,group_or_wave=1); set_switch(11); stop |
| 6 | 42 | 4 / 7 | 1 | 0 | stop |
| 6 | 61 | 6 / 1 | 4 | 10 | stop |
| 6 | 81 | 8 / 1 | 1 | 0 | stop |
| 6 | 121 | 12 / 1 | 0 | 1 | stop |
| 6 | 141 | 14 / 1 | 1 | 0 | stop |
| 6 | 142 | 14 / 2 | 1 | 0 | stop |
| 6 | 151 | 15 / 1 | 1 | 0 | construct_objects(room=15,group_or_wave=1); stop |
| 6 | 152 | 15 / 4 | 0 | 150 | stop |
| 6 | 1531 | 15 / 6 | 0 | 100 | trigger_event(1532); stop |
| 6 | 1532 | 15 / 7 | 0 | 100 | stop |
| 7 | 11 | 1 / 1 | 0 | 1 | set_switch(2); stop |
| 7 | 21 | 2 / 1 | 8 | 10 | trigger_event(211); stop |
| 7 | 211 | 2 / 2 | 6 | 10 | trigger_event(212); stop |
| 7 | 212 | 2 / 3 | 3 | 10 | trigger_event(213); stop |
| 7 | 213 | 2 / 4 | 1 | 10 | set_switch(3); stop |
| 7 | 31 | 3 / 1 | 6 | 10 | trigger_event(312); stop |
| 7 | 312 | 3 / 2 | 6 | 10 | trigger_event(313); stop |
| 7 | 313 | 3 / 3 | 7 | 10 | trigger_event(314); stop |
| 7 | 314 | 3 / 4 | 1 | 10 | set_switch(4); set_switch(5); stop |
| 7 | 41 | 4 / 1 | 0 | 0 | construct_objects(room=4,group_or_wave=1); stop |
| 7 | 42 | 4 / 2 | 0 | 1 | stop |
| 7 | 51 | 5 / 1 | 5 | 10 | trigger_event(511); stop |
| 7 | 511 | 5 / 2 | 3 | 10 | trigger_event(512); stop |
| 7 | 512 | 5 / 3 | 5 | 10 | trigger_event(513); stop |
| 7 | 513 | 5 / 4 | 2 | 10 | trigger_event(514); stop |
| 7 | 514 | 5 / 5 | 8 | 10 | trigger_event(515); stop |
| 7 | 515 | 5 / 6 | 2 | 10 | trigger_event(516); stop |
| 7 | 516 | 5 / 7 | 6 | 10 | trigger_event(517); stop |
| 7 | 517 | 5 / 8 | 3 | 10 | set_switch(6); stop |
| 7 | 71 | 7 / 1 | 6 | 5 | trigger_event(711); stop |
| 7 | 711 | 7 / 2 | 10 | 10 | trigger_event(712); stop |
| 7 | 712 | 7 / 3 | 4 | 10 | trigger_event(713); stop |
| 7 | 713 | 7 / 4 | 1 | 10 | construct_objects(room=7,group_or_wave=1); set_switch(1); stop |
| 7 | 81 | 8 / 1 | 5 | 10 | construct_objects(room=8,group_or_wave=1); stop |
| 8 | 21 | 2 / 1 | 5 | 180 | trigger_event(211); stop |
| 8 | 211 | 2 / 2 | 5 | 10 | set_switch(1); set_switch(103); set_switch(104); set_switch(105); stop |
| 8 | 31 | 3 / 1 | 10 | 10 | trigger_event(311); stop |
| 8 | 311 | 3 / 2 | 9 | 10 | set_switch(204); stop |
| 8 | 32 | 3 / 3 | 6 | 10 | trigger_event(312); stop |
| 8 | 312 | 3 / 4 | 3 | 10 | set_switch(205); stop |
| 8 | 33 | 3 / 5 | 2 | 0 | stop |
| 8 | 41 | 4 / 1 | 7 | 10 | trigger_event(411); stop |
| 8 | 411 | 4 / 2 | 6 | 10 | set_switch(202); stop |
| 8 | 42 | 4 / 3 | 0 | 0 | construct_objects(room=4,group_or_wave=1); stop |
| 8 | 43 | 4 / 4 | 3 | 10 | stop |
| 8 | 51 | 5 / 1 | 7 | 10 | trigger_event(511); stop |
| 8 | 511 | 5 / 2 | 5 | 10 | trigger_event(512); stop |
| 8 | 512 | 5 / 3 | 5 | 10 | trigger_event(513); stop |
| 8 | 513 | 5 / 4 | 5 | 10 | trigger_event(514); stop |
| 8 | 514 | 5 / 5 | 2 | 10 | set_switch(11); stop |
| 8 | 71 | 7 / 1 | 1 | 1 | stop |
| 8 | 81 | 8 / 1 | 5 | 10 | trigger_event(811); stop |
| 8 | 811 | 8 / 2 | 5 | 10 | trigger_event(812); stop |
| 8 | 812 | 8 / 3 | 10 | 10 | trigger_event(813); stop |
| 8 | 813 | 8 / 4 | 1 | 10 | set_switch(201); stop |
| 8 | 82 | 8 / 5 | 7 | 10 | trigger_event(821); stop |
| 8 | 821 | 8 / 6 | 6 | 10 | trigger_event(822); stop |
| 8 | 822 | 8 / 7 | 7 | 10 | set_switch(14); stop |
| 8 | 83 | 8 / 8 | 12 | 10 | trigger_event(831); stop |
| 8 | 831 | 8 / 9 | 3 | 10 | set_switch(13); stop |
| 8 | 101 | 10 / 1 | 3 | 10 | trigger_event(1011); stop |
| 8 | 1011 | 10 / 2 | 4 | 10 | set_switch(206); stop |
| 9 | 31 | 3 / 1 | 8 | 10 | trigger_event(311); stop |
| 9 | 311 | 3 / 2 | 8 | 10 | trigger_event(312); stop |
| 9 | 312 | 3 / 3 | 8 | 10 | trigger_event(313); stop |
| 9 | 313 | 3 / 4 | 2 | 10 | trigger_event(314); stop |
| 9 | 314 | 3 / 4 | 2 | 10 | trigger_event(315); stop |
| 9 | 315 | 3 / 5 | 8 | 10 | trigger_event(316); stop |
| 9 | 316 | 3 / 6 | 8 | 10 | trigger_event(317); stop |
| 9 | 317 | 3 / 7 | 4 | 10 | trigger_event(318); stop |
| 9 | 318 | 3 / 8 | 2 | 10 | set_switch(2); stop |
| 9 | 61 | 6 / 1 | 1 | 0 | stop |
| 9 | 71 | 7 / 1 | 10 | 10 | trigger_event(711); stop |
| 9 | 711 | 7 / 2 | 8 | 10 | trigger_event(712); stop |
| 9 | 712 | 7 / 3 | 6 | 10 | trigger_event(713); stop |
| 9 | 713 | 7 / 4 | 3 | 50 | set_switch(101); stop |
| 9 | 91 | 9 / 1 | 8 | 10 | trigger_event(911); stop |
| 9 | 911 | 9 / 2 | 10 | 10 | trigger_event(912); stop |
| 9 | 912 | 9 / 3 | 10 | 10 | trigger_event(913); stop |
| 9 | 913 | 9 / 4 | 5 | 10 | trigger_event(914); stop |
| 9 | 914 | 9 / 5 | 4 | 10 | set_switch(6); set_switch(8); stop |
| 9 | 111 | 11 / 1 | 8 | 10 | trigger_event(1111); stop |
| 9 | 1111 | 11 / 2 | 8 | 10 | trigger_event(1112); stop |
| 9 | 1112 | 11 / 3 | 12 | 120 | trigger_event(1113); stop |
| 9 | 1113 | 11 / 4 | 5 | 10 | set_switch(9); stop |
| 12 | 1 | 1 / 1 | 1 | 50 | construct_objects(room=1,group_or_wave=1); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
