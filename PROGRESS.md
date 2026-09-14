# Research completion tracker

![Research milestones](analysis/progress.svg)

**3 of 8 defined checkpoints completed. This is milestone progress, not a claim that 37.5% of all PSOBB knowledge is verified.** Partial items do not contribute to the completed count. We can expand the checklist when new requirements are found, recording the reason instead of silently inflating completion.

| Checkpoint | Status | Acceptance criterion / remaining work |
|---|---|---|
| Initial Qedit feature inventory | Complete | Published forms, controls, handler links, record declarations and label inventory; scope limitations recorded |
| NPC appearance source/byte reference | Complete | Published BB layout, editor behavior and 48 observed-block checks; native tests are separate below |
| Placement source/byte reference | Complete | Published object/enemy mappings and 4,444,899 CSV-exposed field checks; source-only fields explicitly identified |
| Full supported appearance gallery | Partial | 443 offline sheets published: 424 selector values, 12 baselines, 7 special models. Remaining: combinations, colours/proportions, other special appearances, native visual checks and source/executable equivalence |
| Scene reconstruction | Partial | Trace camera, actor, dialogue and timing dependencies into complete scene chains; current camera references are not reconstructed scenes |
| Qedit save/reopen compatibility | Pending | One-field fixtures for supported record types and opcode/data paths; verify output bytes and label boundaries in the supplied Qedit |
| Clean-client behavior | Pending | Version-recorded tests of appearances, parameters, maps, spawns, scenes and completion |
| Multiplayer and final completeness audit | Pending | Party synchronization, join/failure paths and all outstanding field/feature gaps verified; no unsupported completeness claims |

## Current evidence

- [Quest limits and placement rules](analysis/quest-limits/README.md): format bounds and 527-variant measurements published; runtime capacity tests pending.

- [Browse the supported appearance selector gallery](analysis/entity-database/appearance-gallery/supported/README.md)

- [Qedit inventory](analysis/qedit-coverage/README.md)
- [NPC appearance fields](analysis/qedit-coverage/npc-appearance/README.md)
- [Monster/object saved fields](analysis/qedit-coverage/placements/README.md)
- [Full coverage gaps](DATABASE-COVERAGE.md)

The current automation surface cannot operate the native Windows Qedit or game client. Native save/reopen and gameplay checks require an available supported control path or user-produced test results. They remain pending; static decoding will not substitute for them.
