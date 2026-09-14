# Native QEdit baseline: Towards the Future

On 2026-09-14 the user saved TTF explicitly as Blue Burst in QEdit v2.0c Public and reported reopening it without errors. The earlier GameCube save is excluded.

[Comparison and hashes](ttf-bb-result.json) · [Script diff](bb-script.diff) · [Map diff](bb-map.diff) · [Source excerpts](source-excerpts.md)

## Results

BB decoding succeeds. Script bytes match except three removed trailing nop/padding bytes. Label tables match. DAT section payloads match exactly; QEdit reordered sections. The maximum-player header changed from 4 to 0.

## Header issue resolved at source level

[PSOQuestHeaderBBBase](../../quest-knowledge/reference/server-source/QuestScript.hh) documents offset 0x15 as max_players: zero means no additional limit (four players). The supplied server Client.cc only rejects excess players when max_players is greater than zero. Therefore this change does not impose a zero-player limit. Running-server binary equivalence and gameplay are not established by source inspection.

QEdit's BB writer writes a zero dword at offsets 0x14–0x17, which include episode, maximum players and joinability in the server header definition. This explains the observed reset. The pinned source is evidence, not proof of exact executable equivalence.

## Scope and next research

One unchanged Episode 1 quest passed save/reopen and structural checks. This is not full editor compatibility. Test max_players values 1/2/3, nonzero episode headers and joinable flags separately: zeroing that word could discard intentional metadata. Do not blindly replace zero with four.

The next encounter fixture needs NPC interaction, two waves, a door and completion. Client gameplay, multiplayer synchronization and capacity tests remain pending. No server quests were overwritten.
