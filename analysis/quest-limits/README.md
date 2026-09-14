# Quest limits and placement rules

Research reference for a future separate quest generator. **Per-wave, per-room, per-quest and simultaneous runtime capacity limits remain unverified.** No safe numeric budget is established here.

[Observed counts and example quests](observed-counts.md) · [Placement requirements](placement-rules.md) · [Native test protocol](test-protocol.md) · [Machine-readable constraints](constraints.json)

## Evidence categories

- **Format bound:** what a stored field can represent; not a gameplay capacity.
- **Observed example:** decoded data present in a supplied quest; not a successful playtest.
- **Tested recommendation:** a versioned, reproduced workload; none established by this audit.
- **Verified runtime limit:** a demonstrated boundary with supporting implementation evidence; none established by this audit.
- **Unknown:** retain explicitly; do not replace with a guessed default.

## Format findings

| Field | Stored representation | Meaning and restriction |
|---|---|---|
| Enemy room, wave and second wave field | unsigned 16-bit; 0–65535 | Identifier encoding, not 65,536 supported rooms or waves |
| EVT1 event ID | unsigned 32-bit; 0–4294967295 | Floor-scoped trigger identifier; duplicate IDs can intentionally activate multiple events |
| EVT1 room / wave | unsigned 16-bit | Select matching placements on the floor; not an enemy count |
| EVT1 delay | unsigned 32-bit | Stored frames; practical duration not established |
| EVT2 min/max enemies | unsigned 8-bit; 0–255 | Random-event field encoding; **not a universal 255-enemy wave limit** |
| EVT2 maximum waves | unsigned 16-bit | Random-event parameter; not a global wave budget |
| Enemy/NPC record size | 0x48 bytes | Includes NPCs and child-count/variant parameters |
| Object record size | 0x44 bytes | Object semantics depend on its type |

Evidence: preserved [Map.hh](../quest-knowledge/reference/decoder-source/Map.hh), EnemySetEntry, Event1Entry and Event2Entry; [DAT schema](../quest-knowledge/DAT-SCHEMA.md). This is source evidence, not a claim that the supplied client has been experimentally tested. Event1Entry source comments describe type 0 as inactive and type 1 as the normal controller; other values are not supported by that description.

The numeric maxima of integer fields must never become generator capacity recommendations. Section sizes and event counts likewise describe storage and do not establish memory, entity-pool or network limits.

## Still unknown

Maximum placed enemies per wave, room and quest; maximum concurrently active enemies; object/NPC pool interaction; child-entity expansion; practical multiplayer budgets; QEdit save/reopen limits; compiler limits; boss-specific setup constraints; valid spawn surfaces and all enemy/map compatibility combinations.

Use the [test protocol](test-protocol.md) to close these gaps. The generator should report “capacity not verified” and preserve uncertainty until results exist. A source menu entry, successful file decode, or absence from a quest is insufficient to prove client compatibility or incompatibility.

## Reproduce the corpus measurements

Run `python analysis/tools/build_quest_limits.py` from the repository root. It reads the published enemy placement CSVs and entity classification table. It does not execute quests. Language variants remain separate; totals are not unique quest counts. Random materialization, children, scripts and reachability are outside these measurements.
