# 思戦の彼方 — vr-ep4/q313-bb-j

Episode4; header quest ID 313; language J. Static scan: **95 objects, 836 enemy/NPC records, 150 events, 156 script labels.** Script roundtrip: byte-identical.

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
0x05, 0x28, 0x00, 0x00, 0x00
0x06, 0x29, 0x00, 0x00, 0x00
0x07, 0x2A, 0x00, 0x00, 0x00
0x08, 0x2B, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 30 | 16 | 0 |
| 1 | 7 | 150 | 30 |
| 5 | 17 | 180 | 30 |
| 6 | 10 | 150 | 30 |
| 7 | 22 | 180 | 30 |
| 8 | 9 | 160 | 30 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 1 | 201 | 20 / 1 | 3 | 0 | trigger_event(202); stop |
| 1 | 202 | 20 / 2 | 3 | 0 | trigger_event(203); stop |
| 1 | 203 | 20 / 3 | 3 | 0 | trigger_event(204); stop |
| 1 | 204 | 20 / 4 | 3 | 0 | trigger_event(205); stop |
| 1 | 205 | 20 / 5 | 3 | 0 | trigger_event(206); stop |
| 1 | 206 | 20 / 6 | 4 | 0 | trigger_event(207); stop |
| 1 | 207 | 20 / 7 | 4 | 0 | trigger_event(208); stop |
| 1 | 208 | 20 / 8 | 4 | 0 | trigger_event(209); stop |
| 1 | 209 | 20 / 9 | 4 | 0 | trigger_event(210); stop |
| 1 | 210 | 20 / 10 | 4 | 0 | trigger_event(211); stop |
| 1 | 211 | 20 / 11 | 5 | 0 | trigger_event(212); stop |
| 1 | 212 | 20 / 12 | 5 | 0 | trigger_event(213); stop |
| 1 | 213 | 20 / 13 | 5 | 0 | trigger_event(214); stop |
| 1 | 214 | 20 / 14 | 5 | 0 | trigger_event(215); stop |
| 1 | 215 | 20 / 15 | 5 | 0 | trigger_event(216); stop |
| 1 | 216 | 20 / 16 | 5 | 0 | trigger_event(217); stop |
| 1 | 217 | 20 / 17 | 5 | 0 | trigger_event(218); stop |
| 1 | 218 | 20 / 18 | 5 | 0 | trigger_event(219); stop |
| 1 | 219 | 20 / 19 | 5 | 0 | trigger_event(220); stop |
| 1 | 220 | 20 / 20 | 5 | 0 | trigger_event(221); stop |
| 1 | 221 | 20 / 21 | 6 | 0 | trigger_event(222); stop |
| 1 | 222 | 20 / 22 | 6 | 0 | trigger_event(223); stop |
| 1 | 223 | 20 / 23 | 6 | 0 | trigger_event(224); stop |
| 1 | 224 | 20 / 24 | 6 | 0 | trigger_event(225); stop |
| 1 | 225 | 20 / 25 | 6 | 0 | trigger_event(226); stop |
| 1 | 226 | 20 / 26 | 7 | 0 | trigger_event(227); stop |
| 1 | 227 | 20 / 27 | 7 | 0 | trigger_event(228); stop |
| 1 | 228 | 20 / 28 | 7 | 0 | trigger_event(229); stop |
| 1 | 229 | 20 / 29 | 7 | 0 | trigger_event(230); stop |
| 1 | 230 | 20 / 30 | 7 | 0 | set_switch(20); stop |
| 5 | 601 | 60 / 1 | 5 | 0 | trigger_event(602); stop |
| 5 | 602 | 60 / 2 | 5 | 0 | trigger_event(603); stop |
| 5 | 603 | 60 / 3 | 5 | 0 | trigger_event(604); stop |
| 5 | 604 | 60 / 4 | 5 | 0 | trigger_event(605); stop |
| 5 | 605 | 60 / 5 | 5 | 0 | trigger_event(606); stop |
| 5 | 606 | 60 / 6 | 5 | 0 | trigger_event(607); stop |
| 5 | 607 | 60 / 7 | 5 | 0 | trigger_event(608); stop |
| 5 | 608 | 60 / 8 | 5 | 0 | trigger_event(609); stop |
| 5 | 609 | 60 / 9 | 5 | 0 | trigger_event(610); stop |
| 5 | 610 | 60 / 10 | 5 | 0 | trigger_event(611); stop |
| 5 | 611 | 60 / 11 | 6 | 0 | trigger_event(612); stop |
| 5 | 612 | 60 / 12 | 6 | 0 | trigger_event(613); stop |
| 5 | 613 | 60 / 13 | 6 | 0 | trigger_event(614); stop |
| 5 | 614 | 60 / 14 | 6 | 0 | trigger_event(615); stop |
| 5 | 615 | 60 / 15 | 6 | 0 | trigger_event(616); stop |
| 5 | 616 | 60 / 16 | 6 | 0 | trigger_event(617); stop |
| 5 | 617 | 60 / 17 | 6 | 0 | trigger_event(618); stop |
| 5 | 618 | 60 / 18 | 6 | 0 | trigger_event(619); stop |
| 5 | 619 | 60 / 19 | 6 | 0 | trigger_event(620); stop |
| 5 | 620 | 60 / 20 | 6 | 0 | trigger_event(621); stop |
| 5 | 621 | 60 / 21 | 7 | 0 | trigger_event(622); stop |
| 5 | 622 | 60 / 22 | 7 | 0 | trigger_event(623); stop |
| 5 | 623 | 60 / 23 | 7 | 0 | trigger_event(624); stop |
| 5 | 624 | 60 / 24 | 7 | 0 | trigger_event(625); stop |
| 5 | 625 | 60 / 25 | 7 | 0 | trigger_event(626); stop |
| 5 | 626 | 60 / 26 | 7 | 0 | trigger_event(627); stop |
| 5 | 627 | 60 / 27 | 7 | 0 | trigger_event(628); stop |
| 5 | 628 | 60 / 28 | 7 | 0 | trigger_event(629); stop |
| 5 | 629 | 60 / 29 | 7 | 0 | trigger_event(630); stop |
| 5 | 630 | 60 / 30 | 7 | 0 | set_switch(60); stop |
| 6 | 301 | 30 / 1 | 3 | 0 | trigger_event(302); stop |
| 6 | 302 | 30 / 2 | 3 | 0 | trigger_event(303); stop |
| 6 | 303 | 30 / 3 | 3 | 0 | trigger_event(304); stop |
| 6 | 304 | 30 / 4 | 3 | 0 | trigger_event(305); stop |
| 6 | 305 | 30 / 5 | 3 | 0 | trigger_event(306); stop |
| 6 | 306 | 30 / 6 | 4 | 0 | trigger_event(307); stop |
| 6 | 307 | 30 / 7 | 4 | 0 | trigger_event(308); stop |
| 6 | 308 | 30 / 8 | 4 | 0 | trigger_event(309); stop |
| 6 | 309 | 30 / 9 | 4 | 0 | trigger_event(310); stop |
| 6 | 310 | 30 / 10 | 4 | 0 | trigger_event(311); stop |
| 6 | 311 | 30 / 11 | 5 | 0 | trigger_event(312); stop |
| 6 | 312 | 30 / 12 | 5 | 0 | trigger_event(313); stop |
| 6 | 313 | 30 / 13 | 5 | 0 | trigger_event(314); stop |
| 6 | 314 | 30 / 14 | 5 | 0 | trigger_event(315); stop |
| 6 | 315 | 30 / 15 | 5 | 0 | trigger_event(316); stop |
| 6 | 316 | 30 / 16 | 5 | 0 | trigger_event(317); stop |
| 6 | 317 | 30 / 17 | 5 | 0 | trigger_event(318); stop |
| 6 | 318 | 30 / 18 | 5 | 0 | trigger_event(319); stop |
| 6 | 319 | 30 / 19 | 5 | 0 | trigger_event(320); stop |
| 6 | 320 | 30 / 20 | 5 | 0 | trigger_event(321); stop |
| 6 | 321 | 30 / 21 | 6 | 0 | trigger_event(322); stop |
| 6 | 322 | 30 / 22 | 6 | 0 | trigger_event(323); stop |
| 6 | 323 | 30 / 23 | 6 | 0 | trigger_event(324); stop |
| 6 | 324 | 30 / 24 | 6 | 0 | trigger_event(325); stop |
| 6 | 325 | 30 / 25 | 6 | 0 | trigger_event(326); stop |
| 6 | 326 | 30 / 26 | 7 | 0 | trigger_event(327); stop |
| 6 | 327 | 30 / 27 | 7 | 0 | trigger_event(328); stop |
| 6 | 328 | 30 / 28 | 7 | 0 | trigger_event(329); stop |
| 6 | 329 | 30 / 29 | 7 | 0 | trigger_event(330); stop |
| 6 | 330 | 30 / 30 | 7 | 0 | set_switch(30); stop |
| 7 | 101 | 10 / 1 | 5 | 0 | trigger_event(102); stop |
| 7 | 102 | 10 / 2 | 5 | 0 | trigger_event(103); stop |
| 7 | 103 | 10 / 3 | 5 | 0 | trigger_event(104); stop |
| 7 | 104 | 10 / 4 | 5 | 0 | trigger_event(105); stop |
| 7 | 105 | 10 / 5 | 5 | 0 | trigger_event(106); stop |
| 7 | 106 | 10 / 6 | 5 | 0 | trigger_event(107); stop |
| 7 | 107 | 10 / 7 | 5 | 0 | trigger_event(108); stop |
| 7 | 108 | 10 / 8 | 5 | 0 | trigger_event(109); stop |
| 7 | 109 | 10 / 9 | 5 | 0 | trigger_event(110); stop |
| 7 | 110 | 10 / 10 | 5 | 0 | trigger_event(111); stop |
| 7 | 111 | 10 / 11 | 6 | 0 | trigger_event(112); stop |
| 7 | 112 | 10 / 12 | 6 | 0 | trigger_event(113); stop |
| 7 | 113 | 10 / 13 | 6 | 0 | trigger_event(114); stop |
| 7 | 114 | 10 / 14 | 6 | 0 | trigger_event(115); stop |
| 7 | 115 | 10 / 15 | 6 | 0 | trigger_event(116); stop |
| 7 | 116 | 10 / 16 | 6 | 0 | trigger_event(117); stop |
| 7 | 117 | 10 / 17 | 6 | 0 | trigger_event(118); stop |
| 7 | 118 | 10 / 18 | 6 | 0 | trigger_event(119); stop |
| 7 | 119 | 10 / 19 | 6 | 0 | trigger_event(120); stop |
| 7 | 120 | 10 / 20 | 6 | 0 | trigger_event(121); stop |
| 7 | 121 | 10 / 21 | 7 | 0 | trigger_event(122); stop |
| 7 | 122 | 10 / 22 | 7 | 0 | trigger_event(123); stop |
| 7 | 123 | 10 / 23 | 7 | 0 | trigger_event(124); stop |
| 7 | 124 | 10 / 24 | 7 | 0 | trigger_event(125); stop |
| 7 | 125 | 10 / 25 | 7 | 0 | trigger_event(126); stop |
| 7 | 126 | 10 / 26 | 7 | 0 | trigger_event(127); stop |
| 7 | 127 | 10 / 27 | 7 | 0 | trigger_event(128); stop |
| 7 | 128 | 10 / 28 | 7 | 0 | trigger_event(129); stop |
| 7 | 129 | 10 / 29 | 7 | 0 | trigger_event(130); stop |
| 7 | 130 | 10 / 30 | 7 | 0 | set_switch(10); stop |
| 8 | 801 | 80 / 1 | 3 | 0 | trigger_event(802); stop |
| 8 | 802 | 80 / 2 | 3 | 0 | trigger_event(803); stop |
| 8 | 803 | 80 / 3 | 3 | 0 | trigger_event(804); stop |
| 8 | 804 | 80 / 4 | 3 | 0 | trigger_event(805); stop |
| 8 | 805 | 80 / 5 | 3 | 0 | trigger_event(806); stop |
| 8 | 806 | 80 / 6 | 4 | 0 | trigger_event(807); stop |
| 8 | 807 | 80 / 7 | 4 | 0 | trigger_event(808); stop |
| 8 | 808 | 80 / 8 | 4 | 0 | trigger_event(809); stop |
| 8 | 809 | 80 / 9 | 4 | 0 | trigger_event(810); stop |
| 8 | 810 | 80 / 10 | 4 | 0 | trigger_event(811); stop |
| 8 | 811 | 80 / 11 | 5 | 0 | trigger_event(812); stop |
| 8 | 812 | 80 / 12 | 5 | 0 | trigger_event(813); stop |
| 8 | 813 | 80 / 13 | 5 | 0 | trigger_event(814); stop |
| 8 | 814 | 80 / 14 | 5 | 0 | trigger_event(815); stop |
| 8 | 815 | 80 / 15 | 5 | 0 | trigger_event(816); stop |
| 8 | 816 | 80 / 16 | 5 | 0 | trigger_event(817); stop |
| 8 | 817 | 80 / 17 | 5 | 0 | trigger_event(818); stop |
| 8 | 818 | 80 / 18 | 5 | 0 | trigger_event(819); stop |
| 8 | 819 | 80 / 19 | 5 | 0 | trigger_event(820); stop |
| 8 | 820 | 80 / 20 | 5 | 0 | trigger_event(821); stop |
| 8 | 821 | 80 / 21 | 6 | 0 | trigger_event(822); stop |
| 8 | 822 | 80 / 22 | 6 | 0 | trigger_event(823); stop |
| 8 | 823 | 80 / 23 | 6 | 0 | trigger_event(824); stop |
| 8 | 824 | 80 / 24 | 6 | 0 | trigger_event(825); stop |
| 8 | 825 | 80 / 25 | 6 | 0 | trigger_event(826); stop |
| 8 | 826 | 80 / 26 | 9 | 0 | trigger_event(827); stop |
| 8 | 827 | 80 / 27 | 9 | 0 | trigger_event(828); stop |
| 8 | 828 | 80 / 28 | 9 | 0 | trigger_event(829); stop |
| 8 | 829 | 80 / 29 | 9 | 0 | trigger_event(830); stop |
| 8 | 830 | 80 / 30 | 9 | 0 | set_switch(80); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
