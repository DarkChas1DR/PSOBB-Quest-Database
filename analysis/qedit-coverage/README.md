# QEdit Feature & Field Coverage Matrix

This is the first source inventory for the supplied Qedit/PSOBB research scope. **It is not a 100% compatibility certification.** Resource objects and label slots are inventory counts, not verified feature counts. No completion percentage is assigned.

## Build scope

Public Qedit source revision `2af5d144485b58ba28b57d98d2daa1a6b141ff4f`, application units explicitly referenced by `qedit.dpr`, their textual DFM resources, and existing Qedit entity/object label exports. External DirectX/Windows SDK units are excluded. See [source hashes and executable identity](provenance.json). **Exact equivalence between this public source and the supplied executable is not established.**

## Verification matrix

| Feature | Available evidence | Next required verification |
|---|---|---|
| BIN / DAT / QST structures | [Documented format and decoded corpus](../quest-knowledge/DAT-SCHEMA.md) | Trace Qedit read/write routines to each serialized field, including conditional formats. |
| Opcodes, operands and assembler dialect | [Source opcode definitions and corpus round trips](../quest-knowledge/COMPILER-PROFILES.md) | Match each editor instruction and alias to BB operands; verify F_ARGS, strings, labels and unsupported versions. |
| NPC placement and interaction | [62 constructor definitions and corpus placements](../entity-database/npcs.md) | Trace editor control → stored field → client behavior; verify every type-specific handler. |
| Class and appearance selectors | [12 classes and seven native special selectors](../entity-database/qedit/native-builder/README.md) | Map all serialized appearance fields and render every supported selection; prove source/executable correspondence. |
| Monster types and area restrictions | [63 constructor definitions, area masks and examples](../entity-database/monsters.md) | Resolve menu/constructor differences; test subtypes, rares and Ultimate behavior. |
| Object parameters and links | [280 ID records and Qedit field labels](../object-database/README.md) | Verify unresolved flags/parameters and door/switch links; complete images. |
| Floor slots, area IDs and variations | [47 areas and source variant tables](../floor-database/README.md) | Trace all map designation controls and variation restrictions. |
| Map sections, coordinates and collision | [126 collision maps with section transforms](../floor-database/geometry/README.md) | Prove room ownership, transform conventions, navigation links and valid spawn bounds. |
| Waves, events, switches and threads | [Per-quest event and placement evidence](../map-sections/README.md) | Verify action chains, completion, yielding and multiplayer state. |
| Dialogue, cameras and scene timing | [351 camera-reference quest variants](../../DATABASE-COVERAGE.md) | Reconstruct full actor/dialogue/camera call chains and timing. |
| Editor forms, menus and settings | [Application resource inventory in this audit](controls.json) | Resolve runtime-created controls and dynamic captions; map commands to data writes. |
| Qedit save/reopen and PSOBB execution | [Static decoder/reassembly results](../quest-knowledge/validation-results.json) | Run Qedit save/reopen fixtures and client tests; these are not covered by decoder round trips. |

## Inventoried resources

46 application units; 41 forms; 656 resource objects; 445 event bindings (445 matching implementation definitions located).

118 record declarations, 530 declared field entries, and 5154 Qedit label slots (2228 placeholders).

[Full controls and events](controls.json) · [Record declarations](record-declarations.json) · [Field labels](field-labels.json) · [Machine-readable matrix](matrix.json) · [Extraction counts](validation.json)

| Editor form | Resource objects | Event bindings |
|---|---:|---:|
| ['Quest Editor V 2.0c Public' — main.pas](forms/main.md) | 141 | 106 |
| ['Quest title' — FTitle.pas](forms/FTitle.md) | 4 | 1 |
| ['Quest Information' — FInfo.pas](forms/FInfo.md) | 4 | 1 |
| ['Script' — FScrypt.pas](forms/FScrypt.md) | 56 | 45 |
| ['Add command' — TCom.pas](forms/TCom.md) | 15 | 16 |
| ['Common setting' — FSetting.pas](forms/FSetting.md) | 6 | 1 |
| ['Edit' — FEdit.pas](forms/FEdit.md) | 12 | 13 |
| ['Map event' — Unit8.pas](forms/Unit8.md) | 8 | 6 |
| ['Add Monster' — Unit9.pas](forms/Unit9.md) | 8 | 3 |
| ['Add Objects' — Unit10.pas](forms/Unit10.md) | 9 | 4 |
| ['Description' — Unit11.pas](forms/Unit11.md) | 4 | 1 |
| ['Quest files manager' — Unit12.pas](forms/Unit12.md) | 11 | 6 |
| ['3D View' — Unit13.pas](forms/Unit13.md) | 2 | 11 |
| ['3D Processing' — Unit14.pas](forms/Unit14.md) | 3 | 0 |
| ['Monster randomness ' — Unit15.pas](forms/Unit15.md) | 12 | 6 |
| ['About' — Unit16.pas](forms/Unit16.md) | 5 | 1 |
| ['3D Settings' — Unit17.pas](forms/Unit17.md) | 12 | 4 |
| ['Form18' — Unit18.pas](forms/Unit18.md) | 2 | 0 |
| ['Items list manager' — Unit19.pas](forms/Unit19.md) | 3 | 3 |
| ['NPC Builder' — NPCBuild.pas](forms/NPCBuild.md) | 40 | 25 |
| ['Enemy stat' — EnemyStat.pas](forms/EnemyStat.md) | 8 | 3 |
| ['Load template' — Unit22.pas](forms/Unit22.md) | 11 | 5 |
| ['Load enemy data' — Unit23.pas](forms/Unit23.md) | 5 | 4 |
| ['Enemy resistance' — FEnemyResist.pas](forms/FEnemyResist.md) | 5 | 3 |
| ['Enemy Attack data' — FEnemyAttack.pas](forms/FEnemyAttack.md) | 6 | 4 |
| ['Enemy mouvement edit' — FEnemyMov.pas](forms/FEnemyMov.md) | 6 | 3 |
| ['Compatibility check' — FCompat.pas](forms/FCompat.md) | 6 | 3 |
| ['Float data editor ' — FFloatEdit.pas](forms/FFloatEdit.md) | 4 | 2 |
| ['Updates' — Unit29.pas](forms/Unit29.md) | 10 | 6 |
| ['Floor filter' — FFFilter.pas](forms/FFFilter.md) | 5 | 2 |
| ['Monster and box details' — FMonsDet.pas](forms/FMonsDet.md) | 4 | 3 |
| ['Vector list' — FVector.pas](forms/FVector.md) | 9 | 10 |
| ['Symbol Chat' — FSymbolChat.pas](forms/FSymbolChat.md) | 28 | 25 |
| ['AsmMode' — FAsmModeSel.pas](forms/FAsmModeSel.md) | 5 | 2 |
| ['Placement Options' — FPlacement.pas](forms/FPlacement.md) | 18 | 3 |
| ['Placement Modifiers' — FHotkeys.pas](forms/FHotkeys.md) | 16 | 1 |
| ['Snap Options' — FSnap.pas](forms/FSnap.md) | 11 | 5 |
| ['Script Text Editor' — FScriptTE.pas](forms/FScriptTE.md) | 125 | 98 |
| ['Replace Text' — FReplace.pas](forms/FReplace.md) | 8 | 4 |
| ['Go To Label' — FGoto.pas](forms/FGoto.md) | 4 | 3 |
| ['Find Text' — FFind.pas](forms/FFind.md) | 5 | 3 |

## How a field becomes verified

1. Locate its resource/control or command and handler in the appropriate source/build.
2. Trace the value into the internal record and serialization code; distinguish editor-only state.
3. Document exact disk type, offset, ranges, defaults and episode/version conditions from evidence.
4. Save and reopen a minimal fixture in the supplied Qedit and compare bytes.
5. Where behavior matters, test the matching clean client, including multiplayer where applicable.

A label alone does not establish parameter semantics. A record declaration does not establish disk packing. A handler link does not prove the full call path. Runtime-created controls, multiline resource values, conditional records and alternate builds require further inspection.

## Next bounded audit

Trace the main.pas `TMonster`, `TObj`, `TMapSection` and `NPCBuild.pas` `TNPCDATA` records through their loaders and save callers. Produce field-by-field mappings and a fixture plan before claiming serialized-field completeness.

[First NPC appearance writeback trace](npc-writeback-trace.md) — editor record to script HEX data, with outstanding fixture checks.
