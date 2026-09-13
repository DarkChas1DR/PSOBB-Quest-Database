# Antigravity repair audit — 2026-09-13

Scope: 20 commits after verified publication `2b398eb`, ending at `ec64966`. The original quest corpus, object catalogue and map geometry were not changed by those commits. The added website and aggregate datasets require separate verification.

## Confirmed problems

| Finding | Evidence | Resolution |
|---|---|---|
| Generator advertised complete, crash-safe playable output without compiler or gameplay validation | Old root README and generate_quest.py docstring | Removed from the research website. Original code remains recoverable at commit ec64966; a separate generator project must pass validation before release. |
| Script label references patched to code byte offsets | Old index.html compileQuestBin writes fnMap[fnId] into SCRIPT16 operands; preserved QuestScript.cc lines 242 and 281 define SCRIPT16 as a function-table index | Generator withdrawn; no claim that its BIN/QST downloads are valid. |
| Episode 4 encoded as 3 | Old compileQuestBin emits primaryEp - 1; public episodes are 1, 2, 4, while quest episode selectors are 0, 1, 2 | Recorded as a generator defect. |
| Binary objective monitor never checks completion | Old function 100 emits only sync and jmp; it does not compile the displayed objective/reward assembly | Generated assembly and binaries cannot be treated as equivalent. |
| Qedit special-model selector extended to 11 entries | Imported master guide says Qedit offers IDs 0–10; preserved NPCBuild.pas names only seven entries and wraps at 7 | Active reference retains verified Qedit IDs 0–6. Other client models require independent evidence; their possible existence is not ruled out. |
| Unobserved persistent flags described as verified safe | Imported flags.json marks flags 0 onward safe based on zero observed references; master guide also recommends 1024+ despite preserved QuestScript.cc documenting 1024 bits for non-Ep3 | Removed from active reference. Corpus absence is not a safety proof. |
| Section origins / calculated centres described as authentic playable spawn positions | Original geometry stores section transforms and collision triangles, without proven room ownership or valid spawn volumes | Restored explicit separation between section markers, room boundaries and spawn validation. |
| Client generator conflated area IDs and floor slots | CLI AREA_KEYWORDS uses Episode 2 Temple area 1, while the canonical floor catalogue identifies its area as 0x13 | Preserve authoritative area/episode/floor mappings; retire experimental hard-coded tables. |

## Preserved work

The added master JSON, SQLite, prose and web-data exports are retained under `analysis/import-review/antigravity/`. They contain a mixture of extracted material and unsupported interpretations. They are excluded from the active catalogue until verified; this is not a declaration that every imported row is wrong. Generator history is preserved in Git at `ec64966`, and a local recovery copy was made before removing its active entry points.

The repaired website reads a reproducible catalogue generated only from the established source outputs. Quest scripts, map records, NPC/object fields, area compatibility, original downloads, geometry and opcode definitions remain accessible. Binary compilation, AI API keys and prompt generation are absent from the database site.

## Additional correction found during this audit

The earlier entity builder used a case-sensitive `Npc` check and misclassified `__QUEST_NPC__` type 0x0118. The classifier and SQLite archive were rebuilt: 63 monster definitions, 62 NPC definitions, 135,547 monster placements, 11,201 NPC placements, five unresolved records, and 3,464 static handler candidates. This was an earlier database defect, not an Antigravity change. Handler candidates are still static evidence, not complete dialogue executions.

## Limits

This repair audits the active publication and demonstrable regressions; it does not certify every imported row or achieve complete PSOBB engine coverage. No new quest was playtested. See [coverage checklist](../../DATABASE-COVERAGE.md) and [site validation](site-validation.json).
