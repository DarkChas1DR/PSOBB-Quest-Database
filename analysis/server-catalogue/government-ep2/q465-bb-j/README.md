# ７－５：亜生命体の島 — government-ep2/q465-bb-j

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/government-ep2/q465-bb-j.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep2/q465-bb-j.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep2/q465-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 465; language J. Static scan: **913 objects, 372 enemy/NPC records, 136 events, 125 script labels.** Script roundtrip: byte-identical.

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
0x00, 0x12, 0x00, 0x00, 0x00
0x05, 0x17, 0x00, 0x00, 0x02
0x06, 0x18, 0x00, 0x00, 0x02
0x07, 0x19, 0x00, 0x00, 0x02
0x08, 0x1A, 0x00, 0x01, 0x01
0x09, 0x1B, 0x00, 0x00, 0x02
0x0C, 0x1E, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 53 | 19 | 0 |
| 5 | 120 | 27 | 13 |
| 6 | 176 | 56 | 19 |
| 7 | 139 | 58 | 27 |
| 8 | 224 | 97 | 34 |
| 9 | 178 | 114 | 42 |
| 12 | 23 | 1 | 1 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 5 | 21 | 2 / 1 | 3 | 200 | set_switch(2); stop |
| 5 | 22 | 2 / 2 | 2 | 60 | stop |
| 5 | 31 | 3 / 1 | 3 | 1 | trigger_event(311); stop |
| 5 | 311 | 3 / 2 | 2 | 100 | trigger_event(312); stop |
| 5 | 312 | 3 / 3 | 1 | 100 | set_switch(3); set_switch(4); stop |
| 5 | 32 | 3 / 4 | 3 | 200 | trigger_event(321); stop |
| 5 | 321 | 3 / 5 | 3 | 200 | stop |
| 5 | 51 | 5 / 1 | 2 | 1 | trigger_event(511); stop |
| 5 | 511 | 5 / 2 | 2 | 100 | trigger_event(512); stop |
| 5 | 512 | 5 / 3 | 2 | 100 | set_switch(5); stop |
| 5 | 52 | 5 / 4 | 1 | 300 | trigger_event(521); stop |
| 5 | 521 | 5 / 5 | 1 | 300 | stop |
| 5 | 62 | 6 / 1 | 2 | 30 | set_switch(6); stop |
| 6 | 21 | 2 / 1 | 3 | 1 | stop |
| 6 | 31 | 3 / 1 | 4 | 1 | trigger_event(311); stop |
| 6 | 311 | 3 / 2 | 4 | 100 | trigger_event(312); stop |
| 6 | 312 | 3 / 3 | 3 | 100 | set_switch(13); set_switch(16); stop |
| 6 | 32 | 3 / 4 | 2 | 100 | trigger_event(321); stop |
| 6 | 321 | 3 / 5 | 3 | 300 | stop |
| 6 | 41 | 4 / 1 | 3 | 1 | trigger_event(411); stop |
| 6 | 411 | 4 / 2 | 3 | 300 | trigger_event(412); stop |
| 6 | 412 | 4 / 3 | 4 | 1 | set_switch(15); set_switch(14); set_switch(12); set_switch(11); set_switch(7); stop |
| 6 | 42 | 4 / 4 | 4 | 100 | trigger_event(421); stop |
| 6 | 421 | 4 / 5 | 3 | 300 | stop |
| 6 | 61 | 6 / 1 | 3 | 150 | stop |
| 6 | 71 | 7 / 1 | 2 | 1 | stop |
| 6 | 101 | 10 / 1 | 2 | 150 | stop |
| 6 | 111 | 11 / 1 | 3 | 1 | trigger_event(1111); stop |
| 6 | 1111 | 11 / 2 | 3 | 200 | trigger_event(1112); stop |
| 6 | 1112 | 11 / 1 | 3 | 100 | set_switch(9); set_switch(10); stop |
| 6 | 112 | 11 / 4 | 2 | 150 | trigger_event(1121); stop |
| 6 | 1121 | 11 / 5 | 2 | 1 | stop |
| 7 | 11 | 1 / 1 | 5 | 1 | set_switch(1); stop |
| 7 | 21 | 2 / 1 | 4 | 1 | trigger_event(211); stop |
| 7 | 211 | 2 / 2 | 3 | 200 | trigger_event(212); stop |
| 7 | 212 | 2 / 3 | 4 | 200 | set_switch(2); stop |
| 7 | 22 | 2 / 4 | 2 | 200 | trigger_event(221); stop |
| 7 | 221 | 2 / 5 | 2 | 10 | stop |
| 7 | 31 | 3 / 1 | 2 | 1 | trigger_event(311); stop |
| 7 | 311 | 3 / 2 | 3 | 100 | trigger_event(312); stop |
| 7 | 312 | 3 / 3 | 3 | 60 | set_switch(3); stop |
| 7 | 33 | 3 / 4 | 3 | 0 | trigger_event(331); stop |
| 7 | 331 | 3 / 5 | 3 | 300 | stop |
| 7 | 51 | 5 / 13 | 4 | 1 | construct_objects(room=5,group_or_wave=1); trigger_event(5101); trigger_event(5102); trigger_event(5103); trigger_event(5104); trigger_event(5105); stop |
| 7 | 5101 | 5 / 14 | 1 | 300 | set_switch(6); set_switch(7); set_switch(102); stop |
| 7 | 5102 | 5 / 1 | 1 | 30 | trigger_event(51021); stop |
| 7 | 51021 | 5 / 2 | 1 | 100 | trigger_event(51022); stop |
| 7 | 51022 | 5 / 3 | 1 | 60 | stop |
| 7 | 5103 | 5 / 4 | 1 | 1 | trigger_event(51031); stop |
| 7 | 51031 | 5 / 5 | 1 | 30 | trigger_event(51032); stop |
| 7 | 51032 | 5 / 6 | 1 | 100 | stop |
| 7 | 5104 | 5 / 7 | 1 | 100 | trigger_event(51041); stop |
| 7 | 51041 | 5 / 8 | 1 | 60 | trigger_event(51042); stop |
| 7 | 51042 | 5 / 9 | 1 | 30 | stop |
| 7 | 5105 | 5 / 10 | 1 | 30 | trigger_event(51051); stop |
| 7 | 51051 | 5 / 11 | 1 | 1 | trigger_event(51052); stop |
| 7 | 51052 | 5 / 12 | 1 | 10 | stop |
| 7 | 71 | 7 / 1 | 1 | 1 | stop |
| 7 | 81 | 8 / 1 | 6 | 1 | stop |
| 8 | 21 | 2 / 1 | 3 | 1 | trigger_event(211); stop |
| 8 | 211 | 2 / 2 | 3 | 100 | trigger_event(212); stop |
| 8 | 212 | 2 / 3 | 3 | 200 | set_switch(3); set_switch(4); set_switch(10); stop |
| 8 | 22 | 2 / 4 | 2 | 300 | trigger_event(221); stop |
| 8 | 221 | 2 / 5 | 2 | 300 | trigger_event(222); stop |
| 8 | 222 | 2 / 6 | 2 | 300 | stop |
| 8 | 24 | 2 / 7 | 2 | 100 | stop |
| 8 | 31 | 3 / 1 | 4 | 1 | trigger_event(311); stop |
| 8 | 311 | 3 / 2 | 3 | 100 | trigger_event(312); stop |
| 8 | 312 | 3 / 3 | 4 | 100 | set_switch(5); stop |
| 8 | 32 | 3 / 4 | 2 | 300 | trigger_event(321); stop |
| 8 | 321 | 3 / 5 | 2 | 300 | trigger_event(322); stop |
| 8 | 322 | 3 / 6 | 3 | 300 | stop |
| 8 | 34 | 3 / 7 | 2 | 300 | stop |
| 8 | 41 | 4 / 4 | 3 | 1 | trigger_event(411); stop |
| 8 | 411 | 4 / 5 | 2 | 500 | stop |
| 8 | 42 | 4 / 1 | 3 | 300 | trigger_event(421); stop |
| 8 | 421 | 4 / 2 | 2 | 10 | trigger_event(422); stop |
| 8 | 422 | 4 / 3 | 3 | 30 | set_switch(7); set_switch(8); set_switch(11); stop |
| 8 | 44 | 4 / 6 | 3 | 1 | stop |
| 8 | 51 | 5 / 1 | 3 | 1 | trigger_event(511); stop |
| 8 | 511 | 5 / 2 | 3 | 30 | stop |
| 8 | 53 | 5 / 3 | 6 | 1 | stop |
| 8 | 55 | 5 / 4 | 3 | 1 | stop |
| 8 | 81 | 8 / 1 | 1 | 1 | set_switch(102); set_switch(19); set_switch(18); set_switch(9); stop |
| 8 | 82 | 8 / 2 | 3 | 300 | trigger_event(821); construct_objects(room=8,group_or_wave=1); stop |
| 8 | 821 | 8 / 3 | 3 | 300 | trigger_event(822); construct_objects(room=8,group_or_wave=2); stop |
| 8 | 822 | 8 / 4 | 3 | 300 | trigger_event(823); stop |
| 8 | 823 | 8 / 5 | 3 | 300 | trigger_event(823); stop |
| 8 | 823 | 8 / 6 | 4 | 300 | set_switch(101); stop |
| 8 | 101 | 10 / 1 | 3 | 1 | trigger_event(1011); stop |
| 8 | 1011 | 10 / 2 | 3 | 1 | stop |
| 8 | 102 | 10 / 3 | 3 | 1 | trigger_event(1021); stop |
| 8 | 1021 | 10 / 4 | 3 | 1 | stop |
| 9 | 31 | 3 / 1 | 2 | 1 | trigger_event(311); trigger_event(3121); trigger_event(3111); stop |
| 9 | 311 | 3 / 2 | 2 | 30 | trigger_event(312); stop |
| 9 | 312 | 3 / 3 | 3 | 10 | trigger_event(313); stop |
| 9 | 313 | 3 / 4 | 4 | 10 | trigger_event(314); trigger_event(3122); stop |
| 9 | 314 | 3 / 5 | 2 | 10 | set_switch(2); set_switch(1); set_switch(8); set_switch(105); stop |
| 9 | 3111 | 3 / 8 | 2 | 100 | trigger_event(3112); stop |
| 9 | 3112 | 3 / 9 | 2 | 100 | trigger_event(3113); stop |
| 9 | 3113 | 3 / 10 | 2 | 100 | trigger_event(3114); stop |
| 9 | 3114 | 3 / 11 | 2 | 100 | trigger_event(3115); stop |
| 9 | 3115 | 3 / 12 | 2 | 100 | trigger_event(3116); stop |
| 9 | 3116 | 3 / 13 | 2 | 100 | trigger_event(3117); stop |
| 9 | 3117 | 3 / 14 | 2 | 100 | trigger_event(3118); stop |
| 9 | 3119 | 3 / 15 | 2 | 100 | trigger_event(3119); stop |
| 9 | 3119 | 3 / 16 | 2 | 100 | trigger_event(31110); stop |
| 9 | 31110 | 3 / 17 | 2 | 100 | trigger_event(31111); stop |
| 9 | 31111 | 3 / 18 | 2 | 100 | set_switch(101); stop |
| 9 | 3121 | 3 / 7 | 2 | 200 | stop |
| 9 | 3122 | 3 / 6 | 2 | 200 | stop |
| 9 | 71 | 7 / 1 | 3 | 1 | trigger_event(711); stop |
| 9 | 711 | 7 / 2 | 3 | 150 | trigger_event(712); stop |
| 9 | 712 | 7 / 3 | 4 | 10 | stop |
| 9 | 72 | 7 / 4 | 2 | 1 | trigger_event(721); stop |
| 9 | 721 | 7 / 5 | 3 | 1 | trigger_event(722); stop |
| 9 | 722 | 7 / 6 | 4 | 1 | trigger_event(723); stop |
| 9 | 723 | 7 / 7 | 4 | 1 | trigger_event(724); stop |
| 9 | 724 | 7 / 8 | 4 | 1 | stop |
| 9 | 91 | 9 / 1 | 1 | 400 | set_switch(6); set_switch(5); set_switch(4); set_switch(8); set_switch(100); stop |
| 9 | 92 | 9 / 2 | 3 | 1 | trigger_event(921); construct_objects(room=9,group_or_wave=1); stop |
| 9 | 921 | 9 / 3 | 4 | 1 | trigger_event(922); construct_objects(room=9,group_or_wave=2); stop |
| 9 | 922 | 9 / 4 | 4 | 1 | trigger_event(923); construct_objects(room=9,group_or_wave=3); stop |
| 9 | 923 | 9 / 5 | 4 | 100 | trigger_event(924); stop |
| 9 | 924 | 9 / 6 | 4 | 100 | trigger_event(925); stop |
| 9 | 925 | 9 / 7 | 3 | 100 | trigger_event(926); stop |
| 9 | 926 | 9 / 8 | 4 | 100 | trigger_event(927); stop |
| 9 | 927 | 9 / 9 | 4 | 100 | set_switch(102); stop |
| 9 | 111 | 11 / 1 | 4 | 1 | trigger_event(1111); stop |
| 9 | 1111 | 11 / 2 | 4 | 100 | trigger_event(1112); stop |
| 9 | 1112 | 11 / 3 | 4 | 1 | set_switch(9); set_switch(10); set_switch(11); set_switch(7); stop |
| 9 | 112 | 11 / 4 | 2 | 1 | trigger_event(1121); stop |
| 9 | 1121 | 11 / 5 | 2 | 1 | stop |
| 9 | 141 | 14 / 1 | 1 | 1 | stop |
| 9 | 51 | 5 / 1 | 0 | 1 | stop |
| 12 | 1 | 1 / 1 | 1 | 50 | construct_objects(room=1,group_or_wave=1); stop |

## Review notes

- Floor 9: event 3117 targets absent event 3118
