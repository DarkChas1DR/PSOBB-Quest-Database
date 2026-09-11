# 9-6:The Chosen (2/2) — government-ep4/q706-bb-e

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/government-ep4/q706-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep4/q706-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/government-ep4/q706-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode4; header quest ID 706; language E. Static scan: **237 objects, 183 enemy/NPC records, 62 events, 203 script labels.** Script roundtrip: byte-identical.

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
0x00, 0x2D, 0x00, 0x00, 0x00
0x07, 0x2A, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 27 | 22 | 0 |
| 7 | 210 | 161 | 62 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 7 | 201 | 20 / 1 | 1 | 30 | trigger_event(202); stop |
| 7 | 202 | 20 / 2 | 2 | 30 | trigger_event(203); stop |
| 7 | 203 | 20 / 3 | 1 | 75 | set_switch(203); stop |
| 7 | 204 | 20 / 4 | 1 | 30 | trigger_event(205); stop |
| 7 | 205 | 20 / 5 | 1 | 30 | trigger_event(206); stop |
| 7 | 206 | 20 / 6 | 1 | 30 | set_switch(206); stop |
| 7 | 207 | 20 / 7 | 1 | 30 | trigger_event(208); stop |
| 7 | 208 | 20 / 8 | 1 | 30 | trigger_event(209); stop |
| 7 | 209 | 20 / 9 | 1 | 30 | set_switch(209); stop |
| 7 | 210 | 20 / 10 | 1 | 30 | trigger_event(211); stop |
| 7 | 211 | 20 / 11 | 1 | 30 | trigger_event(211); stop |
| 7 | 212 | 20 / 12 | 1 | 30 | set_switch(212); stop |
| 7 | 213 | 20 / 13 | 1 | 30 | trigger_event(214); stop |
| 7 | 214 | 20 / 14 | 1 | 30 | trigger_event(215); stop |
| 7 | 215 | 20 / 15 | 1 | 30 | set_switch(215); stop |
| 7 | 221 | 22 / 1 | 2 | 30 | trigger_event(222); stop |
| 7 | 222 | 22 / 2 | 2 | 30 | trigger_event(223); stop |
| 7 | 223 | 22 / 3 | 3 | 75 | set_switch(223); stop |
| 7 | 224 | 22 / 4 | 2 | 30 | trigger_event(225); stop |
| 7 | 225 | 22 / 5 | 2 | 30 | trigger_event(226); stop |
| 7 | 226 | 22 / 6 | 2 | 30 | set_switch(226); stop |
| 7 | 227 | 22 / 7 | 2 | 30 | trigger_event(228); stop |
| 7 | 228 | 22 / 8 | 2 | 30 | trigger_event(229); stop |
| 7 | 229 | 22 / 9 | 2 | 30 | set_switch(229); stop |
| 7 | 231 | 23 / 1 | 5 | 30 | trigger_event(232); stop |
| 7 | 232 | 23 / 2 | 5 | 30 | set_switch(23); stop |
| 7 | 241 | 24 / 1 | 4 | 30 | trigger_event(242); stop |
| 7 | 242 | 24 / 2 | 6 | 30 | set_switch(24); stop |
| 7 | 251 | 25 / 1 | 2 | 30 | trigger_event(252); stop |
| 7 | 252 | 25 / 2 | 2 | 30 | trigger_event(253); stop |
| 7 | 253 | 25 / 3 | 2 | 75 | set_switch(153); stop |
| 7 | 254 | 25 / 4 | 2 | 30 | trigger_event(255); stop |
| 7 | 255 | 25 / 5 | 2 | 30 | trigger_event(256); stop |
| 7 | 256 | 25 / 6 | 2 | 30 | set_switch(156); stop |
| 7 | 257 | 25 / 7 | 1 | 30 | trigger_event(258); stop |
| 7 | 258 | 25 / 8 | 2 | 30 | trigger_event(259); stop |
| 7 | 259 | 25 / 9 | 2 | 30 | set_switch(159); stop |
| 7 | 261 | 26 / 1 | 2 | 30 | trigger_event(262); stop |
| 7 | 262 | 26 / 2 | 2 | 30 | trigger_event(263); stop |
| 7 | 263 | 26 / 3 | 3 | 75 | set_switch(163); stop |
| 7 | 264 | 26 / 4 | 2 | 30 | trigger_event(265); stop |
| 7 | 265 | 26 / 5 | 2 | 30 | trigger_event(266); stop |
| 7 | 266 | 26 / 6 | 3 | 30 | set_switch(166); stop |
| 7 | 267 | 26 / 7 | 2 | 30 | trigger_event(268); stop |
| 7 | 268 | 26 / 8 | 1 | 30 | trigger_event(269); stop |
| 7 | 269 | 26 / 9 | 2 | 30 | set_switch(169); stop |
| 7 | 271 | 27 / 1 | 6 | 90 | trigger_event(272); stop |
| 7 | 272 | 27 / 2 | 6 | 30 | set_switch(27); stop |
| 7 | 401 | 40 / 1 | 6 | 30 | trigger_event(402); stop |
| 7 | 402 | 40 / 2 | 5 | 30 | set_switch(40); stop |
| 7 | 411 | 41 / 1 | 6 | 30 | trigger_event(412); stop |
| 7 | 412 | 41 / 2 | 6 | 30 | set_switch(41); stop |
| 7 | 421 | 42 / 1 | 2 | 30 | trigger_event(422); stop |
| 7 | 422 | 42 / 2 | 1 | 30 | trigger_event(423); stop |
| 7 | 423 | 42 / 3 | 1 | 90 | set_switch(123); stop |
| 7 | 424 | 42 / 4 | 2 | 30 | trigger_event(425); stop |
| 7 | 425 | 42 / 5 | 5 | 30 | set_switch(125); stop |
| 7 | 501 | 50 / 1 | 5 | 30 | trigger_event(502); stop |
| 7 | 502 | 50 / 2 | 5 | 30 | set_switch(50); stop |
| 7 | 503 | 50 / 3 | 5 | 30 | stop |
| 7 | 631 | 63 / 1 | 0 | 3 | stop |
| 7 | 641 | 64 / 1 | 0 | 3 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
