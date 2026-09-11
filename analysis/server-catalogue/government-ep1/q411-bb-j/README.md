# ４－１：地下に眠る遺跡 — government-ep1/q411-bb-j

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/government-ep1/q411-bb-j.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep1/q411-bb-j.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep1/q411-bb-j.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 411; language J. Static scan: **487 objects, 335 enemy/NPC records, 84 events, 75 script labels.** Script roundtrip: byte-identical.

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
0x07, 0x07, 0x00, 0x02, 0x00
0x0D, 0x0D, 0x00, 0x00, 0x00
0x08, 0x08, 0x00, 0x00, 0x00
0x09, 0x08, 0x00, 0x01, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 27 | 20 | 0 |
| 7 | 173 | 109 | 30 |
| 8 | 231 | 151 | 29 |
| 9 | 45 | 55 | 25 |
| 13 | 11 | 0 | 0 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 7 | 211 | 21 / 1 | 5 | 1 | trigger_event(2111); stop |
| 7 | 2111 | 21 / 2 | 2 | 45 | set_switch(18); stop |
| 7 | 301 | 30 / 1 | 7 | 1 | trigger_event(3011); stop |
| 7 | 3011 | 30 / 2 | 2 | 60 | set_switch(16); set_switch(17); stop |
| 7 | 401 | 40 / 1 | 4 | 1 | set_switch(6); stop |
| 7 | 411 | 41 / 1 | 1 | 1 | set_switch(31); stop |
| 7 | 501 | 50 / 1 | 7 | 1 | trigger_event(5011); stop |
| 7 | 5011 | 50 / 2 | 5 | 60 | set_switch(4); set_switch(12); stop |
| 7 | 521 | 52 / 1 | 3 | 1 | trigger_event(5211); stop |
| 7 | 5211 | 52 / 2 | 2 | 60 | stop |
| 7 | 522 | 52 / 3 | 3 | 45 | trigger_event(5221); stop |
| 7 | 5221 | 52 / 4 | 5 | 60 | trigger_event(5222); stop |
| 7 | 5222 | 52 / 5 | 2 | 60 | set_switch(19); set_switch(20); set_switch(21); set_switch(22); set_switch(23); set_switch(24); stop |
| 7 | 531 | 53 / 1 | 1 | 1 | trigger_event(5311); stop |
| 7 | 5311 | 53 / 2 | 7 | 60 | set_switch(25); set_switch(26); stop |
| 7 | 601 | 60 / 1 | 6 | 1 | trigger_event(6011); stop |
| 7 | 6011 | 60 / 2 | 6 | 30 | trigger_event(6012); stop |
| 7 | 6012 | 60 / 3 | 4 | 60 | set_switch(13); set_switch(14); set_switch(15); stop |
| 7 | 603 | 60 / 4 | 4 | 60 | stop |
| 7 | 611 | 61 / 1 | 3 | 1 | trigger_event(6111); stop |
| 7 | 6111 | 61 / 2 | 4 | 60 | trigger_event(6112); stop |
| 7 | 6112 | 61 / 3 | 5 | 30 | stop |
| 7 | 612 | 61 / 4 | 2 | 45 | trigger_event(6121); stop |
| 7 | 6121 | 61 / 5 | 3 | 90 | trigger_event(6122); stop |
| 7 | 6122 | 61 / 6 | 1 | 60 | trigger_event(6123); stop |
| 7 | 6123 | 61 / 7 | 1 | 60 | trigger_event(6124); stop |
| 7 | 6124 | 61 / 8 | 2 | 120 | set_switch(27); set_switch(28); set_switch(29); set_switch(30); stop |
| 7 | 701 | 70 / 1 | 5 | 1 | trigger_event(7011); stop |
| 7 | 7011 | 70 / 2 | 5 | 30 | set_switch(1); set_switch(2); set_switch(3); set_switch(5); stop |
| 7 | 702 | 70 / 3 | 2 | 1 | set_switch(9); stop |
| 8 | 602 | 60 / 2 | 8 | 10 | set_switch(55); set_switch(56); set_switch(52); set_switch(51); stop |
| 8 | 601 | 60 / 1 | 6 | 10 | stop |
| 8 | 201 | 20 / 1 | 6 | 10 | trigger_event(2011); stop |
| 8 | 2011 | 20 / 2 | 6 | 10 | set_switch(50); set_switch(49); set_switch(45); set_switch(46); set_switch(47); set_switch(48); stop |
| 8 | 701 | 70 / 1 | 7 | 10 | trigger_event(7011); stop |
| 8 | 7011 | 70 / 2 | 6 | 10 | trigger_event(7012); stop |
| 8 | 7012 | 70 / 3 | 7 | 10 | set_switch(43); set_switch(44); stop |
| 8 | 311 | 31 / 1 | 2 | 10 | trigger_event(3111); stop |
| 8 | 3111 | 31 / 2 | 3 | 10 | trigger_event(3112); stop |
| 8 | 3112 | 31 / 3 | 3 | 10 | set_switch(34); set_switch(33); set_switch(36); set_switch(35); set_switch(39); set_switch(40); set_switch(37); set_switch(38); set_switch(31); set_switch(32); stop |
| 8 | 401 | 40 / 1 | 9 | 10 | stop |
| 8 | 211 | 21 / 1 | 5 | 10 | set_switch(41); set_switch(42); stop |
| 8 | 212 | 21 / 2 | 7 | 10 | stop |
| 8 | 221 | 22 / 1 | 4 | 10 | trigger_event(2211); stop |
| 8 | 2211 | 22 / 2 | 5 | 10 | set_switch(28); set_switch(27); stop |
| 8 | 501 | 50 / 1 | 4 | 10 | set_switch(23); set_switch(24); stop |
| 8 | 502 | 50 / 2 | 8 | 10 | set_switch(29); set_switch(30); set_switch(31); set_switch(32); stop |
| 8 | 321 | 32 / 1 | 5 | 10 | trigger_event(3211); stop |
| 8 | 3211 | 32 / 2 | 5 | 10 | trigger_event(3212); stop |
| 8 | 3212 | 32 / 3 | 8 | 10 | set_switch(25); set_switch(26); set_switch(21); set_switch(22); set_switch(20); set_switch(19); set_switch(17); set_switch(18); set_switch(16); set_switch(15); set_switch(13); set_switch(14); set_switch(11); set_switch(12); set_switch(10); set_switch(9); set_switch(1); set_switch(2); set_switch(3); set_switch(4); stop |
| 8 | 241 | 24 / 1 | 6 | 10 | trigger_event(2411); stop |
| 8 | 2411 | 24 / 2 | 2 | 10 | trigger_event(2412); stop |
| 8 | 2412 | 24 / 3 | 3 | 10 | stop |
| 8 | 231 | 23 / 1 | 2 | 10 | trigger_event(2311); stop |
| 8 | 2311 | 23 / 2 | 6 | 10 | set_switch(5); set_switch(6); set_switch(3); set_switch(4); stop |
| 8 | 331 | 33 / 1 | 5 | 10 | trigger_event(3311); stop |
| 8 | 3311 | 33 / 2 | 6 | 10 | trigger_event(3312); stop |
| 8 | 3312 | 33 / 3 | 3 | 10 | trigger_event(3313); stop |
| 8 | 3313 | 33 / 4 | 4 | 10 | set_switch(7); set_switch(8); stop |
| 9 | 101 | 10 / 1 | 4 | 30 | trigger_event(1011); stop |
| 9 | 1011 | 10 / 2 | 2 | 30 | set_switch(39); set_switch(43); set_switch(44); stop |
| 9 | 221 | 22 / 1 | 2 | 30 | trigger_event(2211); stop |
| 9 | 2211 | 22 / 2 | 2 | 90 | trigger_event(2212); stop |
| 9 | 2212 | 22 / 3 | 2 | 90 | trigger_event(2213); stop |
| 9 | 2213 | 22 / 4 | 2 | 90 | set_switch(101); stop |
| 9 | 222 | 22 / 5 | 2 | 30 | trigger_event(2221); stop |
| 9 | 2221 | 22 / 6 | 2 | 90 | trigger_event(2222); stop |
| 9 | 2222 | 22 / 7 | 2 | 90 | trigger_event(2223); stop |
| 9 | 2223 | 22 / 8 | 2 | 90 | set_switch(102); stop |
| 9 | 223 | 22 / 9 | 2 | 30 | trigger_event(2231); stop |
| 9 | 2231 | 22 / 10 | 2 | 90 | trigger_event(2232); stop |
| 9 | 2232 | 22 / 11 | 2 | 90 | trigger_event(2233); stop |
| 9 | 2233 | 22 / 12 | 2 | 90 | set_switch(103); stop |
| 9 | 224 | 22 / 13 | 2 | 30 | trigger_event(2241); stop |
| 9 | 2241 | 22 / 14 | 2 | 90 | trigger_event(2242); stop |
| 9 | 2242 | 22 / 15 | 2 | 90 | trigger_event(2243); stop |
| 9 | 2243 | 22 / 16 | 1 | 120 | set_switch(104); stop |
| 9 | 225 | 22 / 17 | 2 | 30 | trigger_event(2251); stop |
| 9 | 2251 | 22 / 18 | 2 | 90 | trigger_event(2252); stop |
| 9 | 2252 | 22 / 19 | 1 | 90 | trigger_event(2253); stop |
| 9 | 2253 | 22 / 20 | 2 | 120 | set_switch(105); stop |
| 9 | 226 | 22 / 21 | 3 | 30 | trigger_event(2261); stop |
| 9 | 2261 | 22 / 22 | 3 | 90 | trigger_event(2262); stop |
| 9 | 2262 | 22 / 23 | 5 | 90 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
