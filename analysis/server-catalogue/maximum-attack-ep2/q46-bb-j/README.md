# Maximum Attack 4 -2R- — maximum-attack-ep2/q46-bb-j

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/maximum-attack-ep2/q46-bb-j.zip?download=1)**

[Original QST](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/maximum-attack-ep2/q46-bb-j.qst?download=1) · [Extracted BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/maximum-attack-ep2/q46-bb-j/q46-bb-j.qst-quest0.bin?download=1) · [Extracted DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/maximum-attack-ep2/q46-bb-j/q46-bb-j.qst-quest0.dat?download=1)

QST is the preserved original package. BIN and DAT are its decoded payload files, not reassembled scripts. The ZIP contains all three formats.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 46; language J. Static scan: **435 objects, 1433 enemy/NPC records, 264 events, 256 script labels.** Script roundtrip: alignment-only.

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
| 0 | 55 | 19 | 0 |
| 3 | 54 | 220 | 33 |
| 4 | 65 | 249 | 35 |
| 5 | 58 | 180 | 32 |
| 9 | 45 | 220 | 42 |
| 10 | 47 | 241 | 45 |
| 11 | 48 | 195 | 40 |
| 17 | 63 | 109 | 37 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 3 | 21 | 2 / 1 | 6 | 3 | trigger_event(22); stop |
| 3 | 22 | 2 / 2 | 6 | 3 | trigger_event(23); stop |
| 3 | 23 | 2 / 3 | 8 | 3 | set_switch(2); stop |
| 3 | 31 | 3 / 1 | 8 | 3 | trigger_event(32); stop |
| 3 | 32 | 3 / 2 | 8 | 3 | trigger_event(33); stop |
| 3 | 33 | 3 / 3 | 4 | 3 | trigger_event(34); stop |
| 3 | 34 | 3 / 4 | 8 | 3 | set_switch(3); stop |
| 3 | 41 | 4 / 1 | 8 | 3 | trigger_event(42); stop |
| 3 | 42 | 4 / 2 | 8 | 3 | trigger_event(43); stop |
| 3 | 43 | 4 / 3 | 8 | 3 | trigger_event(44); stop |
| 3 | 44 | 4 / 4 | 8 | 3 | set_switch(4); stop |
| 3 | 51 | 5 / 1 | 4 | 3 | trigger_event(52); stop |
| 3 | 52 | 5 / 2 | 8 | 3 | trigger_event(53); stop |
| 3 | 53 | 5 / 3 | 8 | 3 | trigger_event(54); stop |
| 3 | 54 | 5 / 4 | 8 | 3 | trigger_event(55); stop |
| 3 | 55 | 5 / 5 | 5 | 3 | set_switch(5); stop |
| 3 | 61 | 6 / 1 | 4 | 3 | trigger_event(62); stop |
| 3 | 62 | 6 / 2 | 4 | 3 | trigger_event(63); stop |
| 3 | 63 | 6 / 3 | 2 | 3 | trigger_event(64); stop |
| 3 | 64 | 6 / 4 | 2 | 3 | set_switch(6); stop |
| 3 | 101 | 10 / 1 | 8 | 3 | trigger_event(102); stop |
| 3 | 102 | 10 / 2 | 9 | 3 | trigger_event(103); stop |
| 3 | 103 | 10 / 3 | 8 | 3 | trigger_event(104); stop |
| 3 | 104 | 10 / 4 | 7 | 3 | set_switch(10); stop |
| 3 | 91 | 9 / 1 | 6 | 3 | trigger_event(92); stop |
| 3 | 92 | 9 / 2 | 9 | 3 | trigger_event(93); stop |
| 3 | 93 | 9 / 3 | 5 | 3 | set_switch(9); stop |
| 3 | 81 | 8 / 1 | 8 | 3 | trigger_event(82); stop |
| 3 | 82 | 8 / 2 | 8 | 3 | trigger_event(83); stop |
| 3 | 83 | 8 / 3 | 8 | 3 | trigger_event(84); stop |
| 3 | 84 | 8 / 4 | 8 | 3 | trigger_event(85); stop |
| 3 | 85 | 8 / 5 | 8 | 3 | trigger_event(86); stop |
| 3 | 86 | 8 / 6 | 3 | 3 | set_switch(8); stop |
| 4 | 21 | 2 / 1 | 6 | 3 | trigger_event(22); stop |
| 4 | 22 | 2 / 2 | 6 | 3 | trigger_event(23); stop |
| 4 | 23 | 2 / 3 | 8 | 3 | set_switch(2); stop |
| 4 | 31 | 3 / 1 | 8 | 3 | trigger_event(32); stop |
| 4 | 32 | 3 / 2 | 8 | 3 | trigger_event(33); stop |
| 4 | 33 | 3 / 3 | 4 | 3 | trigger_event(34); stop |
| 4 | 34 | 3 / 4 | 8 | 3 | set_switch(3); stop |
| 4 | 41 | 4 / 1 | 8 | 3 | trigger_event(42); stop |
| 4 | 42 | 4 / 2 | 8 | 3 | trigger_event(43); stop |
| 4 | 43 | 4 / 3 | 8 | 3 | trigger_event(44); stop |
| 4 | 44 | 4 / 4 | 8 | 3 | set_switch(4); stop |
| 4 | 51 | 5 / 1 | 4 | 3 | trigger_event(52); stop |
| 4 | 52 | 5 / 2 | 8 | 3 | trigger_event(59); stop |
| 4 | 59 | 5 / 3 | 8 | 3 | trigger_event(54); stop |
| 4 | 54 | 5 / 4 | 8 | 3 | trigger_event(55); stop |
| 4 | 55 | 5 / 5 | 5 | 3 | set_switch(5); stop |
| 4 | 61 | 6 / 1 | 8 | 3 | trigger_event(62); stop |
| 4 | 62 | 6 / 2 | 8 | 3 | trigger_event(63); stop |
| 4 | 63 | 6 / 3 | 8 | 3 | set_switch(6); stop |
| 4 | 101 | 10 / 1 | 8 | 3 | trigger_event(102); stop |
| 4 | 102 | 10 / 2 | 8 | 3 | trigger_event(103); stop |
| 4 | 103 | 10 / 3 | 8 | 3 | set_switch(10); stop |
| 4 | 91 | 9 / 1 | 8 | 3 | trigger_event(92); stop |
| 4 | 92 | 9 / 2 | 8 | 3 | set_switch(9); trigger_event(94); stop |
| 4 | 94 | 9 / 3 | 5 | 450 | trigger_event(95); stop |
| 4 | 95 | 9 / 4 | 7 | 3 | stop |
| 4 | 81 | 8 / 1 | 8 | 3 | trigger_event(82); stop |
| 4 | 82 | 8 / 2 | 8 | 3 | trigger_event(83); stop |
| 4 | 83 | 8 / 3 | 8 | 3 | set_switch(8); stop |
| 4 | 121 | 12 / 1 | 7 | 3 | trigger_event(122); stop |
| 4 | 122 | 12 / 2 | 7 | 3 | trigger_event(123); stop |
| 4 | 123 | 12 / 3 | 7 | 3 | trigger_event(124); stop |
| 4 | 124 | 12 / 4 | 4 | 3 | trigger_event(125); stop |
| 4 | 125 | 12 / 5 | 4 | 3 | trigger_event(126); stop |
| 4 | 126 | 12 / 6 | 7 | 3 | set_switch(12); stop |
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
| 5 | 52 | 5 / 2 | 8 | 3 | trigger_event(59); stop |
| 5 | 59 | 5 / 3 | 8 | 3 | trigger_event(54); stop |
| 5 | 54 | 5 / 4 | 8 | 3 | trigger_event(55); stop |
| 5 | 55 | 5 / 5 | 5 | 3 | set_switch(5); stop |
| 5 | 61 | 6 / 1 | 4 | 3 | trigger_event(62); stop |
| 5 | 62 | 6 / 2 | 4 | 3 | trigger_event(63); stop |
| 5 | 63 | 6 / 3 | 2 | 3 | trigger_event(64); stop |
| 5 | 64 | 6 / 4 | 2 | 3 | trigger_event(65); stop |
| 5 | 65 | 6 / 5 | 2 | 3 | set_switch(6); stop |
| 5 | 121 | 12 / 1 | 8 | 3 | trigger_event(122); stop |
| 5 | 122 | 12 / 2 | 8 | 3 | trigger_event(123); stop |
| 5 | 123 | 12 / 3 | 6 | 3 | trigger_event(124); stop |
| 5 | 124 | 12 / 4 | 6 | 3 | trigger_event(125); stop |
| 5 | 125 | 12 / 5 | 8 | 3 | trigger_event(126); stop |
| 5 | 126 | 12 / 6 | 4 | 3 | trigger_event(127); stop |
| 5 | 127 | 12 / 7 | 4 | 3 | trigger_event(128); stop |
| 5 | 128 | 12 / 8 | 2 | 3 | trigger_event(129); stop |
| 5 | 129 | 12 / 9 | 2 | 3 | trigger_event(130); stop |
| 5 | 130 | 12 / 10 | 2 | 3 | trigger_event(131); stop |
| 5 | 131 | 12 / 11 | 3 | 3 | stop |
| 9 | 501 | 50 / 1 | 8 | 3 | trigger_event(502); stop |
| 9 | 502 | 50 / 2 | 8 | 3 | trigger_event(503); stop |
| 9 | 503 | 50 / 3 | 8 | 3 | set_switch(50); trigger_event(504); stop |
| 9 | 504 | 50 / 4 | 8 | 450 | trigger_event(505); stop |
| 9 | 505 | 50 / 5 | 8 | 3 | trigger_event(506); stop |
| 9 | 506 | 50 / 6 | 8 | 3 | set_switch(50); stop |
| 9 | 2111 | 211 / 1 | 2 | 3 | trigger_event(2112); stop |
| 9 | 2112 | 211 / 2 | 2 | 3 | trigger_event(2113); stop |
| 9 | 2113 | 211 / 3 | 6 | 3 | trigger_event(2114); stop |
| 9 | 2114 | 211 / 4 | 2 | 3 | trigger_event(2115); stop |
| 9 | 2115 | 211 / 5 | 8 | 3 | set_switch(211); stop |
| 9 | 301 | 30 / 1 | 6 | 3 | trigger_event(302); stop |
| 9 | 302 | 30 / 2 | 6 | 3 | trigger_event(303); stop |
| 9 | 303 | 30 / 3 | 8 | 3 | stop |
| 9 | 2801 | 280 / 1 | 4 | 3 | trigger_event(2802); stop |
| 9 | 2802 | 280 / 2 | 4 | 3 | trigger_event(2803); stop |
| 9 | 2803 | 280 / 3 | 4 | 3 | trigger_event(2804); stop |
| 9 | 2804 | 280 / 4 | 2 | 3 | trigger_event(2805); stop |
| 9 | 2805 | 280 / 5 | 2 | 3 | set_switch(28); stop |
| 9 | 901 | 90 / 1 | 8 | 3 | trigger_event(902); stop |
| 9 | 902 | 90 / 2 | 8 | 3 | trigger_event(903); stop |
| 9 | 903 | 90 / 3 | 6 | 3 | trigger_event(904); stop |
| 9 | 904 | 90 / 4 | 8 | 3 | trigger_event(905); stop |
| 9 | 905 | 90 / 5 | 2 | 3 | set_switch(90); stop |
| 9 | 201 | 20 / 1 | 6 | 3 | trigger_event(202); stop |
| 9 | 202 | 20 / 2 | 4 | 3 | trigger_event(203); stop |
| 9 | 203 | 20 / 3 | 3 | 3 | trigger_event(204); stop |
| 9 | 204 | 20 / 4 | 1 | 3 | set_switch(20); stop |
| 9 | 2911 | 291 / 1 | 2 | 3 | trigger_event(2912); stop |
| 9 | 2912 | 291 / 2 | 8 | 3 | trigger_event(2913); stop |
| 9 | 2913 | 291 / 3 | 4 | 3 | trigger_event(2914); stop |
| 9 | 2914 | 291 / 4 | 2 | 3 | trigger_event(2915); stop |
| 9 | 2915 | 291 / 5 | 8 | 3 | stop |
| 9 | 951 | 95 / 1 | 8 | 3 | trigger_event(952); stop |
| 9 | 952 | 95 / 2 | 8 | 3 | trigger_event(953); stop |
| 9 | 953 | 95 / 3 | 4 | 3 | trigger_event(954); stop |
| 9 | 954 | 95 / 4 | 4 | 3 | trigger_event(955); stop |
| 9 | 955 | 95 / 5 | 4 | 3 | trigger_event(956); stop |
| 9 | 956 | 95 / 6 | 4 | 3 | set_switch(95); stop |
| 9 | 2901 | 290 / 1 | 10 | 3 | trigger_event(2902); stop |
| 9 | 2902 | 290 / 2 | 2 | 3 | trigger_event(2903); stop |
| 9 | 2903 | 290 / 3 | 2 | 3 | set_switch(29); stop |
| 10 | 501 | 50 / 1 | 8 | 3 | trigger_event(502); stop |
| 10 | 502 | 50 / 2 | 8 | 3 | trigger_event(503); stop |
| 10 | 503 | 50 / 3 | 8 | 3 | trigger_event(504); set_switch(50); stop |
| 10 | 504 | 50 / 4 | 8 | 3 | trigger_event(505); stop |
| 10 | 505 | 50 / 5 | 8 | 3 | trigger_event(506); stop |
| 10 | 506 | 50 / 6 | 8 | 3 | stop |
| 10 | 2111 | 211 / 1 | 2 | 3 | trigger_event(2112); stop |
| 10 | 2112 | 211 / 2 | 2 | 3 | trigger_event(2113); stop |
| 10 | 2113 | 211 / 3 | 6 | 3 | trigger_event(2114); stop |
| 10 | 2114 | 211 / 4 | 2 | 3 | trigger_event(2115); stop |
| 10 | 2115 | 211 / 5 | 8 | 3 | set_switch(211); stop |
| 10 | 301 | 30 / 1 | 6 | 3 | trigger_event(302); stop |
| 10 | 302 | 30 / 2 | 6 | 3 | trigger_event(303); stop |
| 10 | 303 | 30 / 3 | 8 | 3 | trigger_event(304); stop |
| 10 | 304 | 30 / 4 | 6 | 3 | stop |
| 10 | 2801 | 280 / 1 | 4 | 3 | trigger_event(2802); stop |
| 10 | 2802 | 280 / 2 | 4 | 3 | trigger_event(2803); stop |
| 10 | 2803 | 280 / 3 | 4 | 3 | trigger_event(2804); stop |
| 10 | 2804 | 280 / 4 | 2 | 3 | trigger_event(2805); stop |
| 10 | 2805 | 280 / 5 | 2 | 3 | set_switch(28); stop |
| 10 | 901 | 90 / 1 | 5 | 3 | trigger_event(902); stop |
| 10 | 902 | 90 / 2 | 5 | 3 | trigger_event(903); stop |
| 10 | 903 | 90 / 3 | 8 | 3 | trigger_event(904); stop |
| 10 | 904 | 90 / 4 | 4 | 3 | set_switch(90); stop |
| 10 | 201 | 20 / 1 | 6 | 3 | trigger_event(202); stop |
| 10 | 202 | 20 / 2 | 6 | 3 | trigger_event(203); stop |
| 10 | 203 | 20 / 3 | 4 | 3 | trigger_event(204); stop |
| 10 | 204 | 20 / 4 | 4 | 3 | trigger_event(205); stop |
| 10 | 205 | 20 / 5 | 4 | 3 | set_switch(20); stop |
| 10 | 2911 | 291 / 1 | 2 | 3 | trigger_event(2912); stop |
| 10 | 2912 | 291 / 2 | 8 | 3 | trigger_event(2913); stop |
| 10 | 2913 | 291 / 3 | 4 | 3 | trigger_event(2914); stop |
| 10 | 2914 | 291 / 4 | 8 | 3 | trigger_event(2915); stop |
| 10 | 951 | 95 / 1 | 6 | 3 | trigger_event(952); stop |
| 10 | 952 | 95 / 2 | 6 | 3 | trigger_event(953); stop |
| 10 | 953 | 95 / 3 | 8 | 3 | trigger_event(954); stop |
| 10 | 954 | 95 / 4 | 4 | 3 | trigger_event(955); stop |
| 10 | 955 | 95 / 5 | 4 | 3 | trigger_event(956); stop |
| 10 | 956 | 95 / 6 | 6 | 3 | trigger_event(957); stop |
| 10 | 957 | 95 / 7 | 5 | 3 | set_switch(40); stop |
| 10 | 2901 | 290 / 1 | 6 | 3 | trigger_event(2902); stop |
| 10 | 2902 | 290 / 2 | 6 | 3 | trigger_event(2903); stop |
| 10 | 2903 | 290 / 3 | 4 | 3 | trigger_event(2904); stop |
| 10 | 2904 | 290 / 4 | 4 | 3 | trigger_event(2905); stop |
| 10 | 2905 | 290 / 5 | 4 | 3 | set_switch(29); stop |
| 11 | 501 | 50 / 1 | 8 | 3 | trigger_event(502); stop |
| 11 | 502 | 50 / 2 | 8 | 3 | trigger_event(503); stop |
| 11 | 503 | 50 / 3 | 8 | 3 | trigger_event(504); set_switch(50); stop |
| 11 | 504 | 50 / 4 | 8 | 3 | trigger_event(505); stop |
| 11 | 505 | 50 / 5 | 8 | 3 | trigger_event(506); stop |
| 11 | 506 | 50 / 6 | 8 | 3 | stop |
| 11 | 2111 | 211 / 1 | 2 | 3 | trigger_event(2112); stop |
| 11 | 2112 | 211 / 2 | 2 | 3 | trigger_event(2113); stop |
| 11 | 2113 | 211 / 3 | 6 | 3 | trigger_event(2114); stop |
| 11 | 2114 | 211 / 4 | 2 | 3 | trigger_event(2115); stop |
| 11 | 2115 | 211 / 5 | 8 | 3 | set_switch(211); stop |
| 11 | 301 | 30 / 1 | 6 | 3 | trigger_event(302); stop |
| 11 | 302 | 30 / 2 | 6 | 3 | trigger_event(303); stop |
| 11 | 303 | 30 / 3 | 8 | 3 | trigger_event(304); stop |
| 11 | 304 | 30 / 4 | 6 | 3 | stop |
| 11 | 2801 | 280 / 1 | 4 | 3 | trigger_event(2802); stop |
| 11 | 2802 | 280 / 2 | 4 | 3 | trigger_event(2803); stop |
| 11 | 2803 | 280 / 3 | 4 | 3 | trigger_event(2804); stop |
| 11 | 2804 | 280 / 4 | 2 | 3 | trigger_event(2805); stop |
| 11 | 2805 | 280 / 5 | 2 | 3 | set_switch(28); stop |
| 11 | 901 | 90 / 1 | 4 | 3 | trigger_event(902); stop |
| 11 | 902 | 90 / 2 | 4 | 3 | trigger_event(903); stop |
| 11 | 903 | 90 / 3 | 3 | 3 | set_switch(90); stop |
| 11 | 201 | 20 / 1 | 6 | 3 | trigger_event(202); stop |
| 11 | 202 | 20 / 2 | 6 | 3 | trigger_event(203); stop |
| 11 | 203 | 20 / 3 | 3 | 3 | trigger_event(204); stop |
| 11 | 204 | 20 / 4 | 3 | 3 | trigger_event(205); stop |
| 11 | 205 | 20 / 5 | 4 | 3 | set_switch(20); stop |
| 11 | 2911 | 291 / 1 | 2 | 3 | trigger_event(2912); stop |
| 11 | 2912 | 291 / 2 | 2 | 3 | trigger_event(2913); stop |
| 11 | 2913 | 291 / 3 | 2 | 3 | trigger_event(2914); stop |
| 11 | 2914 | 291 / 4 | 2 | 3 | trigger_event(2915); stop |
| 11 | 2915 | 291 / 5 | 2 | 3 | stop |
| 11 | 951 | 95 / 1 | 6 | 3 | trigger_event(952); stop |
| 11 | 952 | 95 / 2 | 6 | 3 | trigger_event(953); stop |
| 11 | 953 | 95 / 3 | 6 | 3 | trigger_event(954); stop |
| 11 | 954 | 95 / 4 | 8 | 3 | trigger_event(955); stop |
| 11 | 955 | 95 / 5 | 8 | 3 | trigger_event(956); stop |
| 11 | 956 | 95 / 6 | 4 | 3 | trigger_event(957); stop |
| 11 | 957 | 95 / 7 | 4 | 3 | set_switch(95); set_switch(21); stop |
| 17 | 11 | 1 / 1 | 6 | 3 | trigger_event(12); stop |
| 17 | 12 | 1 / 2 | 2 | 3 | trigger_event(13); stop |
| 17 | 13 | 1 / 3 | 2 | 3 | trigger_event(14); stop |
| 17 | 14 | 1 / 4 | 3 | 3 | stop |
| 17 | 21 | 2 / 1 | 5 | 3 | trigger_event(22); stop |
| 17 | 22 | 2 / 2 | 5 | 3 | trigger_event(23); stop |
| 17 | 23 | 2 / 3 | 3 | 3 | trigger_event(24); stop |
| 17 | 24 | 2 / 4 | 2 | 3 | stop |
| 17 | 201 | 20 / 1 | 2 | 3 | trigger_event(202); stop |
| 17 | 202 | 20 / 2 | 4 | 3 | trigger_event(203); stop |
| 17 | 203 | 20 / 3 | 6 | 3 | construct_objects(room=20,group_or_wave=1); construct_objects(room=20,group_or_wave=2); stop |
| 17 | 311 | 3 / 1 | 4 | 3 | trigger_event(321); stop |
| 17 | 321 | 3 / 2 | 2 | 3 | trigger_event(331); stop |
| 17 | 331 | 3 / 3 | 1 | 3 | construct_objects(room=3,group_or_wave=1); stop |
| 17 | 312 | 3 / 4 | 4 | 3 | trigger_event(322); stop |
| 17 | 322 | 3 / 5 | 2 | 3 | trigger_event(332); stop |
| 17 | 332 | 3 / 6 | 3 | 3 | construct_objects(room=3,group_or_wave=2); stop |
| 17 | 101 | 10 / 1 | 3 | 3 | trigger_event(102); stop |
| 17 | 102 | 10 / 2 | 2 | 3 | trigger_event(103); stop |
| 17 | 103 | 10 / 3 | 2 | 3 | trigger_event(104); stop |
| 17 | 104 | 10 / 4 | 2 | 3 | trigger_event(105); stop |
| 17 | 105 | 10 / 5 | 3 | 3 | trigger_event(106); stop |
| 17 | 106 | 10 / 6 | 2 | 3 | set_switch(11); stop |
| 17 | 107 | 10 / 7 | 3 | 3 | trigger_event(108); stop |
| 17 | 108 | 10 / 8 | 2 | 3 | trigger_event(109); stop |
| 17 | 109 | 10 / 9 | 2 | 3 | trigger_event(110); stop |
| 17 | 110 | 10 / 10 | 2 | 3 | trigger_event(111); stop |
| 17 | 111 | 10 / 11 | 3 | 3 | trigger_event(112); stop |
| 17 | 112 | 10 / 12 | 2 | 3 | set_switch(10); stop |
| 17 | 301 | 30 / 1 | 1 | 3 | trigger_event(302); stop |
| 17 | 302 | 30 / 2 | 4 | 3 | trigger_event(303); stop |
| 17 | 303 | 30 / 3 | 2 | 3 | trigger_event(304); stop |
| 17 | 304 | 30 / 4 | 5 | 3 | trigger_event(305); stop |
| 17 | 305 | 30 / 5 | 3 | 3 | trigger_event(306); stop |
| 17 | 306 | 30 / 6 | 4 | 3 | trigger_event(307); stop |
| 17 | 307 | 30 / 7 | 3 | 3 | trigger_event(308); stop |
| 17 | 308 | 30 / 8 | 3 | 3 | stop |

## Review notes

- Floor 10: event 2914 targets absent event 2915
