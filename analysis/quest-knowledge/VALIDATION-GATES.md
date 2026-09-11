# Checks required before a generated quest is called ready

## Input and compiler

- Confirm Episode 1/2/4, solo/multiplayer/battle/challenge, client/server build, maximum party size, language, and exact assembler profile.
- Resolve the chosen numeric base, register-pair syntax, argument-stack syntax, comments, strings and label numbering through an actual compiler profile. `.pasm`, `.pbs` and newserv `.txt` are not interchangeable file extensions.
- Match the header episode, script episode and map-designation/item-mask header fields. Preserve or regenerate BB header fields deliberately; an unchanged instruction stream does not imply an unchanged header.

## Control flow

- Function 0 establishes all configuration and Function 1 is the project's ret-only handler.
- Every referenced label is defined or is an explicitly intentional raw-data label with the correct consuming opcode.
- Every repeating polling path passes through sync before repetition. Follow indirect calls and switch branches; do not merely search for a sync somewhere in a function.
- Monitors wait for encounter activation and relevant floor readiness before checking completion. Re-entry does not create uncontrolled duplicate monitors.
- Calls and returns are balanced and register/stack conventions are respected. Guard repeated object/NPC activation.

## Registers and multiplayer

- Each scratch range has an owner; shared variables have a writer/replication rule. Aliased float/int registers and imported helpers are accounted for.
- Keep general allocations within R0–R219 with the documented reserved-use exclusions. Framework values outside that range are explicit exceptions.
- Register synchronization and switch synchronization are distinct. Door operations target the intended floor/switch and reach the party.
- A synchronized read-modify-write increment is not assumed atomic. Test simultaneous events, deaths and completion.
- Specify how absent players, disconnected players, different floors and host changes affect monitors and objective state.

## DAT and assets

- Validate section sizes, offsets, record alignment, termination, and every event action offset before reading it. Preserve malformed source data as evidence; do not invent missing instructions from memory or decoder garbage.
- Match floor, area, map type and both variations with available client assets. Verify room coordinates and safe positions for every spawn and placement.
- Distinguish actual runtime entity IDs from table indices. Validate constructor type/parameters, child behavior, NPC label links and item parameters.
- Match each static event with its intended enemies and each completion action with an event/group/switch on the right floor. Duplicate event IDs require explicit intent.
- Verify trigger shape, radius/bounds, position, room and target. A type-8 activation targets a DAT event; type-18 targets a script label.
- For random encounters, validate EVT2 and tables 4/5 together, room ordering, weight references and runtime materialization. A fixed kill-count total cannot be inferred by counting random definitions.

## Objective, success and rewards

- State transitions have start, success and failure conditions, with a clear difference between objective completion and official quest success.
- Use the correct result flag/callback path; registering a handler alone does not invoke it.
- NPC quest-item checks distinguish a register latch from actual per-player inventory state. Verify item identity and repeat handling; do not silently equate “register set” with “item owned”.
- Item grants use supported operations, header item masks and server behavior. Reward dialogue matches the actual result. Drops depend on server metadata as well as quest bytecode.
- Guard duplicate payouts and interrupted/repeated conversations.

## Artifact and runtime checks

- Assemble, decode, compare and inspect the produced BIN. Validate the matching DAT and packed QST roundtrip if used. Keep all failures visible.
- Open/save/reopen with the actual target Qedit compiler before claiming Qedit compatibility.
- Playtest the intended route, alternate routes, two-player simultaneous triggers, maximum party size, death/revival, returning to areas, cancellation, disconnects and repeated reward conversations. Test each supported difficulty and special mode.
- Record actual evidence and unresolved cases. Never label an untested generated quest “bug-free”.

These are validation criteria. The current reference corpus is statically extracted; its presence in the library is not a pass through these generation gates.
