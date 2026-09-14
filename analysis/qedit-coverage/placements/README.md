# Monster and object saved-field mappings

[Checked fields JSON](fields.json) · [Validation results](validation.json) · [Coverage matrix](../README.md)

The supplied corpus uses 68-byte object records and 72-byte enemy/NPC records. The verification tool compares decompressed DAT records with all 527 quests' placement CSVs: 186,967 objects, 146,753 enemy/NPC records and 4,444,899 matching field comparisons.

This is consistency between preserved bytes and related decoder exports. It is not Qedit save/reopen or client verification.

## Source correspondence

Source: [Map.hh structures](../../quest-knowledge/reference/server-source/Map.hh#L162) and [Qedit main.pas](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/main.pas#L86). Offsets are relative to each placement record, not the DAT file. Multibyte fields are little-endian. Internal Delphi declarations alone do not prove the supplied executable's write behavior.

| Field | Object offset / size | Enemy/NPC offset / size | Qedit correspondence |
|---|---|---|---|
| Type | 0x00 / 2 | 0x00 / 2 | Skin; not appearance skin |
| Runtime set flags | 0x02 / 2 | 0x02 / 2 | Unknow1 |
| Runtime index | 0x04 / 2 | 0x04 / 2 | unknow2 low word |
| Record floor / children | floor 0x06 / 2 | num_children 0x06 / 2 | unknow2 high word; meaning depends on record type |
| Runtime entity ID / floor | entity_id 0x08 / 2 | floor 0x08 / 2 | object id / enemy unknow3 |
| Group / runtime entity ID | group 0x0A / 2 | entity_id 0x0A / 2 | object grp / enemy unknow4 |
| Room | 0x0C / 2 | 0x0C / 2 | map_section |
| Unknown / wave | unknown 0x0E / 2 | wave_number 0x0E / 2 | object unknow4 / enemy Unknow5 |
| Secondary wave | — | 0x10 / 2 | unknow6 low word |
| Unknown | — | 0x12 / 2 | unknow6 high word |
| Position X,Y,Z | 0x10,0x14,0x18 / 4 each | 0x14,0x18,0x1C / 4 each | Pos_X, Pos_Z, Pos_Y; Qedit names differ from serialized XYZ order |
| Angle X,Y,Z | 0x1C,0x20,0x24 / 4 each | 0x20,0x24,0x28 / 4 each | object Unknow5/unknow6/unknow7; enemy unknow7/Direction/unknow8 |
| Float parameters 1–3 | 0x28,0x2C,0x30 / 4 each | 0x2C,0x30,0x34 / 4 each | object unknow8/unknow9/Unknow10; enemy Movement_data/Unknow10/unknow11 |
| Parameters 4–5 | int32 at 0x34,0x38 | float32 at 0x38,0x3C | obj_id/Action versus Char_id/Action |
| Parameter 6 | int32 at 0x3C | int16 at 0x40 | unknow13 versus Movement_flag low word |
| Parameter 7 | — | int16 at 0x42 | Movement_flag high word |
| Runtime object pointer slot | 0x40 / 4 | 0x44 / 4 | unknow14 / unknow_flag |

The EnemySetEntry angle comment in the preserved Map.hh says 0x24, but the declaration places a 12-byte XYZ position at 0x14, so the following angle vector begins at **0x20**. That agrees with Qedit's field sequence and the 0x2C first parameter. This discrepancy is documented rather than copied as an authoritative offset. Angle/header-runtime fields are not included in the CSV comparison because the CSV does not expose them.

## Rules that must remain separate

- The containing DAT section supplies the floor used in the CSV. That is not the same evidence as the record's embedded floor field.
- Object positions are room-relative in the preserved source. Section transforms are required for world coordinates; the field-name swap does not justify swapping axes a second time.
- Parameters are type-specific. A field named Action or obj_id is not a universal script label or switch ID.
- Runtime flags, IDs and pointer slots are documented as runtime/internal by the source; they must not be repurposed based solely on their presence in the record.
- Passing byte checks does not prove area compatibility, walkability, safe spawn placement or multiplayer behavior.

Next: trace Qedit's actual load/save callers; produce one-field mutation fixtures for both record types; save/reopen them in the supplied executable and test behavior in the clean client. Those tests remain pending.
