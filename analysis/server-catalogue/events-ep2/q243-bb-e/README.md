# Defend the main room! — events-ep2/q243-bb-e

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/events-ep2/q243-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/events-ep2/q243-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/events-ep2/q243-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 243; language E. Static scan: **229 objects, 564 enemy/NPC records, 140 events, 219 script labels.** Script roundtrip: alignment-only.

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
0x05, 0x17, 0x00, 0x00, 0x00
0x0B, 0x1D, 0x00, 0x02, 0x00
0x11, 0x23, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 54 | 19 | 0 |
| 5 | 58 | 169 | 32 |
| 11 | 48 | 195 | 40 |
| 17 | 69 | 181 | 68 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 5 | 21 | 2 / 1 | 3 | 3 | trigger_event(22); stop |
| 5 | 22 | 2 / 2 | 2 | 3 | trigger_event(23); stop |
| 5 | 23 | 2 / 3 | 4 | 3 | set_switch(2); stop |
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
| 17 | 11 | 1 / 1 | 0 | 3 | trigger_event(12); stop |
| 17 | 12 | 1 / 2 | 0 | 3 | trigger_event(13); stop |
| 17 | 13 | 1 / 3 | 0 | 3 | trigger_event(14); stop |
| 17 | 14 | 1 / 4 | 0 | 3 | stop |
| 17 | 21 | 2 / 1 | 0 | 3 | trigger_event(22); stop |
| 17 | 22 | 2 / 2 | 0 | 3 | trigger_event(23); stop |
| 17 | 23 | 2 / 3 | 0 | 3 | trigger_event(24); stop |
| 17 | 24 | 2 / 4 | 0 | 3 | stop |
| 17 | 201 | 20 / 1 | 0 | 3 | trigger_event(202); stop |
| 17 | 202 | 20 / 2 | 0 | 3 | trigger_event(203); stop |
| 17 | 203 | 20 / 3 | 0 | 3 | construct_objects(room=20,group_or_wave=1); construct_objects(room=20,group_or_wave=2); stop |
| 17 | 311 | 3 / 1 | 0 | 3 | trigger_event(321); stop |
| 17 | 321 | 3 / 2 | 0 | 3 | trigger_event(331); stop |
| 17 | 331 | 3 / 3 | 0 | 3 | construct_objects(room=3,group_or_wave=1); stop |
| 17 | 312 | 3 / 4 | 0 | 3 | trigger_event(322); stop |
| 17 | 322 | 3 / 5 | 0 | 3 | trigger_event(332); stop |
| 17 | 332 | 3 / 6 | 0 | 3 | construct_objects(room=3,group_or_wave=2); stop |
| 17 | 101 | 10 / 1 | 0 | 3 | trigger_event(102); stop |
| 17 | 102 | 10 / 2 | 0 | 3 | trigger_event(103); stop |
| 17 | 103 | 10 / 3 | 0 | 3 | trigger_event(104); stop |
| 17 | 104 | 10 / 4 | 0 | 3 | trigger_event(105); stop |
| 17 | 105 | 10 / 5 | 0 | 3 | trigger_event(106); stop |
| 17 | 106 | 10 / 6 | 0 | 3 | set_switch(11); stop |
| 17 | 107 | 10 / 7 | 0 | 3 | trigger_event(108); stop |
| 17 | 108 | 10 / 8 | 0 | 3 | trigger_event(109); stop |
| 17 | 109 | 10 / 9 | 0 | 3 | trigger_event(110); stop |
| 17 | 110 | 10 / 10 | 0 | 3 | trigger_event(111); stop |
| 17 | 111 | 10 / 11 | 0 | 3 | trigger_event(112); stop |
| 17 | 112 | 10 / 12 | 0 | 3 | set_switch(10); stop |
| 17 | 301 | 30 / 1 | 6 | 3 | trigger_event(302); stop |
| 17 | 302 | 30 / 2 | 4 | 3 | trigger_event(303); stop |
| 17 | 303 | 30 / 3 | 5 | 3 | trigger_event(304); stop |
| 17 | 304 | 30 / 4 | 8 | 3 | trigger_event(305); stop |
| 17 | 305 | 30 / 5 | 5 | 3 | trigger_event(306); stop |
| 17 | 306 | 30 / 6 | 3 | 3 | trigger_event(307); stop |
| 17 | 307 | 30 / 7 | 9 | 3 | trigger_event(308); stop |
| 17 | 308 | 30 / 8 | 3 | 3 | stop |
| 17 | 350 | 30 / 1 | 6 | 30 | trigger_event(351); stop |
| 17 | 351 | 30 / 2 | 4 | 30 | trigger_event(352); stop |
| 17 | 352 | 30 / 3 | 5 | 30 | trigger_event(353); stop |
| 17 | 353 | 30 / 4 | 8 | 30 | trigger_event(354); stop |
| 17 | 354 | 30 / 5 | 5 | 30 | trigger_event(355); stop |
| 17 | 355 | 30 / 6 | 3 | 30 | trigger_event(356); stop |
| 17 | 356 | 30 / 7 | 9 | 30 | trigger_event(357); stop |
| 17 | 357 | 30 / 8 | 3 | 30 | trigger_event(358); stop |
| 17 | 358 | 30 / 9 | 5 | 30 | trigger_event(359); stop |
| 17 | 359 | 30 / 10 | 3 | 30 | trigger_event(360); stop |
| 17 | 360 | 30 / 11 | 3 | 30 | trigger_event(361); stop |
| 17 | 361 | 30 / 12 | 6 | 30 | trigger_event(362); stop |
| 17 | 362 | 30 / 13 | 6 | 30 | trigger_event(363); stop |
| 17 | 363 | 30 / 14 | 6 | 30 | trigger_event(364); stop |
| 17 | 364 | 30 / 15 | 9 | 30 | trigger_event(365); stop |
| 17 | 365 | 30 / 16 | 6 | 30 | trigger_event(366); stop |
| 17 | 366 | 30 / 17 | 8 | 30 | trigger_event(367); stop |
| 17 | 367 | 30 / 18 | 6 | 300 | trigger_event(368); stop |
| 17 | 368 | 30 / 19 | 4 | 30 | trigger_event(369); stop |
| 17 | 369 | 30 / 20 | 4 | 30 | trigger_event(370); stop |
| 17 | 370 | 30 / 21 | 8 | 30 | trigger_event(371); stop |
| 17 | 371 | 30 / 22 | 5 | 30 | trigger_event(372); stop |
| 17 | 372 | 30 / 23 | 6 | 300 | trigger_event(373); stop |
| 17 | 373 | 30 / 24 | 4 | 30 | trigger_event(374); stop |
| 17 | 374 | 30 / 25 | 7 | 30 | trigger_event(375); stop |
| 17 | 375 | 30 / 26 | 5 | 30 | trigger_event(376); stop |
| 17 | 376 | 30 / 27 | 6 | 30 | trigger_event(377); stop |
| 17 | 377 | 30 / 28 | 7 | 30 | trigger_event(378); stop |
| 17 | 378 | 30 / 29 | 5 | 300 | trigger_event(379); stop |
| 17 | 379 | 30 / 30 | 7 | 300 | trigger_event(380); construct_objects(room=30,group_or_wave=1); stop |
| 17 | 380 | 30 / 31 | 12 | 3000 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

A backup is present; decompressed content identical: True. See [text differences](<backup-diff.txt>).

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
