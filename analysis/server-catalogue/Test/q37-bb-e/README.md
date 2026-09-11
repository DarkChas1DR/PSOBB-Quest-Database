# Ferets Sekrit of Draknes — Test/q37-bb-e

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/Test/q37-bb-e.zip?download=1)**

[Original QST](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/Test/q37-bb-e.qst?download=1) · [Extracted BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/Test/q37-bb-e/q37-bb-e.qst-quest0.bin?download=1) · [Extracted DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/Test/q37-bb-e/q37-bb-e.qst-quest0.dat?download=1)

QST is the preserved original package. BIN and DAT are its decoded payload files, not reassembled scripts. The ZIP contains all three formats.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 37; language E. Static scan: **266 objects, 383 enemy/NPC records, 102 events, 59 script labels.** Script roundtrip: alignment-only.

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
| 0 | 28 | 28 | 0 |
| 1 | 97 | 110 | 45 |
| 2 | 100 | 242 | 54 |
| 5 | 9 | 0 | 0 |
| 11 | 6 | 1 | 1 |
| 12 | 6 | 1 | 1 |
| 13 | 20 | 1 | 1 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 101 | 4 / 1 | 4 | 0 | trigger_event(102); stop |
| 1 | 102 | 4 / 2 | 2 | 0 | trigger_event(103); stop |
| 1 | 103 | 4 / 3 | 2 | 0 | trigger_event(104); stop |
| 1 | 104 | 4 / 4 | 2 | 0 | trigger_event(105); stop |
| 1 | 105 | 4 / 5 | 2 | 0 | set_switch(2); stop |
| 1 | 201 | 2 / 1 | 1 | 0 | trigger_event(202); trigger_event(203); stop |
| 1 | 202 | 2 / 2 | 1 | 0 | trigger_event(204); trigger_event(205); stop |
| 1 | 203 | 2 / 3 | 1 | 0 | trigger_event(206); trigger_event(207); stop |
| 1 | 204 | 2 / 4 | 1 | 0 | trigger_event(208); trigger_event(209); stop |
| 1 | 205 | 2 / 5 | 1 | 0 | trigger_event(210); trigger_event(211); stop |
| 1 | 206 | 2 / 6 | 1 | 0 | trigger_event(212); trigger_event(213); stop |
| 1 | 207 | 2 / 7 | 1 | 0 | trigger_event(214); trigger_event(215); stop |
| 1 | 208 | 2 / 8 | 1 | 0 | trigger_event(216); trigger_event(217); stop |
| 1 | 209 | 2 / 9 | 1 | 0 | trigger_event(218); trigger_event(219); stop |
| 1 | 210 | 2 / 10 | 1 | 0 | trigger_event(220); trigger_event(221); stop |
| 1 | 211 | 2 / 11 | 1 | 0 | trigger_event(222); trigger_event(223); stop |
| 1 | 212 | 2 / 12 | 1 | 0 | trigger_event(224); trigger_event(225); stop |
| 1 | 213 | 2 / 13 | 1 | 0 | trigger_event(226); trigger_event(227); stop |
| 1 | 214 | 2 / 14 | 1 | 0 | trigger_event(228); trigger_event(229); stop |
| 1 | 215 | 2 / 15 | 1 | 0 | trigger_event(230); trigger_event(231); stop |
| 1 | 216 | 2 / 16 | 1 | 0 | stop |
| 1 | 217 | 2 / 17 | 1 | 0 | stop |
| 1 | 218 | 2 / 18 | 1 | 0 | stop |
| 1 | 219 | 2 / 19 | 1 | 0 | stop |
| 1 | 220 | 2 / 20 | 1 | 0 | stop |
| 1 | 221 | 2 / 21 | 1 | 0 | stop |
| 1 | 222 | 2 / 22 | 1 | 0 | stop |
| 1 | 223 | 2 / 23 | 1 | 0 | stop |
| 1 | 224 | 2 / 24 | 1 | 0 | stop |
| 1 | 225 | 2 / 25 | 1 | 0 | stop |
| 1 | 226 | 2 / 26 | 1 | 0 | stop |
| 1 | 227 | 2 / 27 | 1 | 0 | stop |
| 1 | 228 | 2 / 28 | 1 | 0 | stop |
| 1 | 229 | 2 / 29 | 1 | 0 | stop |
| 1 | 230 | 2 / 30 | 1 | 0 | stop |
| 1 | 231 | 2 / 31 | 1 | 0 | stop |
| 1 | 301 | 9 / 1 | 35 | 0 | set_switch(4); stop |
| 1 | 401 | 10 / 2 | 4 | 0 | trigger_event(402); stop |
| 1 | 402 | 10 / 3 | 4 | 0 | trigger_event(403); stop |
| 1 | 403 | 10 / 4 | 4 | 0 | trigger_event(404); stop |
| 1 | 404 | 10 / 5 | 4 | 0 | trigger_event(405); stop |
| 1 | 405 | 10 / 6 | 4 | 0 | trigger_event(406); stop |
| 1 | 406 | 10 / 7 | 4 | 0 | trigger_event(407); stop |
| 1 | 407 | 10 / 8 | 4 | 0 | trigger_event(408); stop |
| 1 | 408 | 10 / 9 | 4 | 0 | set_switch(5); stop |
| 2 | 1 | 0 / 0 | 0 | 0 | construct_objects(room=11,group_or_wave=50); stop |
| 2 | 2 | 11 / 2 | 4 | 0 | stop |
| 2 | 3 | 0 / 0 | 0 | 0 | set_switch(2); construct_objects(room=1,group_or_wave=10); stop |
| 2 | 101 | 2 / 1 | 1 | 0 | trigger_event(102); stop |
| 2 | 102 | 2 / 2 | 3 | 0 | trigger_event(103); stop |
| 2 | 103 | 2 / 3 | 6 | 0 | trigger_event(104); stop |
| 2 | 104 | 2 / 4 | 3 | 0 | set_switch(4); stop |
| 2 | 201 | 11 / 1 | 10 | 0 | set_switch(5); set_switch(6); set_switch(9); set_switch(10); stop |
| 2 | 301 | 13 / 1 | 9 | 0 | trigger_event(302); stop |
| 2 | 302 | 13 / 2 | 6 | 0 | set_switch(8); stop |
| 2 | 401 | 6 / 1 | 1 | 0 | trigger_event(402); stop |
| 2 | 402 | 6 / 2 | 6 | 0 | trigger_event(403); stop |
| 2 | 403 | 6 / 3 | 7 | 0 | trigger_event(404); stop |
| 2 | 404 | 6 / 4 | 6 | 0 | trigger_event(405); stop |
| 2 | 405 | 6 / 5 | 1 | 0 | stop |
| 2 | 501 | 3 / 1 | 1 | 0 | trigger_event(502); stop |
| 2 | 502 | 3 / 2 | 1 | 0 | trigger_event(503); stop |
| 2 | 503 | 3 / 3 | 1 | 0 | trigger_event(504); stop |
| 2 | 504 | 3 / 4 | 1 | 0 | trigger_event(505); stop |
| 2 | 505 | 3 / 5 | 1 | 0 | trigger_event(506); stop |
| 2 | 506 | 3 / 6 | 1 | 0 | trigger_event(507); stop |
| 2 | 507 | 3 / 7 | 1 | 0 | trigger_event(508); stop |
| 2 | 508 | 3 / 8 | 1 | 0 | trigger_event(509); stop |
| 2 | 509 | 3 / 9 | 1 | 0 | trigger_event(510); stop |
| 2 | 510 | 3 / 10 | 1 | 0 | trigger_event(511); stop |
| 2 | 511 | 3 / 11 | 1 | 0 | trigger_event(512); stop |
| 2 | 512 | 3 / 12 | 1 | 0 | trigger_event(513); stop |
| 2 | 513 | 3 / 13 | 1 | 0 | trigger_event(514); stop |
| 2 | 514 | 3 / 14 | 1 | 0 | trigger_event(515); stop |
| 2 | 515 | 3 / 15 | 1 | 0 | stop |
| 2 | 71 | 7 / 1 | 1 | 0 | trigger_event(72); stop |
| 2 | 72 | 7 / 2 | 6 | 0 | stop |
| 2 | 701 | 10 / 1 | 31 | 0 | stop |
| 2 | 801 | 15 / 1 | 8 | 0 | trigger_event(802); stop |
| 2 | 802 | 15 / 2 | 6 | 0 | trigger_event(803); stop |
| 2 | 803 | 15 / 3 | 9 | 0 | trigger_event(804); stop |
| 2 | 804 | 15 / 4 | 10 | 0 | trigger_event(805); stop |
| 2 | 805 | 15 / 5 | 4 | 0 | trigger_event(806); stop |
| 2 | 806 | 15 / 6 | 1 | 0 | set_switch(12); stop |
| 2 | 901 | 12 / 1 | 2 | 0 | trigger_event(902); stop |
| 2 | 902 | 12 / 2 | 2 | 0 | trigger_event(903); stop |
| 2 | 903 | 12 / 3 | 2 | 0 | trigger_event(904); stop |
| 2 | 904 | 12 / 4 | 2 | 0 | trigger_event(905); stop |
| 2 | 905 | 12 / 5 | 1 | 0 | construct_objects(room=12,group_or_wave=5); stop |
| 2 | 906 | 12 / 6 | 11 | 0 | trigger_event(907); stop |
| 2 | 907 | 12 / 7 | 11 | 0 | trigger_event(908); stop |
| 2 | 908 | 12 / 8 | 11 | 0 | trigger_event(909); stop |
| 2 | 909 | 12 / 9 | 6 | 0 | trigger_event(910); stop |
| 2 | 910 | 12 / 10 | 5 | 0 | trigger_event(911); stop |
| 2 | 911 | 12 / 11 | 5 | 0 | trigger_event(912); stop |
| 2 | 912 | 12 / 12 | 3 | 0 | trigger_event(913); stop |
| 2 | 913 | 12 / 13 | 8 | 0 | trigger_event(914); stop |
| 2 | 914 | 12 / 14 | 16 | 0 | trigger_event(915); stop |
| 2 | 915 | 12 / 15 | 1 | 0 | set_switch(7); stop |
| 11 | 1 | 1 / 1 | 1 | 0 | stop |
| 12 | 1 | 1 / 1 | 1 | 0 | stop |
| 13 | 1 | 1 / 1 | 1 | 0 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
