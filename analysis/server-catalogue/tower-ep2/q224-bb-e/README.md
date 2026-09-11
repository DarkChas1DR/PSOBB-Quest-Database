# The West Tower — tower-ep2/q224-bb-e

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/tower-ep2/q224-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/tower-ep2/q224-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/tower-ep2/q224-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode2; header quest ID 224; language E. Static scan: **495 objects, 143 enemy/NPC records, 61 events, 222 script labels.** Script roundtrip: byte-identical.

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
0x0A, 0x1C, 0x00, 0x02, 0x00
0x11, 0x23, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 89 | 22 | 0 |
| 10 | 116 | 55 | 18 |
| 17 | 290 | 66 | 43 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 10 | 301 | 30 / 1 | 6 | 10 | stop |
| 10 | 401 | 40 / 1 | 6 | 10 | stop |
| 10 | 601 | 60 / 1 | 6 | 10 | set_switch(1); set_switch(2); set_switch(3); set_switch(4); set_switch(5); set_switch(6); set_switch(14); set_switch(15); set_switch(16); set_switch(21); set_switch(22); set_switch(23); set_switch(24); set_switch(25); set_switch(26); set_switch(27); set_switch(28); set_switch(29); set_switch(30); set_switch(31); set_switch(32); set_switch(33); set_switch(34); set_switch(36); set_switch(37); set_switch(38); set_switch(39); set_switch(40); set_switch(41); set_switch(42); set_switch(43); set_switch(44); set_switch(45); set_switch(46); set_switch(47); stop |
| 10 | 611 | 61 / 1 | 2 | 60 | set_switch(19); stop |
| 10 | 631 | 63 / 1 | 2 | 60 | set_switch(12); stop |
| 10 | 701 | 70 / 1 | 5 | 30 | trigger_event(7011); stop |
| 10 | 7011 | 70 / 2 | 5 | 10 | trigger_event(7012); stop |
| 10 | 7012 | 70 / 3 | 2 | 100 | set_switch(9); set_switch(10); stop |
| 10 | 711 | 71 / 1 | 5 | 30 | trigger_event(7111); stop |
| 10 | 7111 | 71 / 2 | 5 | 10 | trigger_event(7112); stop |
| 10 | 7112 | 71 / 3 | 2 | 100 | set_switch(17); set_switch(18); stop |
| 10 | 801 | 80 / 1 | 1 | 150 | stop |
| 10 | 811 | 81 / 1 | 1 | 150 | stop |
| 10 | 901 | 90 / 1 | 2 | 10 | stop |
| 10 | 2101 | 210 / 1 | 1 | 30 | stop |
| 10 | 2101 | 210 / 1 | 1 | 30 | stop |
| 10 | 2201 | 220 / 1 | 2 | 10 | stop |
| 10 | 2521 | 252 / 1 | 1 | 10 | stop |
| 17 | 11 | 1 / 1 | 1 | 180 | set_switch(1); stop |
| 17 | 21 | 2 / 1 | 1 | 10 | trigger_event(216); stop |
| 17 | 216 | 2 / 2 | 2 | 10 | set_switch(2); stop |
| 17 | 31 | 3 / 1 | 1 | 10 | trigger_event(311); stop |
| 17 | 311 | 3 / 2 | 1 | 30 | trigger_event(312); stop |
| 17 | 312 | 3 / 3 | 2 | 120 | set_switch(5); stop |
| 17 | 32 | 3 / 4 | 1 | 10 | trigger_event(321); stop |
| 17 | 321 | 3 / 5 | 1 | 10 | stop |
| 17 | 33 | 3 / 6 | 1 | 10 | trigger_event(331); stop |
| 17 | 331 | 3 / 7 | 1 | 10 | stop |
| 17 | 34 | 3 / 8 | 4 | 10 | stop |
| 17 | 41 | 4 / 1 | 2 | 10 | trigger_event(411); stop |
| 17 | 411 | 4 / 2 | 2 | 240 | set_switch(6); stop |
| 17 | 51 | 5 / 1 | 1 | 10 | trigger_event(511); stop |
| 17 | 511 | 5 / 2 | 1 | 10 | trigger_event(512); stop |
| 17 | 512 | 5 / 3 | 1 | 10 | trigger_event(513); stop |
| 17 | 513 | 5 / 4 | 2 | 10 | set_switch(8); stop |
| 17 | 52 | 5 / 5 | 1 | 30 | trigger_event(521); stop |
| 17 | 521 | 5 / 6 | 1 | 30 | stop |
| 17 | 101 | 10 / 1 | 1 | 30 | trigger_event(1011); stop |
| 17 | 1011 | 10 / 2 | 2 | 90 | set_switch(4); stop |
| 17 | 201 | 20 / 1 | 1 | 10 | trigger_event(2011); stop |
| 17 | 2011 | 20 / 2 | 1 | 10 | stop |
| 17 | 202 | 20 / 3 | 1 | 10 | trigger_event(2021); stop |
| 17 | 2021 | 20 / 4 | 1 | 10 | stop |
| 17 | 203 | 20 / 5 | 1 | 10 | trigger_event(2031); stop |
| 17 | 2031 | 20 / 6 | 2 | 10 | set_switch(3); stop |
| 17 | 204 | 20 / 7 | 2 | 10 | stop |
| 17 | 211 | 21 / 1 | 1 | 10 | trigger_event(2111); stop |
| 17 | 2111 | 21 / 2 | 1 | 10 | stop |
| 17 | 212 | 21 / 3 | 1 | 10 | trigger_event(2121); stop |
| 17 | 2121 | 21 / 4 | 1 | 10 | stop |
| 17 | 213 | 21 / 5 | 1 | 10 | trigger_event(2131); stop |
| 17 | 2131 | 21 / 6 | 3 | 90 | set_switch(7); stop |
| 17 | 214 | 21 / 7 | 1 | 10 | stop |
| 17 | 221 | 22 / 1 | 1 | 10 | trigger_event(2211); stop |
| 17 | 2211 | 22 / 2 | 3 | 10 | trigger_event(2212); stop |
| 17 | 2212 | 22 / 3 | 3 | 10 | trigger_event(2213); stop |
| 17 | 2213 | 22 / 4 | 3 | 90 | trigger_event(2214); stop |
| 17 | 2214 | 22 / 5 | 3 | 240 | set_switch(9); stop |
| 17 | 222 | 22 / 6 | 1 | 10 | trigger_event(2221); stop |
| 17 | 2221 | 22 / 7 | 3 | 10 | stop |
| 17 | 301 | 30 / 1 | 1 | 10 | set_switch(10); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

A backup is present; decompressed content identical: True. See [text differences](<backup-diff.txt>).

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
