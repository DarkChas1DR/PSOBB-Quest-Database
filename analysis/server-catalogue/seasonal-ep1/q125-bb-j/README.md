# ホワイトデーイベント — seasonal-ep1/q125-bb-j

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/seasonal-ep1/q125-bb-j.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/seasonal-ep1/q125-bb-j.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/seasonal-ep1/q125-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 125; language J. Static scan: **199 objects, 133 enemy/NPC records, 61 events, 274 script labels.** Script roundtrip: byte-identical.

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
0x05, 0x05, 0x00, 0x02, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 17 | 0 |
| 5 | 173 | 116 | 61 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 5 | 221 | 22 / 1 | 3 | 60 | set_switch(28); set_switch(27); set_switch(23); stop |
| 5 | 301 | 30 / 1 | 3 | 60 | trigger_event(3011); stop |
| 5 | 3011 | 30 / 2 | 6 | 1 | set_switch(10); stop |
| 5 | 501 | 50 / 1 | 6 | 60 | trigger_event(5011); stop |
| 5 | 5011 | 50 / 2 | 6 | 60 | trigger_event(5012); stop |
| 5 | 5012 | 50 / 3 | 6 | 60 | set_switch(4); set_switch(5); set_switch(6); set_switch(7); set_switch(8); set_switch(9); stop |
| 5 | 711 | 71 / 13 | 6 | 60 | trigger_event(7111101); trigger_event(7111201); trigger_event(7111301); trigger_event(7111401); trigger_event(7111501); trigger_event(7111601); stop |
| 5 | 7111101 | 71 / 1 | 1 | 1 | trigger_event(7111102); stop |
| 5 | 7111102 | 71 / 2 | 1 | 1 | trigger_event(7111103); stop |
| 5 | 7111201 | 71 / 3 | 1 | 1 | trigger_event(7111202); stop |
| 5 | 7111202 | 71 / 4 | 1 | 1 | trigger_event(7111203); stop |
| 5 | 7111301 | 71 / 5 | 1 | 1 | trigger_event(7111302); stop |
| 5 | 7111302 | 71 / 6 | 1 | 1 | trigger_event(7111303); stop |
| 5 | 7111401 | 71 / 7 | 1 | 1 | trigger_event(7111402); stop |
| 5 | 7111402 | 71 / 8 | 1 | 1 | trigger_event(7111403); stop |
| 5 | 7111501 | 71 / 9 | 1 | 1 | trigger_event(7111502); stop |
| 5 | 7111502 | 71 / 10 | 1 | 1 | trigger_event(7111503); stop |
| 5 | 7111601 | 71 / 11 | 1 | 1 | trigger_event(7111602); stop |
| 5 | 7111602 | 71 / 12 | 1 | 200 | set_switch(16); set_switch(17); stop |
| 5 | 521 | 52 / 13 | 6 | 60 | trigger_event(5211101); trigger_event(5211201); trigger_event(5211301); trigger_event(5211401); trigger_event(5211501); trigger_event(5211601); stop |
| 5 | 5211101 | 52 / 1 | 1 | 1 | trigger_event(5211102); stop |
| 5 | 5211102 | 52 / 2 | 1 | 1 | trigger_event(5211103); stop |
| 5 | 5211201 | 52 / 3 | 1 | 1 | trigger_event(5211202); stop |
| 5 | 5211202 | 52 / 4 | 1 | 1 | trigger_event(5211203); stop |
| 5 | 5211301 | 52 / 5 | 1 | 1 | trigger_event(5211302); stop |
| 5 | 5211302 | 52 / 6 | 1 | 1 | trigger_event(5211303); stop |
| 5 | 5211401 | 52 / 7 | 1 | 1 | trigger_event(5211402); stop |
| 5 | 5211402 | 52 / 8 | 1 | 1 | trigger_event(5211403); stop |
| 5 | 5211501 | 52 / 9 | 1 | 1 | trigger_event(5211502); stop |
| 5 | 5211502 | 52 / 10 | 1 | 1 | trigger_event(5211503); stop |
| 5 | 5211601 | 52 / 11 | 1 | 1 | trigger_event(5211602); stop |
| 5 | 5211602 | 52 / 12 | 1 | 200 | set_switch(29); stop |
| 5 | 531 | 53 / 13 | 6 | 60 | trigger_event(5311101); trigger_event(5311201); trigger_event(5311301); trigger_event(5311401); trigger_event(5311501); trigger_event(5311601); stop |
| 5 | 5311101 | 53 / 1 | 1 | 1 | trigger_event(5311102); stop |
| 5 | 5311102 | 53 / 2 | 1 | 1 | trigger_event(5311103); stop |
| 5 | 5311201 | 53 / 3 | 1 | 1 | trigger_event(5311202); stop |
| 5 | 5311202 | 53 / 4 | 1 | 1 | trigger_event(5311203); stop |
| 5 | 5311301 | 53 / 5 | 1 | 1 | trigger_event(5311302); stop |
| 5 | 5311302 | 53 / 6 | 1 | 1 | trigger_event(5311303); stop |
| 5 | 5311401 | 53 / 7 | 1 | 1 | trigger_event(5311402); stop |
| 5 | 5311402 | 53 / 8 | 1 | 1 | trigger_event(5311403); stop |
| 5 | 5311501 | 53 / 9 | 1 | 1 | trigger_event(5311502); stop |
| 5 | 5311502 | 53 / 10 | 1 | 1 | trigger_event(5311503); stop |
| 5 | 5311601 | 53 / 11 | 1 | 1 | trigger_event(5311602); stop |
| 5 | 5311602 | 53 / 12 | 1 | 1 | set_switch(26); stop |
| 5 | 601 | 60 / 1 | 3 | 1 | set_switch(18); set_switch(12); set_switch(13); set_switch(14); stop |
| 5 | 611 | 61 / 1 | 8 | 1 | set_switch(15); stop |
| 5 | 701 | 70 / 1 | 2 | 1 | trigger_event(7011); stop |
| 5 | 7011 | 70 / 2 | 5 | 100 | set_switch(24); set_switch(25); set_switch(19); stop |
| 5 | 511 | 51 / 1 | 1 | 150 | trigger_event(5111); stop |
| 5 | 5111 | 51 / 2 | 1 | 1 | trigger_event(5112); stop |
| 5 | 512 | 51 / 3 | 1 | 100 | trigger_event(5121); stop |
| 5 | 5121 | 51 / 4 | 1 | 1 | trigger_event(5122); stop |
| 5 | 513 | 51 / 5 | 1 | 200 | trigger_event(5131); stop |
| 5 | 5131 | 51 / 6 | 1 | 1 | trigger_event(5132); stop |
| 5 | 514 | 51 / 7 | 1 | 130 | trigger_event(5141); stop |
| 5 | 5141 | 51 / 8 | 1 | 1 | trigger_event(5142); stop |
| 5 | 515 | 51 / 9 | 1 | 60 | trigger_event(5151); stop |
| 5 | 5151 | 51 / 10 | 1 | 1 | trigger_event(5152); stop |
| 5 | 516 | 51 / 11 | 1 | 100 | trigger_event(5161); stop |
| 5 | 5161 | 51 / 12 | 1 | 100 | set_switch(21); set_switch(30); set_switch(31); stop |

## Review notes

- Floor 5: event 7111102 targets absent event 7111103
- Floor 5: event 7111202 targets absent event 7111203
- Floor 5: event 7111302 targets absent event 7111303
- Floor 5: event 7111402 targets absent event 7111403
- Floor 5: event 7111502 targets absent event 7111503
- Floor 5: event 5211102 targets absent event 5211103
- Floor 5: event 5211202 targets absent event 5211203
- Floor 5: event 5211302 targets absent event 5211303
- Floor 5: event 5211402 targets absent event 5211403
- Floor 5: event 5211502 targets absent event 5211503
- Floor 5: event 5311102 targets absent event 5311103
- Floor 5: event 5311202 targets absent event 5311203
- Floor 5: event 5311302 targets absent event 5311303
- Floor 5: event 5311402 targets absent event 5311403
- Floor 5: event 5311502 targets absent event 5311503
- Floor 5: event 5111 targets absent event 5112
- Floor 5: event 5121 targets absent event 5122
- Floor 5: event 5131 targets absent event 5132
- Floor 5: event 5141 targets absent event 5142
- Floor 5: event 5151 targets absent event 5152

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
