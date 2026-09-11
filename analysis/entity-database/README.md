# Monster and NPC databases

Companion registries to the quest library, built from the preserved newserv and Qedit definitions and all 527 decoded quest variants.

## Browse

- [Monster IDs, parameters and quest examples](monsters.md)
- [Monster availability by episode and area](areas.md)
- [NPC types, Qedit names, placements and interaction candidates](npcs.md)
- [Player class IDs, races and appearance ranges](classes.md)
- [Monster game names, Ultimate names and battle-parameter source mappings](monster-names.json)
- [Decoded NPC visual blocks, including names and face/hair/costume fields](npc-visual-blocks.json)
- [NPC opcode names, operands and source documentation](npc-opcodes.json)
- [Queryable SQLite database archive](entities.sqlite.gz), [definitions JSON](definitions.json), [validation](validation.json) and [source hashes](provenance.json)

## What is covered

The initial registry includes 64 BB monster constructor definitions, 61 NPC constructor definitions, and all 146,753 enemy/NPC placement records from the supplied corpus. It classifies 135,708 records as monsters and 11,040 as NPCs; five records have unclassified types and remain explicitly unresolved. These counts include language duplicates and are not counts of distinct monster species.

There are 12 player classes, 48 disassembler-recognized visual configuration blocks, and 3,370 distinct resolved static NPC handler candidates. The SQLite `handlers` table retains their complete label bodies; per-NPC pages link example handlers to the full quest script, where dialogue and called functions can be inspected. Handler bodies may call other labels, so a single label is not necessarily the entire conversation. Visual blocks are examples, not a catalogue of every named NPC or every face.

## ID namespaces and placement safety

**DAT base types, player class IDs, character IDs, function labels, extra-model selectors, and server EnemyType enums are different namespaces.** A RAmar player has class ID 3. Qedit's default RAmar/Bernie DAT NPC type is 36 (0x24). Neither value is the NPC's quest interaction label.

The area tables come from the BB version bit and area masks in the stored constructor definitions. For Hildebear, DAT type 0x0040 excludes Forest 1 and includes Forest 2. The same definition also lists the Episode 1 battle areas and Episode 2 VR Temple areas. It does not say all Episode 2 VR areas are valid.

Quest floor numbers are script slots. Resolve the actual map designation to an area before applying an area restriction. Observing an enemy in a file does not prove it spawns correctly. Unreachable waves, custom map designations, and client patches can explain apparent exceptions. Constructor masks are source-documented evidence, not tests of the supplied modded client.

## Standard NPC interaction fields

For the ordinary NPC family, the source documents:

| DAT parameter | Meaning |
|---|---|
| p1 | Action parameter; wandering distance when applicable |
| p2 | Visibility register selector |
| p3 | Hide-override register selector |
| p4 | Character/object number; values outside 100–999 select a free-play script context for interaction |
| p5 | Interaction label; zero means no interaction |
| p6 | Idle behavior; zero stationary, one random wandering |

Register selectors of 1000 or more have special free-play behavior; see [the exact source](../quest-knowledge/reference/server-source/Map.cc#L2514). Type-specific NPCs can differ. The stage NPC type 0x33 is excluded from generic handler matching. Other resolved handlers remain candidates until their constructor-specific rules and actual calls are checked. DAT float parameters are truncated to integers for this candidate search; original float values are retained.

Position, room, wave, facing angles and all seven parameters are available in each type's complete observation CSV and in SQLite. Angles remain raw engine values. Generic NPC fields alone do not establish a character's full appearance or complete dialogue.

## Appearance and code references

[PlayerSubordinates.hh](reference/PlayerSubordinates.hh) contains the visual structure, V3/V4 normalization bounds and special-model safety handling. [PlayerSubordinates.cc](reference/PlayerSubordinates.cc) retains related implementation. The structure's shared fields include class, name color, costume, skin, face, head, hair, hair color and proportions. BB adds its encoded name. Some bytes are explicitly newserv extensions, not original game requirements.

[EnemyType.cc](reference/EnemyType.cc) preserves game-name/Ultimate-name and battle-parameter mappings. [Map.cc](../quest-knowledge/reference/server-source/Map.cc) contains constructor definitions and server-side enemy variant/child interpretation. [QuestScript.cc](../quest-knowledge/reference/decoder-source/QuestScript.cc) supplies opcode semantics. These are source implementations and reference documentation; the complete client AI and animation code has not been reverse engineered here.

## Remaining gaps before unrestricted generation

- Face, costume and skin thumbnails, and visual confirmation of every NPC appearance.
- Complete NPC identity-to-dialogue linkage, dynamic handlers and script-created NPC tracking.
- Type-specific validation of every generic NPC handler candidate.
- Full client behavior, animation, collision and resource-loading rules; room geometry and safe spawn positions for each layout.
- Tests of monster availability and special NPC model combinations in the actual client build.
- Battle-stat values for each difficulty and mode, beyond the preserved parameter-index mappings.

The first database version is a usable, source-linked reference with explicit gaps. It must not be described as understanding every detail of every entity's code.

## Query and rebuild

```sh
python restore_library.py
python analysis/tools/query_entities.py type 0x40
python analysis/tools/query_entities.py type 0x24
python analysis/tools/query_entities.py class 3
python analysis/tools/query_entities.py check-area 0x40 --area 1
python analysis/tools/query_entities.py placements 0x24 --limit 10
```

`check-area` reports whether the source mask lists the area, not whether a gameplay test passed. Rebuild with `python analysis/tools/build_entity_database.py` after restoring the main quest database. Original source snapshots and the main database are not modified.
