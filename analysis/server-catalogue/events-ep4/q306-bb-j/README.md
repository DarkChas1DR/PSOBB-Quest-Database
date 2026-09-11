# LOGiN presents 勇場のマッチレース — events-ep4/q306-bb-j

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/events-ep4/q306-bb-j.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/events-ep4/q306-bb-j.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/events-ep4/q306-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode4; header quest ID 306; language J. Static scan: **724 objects, 663 enemy/NPC records, 256 events, 507 script labels.** Script roundtrip: byte-identical.

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
0x01, 0x24, 0x00, 0x00, 0x00
0x02, 0x25, 0x00, 0x00, 0x00
0x06, 0x29, 0x00, 0x02, 0x00
0x07, 0x2A, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 18 | 0 |
| 1 | 222 | 147 | 50 |
| 2 | 171 | 148 | 46 |
| 6 | 151 | 166 | 50 |
| 7 | 154 | 184 | 110 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 101 | 10 / 1 | 3 | 30 | trigger_event(102); stop |
| 1 | 102 | 10 / 2 | 3 | 3 | trigger_event(103); stop |
| 1 | 103 | 10 / 3 | 3 | 3 | set_switch(10); stop |
| 1 | 104 | 10 / 4 | 4 | 30 | trigger_event(105); stop |
| 1 | 105 | 10 / 5 | 4 | 3 | stop |
| 1 | 501 | 50 / 1 | 2 | 30 | trigger_event(502); stop |
| 1 | 502 | 50 / 2 | 1 | 3 | set_switch(50); trigger_event(503); stop |
| 1 | 503 | 50 / 3 | 3 | 3 | set_switch(51); trigger_event(504); stop |
| 1 | 504 | 50 / 4 | 3 | 3 | set_switch(52); stop |
| 1 | 601 | 60 / 1 | 3 | 30 | set_switch(60); trigger_event(602); stop |
| 1 | 602 | 60 / 2 | 3 | 300 | trigger_event(603); stop |
| 1 | 603 | 60 / 3 | 1 | 3 | set_switch(61); stop |
| 1 | 111 | 11 / 1 | 2 | 30 | trigger_event(112); stop |
| 1 | 112 | 11 / 2 | 2 | 3 | trigger_event(113); stop |
| 1 | 113 | 11 / 3 | 2 | 3 | set_switch(11); stop |
| 1 | 114 | 11 / 4 | 3 | 300 | trigger_event(115); stop |
| 1 | 115 | 11 / 5 | 3 | 3 | stop |
| 1 | 401 | 40 / 1 | 3 | 30 | trigger_event(402); stop |
| 1 | 402 | 40 / 2 | 3 | 3 | stop |
| 1 | 2101 | 21 / 1 | 4 | 30 | trigger_event(2102); stop |
| 1 | 2102 | 21 / 2 | 4 | 3 | set_switch(21); trigger_event(2103); stop |
| 1 | 2103 | 21 / 3 | 3 | 300 | trigger_event(2104); stop |
| 1 | 2104 | 21 / 4 | 4 | 3 | set_switch(22); trigger_event(2105); stop |
| 1 | 2105 | 21 / 5 | 3 | 3 | trigger_event(2106); stop |
| 1 | 2106 | 21 / 6 | 3 | 3 | trigger_event(2107); stop |
| 1 | 2107 | 21 / 7 | 4 | 3 | set_switch(23); stop |
| 1 | 801 | 80 / 1 | 3 | 30 | trigger_event(802); stop |
| 1 | 802 | 80 / 2 | 3 | 3 | stop |
| 1 | 2001 | 20 / 1 | 3 | 3 | trigger_event(2002); stop |
| 1 | 2002 | 20 / 2 | 3 | 3 | trigger_event(2003); stop |
| 1 | 2003 | 20 / 3 | 3 | 3 | trigger_event(2004); stop |
| 1 | 2004 | 20 / 4 | 3 | 3 | set_switch(20); trigger_event(2005); stop |
| 1 | 2005 | 20 / 5 | 4 | 3 | trigger_event(2006); stop |
| 1 | 2006 | 20 / 6 | 4 | 3 | trigger_event(2007); stop |
| 1 | 2007 | 20 / 7 | 1 | 3 | trigger_event(2008); stop |
| 1 | 2008 | 20 / 8 | 2 | 3 | trigger_event(2009); stop |
| 1 | 2009 | 20 / 9 | 2 | 3 | set_switch(24); trigger_event(2010); stop |
| 1 | 2010 | 20 / 10 | 3 | 3 | trigger_event(2011); stop |
| 1 | 2011 | 20 / 11 | 3 | 3 | set_switch(25); trigger_event(2012); stop |
| 1 | 2012 | 20 / 12 | 4 | 300 | trigger_event(2013); stop |
| 1 | 2013 | 20 / 13 | 2 | 3 | set_switch(26); stop |
| 1 | 301 | 30 / 1 | 2 | 30 | trigger_event(302); stop |
| 1 | 302 | 30 / 2 | 2 | 3 | set_switch(30); trigger_event(303); stop |
| 1 | 303 | 30 / 3 | 3 | 3 | trigger_event(304); stop |
| 1 | 304 | 30 / 4 | 4 | 3 | trigger_event(306); stop |
| 1 | 305 | 30 / 5 | 2 | 300 | stop |
| 1 | 306 | 30 / 6 | 5 | 3 | set_switch(31); stop |
| 1 | 307 | 30 / 7 | 4 | 3 | trigger_event(308); stop |
| 1 | 308 | 30 / 8 | 3 | 3 | trigger_event(309); stop |
| 1 | 309 | 30 / 9 | 3 | 3 | stop |
| 2 | 111 | 11 / 1 | 3 | 30 | trigger_event(112); stop |
| 2 | 112 | 11 / 2 | 3 | 3 | trigger_event(113); stop |
| 2 | 113 | 11 / 3 | 3 | 3 | stop |
| 2 | 114 | 11 / 4 | 4 | 30 | trigger_event(115); stop |
| 2 | 115 | 11 / 5 | 4 | 3 | set_switch(11); stop |
| 2 | 501 | 50 / 1 | 2 | 30 | trigger_event(502); stop |
| 2 | 502 | 50 / 2 | 1 | 3 | set_switch(50); trigger_event(503); stop |
| 2 | 503 | 50 / 3 | 3 | 3 | set_switch(51); trigger_event(504); stop |
| 2 | 504 | 50 / 4 | 3 | 3 | set_switch(52); stop |
| 2 | 801 | 80 / 1 | 3 | 30 | set_switch(80); trigger_event(802); stop |
| 2 | 802 | 80 / 2 | 3 | 300 | trigger_event(803); stop |
| 2 | 803 | 80 / 3 | 1 | 3 | set_switch(81); stop |
| 2 | 101 | 10 / 1 | 2 | 30 | trigger_event(102); stop |
| 2 | 102 | 10 / 2 | 2 | 3 | trigger_event(103); stop |
| 2 | 103 | 10 / 3 | 2 | 3 | set_switch(10); stop |
| 2 | 104 | 10 / 4 | 3 | 300 | trigger_event(105); stop |
| 2 | 105 | 10 / 5 | 3 | 3 | stop |
| 2 | 401 | 40 / 1 | 3 | 30 | trigger_event(402); stop |
| 2 | 402 | 40 / 2 | 3 | 3 | stop |
| 2 | 201 | 20 / 1 | 4 | 30 | trigger_event(202); stop |
| 2 | 202 | 20 / 2 | 4 | 3 | set_switch(20); trigger_event(203); stop |
| 2 | 203 | 20 / 3 | 3 | 300 | trigger_event(204); stop |
| 2 | 204 | 20 / 4 | 4 | 3 | set_switch(21); trigger_event(205); stop |
| 2 | 205 | 20 / 5 | 3 | 3 | trigger_event(206); stop |
| 2 | 206 | 20 / 6 | 3 | 3 | trigger_event(207); stop |
| 2 | 207 | 20 / 7 | 4 | 3 | set_switch(22); stop |
| 2 | 411 | 41 / 1 | 3 | 30 | trigger_event(412); stop |
| 2 | 412 | 41 / 2 | 3 | 3 | stop |
| 2 | 601 | 60 / 1 | 5 | 30 | trigger_event(602); stop |
| 2 | 602 | 60 / 2 | 5 | 150 | trigger_event(603); stop |
| 2 | 603 | 60 / 3 | 6 | 150 | trigger_event(604); stop |
| 2 | 604 | 60 / 4 | 3 | 150 | trigger_event(605); stop |
| 2 | 605 | 60 / 5 | 5 | 150 | set_switch(60); trigger_event(606); stop |
| 2 | 606 | 60 / 6 | 4 | 300 | trigger_event(607); stop |
| 2 | 607 | 60 / 7 | 4 | 3 | trigger_event(608); stop |
| 2 | 608 | 60 / 8 | 4 | 3 | trigger_event(609); stop |
| 2 | 609 | 60 / 9 | 2 | 3 | set_switch(61); stop |
| 2 | 301 | 30 / 1 | 2 | 30 | trigger_event(302); stop |
| 2 | 302 | 30 / 2 | 2 | 3 | set_switch(30); trigger_event(303); stop |
| 2 | 303 | 30 / 3 | 3 | 3 | trigger_event(304); stop |
| 2 | 304 | 30 / 4 | 4 | 3 | trigger_event(306); stop |
| 2 | 305 | 30 / 5 | 2 | 300 | stop |
| 2 | 306 | 30 / 6 | 5 | 3 | set_switch(31); stop |
| 2 | 307 | 30 / 7 | 4 | 3 | trigger_event(308); stop |
| 2 | 308 | 30 / 8 | 3 | 3 | trigger_event(309); stop |
| 2 | 309 | 30 / 9 | 3 | 3 | stop |
| 6 | 120 | 64 / 1 | 3 | 30 | trigger_event(641); stop |
| 6 | 641 | 64 / 2 | 3 | 90 | trigger_event(642); stop |
| 6 | 642 | 64 / 3 | 2 | 90 | set_switch(64); stop |
| 6 | 90 | 90 / 1 | 3 | 30 | trigger_event(901); stop |
| 6 | 901 | 90 / 2 | 4 | 3 | trigger_event(902); stop |
| 6 | 902 | 90 / 3 | 6 | 3 | set_switch(98); stop |
| 6 | 62 | 62 / 1 | 2 | 30 | trigger_event(621); stop |
| 6 | 621 | 62 / 2 | 3 | 3 | set_switch(62); stop |
| 6 | 622 | 62 / 3 | 4 | 300 | stop |
| 6 | 70 | 70 / 1 | 3 | 30 | trigger_event(702); stop |
| 6 | 702 | 70 / 2 | 3 | 90 | trigger_event(703); stop |
| 6 | 703 | 70 / 3 | 2 | 90 | set_switch(70); stop |
| 6 | 704 | 70 / 4 | 3 | 3 | trigger_event(705); stop |
| 6 | 705 | 70 / 5 | 2 | 3 | trigger_event(706); stop |
| 6 | 706 | 70 / 6 | 1 | 3 | stop |
| 6 | 20 | 20 / 1 | 4 | 30 | trigger_event(201); stop |
| 6 | 201 | 20 / 2 | 4 | 3 | set_switch(20); stop |
| 6 | 202 | 20 / 3 | 4 | 30 | trigger_event(203); stop |
| 6 | 203 | 20 / 4 | 3 | 3 | stop |
| 6 | 50 | 50 / 1 | 4 | 30 | trigger_event(502); stop |
| 6 | 502 | 50 / 2 | 4 | 90 | set_switch(51); stop |
| 6 | 503 | 50 / 3 | 4 | 3 | trigger_event(504); stop |
| 6 | 504 | 50 / 4 | 4 | 3 | stop |
| 6 | 100 | 100 / 1 | 4 | 30 | trigger_event(1001); stop |
| 6 | 1001 | 100 / 2 | 4 | 3 | stop |
| 6 | 110 | 110 / 1 | 3 | 30 | trigger_event(1102); stop |
| 6 | 1102 | 110 / 2 | 3 | 90 | trigger_event(1103); stop |
| 6 | 1103 | 110 / 3 | 2 | 90 | set_switch(110); stop |
| 6 | 1104 | 110 / 4 | 3 | 3 | trigger_event(1105); stop |
| 6 | 1105 | 110 / 5 | 2 | 3 | trigger_event(1106); stop |
| 6 | 1106 | 110 / 6 | 1 | 3 | stop |
| 6 | 91 | 90 / 4 | 3 | 30 | trigger_event(905); stop |
| 6 | 905 | 90 / 5 | 4 | 3 | trigger_event(906); stop |
| 6 | 906 | 90 / 6 | 6 | 3 | set_switch(99); stop |
| 6 | 61 | 61 / 1 | 2 | 30 | trigger_event(612); stop |
| 6 | 612 | 61 / 2 | 3 | 3 | set_switch(61); stop |
| 6 | 613 | 61 / 3 | 4 | 300 | stop |
| 6 | 30 | 30 / 1 | 3 | 30 | trigger_event(302); stop |
| 6 | 302 | 30 / 2 | 3 | 90 | trigger_event(303); stop |
| 6 | 303 | 30 / 3 | 2 | 90 | set_switch(30); stop |
| 6 | 51 | 50 / 5 | 4 | 30 | trigger_event(506); stop |
| 6 | 506 | 50 / 6 | 4 | 3 | set_switch(50); stop |
| 6 | 507 | 50 / 7 | 4 | 30 | trigger_event(508); stop |
| 6 | 508 | 50 / 8 | 3 | 3 | stop |
| 6 | 21 | 20 / 5 | 4 | 30 | trigger_event(206); stop |
| 6 | 206 | 20 / 6 | 4 | 90 | set_switch(21); stop |
| 6 | 207 | 20 / 7 | 4 | 3 | trigger_event(208); stop |
| 6 | 208 | 20 / 8 | 4 | 3 | stop |
| 6 | 101 | 100 / 3 | 4 | 30 | trigger_event(1004); stop |
| 6 | 1004 | 100 / 4 | 4 | 3 | stop |
| 7 | 251 | 25 / 99 | 0 | 3 | trigger_event(2511); trigger_event(252); trigger_event(253); stop |
| 7 | 2511 | 25 / 1 | 3 | 30 | trigger_event(254); stop |
| 7 | 252 | 25 / 2 | 2 | 30 | trigger_event(255); stop |
| 7 | 253 | 25 / 3 | 1 | 30 | trigger_event(256); stop |
| 7 | 254 | 25 / 4 | 3 | 3 | trigger_event(257); stop |
| 7 | 255 | 25 / 5 | 2 | 3 | stop |
| 7 | 256 | 25 / 6 | 1 | 3 | stop |
| 7 | 257 | 25 / 7 | 3 | 3 | set_switch(158); stop |
| 7 | 501 | 50 / 99 | 0 | 3 | trigger_event(5011); trigger_event(504); stop |
| 7 | 5011 | 50 / 1 | 3 | 30 | trigger_event(502); stop |
| 7 | 502 | 50 / 2 | 4 | 3 | trigger_event(503); stop |
| 7 | 503 | 50 / 3 | 4 | 3 | stop |
| 7 | 504 | 50 / 4 | 3 | 300 | trigger_event(505); stop |
| 7 | 505 | 50 / 5 | 4 | 3 | set_switch(160); stop |
| 7 | 411 | 41 / 1 | 3 | 30 | trigger_event(412); stop |
| 7 | 412 | 41 / 2 | 3 | 3 | trigger_event(413); stop |
| 7 | 413 | 41 / 3 | 3 | 3 | set_switch(172); trigger_event(414); stop |
| 7 | 414 | 41 / 4 | 3 | 300 | trigger_event(415); stop |
| 7 | 415 | 41 / 5 | 3 | 3 | set_switch(171); stop |
| 7 | 261 | 26 / 1 | 1 | 30 | trigger_event(264); stop |
| 7 | 262 | 26 / 2 | 2 | 3 | trigger_event(265); stop |
| 7 | 263 | 26 / 3 | 2 | 3 | trigger_event(266); stop |
| 7 | 264 | 26 / 4 | 2 | 150 | trigger_event(267); stop |
| 7 | 265 | 26 / 5 | 2 | 3 | trigger_event(268); stop |
| 7 | 266 | 26 / 6 | 2 | 3 | trigger_event(269); stop |
| 7 | 267 | 26 / 7 | 2 | 150 | set_switch(161); stop |
| 7 | 268 | 26 / 8 | 2 | 3 | stop |
| 7 | 269 | 26 / 9 | 2 | 3 | stop |
| 7 | 271 | 27 / 1 | 1 | 30 | trigger_event(272); stop |
| 7 | 272 | 27 / 2 | 1 | 300 | trigger_event(273); stop |
| 7 | 273 | 27 / 3 | 1 | 300 | set_switch(162); stop |
| 7 | 2704 | 27 / 4 | 1 | 3 | trigger_event(275); stop |
| 7 | 275 | 27 / 5 | 1 | 150 | trigger_event(276); stop |
| 7 | 276 | 27 / 6 | 1 | 150 | stop |
| 7 | 2707 | 27 / 7 | 1 | 3 | trigger_event(278); stop |
| 7 | 278 | 27 / 8 | 1 | 90 | trigger_event(279); stop |
| 7 | 279 | 27 / 9 | 1 | 90 | trigger_event(2710); stop |
| 7 | 2710 | 27 / 10 | 1 | 90 | stop |
| 7 | 2711 | 27 / 11 | 1 | 3 | trigger_event(2712); stop |
| 7 | 2712 | 27 / 12 | 1 | 300 | stop |
| 7 | 2713 | 27 / 13 | 1 | 3 | trigger_event(2714); stop |
| 7 | 2714 | 27 / 14 | 1 | 90 | trigger_event(2715); stop |
| 7 | 2715 | 27 / 15 | 1 | 90 | trigger_event(2716); stop |
| 7 | 2716 | 27 / 16 | 1 | 90 | stop |
| 7 | 2717 | 27 / 17 | 1 | 3 | trigger_event(2718); stop |
| 7 | 2718 | 27 / 18 | 1 | 60 | trigger_event(2719); stop |
| 7 | 2719 | 27 / 19 | 1 | 60 | stop |
| 7 | 2720 | 27 / 20 | 1 | 3 | trigger_event(2721); stop |
| 7 | 2721 | 27 / 21 | 1 | 60 | trigger_event(2722); stop |
| 7 | 2722 | 27 / 22 | 1 | 60 | trigger_event(2723); stop |
| 7 | 2723 | 27 / 23 | 1 | 60 | stop |
| 7 | 2727 | 27 / 24 | 1 | 3 | trigger_event(2728); stop |
| 7 | 2728 | 27 / 25 | 1 | 3 | trigger_event(2729); stop |
| 7 | 2729 | 27 / 26 | 1 | 3 | trigger_event(2730); stop |
| 7 | 2730 | 27 / 27 | 1 | 3 | stop |
| 7 | 201 | 20 / 99 | 0 | 3 | trigger_event(2011); trigger_event(202); trigger_event(203); stop |
| 7 | 2011 | 20 / 1 | 3 | 30 | trigger_event(204); stop |
| 7 | 202 | 20 / 2 | 2 | 30 | trigger_event(205); stop |
| 7 | 203 | 20 / 3 | 1 | 30 | trigger_event(206); stop |
| 7 | 204 | 20 / 4 | 3 | 3 | trigger_event(207); stop |
| 7 | 205 | 20 / 5 | 2 | 3 | stop |
| 7 | 206 | 20 / 6 | 1 | 3 | stop |
| 7 | 207 | 20 / 7 | 3 | 3 | set_switch(155); stop |
| 7 | 401 | 40 / 99 | 0 | 3 | trigger_event(4011); trigger_event(404); stop |
| 7 | 4011 | 40 / 1 | 3 | 30 | trigger_event(402); stop |
| 7 | 402 | 40 / 2 | 4 | 3 | trigger_event(403); stop |
| 7 | 403 | 40 / 3 | 4 | 3 | stop |
| 7 | 404 | 40 / 4 | 3 | 300 | trigger_event(405); stop |
| 7 | 405 | 40 / 5 | 4 | 3 | set_switch(154); stop |
| 7 | 211 | 21 / 1 | 3 | 30 | trigger_event(212); stop |
| 7 | 212 | 21 / 2 | 3 | 3 | trigger_event(213); stop |
| 7 | 213 | 21 / 3 | 3 | 3 | set_switch(168); trigger_event(214); stop |
| 7 | 214 | 21 / 4 | 3 | 300 | trigger_event(215); stop |
| 7 | 215 | 21 / 5 | 3 | 3 | set_switch(169); stop |
| 7 | 221 | 22 / 1 | 1 | 30 | trigger_event(224); stop |
| 7 | 222 | 22 / 2 | 2 | 3 | trigger_event(225); stop |
| 7 | 223 | 22 / 3 | 2 | 3 | trigger_event(226); stop |
| 7 | 224 | 22 / 4 | 2 | 150 | trigger_event(227); stop |
| 7 | 225 | 22 / 5 | 2 | 3 | trigger_event(228); stop |
| 7 | 226 | 22 / 6 | 2 | 3 | trigger_event(229); stop |
| 7 | 227 | 22 / 7 | 2 | 150 | set_switch(167); stop |
| 7 | 228 | 22 / 8 | 2 | 3 | stop |
| 7 | 229 | 22 / 9 | 2 | 3 | stop |
| 7 | 231 | 23 / 1 | 1 | 30 | trigger_event(232); stop |
| 7 | 232 | 23 / 2 | 1 | 300 | trigger_event(233); stop |
| 7 | 233 | 23 / 3 | 1 | 300 | set_switch(166); stop |
| 7 | 2304 | 23 / 4 | 1 | 3 | trigger_event(235); stop |
| 7 | 235 | 23 / 5 | 1 | 150 | trigger_event(236); stop |
| 7 | 236 | 23 / 6 | 1 | 150 | stop |
| 7 | 2307 | 23 / 7 | 1 | 3 | trigger_event(238); stop |
| 7 | 238 | 23 / 8 | 1 | 90 | trigger_event(239); stop |
| 7 | 239 | 23 / 9 | 1 | 90 | trigger_event(2310); stop |
| 7 | 2310 | 23 / 10 | 1 | 90 | stop |
| 7 | 2311 | 23 / 11 | 1 | 3 | trigger_event(2312); stop |
| 7 | 2312 | 23 / 12 | 1 | 300 | stop |
| 7 | 2313 | 23 / 13 | 1 | 3 | trigger_event(2314); stop |
| 7 | 2314 | 23 / 14 | 1 | 90 | trigger_event(2315); stop |
| 7 | 2315 | 23 / 15 | 1 | 90 | trigger_event(2316); stop |
| 7 | 2316 | 23 / 16 | 1 | 90 | stop |
| 7 | 2317 | 23 / 17 | 1 | 3 | trigger_event(2318); stop |
| 7 | 2318 | 23 / 18 | 1 | 60 | trigger_event(2319); stop |
| 7 | 2319 | 23 / 19 | 1 | 60 | stop |
| 7 | 2320 | 23 / 20 | 1 | 3 | trigger_event(2321); stop |
| 7 | 2321 | 23 / 21 | 1 | 60 | trigger_event(2322); stop |
| 7 | 2322 | 23 / 22 | 1 | 60 | trigger_event(2323); stop |
| 7 | 2323 | 23 / 23 | 1 | 60 | stop |
| 7 | 2327 | 23 / 24 | 1 | 3 | trigger_event(2328); stop |
| 7 | 2328 | 23 / 25 | 1 | 3 | trigger_event(2329); stop |
| 7 | 2329 | 23 / 26 | 1 | 3 | trigger_event(2330); stop |
| 7 | 2330 | 23 / 27 | 1 | 3 | stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

A backup is present; decompressed content identical: True. See [text differences](<backup-diff.txt>).

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
