# Maximum Attack 4 2A — maximum-attack-ep2/q86-bb-j

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/maximum-attack-ep2/q86-bb-j.zip?download=1)**

[Original QST](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/maximum-attack-ep2/q86-bb-j.qst?download=1) · [Extracted BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/maximum-attack-ep2/q86-bb-j/q86-bb-j.qst-quest0.bin?download=1) · [Extracted DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/maximum-attack-ep2/q86-bb-j/q86-bb-j.qst-quest0.dat?download=1)

QST is the preserved original package. BIN and DAT are its decoded payload files, not reassembled scripts. The ZIP contains all three formats.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 86; language J. Static scan: **153 objects, 459 enemy/NPC records, 75 events, 210 script labels.** Script roundtrip: alignment-only.

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
| 0 | 54 | 19 | 0 |
| 5 | 54 | 220 | 33 |
| 11 | 45 | 220 | 42 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 5 | 21 | 2 / 1 | 6 | 3 | trigger_event(22); stop |
| 5 | 22 | 2 / 2 | 6 | 3 | trigger_event(23); stop |
| 5 | 23 | 2 / 3 | 8 | 3 | set_switch(2); stop |
| 5 | 31 | 3 / 1 | 8 | 3 | trigger_event(32); stop |
| 5 | 32 | 3 / 2 | 8 | 3 | trigger_event(33); stop |
| 5 | 33 | 3 / 3 | 4 | 3 | trigger_event(34); stop |
| 5 | 34 | 3 / 4 | 8 | 3 | set_switch(3); stop |
| 5 | 41 | 4 / 1 | 8 | 3 | trigger_event(42); stop |
| 5 | 42 | 4 / 2 | 8 | 3 | trigger_event(43); stop |
| 5 | 43 | 4 / 3 | 8 | 3 | trigger_event(44); stop |
| 5 | 44 | 4 / 4 | 8 | 3 | set_switch(4); stop |
| 5 | 51 | 5 / 1 | 4 | 3 | trigger_event(52); stop |
| 5 | 52 | 5 / 2 | 8 | 3 | trigger_event(53); stop |
| 5 | 53 | 5 / 3 | 8 | 3 | trigger_event(54); stop |
| 5 | 54 | 5 / 4 | 8 | 3 | trigger_event(55); stop |
| 5 | 55 | 5 / 5 | 5 | 3 | set_switch(5); stop |
| 5 | 61 | 6 / 1 | 4 | 3 | trigger_event(62); stop |
| 5 | 62 | 6 / 2 | 4 | 3 | trigger_event(63); stop |
| 5 | 63 | 6 / 3 | 2 | 3 | trigger_event(64); stop |
| 5 | 64 | 6 / 4 | 2 | 3 | set_switch(6); stop |
| 5 | 101 | 10 / 1 | 8 | 3 | trigger_event(102); stop |
| 5 | 102 | 10 / 2 | 9 | 3 | trigger_event(103); stop |
| 5 | 103 | 10 / 3 | 8 | 3 | trigger_event(104); stop |
| 5 | 104 | 10 / 4 | 7 | 3 | set_switch(10); stop |
| 5 | 91 | 9 / 1 | 6 | 3 | trigger_event(92); stop |
| 5 | 92 | 9 / 2 | 9 | 3 | trigger_event(93); stop |
| 5 | 93 | 9 / 3 | 5 | 3 | set_switch(9); stop |
| 5 | 81 | 8 / 1 | 8 | 3 | trigger_event(82); stop |
| 5 | 82 | 8 / 2 | 8 | 3 | trigger_event(83); stop |
| 5 | 83 | 8 / 3 | 8 | 3 | trigger_event(84); stop |
| 5 | 84 | 8 / 4 | 8 | 3 | trigger_event(85); stop |
| 5 | 85 | 8 / 5 | 8 | 3 | trigger_event(86); stop |
| 5 | 86 | 8 / 6 | 3 | 3 | set_switch(8); stop |
| 11 | 501 | 50 / 1 | 8 | 3 | trigger_event(502); stop |
| 11 | 502 | 50 / 2 | 8 | 3 | trigger_event(503); stop |
| 11 | 503 | 50 / 3 | 8 | 3 | set_switch(50); trigger_event(504); stop |
| 11 | 504 | 50 / 4 | 8 | 450 | trigger_event(505); stop |
| 11 | 505 | 50 / 5 | 8 | 3 | trigger_event(506); stop |
| 11 | 506 | 50 / 6 | 8 | 3 | set_switch(50); stop |
| 11 | 2111 | 211 / 1 | 2 | 3 | trigger_event(2112); stop |
| 11 | 2112 | 211 / 2 | 2 | 3 | trigger_event(2113); stop |
| 11 | 2113 | 211 / 3 | 6 | 3 | trigger_event(2114); stop |
| 11 | 2114 | 211 / 4 | 2 | 3 | trigger_event(2115); stop |
| 11 | 2115 | 211 / 5 | 8 | 3 | set_switch(211); stop |
| 11 | 301 | 30 / 1 | 6 | 3 | trigger_event(302); stop |
| 11 | 302 | 30 / 2 | 6 | 3 | trigger_event(303); stop |
| 11 | 303 | 30 / 3 | 8 | 3 | stop |
| 11 | 2801 | 280 / 1 | 4 | 3 | trigger_event(2802); stop |
| 11 | 2802 | 280 / 2 | 4 | 3 | trigger_event(2803); stop |
| 11 | 2803 | 280 / 3 | 4 | 3 | trigger_event(2804); stop |
| 11 | 2804 | 280 / 4 | 2 | 3 | trigger_event(2805); stop |
| 11 | 2805 | 280 / 5 | 2 | 3 | set_switch(28); stop |
| 11 | 901 | 90 / 1 | 8 | 3 | trigger_event(902); stop |
| 11 | 902 | 90 / 2 | 8 | 3 | trigger_event(903); stop |
| 11 | 903 | 90 / 3 | 6 | 3 | trigger_event(904); stop |
| 11 | 904 | 90 / 4 | 8 | 3 | trigger_event(905); stop |
| 11 | 905 | 90 / 5 | 2 | 3 | set_switch(90); stop |
| 11 | 201 | 20 / 1 | 6 | 3 | trigger_event(202); stop |
| 11 | 202 | 20 / 2 | 4 | 3 | trigger_event(203); stop |
| 11 | 203 | 20 / 3 | 3 | 3 | trigger_event(204); stop |
| 11 | 204 | 20 / 4 | 1 | 3 | set_switch(20); stop |
| 11 | 2911 | 291 / 1 | 2 | 3 | trigger_event(2912); stop |
| 11 | 2912 | 291 / 2 | 8 | 3 | trigger_event(2913); stop |
| 11 | 2913 | 291 / 3 | 4 | 3 | trigger_event(2914); stop |
| 11 | 2914 | 291 / 4 | 2 | 3 | trigger_event(2915); stop |
| 11 | 2915 | 291 / 5 | 8 | 3 | stop |
| 11 | 951 | 95 / 1 | 8 | 3 | trigger_event(952); stop |
| 11 | 952 | 95 / 2 | 8 | 3 | trigger_event(953); stop |
| 11 | 953 | 95 / 3 | 4 | 3 | trigger_event(954); stop |
| 11 | 954 | 95 / 4 | 4 | 3 | trigger_event(955); stop |
| 11 | 955 | 95 / 5 | 4 | 3 | trigger_event(956); stop |
| 11 | 956 | 95 / 6 | 4 | 3 | set_switch(95); stop |
| 11 | 2901 | 290 / 1 | 10 | 3 | trigger_event(2902); stop |
| 11 | 2902 | 290 / 2 | 2 | 3 | trigger_event(2903); stop |
| 11 | 2903 | 290 / 3 | 2 | 3 | set_switch(29); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
