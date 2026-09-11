# Claire\'s Deal — shops-ep1/q82-bb-j

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/shops-ep1/q82-bb-j.zip?download=1)**

[Original QST](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/shops-ep1/q82-bb-j.qst?download=1) · [Extracted BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/shops-ep1/q82-bb-j/q82-bb-j.qst-quest0.bin?download=1) · [Extracted DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/shops-ep1/q82-bb-j/q82-bb-j.qst-quest0.dat?download=1)

QST is the preserved original package. BIN and DAT are its decoded payload files, not reassembled scripts. The ZIP contains all three formats.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 82; language J. Static scan: **81 objects, 134 enemy/NPC records, 32 events, 281 script labels.** Script roundtrip: alignment-only.

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
| 0 | 28 | 20 | 0 |
| 5 | 46 | 114 | 32 |
| 8 | 7 | 0 | 0 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 5 | 231 | 23 / 1 | 3 | 0 | trigger_event(232); stop |
| 5 | 232 | 23 / 2 | 3 | 0 | trigger_event(233); stop |
| 5 | 233 | 23 / 3 | 4 | 0 | trigger_event(234); stop |
| 5 | 234 | 23 / 4 | 4 | 0 | trigger_event(235); stop |
| 5 | 235 | 23 / 5 | 5 | 0 | set_switch(10); stop |
| 5 | 401 | 40 / 1 | 3 | 0 | trigger_event(402); stop |
| 5 | 402 | 40 / 2 | 4 | 0 | trigger_event(403); stop |
| 5 | 403 | 40 / 3 | 5 | 0 | trigger_event(404); stop |
| 5 | 404 | 40 / 4 | 3 | 0 | set_switch(20); stop |
| 5 | 241 | 24 / 1 | 4 | 0 | trigger_event(242); stop |
| 5 | 242 | 24 / 2 | 4 | 0 | trigger_event(243); stop |
| 5 | 243 | 24 / 3 | 4 | 0 | trigger_event(244); stop |
| 5 | 244 | 24 / 4 | 5 | 0 | trigger_event(245); stop |
| 5 | 245 | 24 / 5 | 3 | 0 | trigger_event(246); stop |
| 5 | 246 | 24 / 6 | 3 | 0 | trigger_event(247); stop |
| 5 | 247 | 24 / 7 | 2 | 0 | set_switch(30); stop |
| 5 | 611 | 61 / 1 | 3 | 0 | trigger_event(612); stop |
| 5 | 612 | 61 / 2 | 3 | 0 | trigger_event(613); stop |
| 5 | 613 | 61 / 3 | 3 | 0 | trigger_event(614); stop |
| 5 | 614 | 61 / 4 | 4 | 0 | trigger_event(615); stop |
| 5 | 615 | 61 / 5 | 3 | 0 | set_switch(40); stop |
| 5 | 321 | 32 / 1 | 3 | 0 | trigger_event(322); stop |
| 5 | 322 | 32 / 2 | 4 | 0 | trigger_event(323); stop |
| 5 | 323 | 32 / 3 | 3 | 0 | trigger_event(324); stop |
| 5 | 324 | 32 / 4 | 3 | 0 | set_switch(50); stop |
| 5 | 711 | 71 / 1 | 3 | 0 | trigger_event(712); stop |
| 5 | 712 | 71 / 2 | 2 | 0 | trigger_event(713); stop |
| 5 | 713 | 71 / 3 | 3 | 0 | trigger_event(714); stop |
| 5 | 714 | 71 / 4 | 3 | 0 | trigger_event(715); stop |
| 5 | 715 | 71 / 5 | 4 | 0 | trigger_event(716); stop |
| 5 | 716 | 71 / 6 | 5 | 0 | trigger_event(717); stop |
| 5 | 717 | 71 / 7 | 6 | 0 | set_switch(60); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
