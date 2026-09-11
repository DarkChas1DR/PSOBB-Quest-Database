# Hazardous Dimension — vr-ep1/q85-bb-j

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/vr-ep1/q85-bb-j.zip?download=1)**

[Original QST](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/vr-ep1/q85-bb-j.qst?download=1) · [Extracted BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/vr-ep1/q85-bb-j/q85-bb-j.qst-quest0.bin?download=1) · [Extracted DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/vr-ep1/q85-bb-j/q85-bb-j.qst-quest0.dat?download=1)

QST is the preserved original package. BIN and DAT are its decoded payload files, not reassembled scripts. The ZIP contains all three formats.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 85; language J. Static scan: **443 objects, 482 enemy/NPC records, 76 events, 215 script labels.** Script roundtrip: alignment-only.

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
| 0 | 28 | 8 | 0 |
| 9 | 61 | 94 | 11 |
| 10 | 308 | 379 | 64 |
| 14 | 46 | 1 | 1 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 9 | 101 | 80 / 1 | 5 | 100 | trigger_event(102); stop |
| 9 | 102 | 80 / 2 | 7 | 0 | trigger_event(103); stop |
| 9 | 103 | 80 / 3 | 10 | 0 | trigger_event(104); stop |
| 9 | 104 | 80 / 4 | 6 | 0 | trigger_event(105); stop |
| 9 | 105 | 80 / 5 | 4 | 0 | trigger_event(106); stop |
| 9 | 106 | 80 / 6 | 10 | 0 | trigger_event(107); stop |
| 9 | 107 | 80 / 7 | 9 | 0 | trigger_event(108); stop |
| 9 | 108 | 80 / 8 | 10 | 0 | trigger_event(109); stop |
| 9 | 109 | 80 / 9 | 6 | 0 | trigger_event(110); stop |
| 9 | 110 | 80 / 10 | 15 | 0 | trigger_event(111); stop |
| 9 | 111 | 80 / 11 | 12 | 0 | construct_objects(room=80,group_or_wave=1); stop |
| 10 | 101 | 42 / 1 | 5 | 100 | trigger_event(102); stop |
| 10 | 102 | 42 / 2 | 6 | 0 | trigger_event(103); stop |
| 10 | 103 | 42 / 3 | 6 | 0 | trigger_event(104); trigger_event(106); stop |
| 10 | 104 | 42 / 4 | 7 | 0 | trigger_event(105); stop |
| 10 | 105 | 42 / 5 | 5 | 0 | set_switch(101); construct_objects(room=42,group_or_wave=1); stop |
| 10 | 106 | 42 / 6 | 0 | 400 | stop |
| 10 | 107 | 33 / 7 | 4 | 20 | trigger_event(108); stop |
| 10 | 108 | 33 / 8 | 7 | 0 | trigger_event(109); stop |
| 10 | 109 | 33 / 9 | 7 | 0 | trigger_event(110); stop |
| 10 | 110 | 33 / 10 | 4 | 0 | set_switch(102); stop |
| 10 | 111 | 20 / 11 | 4 | 0 | trigger_event(112); trigger_event(114); stop |
| 10 | 112 | 20 / 12 | 5 | 0 | trigger_event(113); stop |
| 10 | 113 | 20 / 13 | 5 | 0 | set_switch(103); stop |
| 10 | 114 | 20 / 14 | 0 | 800 | stop |
| 10 | 115 | 41 / 15 | 5 | 200 | trigger_event(116); stop |
| 10 | 116 | 41 / 16 | 5 | 0 | trigger_event(117); stop |
| 10 | 117 | 41 / 17 | 6 | 0 | trigger_event(118); stop |
| 10 | 118 | 41 / 18 | 7 | 0 | trigger_event(119); stop |
| 10 | 119 | 41 / 19 | 11 | 0 | set_switch(104); clear_switch(79); clear_switch(80); construct_objects(room=41,group_or_wave=3); stop |
| 10 | 120 | 23 / 20 | 9 | 0 | trigger_event(121); stop |
| 10 | 121 | 23 / 21 | 9 | 0 | trigger_event(122); stop |
| 10 | 122 | 23 / 22 | 7 | 0 | set_switch(105); stop |
| 10 | 123 | 40 / 23 | 5 | 0 | trigger_event(124); stop |
| 10 | 124 | 40 / 24 | 4 | 0 | trigger_event(125); stop |
| 10 | 125 | 40 / 25 | 7 | 0 | trigger_event(126); stop |
| 10 | 126 | 40 / 26 | 5 | 0 | trigger_event(127); trigger_event(128); stop |
| 10 | 127 | 40 / 27 | 7 | 0 | set_switch(106); stop |
| 10 | 128 | 40 / 28 | 4 | 400 | construct_objects(room=7,group_or_wave=1); stop |
| 10 | 129 | 50 / 29 | 6 | 0 | trigger_event(130); trigger_event(131); stop |
| 10 | 130 | 50 / 30 | 2 | 0 | set_switch(107); construct_objects(room=50,group_or_wave=1); stop |
| 10 | 131 | 50 / 31 | 2 | 250 | stop |
| 10 | 132 | 22 / 32 | 8 | 0 | trigger_event(133); stop |
| 10 | 133 | 22 / 33 | 4 | 0 | trigger_event(134); stop |
| 10 | 134 | 22 / 34 | 6 | 0 | set_switch(108); stop |
| 10 | 135 | 65 / 35 | 6 | 0 | trigger_event(136); stop |
| 10 | 136 | 65 / 36 | 5 | 50 | trigger_event(137); stop |
| 10 | 137 | 65 / 37 | 4 | 0 | set_switch(109); stop |
| 10 | 138 | 32 / 38 | 4 | 0 | trigger_event(139); stop |
| 10 | 139 | 32 / 39 | 6 | 0 | trigger_event(140); stop |
| 10 | 140 | 32 / 40 | 8 | 0 | trigger_event(141); stop |
| 10 | 141 | 32 / 41 | 8 | 0 | set_switch(110); construct_objects(room=32,group_or_wave=1); stop |
| 10 | 142 | 55 / 42 | 4 | 50 | trigger_event(143); stop |
| 10 | 143 | 55 / 43 | 4 | 0 | trigger_event(144); stop |
| 10 | 144 | 55 / 44 | 6 | 0 | set_switch(68); set_switch(111); construct_objects(room=55,group_or_wave=1); stop |
| 10 | 145 | 31 / 45 | 4 | 200 | trigger_event(146); stop |
| 10 | 146 | 31 / 46 | 5 | 0 | trigger_event(147); stop |
| 10 | 147 | 31 / 47 | 8 | 0 | trigger_event(148); stop |
| 10 | 148 | 31 / 48 | 5 | 0 | set_switch(112); construct_objects(room=31,group_or_wave=1); clear_switch(68); stop |
| 10 | 149 | 70 / 49 | 8 | 0 | set_switch(113); construct_objects(room=70,group_or_wave=1); stop |
| 10 | 150 | 30 / 50 | 5 | 0 | trigger_event(151); stop |
| 10 | 151 | 30 / 51 | 6 | 0 | trigger_event(152); stop |
| 10 | 152 | 30 / 52 | 8 | 0 | trigger_event(153); stop |
| 10 | 153 | 30 / 53 | 8 | 0 | set_switch(114); stop |
| 10 | 154 | 43 / 54 | 4 | 0 | trigger_event(155); stop |
| 10 | 155 | 43 / 55 | 7 | 0 | trigger_event(156); stop |
| 10 | 156 | 43 / 56 | 5 | 0 | set_switch(115); construct_objects(room=43,group_or_wave=1); clear_switch(64); stop |
| 10 | 157 | 85 / 57 | 10 | 30 | set_switch(116); stop |
| 10 | 158 | 80 / 58 | 7 | 0 | trigger_event(159); stop |
| 10 | 159 | 80 / 59 | 7 | 0 | trigger_event(160); stop |
| 10 | 160 | 80 / 60 | 8 | 0 | trigger_event(161); set_switch(64); stop |
| 10 | 161 | 80 / 61 | 6 | 0 | trigger_event(162); stop |
| 10 | 162 | 80 / 62 | 9 | 0 | trigger_event(163); stop |
| 10 | 163 | 80 / 63 | 5 | 0 | trigger_event(164); stop |
| 10 | 164 | 80 / 64 | 15 | 0 | set_switch(117); clear_switch(64); construct_objects(room=80,group_or_wave=1); stop |
| 14 | 1 | 0 / 1 | 1 | 50 | construct_objects(room=0,group_or_wave=1); construct_objects(room=1,group_or_wave=1); construct_objects(room=2,group_or_wave=1); clear_switch(50); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
