# Maximum Attack 4 -R- — maximum-attack-ep1/q45-bb-j

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/maximum-attack-ep1/q45-bb-j.zip?download=1)**

[Original QST](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/maximum-attack-ep1/q45-bb-j.qst?download=1) · [Extracted BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/maximum-attack-ep1/q45-bb-j/q45-bb-j.qst-quest0.bin?download=1) · [Extracted DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/server-catalogue/maximum-attack-ep1/q45-bb-j/q45-bb-j.qst-quest0.dat?download=1)

QST is the preserved original package. BIN and DAT are its decoded payload files, not reassembled scripts. The ZIP contains all three formats.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 45; language J. Static scan: **468 objects, 1400 enemy/NPC records, 261 events, 274 script labels.** Script roundtrip: byte-identical.

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
| 0 | 28 | 21 | 0 |
| 3 | 48 | 210 | 33 |
| 4 | 67 | 218 | 41 |
| 5 | 60 | 166 | 35 |
| 6 | 46 | 132 | 26 |
| 7 | 47 | 118 | 28 |
| 8 | 72 | 230 | 41 |
| 9 | 72 | 190 | 36 |
| 10 | 22 | 114 | 20 |
| 14 | 6 | 1 | 1 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 3 | 101 | 10 / 1 | 7 | 3 | trigger_event(102); stop |
| 3 | 102 | 10 / 2 | 7 | 3 | trigger_event(103); stop |
| 3 | 103 | 10 / 3 | 6 | 3 | set_switch(10); stop |
| 3 | 201 | 20 / 1 | 7 | 3 | trigger_event(202); stop |
| 3 | 202 | 20 / 2 | 7 | 3 | trigger_event(203); stop |
| 3 | 203 | 20 / 3 | 7 | 3 | trigger_event(204); stop |
| 3 | 204 | 20 / 4 | 5 | 300 | trigger_event(205); stop |
| 3 | 205 | 20 / 5 | 7 | 3 | trigger_event(206); stop |
| 3 | 206 | 20 / 6 | 7 | 3 | set_switch(20); stop |
| 3 | 221 | 22 / 1 | 8 | 3 | trigger_event(222); stop |
| 3 | 222 | 22 / 2 | 8 | 3 | trigger_event(223); stop |
| 3 | 223 | 22 / 3 | 4 | 3 | set_switch(22); stop |
| 3 | 121 | 12 / 1 | 7 | 3 | trigger_event(122); stop |
| 3 | 122 | 12 / 2 | 7 | 3 | trigger_event(123); stop |
| 3 | 123 | 12 / 3 | 5 | 3 | trigger_event(124); stop |
| 3 | 124 | 12 / 4 | 6 | 3 | set_switch(12); stop |
| 3 | 211 | 21 / 1 | 5 | 3 | trigger_event(212); stop |
| 3 | 212 | 21 / 2 | 5 | 3 | trigger_event(213); stop |
| 3 | 213 | 21 / 3 | 7 | 3 | trigger_event(214); stop |
| 3 | 214 | 21 / 4 | 7 | 150 | trigger_event(215); stop |
| 3 | 215 | 21 / 5 | 6 | 3 | set_switch(21); stop |
| 3 | 111 | 11 / 1 | 6 | 3 | trigger_event(112); stop |
| 3 | 112 | 11 / 2 | 6 | 3 | trigger_event(113); stop |
| 3 | 113 | 11 / 3 | 3 | 3 | trigger_event(114); stop |
| 3 | 114 | 11 / 4 | 4 | 300 | trigger_event(115); stop |
| 3 | 115 | 11 / 5 | 8 | 3 | trigger_event(116); stop |
| 3 | 116 | 11 / 6 | 8 | 3 | set_switch(11); stop |
| 3 | 131 | 13 / 1 | 8 | 3 | trigger_event(132); stop |
| 3 | 132 | 13 / 2 | 8 | 3 | trigger_event(133); stop |
| 3 | 133 | 13 / 3 | 8 | 300 | trigger_event(134); stop |
| 3 | 134 | 13 / 4 | 5 | 3 | trigger_event(135); stop |
| 3 | 135 | 13 / 5 | 5 | 3 | trigger_event(136); stop |
| 3 | 136 | 13 / 6 | 6 | 3 | set_switch(13); stop |
| 4 | 121 | 12 / 1 | 7 | 3 | trigger_event(122); stop |
| 4 | 122 | 12 / 2 | 7 | 3 | trigger_event(123); stop |
| 4 | 123 | 12 / 3 | 5 | 3 | trigger_event(124); stop |
| 4 | 124 | 12 / 4 | 6 | 3 | set_switch(121); stop |
| 4 | 221 | 22 / 1 | 8 | 3 | trigger_event(222); stop |
| 4 | 222 | 22 / 2 | 8 | 3 | trigger_event(223); stop |
| 4 | 223 | 22 / 3 | 4 | 3 | set_switch(22); stop |
| 4 | 601 | 60 / 1 | 7 | 3 | trigger_event(602); stop |
| 4 | 602 | 60 / 2 | 7 | 3 | trigger_event(603); stop |
| 4 | 603 | 60 / 3 | 7 | 3 | trigger_event(604); set_switch(60); stop |
| 4 | 604 | 60 / 4 | 1 | 450 | stop |
| 4 | 451 | 45 / 1 | 6 | 3 | trigger_event(452); stop |
| 4 | 452 | 45 / 2 | 6 | 3 | trigger_event(453); stop |
| 4 | 453 | 45 / 3 | 5 | 3 | trigger_event(454); stop |
| 4 | 454 | 45 / 4 | 3 | 3 | set_switch(45); stop |
| 4 | 301 | 30 / 1 | 5 | 3 | trigger_event(302); stop |
| 4 | 302 | 30 / 2 | 5 | 3 | trigger_event(303); stop |
| 4 | 303 | 30 / 3 | 5 | 3 | trigger_event(304); stop |
| 4 | 304 | 30 / 4 | 5 | 3 | set_switch(30); stop |
| 4 | 351 | 35 / 1 | 8 | 3 | trigger_event(352); stop |
| 4 | 352 | 35 / 2 | 8 | 3 | trigger_event(353); stop |
| 4 | 353 | 35 / 3 | 8 | 3 | set_switch(35); trigger_event(354); stop |
| 4 | 354 | 35 / 4 | 3 | 3 | trigger_event(355); stop |
| 4 | 355 | 35 / 5 | 2 | 3 | trigger_event(356); stop |
| 4 | 356 | 35 / 6 | 1 | 3 | construct_objects(room=35,group_or_wave=1); stop |
| 4 | 401 | 40 / 1 | 2 | 3 | trigger_event(402); stop |
| 4 | 402 | 40 / 2 | 8 | 3 | trigger_event(403); stop |
| 4 | 403 | 40 / 3 | 7 | 3 | trigger_event(404); stop |
| 4 | 404 | 40 / 4 | 7 | 3 | trigger_event(405); stop |
| 4 | 405 | 40 / 5 | 3 | 3 | trigger_event(406); stop |
| 4 | 406 | 40 / 6 | 3 | 3 | set_switch(41); stop |
| 4 | 161 | 16 / 1 | 4 | 3 | trigger_event(162); stop |
| 4 | 162 | 16 / 2 | 6 | 3 | trigger_event(163); stop |
| 4 | 163 | 16 / 3 | 4 | 3 | trigger_event(164); stop |
| 4 | 164 | 16 / 4 | 6 | 3 | set_switch(16); stop |
| 4 | 231 | 23 / 1 | 8 | 3 | trigger_event(232); stop |
| 4 | 232 | 23 / 2 | 8 | 3 | trigger_event(233); stop |
| 4 | 233 | 23 / 3 | 4 | 3 | set_switch(23); set_switch(15); stop |
| 4 | 151 | 15 / 1 | 5 | 3 | trigger_event(152); stop |
| 4 | 152 | 15 / 2 | 5 | 3 | trigger_event(153); set_switch(40); stop |
| 4 | 153 | 15 / 3 | 1 | 300 | stop |
| 5 | 201 | 20 / 1 | 5 | 3 | trigger_event(202); stop |
| 5 | 202 | 20 / 2 | 5 | 3 | trigger_event(203); stop |
| 5 | 203 | 20 / 3 | 1 | 150 | trigger_event(204); stop |
| 5 | 204 | 20 / 4 | 1 | 3 | set_switch(20); stop |
| 5 | 701 | 70 / 1 | 6 | 3 | trigger_event(702); stop |
| 5 | 702 | 70 / 2 | 6 | 3 | trigger_event(703); stop |
| 5 | 703 | 70 / 3 | 6 | 3 | trigger_event(704); stop |
| 5 | 704 | 70 / 4 | 3 | 3 | trigger_event(705); stop |
| 5 | 705 | 70 / 5 | 3 | 300 | trigger_event(706); stop |
| 5 | 706 | 70 / 6 | 3 | 3 | trigger_event(707); stop |
| 5 | 707 | 70 / 7 | 3 | 3 | set_switch(70); set_switch(71); stop |
| 5 | 501 | 50 / 1 | 8 | 3 | trigger_event(502); stop |
| 5 | 502 | 50 / 2 | 8 | 3 | trigger_event(503); stop |
| 5 | 503 | 50 / 3 | 7 | 3 | trigger_event(504); stop |
| 5 | 504 | 50 / 4 | 7 | 3 | set_switch(50); stop |
| 5 | 401 | 40 / 1 | 6 | 3 | trigger_event(402); stop |
| 5 | 402 | 40 / 2 | 6 | 3 | trigger_event(403); stop |
| 5 | 403 | 40 / 3 | 4 | 3 | trigger_event(404); stop |
| 5 | 404 | 40 / 4 | 4 | 300 | trigger_event(405); stop |
| 5 | 405 | 40 / 5 | 1 | 3 | trigger_event(406); stop |
| 5 | 406 | 40 / 6 | 1 | 3 | set_switch(40); stop |
| 5 | 511 | 51 / 1 | 8 | 3 | trigger_event(512); stop |
| 5 | 512 | 51 / 2 | 8 | 3 | trigger_event(513); stop |
| 5 | 513 | 51 / 3 | 8 | 3 | trigger_event(514); stop |
| 5 | 514 | 51 / 4 | 4 | 150 | trigger_event(515); stop |
| 5 | 515 | 51 / 5 | 2 | 3 | set_switch(51); stop |
| 5 | 601 | 60 / 1 | 4 | 3 | trigger_event(602); stop |
| 5 | 602 | 60 / 2 | 8 | 3 | trigger_event(603); stop |
| 5 | 603 | 60 / 3 | 1 | 3 | trigger_event(604); stop |
| 5 | 604 | 60 / 4 | 8 | 3 | trigger_event(605); stop |
| 5 | 605 | 60 / 5 | 4 | 300 | trigger_event(606); stop |
| 5 | 606 | 60 / 6 | 4 | 15 | trigger_event(607); stop |
| 5 | 607 | 60 / 7 | 5 | 3 | trigger_event(608); stop |
| 5 | 608 | 60 / 8 | 2 | 3 | trigger_event(609); stop |
| 5 | 609 | 60 / 9 | 6 | 3 | set_switch(60); stop |
| 6 | 2201 | 220 / 1 | 5 | 3 | trigger_event(222); stop |
| 6 | 222 | 220 / 2 | 1 | 3 | trigger_event(223); stop |
| 6 | 223 | 220 / 3 | 2 | 3 | trigger_event(224); stop |
| 6 | 224 | 220 / 4 | 2 | 3 | set_switch(220); stop |
| 6 | 531 | 53 / 1 | 5 | 3 | trigger_event(532); stop |
| 6 | 532 | 53 / 2 | 6 | 3 | trigger_event(533); stop |
| 6 | 533 | 53 / 3 | 1 | 3 | trigger_event(534); stop |
| 6 | 534 | 53 / 4 | 5 | 3 | trigger_event(535); stop |
| 6 | 535 | 53 / 5 | 8 | 3 | trigger_event(536); stop |
| 6 | 536 | 53 / 6 | 7 | 3 | set_switch(53); stop |
| 6 | 521 | 52 / 1 | 8 | 3 | trigger_event(522); stop |
| 6 | 522 | 52 / 2 | 9 | 3 | trigger_event(523); stop |
| 6 | 523 | 52 / 3 | 8 | 3 | trigger_event(524); stop |
| 6 | 524 | 52 / 4 | 1 | 3 | trigger_event(525); stop |
| 6 | 525 | 52 / 5 | 6 | 3 | set_switch(52); stop |
| 6 | 611 | 61 / 1 | 1 | 3 | trigger_event(612); stop |
| 6 | 612 | 61 / 2 | 8 | 3 | trigger_event(613); stop |
| 6 | 613 | 61 / 3 | 5 | 3 | trigger_event(614); stop |
| 6 | 614 | 61 / 4 | 5 | 300 | trigger_event(615); stop |
| 6 | 615 | 61 / 5 | 5 | 3 | trigger_event(616); stop |
| 6 | 616 | 61 / 6 | 9 | 3 | set_switch(62); stop |
| 6 | 411 | 41 / 1 | 5 | 3 | trigger_event(412); stop |
| 6 | 412 | 41 / 2 | 5 | 3 | trigger_event(413); stop |
| 6 | 413 | 41 / 3 | 5 | 3 | trigger_event(414); stop |
| 6 | 414 | 41 / 4 | 5 | 450 | trigger_event(415); stop |
| 6 | 415 | 41 / 5 | 5 | 3 | set_switch(41); stop |
| 7 | 2201 | 220 / 1 | 3 | 3 | trigger_event(222); stop |
| 7 | 222 | 220 / 2 | 2 | 3 | trigger_event(223); stop |
| 7 | 223 | 220 / 3 | 8 | 3 | trigger_event(224); stop |
| 7 | 224 | 220 / 4 | 2 | 3 | set_switch(220); stop |
| 7 | 531 | 53 / 1 | 1 | 3 | trigger_event(532); stop |
| 7 | 532 | 53 / 2 | 1 | 3 | trigger_event(533); stop |
| 7 | 533 | 53 / 3 | 2 | 3 | trigger_event(534); stop |
| 7 | 534 | 53 / 4 | 9 | 3 | trigger_event(535); stop |
| 7 | 535 | 53 / 5 | 9 | 3 | trigger_event(536); stop |
| 7 | 536 | 53 / 6 | 2 | 3 | trigger_event(537); stop |
| 7 | 537 | 53 / 7 | 2 | 3 | set_switch(8); stop |
| 7 | 538 | 53 / 8 | 5 | 3 | trigger_event(539); stop |
| 7 | 539 | 53 / 9 | 3 | 3 | set_switch(53); stop |
| 7 | 521 | 52 / 1 | 9 | 3 | trigger_event(522); stop |
| 7 | 522 | 52 / 2 | 1 | 3 | trigger_event(523); stop |
| 7 | 523 | 52 / 3 | 4 | 3 | trigger_event(524); stop |
| 7 | 524 | 52 / 4 | 4 | 3 | trigger_event(525); stop |
| 7 | 525 | 52 / 5 | 4 | 3 | trigger_event(526); stop |
| 7 | 526 | 52 / 6 | 2 | 3 | trigger_event(527); stop |
| 7 | 527 | 52 / 7 | 3 | 3 | set_switch(52); stop |
| 7 | 611 | 61 / 1 | 5 | 3 | trigger_event(612); stop |
| 7 | 612 | 61 / 2 | 8 | 3 | trigger_event(613); stop |
| 7 | 613 | 61 / 3 | 5 | 3 | trigger_event(614); stop |
| 7 | 614 | 61 / 4 | 6 | 300 | trigger_event(615); stop |
| 7 | 615 | 61 / 5 | 1 | 3 | trigger_event(616); stop |
| 7 | 616 | 61 / 6 | 9 | 3 | trigger_event(617); stop |
| 7 | 617 | 61 / 7 | 4 | 3 | trigger_event(618); stop |
| 7 | 618 | 61 / 8 | 4 | 600 | set_switch(61); stop |
| 8 | 421 | 42 / 1 | 7 | 3 | trigger_event(422); stop |
| 8 | 422 | 42 / 2 | 7 | 3 | trigger_event(423); stop |
| 8 | 423 | 42 / 3 | 6 | 3 | set_switch(42); stop |
| 8 | 651 | 65 / 1 | 6 | 3 | trigger_event(652); stop |
| 8 | 652 | 65 / 2 | 2 | 3 | trigger_event(653); stop |
| 8 | 653 | 65 / 3 | 4 | 3 | trigger_event(654); stop |
| 8 | 654 | 65 / 4 | 3 | 3 | set_switch(65); stop |
| 8 | 331 | 33 / 1 | 7 | 3 | trigger_event(332); stop |
| 8 | 332 | 33 / 2 | 7 | 3 | trigger_event(333); stop |
| 8 | 333 | 33 / 3 | 5 | 150 | trigger_event(334); stop |
| 8 | 334 | 33 / 4 | 6 | 3 | trigger_event(335); stop |
| 8 | 335 | 33 / 5 | 7 | 3 | set_switch(33); stop |
| 8 | 201 | 20 / 1 | 4 | 3 | trigger_event(202); stop |
| 8 | 202 | 20 / 2 | 4 | 3 | trigger_event(203); stop |
| 8 | 203 | 20 / 3 | 4 | 150 | trigger_event(204); stop |
| 8 | 204 | 20 / 4 | 9 | 3 | trigger_event(205); stop |
| 8 | 205 | 20 / 5 | 4 | 3 | set_switch(20); stop |
| 8 | 411 | 41 / 1 | 1 | 3 | trigger_event(412); stop |
| 8 | 412 | 41 / 2 | 8 | 3 | trigger_event(413); stop |
| 8 | 413 | 41 / 3 | 8 | 3 | trigger_event(414); stop |
| 8 | 414 | 41 / 4 | 10 | 3 | trigger_event(415); stop |
| 8 | 415 | 41 / 5 | 4 | 300 | trigger_event(416); stop |
| 8 | 416 | 41 / 6 | 2 | 3 | trigger_event(417); stop |
| 8 | 417 | 41 / 7 | 3 | 3 | set_switch(41); stop |
| 8 | 211 | 21 / 1 | 7 | 3 | trigger_event(212); stop |
| 8 | 212 | 21 / 2 | 9 | 3 | trigger_event(213); stop |
| 8 | 213 | 21 / 3 | 5 | 3 | trigger_event(214); stop |
| 8 | 214 | 21 / 4 | 4 | 150 | trigger_event(215); stop |
| 8 | 215 | 21 / 5 | 5 | 3 | set_switch(21); set_switch(41); stop |
| 8 | 221 | 22 / 1 | 8 | 3 | trigger_event(222); stop |
| 8 | 222 | 22 / 2 | 7 | 3 | trigger_event(223); stop |
| 8 | 223 | 22 / 3 | 6 | 3 | trigger_event(224); stop |
| 8 | 224 | 22 / 4 | 9 | 150 | trigger_event(225); stop |
| 8 | 225 | 22 / 5 | 1 | 3 | set_switch(22); set_switch(65); set_switch(21); stop |
| 8 | 311 | 31 / 1 | 9 | 3 | trigger_event(312); stop |
| 8 | 312 | 31 / 2 | 2 | 3 | trigger_event(313); stop |
| 8 | 313 | 31 / 3 | 8 | 3 | trigger_event(314); stop |
| 8 | 314 | 31 / 4 | 8 | 3 | trigger_event(315); stop |
| 8 | 315 | 31 / 5 | 4 | 300 | trigger_event(316); stop |
| 8 | 316 | 31 / 6 | 9 | 3 | trigger_event(317); stop |
| 8 | 317 | 31 / 7 | 1 | 3 | set_switch(31); stop |
| 9 | 401 | 40 / 1 | 8 | 3 | trigger_event(402); stop |
| 9 | 402 | 40 / 2 | 8 | 3 | trigger_event(403); stop |
| 9 | 403 | 40 / 3 | 7 | 3 | trigger_event(404); stop |
| 9 | 404 | 40 / 4 | 3 | 3 | set_switch(40); stop |
| 9 | 231 | 23 / 1 | 4 | 3 | trigger_event(232); stop |
| 9 | 232 | 23 / 2 | 6 | 3 | trigger_event(233); stop |
| 9 | 233 | 23 / 3 | 8 | 3 | trigger_event(234); stop |
| 9 | 234 | 23 / 4 | 2 | 3 | set_switch(23); stop |
| 9 | 501 | 50 / 1 | 8 | 3 | trigger_event(502); stop |
| 9 | 502 | 50 / 2 | 6 | 3 | trigger_event(503); stop |
| 9 | 503 | 50 / 3 | 3 | 3 | trigger_event(504); stop |
| 9 | 504 | 50 / 4 | 5 | 3 | trigger_event(505); stop |
| 9 | 505 | 50 / 5 | 3 | 3 | set_switch(50); stop |
| 9 | 701 | 70 / 1 | 8 | 3 | trigger_event(702); stop |
| 9 | 702 | 70 / 2 | 8 | 3 | trigger_event(703); stop |
| 9 | 703 | 70 / 3 | 2 | 3 | trigger_event(704); stop |
| 9 | 704 | 70 / 4 | 2 | 3 | set_switch(70); stop |
| 9 | 705 | 70 / 5 | 4 | 3 | trigger_event(706); stop |
| 9 | 706 | 70 / 6 | 6 | 3 | set_switch(70); stop |
| 9 | 551 | 55 / 1 | 2 | 3 | trigger_event(552); stop |
| 9 | 552 | 55 / 2 | 7 | 3 | trigger_event(553); stop |
| 9 | 553 | 55 / 3 | 8 | 3 | trigger_event(554); stop |
| 9 | 554 | 55 / 4 | 3 | 3 | trigger_event(555); stop |
| 9 | 555 | 55 / 5 | 1 | 300 | set_switch(55); stop |
| 9 | 301 | 30 / 1 | 6 | 3 | trigger_event(302); stop |
| 9 | 302 | 30 / 2 | 9 | 3 | trigger_event(303); stop |
| 9 | 303 | 30 / 3 | 6 | 3 | trigger_event(304); stop |
| 9 | 304 | 30 / 4 | 3 | 300 | trigger_event(305); stop |
| 9 | 305 | 30 / 5 | 3 | 3 | stop |
| 9 | 321 | 32 / 1 | 8 | 3 | trigger_event(322); stop |
| 9 | 322 | 32 / 2 | 7 | 3 | trigger_event(323); stop |
| 9 | 323 | 32 / 3 | 3 | 3 | trigger_event(324); stop |
| 9 | 324 | 32 / 4 | 7 | 3 | trigger_event(325); stop |
| 9 | 325 | 32 / 5 | 5 | 3 | trigger_event(326); stop |
| 9 | 326 | 32 / 6 | 5 | 3 | trigger_event(327); stop |
| 9 | 327 | 32 / 7 | 6 | 3 | set_switch(32); stop |
| 10 | 431 | 43 / 1 | 4 | 3 | trigger_event(432); stop |
| 10 | 432 | 43 / 2 | 8 | 3 | trigger_event(433); stop |
| 10 | 433 | 43 / 3 | 8 | 3 | trigger_event(434); stop |
| 10 | 434 | 43 / 4 | 3 | 3 | trigger_event(435); stop |
| 10 | 435 | 43 / 5 | 2 | 3 | set_switch(43); stop |
| 10 | 801 | 80 / 1 | 3 | 3 | trigger_event(802); stop |
| 10 | 802 | 80 / 2 | 6 | 3 | trigger_event(803); stop |
| 10 | 803 | 80 / 3 | 7 | 3 | trigger_event(804); stop |
| 10 | 804 | 80 / 4 | 8 | 3 | trigger_event(805); stop |
| 10 | 805 | 80 / 5 | 6 | 3 | set_switch(3); stop |
| 10 | 806 | 80 / 6 | 7 | 3 | trigger_event(807); stop |
| 10 | 807 | 80 / 7 | 5 | 3 | trigger_event(808); stop |
| 10 | 808 | 80 / 8 | 8 | 3 | trigger_event(809); stop |
| 10 | 809 | 80 / 9 | 3 | 3 | trigger_event(810); stop |
| 10 | 810 | 80 / 10 | 8 | 3 | trigger_event(811); stop |
| 10 | 811 | 80 / 11 | 9 | 3 | set_switch(2); stop |
| 10 | 812 | 80 / 12 | 3 | 3 | trigger_event(813); stop |
| 10 | 813 | 80 / 13 | 6 | 3 | trigger_event(814); stop |
| 10 | 814 | 80 / 14 | 6 | 3 | trigger_event(815); stop |
| 10 | 815 | 80 / 15 | 4 | 3 | set_switch(80); stop |
| 14 | 1 | 0 / 1 | 1 | 50 | construct_objects(room=0,group_or_wave=1); construct_objects(room=1,group_or_wave=1); construct_objects(room=2,group_or_wave=1); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.
