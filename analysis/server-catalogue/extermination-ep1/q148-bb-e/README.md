# Mine Offensive — extermination-ep1/q148-bb-e

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/extermination-ep1/q148-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/extermination-ep1/q148-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/extermination-ep1/q148-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 148; language E. Static scan: **452 objects, 188 enemy/NPC records, 94 events, 140 script labels.** Script roundtrip: byte-identical.

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
0x00, 0x00, 0x00, 0x00, 0x00
0x06, 0x06, 0x00, 0x00, 0x00
0x07, 0x07, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 19 | 0 |
| 6 | 249 | 84 | 22 |
| 7 | 177 | 85 | 72 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 6 | 100 | 50 / 1 | 1 | 5 | trigger_event(102); stop |
| 6 | 101 | 50 / 2 | 2 | 30 | stop |
| 6 | 102 | 50 / 3 | 8 | 50 | set_switch(2); set_switch(3); trigger_event(105); stop |
| 6 | 104 | 50 / 4 | 2 | 60 | stop |
| 6 | 105 | 60 / 1 | 2 | 50 | stop |
| 6 | 106 | 60 / 2 | 5 | 40 | set_switch(5); set_switch(6); set_switch(8); stop |
| 6 | 107 | 60 / 3 | 3 | 50 | stop |
| 6 | 108 | 51 / 1 | 6 | 1 | set_switch(11); stop |
| 6 | 109 | 51 / 2 | 3 | 1 | trigger_event(110); stop |
| 6 | 110 | 51 / 3 | 3 | 1 | construct_objects(room=51,group_or_wave=1); stop |
| 6 | 111 | 75 / 1 | 6 | 50 | set_switch(12); stop |
| 6 | 112 | 75 / 2 | 3 | 1 | stop |
| 6 | 113 | 75 / 3 | 3 | 50 | stop |
| 6 | 114 | 75 / 4 | 6 | 300 | set_switch(13); stop |
| 6 | 115 | 75 / 5 | 1 | 30 | stop |
| 6 | 116 | 30 / 1 | 3 | 20 | trigger_event(118); stop |
| 6 | 117 | 60 / 4 | 2 | 1 | stop |
| 6 | 118 | 30 / 2 | 4 | 50 | construct_objects(room=30,group_or_wave=1); stop |
| 6 | 119 | 52 / 1 | 5 | 1 | set_switch(14); stop |
| 6 | 120 | 75 / 6 | 2 | 30 | stop |
| 6 | 121 | 40 / 1 | 4 | 100 | stop |
| 6 | 122 | 220 / 1 | 3 | 60 | set_switch(16); stop |
| 7 | 100 | 50 / 1 | 4 | 200 | trigger_event(101); stop |
| 7 | 101 | 50 / 2 | 5 | 1 | trigger_event(102); stop |
| 7 | 102 | 50 / 3 | 4 | 1 | construct_objects(room=50,group_or_wave=1); stop |
| 7 | 103 | 40 / 1 | 6 | 1 | trigger_event(104); stop |
| 7 | 104 | 40 / 2 | 4 | 1 | construct_objects(room=40,group_or_wave=1); stop |
| 7 | 105 | 52 / 1 | 8 | 50 | stop |
| 7 | 106 | 220 / 1 | 5 | 50 | trigger_event(107); stop |
| 7 | 107 | 220 / 2 | 4 | 60 | construct_objects(room=220,group_or_wave=1); stop |
| 7 | 108 | 80 / 1 | 7 | 20 | set_switch(62); stop |
| 7 | 109 | 30 / 1 | 3 | 1 | trigger_event(110); stop |
| 7 | 110 | 30 / 2 | 6 | 1 | construct_objects(room=30,group_or_wave=1); stop |
| 7 | 111 | 61 / 1 | 6 | 1 | trigger_event(112); stop |
| 7 | 112 | 61 / 2 | 6 | 1 | trigger_event(113); stop |
| 7 | 113 | 61 / 3 | 6 | 1 | trigger_event(114); stop |
| 7 | 114 | 61 / 4 | 2 | 1 | trigger_event(115); stop |
| 7 | 115 | 61 / 5 | 9 | 1 | set_switch(120); stop |
| 7 | 202 | 0 / 0 | 0 | 0 | trigger_event(302); stop |
| 7 | 203 | 0 / 0 | 0 | 0 | trigger_event(303); stop |
| 7 | 204 | 0 / 0 | 0 | 0 | trigger_event(304); stop |
| 7 | 205 | 0 / 0 | 0 | 0 | trigger_event(305); stop |
| 7 | 206 | 0 / 0 | 0 | 0 | trigger_event(306); stop |
| 7 | 207 | 0 / 0 | 0 | 0 | trigger_event(307); stop |
| 7 | 208 | 0 / 0 | 0 | 0 | trigger_event(308); stop |
| 7 | 209 | 0 / 0 | 0 | 0 | trigger_event(309); stop |
| 7 | 210 | 0 / 0 | 0 | 0 | trigger_event(310); stop |
| 7 | 211 | 0 / 0 | 0 | 0 | trigger_event(311); stop |
| 7 | 212 | 0 / 0 | 0 | 0 | trigger_event(312); stop |
| 7 | 213 | 0 / 0 | 0 | 0 | trigger_event(313); stop |
| 7 | 214 | 0 / 0 | 0 | 0 | trigger_event(314); stop |
| 7 | 215 | 0 / 0 | 0 | 0 | trigger_event(315); stop |
| 7 | 216 | 0 / 0 | 0 | 0 | trigger_event(316); stop |
| 7 | 217 | 0 / 0 | 0 | 0 | trigger_event(317); stop |
| 7 | 218 | 0 / 0 | 0 | 0 | trigger_event(318); stop |
| 7 | 219 | 0 / 0 | 0 | 0 | trigger_event(319); stop |
| 7 | 220 | 0 / 0 | 0 | 0 | trigger_event(320); stop |
| 7 | 221 | 0 / 0 | 0 | 0 | trigger_event(321); stop |
| 7 | 222 | 0 / 0 | 0 | 0 | trigger_event(322); stop |
| 7 | 223 | 0 / 0 | 0 | 0 | trigger_event(323); stop |
| 7 | 224 | 0 / 0 | 0 | 0 | trigger_event(324); stop |
| 7 | 225 | 0 / 0 | 0 | 0 | trigger_event(325); stop |
| 7 | 226 | 0 / 0 | 0 | 0 | trigger_event(326); stop |
| 7 | 227 | 0 / 0 | 0 | 0 | trigger_event(327); stop |
| 7 | 228 | 0 / 0 | 0 | 0 | trigger_event(328); stop |
| 7 | 229 | 0 / 0 | 0 | 0 | trigger_event(329); stop |
| 7 | 302 | 0 / 0 | 0 | 0 | construct_objects(room=61,group_or_wave=2); stop |
| 7 | 303 | 0 / 0 | 0 | 0 | construct_objects(room=61,group_or_wave=3); stop |
| 7 | 304 | 0 / 0 | 0 | 0 | construct_objects(room=61,group_or_wave=4); stop |
| 7 | 305 | 0 / 0 | 0 | 0 | construct_objects(room=61,group_or_wave=5); stop |
| 7 | 306 | 0 / 0 | 0 | 0 | construct_objects(room=61,group_or_wave=6); stop |
| 7 | 307 | 0 / 0 | 0 | 0 | construct_objects(room=61,group_or_wave=7); stop |
| 7 | 308 | 0 / 0 | 0 | 0 | construct_objects(room=61,group_or_wave=8); stop |
| 7 | 309 | 0 / 0 | 0 | 0 | construct_objects(room=61,group_or_wave=9); stop |
| 7 | 310 | 0 / 0 | 0 | 0 | construct_objects(room=61,group_or_wave=10); stop |
| 7 | 311 | 0 / 0 | 0 | 0 | construct_objects(room=61,group_or_wave=11); stop |
| 7 | 312 | 0 / 0 | 0 | 0 | construct_objects(room=61,group_or_wave=12); stop |
| 7 | 313 | 0 / 0 | 0 | 0 | construct_objects(room=61,group_or_wave=13); stop |
| 7 | 314 | 0 / 0 | 0 | 0 | construct_objects(room=61,group_or_wave=14); stop |
| 7 | 315 | 0 / 0 | 0 | 0 | construct_objects(room=61,group_or_wave=15); stop |
| 7 | 316 | 0 / 0 | 0 | 0 | construct_objects(room=61,group_or_wave=16); stop |
| 7 | 317 | 0 / 0 | 0 | 0 | construct_objects(room=61,group_or_wave=17); stop |
| 7 | 318 | 0 / 0 | 0 | 0 | construct_objects(room=61,group_or_wave=18); stop |
| 7 | 319 | 0 / 0 | 0 | 0 | construct_objects(room=61,group_or_wave=19); stop |
| 7 | 320 | 0 / 0 | 0 | 0 | construct_objects(room=61,group_or_wave=20); stop |
| 7 | 321 | 0 / 0 | 0 | 0 | construct_objects(room=61,group_or_wave=21); stop |
| 7 | 322 | 0 / 0 | 0 | 0 | construct_objects(room=61,group_or_wave=22); stop |
| 7 | 323 | 0 / 0 | 0 | 0 | construct_objects(room=61,group_or_wave=23); stop |
| 7 | 324 | 0 / 0 | 0 | 0 | construct_objects(room=61,group_or_wave=24); stop |
| 7 | 325 | 0 / 0 | 0 | 0 | construct_objects(room=61,group_or_wave=25); stop |
| 7 | 326 | 0 / 0 | 0 | 0 | construct_objects(room=61,group_or_wave=26); stop |
| 7 | 327 | 0 / 0 | 0 | 0 | construct_objects(room=61,group_or_wave=27); stop |
| 7 | 328 | 0 / 0 | 0 | 0 | construct_objects(room=61,group_or_wave=28); stop |
| 7 | 329 | 0 / 0 | 0 | 0 | construct_objects(room=61,group_or_wave=29); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

A backup is present; decompressed content identical: False. See [text differences](<backup-diff.txt>).

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
