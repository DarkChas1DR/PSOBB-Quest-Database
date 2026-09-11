# Sister\'s Dream — events-ep2/q91-bb-j

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/events-ep2/q91-bb-j.zip?download=1)**

[Original QST](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/events-ep2/q91-bb-j.qst?download=1) · [Extracted BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/events-ep2/q91-bb-j/q91-bb-j.qst-quest0.bin?download=1) · [Extracted DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/events-ep2/q91-bb-j/q91-bb-j.qst-quest0.dat?download=1)

QST is the preserved original package. BIN and DAT are its decoded payload files, not reassembled scripts. The ZIP contains all three formats.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 91; language J. Static scan: **686 objects, 269 enemy/NPC records, 85 events, 675 script labels.** Script roundtrip: alignment-only.

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
| 0 | 66 | 16 | 0 |
| 2 | 83 | 35 | 18 |
| 3 | 179 | 81 | 24 |
| 4 | 191 | 62 | 22 |
| 5 | 145 | 73 | 19 |
| 6 | 16 | 1 | 1 |
| 7 | 6 | 1 | 1 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 2 | 201 | 20 / 1 | 3 | 30 | trigger_event(2011); stop |
| 2 | 2011 | 20 / 2 | 3 | 60 | trigger_event(2012); stop |
| 2 | 2012 | 20 / 3 | 4 | 60 | trigger_event(2013); stop |
| 2 | 2013 | 20 / 4 | 4 | 60 | set_switch(3); set_switch(4); stop |
| 2 | 301 | 30 / 1 | 1 | 30 | set_switch(7); set_switch(8); stop |
| 2 | 501 | 50 / 1 | 2 | 30 | set_switch(101); trigger_event(5011); stop |
| 2 | 5011 | 50 / 2 | 1 | 180 | set_switch(151); set_switch(9); set_switch(11); set_switch(2); stop |
| 2 | 502 | 50 / 3 | 1 | 90 | set_switch(101); stop |
| 2 | 701 | 70 / 1 | 2 | 30 | stop |
| 2 | 702 | 70 / 2 | 2 | 30 | stop |
| 2 | 901 | 90 / 1 | 2 | 30 | stop |
| 2 | 911 | 91 / 1 | 2 | 30 | stop |
| 2 | 1611 | 161 / 1 | 1 | 30 | stop |
| 2 | 1011 | 101 / 1 | 2 | 30 | stop |
| 2 | 1021 | 102 / 1 | 2 | 30 | stop |
| 2 | 1101 | 110 / 1 | 1 | 30 | stop |
| 2 | 1401 | 140 / 1 | 1 | 30 | stop |
| 2 | 1501 | 150 / 1 | 1 | 30 | stop |
| 3 | 101 | 10 / 1 | 4 | 10 | trigger_event(1011); stop |
| 3 | 1011 | 10 / 2 | 4 | 10 | set_switch(11); stop |
| 3 | 111 | 11 / 1 | 2 | 180 | trigger_event(1111); stop |
| 3 | 1111 | 11 / 2 | 4 | 120 | set_switch(32); stop |
| 3 | 201 | 20 / 1 | 4 | 10 | trigger_event(2011); stop |
| 3 | 2011 | 20 / 2 | 4 | 60 | set_switch(9); stop |
| 3 | 401 | 40 / 1 | 4 | 0 | trigger_event(4011); stop |
| 3 | 4011 | 40 / 2 | 4 | 10 | trigger_event(4012); stop |
| 3 | 4012 | 40 / 3 | 4 | 10 | trigger_event(4013); stop |
| 3 | 4013 | 40 / 4 | 3 | 10 | trigger_event(4014); stop |
| 3 | 4014 | 40 / 5 | 3 | 10 | trigger_event(4015); stop |
| 3 | 4015 | 40 / 6 | 5 | 10 | trigger_event(4016); stop |
| 3 | 4016 | 40 / 7 | 4 | 10 | trigger_event(4017); stop |
| 3 | 4017 | 40 / 8 | 4 | 10 | trigger_event(4018); stop |
| 3 | 4018 | 40 / 9 | 2 | 30 | trigger_event(4019); stop |
| 3 | 4019 | 40 / 10 | 4 | 120 | stop |
| 3 | 402 | 40 / 11 | 1 | 0 | trigger_event(4021); stop |
| 3 | 4021 | 40 / 12 | 2 | 0 | trigger_event(4022); stop |
| 3 | 4022 | 40 / 13 | 2 | 30 | trigger_event(4023); stop |
| 3 | 4023 | 40 / 14 | 2 | 30 | trigger_event(4024); stop |
| 3 | 4024 | 40 / 15 | 1 | 60 | stop |
| 3 | 601 | 60 / 1 | 4 | 0 | trigger_event(6011); stop |
| 3 | 6011 | 60 / 2 | 4 | 0 | trigger_event(6012); stop |
| 3 | 6012 | 60 / 3 | 6 | 0 | set_switch(17); stop |
| 4 | 901 | 90 / 1 | 3 | 0 | set_switch(15); set_switch(18); set_switch(19); set_switch(20); set_switch(21); set_switch(22); stop |
| 4 | 911 | 91 / 1 | 4 | 0 | trigger_event(9111); stop |
| 4 | 9111 | 91 / 2 | 3 | 30 | set_switch(14); set_switch(21); set_switch(22); set_switch(23); set_switch(31); stop |
| 4 | 912 | 91 / 3 | 2 | 30 | stop |
| 4 | 921 | 92 / 1 | 3 | 0 | trigger_event(9211); stop |
| 4 | 9211 | 92 / 2 | 2 | 30 | trigger_event(9212); stop |
| 4 | 9212 | 92 / 3 | 2 | 30 | set_switch(8); set_switch(9); set_switch(15); set_switch(20); stop |
| 4 | 931 | 93 / 1 | 1 | 0 | trigger_event(9311); stop |
| 4 | 9311 | 93 / 2 | 3 | 30 | set_switch(18); set_switch(19); stop |
| 4 | 941 | 94 / 1 | 2 | 0 | trigger_event(9411); stop |
| 4 | 9411 | 94 / 2 | 4 | 30 | set_switch(27); set_switch(28); stop |
| 4 | 951 | 95 / 1 | 4 | 0 | trigger_event(9511); stop |
| 4 | 9511 | 95 / 2 | 3 | 30 | set_switch(30); stop |
| 4 | 952 | 95 / 3 | 2 | 30 | stop |
| 4 | 961 | 96 / 1 | 3 | 0 | trigger_event(9611); stop |
| 4 | 9611 | 96 / 2 | 3 | 30 | set_switch(7); set_switch(16); set_switch(17); stop |
| 4 | 971 | 97 / 1 | 1 | 0 | trigger_event(9711); stop |
| 4 | 9711 | 97 / 2 | 4 | 30 | trigger_event(9712); stop |
| 4 | 9712 | 97 / 3 | 3 | 30 | trigger_event(9713); stop |
| 4 | 9713 | 97 / 4 | 4 | 30 | set_switch(26); stop |
| 4 | 981 | 98 / 1 | 3 | 0 | trigger_event(9811); stop |
| 4 | 9811 | 98 / 2 | 3 | 30 | set_switch(8); set_switch(9); set_switch(14); stop |
| 5 | 121 | 12 / 1 | 3 | 30 | trigger_event(1211); stop |
| 5 | 1211 | 12 / 2 | 5 | 10 | set_switch(32); stop |
| 5 | 411 | 41 / 1 | 4 | 30 | trigger_event(4111); stop |
| 5 | 4111 | 41 / 2 | 5 | 30 | trigger_event(4112); stop |
| 5 | 4112 | 41 / 3 | 1 | 30 | trigger_event(4113); stop |
| 5 | 4113 | 41 / 4 | 1 | 60 | trigger_event(4114); stop |
| 5 | 4114 | 41 / 5 | 2 | 90 | stop |
| 5 | 412 | 41 / 6 | 3 | 90 | trigger_event(4121); stop |
| 5 | 4121 | 41 / 7 | 3 | 90 | stop |
| 5 | 421 | 42 / 1 | 1 | 30 | trigger_event(4211); stop |
| 5 | 4211 | 42 / 2 | 4 | 10 | trigger_event(4212); stop |
| 5 | 4212 | 42 / 3 | 6 | 30 | trigger_event(4213); stop |
| 5 | 4213 | 42 / 4 | 3 | 60 | set_switch(7); stop |
| 5 | 501 | 50 / 1 | 7 | 30 | trigger_event(5011); stop |
| 5 | 5011 | 50 / 2 | 6 | 10 | trigger_event(5012); stop |
| 5 | 5012 | 50 / 3 | 7 | 10 | trigger_event(5013); stop |
| 5 | 5013 | 50 / 4 | 3 | 60 | set_switch(20); stop |
| 5 | 521 | 52 / 1 | 7 | 30 | trigger_event(5211); stop |
| 5 | 5211 | 52 / 2 | 2 | 30 | set_switch(30); stop |
| 6 | 1 | 1 / 1 | 1 | 50 | construct_objects(room=1,group_or_wave=1); stop |
| 7 | 1 | 1 / 1 | 1 | 50 | construct_objects(room=1,group_or_wave=1); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
