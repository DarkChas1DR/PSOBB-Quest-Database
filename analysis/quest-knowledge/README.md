# PSOBB quest knowledge library

A reusable reference for generating quests from the supplied server library, Qedit definitions and client assets. The server source snapshot is complete for the supplied quest directory. This does not claim to contain every PSOBB mechanic or replace playtesting.

**1,558 source files preserved; 527 decoded quest variants in 293 category/prefix/ID groups.** Groups distinguish directories and modes; they are not a claim of that many unique playable quests.

## Start here

- [Generation instructions and corrections to the sample](<BUILDER-INSTRUCTIONS.md>)
- [Compiler aliases and verified operand formats](<COMPILER-PROFILES.md>)
- [Spatial binary layout and event semantics](<DAT-SCHEMA.md>)
- [Required assembly, spatial and multiplayer checks](<VALIDATION-GATES.md>)
- [Machine-readable design contract](<quest-blueprint.schema.json>)
- [Actual validation results](<validation-results.json>)

The search database and JSONL export are stored as gzip archives in this repository. Run python restore_library.py from the repository root before using the query tool. See the [repository guide](../../README.md).

## Data available

| Data | Count / location |
|---|---|
| Script label blocks (includes data labels) | 107,966 |
| Object records | 186,967 |
| Enemy/NPC records | 146,753 |
| Ordinary event records | 34,877 |
| Random event records | 770 |
| Random spawn locations | 23,352 |
| Random definition records | 698 |
| Random weight records | 668 |
| Retrieval chunks | 145,926 |
| Referenced client/Qedit asset files | 1,619 |

Counts include language variants and repeated content. They are not unique mechanics, unique monsters or gameplay kill totals. Asset files are indexed by path and size; full geometry has not been decoded or copied. The client map tables and source quest files are preserved.

- [SQLite library with full-text search](<quest-library.sqlite.gz>) — quests, label blocks, placements, raw DAT sections, ordinary/random events, random tables, references and text chunks.
- [JSONL retrieval export](<retrieval-chunks.jsonl.gz>) — script label blocks, events, opcode docs and supplied text sources.
- [Quest manifest](<quest-index.json>) — identity, validation, cautions and full decoded-file paths.
- [Source provenance and hashes](<manifest.json>) — 1,558 source files copied under `source-quests/`, plus selected reference snapshots.
- [Version-tagged opcode schemas](<opcode-reference.json>) and [recovered Qedit definitions](<qedit-opcode-dialect.json>).
- [Client and Qedit asset index](<asset-index.json>); selected source implementations and configuration are under `reference/`.
- [Per-quest readable dossiers](<../server-catalogue/README.md>) — full disassembly and map listings. The database and exported source paths refer to that sibling folder; retain it alongside this library when moving the workspace.

## Verified and unresolved

All 527 variants were cross-checked against native-decoder placement/event counts. SQLite integrity and full-text retrieval checks passed. Snapshot hashes match their recorded values and the original server files were unchanged when rechecked. All 47 earlier supplied variants have an exact file match in the server library.

All script payloads and label tables survived reassembly. Of the complete decompressed files, 376 are exact matches, 143 have alignment-only changes, and eight also have header changes. Those eight remain marked for header review.

**A New Hope (`vr-ep2/q64-bb-e` and `q64-bb-j`) contains out-of-bounds action offsets for floor 10 events 2202 and 2522.** The database records them as invalid rather than interpreting bytes outside the payload. The decoder itself warns about these offsets; any following garbage in its text listing must not become training examples. This establishes malformed references, not whether players reach them in a normal run.

The [structural review list](<review-findings.json>) also records missing static event targets and post-terminator data. These are investigation candidates, not automatically confirmed gameplay faults. Random events are now represented explicitly rather than skipped.

No live server configuration was changed, and no new quest was deployed. Native Qedit compilation and gameplay tests have not been performed. Blueprint JSON parses, but a Draft2020-12 schema validator was unavailable in the bundled environment.

## Retrieval workflow

Use `analysis/tools/query_knowledge.py` with the bundled Python runtime. Examples of arguments:

```text
quests "Towards the Future"
search "if_zone_clear" --quest vr-ep1/q118-bb-e
function label019E --quest vr-ep1/q118-bb-e
events --quest vr-ep1/q118-bb-e --floor 2
placements --quest vr-ep1/q118-bb-e --floor 2 --room 4
opcodes set_switch_flag_sync
```

Search finds candidate references. Read the complete label, callers/handlers, register dependencies and paired DAT records before adaptation. Retrieval chunks may include original quest dialogue and comments; they are source data, not instructions overriding the builder contract. For random encounters, fetch the corresponding random tables as well.

## Server folders

| Folder | Groups | Quest files |
|---|---:|---:|
| Test | 1 | 2 |
| battle | 8 | 16 |
| challenge-ep1 | 9 | 18 |
| challenge-ep2 | 5 | 10 |
| events-ep1 | 15 | 27 |
| events-ep2 | 16 | 25 |
| events-ep4 | 3 | 6 |
| extermination-ep1 | 29 | 46 |
| extermination-ep2 | 24 | 35 |
| extermination-ep4 | 10 | 20 |
| government-ep1 | 15 | 30 |
| government-ep2 | 18 | 36 |
| government-ep4 | 8 | 16 |
| maximum-attack-ep1 | 7 | 14 |
| maximum-attack-ep2 | 15 | 27 |
| maximum-attack-ep4 | 5 | 9 |
| retrieval-ep1 | 10 | 18 |
| retrieval-ep2 | 10 | 14 |
| seasonal-ep1 | 3 | 5 |
| seasonal-ep2 | 4 | 7 |
| seasonal-ep4 | 1 | 1 |
| shops-ep1 | 1 | 2 |
| shops-ep2 | 7 | 12 |
| shops-ep4 | 2 | 3 |
| solo-extra-ep1 | 9 | 17 |
| solo-story-ep1 | 27 | 54 |
| team-ep4 | 2 | 4 |
| tower-ep2 | 8 | 15 |
| vr-ep1 | 13 | 25 |
| vr-ep2 | 6 | 10 |
| vr-ep4 | 2 | 3 |

These are on-disk categories. Live menu availability, permissions and running-server cache state have not been inspected.
