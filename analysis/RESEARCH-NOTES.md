# PSOBB quest research handoff

## Full server library and generation contract

Start future quest work with `quest-knowledge/README.md` and `quest-knowledge/BUILDER-INSTRUCTIONS.md`. The complete supplied server quest directory is preserved: 1,558 source files, 527 decoded variants in 293 category/prefix/ID groups, including Episode 4. The searchable library contains scripts, placements, ordinary and random events, opcode references and compiler distinctions. All 47 earlier supplied variants match server files exactly. Validation results and generation cautions are recorded; eight reassembled headers need review and two language variants of A New Hope contain malformed event action offsets. No live gameplay or native Qedit compilation has been verified. The root `PSOBB-QUEST-BUILDER.md` routes future work to this contract. Originals remain unchanged.

## Episode 1 / Episode 2 batch added

The root input folder was expanded with quests. `catalogue/README.md` indexes 30 quest IDs / 47 language variants (including TTF): 5 Episode 1 and 25 Episode 2 by decoded English headers. All variants decoded and assembled; 26 exact byte roundtrips, 21 alignment-only changes preserving script bytes and label tables. See `catalogue/SCAN-FINDINGS.md` for the four absent-event-target candidates, seven map trailers, and Military Strikes Back's added startup-skip choice. Each dossier has complete script/map listings, placements, waves, label/reference indexes and state/reward operation locations. This is a batch structural scan, not manual interpretation of every script branch. Rerun with `tools/catalogue_quests.py`; it only scans root q*-bb-[ej].bin/qst files, preserving source files. Catalogue JSON stores individual source hashes and validation outcomes.

## Scope and location

Original inputs: `C:\Users\chasm\Documents\ChatGPT\PSOBB`. Keep them unchanged. The synced project `sources/` directory is empty and is read-only by project policy. All research outputs belong under this project's `analysis/` directory.

Read `QUEST-BUILDING-GUIDE.md` before further work. It distinguishes directly decoded facts from static inferences and untested runtime behavior.

## Confirmed results

- TTF English BIN: 15,748 bytes compressed, 71,436 bytes decompressed; quest 118, Episode 1, maximum four players.
- DAT: 11,412 bytes compressed, 36,780 bytes decompressed; 25 nonterminal sections, 16-byte terminating header; 277 objects, 216 enemy/NPC records, 69 events.
- 357 labels identified by the disassembler. Do not confuse populated labels with label-table capacity.
- Reassembling `extracted/ttf-qedit.txt` with newserv produces exactly the original decompressed BIN. Compressed bytes differ because the compressor's representation differs.
- Every trigger-event destination in the decoded DAT action streams resolves on its floor.
- `Qedit1.exe`: contains version title 2.0c Public; the nested Qedit executable is a different, apparently packed build.
- Main Qedit native code references and successfully loads archive members through its configuration path. Extracted `config.ppk` members are in `extracted/qedit-config/`.
- Crucial dialect difference: bundled F951 schema is BYTE/WORD/BYTE/BYTE; modern schema is five BYTEs. The WORD combines area and type. Bundled F8BC name is `set_epiII`; TTF uses value 0 for Episode 1.
- Qedit naming mode on the disassembler does not make its output directly importable Qedit text. It remains newserv syntax.
- Client native routine at VA 006B9A54 selects language-specific BIN suffixes. `SetDataTableOn.rel` was decoded with an explicit output path.

## Important TTF links

- Start registers floors 0, 2, 11, 5, 12, 7, 13, 8, 10, 14. Floor 8 has script handling but no DAT section.
- Forest: event 41 -> 411 -> 412 -> switch 90; alternative 42 -> switch 90. Trigger for 41 is placed in room 12; its event's enemy room is 4.
- Forest: 121 -> 1211 -> 1212 -> switch 10; alternative 122 -> switch 10.
- Boss teleporter 0x19 uses p5 as switch condition. Forest Door 0x80 packs switch number in p4's low byte.
- Dragon event 1 constructs room-1/group-1 objects, including script collision label 0x190 -> r15.
- Falz event 1 constructs group 1 across rooms 0/1/2; collisions call 0x193 -> r18. Completion monitors 0x1AE/0x1B0 -> r254; result finish 0x68 -> r255; success callback 0xFA.
- r54 elapsed seconds; r55 initial time; r110 death count; r112 enemy destruction count; r190 score/rank; r88 high-kill; r97 low-kill.
- Rank logic 0x262–0x26E; kill classification 0x3D4/0x3D5; result promotion 0x135/0x13D and related branches.
- Template EP1 console: label 50 -> r50; NPC state handler 1000; completion 1003 -> r255; reward 250.

## Reproduction

`tools/newserv/release/newserv-windows.exe` is the downloaded public newserv analysis tool (build `1f7faff9+`). Use named analysis actions; do not invoke without an action, which would start server mode.

Relevant actions: `decompress-prs`, `disassemble-quest-script --bb --language=E --map-file=...`, `disassemble-quest-map --bb`, `assemble-quest-script`, `encode-qst --bb`, `decode-qst`, `extract-ppk`, `disassemble-set-data-table --bb`.

Always supply an explicit output location where supported. `decode-qst` writes adjacent to its input, so first copy any source QST into the workspace. The help for set-data-table omits an output filename, but the actual tool accepts one; otherwise it attempts to write adjacent to its input. One such attempt against the read-only originals was denied, then corrected with an explicit workspace output path.

`tools/inspect_files.py` uses standard Python and reads originals plus decompressed outputs. It writes hashes, independent DAT parsing, CSVs, wave actions and validation results. It expects `ttf-reassembled.bind` to exist for its roundtrip assertion.

`tools/native_trace.py` uses pefile and Capstone installed locally under `tools/pythonlibs/`. These libraries required elevated read access after installation in this environment. Selected traces begin at checked instruction boundaries; they are not complete function decompilations. Raw pointer matches in `*-strings.csv` are leads, not automatically verified code cross-references.

Python runtime: `C:\Users\chasm\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe`.

## Work not yet established

No live Qedit save/reopen test or PSOBB playtest was performed. No server was launched or changed. The modded client's full VM, object constructors and differences from stock have not been reconstructed. No claim that all rewards, Love Check branches, dragon-control paths or hidden/debug branches are fully understood. No blanket claim that English/Japanese quest behavior is identical merely because both were decoded.

Further quest authoring should start with a concrete user design, a separate working copy, and a test server context. Preserve label/register/event mappings and verify multiplayer behavior before treating a new quest as playable.
