# ステージ３ — challenge-ep2/d88203-bb-j

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/challenge-ep2/d88203-bb-j.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/challenge-ep2/d88203-bb-j.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/challenge-ep2/d88203-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 65535; language J. Static scan: **949 objects, 460 enemy/NPC records, 182 events, 54 script labels.** Script roundtrip: alignment-only.

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
0x01, 0x18, 0x00, 0x00, 0x00
0x02, 0x19, 0x00, 0x00, 0x00
0x03, 0x1A, 0x00, 0x02, 0x00
0x04, 0x1B, 0x00, 0x00, 0x00
0x05, 0x17, 0x00, 0x00, 0x00
0x0C, 0x1E, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 40 | 12 | 0 |
| 1 | 175 | 62 | 25 |
| 2 | 147 | 87 | 41 |
| 3 | 241 | 114 | 36 |
| 4 | 207 | 90 | 37 |
| 5 | 133 | 94 | 42 |
| 12 | 6 | 1 | 1 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 11 | 1 / 1 | 2 | 1 | stop |
| 1 | 31 | 3 / 1 | 2 | 10 | trigger_event(311); stop |
| 1 | 311 | 3 / 2 | 3 | 100 | trigger_event(312); stop |
| 1 | 312 | 3 / 3 | 1 | 100 | set_switch(1); set_switch(2); set_switch(5); set_switch(8); set_switch(13); set_switch(16); construct_objects(room=3,group_or_wave=1); stop |
| 1 | 32 | 3 / 4 | 2 | 100 | trigger_event(321); stop |
| 1 | 321 | 3 / 5 | 3 | 10 | stop |
| 1 | 33 | 3 / 6 | 3 | 10 | stop |
| 1 | 41 | 4 / 1 | 2 | 10 | trigger_event(411); stop |
| 1 | 411 | 4 / 2 | 3 | 100 | set_switch(9); set_switch(10); set_switch(12); set_switch(14); set_switch(15); stop |
| 1 | 42 | 4 / 3 | 2 | 100 | stop |
| 1 | 43 | 4 / 4 | 3 | 10 | stop |
| 1 | 71 | 7 / 1 | 3 | 10 | stop |
| 1 | 111 | 11 / 1 | 3 | 100 | trigger_event(1111); stop |
| 1 | 1111 | 11 / 2 | 4 | 10 | trigger_event(1112); stop |
| 1 | 1112 | 11 / 3 | 3 | 100 | set_switch(6); stop |
| 1 | 112 | 11 / 4 | 2 | 10 | trigger_event(1121); stop |
| 1 | 1121 | 11 / 5 | 2 | 100 | stop |
| 1 | 113 | 11 / 6 | 1 | 10 | stop |
| 1 | 121 | 12 / 1 | 2 | 60 | construct_objects(room=12,group_or_wave=2); stop |
| 1 | 151 | 15 / 1 | 3 | 10 | trigger_event(1511); stop |
| 1 | 1511 | 15 / 2 | 3 | 100 | trigger_event(1512); stop |
| 1 | 1512 | 15 / 3 | 3 | 100 | set_switch(1); set_switch(2); stop |
| 1 | 152 | 15 / 4 | 2 | 100 | trigger_event(1521); stop |
| 1 | 1521 | 15 / 5 | 4 | 100 | stop |
| 1 | 153 | 15 / 6 | 1 | 10 | set_switch(4); stop |
| 2 | 21 | 2 / 1 | 1 | 100 | construct_objects(room=2,group_or_wave=4); set_switch(105); stop |
| 2 | 31 | 3 / 1 | 4 | 10 | trigger_event(311); stop |
| 2 | 311 | 3 / 2 | 3 | 100 | trigger_event(312); stop |
| 2 | 312 | 3 / 3 | 3 | 10 | set_switch(3); stop |
| 2 | 32 | 3 / 4 | 2 | 100 | trigger_event(321); stop |
| 2 | 321 | 3 / 5 | 3 | 100 | stop |
| 2 | 41 | 4 / 1 | 3 | 1 | stop |
| 2 | 51 | 5 / 1 | 3 | 10 | set_switch(5); set_switch(4); stop |
| 2 | 52 | 5 / 2 | 1 | 10 | trigger_event(521); stop |
| 2 | 521 | 5 / 3 | 1 | 30 | trigger_event(522); stop |
| 2 | 522 | 5 / 4 | 1 | 10 | construct_objects(room=5,group_or_wave=1); stop |
| 2 | 53 | 5 / 5 | 1 | 100 | trigger_event(531); stop |
| 2 | 531 | 5 / 6 | 1 | 10 | trigger_event(532); stop |
| 2 | 532 | 5 / 7 | 1 | 10 | construct_objects(room=5,group_or_wave=2); stop |
| 2 | 54 | 5 / 8 | 1 | 60 | trigger_event(541); stop |
| 2 | 541 | 5 / 9 | 1 | 10 | trigger_event(542); stop |
| 2 | 542 | 5 / 10 | 1 | 100 | construct_objects(room=5,group_or_wave=3); stop |
| 2 | 55 | 5 / 11 | 1 | 120 | trigger_event(551); stop |
| 2 | 551 | 5 / 12 | 1 | 120 | trigger_event(552); stop |
| 2 | 552 | 5 / 13 | 1 | 10 | stop |
| 2 | 56 | 5 / 14 | 1 | 30 | trigger_event(561); stop |
| 2 | 561 | 5 / 15 | 1 | 100 | trigger_event(562); stop |
| 2 | 562 | 5 / 16 | 1 | 100 | stop |
| 2 | 61 | 6 / 1 | 3 | 10 | trigger_event(611); stop |
| 2 | 611 | 6 / 2 | 4 | 60 | trigger_event(612); stop |
| 2 | 612 | 6 / 3 | 4 | 60 | set_switch(6); stop |
| 2 | 62 | 6 / 4 | 2 | 200 | trigger_event(621); stop |
| 2 | 621 | 6 / 5 | 3 | 200 | stop |
| 2 | 72 | 7 / 1 | 3 | 10 | trigger_event(721); stop |
| 2 | 721 | 7 / 2 | 4 | 100 | trigger_event(722); stop |
| 2 | 722 | 7 / 3 | 2 | 10 | stop |
| 2 | 71 | 7 / 4 | 2 | 100 | trigger_event(711); stop |
| 2 | 711 | 7 / 5 | 1 | 100 | stop |
| 2 | 81 | 8 / 1 | 3 | 10 | trigger_event(811); stop |
| 2 | 811 | 8 / 2 | 3 | 10 | trigger_event(812); stop |
| 2 | 812 | 8 / 3 | 4 | 10 | trigger_event(813); stop |
| 2 | 813 | 8 / 4 | 4 | 100 | set_switch(7); stop |
| 2 | 82 | 8 / 5 | 2 | 100 | trigger_event(821); stop |
| 2 | 821 | 8 / 6 | 2 | 10 | stop |
| 2 | 83 | 8 / 7 | 2 | 200 | trigger_event(831); stop |
| 2 | 831 | 8 / 8 | 2 | 100 | stop |
| 3 | 21 | 2 / 1 | 3 | 100 | trigger_event(211); construct_objects(room=2,group_or_wave=1); stop |
| 3 | 211 | 2 / 2 | 3 | 60 | trigger_event(212); construct_objects(room=2,group_or_wave=2); stop |
| 3 | 212 | 2 / 3 | 3 | 30 | trigger_event(213); construct_objects(room=2,group_or_wave=3); stop |
| 3 | 213 | 2 / 4 | 3 | 100 | trigger_event(214); construct_objects(room=2,group_or_wave=4); stop |
| 3 | 214 | 2 / 5 | 3 | 60 | set_switch(1); set_switch(4); set_switch(10); stop |
| 3 | 22 | 2 / 6 | 2 | 10 | trigger_event(221); stop |
| 3 | 221 | 2 / 7 | 2 | 10 | trigger_event(222); stop |
| 3 | 222 | 2 / 8 | 2 | 100 | trigger_event(223); stop |
| 3 | 23 | 2 / 9 | 2 | 150 | trigger_event(231); stop |
| 3 | 231 | 2 / 10 | 2 | 100 | trigger_event(232); stop |
| 3 | 232 | 2 / 11 | 2 | 10 | trigger_event(233); stop |
| 3 | 31 | 3 / 1 | 3 | 10 | trigger_event(311); construct_objects(room=3,group_or_wave=1); stop |
| 3 | 311 | 3 / 2 | 3 | 100 | trigger_event(312); construct_objects(room=3,group_or_wave=2); stop |
| 3 | 312 | 3 / 3 | 3 | 10 | trigger_event(313); construct_objects(room=3,group_or_wave=3); stop |
| 3 | 313 | 3 / 4 | 3 | 100 | trigger_event(314); construct_objects(room=3,group_or_wave=4); stop |
| 3 | 314 | 3 / 5 | 3 | 10 | set_switch(5); stop |
| 3 | 32 | 3 / 6 | 2 | 10 | trigger_event(321); stop |
| 3 | 321 | 3 / 7 | 3 | 10 | trigger_event(322); stop |
| 3 | 322 | 3 / 8 | 4 | 10 | trigger_event(323); stop |
| 3 | 323 | 3 / 9 | 4 | 10 | stop |
| 3 | 51 | 5 / 1 | 3 | 10 | trigger_event(511); construct_objects(room=5,group_or_wave=1); stop |
| 3 | 511 | 5 / 2 | 3 | 100 | trigger_event(512); construct_objects(room=5,group_or_wave=2); stop |
| 3 | 512 | 5 / 3 | 3 | 10 | trigger_event(513); construct_objects(room=5,group_or_wave=3); stop |
| 3 | 513 | 5 / 4 | 3 | 100 | trigger_event(514); construct_objects(room=5,group_or_wave=4); stop |
| 3 | 514 | 5 / 5 | 3 | 10 | set_switch(15); set_switch(16); stop |
| 3 | 52 | 5 / 6 | 2 | 10 | trigger_event(521); stop |
| 3 | 521 | 5 / 7 | 3 | 10 | trigger_event(522); stop |
| 3 | 522 | 5 / 8 | 2 | 10 | trigger_event(523); stop |
| 3 | 523 | 5 / 9 | 4 | 10 | stop |
| 3 | 81 | 8 / 1 | 6 | 10 | trigger_event(811); construct_objects(room=8,group_or_wave=1); stop |
| 3 | 811 | 8 / 2 | 6 | 10 | trigger_event(812); construct_objects(room=8,group_or_wave=3); stop |
| 3 | 812 | 8 / 3 | 4 | 10 | trigger_event(813); construct_objects(room=8,group_or_wave=2); stop |
| 3 | 813 | 8 / 4 | 7 | 10 | trigger_event(814); construct_objects(room=8,group_or_wave=4); stop |
| 3 | 814 | 8 / 5 | 8 | 100 | set_switch(9); set_switch(18); set_switch(19); stop |
| 3 | 41 | 4 / 1 | 1 | 10 | construct_objects(room=4,group_or_wave=1); set_switch(105); stop |
| 3 | 101 | 10 / 1 | 1 | 10 | stop |
| 4 | 31 | 3 / 1 | 3 | 10 | trigger_event(311); stop |
| 4 | 311 | 3 / 2 | 2 | 10 | trigger_event(312); stop |
| 4 | 312 | 3 / 3 | 3 | 10 | trigger_event(313); stop |
| 4 | 313 | 3 / 4 | 3 | 10 | trigger_event(314); stop |
| 4 | 314 | 3 / 5 | 3 | 10 | trigger_event(315); stop |
| 4 | 315 | 3 / 6 | 2 | 10 | trigger_event(316); stop |
| 4 | 316 | 3 / 7 | 3 | 10 | trigger_event(317); stop |
| 4 | 317 | 3 / 8 | 2 | 10 | construct_objects(room=3,group_or_wave=1); set_switch(1); stop |
| 4 | 32 | 3 / 9 | 2 | 100 | trigger_event(321); stop |
| 4 | 321 | 3 / 10 | 2 | 100 | trigger_event(322); stop |
| 4 | 322 | 3 / 11 | 2 | 10 | trigger_event(323); stop |
| 4 | 323 | 3 / 12 | 3 | 100 | trigger_event(324); stop |
| 4 | 324 | 3 / 13 | 2 | 10 | stop |
| 4 | 33 | 3 / 14 | 2 | 10 | trigger_event(331); stop |
| 4 | 331 | 3 / 15 | 2 | 10 | trigger_event(332); stop |
| 4 | 332 | 3 / 16 | 2 | 10 | trigger_event(333); stop |
| 4 | 333 | 3 / 17 | 2 | 10 | trigger_event(334); stop |
| 4 | 334 | 3 / 18 | 2 | 10 | trigger_event(335); stop |
| 4 | 335 | 3 / 19 | 2 | 10 | trigger_event(336); stop |
| 4 | 336 | 3 / 20 | 2 | 10 | trigger_event(337); stop |
| 4 | 71 | 7 / 1 | 3 | 200 | trigger_event(711); stop |
| 4 | 711 | 7 / 2 | 2 | 10 | trigger_event(712); stop |
| 4 | 712 | 7 / 3 | 3 | 10 | set_switch(2); set_switch(3); stop |
| 4 | 72 | 7 / 4 | 3 | 10 | trigger_event(721); stop |
| 4 | 721 | 7 / 5 | 3 | 100 | stop |
| 4 | 73 | 7 / 6 | 1 | 10 | stop |
| 4 | 91 | 9 / 1 | 2 | 200 | trigger_event(911); stop |
| 4 | 911 | 9 / 2 | 3 | 10 | trigger_event(912); stop |
| 4 | 912 | 9 / 3 | 3 | 10 | trigger_event(913); stop |
| 4 | 913 | 9 / 4 | 3 | 100 | construct_objects(room=9,group_or_wave=2); set_switch(4); set_switch(5); stop |
| 4 | 92 | 9 / 5 | 3 | 100 | trigger_event(921); stop |
| 4 | 921 | 9 / 6 | 3 | 100 | trigger_event(922); stop |
| 4 | 922 | 9 / 7 | 3 | 10 | stop |
| 4 | 93 | 9 / 8 | 3 | 10 | set_switch(120); stop |
| 4 | 101 | 10 / 1 | 2 | 10 | construct_objects(room=10,group_or_wave=3); stop |
| 4 | 111 | 11 / 1 | 1 | 150 | construct_objects(room=11,group_or_wave=5); set_switch(121); stop |
| 4 | 131 | 13 / 1 | 3 | 10 | construct_objects(room=13,group_or_wave=4); set_switch(7); set_switch(11); stop |
| 5 | 21 | 2 / 1 | 2 | 10 | trigger_event(211); stop |
| 5 | 211 | 2 / 2 | 2 | 100 | trigger_event(212); stop |
| 5 | 212 | 2 / 3 | 1 | 10 | set_switch(1); stop |
| 5 | 22 | 2 / 4 | 1 | 150 | trigger_event(221); stop |
| 5 | 221 | 2 / 5 | 2 | 150 | stop |
| 5 | 31 | 3 / 1 | 1 | 100 | construct_objects(room=3,group_or_wave=6); set_switch(2); stop |
| 5 | 32 | 3 / 2 | 3 | 10 | trigger_event(321); stop |
| 5 | 321 | 3 / 3 | 3 | 10 | trigger_event(322); stop |
| 5 | 322 | 3 / 4 | 4 | 10 | stop |
| 5 | 41 | 4 / 1 | 1 | 300 | construct_objects(room=4,group_or_wave=5); set_switch(3); stop |
| 5 | 42 | 4 / 2 | 4 | 10 | trigger_event(421); stop |
| 5 | 421 | 4 / 3 | 3 | 100 | trigger_event(422); stop |
| 5 | 422 | 4 / 4 | 4 | 10 | stop |
| 5 | 51 | 5 / 1 | 1 | 10 | construct_objects(room=5,group_or_wave=4); set_switch(4); stop |
| 5 | 52 | 5 / 2 | 3 | 100 | trigger_event(521); stop |
| 5 | 521 | 5 / 3 | 4 | 10 | trigger_event(522); stop |
| 5 | 522 | 5 / 4 | 4 | 10 | stop |
| 5 | 61 | 6 / 1 | 2 | 10 | stop |
| 5 | 81 | 8 / 1 | 1 | 10 | stop |
| 5 | 91 | 9 / 1 | 1 | 10 | stop |
| 5 | 101 | 10 / 1 | 1 | 10 | stop |
| 5 | 111 | 11 / 1 | 4 | 10 | trigger_event(1111); stop |
| 5 | 1111 | 11 / 2 | 2 | 100 | trigger_event(1112); stop |
| 5 | 1112 | 11 / 3 | 2 | 10 | construct_objects(room=11,group_or_wave=1); set_switch(102); stop |
| 5 | 112 | 11 / 4 | 2 | 10 | trigger_event(1121); stop |
| 5 | 1121 | 11 / 5 | 2 | 10 | stop |
| 5 | 113 | 11 / 6 | 2 | 100 | trigger_event(1131); stop |
| 5 | 1131 | 11 / 7 | 2 | 10 | stop |
| 5 | 121 | 12 / 1 | 2 | 10 | trigger_event(1211); stop |
| 5 | 1211 | 12 / 2 | 3 | 100 | trigger_event(1212); stop |
| 5 | 1212 | 12 / 3 | 2 | 10 | construct_objects(room=12,group_or_wave=2); set_switch(101); stop |
| 5 | 122 | 12 / 4 | 2 | 10 | trigger_event(1221); stop |
| 5 | 1221 | 12 / 5 | 2 | 10 | stop |
| 5 | 123 | 12 / 6 | 2 | 100 | trigger_event(1231); stop |
| 5 | 1231 | 12 / 7 | 2 | 10 | stop |
| 5 | 131 | 13 / 1 | 2 | 10 | trigger_event(1311); stop |
| 5 | 1311 | 13 / 2 | 2 | 100 | trigger_event(1312); stop |
| 5 | 1312 | 13 / 3 | 3 | 10 | construct_objects(room=13,group_or_wave=3); set_switch(100); stop |
| 5 | 132 | 13 / 4 | 2 | 10 | trigger_event(1321); stop |
| 5 | 1321 | 13 / 5 | 2 | 10 | stop |
| 5 | 133 | 13 / 6 | 2 | 100 | trigger_event(1331); stop |
| 5 | 1331 | 13 / 7 | 2 | 10 | stop |
| 12 | 1 | 1 / 1 | 1 | 50 | construct_objects(room=1,group_or_wave=1); stop |

## Review notes

- Floor 3: event 222 targets absent event 223
- Floor 3: event 232 targets absent event 233
- Floor 4: event 336 targets absent event 337

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
