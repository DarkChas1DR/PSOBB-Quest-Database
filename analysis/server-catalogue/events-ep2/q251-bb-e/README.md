# Gal Da Val\'s Darkness — events-ep2/q251-bb-e

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/events-ep2/q251-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/events-ep2/q251-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/events-ep2/q251-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 251; language E. Static scan: **273 objects, 377 enemy/NPC records, 68 events, 64 script labels.** Script roundtrip: byte-identical.

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
0x03, 0x15, 0x00, 0x00, 0x00
0x05, 0x17, 0x00, 0x00, 0x00
0x0C, 0x1E, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 44 | 16 | 0 |
| 3 | 91 | 177 | 35 |
| 5 | 115 | 183 | 32 |
| 12 | 23 | 1 | 1 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 3 | 100 | 50 / 1 | 5 | 1 | trigger_event(101); stop |
| 3 | 101 | 50 / 2 | 6 | 1 | trigger_event(102); stop |
| 3 | 102 | 50 / 3 | 2 | 1 | set_switch(21); stop |
| 3 | 103 | 41 / 1 | 6 | 1 | trigger_event(104); stop |
| 3 | 104 | 41 / 2 | 4 | 1 | trigger_event(105); stop |
| 3 | 105 | 41 / 3 | 6 | 1 | set_switch(23); stop |
| 3 | 106 | 181 / 1 | 3 | 1 | set_switch(24); stop |
| 3 | 107 | 51 / 1 | 10 | 1 | trigger_event(108); stop |
| 3 | 108 | 51 / 2 | 4 | 1 | trigger_event(109); stop |
| 3 | 109 | 51 / 3 | 6 | 1 | trigger_event(110); stop |
| 3 | 110 | 51 / 4 | 6 | 1 | set_switch(25); stop |
| 3 | 111 | 160 / 1 | 3 | 1 | trigger_event(112); stop |
| 3 | 112 | 160 / 2 | 1 | 1 | set_switch(26); stop |
| 3 | 113 | 10 / 1 | 5 | 1 | trigger_event(114); stop |
| 3 | 114 | 10 / 2 | 6 | 1 | trigger_event(115); stop |
| 3 | 115 | 10 / 3 | 7 | 1 | construct_objects(room=10,group_or_wave=1); set_switch(27); stop |
| 3 | 116 | 180 / 1 | 3 | 1 | set_switch(28); stop |
| 3 | 117 | 40 / 1 | 5 | 1 | trigger_event(118); stop |
| 3 | 118 | 40 / 2 | 6 | 1 | trigger_event(119); stop |
| 3 | 119 | 40 / 3 | 12 | 1 | trigger_event(120); stop |
| 3 | 120 | 40 / 4 | 6 | 1 | construct_objects(room=40,group_or_wave=1); set_switch(31); stop |
| 3 | 121 | 100 / 1 | 2 | 1 | stop |
| 3 | 122 | 30 / 1 | 3 | 1 | trigger_event(124); stop |
| 3 | 123 | 30 / 2 | 4 | 1 | stop |
| 3 | 124 | 30 / 3 | 3 | 1 | set_switch(32); stop |
| 3 | 125 | 31 / 1 | 7 | 1 | trigger_event(126); stop |
| 3 | 126 | 31 / 2 | 6 | 1 | trigger_event(127); stop |
| 3 | 127 | 31 / 3 | 7 | 1 | construct_objects(room=31,group_or_wave=1); stop |
| 3 | 128 | 140 / 1 | 3 | 1 | set_switch(33); stop |
| 3 | 129 | 11 / 1 | 2 | 1 | stop |
| 3 | 130 | 21 / 1 | 5 | 1 | trigger_event(131); stop |
| 3 | 131 | 21 / 2 | 7 | 1 | trigger_event(132); stop |
| 3 | 132 | 21 / 3 | 6 | 1 | trigger_event(133); stop |
| 3 | 133 | 21 / 4 | 6 | 1 | set_switch(34); stop |
| 3 | 134 | 21 / 5 | 4 | 1 | stop |
| 5 | 100 | 2 / 1 | 6 | 1 | trigger_event(101); stop |
| 5 | 101 | 2 / 2 | 6 | 1 | trigger_event(102); stop |
| 5 | 102 | 2 / 3 | 7 | 1 | set_switch(10); stop |
| 5 | 103 | 3 / 1 | 7 | 1 | trigger_event(104); stop |
| 5 | 104 | 3 / 2 | 7 | 1 | trigger_event(105); stop |
| 5 | 105 | 3 / 3 | 8 | 1 | set_switch(11); stop |
| 5 | 106 | 4 / 1 | 7 | 1 | trigger_event(107); stop |
| 5 | 107 | 4 / 2 | 8 | 1 | trigger_event(108); stop |
| 5 | 108 | 4 / 3 | 8 | 1 | set_switch(12); stop |
| 5 | 110 | 5 / 1 | 7 | 1 | trigger_event(111); stop |
| 5 | 111 | 5 / 2 | 9 | 1 | trigger_event(112); stop |
| 5 | 112 | 5 / 3 | 5 | 1 | construct_objects(room=5,group_or_wave=1); stop |
| 5 | 113 | 10 / 1 | 2 | 1 | trigger_event(114); stop |
| 5 | 114 | 10 / 2 | 6 | 1 | trigger_event(115); stop |
| 5 | 115 | 10 / 3 | 8 | 1 | set_switch(13); stop |
| 5 | 116 | 9 / 1 | 7 | 1 | trigger_event(117); stop |
| 5 | 117 | 9 / 2 | 6 | 1 | trigger_event(118); stop |
| 5 | 118 | 9 / 3 | 8 | 1 | set_switch(14); stop |
| 5 | 119 | 8 / 1 | 5 | 1 | trigger_event(120); stop |
| 5 | 120 | 8 / 2 | 5 | 1 | trigger_event(121); stop |
| 5 | 121 | 8 / 3 | 5 | 1 | construct_objects(room=8,group_or_wave=1); stop |
| 5 | 122 | 13 / 1 | 7 | 1 | trigger_event(123); trigger_event(124); stop |
| 5 | 123 | 13 / 2 | 6 | 1 | stop |
| 5 | 124 | 13 / 3 | 2 | 400 | construct_objects(room=13,group_or_wave=1); stop |
| 5 | 125 | 12 / 1 | 5 | 1 | trigger_event(126); trigger_event(127); stop |
| 5 | 126 | 12 / 2 | 4 | 1 | stop |
| 5 | 127 | 12 / 3 | 2 | 500 | construct_objects(room=12,group_or_wave=1); stop |
| 5 | 128 | 11 / 1 | 6 | 1 | trigger_event(129); trigger_event(130); trigger_event(131); stop |
| 5 | 129 | 11 / 2 | 4 | 1 | stop |
| 5 | 130 | 11 / 3 | 3 | 500 | stop |
| 5 | 131 | 11 / 4 | 2 | 700 | trigger_event(132); stop |
| 5 | 132 | 11 / 5 | 5 | 50 | construct_objects(room=11,group_or_wave=1); set_switch(40); stop |
| 12 | 1 | 1 / 1 | 1 | 50 | construct_objects(room=1,group_or_wave=1); set_switch(50); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

A backup is present; decompressed content identical: False. See [text differences](<backup-diff.txt>).

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
