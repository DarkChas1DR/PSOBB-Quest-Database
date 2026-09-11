# Special NPC appearances and IDs

[Appearance gallery](README.md) · [Machine-readable special IDs](special-characters.json)

Sonic, Knuckles and Tails are present in Qedit's NPC Builder. NiGHTS is present through an area-specific stage NPC selector. Eggman remains unverified.

## NPC Builder special models

These numbers are **`extra_model` appearance selectors**, not DAT NPC types or player class IDs. Qedit's preview loader requires `v2_flags & 2` to be nonzero. Its forward and backward mode buttons set different flag values (11 and 2 respectively); do not treat those whole bytes as interchangeable client configuration without validation.

| Character | Qedit label | extra_model decimal / hex | Qedit asset prefix |
|---|---|---|---|
| GM | GM | 0 / 0x00 | plY |
| Rico | Rico | 1 / 0x01 | plX |
| Sonic | Sonic | 2 / 0x02 | plW |
| Knuckles | Knux | 3 / 0x03 | plV |
| Tails | Tails | 4 / 0x04 | plU |
| Flowen | Flowen | 5 / 0x05 | plT |
| Elly | Elly | 6 / 0x06 | plS |

The preview loads `<prefix>bdy00.nj`, `<prefix>hed00.nj` and `<prefix>tex.afs`. Flowen and Elly also load `<prefix>hai00.nj`. This establishes Qedit's asset lookup and selector meaning; these entries have not been client-playtested here. The extracted preview archive does not supply named screenshots of all these special models, so their visual gallery remains incomplete.

Source: [NPCBuild.pas selector names](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/NPCBuild.pas#L164), [model loading](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/NPCBuild.pas#L332), and [mode buttons](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/NPCBuild.pas#L847).

## NiGHTS

| Appearance | DAT NPC type | Area ID | Qedit selector field | Selector value |
|---|---|---|---|---|
| Nights sit | 51 / 0x0033 | 34 / 0x22: Episode 2 Seaside (night) | TMonster.unknow7 | 7 / 0x07 |
| Nights Fly | 51 / 0x0033 | 34 / 0x22: Episode 2 Seaside (night) | TMonster.unknow7 | 8 / 0x08 |

The area is the designated map area, not an unconditional quest floor slot. These selectors cannot be applied indiscriminately on other areas: the same values select other models there. [Stage NPC parameters](../npcs/0033-TObjNpcEnemy.md) document the separate placement behavior. Position, room, facing and interaction fields must still be supplied for a quest.

Source: [NPC51Name area table](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/MyConst.pas#L54) and [type 51 model selection](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/Unit1.pas#L2317). This is source verification, not a live-client spawn test. A NiGHTS preview has not yet been added.

## Eggman / Robotnik

No verified Eggman or Robotnik ID was found in the inspected Qedit Pascal definitions or its seven-entry special-model selector. This does not prove that no compatible model exists elsewhere. The database stores a null ID and an unresolved status; no other character's ID is substituted.

## Hair, face, body and colours

[The class selector reference](../qedit/native-builder/README.md) and [all recorded selector IDs](../qedit/native-builder/appearance-ids.json) cover the 12 player visual classes and their Qedit ranges for hair, face, head, skin and costume. Hair RGB, name colour and body proportions are separate fields, not one universal body-colour ID. A DAT NPC type such as HUmar/Ash `0x0021` is not visual class HUmar `0`.

The gallery provides fixed NPC previews. It is not yet an exhaustive picture of every hair/face/costume/colour combination. Appearance ranges are editor evidence; runtime restrictions and final quest serialization still require validation. See [observed quest appearance blocks](../npc-visual-blocks.json) for concrete recorded configurations.
