# New Mop-Up Operation #4 — extermination-ep4/q819-bb-e

[Browse recorded rooms / sections](sections.md) · [Section data](sections.json)

<!-- quest-downloads:start -->
## Download quest files

**[Download quest ZIP](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/downloads/extermination-ep4/q819-bb-e.zip?download=1)**

[Original BIN](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/extermination-ep4/q819-bb-e.bin?download=1) · [Original DAT](https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/analysis/quest-knowledge/source-quests/extermination-ep4/q819-bb.dat?download=1)

BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.

These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page's variant.
<!-- quest-downloads:end -->

Episode4; header quest ID 819; language E. Static scan: **177 objects, 223 enemy/NPC records, 41 events, 151 script labels.** Script roundtrip: alignment-only.

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
0x07, 0x2A, 0x00, 0x00, 0x00
```

## Floors

| Floor | Objects | Enemy/NPC records | Events |
|---|---:|---:|---:|
| 0 | 26 | 17 | 0 |
| 7 | 151 | 206 | 41 |

## Wave progression

Numbers below are decimal; delays are frames. Alternatives and parallel triggers must not be mistaken for one compulsory sequence.

| Floor | Event | Room / wave | Records | Delay | Completion actions |
|---|---:|---|---:|---:|---|
| 7 | 101 | 10 / 1 | 6 | 3 | trigger_event(102); stop |
| 7 | 102 | 10 / 2 | 9 | 3 | trigger_event(103); stop |
| 7 | 103 | 10 / 3 | 8 | 3 | trigger_event(104); stop |
| 7 | 104 | 10 / 4 | 9 | 3 | set_switch(10); stop |
| 7 | 201 | 20 / 1 | 2 | 3 | trigger_event(202); stop |
| 7 | 202 | 20 / 2 | 5 | 3 | trigger_event(203); stop |
| 7 | 203 | 20 / 3 | 7 | 3 | set_switch(20); stop |
| 7 | 211 | 21 / 1 | 3 | 3 | trigger_event(212); stop |
| 7 | 212 | 21 / 2 | 4 | 3 | trigger_event(213); stop |
| 7 | 213 | 21 / 3 | 5 | 3 | set_switch(21); stop |
| 7 | 221 | 22 / 1 | 5 | 3 | trigger_event(222); stop |
| 7 | 222 | 22 / 2 | 7 | 3 | trigger_event(223); stop |
| 7 | 223 | 22 / 3 | 5 | 3 | set_switch(22); stop |
| 7 | 231 | 23 / 1 | 4 | 3 | trigger_event(232); stop |
| 7 | 232 | 23 / 2 | 4 | 3 | trigger_event(233); stop |
| 7 | 233 | 23 / 3 | 3 | 3 | set_switch(23); stop |
| 7 | 241 | 24 / 1 | 5 | 3 | trigger_event(242); stop |
| 7 | 242 | 24 / 2 | 4 | 3 | trigger_event(243); stop |
| 7 | 243 | 24 / 3 | 4 | 3 | set_switch(24); stop |
| 7 | 251 | 25 / 1 | 5 | 3 | trigger_event(252); stop |
| 7 | 252 | 25 / 2 | 4 | 3 | trigger_event(253); stop |
| 7 | 253 | 25 / 3 | 6 | 3 | set_switch(25); stop |
| 7 | 261 | 26 / 1 | 4 | 3 | trigger_event(262); stop |
| 7 | 262 | 26 / 2 | 6 | 3 | trigger_event(263); stop |
| 7 | 263 | 26 / 3 | 6 | 3 | set_switch(26); stop |
| 7 | 271 | 27 / 1 | 4 | 3 | trigger_event(272); stop |
| 7 | 272 | 27 / 2 | 3 | 3 | trigger_event(273); stop |
| 7 | 273 | 27 / 3 | 5 | 3 | set_switch(27); stop |
| 7 | 401 | 40 / 1 | 5 | 3 | trigger_event(402); stop |
| 7 | 402 | 40 / 2 | 4 | 3 | trigger_event(403); stop |
| 7 | 403 | 40 / 3 | 5 | 3 | set_switch(40); stop |
| 7 | 411 | 41 / 1 | 4 | 3 | trigger_event(412); stop |
| 7 | 412 | 41 / 2 | 5 | 3 | trigger_event(413); stop |
| 7 | 413 | 41 / 3 | 5 | 3 | trigger_event(414); stop |
| 7 | 414 | 41 / 4 | 9 | 3 | set_switch(41); stop |
| 7 | 421 | 42 / 1 | 4 | 3 | trigger_event(422); stop |
| 7 | 422 | 42 / 2 | 4 | 3 | trigger_event(423); stop |
| 7 | 423 | 42 / 3 | 4 | 3 | set_switch(42); stop |
| 7 | 501 | 50 / 1 | 3 | 3 | trigger_event(502); stop |
| 7 | 502 | 50 / 2 | 5 | 3 | trigger_event(503); stop |
| 7 | 503 | 50 / 3 | 7 | 3 | set_switch(50); stop |

## Review notes

No structural or event-destination issues found by these checks. This does not establish reachability or runtime correctness.

A backup is present; decompressed content identical: True. See [text differences](<backup-diff.txt>).

Additional [server metadata](<server-metadata.json>) is supplied. It is separate from quest bytecode and can affect drops.
