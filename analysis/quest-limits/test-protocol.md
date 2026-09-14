# Native limits test protocol

Status: planned; **no results fabricated or inferred from decoding**.

## Record the environment

Record client, QEdit, compiler and server versions/hashes; episode, difficulty, floor/map variants; party size; quest artifact hashes; test steps and expected behavior. Keep original fixtures and outputs.

## Establish a working baseline

Use a small encounter already verified in the exact environment. Save, close, reopen and compare fields/bytes in QEdit. Compile/decompile using the selected dialect. Run the encounter through clear, door opening and quest completion.

## Vary one dimension

- Increase simultaneous ordinary enemy placements in a single wave.
- Increase sequential waves while keeping simultaneous enemy count fixed.
- Increase rooms and total placements while keeping active load fixed.
- Repeat separately for child-spawning enemies, NPCs and objects.
- Test random EVT2 generation separately from fixed placements.
- Test boss setups individually with their required arena and script flow.

Increase workloads gradually. At the first failure, preserve logs and artifacts, repeat, and narrow the boundary. A single crash does not establish a global limit; classify compile errors, serialization errors, activation bugs, pool exhaustion and performance separately. A successful trial gives a tested workload, not the true maximum.

## Multiplayer and completion

Repeat with four players. Check synchronization, permitted late joins, disconnects, wipes, retries, floor transitions and completion. Record each player's observed enemies and clear/door state. Mark unsupported join behavior explicitly.

## Result record

Each finding needs: measured dimension, workload, environment hashes, fixture links, expected/actual result, repeats, solo/party scope, evidence, and classification (tested recommendation or verified boundary). Until then, the constraint remains unknown.
