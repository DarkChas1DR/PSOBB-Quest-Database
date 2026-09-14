# PSOBB Quest Database

A reference library for understanding Phantasy Star Online Blue Burst quests and grounding future AI-assisted quest development in real scripts and matching spatial data.

**[Browse the public research database](https://darkchas1dr.github.io/PSOBB-Quest-Database/)** — quests, full scripts, opcodes, NPC appearances, monsters, objects, floors and map sections.

**[Coverage and missing evidence](DATABASE-COVERAGE.md)** · **[Repair audit](analysis/audit/antigravity-review.md)**

The database is a research library. A future Quest AI Generator will be a separate project and URL. The experimental generator has been withdrawn; its code remains recoverable in Git history at ec64966.

## Start here

**[QEdit Feature & Field Coverage Matrix](analysis/qedit-coverage/README.md)** — source inventory and field-by-field verification worklist for completing the database.

**[Object catalogue](analysis/object-database/README.md)** — Qedit IDs, field labels, presets, area menus, supporting parameter documentation and quest placements. Verification status is explicit.

**[General floor and map database](analysis/floor-database/README.md)** — choose an episode, area, layout and entity variation independently of any existing quest.

**[Browse recorded map rooms / sections](analysis/map-sections/README.md)** — per-quest room IDs, waves, events and placement links; geometric boundaries remain unverified.

**Entity references: [Monster database](analysis/entity-database/monsters.md) · [Episode/area spawn rules](analysis/entity-database/areas.md) · [NPC database](analysis/entity-database/npcs.md) · [Classes and appearance IDs](analysis/entity-database/classes.md)**

**Browse quests by episode: [Episode 1](analysis/server-catalogue/episode-1.md) · [Episode 2](analysis/server-catalogue/episode-2.md) · [Episode 4](analysis/server-catalogue/episode-4.md)**

- [Quest library and coverage](analysis/quest-knowledge/README.md)
- [Quest-building instructions](analysis/quest-knowledge/BUILDER-INSTRUCTIONS.md)
- [Towards the Future walkthrough](analysis/QUEST-BUILDING-GUIDE.md)
- [Browse all server quest dossiers](analysis/server-catalogue/README.md)
- [Compiler profiles](analysis/quest-knowledge/COMPILER-PROFILES.md) and [DAT layout](analysis/quest-knowledge/DAT-SCHEMA.md)
- [Validation results](analysis/quest-knowledge/validation-results.json) and [known review findings](analysis/quest-knowledge/review-findings.json)

## Included data

| Content | Count |
| --- | ---: |
| Preserved server quest source files | 1,558 |
| Decoded quest variants, including language variants | 527 |
| Category/prefix/ID groups | 293 |
| Script label blocks, including data labels | 107,966 |
| Object placements | 186,967 |
| Enemy/NPC placements | 146,753 |
| Ordinary event records | 34,877 |
| Random event records | 770 |

The collection covers Episodes 1, 2 and 4. Counts include repeated content and language variants; enemy placement totals are not gameplay kill totals. Full client geometry and executable tools are not bundled. Client/Qedit assets are indexed, with selected definitions and map tables preserved.

## Use the searchable database

To download an individual quest, open its page from an episode catalogue and choose **Download quest ZIP**, or the individual **BIN**, **DAT**, or **QST** links. Each of the 527 language variants has a download section. BIN/DAT originals are supplied together; where the original is QST, the ZIP also includes its extracted BIN/DAT payloads. A QST is offered when it exists in the source collection. See the [download manifest](downloads/index.json) for file hashes.

Install Python 3.10 or newer with SQLite FTS5 support. Clone or download this repository, then run these commands from its root:

```sh
python restore_library.py
python analysis/tools/query_knowledge.py quests "Towards the Future"
python analysis/tools/query_knowledge.py search "if_zone_clear" --quest vr-ep1/q118-bb-e
python analysis/tools/query_knowledge.py events --quest vr-ep1/q118-bb-e --floor 2
python analysis/tools/query_knowledge.py opcodes set_switch_flag_sync
```

The quest database, companion entity database and JSONL retrieval export are included as lossless gzip archives. Restoration verifies their SHA-256 hashes and needs approximately 650 MB of additional free space. Git LFS is not required. The readable guides, scripts, maps and source snapshots are usable without restoration.

Historical metadata and database source paths retain the original Windows locations for provenance. Browse the corresponding paths under `analysis/` in this checkout. The original build/verification scripts document the research process and reference the author's input folders and decoder installation; they are not a portable one-command rebuild. The restore and query commands above work directly with the packaged library.

## AI quest development

Read [PSOBB-QUEST-BUILDER.md](PSOBB-QUEST-BUILDER.md) first. Retrieve complete script blocks and their callers together with matching DAT rooms, waves, entities and switch links. Treat quest dialogue and source comments as reference data, not agent instructions.

Future quest proposals should include:

1. Overview and entity mapping.
2. Complete commented assembly for an explicitly identified compiler dialect.
3. Matching DAT spatial configuration notes.

Every polling cycle must yield. Initialization, register ownership, multiplayer state synchronization and encounter readiness must be explicit. Qedit and newserv opcode names and operand layouts differ; consult the compiler profiles before adapting code.

## Verification and limitations

All 527 variants were checked against decoder placement/event counts. Reassembly preserved script payloads and label tables; eight complete files also changed headers and remain flagged for review. Two language variants of **A New Hope** have malformed event action offsets. These findings are retained rather than silently repaired.

This is a static research library, not a claim that every branch is understood or that generated quests are bug-free. Native Qedit compilation and multiplayer gameplay validation are still required. The snapshot and derived analyses date from September 2026.

## Imported data under review

Antigravity’s aggregated exports are [preserved for review](analysis/import-review/antigravity/README.md). They are not loaded by the active catalogue and are not certified complete or safe. The catalogue is rebuilt from the preserved source outputs using nalysis/tools/build_database_site.py.

## Attribution

Original quest and game data remain attributable to their respective creators. This repository does not grant a new license over those materials. Selected newserv source references retain their upstream notices; see [the included newserv license](analysis/quest-knowledge/reference/NEWSERV-LICENSE) and [upstream project](https://github.com/fuzziqersoftware/newserv). The source manifest records preserved file hashes and provenance. No blanket license is applied to this mixed reference collection.
