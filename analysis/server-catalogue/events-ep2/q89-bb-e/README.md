# Oceanic Invasion — events-ep2/q89-bb-e

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/events-ep2/q89-bb-e.zip?download=1)**

[Original QST](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/events-ep2/q89-bb-e.qst?download=1) · [Extracted BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/events-ep2/q89-bb-e/q89-bb-e.qst-quest0.bin?download=1) · [Extracted DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/events-ep2/q89-bb-e/q89-bb-e.qst-quest0.dat?download=1)

QST is the preserved original package. BIN and DAT are its decoded payload files, not reassembled scripts. The ZIP contains all three formats.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 89; language E. Static scan: **262 objects, 361 enemy/NPC records, 66 events, 255 script labels.** Script roundtrip: alignment-only.

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
| 0 | 37 | 8 | 0 |
| 11 | 225 | 353 | 66 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 11 | 101 | 52 / 1 | 7 | 0 | trigger_event(102); stop |
| 11 | 102 | 52 / 2 | 5 | 0 | trigger_event(103); stop |
| 11 | 103 | 52 / 3 | 6 | 10 | trigger_event(104); stop |
| 11 | 104 | 52 / 4 | 6 | 0 | trigger_event(105); stop |
| 11 | 105 | 52 / 5 | 2 | 20 | set_switch(101); stop |
| 11 | 106 | 81 / 6 | 3 | 100 | trigger_event(107); stop |
| 11 | 107 | 81 / 7 | 4 | 0 | trigger_event(108); stop |
| 11 | 108 | 81 / 8 | 9 | 0 | trigger_event(109); stop |
| 11 | 109 | 81 / 9 | 5 | 0 | trigger_event(110); stop |
| 11 | 110 | 81 / 10 | 6 | 0 | trigger_event(111); stop |
| 11 | 111 | 81 / 11 | 5 | 0 | set_switch(102); construct_objects(room=81,group_or_wave=7); stop |
| 11 | 112 | 51 / 12 | 5 | 0 | trigger_event(113); stop |
| 11 | 113 | 51 / 13 | 7 | 0 | trigger_event(114); stop |
| 11 | 114 | 51 / 14 | 4 | 0 | trigger_event(115); stop |
| 11 | 115 | 51 / 15 | 8 | 0 | set_switch(103); stop |
| 11 | 116 | 20 / 16 | 5 | 0 | trigger_event(118); construct_objects(room=20,group_or_wave=1); stop |
| 11 | 117 | 20 / 17 | 1 | 100 | stop |
| 11 | 118 | 20 / 18 | 4 | 0 | trigger_event(119); trigger_event(120); trigger_event(121); trigger_event(122); stop |
| 11 | 119 | 20 / 19 | 5 | 0 | trigger_event(123); stop |
| 11 | 120 | 20 / 20 | 1 | 150 | stop |
| 11 | 121 | 20 / 21 | 2 | 300 | stop |
| 11 | 122 | 20 / 22 | 3 | 500 | stop |
| 11 | 123 | 20 / 23 | 2 | 50 | set_switch(104); stop |
| 11 | 124 | 31 / 24 | 6 | 50 | trigger_event(125); stop |
| 11 | 125 | 31 / 25 | 6 | 0 | trigger_event(126); stop |
| 11 | 126 | 31 / 26 | 4 | 0 | set_switch(105); stop |
| 11 | 127 | 271 / 27 | 8 | 0 | set_switch(106); stop |
| 11 | 128 | 31 / 28 | 3 | 0 | trigger_event(129); stop |
| 11 | 129 | 31 / 29 | 3 | 0 | trigger_event(130); stop |
| 11 | 130 | 31 / 30 | 4 | 0 | construct_objects(room=31,group_or_wave=2); construct_objects(room=31,group_or_wave=5); stop |
| 11 | 131 | 31 / 31 | 2 | 100 | trigger_event(132); stop |
| 11 | 132 | 31 / 32 | 4 | 0 | construct_objects(room=31,group_or_wave=3); clear_switch(190); stop |
| 11 | 133 | 71 / 33 | 4 | 0 | trigger_event(134); stop |
| 11 | 134 | 71 / 34 | 4 | 20 | trigger_event(135); trigger_event(136); stop |
| 11 | 135 | 71 / 35 | 7 | 0 | trigger_event(137); stop |
| 11 | 136 | 71 / 36 | 2 | 100 | stop |
| 11 | 137 | 71 / 37 | 11 | 0 | trigger_event(138); stop |
| 11 | 138 | 71 / 38 | 6 | 0 | trigger_event(139); stop |
| 11 | 139 | 71 / 39 | 6 | 0 | trigger_event(140); stop |
| 11 | 140 | 71 / 40 | 6 | 0 | set_switch(107); stop |
| 11 | 141 | 90 / 41 | 10 | 0 | trigger_event(142); stop |
| 11 | 142 | 90 / 42 | 3 | 0 | trigger_event(143); stop |
| 11 | 143 | 90 / 43 | 5 | 0 | trigger_event(144); stop |
| 11 | 144 | 90 / 44 | 6 | 0 | set_switch(108); construct_objects(room=90,group_or_wave=1); stop |
| 11 | 145 | 291 / 45 | 5 | 0 | set_switch(109); stop |
| 11 | 146 | 95 / 46 | 5 | 0 | trigger_event(147); stop |
| 11 | 147 | 95 / 47 | 11 | 0 | trigger_event(148); trigger_event(149); stop |
| 11 | 148 | 95 / 48 | 4 | 0 | trigger_event(150); stop |
| 11 | 149 | 95 / 49 | 2 | 200 | stop |
| 11 | 150 | 95 / 50 | 6 | 0 | trigger_event(151); stop |
| 11 | 151 | 95 / 51 | 5 | 0 | set_switch(110); stop |
| 11 | 152 | 80 / 52 | 5 | 150 | construct_objects(room=80,group_or_wave=1); trigger_event(153); stop |
| 11 | 153 | 80 / 53 | 4 | 0 | trigger_event(154); stop |
| 11 | 154 | 80 / 54 | 9 | 0 | trigger_event(155); stop |
| 11 | 155 | 80 / 55 | 9 | 0 | construct_objects(room=80,group_or_wave=2); trigger_event(156); stop |
| 11 | 156 | 80 / 56 | 6 | 0 | trigger_event(157); stop |
| 11 | 157 | 80 / 57 | 7 | 0 | trigger_event(158); stop |
| 11 | 158 | 80 / 58 | 5 | 0 | construct_objects(room=80,group_or_wave=3); construct_objects(room=80,group_or_wave=4); set_switch(111); clear_switch(191); stop |
| 11 | 159 | 50 / 59 | 8 | 0 | trigger_event(160); stop |
| 11 | 160 | 50 / 60 | 8 | 0 | set_switch(112); stop |
| 11 | 161 | 70 / 61 | 6 | 0 | trigger_event(162); stop |
| 11 | 162 | 70 / 62 | 4 | 0 | construct_objects(room=70,group_or_wave=1); trigger_event(163); stop |
| 11 | 163 | 70 / 63 | 6 | 0 | trigger_event(164); stop |
| 11 | 164 | 70 / 64 | 6 | 0 | clear_switch(192); construct_objects(room=70,group_or_wave=2); trigger_event(165); stop |
| 11 | 165 | 70 / 65 | 12 | 0 | trigger_event(166); stop |
| 11 | 166 | 70 / 66 | 5 | 0 | clear_switch(193); set_switch(113); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
