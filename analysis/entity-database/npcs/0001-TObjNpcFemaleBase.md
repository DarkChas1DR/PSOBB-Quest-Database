# Unknown 1

DAT ID **0x0001 / 1**, constructor **TObjNpcFemaleBase**.

[Definition source](../../quest-knowledge/reference/server-source/Map.cc#L2533) · [Database index](../npcs.md)

## Source-documented areas

Episode 1: Pioneer 2 (area 0x00, default floor 0); Episode 4: Pioneer 2 (area 0x2D, default floor 0)

Floor numbers are script slots. Resolve the quest map designation to an area before checking compatibility. Custom client patches may change constructor availability; this table describes the stored reference, not a live client test.

## Parameters and source notes

```text
This is newserv's canonical definition of map enemy and NPC types.
Enemies and NPCs take a similar arguments structure as objects: objects use ObjectSetEntry, enemies use
EnemySetEntry. Like objects, some IDs are reused across game versions or areas, so the same enemy type can
generate a completely different entity on different game versions. This is why some enemies have multiple
entries with the same type and different names.
Some enemies have params that the game's code references, but only in places where their effects can't be seen
(for example, in normally-unused debug menus). These may have been used to test frame-by-frame animations for
some enemies; see TObjEneMe3Shinowa_v76 for an example of this usage. The enemies with params like this are:
- TObjEneMe3ShinowaReal (param3, param4)
- TObjEneDf2Bringer (param1, param2)
- TObjEneRe7Berura (param1, param2)
- TBoss1Dragon (param1, param2)
- TBoss5Gryphon (param1, param2)
- TBoss2DeRolLe (param1, param2, param3)
- TBoss8Dragon (param1, param2)
- TObjEneBm5GibonU (param4, param5; these params also have non-debug meanings)
- TObjEneMorfos (oaram1, param2; these params also have non-debug meanings)
NPCs. Params:
param1 = action parameter (depends on param6; see below)
param2 = visibility register number (if this is > 0, the NPC will only be visible when this register is
nonzero; if this is >= 1000, the effective register is param2 - 1000 and register values for both param2 and
param3 are read from the free play script environment instead of the quest script environment)
param3 = hide override register number (if this is > 0, the NPC will not be visible when this register is
nonzero, regardless of the state of the register specified by param2; if this is >= 1000, the effective
register is param3 - 1000 and register values for both param2 and param3 are read from the free play script
environment instead of the quest script environment)
param4 = object number ("character ID" in qedit; if this is outside the range [100, 999], the quest label in
param5 is called in the free play script instead of the quest script)
param5 = quest label to call when interacted with (if zero, NPC does nothing upon interaction)
param6 = specifies what NPC does when idle:
0 = stand still (param1 is ignored)
1 = walk around randomly (param1 = max walk distance from home)
2 = TODO (Ep3 only; appears to be unused)
3 = TODO (Ep3 only; appears to be unused)
TODO: setting param4 to 0 changes something else about the NPC; figure out what this does (see
TObjNpcBase_v57_set_config_from_params)
Woman with red hair and purple outfit
```

## Observed quest placements

6 records, including language duplicates. These are observations, not spawn permissions.

[All observed positions, angles, parameters and handler candidates](../observations/0001.csv)

| Quest | Floor | Room / wave | Handler candidate |
|---|---:|---|---|
| [retrieval-ep1/q138-bb-e](../../server-catalogue/retrieval-ep1/q138-bb-e/README.md) | 0 | 20 / 0 | [label0068](../../server-catalogue/retrieval-ep1/q138-bb-e/script.txt#L1092) |
| [retrieval-ep1/q138-bb-j](../../server-catalogue/retrieval-ep1/q138-bb-j/README.md) | 0 | 20 / 0 | [label0068](../../server-catalogue/retrieval-ep1/q138-bb-j/script.txt#L1086) |
| [seasonal-ep1/q124-bb-e](../../server-catalogue/seasonal-ep1/q124-bb-e/README.md) | 0 | 20 / 0 | [label0168](../../server-catalogue/seasonal-ep1/q124-bb-e/script.txt#L1878) |
| [seasonal-ep1/q124-bb-j](../../server-catalogue/seasonal-ep1/q124-bb-j/README.md) | 0 | 20 / 0 | [label0168](../../server-catalogue/seasonal-ep1/q124-bb-j/script.txt#L1880) |
| [solo-story-ep1/q009-bb-e](../../server-catalogue/solo-story-ep1/q009-bb-e/README.md) | 0 | 20 / 0 | [label0190](../../server-catalogue/solo-story-ep1/q009-bb-e/script.txt#L298) |
| [solo-story-ep1/q009-bb-j](../../server-catalogue/solo-story-ep1/q009-bb-j/README.md) | 0 | 20 / 0 | [label0190](../../server-catalogue/solo-story-ep1/q009-bb-j/script.txt#L298) |
