# Spring Cleaning — events-ep1/q512-bb-e

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/events-ep1/q512-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/events-ep1/q512-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/events-ep1/q512-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 512; language E. Static scan: **787 objects, 837 enemy/NPC records, 160 events, 75 script labels.** Script roundtrip: byte-identical.

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
| 0 | 28 | 16 | 0 |
| 1 | 118 | 137 | 29 |
| 3 | 216 | 228 | 38 |
| 6 | 213 | 205 | 40 |
| 8 | 212 | 251 | 53 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 111 | 11 / 1 | 8 | 0 | trigger_event(1111); stop |
| 1 | 1111 | 11 / 2 | 9 | 0 | trigger_event(1112); stop |
| 1 | 1112 | 11 / 3 | 3 | 0 | set_switch(6); set_switch(5); stop |
| 1 | 101 | 10 / 1 | 4 | 0 | trigger_event(1011); stop |
| 1 | 1011 | 10 / 2 | 3 | 0 | trigger_event(1012); stop |
| 1 | 1012 | 10 / 3 | 1 | 0 | trigger_event(1013); stop |
| 1 | 1013 | 10 / 4 | 8 | 0 | set_switch(7); set_switch(8); stop |
| 1 | 51 | 5 / 1 | 5 | 0 | trigger_event(511); stop |
| 1 | 511 | 5 / 2 | 9 | 0 | trigger_event(512); stop |
| 1 | 512 | 5 / 3 | 10 | 0 | set_switch(1); stop |
| 1 | 21 | 2 / 1 | 4 | 0 | trigger_event(211); stop |
| 1 | 211 | 2 / 2 | 6 | 0 | set_switch(2); stop |
| 1 | 71 | 7 / 1 | 4 | 0 | trigger_event(711); stop |
| 1 | 711 | 7 / 2 | 8 | 0 | trigger_event(712); stop |
| 1 | 712 | 7 / 3 | 6 | 0 | trigger_event(713); stop |
| 1 | 713 | 7 / 4 | 3 | 0 | trigger_event(714); stop |
| 1 | 714 | 7 / 5 | 4 | 0 | trigger_event(715); stop |
| 1 | 715 | 7 / 6 | 5 | 0 | set_switch(3); stop |
| 1 | 41 | 4 / 1 | 2 | 0 | trigger_event(411); stop |
| 1 | 411 | 4 / 2 | 2 | 0 | trigger_event(412); stop |
| 1 | 412 | 4 / 3 | 2 | 0 | trigger_event(413); stop |
| 1 | 413 | 4 / 4 | 3 | 0 | trigger_event(414); stop |
| 1 | 414 | 4 / 5 | 8 | 0 | trigger_event(42); stop |
| 1 | 42 | 4 / 6 | 2 | 0 | trigger_event(421); stop |
| 1 | 421 | 4 / 7 | 2 | 0 | trigger_event(422); stop |
| 1 | 422 | 4 / 8 | 2 | 0 | trigger_event(423); stop |
| 1 | 423 | 4 / 9 | 3 | 0 | trigger_event(424); stop |
| 1 | 424 | 4 / 10 | 7 | 0 | trigger_event(425); stop |
| 1 | 425 | 4 / 11 | 0 | 0 | set_switch(9); stop |
| 3 | 502 | 50 / 2 | 5 | 1 | trigger_event(5021); stop |
| 3 | 5021 | 50 / 3 | 6 | 1 | trigger_event(5022); stop |
| 3 | 5022 | 50 / 4 | 3 | 1 | trigger_event(5023); stop |
| 3 | 5023 | 50 / 1 | 4 | 1 | set_switch(2); set_switch(3); stop |
| 3 | 321 | 32 / 1 | 7 | 1 | trigger_event(3211); stop |
| 3 | 3211 | 32 / 2 | 6 | 1 | trigger_event(3212); stop |
| 3 | 3212 | 32 / 3 | 5 | 1 | set_switch(27); set_switch(5); set_switch(7); set_switch(8); set_switch(11); set_switch(12); stop |
| 3 | 341 | 34 / 1 | 3 | 1 | trigger_event(3411); stop |
| 3 | 3411 | 34 / 2 | 3 | 1 | trigger_event(3412); stop |
| 3 | 3412 | 34 / 3 | 3 | 1 | trigger_event(342); stop |
| 3 | 342 | 34 / 4 | 1 | 1 | trigger_event(3421); stop |
| 3 | 3421 | 34 / 5 | 3 | 1 | trigger_event(3422); stop |
| 3 | 3422 | 34 / 6 | 2 | 1 | set_switch(10); set_switch(6); stop |
| 3 | 531 | 53 / 1 | 6 | 1 | trigger_event(5311); stop |
| 3 | 5311 | 53 / 2 | 4 | 1 | trigger_event(5312); stop |
| 3 | 5312 | 53 / 3 | 5 | 1 | trigger_event(5313); stop |
| 3 | 5313 | 53 / 4 | 5 | 1 | set_switch(8); set_switch(11); set_switch(12); set_switch(9); stop |
| 3 | 601 | 60 / 1 | 5 | 1 | trigger_event(6011); stop |
| 3 | 6011 | 60 / 2 | 6 | 1 | trigger_event(6012); stop |
| 3 | 6012 | 60 / 3 | 7 | 1 | trigger_event(6013); stop |
| 3 | 6013 | 60 / 4 | 6 | 1 | set_switch(13); stop |
| 3 | 113 | 11 / 1 | 4 | 1 | trigger_event(1111); stop |
| 3 | 1111 | 11 / 2 | 5 | 1 | trigger_event(1112); stop |
| 3 | 1112 | 11 / 3 | 15 | 1 | set_switch(14); set_switch(17); set_switch(18); stop |
| 3 | 511 | 51 / 1 | 7 | 1 | trigger_event(5111); stop |
| 3 | 5111 | 51 / 2 | 7 | 1 | trigger_event(5112); stop |
| 3 | 5112 | 51 / 3 | 8 | 1 | trigger_event(5113); stop |
| 3 | 5113 | 51 / 4 | 6 | 1 | trigger_event(5114); stop |
| 3 | 5114 | 51 / 5 | 12 | 1 | set_switch(19); set_switch(20); set_switch(23); set_switch(25); set_switch(26); set_switch(24); set_switch(22); stop |
| 3 | 521 | 52 / 1 | 2 | 1 | trigger_event(5211); stop |
| 3 | 5211 | 52 / 2 | 8 | 1 | trigger_event(5212); stop |
| 3 | 5212 | 52 / 3 | 6 | 1 | trigger_event(5213); stop |
| 3 | 5213 | 52 / 4 | 3 | 1 | trigger_event(8202); stop |
| 3 | 522 | 52 / 5 | 2 | 1 | trigger_event(5221); stop |
| 3 | 5221 | 52 / 6 | 4 | 1 | trigger_event(5222); stop |
| 3 | 5222 | 52 / 7 | 3 | 1 | trigger_event(5223); stop |
| 3 | 5223 | 52 / 8 | 4 | 1 | trigger_event(5224); stop |
| 3 | 5224 | 52 / 9 | 0 | 1 | set_switch(21); stop |
| 6 | 301 | 30 / 1 | 3 | 30 | trigger_event(3011); stop |
| 6 | 3011 | 30 / 2 | 4 | 0 | trigger_event(3012); stop |
| 6 | 3012 | 30 / 3 | 2 | 0 | trigger_event(3013); stop |
| 6 | 3013 | 30 / 4 | 2 | 0 | trigger_event(302); stop |
| 6 | 302 | 30 / 5 | 4 | 0 | trigger_event(3021); stop |
| 6 | 3021 | 30 / 6 | 4 | 0 | trigger_event(3022); stop |
| 6 | 3022 | 30 / 7 | 4 | 0 | trigger_event(3023); stop |
| 6 | 3023 | 30 / 8 | 5 | 0 | set_switch(16); set_switch(17); set_switch(18); set_switch(20); set_switch(21); set_switch(22); set_switch(23); stop |
| 6 | 501 | 50 / 1 | 1 | 1 | trigger_event(5011); stop |
| 6 | 5011 | 50 / 2 | 11 | 15 | set_switch(2); set_switch(3); set_switch(235); stop |
| 6 | 511 | 51 / 1 | 4 | 1 | trigger_event(5111); stop |
| 6 | 5111 | 51 / 2 | 4 | 1 | trigger_event(512); stop |
| 6 | 512 | 51 / 3 | 2 | 1 | trigger_event(5121); stop |
| 6 | 5121 | 51 / 4 | 4 | 40 | trigger_event(5122); stop |
| 6 | 5122 | 51 / 5 | 4 | 60 | set_switch(8); set_switch(9); set_switch(11); set_switch(12); set_switch(13); set_switch(38); stop |
| 6 | 531 | 53 / 1 | 10 | 60 | trigger_event(5311); stop |
| 6 | 5311 | 53 / 2 | 10 | 30 | trigger_event(5312); stop |
| 6 | 5312 | 53 / 3 | 8 | 50 | trigger_event(5313); stop |
| 6 | 5313 | 53 / 4 | 10 | 50 | trigger_event(532); stop |
| 6 | 532 | 53 / 5 | 0 | 70 | trigger_event(5321); stop |
| 6 | 5321 | 53 / 6 | 0 | 30 | trigger_event(5322); stop |
| 6 | 5322 | 53 / 7 | 0 | 30 | trigger_event(5323); stop |
| 6 | 5323 | 53 / 8 | 0 | 30 | set_switch(34); set_switch(37); stop |
| 6 | 541 | 54 / 1 | 8 | 1 | trigger_event(5411); stop |
| 6 | 5411 | 54 / 2 | 10 | 1 | set_switch(33); set_switch(34); set_switch(36); stop |
| 6 | 601 | 60 / 1 | 3 | 1 | trigger_event(6011); stop |
| 6 | 6011 | 60 / 2 | 6 | 40 | trigger_event(6012); stop |
| 6 | 6012 | 60 / 3 | 2 | 60 | trigger_event(602); stop |
| 6 | 602 | 60 / 4 | 5 | 40 | trigger_event(6021); stop |
| 6 | 6021 | 60 / 5 | 8 | 40 | set_switch(5); set_switch(6); set_switch(7); set_switch(8); stop |
| 6 | 611 | 61 / 1 | 11 | 1 | trigger_event(6111); stop |
| 6 | 6111 | 61 / 2 | 2 | 20 | trigger_event(6112); stop |
| 6 | 6112 | 61 / 3 | 9 | 20 | trigger_event(6113); stop |
| 6 | 6113 | 61 / 4 | 8 | 1 | set_switch(31); set_switch(32); stop |
| 6 | 751 | 75 / 1 | 14 | 0 | trigger_event(7511); stop |
| 6 | 7511 | 75 / 2 | 1 | 0 | trigger_event(752); stop |
| 6 | 752 | 75 / 3 | 0 | 0 | set_switch(14); set_switch(15); set_switch(200); set_switch(204); stop |
| 6 | 901 | 90 / 1 | 12 | 0 | trigger_event(9011); stop |
| 6 | 9011 | 90 / 2 | 6 | 0 | construct_objects(room=90,group_or_wave=2); trigger_event(902); stop |
| 6 | 902 | 0 / 3 | 0 | 0 | set_switch(24); set_switch(26); set_switch(27); set_switch(28); set_switch(29); set_switch(30); stop |
| 8 | 101 | 10 / 1 | 5 | 1 | trigger_event(1011); stop |
| 8 | 1011 | 10 / 2 | 5 | 1 | trigger_event(1012); stop |
| 8 | 1012 | 10 / 3 | 7 | 1 | trigger_event(1013); stop |
| 8 | 1013 | 10 / 4 | 4 | 1 | trigger_event(1014); stop |
| 8 | 1014 | 10 / 5 | 7 | 1 | trigger_event(1015); stop |
| 8 | 1015 | 10 / 6 | 5 | 1 | set_switch(43); set_switch(44); stop |
| 8 | 301 | 30 / 1 | 2 | 1 | trigger_event(3011); stop |
| 8 | 3011 | 30 / 2 | 6 | 1 | trigger_event(3012); stop |
| 8 | 3012 | 30 / 3 | 5 | 1 | trigger_event(303); stop |
| 8 | 303 | 30 / 4 | 1 | 1 | trigger_event(3031); stop |
| 8 | 3031 | 30 / 5 | 3 | 1 | trigger_event(3032); stop |
| 8 | 3032 | 30 / 6 | 3 | 1 | set_switch(35); set_switch(36); set_switch(37); set_switch(38); set_switch(40); set_switch(33); set_switch(34); set_switch(27); set_switch(28); set_switch(31); set_switch(32); trigger_event(3031); stop |
| 8 | 221 | 22 / 1 | 10 | 1 | trigger_event(2211); stop |
| 8 | 2211 | 22 / 2 | 9 | 1 | trigger_event(2212); stop |
| 8 | 2212 | 22 / 3 | 5 | 1 | set_switch(41); set_switch(42); stop |
| 8 | 111 | 11 / 1 | 4 | 1 | trigger_event(1111); stop |
| 8 | 1111 | 11 / 2 | 9 | 1 | trigger_event(1112); stop |
| 8 | 1112 | 11 / 3 | 3 | 1 | set_switch(30); set_switch(29); set_switch(26); set_switch(25); set_switch(31); set_switch(32); stop |
| 8 | 401 | 40 / 1 | 14 | 1 | trigger_event(4011); stop |
| 8 | 4011 | 40 / 2 | 7 | 1 | set_switch(23); stop |
| 8 | 121 | 12 / 1 | 4 | 1 | trigger_event(1211); stop |
| 8 | 1211 | 12 / 2 | 6 | 1 | trigger_event(1212); stop |
| 8 | 1212 | 12 / 3 | 11 | 1 | set_switch(19); set_switch(20); set_switch(21); set_switch(22); stop |
| 8 | 311 | 31 / 1 | 3 | 1 | trigger_event(3111); stop |
| 8 | 3111 | 31 / 2 | 4 | 1 | trigger_event(3112); stop |
| 8 | 3112 | 31 / 3 | 3 | 1 | trigger_event(313); stop |
| 8 | 313 | 31 / 4 | 3 | 1 | trigger_event(3131); stop |
| 8 | 3131 | 31 / 5 | 7 | 1 | trigger_event(3132); stop |
| 8 | 3132 | 31 / 6 | 0 | 1 | set_switch(15); set_switch(16); set_switch(17); set_switch(18); nop; stop |
| 8 | 701 | 70 / 1 | 2 | 1 | trigger_event(7011); stop |
| 8 | 7011 | 70 / 2 | 4 | 1 | trigger_event(7012); stop |
| 8 | 7012 | 70 / 3 | 2 | 1 | trigger_event(702); stop |
| 8 | 702 | 70 / 4 | 5 | 1 | trigger_event(7021); stop |
| 8 | 7021 | 70 / 5 | 9 | 1 | trigger_event(7022); stop |
| 8 | 7022 | 70 / 6 | 4 | 1 | set_switch(11); set_switch(12); set_switch(14); set_switch(269); trigger_event(5511); stop |
| 8 | 551 | 55 / 1 | 2 | 1 | trigger_event(5511); stop |
| 8 | 5511 | 55 / 2 | 10 | 1 | set_switch(9); set_switch(10); stop |
| 8 | 321 | 32 / 1 | 5 | 1 | trigger_event(3211); stop |
| 8 | 3211 | 32 / 2 | 10 | 1 | trigger_event(3212); stop |
| 8 | 3212 | 32 / 3 | 13 | 1 | set_switch(7); set_switch(8); stop |
| 8 | 201 | 20 / 1 | 3 | 1 | trigger_event(2011); stop |
| 8 | 2011 | 20 / 2 | 3 | 1 | trigger_event(2012); stop |
| 8 | 2012 | 20 / 3 | 3 | 1 | trigger_event(2013); stop |
| 8 | 2013 | 20 / 4 | 2 | 1 | trigger_event(2014); stop |
| 8 | 2014 | 20 / 5 | 3 | 1 | stop |
| 8 | 202 | 20 / 6 | 3 | 1 | trigger_event(2021); stop |
| 8 | 2021 | 20 / 7 | 4 | 1 | trigger_event(2022); stop |
| 8 | 2022 | 20 / 8 | 3 | 1 | trigger_event(2023); stop |
| 8 | 2023 | 20 / 9 | 2 | 1 | trigger_event(2024); stop |
| 8 | 2024 | 20 / 10 | 2 | 1 | set_switch(1); set_switch(2); set_switch(3); set_switch(5); set_switch(47); set_switch(48); stop |
| 8 | 801 | 50 / 1 | 0 | 0 | trigger_event(8011); stop |
| 8 | 8011 | 50 / 2 | 0 | 0 | clear_switch(37); stop |
| 8 | 8012 | 50 / 0 | 0 | 0 | stop |

## Review notes

- Floor 3: event 5213 targets absent event 8202

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
