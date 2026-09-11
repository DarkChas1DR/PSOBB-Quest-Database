# PSOBB quest research

The original files are unchanged. Begin with the guide, then open the study QST in Qedit alongside the decoded script and map. Runtime behavior has not been playtested.

| Artifact | Contents |
|---|---|
| [Quest-building guide](<QUEST-BUILDING-GUIDE.md>) | Start here: architecture, TTF walkthrough and first-quest exercise. |
| [TTF study QST](<study/Towards-the-Future-study.qst>) | Complete English quest container for opening in Qedit; original BIN/DAT payloads preserved. |
| [Barebones EP1 QST copy](<extracted/barebones-ep1.qst>) | Copy of your supplied small template; unmodified. |
| [TTF annotated disassembly](<extracted/ttf-script.txt>) | Script offsets and map-to-script references. |
| [TTF Qedit-named disassembly](<extracted/ttf-qedit.txt>) | Uses newserv syntax, despite the opcode naming option; roundtrip verified. |
| [TTF map listing](<extracted/ttf-map.txt>) | All placements and event action streams. |
| [Wave chains](<extracted/wave-chains.csv>) | Join of events to their enemy records and completion actions. |
| [Objects](<extracted/objects.csv>) | Raw field values with floor-relative indices and decompressed file offsets. |
| [Enemy/NPC records](<extracted/enemy-sets.csv>) | Raw fields; includes NPCs and does not equal gameplay kill count. |
| [Events](<extracted/events.csv>) | All 69 events and their actions. |
| [Barebones script](<extracted/barebones-script.txt>) | Decoded from the supplied QST, with map references. |
| [Barebones map](<extracted/barebones-map.txt>) | Template map and console wiring. |
| [Recovered Qedit opcode definitions](<extracted/qedit-config/Asm.txt>) | Bundled opcode numbers, names and argument types. |
| [Recovered Qedit object fields](<extracted/qedit-config/itemsname.ini>) | Bundled parameter labels. |
| [Client area/variation table](<extracted/client-online-map-table.txt>) | Decoded from your actual client assets. |
| [Qedit native trace](<extracted/Qedit1-native-trace.txt>) | Selected static instruction sequences; not a complete decompilation. |
| [Client native trace](<extracted/psobb-native-trace.txt>) | Selected static instruction sequences from your client build. |
| [Validation results](<validation.json>) | Byte roundtrips, structural parsing and event target checks. |
| [Input inventory and hashes](<inventory.json>) | Precise executable and quest identities. |
| [Research handoff](<RESEARCH-NOTES.md>) | Durable notes and remaining boundaries for future tasks. |
