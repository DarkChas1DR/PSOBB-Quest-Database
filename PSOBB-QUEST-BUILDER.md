# PSOBB quest-building reference for future work

The user wants future AI-generated PSOBB quests grounded in their client, Qedit and server quest data.

Start with `analysis/quest-knowledge/README.md` and `analysis/quest-knowledge/BUILDER-INSTRUCTIONS.md`. The SQLite database, JSONL retrieval chunks, compiler profiles, DAT schema, raw source snapshot and validation report are in that folder. The full per-quest disassemblies are under `analysis/server-catalogue/`.

For any requested quest/feature, deliver (1) overview/entity mapping, (2) complete commented assembly with exact compiler profile, (3) matching DAT spatial notes. Require Function 0 initialization, project-standard ret-only Function 1, yielding polling loops, explicit register ownership and multiplayer state synchronization. General scratch allocation is R0–R219 with documented reserved-use exclusions.

Do not copy the user's original monitor sketch verbatim: it needs window-message end correction, encounter-readiness gating, full spawn definitions and a synchronized floor-specific switch operation. `sync_register` does not synchronize a door by itself. The recovered Qedit opcode aliases differ from modern newserv names.

The source snapshot covers 1,558 server quest files and 527 decoded BIN/QST language variants. It is reference data for retrieval, not proof that every quest is bug-free or that every branch has been manually understood. Preserve all originals and distinguish assembled, statically checked and playtested status.

Query tool: `analysis/tools/query_knowledge.py`; rebuild tool: `analysis/tools/build_knowledge.py`; verification tool: `analysis/tools/verify_knowledge.py`. The research handoff remains in `analysis/RESEARCH-NOTES.md`.
