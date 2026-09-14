# PSOBB research coverage

[QEdit Feature & Field Coverage Matrix](analysis/qedit-coverage/README.md) — editor forms, event handlers, declared records and entity/object labels, with evidence and required verification.

The goal is complete, source-backed quest research. The current database is **not 100% complete**. Counts refer to the supplied collection and tool versions, not every PSOBB quest or every possible client configuration.

| Research category | Available now | Remaining evidence needed |
|---|---|---|
| Quests and scripts | 527 decoded variants; full assembly, labels, cross-references, dialogue-bearing scripts, original downloads | Prove completeness of the global quest catalogue; gameplay verification and dynamic execution paths |
| Opcodes | 515 BB-supported source signatures (512 opcode values), aliases, operands, version flags, Qedit dialect | Verify every BB opcode behavior and edge case against client execution |
| NPCs | 62 constructor definitions, parameters, area masks, 11,201 placements, 3,464 handler candidates | Type-specific dynamic behavior, full dialogue/call-chain validation |
| Appearances | 57 Qedit previews; 12 visual classes with selector ranges; 48 observed visual blocks; seven Qedit special selectors | Every visual combination, special-model renders, client acceptance rules; Eggman identification unresolved |
| Scenes / cutscenes | 351 quest variants with indexed camera-opcode references, plus original scripts | A dedicated scene catalogue linking cameras, motion, dialogue, actors, timing and complete call chains |
| Floors and map IDs | 47 areas and source variant tables | Verify additional client versions and all runtime restrictions |
| Rooms and collision | 126 Qedit geometry maps with section IDs, transforms and collision meshes; per-quest room/wave records | Room-boundary ownership, navigation connections and validated spawn volumes |
| Monsters | 63 BB constructor definitions, parameters, names, area masks and 135,547 placements | Every parameter behavior, rare/Ultimate variant details and runtime spawn tests |
| Monster floor compatibility | Source-documented area masks, Qedit menus and corpus observations kept distinct | Resolve disagreements through client tests; presence in a quest alone is not compatibility proof |
| Objects | 280 ID records from Qedit, BB definitions and observations | Unresolved fields, complete visual gallery and runtime interaction tests |
| Waves, switches and interactions | Per-quest placements/events, script references and state/reward records | Dynamic dependencies and multiplayer verification |
| Items, flags, sound, particles, minigames | Relevant source code and existing quest examples; Antigravity exports held for review | Row-level source provenance and behavior verification before promoting imported claims |

## Evidence rules

Each category distinguishes extracted bytes, source-documented behavior, observed usage and runtime verification. Unknown values stay unknown. A source record does not prove every parameter combination is valid. A missing flag reference does not prove a flag is safe. Player classes, DAT types, instance IDs, area IDs, floor slots, room IDs and script labels remain separate namespaces.

The Quest AI Generator will be a separate project and URL after the research and compiler validation are ready. No generator is published at the database link.
