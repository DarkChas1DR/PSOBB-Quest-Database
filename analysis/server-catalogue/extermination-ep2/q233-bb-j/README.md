# 幻界の果てに １ — extermination-ep2/q233-bb-j

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/extermination-ep2/q233-bb-j.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/extermination-ep2/q233-bb-j.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/extermination-ep2/q233-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 233; language J. Static scan: **418 objects, 381 enemy/NPC records, 93 events, 126 script labels.** Script roundtrip: byte-identical.

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
0x06, 0x18, 0x00, 0x00, 0x00
0x09, 0x1B, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 44 | 20 | 0 |
| 6 | 126 | 203 | 52 |
| 9 | 248 | 158 | 41 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 6 | 151 | 15 / 1 | 6 | 10 | trigger_event(1511); stop |
| 6 | 1511 | 15 / 2 | 4 | 10 | trigger_event(1512); stop |
| 6 | 1512 | 15 / 3 | 6 | 180 | trigger_event(1513); stop |
| 6 | 1513 | 15 / 4 | 4 | 10 | set_switch(4); set_switch(5); stop |
| 6 | 152 | 15 / 5 | 1 | 10 | stop |
| 6 | 153 | 15 / 6 | 1 | 10 | stop |
| 6 | 154 | 15 / 7 | 1 | 10 | stop |
| 6 | 31 | 3 / 1 | 5 | 10 | trigger_event(311); stop |
| 6 | 311 | 3 / 2 | 3 | 10 | trigger_event(312); stop |
| 6 | 312 | 3 / 3 | 6 | 120 | trigger_event(313); stop |
| 6 | 313 | 3 / 4 | 4 | 10 | trigger_event(314); stop |
| 6 | 314 | 3 / 5 | 1 | 180 | trigger_event(315); stop |
| 6 | 315 | 3 / 6 | 8 | 10 | set_switch(13); stop |
| 6 | 11 | 1 / 1 | 1 | 10 | trigger_event(111); stop |
| 6 | 111 | 1 / 2 | 3 | 10 | trigger_event(112); stop |
| 6 | 112 | 1 / 3 | 6 | 120 | trigger_event(113); stop |
| 6 | 113 | 1 / 4 | 7 | 10 | trigger_event(114); stop |
| 6 | 114 | 1 / 5 | 4 | 120 | construct_objects(room=1,group_or_wave=1); stop |
| 6 | 41 | 4 / 1 | 5 | 10 | trigger_event(411); stop |
| 6 | 411 | 4 / 2 | 6 | 10 | trigger_event(412); stop |
| 6 | 412 | 4 / 3 | 6 | 180 | trigger_event(413); stop |
| 6 | 413 | 4 / 4 | 5 | 10 | trigger_event(414); stop |
| 6 | 414 | 4 / 5 | 3 | 10 | trigger_event(415); stop |
| 6 | 415 | 4 / 6 | 6 | 120 | trigger_event(416); stop |
| 6 | 416 | 4 / 7 | 2 | 10 | trigger_event(417); stop |
| 6 | 417 | 4 / 8 | 2 | 10 | set_switch(11); stop |
| 6 | 42 | 4 / 9 | 1 | 10 | stop |
| 6 | 11123 | 11 / 1 | 4 | 10 | trigger_event(1111); stop |
| 6 | 1111 | 11 / 2 | 4 | 10 | trigger_event(1112); stop |
| 6 | 1112 | 11 / 3 | 4 | 10 | trigger_event(1113); stop |
| 6 | 1113 | 11 / 4 | 6 | 10 | trigger_event(1114); stop |
| 6 | 1114 | 11 / 5 | 4 | 10 | trigger_event(1115); stop |
| 6 | 1115 | 11 / 6 | 6 | 10 | trigger_event(1116); stop |
| 6 | 1116 | 11 / 7 | 7 | 10 | construct_objects(room=11,group_or_wave=4); stop |
| 6 | 1117 | 11 / 8 | 2 | 180 | trigger_event(1118); stop |
| 6 | 1118 | 11 / 9 | 3 | 10 | trigger_event(1119); stop |
| 6 | 1119 | 11 / 10 | 3 | 10 | trigger_event(11110); stop |
| 6 | 11110 | 11 / 11 | 3 | 10 | trigger_event(11111); stop |
| 6 | 11111 | 11 / 12 | 3 | 10 | trigger_event(11112); stop |
| 6 | 11112 | 11 / 13 | 3 | 10 | trigger_event(11113); stop |
| 6 | 11113 | 11 / 14 | 4 | 10 | trigger_event(11124); stop |
| 6 | 11124 | 11 / 15 | 4 | 10 | set_switch(100); stop |
| 6 | 11116 | 11 / 17 | 5 | 180 | trigger_event(11117); stop |
| 6 | 11117 | 11 / 18 | 3 | 10 | trigger_event(11118); stop |
| 6 | 11118 | 11 / 19 | 3 | 10 | trigger_event(11119); stop |
| 6 | 11119 | 11 / 20 | 3 | 10 | trigger_event(11120); stop |
| 6 | 11120 | 11 / 21 | 4 | 10 | trigger_event(11121); stop |
| 6 | 11121 | 11 / 22 | 3 | 10 | trigger_event(11122); stop |
| 6 | 11122 | 11 / 23 | 4 | 10 | trigger_event(11125); stop |
| 6 | 11125 | 11 / 24 | 4 | 10 | set_switch(101); stop |
| 6 | 11114 | 11 / 25 | 6 | 360 | set_switch(3); set_switch(6); construct_objects(room=15,group_or_wave=3); stop |
| 6 | 121 | 12 / 1 | 1 | 10 | stop |
| 9 | 141 | 14 / 1 | 1 | 30 | stop |
| 9 | 11 | 11 / 1 | 4 | 30 | trigger_event(111); stop |
| 9 | 111 | 11 / 2 | 1 | 60 | trigger_event(112); stop |
| 9 | 112 | 11 / 3 | 3 | 120 | set_switch(8); stop |
| 9 | 9 | 9 / 1 | 4 | 30 | trigger_event(91); stop |
| 9 | 91 | 9 / 2 | 5 | 30 | set_switch(150); stop |
| 9 | 3 | 3 / 1 | 6 | 30 | trigger_event(31); stop |
| 9 | 31 | 3 / 2 | 5 | 30 | trigger_event(32); stop |
| 9 | 32 | 3 / 3 | 8 | 60 | trigger_event(33); stop |
| 9 | 33 | 3 / 4 | 3 | 30 | set_switch(1); set_switch(3); stop |
| 9 | 1 | 1 / 1 | 1 | 30 | stop |
| 9 | 71 | 7 / 1 | 4 | 60 | trigger_event(711); stop |
| 9 | 711 | 7 / 2 | 4 | 30 | trigger_event(712); stop |
| 9 | 712 | 7 / 3 | 4 | 30 | trigger_event(713); stop |
| 9 | 713 | 7 / 4 | 4 | 30 | trigger_event(714); stop |
| 9 | 714 | 7 / 5 | 4 | 60 | trigger_event(715); stop |
| 9 | 715 | 7 / 6 | 3 | 60 | trigger_event(716); stop |
| 9 | 716 | 7 / 7 | 3 | 30 | trigger_event(717); stop |
| 9 | 717 | 7 / 8 | 4 | 30 | trigger_event(718); stop |
| 9 | 718 | 7 / 9 | 2 | 60 | trigger_event(719); stop |
| 9 | 719 | 7 / 10 | 5 | 60 | trigger_event(7111); stop |
| 9 | 7111 | 7 / 11 | 2 | 30 | trigger_event(7112); stop |
| 9 | 7112 | 7 / 12 | 5 | 30 | trigger_event(7113); stop |
| 9 | 7113 | 7 / 13 | 5 | 90 | trigger_event(7114); stop |
| 9 | 7114 | 7 / 14 | 4 | 30 | trigger_event(7115); stop |
| 9 | 7115 | 7 / 15 | 3 | 60 | trigger_event(7116); stop |
| 9 | 7116 | 7 / 16 | 5 | 45 | trigger_event(7117); stop |
| 9 | 7117 | 7 / 17 | 6 | 30 | trigger_event(7118); stop |
| 9 | 7118 | 7 / 18 | 6 | 30 | set_switch(100); stop |
| 9 | 72 | 7 / 19 | 2 | 120 | trigger_event(721); stop |
| 9 | 721 | 7 / 20 | 3 | 150 | trigger_event(722); stop |
| 9 | 722 | 7 / 21 | 4 | 150 | trigger_event(723); stop |
| 9 | 723 | 7 / 22 | 3 | 150 | trigger_event(724); stop |
| 9 | 724 | 7 / 23 | 3 | 150 | construct_objects(room=7,group_or_wave=1); stop |
| 9 | 73 | 7 / 24 | 3 | 150 | trigger_event(731); stop |
| 9 | 731 | 7 / 25 | 1 | 150 | trigger_event(732); stop |
| 9 | 732 | 7 / 26 | 4 | 150 | trigger_event(733); stop |
| 9 | 733 | 7 / 27 | 1 | 150 | trigger_event(734); stop |
| 9 | 734 | 7 / 28 | 6 | 150 | set_switch(101); stop |
| 9 | 74 | 7 / 29 | 6 | 60 | trigger_event(741); stop |
| 9 | 741 | 7 / 30 | 8 | 120 | set_switch(4); set_switch(5); set_switch(7); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
