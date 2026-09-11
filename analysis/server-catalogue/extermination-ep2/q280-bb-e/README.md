# Military Strikes Back — extermination-ep2/q280-bb-e

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/extermination-ep2/q280-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/extermination-ep2/q280-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/extermination-ep2/q280-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 280; language E. Static scan: **684 objects, 154 enemy/NPC records, 107 events, 68 script labels.** Script roundtrip: byte-identical.

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
0x02, 0x14, 0x00, 0x00, 0x00
0x05, 0x17, 0x00, 0x00, 0x00
0x07, 0x19, 0x00, 0x00, 0x00
0x09, 0x1B, 0x00, 0x00, 0x00
0x0A, 0x1C, 0x00, 0x02, 0x00
0x0C, 0x1E, 0x00, 0x00, 0x00
0x0D, 0x1F, 0x00, 0x00, 0x00
0x0F, 0x21, 0x00, 0x00, 0x00
0x11, 0x23, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 47 | 21 | 0 |
| 2 | 87 | 0 | 0 |
| 5 | 126 | 0 | 0 |
| 7 | 76 | 70 | 34 |
| 9 | 109 | 55 | 11 |
| 10 | 110 | 0 | 0 |
| 12 | 22 | 1 | 1 |
| 13 | 27 | 1 | 1 |
| 15 | 30 | 2 | 2 |
| 17 | 50 | 4 | 58 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 7 | 31 | 3 / 1 | 2 | 150 | trigger_event(311); stop |
| 7 | 311 | 3 / 2 | 6 | 10 | trigger_event(312); stop |
| 7 | 312 | 3 / 3 | 5 | 100 | trigger_event(313); stop |
| 7 | 313 | 3 / 4 | 6 | 10 | set_switch(4); set_switch(5); stop |
| 7 | 51 | 5 / 1 | 3 | 10 | construct_objects(room=5,group_or_wave=1); trigger_event(51011); trigger_event(51021); trigger_event(51031); trigger_event(51041); trigger_event(51051); trigger_event(51061); stop |
| 7 | 51011 | 5 / 2 | 1 | 150 | stop |
| 7 | 51021 | 5 / 3 | 1 | 300 | stop |
| 7 | 51031 | 5 / 4 | 1 | 450 | set_switch(6); set_switch(7); set_switch(102); stop |
| 7 | 51041 | 5 / 5 | 1 | 10 | trigger_event(51042); stop |
| 7 | 51042 | 5 / 6 | 1 | 10 | trigger_event(51043); stop |
| 7 | 51043 | 5 / 7 | 1 | 10 | trigger_event(51044); stop |
| 7 | 51044 | 5 / 8 | 1 | 10 | trigger_event(51045); stop |
| 7 | 51045 | 5 / 9 | 1 | 10 | stop |
| 7 | 51051 | 5 / 10 | 1 | 10 | trigger_event(51052); stop |
| 7 | 51052 | 5 / 11 | 1 | 10 | trigger_event(51053); stop |
| 7 | 51053 | 5 / 12 | 1 | 10 | trigger_event(51054); stop |
| 7 | 51054 | 5 / 13 | 1 | 10 | trigger_event(51055); stop |
| 7 | 51055 | 5 / 14 | 1 | 10 | stop |
| 7 | 51061 | 5 / 15 | 1 | 10 | trigger_event(51062); stop |
| 7 | 51062 | 5 / 16 | 1 | 10 | trigger_event(51063); stop |
| 7 | 51063 | 5 / 17 | 1 | 10 | trigger_event(51064); stop |
| 7 | 51064 | 5 / 18 | 1 | 10 | trigger_event(51065); stop |
| 7 | 51065 | 5 / 19 | 1 | 10 | stop |
| 7 | 71 | 7 / 1 | 0 | 10 | trigger_event(711); stop |
| 7 | 711 | 7 / 2 | 0 | 10 | trigger_event(712); stop |
| 7 | 712 | 7 / 3 | 0 | 10 | trigger_event(713); stop |
| 7 | 713 | 7 / 4 | 1 | 10 | trigger_event(714); stop |
| 7 | 714 | 7 / 5 | 0 | 10 | trigger_event(715); stop |
| 7 | 715 | 7 / 6 | 0 | 1000 | stop |
| 7 | 81 | 8 / 1 | 5 | 10 | trigger_event(811); stop |
| 7 | 811 | 8 / 2 | 5 | 10 | trigger_event(812); stop |
| 7 | 812 | 8 / 3 | 6 | 100 | trigger_event(813); stop |
| 7 | 813 | 8 / 4 | 6 | 100 | trigger_event(814); stop |
| 7 | 814 | 8 / 5 | 7 | 10 | stop |
| 9 | 900 | 7 / 1 | 6 | 1 | trigger_event(901); stop |
| 9 | 901 | 7 / 2 | 7 | 1 | trigger_event(902); stop |
| 9 | 902 | 7 / 3 | 11 | 1 | trigger_event(903); stop |
| 9 | 903 | 7 / 4 | 13 | 1 | trigger_event(904); stop |
| 9 | 904 | 7 / 5 | 2 | 1 | set_switch(1); stop |
| 9 | 905 | 7 / 6 | 1 | 1 | stop |
| 9 | 910 | 9 / 1 | 6 | 100 | trigger_event(911); stop |
| 9 | 911 | 9 / 2 | 6 | 1 | trigger_event(912); stop |
| 9 | 912 | 9 / 3 | 0 | 1 | trigger_event(913); stop |
| 9 | 913 | 9 / 4 | 0 | 1 | trigger_event(914); stop |
| 9 | 914 | 9 / 5 | 0 | 1 | set_switch(2); stop |
| 12 | 1 | 1 / 1 | 1 | 50 | construct_objects(room=1,group_or_wave=1); stop |
| 13 | 1 | 0 / 1 | 1 | 0 | construct_objects(room=1,group_or_wave=1); stop |
| 15 | 1 | 1 / 1 | 1 | 50 | stop |
| 15 | 2 | 1 / 2 | 1 | 500 | construct_objects(room=1,group_or_wave=1); stop |
| 17 | 11 | 1 / 1 | 0 | 60 | trigger_event(111); stop |
| 17 | 111 | 1 / 2 | 1 | 60 | set_switch(1); stop |
| 17 | 21 | 2 / 1 | 0 | 30 | set_switch(2); stop |
| 17 | 201 | 20 / 1 | 0 | 30 | trigger_event(2011); stop |
| 17 | 2011 | 20 / 2 | 0 | 30 | set_switch(3); stop |
| 17 | 202 | 20 / 3 | 0 | 15 | stop |
| 17 | 203 | 20 / 4 | 1 | 15 | stop |
| 17 | 101 | 10 / 1 | 0 | 60 | trigger_event(1011); stop |
| 17 | 1011 | 10 / 2 | 0 | 30 | trigger_event(1012); stop |
| 17 | 1012 | 10 / 3 | 1 | 30 | trigger_event(1013); stop |
| 17 | 1013 | 10 / 4 | 0 | 60 | set_switch(4); stop |
| 17 | 33 | 3 / 1 | 0 | 60 | trigger_event(331); stop |
| 17 | 331 | 3 / 2 | 0 | 30 | trigger_event(332); stop |
| 17 | 332 | 3 / 3 | 0 | 150 | set_switch(5); stop |
| 17 | 41 | 4 / 1 | 0 | 30 | trigger_event(411); stop |
| 17 | 411 | 4 / 2 | 0 | 30 | set_switch(6); stop |
| 17 | 211 | 21 / 1 | 0 | 30 | trigger_event(2111); stop |
| 17 | 2111 | 21 / 2 | 0 | 30 | trigger_event(2112); stop |
| 17 | 2112 | 21 / 3 | 0 | 30 | set_switch(7); stop |
| 17 | 51 | 5 / 1 | 0 | 60 | trigger_event(511); stop |
| 17 | 511 | 5 / 2 | 0 | 60 | trigger_event(512); stop |
| 17 | 512 | 5 / 3 | 0 | 60 | trigger_event(513); stop |
| 17 | 513 | 5 / 4 | 0 | 60 | set_switch(8); construct_objects(room=5,group_or_wave=6); stop |
| 17 | 52 | 5 / 5 | 0 | 30 | stop |
| 17 | 221 | 22 / 1 | 0 | 90 | trigger_event(2211); stop |
| 17 | 2211 | 22 / 2 | 0 | 120 | trigger_event(2212); stop |
| 17 | 2212 | 22 / 3 | 0 | 120 | trigger_event(2213); stop |
| 17 | 2213 | 22 / 4 | 0 | 30 | set_switch(9); stop |
| 17 | 301 | 30 / 1 | 0 | 30 | trigger_event(3011); stop |
| 17 | 3011 | 30 / 2 | 0 | 150 | trigger_event(3012); stop |
| 17 | 3012 | 30 / 3 | 0 | 30 | trigger_event(3013); stop |
| 17 | 3013 | 30 / 4 | 0 | 120 | trigger_event(3014); stop |
| 17 | 3014 | 30 / 5 | 0 | 90 | trigger_event(3015); stop |
| 17 | 3015 | 30 / 6 | 0 | 60 | trigger_event(3016); stop |
| 17 | 3016 | 30 / 7 | 0 | 120 | trigger_event(3017); stop |
| 17 | 3017 | 30 / 8 | 0 | 30 | trigger_event(3018); stop |
| 17 | 3018 | 30 / 9 | 0 | 30 | trigger_event(3019); stop |
| 17 | 3019 | 30 / 10 | 0 | 30 | trigger_event(30111); stop |
| 17 | 30111 | 30 / 11 | 0 | 30 | trigger_event(30112); stop |
| 17 | 30112 | 30 / 12 | 0 | 30 | set_switch(100); stop |
| 17 | 302 | 30 / 13 | 0 | 60 | trigger_event(3021); stop |
| 17 | 3021 | 30 / 14 | 0 | 120 | trigger_event(3022); stop |
| 17 | 3022 | 30 / 15 | 0 | 150 | trigger_event(3023); stop |
| 17 | 3023 | 30 / 16 | 0 | 90 | trigger_event(3024); stop |
| 17 | 3024 | 30 / 17 | 0 | 120 | trigger_event(3025); stop |
| 17 | 3025 | 30 / 18 | 0 | 30 | trigger_event(3026); stop |
| 17 | 3026 | 30 / 19 | 0 | 90 | trigger_event(3027); stop |
| 17 | 3027 | 30 / 20 | 0 | 30 | trigger_event(3028); stop |
| 17 | 3028 | 30 / 21 | 1 | 30 | trigger_event(3029); stop |
| 17 | 3029 | 30 / 22 | 0 | 30 | trigger_event(30211); stop |
| 17 | 30211 | 30 / 23 | 0 | 30 | trigger_event(30212); stop |
| 17 | 30212 | 30 / 24 | 0 | 30 | set_switch(101); stop |
| 17 | 303 | 30 / 25 | 0 | 120 | trigger_event(3031); stop |
| 17 | 3031 | 30 / 26 | 0 | 60 | trigger_event(3032); stop |
| 17 | 3032 | 30 / 27 | 0 | 30 | trigger_event(3033); stop |
| 17 | 3033 | 30 / 28 | 0 | 150 | trigger_event(3034); stop |
| 17 | 3034 | 30 / 29 | 0 | 30 | trigger_event(3035); stop |
| 17 | 3035 | 30 / 30 | 0 | 150 | set_switch(120); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

A backup is present; decompressed content identical: False. See [text differences](<backup-diff.txt>).

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
