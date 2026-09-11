# World of Illusion — vr-ep2/q946-bb-e

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/vr-ep2/q946-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/vr-ep2/q946-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/vr-ep2/q946-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 946; language E. Static scan: **281 objects, 781 enemy/NPC records, 251 events, 270 script labels.** Script roundtrip: differs.

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
| 1 | 21 | 160 | 44 |
| 2 | 47 | 149 | 44 |
| 3 | 27 | 123 | 29 |
| 4 | 22 | 1 | 0 |
| 5 | 25 | 117 | 41 |
| 10 | 58 | 83 | 43 |
| 13 | 26 | 1 | 1 |
| 17 | 55 | 147 | 49 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 100 | 0 / 0 | 0 | 0 | trigger_event(101); construct_objects(room=41,group_or_wave=2); stop |
| 1 | 101 | 41 / 1 | 3 | 100 | clear_switch(99); construct_objects(room=116,group_or_wave=1); trigger_event(102); trigger_event(103); stop |
| 1 | 102 | 41 / 2 | 4 | 100 | trigger_event(104); stop |
| 1 | 103 | 41 / 3 | 1 | 100 | trigger_event(105); stop |
| 1 | 104 | 41 / 4 | 5 | 100 | trigger_event(106); stop |
| 1 | 105 | 41 / 5 | 6 | 100 | trigger_event(107); stop |
| 1 | 106 | 41 / 6 | 4 | 100 | set_switch(10); trigger_event(108); trigger_event(110); stop |
| 1 | 107 | 41 / 7 | 5 | 100 | trigger_event(109); stop |
| 1 | 108 | 41 / 8 | 5 | 100 | trigger_event(111); stop |
| 1 | 109 | 41 / 9 | 6 | 100 | set_switch(32); stop |
| 1 | 110 | 41 / 10 | 1 | 100 | trigger_event(112); stop |
| 1 | 111 | 41 / 11 | 7 | 100 | set_switch(31); stop |
| 1 | 112 | 41 / 12 | 7 | 100 | trigger_event(113); stop |
| 1 | 113 | 41 / 13 | 5 | 100 | set_switch(30); stop |
| 1 | 200 | 0 / 0 | 0 | 0 | trigger_event(201); construct_objects(room=41,group_or_wave=2); stop |
| 1 | 201 | 41 / 14 | 3 | 100 | clear_switch(99); construct_objects(room=116,group_or_wave=1); trigger_event(202); trigger_event(203); stop |
| 1 | 202 | 41 / 15 | 4 | 100 | trigger_event(204); stop |
| 1 | 203 | 41 / 3 | 1 | 100 | trigger_event(205); stop |
| 1 | 204 | 41 / 16 | 3 | 100 | trigger_event(206); stop |
| 1 | 205 | 41 / 7 | 5 | 100 | trigger_event(207); stop |
| 1 | 206 | 41 / 17 | 6 | 100 | trigger_event(208); set_switch(10); stop |
| 1 | 207 | 41 / 18 | 4 | 100 | set_switch(32); stop |
| 1 | 208 | 41 / 19 | 5 | 100 | trigger_event(209); trigger_event(210); stop |
| 1 | 209 | 41 / 20 | 4 | 100 | trigger_event(211); stop |
| 1 | 210 | 41 / 21 | 1 | 100 | trigger_event(212); stop |
| 1 | 211 | 41 / 22 | 6 | 100 | set_switch(31); stop |
| 1 | 212 | 41 / 11 | 7 | 100 | trigger_event(213); stop |
| 1 | 213 | 41 / 23 | 4 | 100 | set_switch(30); stop |
| 1 | 300 | 0 / 0 | 0 | 0 | trigger_event(301); stop |
| 1 | 301 | 41 / 24 | 3 | 100 | clear_switch(99); construct_objects(room=116,group_or_wave=1); trigger_event(302); trigger_event(303); trigger_event(304); stop |
| 1 | 302 | 41 / 25 | 6 | 100 | trigger_event(305); stop |
| 1 | 303 | 41 / 26 | 4 | 500 | trigger_event(306); stop |
| 1 | 304 | 41 / 27 | 6 | 1000 | trigger_event(307); stop |
| 1 | 305 | 41 / 28 | 6 | 100 | trigger_event(308); stop |
| 1 | 306 | 41 / 29 | 3 | 100 | trigger_event(309); stop |
| 1 | 307 | 41 / 30 | 5 | 100 | trigger_event(310); stop |
| 1 | 308 | 41 / 31 | 5 | 100 | trigger_event(311); stop |
| 1 | 309 | 41 / 32 | 6 | 100 | trigger_event(312); stop |
| 1 | 310 | 41 / 33 | 4 | 100 | trigger_event(313); stop |
| 1 | 311 | 41 / 34 | 5 | 100 | set_switch(30); stop |
| 1 | 312 | 41 / 35 | 3 | 100 | set_switch(31); stop |
| 1 | 313 | 41 / 36 | 5 | 100 | set_switch(32); stop |
| 1 | 500 | 0 / 0 | 0 | 0 | trigger_event(501); stop |
| 1 | 501 | 0 / 0 | 0 | 0 | set_switch(30); set_switch(31); set_switch(32); stop |
| 2 | 100 | 0 / 0 | 0 | 0 | trigger_event(101); stop |
| 2 | 101 | 40 / 1 | 3 | 100 | trigger_event(102); stop |
| 2 | 102 | 40 / 2 | 5 | 100 | set_switch(10); trigger_event(103); trigger_event(104); stop |
| 2 | 103 | 40 / 3 | 5 | 100 | trigger_event(105); set_switch(11); stop |
| 2 | 104 | 40 / 4 | 1 | 100 | trigger_event(106); stop |
| 2 | 105 | 40 / 5 | 5 | 100 | trigger_event(107); set_switch(12); set_switch(15); set_switch(16); stop |
| 2 | 106 | 40 / 6 | 5 | 100 | trigger_event(108); stop |
| 2 | 107 | 40 / 7 | 6 | 100 | trigger_event(109); stop |
| 2 | 108 | 40 / 8 | 3 | 100 | set_switch(32); stop |
| 2 | 109 | 40 / 9 | 7 | 100 | trigger_event(110); stop |
| 2 | 110 | 40 / 10 | 9 | 100 | set_switch(13); trigger_event(111); trigger_event(112); stop |
| 2 | 111 | 40 / 11 | 3 | 100 | trigger_event(113); stop |
| 2 | 112 | 40 / 12 | 5 | 900 | set_switch(31); stop |
| 2 | 113 | 40 / 13 | 5 | 100 | set_switch(30); clear_switch(15); clear_switch(16); stop |
| 2 | 200 | 0 / 0 | 0 | 0 | trigger_event(201); stop |
| 2 | 201 | 40 / 14 | 3 | 100 | trigger_event(202); stop |
| 2 | 202 | 40 / 15 | 3 | 100 | trigger_event(203); trigger_event(204); trigger_event(205); stop |
| 2 | 203 | 40 / 16 | 1 | 100 | set_switch(10); trigger_event(206); stop |
| 2 | 204 | 40 / 17 | 4 | 500 | trigger_event(207); stop |
| 2 | 205 | 40 / 18 | 3 | 900 | trigger_event(208); stop |
| 2 | 206 | 40 / 19 | 3 | 100 | trigger_event(209); stop |
| 2 | 207 | 40 / 20 | 4 | 100 | set_switch(32); stop |
| 2 | 208 | 40 / 21 | 4 | 100 | trigger_event(210); stop |
| 2 | 209 | 40 / 22 | 3 | 100 | set_switch(11); trigger_event(211); stop |
| 2 | 210 | 40 / 23 | 7 | 100 | set_switch(31); stop |
| 2 | 211 | 40 / 24 | 6 | 100 | set_switch(12); set_switch(15); set_switch(16); trigger_event(212); stop |
| 2 | 212 | 40 / 25 | 5 | 100 | set_switch(13); trigger_event(213); stop |
| 2 | 213 | 40 / 26 | 5 | 100 | set_switch(30); clear_switch(15); clear_switch(16); stop |
| 2 | 300 | 0 / 0 | 0 | 0 | trigger_event(301); stop |
| 2 | 301 | 40 / 27 | 5 | 100 | trigger_event(302); trigger_event(303); set_switch(10); stop |
| 2 | 302 | 40 / 2 | 5 | 100 | trigger_event(304); stop |
| 2 | 303 | 40 / 3 | 5 | 1000 | trigger_event(305); stop |
| 2 | 304 | 40 / 28 | 3 | 100 | set_switch(11); trigger_event(306); stop |
| 2 | 305 | 40 / 29 | 2 | 100 | set_switch(32); stop |
| 2 | 306 | 40 / 22 | 3 | 100 | trigger_event(307); stop |
| 2 | 307 | 40 / 30 | 4 | 100 | set_switch(12); trigger_event(308); trigger_event(309); set_switch(15); set_switch(16); stop |
| 2 | 308 | 40 / 4 | 1 | 100 | trigger_event(310); stop |
| 2 | 309 | 40 / 31 | 1 | 100 | trigger_event(311); stop |
| 2 | 310 | 40 / 32 | 6 | 100 | set_switch(13); trigger_event(312); stop |
| 2 | 311 | 40 / 33 | 4 | 100 | trigger_event(313); stop |
| 2 | 312 | 40 / 34 | 6 | 100 | set_switch(31); stop |
| 2 | 313 | 40 / 35 | 5 | 100 | set_switch(30); clear_switch(15); clear_switch(16); stop |
| 2 | 500 | 0 / 0 | 0 | 0 | trigger_event(501); stop |
| 2 | 501 | 0 / 0 | 0 | 0 | set_switch(30); set_switch(31); set_switch(32); stop |
| 3 | 100 | 0 / 0 | 0 | 0 | trigger_event(101); trigger_event(102); stop |
| 3 | 101 | 40 / 1 | 8 | 100 | trigger_event(103); trigger_event(104); stop |
| 3 | 102 | 40 / 2 | 1 | 100 | trigger_event(105); stop |
| 3 | 103 | 40 / 3 | 6 | 100 | trigger_event(106); set_switch(10); stop |
| 3 | 104 | 40 / 4 | 3 | 100 | trigger_event(107); stop |
| 3 | 105 | 40 / 5 | 3 | 100 | trigger_event(108); stop |
| 3 | 106 | 40 / 6 | 9 | 100 | set_switch(30); stop |
| 3 | 107 | 40 / 7 | 9 | 100 | set_switch(31); stop |
| 3 | 108 | 40 / 8 | 3 | 100 | set_switch(32); stop |
| 3 | 200 | 0 / 0 | 0 | 0 | trigger_event(201); stop |
| 3 | 201 | 40 / 9 | 8 | 100 | trigger_event(202); stop |
| 3 | 202 | 40 / 10 | 3 | 100 | trigger_event(203); stop |
| 3 | 203 | 40 / 11 | 8 | 100 | trigger_event(204); set_switch(10); set_switch(15); stop |
| 3 | 204 | 40 / 12 | 7 | 100 | trigger_event(205); stop |
| 3 | 205 | 40 / 13 | 3 | 100 | trigger_event(206); stop |
| 3 | 206 | 40 / 14 | 5 | 100 | trigger_event(207); stop |
| 3 | 207 | 40 / 15 | 5 | 100 | trigger_event(208); stop |
| 3 | 208 | 40 / 16 | 5 | 100 | set_switch(30); set_switch(31); set_switch(32); clear_switch(15); stop |
| 3 | 300 | 0 / 0 | 0 | 0 | trigger_event(301); stop |
| 3 | 301 | 40 / 17 | 6 | 100 | trigger_event(302); stop |
| 3 | 302 | 40 / 18 | 11 | 100 | trigger_event(303); stop |
| 3 | 303 | 40 / 19 | 2 | 100 | trigger_event(304); stop |
| 3 | 304 | 40 / 20 | 3 | 100 | set_switch(10); set_switch(15); trigger_event(305); stop |
| 3 | 305 | 40 / 21 | 6 | 100 | trigger_event(306); stop |
| 3 | 306 | 40 / 22 | 3 | 100 | trigger_event(307); stop |
| 3 | 307 | 0 / 23 | 0 | 100 | trigger_event(308); stop |
| 3 | 308 | 40 / 24 | 3 | 100 | set_switch(30); set_switch(31); set_switch(32); clear_switch(15); stop |
| 3 | 500 | 0 / 0 | 0 | 0 | trigger_event(501); stop |
| 3 | 501 | 0 / 0 | 0 | 0 | set_switch(30); set_switch(31); set_switch(32); stop |
| 5 | 100 | 0 / 0 | 0 | 0 | trigger_event(101); trigger_event(102); stop |
| 5 | 101 | 11 / 1 | 8 | 100 | trigger_event(103); stop |
| 5 | 102 | 11 / 2 | 1 | 100 | trigger_event(104); stop |
| 5 | 103 | 11 / 3 | 2 | 100 | trigger_event(105); stop |
| 5 | 104 | 11 / 4 | 1 | 100 | trigger_event(106); stop |
| 5 | 105 | 11 / 5 | 6 | 100 | trigger_event(107); stop |
| 5 | 106 | 11 / 6 | 5 | 100 | trigger_event(108); stop |
| 5 | 107 | 11 / 7 | 3 | 100 | trigger_event(109); trigger_event(110); stop |
| 5 | 108 | 11 / 8 | 4 | 100 | set_switch(32); stop |
| 5 | 109 | 11 / 9 | 6 | 100 | set_switch(31); stop |
| 5 | 110 | 11 / 10 | 1 | 100 | trigger_event(111); stop |
| 5 | 111 | 11 / 11 | 3 | 100 | trigger_event(112); stop |
| 5 | 112 | 11 / 12 | 7 | 100 | set_switch(30); stop |
| 5 | 200 | 0 / 0 | 0 | 0 | trigger_event(201); trigger_event(202); stop |
| 5 | 201 | 11 / 1 | 8 | 100 | trigger_event(203); stop |
| 5 | 202 | 11 / 2 | 1 | 100 | trigger_event(204); stop |
| 5 | 203 | 11 / 13 | 3 | 100 | set_switch(15); trigger_event(205); stop |
| 5 | 204 | 11 / 14 | 2 | 100 | trigger_event(206); stop |
| 5 | 205 | 11 / 15 | 9 | 100 | trigger_event(207); stop |
| 5 | 206 | 11 / 16 | 5 | 100 | set_switch(32); stop |
| 5 | 207 | 11 / 17 | 6 | 100 | trigger_event(208); stop |
| 5 | 208 | 11 / 18 | 3 | 100 | trigger_event(209); trigger_event(210); stop |
| 5 | 209 | 11 / 19 | 3 | 100 | trigger_event(211); stop |
| 5 | 210 | 11 / 20 | 3 | 100 | trigger_event(212); stop |
| 5 | 211 | 11 / 21 | 3 | 100 | set_switch(31); stop |
| 5 | 212 | 11 / 22 | 3 | 100 | set_switch(30); clear_switch(15); stop |
| 5 | 300 | 0 / 0 | 0 | 0 | trigger_event(301); trigger_event(302); stop |
| 5 | 301 | 11 / 1 | 8 | 100 | trigger_event(303); stop |
| 5 | 302 | 11 / 2 | 1 | 100 | trigger_event(304); stop |
| 5 | 303 | 11 / 23 | 9 | 100 | trigger_event(305); stop |
| 5 | 304 | 11 / 24 | 1 | 100 | trigger_event(306); stop |
| 5 | 305 | 11 / 25 | 2 | 100 | trigger_event(307); stop |
| 5 | 306 | 11 / 26 | 1 | 100 | set_switch(32); stop |
| 5 | 307 | 11 / 27 | 7 | 100 | trigger_event(308); stop |
| 5 | 308 | 11 / 27 | 7 | 100 | trigger_event(309); trigger_event(310); stop |
| 5 | 309 | 11 / 28 | 2 | 100 | trigger_event(311); stop |
| 5 | 310 | 11 / 29 | 1 | 100 | trigger_event(312); stop |
| 5 | 311 | 11 / 30 | 4 | 100 | set_switch(31); stop |
| 5 | 312 | 11 / 31 | 3 | 100 | set_switch(30); stop |
| 5 | 500 | 0 / 0 | 0 | 0 | trigger_event(501); stop |
| 5 | 501 | 0 / 0 | 0 | 0 | set_switch(30); set_switch(31); set_switch(32); stop |
| 10 | 100 | 0 / 0 | 0 | 0 | trigger_event(101); trigger_event(102); stop |
| 10 | 101 | 80 / 1 | 2 | 100 | trigger_event(103); stop |
| 10 | 102 | 80 / 2 | 1 | 100 | trigger_event(104); stop |
| 10 | 103 | 80 / 3 | 9 | 100 | trigger_event(105); stop |
| 10 | 104 | 80 / 4 | 2 | 100 | trigger_event(106); stop |
| 10 | 105 | 80 / 5 | 9 | 100 | trigger_event(107); construct_objects(room=80,group_or_wave=2); stop |
| 10 | 106 | 80 / 6 | 4 | 100 | trigger_event(108); stop |
| 10 | 107 | 80 / 7 | 3 | 100 | set_switch(32); stop |
| 10 | 108 | 80 / 8 | 3 | 100 | set_switch(11); set_switch(13); trigger_event(109); stop |
| 10 | 109 | 80 / 9 | 3 | 900 | trigger_event(110); stop |
| 10 | 110 | 80 / 10 | 5 | 100 | trigger_event(111); stop |
| 10 | 111 | 80 / 11 | 4 | 100 | trigger_event(112); stop |
| 10 | 112 | 80 / 12 | 3 | 100 | set_switch(30); set_switch(31); stop |
| 10 | 200 | 0 / 0 | 0 | 0 | trigger_event(201); trigger_event(202); stop |
| 10 | 201 | 80 / 1 | 2 | 100 | trigger_event(203); stop |
| 10 | 202 | 8 / 2 | 0 | 100 | trigger_event(204); stop |
| 10 | 203 | 80 / 3 | 9 | 100 | trigger_event(205); stop |
| 10 | 204 | 80 / 4 | 2 | 100 | trigger_event(206); stop |
| 10 | 205 | 80 / 5 | 9 | 100 | trigger_event(207); stop |
| 10 | 206 | 80 / 6 | 4 | 100 | trigger_event(208); stop |
| 10 | 207 | 80 / 7 | 3 | 100 | set_switch(32); stop |
| 10 | 208 | 80 / 13 | 3 | 100 | set_switch(15); set_switch(11); set_switch(12); trigger_event(209); stop |
| 10 | 209 | 80 / 14 | 1 | 900 | trigger_event(210); stop |
| 10 | 210 | 80 / 15 | 4 | 100 | trigger_event(211); stop |
| 10 | 211 | 80 / 16 | 3 | 100 | trigger_event(212); stop |
| 10 | 212 | 80 / 17 | 4 | 100 | set_switch(30); set_switch(31); stop |
| 10 | 300 | 0 / 0 | 0 | 0 | trigger_event(301); trigger_event(302); stop |
| 10 | 301 | 80 / 1 | 2 | 100 | trigger_event(303); stop |
| 10 | 302 | 80 / 2 | 1 | 100 | trigger_event(304); stop |
| 10 | 303 | 80 / 3 | 9 | 100 | trigger_event(305); stop |
| 10 | 304 | 80 / 4 | 2 | 100 | trigger_event(306); stop |
| 10 | 305 | 80 / 5 | 9 | 100 | trigger_event(307); stop |
| 10 | 306 | 80 / 6 | 4 | 100 | trigger_event(308); stop |
| 10 | 307 | 80 / 7 | 3 | 100 | set_switch(32); stop |
| 10 | 308 | 80 / 18 | 4 | 100 | set_switch(11); set_switch(14); set_switch(15); set_switch(12); set_switch(13); trigger_event(309); trigger_event(310); stop |
| 10 | 309 | 80 / 19 | 4 | 900 | trigger_event(311); stop |
| 10 | 310 | 80 / 20 | 2 | 900 | trigger_event(312); stop |
| 10 | 311 | 80 / 21 | 5 | 100 | set_switch(31); stop |
| 10 | 312 | 80 / 22 | 5 | 100 | set_switch(30); stop |
| 10 | 500 | 0 / 0 | 0 | 0 | trigger_event(501); stop |
| 10 | 501 | 0 / 0 | 0 | 0 | set_switch(30); set_switch(31); set_switch(32); stop |
| 10 | 600 | 0 / 0 | 0 | 0 | trigger_event(601); stop |
| 10 | 601 | 0 / 0 | 0 | 1 | construct_objects(room=80,group_or_wave=5); stop |
| 13 | 1 | 0 / 1 | 1 | 0 | construct_objects(room=1,group_or_wave=1); stop |
| 17 | 100 | 0 / 0 | 0 | 0 | trigger_event(101); trigger_event(102); construct_objects(room=30,group_or_wave=1); stop |
| 17 | 101 | 30 / 1 | 4 | 200 | trigger_event(103); stop |
| 17 | 102 | 30 / 2 | 1 | 200 | trigger_event(104); stop |
| 17 | 103 | 30 / 3 | 2 | 100 | trigger_event(105); trigger_event(106); stop |
| 17 | 104 | 30 / 4 | 6 | 100 | trigger_event(107); stop |
| 17 | 105 | 30 / 5 | 5 | 100 | set_switch(10); trigger_event(108); stop |
| 17 | 106 | 30 / 6 | 2 | 100 | trigger_event(109); stop |
| 17 | 107 | 30 / 7 | 5 | 100 | set_switch(32); stop |
| 17 | 108 | 30 / 8 | 6 | 500 | trigger_event(110); stop |
| 17 | 109 | 30 / 9 | 6 | 500 | trigger_event(111); stop |
| 17 | 110 | 30 / 10 | 6 | 500 | trigger_event(112); stop |
| 17 | 111 | 30 / 11 | 6 | 500 | set_switch(31); stop |
| 17 | 112 | 30 / 12 | 4 | 500 | set_switch(30); stop |
| 17 | 200 | 0 / 0 | 0 | 0 | trigger_event(201); trigger_event(202); construct_objects(room=30,group_or_wave=6); stop |
| 17 | 201 | 30 / 13 | 3 | 200 | trigger_event(203); stop |
| 17 | 202 | 30 / 14 | 3 | 200 | trigger_event(204); stop |
| 17 | 203 | 30 / 15 | 3 | 100 | trigger_event(205); stop |
| 17 | 204 | 30 / 16 | 2 | 100 | trigger_event(206); stop |
| 17 | 205 | 30 / 17 | 3 | 100 | trigger_event(207); stop |
| 17 | 206 | 30 / 18 | 4 | 100 | trigger_event(208); stop |
| 17 | 207 | 30 / 19 | 5 | 100 | trigger_event(209); construct_objects(room=30,group_or_wave=7); stop |
| 17 | 208 | 30 / 20 | 4 | 100 | set_switch(32); stop |
| 17 | 209 | 30 / 21 | 4 | 100 | trigger_event(210); stop |
| 17 | 210 | 30 / 22 | 5 | 100 | trigger_event(211); stop |
| 17 | 211 | 30 / 23 | 2 | 100 | trigger_event(212); stop |
| 17 | 212 | 30 / 24 | 4 | 100 | set_switch(31); set_switch(30); stop |
| 17 | 300 | 0 / 0 | 0 | 0 | trigger_event(301); trigger_event(302); construct_objects(room=30,group_or_wave=8); stop |
| 17 | 301 | 30 / 25 | 3 | 200 | trigger_event(303); stop |
| 17 | 302 | 30 / 26 | 6 | 100 | trigger_event(304); stop |
| 17 | 303 | 30 / 27 | 2 | 100 | trigger_event(305); stop |
| 17 | 304 | 30 / 28 | 2 | 100 | set_switch(32); stop |
| 17 | 305 | 30 / 29 | 5 | 100 | trigger_event(306); stop |
| 17 | 306 | 30 / 30 | 3 | 100 | trigger_event(307); stop |
| 17 | 307 | 30 / 31 | 9 | 100 | trigger_event(308); stop |
| 17 | 308 | 30 / 32 | 7 | 100 | trigger_event(309); stop |
| 17 | 309 | 30 / 33 | 4 | 100 | trigger_event(310); stop |
| 17 | 310 | 30 / 34 | 2 | 100 | trigger_event(311); stop |
| 17 | 311 | 30 / 35 | 3 | 100 | trigger_event(312); stop |
| 17 | 312 | 30 / 36 | 6 | 100 | set_switch(31); set_switch(30); stop |
| 17 | 500 | 0 / 0 | 0 | 0 | trigger_event(501); stop |
| 17 | 501 | 0 / 0 | 0 | 0 | set_switch(30); set_switch(31); set_switch(32); stop |
| 17 | 600 | 0 / 0 | 0 | 0 | trigger_event(601); stop |
| 17 | 601 | 0 / 0 | 0 | 0 | construct_objects(room=30,group_or_wave=2); stop |
| 17 | 610 | 0 / 0 | 0 | 0 | trigger_event(611); stop |
| 17 | 611 | 0 / 0 | 0 | 0 | construct_objects(room=30,group_or_wave=3); stop |
| 17 | 620 | 0 / 0 | 0 | 0 | trigger_event(621); stop |
| 17 | 621 | 0 / 0 | 0 | 0 | construct_objects(room=30,group_or_wave=4); stop |
| 17 | 630 | 0 / 0 | 0 | 0 | trigger_event(631); stop |
| 17 | 631 | 0 / 0 | 0 | 0 | construct_objects(room=30,group_or_wave=5); stop |

## Review notes

- Reassembled bytes differ beyond recognized alignment; inspect before rebuilding

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
