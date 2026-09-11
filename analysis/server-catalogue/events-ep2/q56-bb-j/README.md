# Rare Rappies — events-ep2/q56-bb-j

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/events-ep2/q56-bb-j.zip?download=1)**

[Original QST](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/events-ep2/q56-bb-j.qst?download=1) · [Extracted BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/events-ep2/q56-bb-j/q56-bb-j.qst-quest0.bin?download=1) · [Extracted DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/events-ep2/q56-bb-j/q56-bb-j.qst-quest0.dat?download=1)

QST is the preserved original package. BIN and DAT are its decoded payload files, not reassembled scripts. The ZIP contains all three formats.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 56; language J. Static scan: **706 objects, 362 enemy/NPC records, 116 events, 517 script labels.** Script roundtrip: alignment-only.

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
| 0 | 44 | 24 | 0 |
| 1 | 87 | 66 | 23 |
| 3 | 93 | 40 | 12 |
| 9 | 123 | 122 | 40 |
| 11 | 101 | 51 | 19 |
| 12 | 22 | 1 | 1 |
| 13 | 6 | 1 | 1 |
| 14 | 30 | 1 | 1 |
| 15 | 30 | 1 | 1 |
| 17 | 170 | 55 | 18 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 101 | 10 / 1 | 4 | 1 | trigger_event(10101); stop |
| 1 | 10101 | 10 / 2 | 4 | 100 | trigger_event(10102); stop |
| 1 | 10102 | 10 / 3 | 0 | 10 | set_switch(3); set_switch(4); stop |
| 1 | 402 | 40 / 5 | 1 | 10 | stop |
| 1 | 403 | 40 / 6 | 1 | 40 | stop |
| 1 | 404 | 40 / 7 | 1 | 70 | stop |
| 1 | 401 | 40 / 1 | 1 | 130 | trigger_event(4011); stop |
| 1 | 4011 | 40 / 2 | 5 | 10 | trigger_event(4012); stop |
| 1 | 4012 | 40 / 3 | 3 | 10 | trigger_event(4013); stop |
| 1 | 4013 | 40 / 4 | 2 | 150 | set_switch(7); set_switch(8); set_switch(9); set_switch(10); set_switch(17); set_switch(18); set_switch(22); stop |
| 1 | 411 | 41 / 1 | 5 | 10 | trigger_event(4111); stop |
| 1 | 4111 | 41 / 2 | 5 | 10 | trigger_event(4112); stop |
| 1 | 4112 | 41 / 3 | 6 | 60 | trigger_event(4113); stop |
| 1 | 4113 | 41 / 4 | 5 | 100 | trigger_event(4114); stop |
| 1 | 4114 | 41 / 5 | 5 | 10 | set_switch(11); set_switch(12); stop |
| 1 | 601 | 60 / 1 | 4 | 30 | trigger_event(6011); stop |
| 1 | 6011 | 60 / 2 | 4 | 100 | trigger_event(6012); stop |
| 1 | 6012 | 60 / 3 | 0 | 10 | set_switch(23); set_switch(24); set_switch(25); set_switch(13); set_switch(14); stop |
| 1 | 602 | 60 / 4 | 0 | 100 | stop |
| 1 | 901 | 90 / 1 | 4 | 1 | set_switch(15); set_switch(16); stop |
| 1 | 911 | 91 / 1 | 3 | 1 | set_switch(5); set_switch(6); stop |
| 1 | 1011 | 101 / 1 | 1 | 1 | stop |
| 1 | 1601 | 160 / 1 | 2 | 1 | stop |
| 14 | 1 | 1 / 1 | 1 | 50 | construct_objects(room=1,group_or_wave=1); stop |
| 3 | 101 | 10 / 1 | 1 | 10 | set_switch(13); set_switch(14); set_switch(15); set_switch(16); set_switch(17); set_switch(18); set_switch(24); set_switch(25); stop |
| 3 | 102 | 10 / 2 | 5 | 100 | stop |
| 3 | 201 | 20 / 1 | 1 | 60 | set_switch(5); set_switch(6); stop |
| 3 | 202 | 20 / 2 | 3 | 60 | stop |
| 3 | 401 | 40 / 1 | 1 | 30 | set_switch(7); set_switch(8); set_switch(9); set_switch(10); stop |
| 3 | 402 | 40 / 2 | 6 | 30 | stop |
| 3 | 411 | 41 / 1 | 1 | 200 | set_switch(21); set_switch(22); set_switch(23); stop |
| 3 | 412 | 41 / 2 | 7 | 1 | stop |
| 3 | 501 | 50 / 1 | 1 | 1 | set_switch(11); set_switch(12); set_switch(13); set_switch(14); stop |
| 3 | 502 | 50 / 2 | 6 | 60 | stop |
| 3 | 511 | 51 / 1 | 1 | 200 | set_switch(19); set_switch(20); stop |
| 3 | 512 | 51 / 2 | 7 | 10 | stop |
| 15 | 1 | 1 / 1 | 1 | 50 | construct_objects(room=1,group_or_wave=1); stop |
| 9 | 31 | 3 / 1 | 3 | 1 | trigger_event(311); trigger_event(3121); stop |
| 9 | 311 | 3 / 2 | 4 | 120 | trigger_event(312); stop |
| 9 | 3121 | 3 / 3 | 2 | 30 | stop |
| 9 | 312 | 3 / 4 | 4 | 10 | trigger_event(313); stop |
| 9 | 313 | 3 / 5 | 4 | 1 | trigger_event(314); trigger_event(3141); stop |
| 9 | 314 | 3 / 6 | 3 | 200 | trigger_event(315); stop |
| 9 | 3141 | 3 / 7 | 2 | 60 | stop |
| 9 | 315 | 3 / 8 | 3 | 100 | trigger_event(316); stop |
| 9 | 316 | 3 / 9 | 2 | 1 | trigger_event(317); trigger_event(3171); stop |
| 9 | 317 | 3 / 10 | 3 | 100 | trigger_event(319); stop |
| 9 | 319 | 3 / 11 | 4 | 60 | set_switch(2); set_switch(3); set_switch(12); stop |
| 9 | 3171 | 3 / 12 | 2 | 1 | stop |
| 9 | 32 | 3 / 13 | 2 | 100 | trigger_event(321); stop |
| 9 | 321 | 3 / 14 | 2 | 60 | trigger_event(3211); stop |
| 9 | 3211 | 3 / 15 | 2 | 30 | trigger_event(3212); stop |
| 9 | 3212 | 3 / 16 | 2 | 130 | trigger_event(3213); stop |
| 9 | 3213 | 3 / 17 | 2 | 100 | trigger_event(3214); stop |
| 9 | 3214 | 3 / 18 | 2 | 10 | stop |
| 9 | 61 | 6 / 1 | 2 | 1 | stop |
| 9 | 71 | 7 / 1 | 3 | 30 | trigger_event(711); stop |
| 9 | 711 | 7 / 2 | 3 | 1 | trigger_event(712); stop |
| 9 | 712 | 7 / 3 | 4 | 50 | trigger_event(713); stop |
| 9 | 713 | 7 / 6 | 6 | 50 | set_switch(4); set_switch(5); stop |
| 9 | 72 | 7 / 4 | 2 | 300 | trigger_event(721); stop |
| 9 | 721 | 7 / 5 | 3 | 500 | stop |
| 9 | 91 | 9 / 1 | 4 | 100 | trigger_event(911); stop |
| 9 | 911 | 9 / 2 | 4 | 200 | set_switch(6); set_switch(8); stop |
| 9 | 92 | 9 / 3 | 3 | 60 | trigger_event(921); stop |
| 9 | 921 | 9 / 4 | 4 | 30 | stop |
| 9 | 101 | 10 / 1 | 3 | 1 | stop |
| 9 | 111 | 11 / 1 | 1 | 400 | construct_objects(room=11,group_or_wave=1); set_switch(7); set_switch(9); set_switch(10); set_switch(11); stop |
| 9 | 112 | 11 / 2 | 3 | 1 | construct_objects(room=11,group_or_wave=2); trigger_event(1121); stop |
| 9 | 1121 | 11 / 3 | 3 | 60 | construct_objects(room=11,group_or_wave=3); trigger_event(1122); stop |
| 9 | 1122 | 11 / 4 | 3 | 60 | trigger_event(1123); stop |
| 9 | 1123 | 11 / 5 | 4 | 1 | trigger_event(1124); stop |
| 9 | 1124 | 11 / 6 | 4 | 1 | trigger_event(1125); stop |
| 9 | 1125 | 11 / 7 | 4 | 1 | trigger_event(1126); stop |
| 9 | 1126 | 11 / 8 | 5 | 1 | trigger_event(1127); stop |
| 9 | 1127 | 11 / 9 | 5 | 1 | stop |
| 9 | 141 | 14 / 1 | 1 | 1 | stop |
| 12 | 1 | 1 / 1 | 1 | 50 | construct_objects(room=1,group_or_wave=1); stop |
| 11 | 201 | 20 / 1 | 2 | 300 | stop |
| 11 | 202 | 20 / 2 | 4 | 10 | set_switch(3); set_switch(6); stop |
| 11 | 401 | 40 / 1 | 3 | 10 | set_switch(20); set_switch(22); set_switch(21); stop |
| 11 | 402 | 40 / 2 | 3 | 10 | stop |
| 11 | 501 | 50 / 1 | 2 | 150 | set_switch(15); set_switch(16); set_switch(17); set_switch(18); set_switch(19); stop |
| 11 | 502 | 50 / 2 | 4 | 10 | stop |
| 11 | 701 | 70 / 1 | 1 | 200 | set_switch(25); set_switch(26); set_switch(9); set_switch(10); stop |
| 11 | 702 | 70 / 2 | 4 | 10 | stop |
| 11 | 801 | 80 / 1 | 3 | 10 | trigger_event(8011); stop |
| 11 | 8011 | 80 / 2 | 1 | 100 | set_switch(23); set_switch(24); stop |
| 11 | 802 | 80 / 3 | 3 | 10 | stop |
| 11 | 901 | 90 / 1 | 2 | 150 | stop |
| 11 | 902 | 90 / 2 | 4 | 10 | set_switch(7); stop |
| 11 | 951 | 95 / 1 | 2 | 250 | set_switch(4); set_switch(5); set_switch(1); stop |
| 11 | 952 | 95 / 2 | 5 | 10 | stop |
| 11 | 2801 | 280 / 1 | 3 | 10 | stop |
| 11 | 2641 | 264 / 1 | 1 | 10 | stop |
| 11 | 2111 | 211 / 1 | 2 | 10 | stop |
| 11 | 2901 | 290 / 1 | 2 | 10 | stop |
| 13 | 1 | 0 / 1 | 1 | 0 | construct_objects(room=1,group_or_wave=1); stop |
| 17 | 11 | 1 / 1 | 6 | 1 | stop |
| 17 | 21 | 2 / 1 | 2 | 100 | trigger_event(213); stop |
| 17 | 213 | 2 / 2 | 1 | 100 | set_switch(2); stop |
| 17 | 201 | 20 / 1 | 2 | 100 | set_switch(3); stop |
| 17 | 202 | 20 / 2 | 4 | 10 | stop |
| 17 | 101 | 10 / 1 | 7 | 10 | set_switch(4); stop |
| 17 | 102 | 10 / 2 | 3 | 10 | stop |
| 17 | 31 | 3 / 1 | 2 | 10 | trigger_event(311); stop |
| 17 | 311 | 3 / 2 | 3 | 100 | set_switch(5); stop |
| 17 | 41 | 4 / 1 | 1 | 150 | set_switch(6); stop |
| 17 | 211 | 21 / 1 | 1 | 150 | set_switch(7); stop |
| 17 | 212 | 21 / 2 | 6 | 10 | stop |
| 17 | 51 | 5 / 1 | 3 | 10 | trigger_event(511); stop |
| 17 | 511 | 5 / 2 | 3 | 100 | trigger_event(512); stop |
| 17 | 512 | 5 / 3 | 2 | 100 | set_switch(8); stop |
| 17 | 221 | 22 / 1 | 2 | 200 | set_switch(9); stop |
| 17 | 222 | 22 / 2 | 6 | 10 | stop |
| 17 | 301 | 30 / 1 | 1 | 200 | set_switch(1); construct_objects(room=30,group_or_wave=1); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
