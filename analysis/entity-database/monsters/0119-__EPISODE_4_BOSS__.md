# Saint million

DAT ID **0x0119 / 281**, constructor **__EPISODE_4_BOSS__**.

[Definition source](../../quest-knowledge/reference/server-source/Map.cc#L3149) · [Database index](../monsters.md)

## Source-documented areas

Episode 4: Meteor Impact Site (area 0x2C, default floor 9)

Floor numbers are script slots. Resolve the quest map designation to an area before checking compatibility. Custom client patches may change constructor availability; this table describes the stored reference, not a live client test.

## Parameters and source notes

```text
Saint-Milion / Shambertin / Kondrieu. Params:
param1 = TODO (see TObjEneV00b43ca0::set_params; seems it only matters if this is zero or not)
param6 = flags (bit field):
0001 = type (0 = Saint-Milion, 1 = Shambertin; ignored if enemy is set as rare by the server, in which case
it's Kondrieu)

```

## Observed quest placements

5 records, including language duplicates. These are observations, not spawn permissions.

[All observed positions, angles, parameters and handler candidates](../observations/0119.csv)

| Quest | Floor | Room / wave | Handler candidate |
|---|---:|---|---|
| [government-ep4/q708-bb-e](../../server-catalogue/government-ep4/q708-bb-e/README.md) | 9 | 10 / 1 | — |
| [government-ep4/q708-bb-j](../../server-catalogue/government-ep4/q708-bb-j/README.md) | 9 | 10 / 1 | — |
| [team-ep4/q709-bb-e](../../server-catalogue/team-ep4/q709-bb-e/README.md) | 9 | 10 / 0 | — |
| [team-ep4/q709-bb-j](../../server-catalogue/team-ep4/q709-bb-j/README.md) | 9 | 10 / 0 | — |
| [vr-ep4/q991-bb-e](../../server-catalogue/vr-ep4/q991-bb-e/README.md) | 9 | 10 / 1 | — |
