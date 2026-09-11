# Findings from the Episode 1 / Episode 2 batch

The supplied folder contains **30 quest IDs and 47 language variants**, including the previously examined Towards the Future. The decoded English headers identify 5 Episode 1 quests and 25 Episode 2 quests. Filename ranges are not reliable episode identifiers.

Across one English copy of each quest, the scan indexed **10,083 object records, 8,506 enemy/NPC records, 2,462 wave events and 4,682 script labels**. These are structural counts, not totals of monsters a player can kill.

Each quest dossier includes the complete disassembled script and map, individual placement fields, wave chains and delays, an explicit script-reference index, and locations of state/timing/reward operations. These indexes make detailed questions answerable without repeatedly unpacking the source files. They do not mean every optional branch has already been manually explained.

## Rebuild validation

All 47 scripts assembled successfully. For 26, the decompressed rebuilt file matches the original byte for byte. For 21, the only differences are 1–3 zero padding bytes before the label table and the corresponding header size/offset changes. The actual script bytes and label-table contents match in all 47 variants. No rebuilt quest was deployed or playtested.

## Specific findings

Four quests have event actions pointing to event IDs absent from that floor's decoded event table:

| Quest | Floor | Source event | Absent target |
|---|---:|---:|---:|
| Malicious Uprising #1 | 2 | 14 | 142 |
| Twilight Sanctuary | 17 | 102 | 103 |
| Penumbral Surge #1 | 1 | 30 | 31 |
| Penumbral Surge #2 | 4 | 22 | 23 |

The Malicious Uprising finding appears in both supplied language variants. These are review candidates, not confirmed gameplay bugs: reachability, deliberate no-op endings, script-driven state and actual client behavior still matter.

Seven English map files contain extra nonzero bytes after their all-zero terminating header: Twilight Sanctuary, Sweep-up Operation #5, #7 and #9, and Penumbral Surge #1, #3 and #5. The parser preserves the full decompressed file and stops at the terminator. No claim that these trailing bytes cause an in-game problem.

Eight English BIN backups were present. Seven match their active versions after decompression. **Military Strikes Back differs:** the active script adds a “Skip startup dialogue?” choice. YES sets r0 and returns; NO invokes the original startup call and resumes the original sequence. Its dossier includes a text diff with generated reference comments excluded.

Supplied server metadata includes drop configuration such as `DefaultDropMode: SERVER_PRIVATE`. Those settings are separate from the quest script; a catalogue of the BIN alone would miss that part of the supplied configuration.

## Reading limits

Wave chains are explicit DAT relationships. Script-reference indexes include calls, jumps, callbacks and handler registrations; they are not complete runtime call graphs. Registers and dynamic targets may require tracing across multiple functions. Object constructors can spawn children and enemy records include NPCs. English/Japanese map identity does not establish script identity. Treat the language comparison as a guide to deeper review.

Original files remain unchanged. Use the catalogue index to select a quest for a more detailed gameplay or implementation walkthrough.
