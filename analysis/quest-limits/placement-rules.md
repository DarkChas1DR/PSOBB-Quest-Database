# Placement requirements for quest authoring

[Limits reference](README.md)

## Select the environment first

Choose episode and difficulty mode, then a floor slot, area ID and exact layout/entity variations from the [floor database](../floor-database/README.md). Store these separately. Select a room/section from the matching [geometry](../floor-database/geometry/README.md), retaining its coordinate convention and transform evidence. A numbered section marker is not a verified room boundary or safe spawning polygon.

## Required authoring records

| Record | Required information |
|---|---|
| NPC | DAT type; separate visual class/extra_model and appearance fields; floor; map variant; room; XYZ; raw facing/angles; position convention; interaction function; dialogue and activation conditions |
| Monster | DAT type; variant parameters and child-count meaning; floor/map/room; wave and second wave field; XYZ/angles; compatibility evidence |
| Wave | Floor/room/wave identity; matching placements; event ID(s); activation source; delay; clear actions; next-event links; expected child/random expansion, or unknown |
| Object | Type; floor/map/room; XYZ/angles; type-specific parameters; applicable switch/group/function links |
| Boss encounter | Boss type and supported episode/arena; exact map setup; script and event dependencies; entry/exit behavior; defeat detection; completion and multiplayer evidence |

For each NPC, show its actual floor, map variant and room beside the appearance preview. Do not infer a DAT type from a player class ID. For each wave, show placed monster records, child/random expansion if known, and estimated simultaneous runtime count only when supported. Keep NPC and unclassified records separate.

## Checks before export

1. Resolve every floor/map/room reference and script function against the chosen compiler dialect.
2. Validate field encodings without interpreting their ranges as gameplay budgets.
3. Trace event activation and clear actions. Preserve intentional duplicate event IDs and flag unexplained duplicates for review.
4. Match wave placements by floor, room and wave. Flag orphans for review; scripts may deliberately construct them directly.
5. Trace doors and switches using each object's documented semantics. Do not assume every door shares one generic unlock opcode.
6. Inspect polling loops for yielding and multiplayer state changes for the appropriate synchronization mechanism.
7. Preserve unknown/raw fields and distinguish local coordinates from transformed coordinates.
8. Report compatibility and runtime capacity as unknown wherever evidence is missing.

## Boss selector policy

Offer a boss as a buildable preset only after a complete encounter configuration has been reproduced. Other bosses may be browsed as research entries with missing requirements listed. Replacing an ordinary monster with a boss ID does not establish a working boss encounter.
