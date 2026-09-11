# 奪われたヘルパラッシュ — retrieval-ep1/q061-bb-j

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/retrieval-ep1/q061-bb-j.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/retrieval-ep1/q061-bb-j.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/retrieval-ep1/q061-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode1; header quest ID 120; language J. Static scan: **354 objects, 512 enemy/NPC records, 137 events, 135 script labels.** Script roundtrip: byte-identical.

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
0x08, 0x08, 0x00, 0x00, 0x00
0x09, 0x09, 0x00, 0x00, 0x00
0x0A, 0x0A, 0x00, 0x00, 0x00
0x0E, 0x0E, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 20 | 0 |
| 8 | 109 | 184 | 52 |
| 9 | 121 | 147 | 42 |
| 10 | 92 | 160 | 42 |
| 14 | 6 | 1 | 1 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 8 | 321 | 32 / 1 | 3 | 3 | trigger_event(322); stop |
| 8 | 322 | 32 / 2 | 4 | 3 | trigger_event(323); stop |
| 8 | 323 | 32 / 3 | 4 | 3 | set_switch(32); stop |
| 8 | 501 | 50 / 1 | 2 | 3 | trigger_event(502); stop |
| 8 | 502 | 50 / 2 | 3 | 3 | trigger_event(503); stop |
| 8 | 503 | 50 / 3 | 3 | 3 | set_switch(50); stop |
| 8 | 504 | 50 / 4 | 2 | 3 | trigger_event(505); stop |
| 8 | 505 | 50 / 5 | 2 | 3 | set_switch(52); stop |
| 8 | 221 | 22 / 1 | 4 | 3 | trigger_event(222); stop |
| 8 | 222 | 22 / 2 | 3 | 3 | trigger_event(223); stop |
| 8 | 223 | 22 / 3 | 4 | 3 | construct_objects(room=22,group_or_wave=1); stop |
| 8 | 401 | 40 / 1 | 3 | 3 | trigger_event(402); stop |
| 8 | 402 | 40 / 2 | 4 | 3 | trigger_event(403); stop |
| 8 | 403 | 40 / 3 | 5 | 3 | set_switch(40); stop |
| 8 | 311 | 31 / 1 | 4 | 3 | trigger_event(312); stop |
| 8 | 312 | 31 / 2 | 3 | 3 | trigger_event(313); stop |
| 8 | 313 | 31 / 3 | 4 | 3 | construct_objects(room=31,group_or_wave=1); stop |
| 8 | 241 | 24 / 1 | 3 | 3 | trigger_event(242); stop |
| 8 | 242 | 24 / 2 | 4 | 3 | trigger_event(243); stop |
| 8 | 243 | 24 / 3 | 4 | 3 | set_switch(24); stop |
| 8 | 611 | 61 / 1 | 4 | 3 | trigger_event(612); stop |
| 8 | 612 | 61 / 2 | 6 | 3 | set_switch(61); stop |
| 8 | 651 | 65 / 1 | 3 | 3 | trigger_event(652); stop |
| 8 | 652 | 65 / 2 | 3 | 3 | trigger_event(653); stop |
| 8 | 653 | 65 / 3 | 3 | 3 | trigger_event(654); stop |
| 8 | 654 | 65 / 4 | 3 | 3 | set_switch(65); stop |
| 8 | 211 | 21 / 1 | 3 | 3 | trigger_event(212); stop |
| 8 | 212 | 21 / 2 | 4 | 3 | trigger_event(213); stop |
| 8 | 213 | 21 / 3 | 4 | 3 | set_switch(21); stop |
| 8 | 101 | 10 / 1 | 3 | 3 | trigger_event(102); stop |
| 8 | 102 | 10 / 2 | 4 | 3 | set_switch(10); stop |
| 8 | 111 | 11 / 1 | 3 | 3 | trigger_event(112); stop |
| 8 | 112 | 11 / 2 | 3 | 3 | set_switch(11); stop |
| 8 | 231 | 23 / 1 | 2 | 3 | trigger_event(232); stop |
| 8 | 232 | 23 / 2 | 3 | 3 | trigger_event(233); stop |
| 8 | 233 | 23 / 3 | 4 | 3 | set_switch(23); stop |
| 8 | 331 | 33 / 1 | 3 | 3 | trigger_event(332); stop |
| 8 | 332 | 33 / 2 | 4 | 3 | trigger_event(333); stop |
| 8 | 333 | 33 / 3 | 4 | 3 | set_switch(33); stop |
| 8 | 701 | 70 / 1 | 3 | 3 | trigger_event(702); stop |
| 8 | 702 | 70 / 2 | 3 | 3 | trigger_event(703); stop |
| 8 | 703 | 70 / 3 | 4 | 3 | trigger_event(704); stop |
| 8 | 704 | 70 / 4 | 5 | 3 | trigger_event(705); stop |
| 8 | 705 | 70 / 5 | 5 | 3 | set_switch(70); stop |
| 8 | 301 | 30 / 1 | 4 | 3 | trigger_event(302); stop |
| 8 | 302 | 30 / 2 | 2 | 3 | trigger_event(303); stop |
| 8 | 303 | 30 / 3 | 4 | 3 | set_switch(30); stop |
| 8 | 201 | 20 / 1 | 3 | 3 | trigger_event(202); stop |
| 8 | 202 | 20 / 2 | 3 | 3 | trigger_event(203); stop |
| 8 | 203 | 20 / 3 | 4 | 3 | set_switch(20); stop |
| 8 | 601 | 60 / 1 | 4 | 3 | trigger_event(602); stop |
| 8 | 602 | 60 / 2 | 6 | 3 | set_switch(60); stop |
| 9 | 301 | 30 / 1 | 3 | 3 | trigger_event(302); stop |
| 9 | 302 | 30 / 2 | 4 | 3 | trigger_event(303); stop |
| 9 | 303 | 30 / 3 | 4 | 3 | set_switch(30); stop |
| 9 | 411 | 41 / 1 | 4 | 3 | trigger_event(412); stop |
| 9 | 412 | 41 / 2 | 4 | 3 | trigger_event(413); stop |
| 9 | 413 | 41 / 3 | 5 | 3 | set_switch(41); stop |
| 9 | 501 | 50 / 1 | 3 | 3 | trigger_event(502); stop |
| 9 | 502 | 50 / 2 | 3 | 3 | set_switch(50); stop |
| 9 | 321 | 32 / 1 | 3 | 3 | trigger_event(322); stop |
| 9 | 322 | 32 / 2 | 4 | 3 | trigger_event(323); stop |
| 9 | 323 | 32 / 3 | 2 | 3 | set_switch(32); stop |
| 9 | 441 | 44 / 1 | 2 | 3 | trigger_event(442); stop |
| 9 | 442 | 44 / 2 | 4 | 3 | trigger_event(443); stop |
| 9 | 443 | 44 / 3 | 5 | 3 | set_switch(44); stop |
| 9 | 221 | 22 / 1 | 3 | 3 | trigger_event(222); stop |
| 9 | 222 | 22 / 2 | 4 | 3 | set_switch(22); stop |
| 9 | 601 | 60 / 1 | 3 | 3 | trigger_event(602); stop |
| 9 | 602 | 60 / 2 | 4 | 3 | trigger_event(603); stop |
| 9 | 603 | 60 / 3 | 4 | 3 | set_switch(60); stop |
| 9 | 421 | 42 / 1 | 1 | 3 | trigger_event(422); stop |
| 9 | 422 | 42 / 2 | 4 | 3 | trigger_event(423); stop |
| 9 | 423 | 42 / 3 | 5 | 3 | set_switch(42); stop |
| 9 | 331 | 33 / 1 | 2 | 3 | trigger_event(332); stop |
| 9 | 332 | 33 / 2 | 3 | 3 | trigger_event(333); stop |
| 9 | 333 | 33 / 3 | 4 | 3 | set_switch(33); stop |
| 9 | 241 | 24 / 1 | 4 | 3 | trigger_event(242); stop |
| 9 | 242 | 24 / 2 | 4 | 3 | set_switch(24); stop |
| 9 | 231 | 23 / 1 | 3 | 3 | trigger_event(232); stop |
| 9 | 232 | 23 / 2 | 4 | 3 | set_switch(23); stop |
| 9 | 431 | 43 / 1 | 2 | 3 | trigger_event(432); stop |
| 9 | 432 | 43 / 2 | 3 | 3 | trigger_event(433); stop |
| 9 | 433 | 43 / 3 | 4 | 3 | set_switch(43); stop |
| 9 | 311 | 31 / 1 | 3 | 3 | trigger_event(312); stop |
| 9 | 312 | 31 / 2 | 4 | 3 | trigger_event(313); stop |
| 9 | 313 | 31 / 3 | 5 | 3 | set_switch(31); stop |
| 9 | 401 | 40 / 1 | 3 | 3 | trigger_event(402); stop |
| 9 | 402 | 40 / 2 | 4 | 3 | trigger_event(403); stop |
| 9 | 403 | 40 / 3 | 4 | 3 | set_switch(40); stop |
| 9 | 211 | 21 / 1 | 3 | 3 | trigger_event(212); stop |
| 9 | 212 | 21 / 2 | 3 | 3 | set_switch(21); stop |
| 9 | 201 | 20 / 1 | 3 | 3 | trigger_event(202); stop |
| 9 | 202 | 20 / 2 | 4 | 3 | set_switch(20); stop |
| 10 | 401 | 40 / 1 | 3 | 3 | trigger_event(402); stop |
| 10 | 402 | 40 / 2 | 3 | 3 | trigger_event(403); stop |
| 10 | 403 | 40 / 3 | 5 | 3 | set_switch(40); stop |
| 10 | 301 | 30 / 1 | 4 | 3 | trigger_event(302); stop |
| 10 | 302 | 30 / 2 | 4 | 3 | trigger_event(303); stop |
| 10 | 303 | 30 / 3 | 4 | 3 | set_switch(30); stop |
| 10 | 201 | 20 / 1 | 3 | 3 | trigger_event(202); stop |
| 10 | 202 | 20 / 2 | 4 | 3 | set_switch(20); stop |
| 10 | 411 | 41 / 1 | 3 | 3 | trigger_event(412); stop |
| 10 | 412 | 41 / 2 | 4 | 3 | trigger_event(413); stop |
| 10 | 413 | 41 / 3 | 4 | 3 | set_switch(41); stop |
| 10 | 311 | 31 / 1 | 4 | 3 | trigger_event(312); stop |
| 10 | 312 | 31 / 2 | 6 | 3 | trigger_event(313); stop |
| 10 | 313 | 31 / 3 | 6 | 3 | set_switch(31); stop |
| 10 | 421 | 42 / 1 | 3 | 3 | trigger_event(422); stop |
| 10 | 422 | 42 / 2 | 4 | 3 | trigger_event(423); stop |
| 10 | 423 | 42 / 3 | 5 | 3 | set_switch(42); stop |
| 10 | 431 | 43 / 1 | 3 | 3 | trigger_event(432); stop |
| 10 | 432 | 43 / 2 | 4 | 3 | trigger_event(433); stop |
| 10 | 433 | 43 / 3 | 3 | 3 | set_switch(43); stop |
| 10 | 221 | 22 / 1 | 3 | 3 | trigger_event(222); stop |
| 10 | 222 | 22 / 2 | 4 | 3 | set_switch(22); stop |
| 10 | 601 | 60 / 1 | 2 | 3 | trigger_event(602); stop |
| 10 | 602 | 60 / 2 | 1 | 3 | set_switch(60); stop |
| 10 | 603 | 60 / 3 | 3 | 3 | trigger_event(604); stop |
| 10 | 604 | 60 / 4 | 3 | 3 | trigger_event(605); stop |
| 10 | 605 | 60 / 5 | 3 | 3 | set_switch(61); stop |
| 10 | 501 | 50 / 1 | 4 | 3 | trigger_event(502); stop |
| 10 | 502 | 50 / 2 | 4 | 3 | construct_objects(room=50,group_or_wave=1); stop |
| 10 | 321 | 32 / 1 | 4 | 3 | trigger_event(322); stop |
| 10 | 322 | 32 / 2 | 5 | 3 | trigger_event(323); stop |
| 10 | 323 | 32 / 3 | 6 | 3 | set_switch(32); stop |
| 10 | 211 | 21 / 1 | 2 | 3 | trigger_event(212); stop |
| 10 | 212 | 21 / 2 | 3 | 3 | set_switch(21); stop |
| 10 | 441 | 44 / 1 | 4 | 3 | trigger_event(442); stop |
| 10 | 442 | 44 / 2 | 4 | 3 | trigger_event(443); stop |
| 10 | 443 | 44 / 3 | 4 | 3 | set_switch(44); stop |
| 10 | 801 | 80 / 1 | 4 | 3 | trigger_event(802); stop |
| 10 | 802 | 80 / 2 | 4 | 3 | trigger_event(803); stop |
| 10 | 803 | 80 / 3 | 4 | 3 | trigger_event(804); stop |
| 10 | 804 | 80 / 4 | 4 | 3 | trigger_event(805); stop |
| 10 | 805 | 80 / 5 | 6 | 3 | set_switch(80); stop |
| 14 | 1 | 0 / 1 | 1 | 50 | construct_objects(room=0,group_or_wave=1); construct_objects(room=1,group_or_wave=1); construct_objects(room=2,group_or_wave=1); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
