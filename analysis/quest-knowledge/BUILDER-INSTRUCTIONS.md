# PSOBB Quest Builder — project instructions

These instructions implement the user's quest-building conventions while keeping them separate from verified VM behavior and compiler dialect. Use this file together with the evidence database; do not rely on an isolated sample or opcode name.

## Required output when building a quest or feature

1. **Overview and entity mapping:** episode, game mode, compiler profile, floors, areas, variations, rooms, waves, event IDs, door/switch links, NPCs, script labels, register allocation and objective progression.
2. **Complete commented PASM assembly:** all referenced functions and labels defined, with exact compiler dialect declared. Supply a separately labelled newserv source if that is the format actually assembled. Do not call newserv text Qedit-importable PASM without verifying conversion.
3. **DAT spatial configuration:** positions, rotations, rooms, types and every relevant parameter; activation bounds; event actions; entry/return spawns; and a table linking each DAT reference to the script.

Also state what was compiled, structurally checked and playtested. “Bug-free” is an aim, not a status established merely by generating or assembling text. A complete runnable quest needs the compiled BIN, matching DAT and a compatible server/client test.

## Architecture required for newly generated quests

- Function **0** is the entry point. Set the episode before any map designation: `set_episode` resets the floor configuration. Initialize all used floor mappings, success/failure handlers, floor handlers, initial floor and player spawn arrangements, and start required background monitors with the logical `thread` operation. Resolve its exact mnemonic through the selected compiler profile.
- Function **1** is `ret` only, by project convention. Use it for intentionally blank callbacks. Do not change existing imported quests to this numbering scheme without remapping every reference.
- Every infinite or polling loop must yield with `sync` on **every repeating execution path**. A sync somewhere in a larger loop is insufficient if a branch bypasses it. In the recovered Qedit profile, opcode 02 is named `wait_vsync`.
- Reserve **R0–R219** as the permitted general-purpose allocation range. Allocate disjoint scratch ranges or explicitly documented shared state between concurrent threads. Do not assume that range is automatically private to each thread. Account for calling conventions and float/integer register aliasing.
- Within that range, **R74–R79 have quest-board display behavior**; do not allocate them as unrelated scratch when quest-board operations are used. Preserve the register requirements of imported helpers. Registers above 219 are reserved by project policy, except explicitly documented engine/framework roles such as R253 failure and R255 success. Never blindly remap an existing quest's registers.
- For shared quest-register changes, use the compiler's verified `sync_register` operation. It propagates values; it is not an atomic transaction, lock or race-free counter increment. Define who originates transitions, guard repeated triggers, and make repeat delivery harmless.
- For a multiplayer door, synchronize the actual **switch flag on the intended floor**. A synchronized register is not a substitute for a synchronized switch. The floor-explicit operation `set_switch_flag_sync` / bundled Qedit `unlock_door2` takes floor and switch ID.
- `initial_floor` selects a floor, not XYZ coordinates. Provide valid spawn points for every supported player slot and all required return paths using appropriate DAT Player Set objects or verified script positioning.
- Registering success/failure callbacks does not complete or fail a quest. The objective logic must explicitly set the intended result state. R255=1 and R253=1 are the success/failure flags used by the guild callback mechanism. Avoid contradictory states and repeated rewards.

## Encounter readiness and progression

A monitor created during initialization must not interpret an unloaded or unstarted encounter as victory. Before checking completion, establish that the relevant floor/room is ready and the intended event chain has started. Use a documented encounter-start state, floor handler or event-driven transition.

Prefer direct event chains for deterministic waves: trigger event A; A selects room/wave 1; its completion triggers B; B completes and sets a switch or constructs a script-trigger group. A room-clear query is not a replacement for specifying which waves exist, how they start, and which of them are required.

`if_zone_clear R1, R2` consumes a consecutive input register pair: **R2=floor, R3=room**; R1 receives the result. Its opcode does not take a wave ID. Results may depend on the constructed set-event state, so preserve the readiness and completion guards and test the intended client behavior.

An event ID is not a wave number, an object group is not a switch ID, and none is automatically a script label. Always use explicit mapping tables.

For Challenge/random encounters, preserve EVT2, random-location, random-definition and weight data. The runtime seed determines the materialized encounter; the file alone does not specify one fixed enemy sequence. Do not report an unresolved dynamic event reference as a confirmed missing static event.

## Spatial requirements

- Every floor has an explicit area/type/layout/entities designation and evidence for available client assets.
- Every placement names its floor and room and gives coordinates in the correct space. Object positions are room-relative; verify room transforms before treating coordinates as world coordinates. Reuse validated source placements on the same layout or decode the layout transform; do not invent safe XYZ values.
- Include rotations and entity-specific parameters, not just the visible enemy name. Variants, child counts and difficulty can change the result of one base type.
- For each wave: define its floor, room, wave number, trigger/event ID, delay, enemy records and post-wave action sequence.
- For each door/fence: document its actual type, switch parameter and packed bits. Forest Door 0x80 puts the switch in the low byte of p4; Boss Teleporter 0x19 uses p5 for its enabling switch. There is no universal parameter layout for every door.
- Collision shape is type-dependent. Type 0x08 is a radius-based event activation; type 0x12 is a radius-based script trigger. Do not describe all invisible triggers as boxes. Other collision types need their own parameter evidence.
- Distinguish placed NPC records, enemy constructor records, runtime entity IDs and script-created NPCs. Counts of DAT enemy records are not gameplay kill totals.

## Required corrections to the supplied example

| Sample assumption | Adopted correction |
|---|---|
| `window_msg` followed by `mesend` | Pair `window_msg` with `winend` (opcode 5E); `mesend` is opcode 5C for the other message mechanism |
| `unlock 00000003` | No such generic mnemonic is established for the recovered compiler. Use floor-explicit synchronized switch opcode F82B; its Qedit name is `unlock_door2` |
| Sync R1, then unlock | Synchronizing R1 only mirrors that register. Synchronize the actual switch separately; use R1 as scratch only if ownership is safe |
| `thread 100` immediately checks room completion | Gate it on encounter readiness/start, then yield while waiting |
| `initial_floor 0` defines all spawn points | Define player-slot coordinates/rotations as well |
| `BB_Map_Designate 01, 0001, 00, 00` means variant 1 | In the recovered BYTE/WORD/BYTE/BYTE dialect it means floor 1, area 1, type 0, layout 0, entities 0 |
| R0–R219 means independent thread storage | Treat it as an allocation range and explicitly manage ownership and imported helper requirements |
| Success callback displays victory | Also define the objective transition that sets R255; callbacks do not establish the objective themselves |
| `sync` guarantees a fixed elapsed time | It yields one VM frame. Use verified time operations for real elapsed-time requirements |

The example is therefore a conceptual sketch, not a complete validated multiplayer quest. Its corrected form must be generated together with actual DAT placements and the chosen compiler profile.

## Retrieval before generation

1. Find at least one working-pattern candidate matching episode, mode and feature in `quest-library.sqlite` or `retrieval-chunks.jsonl`.
2. Read the complete relevant functions, caller/handler setup, register writes and matching DAT records. Search snippets are pointers, not sufficient context.
3. Resolve opcode numbers, aliases, operand widths, argument-stack behavior and client applicability from the source definitions and recovered compiler configuration.
4. Design a state table and entity map. Allocate every register, function label, event, room/wave and switch before writing code.
5. Generate a complete script and DAT specification. Compile using a stated toolchain and decode the result again.
6. Validate references, readiness, yield paths, spatial support, output headers, shared state and reward idempotence. Finish with in-game tests before claiming the quest is playtested.

## Output validation status

- **Draft:** proposed script and DAT plan, not compiled.
- **Assembled:** the declared compiler accepted the source; this does not establish correct gameplay.
- **Statically checked:** relevant binary/header/reference checks pass; remaining uncertainty is listed.
- **Playtested:** record the actual client build, server build, party sizes, difficulties and cases tested.

Preserve original files. Build into a separate output directory. Do not deploy to the live server just because a script assembles. When the user authorizes a deployment, first have concrete reviewed artifacts and test evidence ready.
