# NPC appearance fields: source and byte verification

[Coverage matrix](../README.md) · [Field offsets JSON](fields.json) · [Observed blocks](observed-blocks.json) · [Validation](validation.json)

Offsets below are relative to a **112-byte PlayerVisualConfigV4 block**, not to the BIN file or DAT NPC placement. They follow the preserved [PlayerSubordinates.hh](../../entity-database/reference/PlayerSubordinates.hh) definition: a 16-byte prefix, a 64-byte shared visual structure, then a 32-byte marked UTF-16 name.

## Field layout

| Offset | Bytes | BB field | Qedit source name / control |
|---|---:|---|---|
| 0x00 | 16 | guild_card_number prefix | char_name; its meaning differs from the V4 definition |
| 0x10 | 8 | unknown_a2 | unused1 / unused2 |
| 0x18 | 4 | name_color (ARGB) | name_color / Panel3Click |
| 0x1C | 1 | extra_model | extra_model / special-mode buttons |
| 0x1D | 15 | reserved / server-specific extensions | unused array; do not reinterpret newserv extensions as standard Sega behavior |
| 0x2C | 4 | name_color_checksum | same name |
| 0x30 | 1 | section_id | same name |
| 0x31 | 1 | char_class | same name; separate from DAT NPC type |
| 0x32 | 1 | validation_flags | v2_flags; naming and preview usage differ |
| 0x33 | 1 | version | same name |
| 0x34 | 4 | class_flags | v1_flags |
| 0x38 | 2 | costume | costume |
| 0x3A | 2 | skin | skin |
| 0x3C | 2 | face | face |
| 0x3E | 2 | head | head |
| 0x40 | 2 | hair | hair |
| 0x42 | 2 | hair_r | hair_red / Panel2Click |
| 0x44 | 2 | hair_g | hair_green / Panel2Click |
| 0x46 | 2 | hair_b | hair_blue / Panel2Click |
| 0x48 | 4 | proportion_x | TrackBar1Change |
| 0x4C | 4 | proportion_y | TrackBar2Change |
| 0x50 | 32 | marked UTF-16 name | UNINAME is declared as 36 bytes in Qedit source; equivalence requires testing |

All multibyte numeric BB fields here are little-endian; proportions are float32. These are source-defined BB offsets, not a certification of the supplied Qedit executable's emitted layout.

## Confirmed editor-source behavior

- **Hair colour:** [Panel2Click](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/NPCBuild.pas#L632) extracts three 8-bit channels and stores them in WORD fields. It changes the complete RGB colour 0x000000 to 0x010101 and 0xFFFFFF to 0xFEFEFE. Individual channels can still be 0 or 255 for other colours. This picker rule is not proof that the client rejects pure black or white.
- **Name colour:** Panel3Click swaps the dialog's colour byte order and forces alpha to 0xFF. See the [handler inventory](../forms/NPCBuild.md).
- **Proportions:** TrackBar1Change and TrackBar2Change store slider Position / 100. Both DFM resources explicitly declare Max=100. The lower bound is not explicitly declared there and should be checked in the executable/component defaults before claiming a verified range.
- **Selectors:** [Native selector tables](../../entity-database/qedit/native-builder/README.md) contain the class-dependent hair, face, head, skin and costume ranges. The preview uses skin for android body selection and costume for non-android body selection; those are separate settings.
- **Name entry:** [Edit1Change](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/NPCBuild.pas#L831) converts edit text to an ANSI string, copies it into the 16-byte char_name buffer, writes a tab/J marker into UNINAME, and copies the first 13 ANSI bytes into alternate positions. This is not a general Unicode conversion. The DFM declares MaxLength=15; byte length after conversion still needs non-ASCII testing.

## Important layout differences

Qedit's TNPCDATA declaration contains an 80-byte prefix and a 36-byte trailing buffer under ordinary Delphi scalar sizing. That suggests 116 bytes, while the preserved BB structure is explicitly 112 bytes. The save routine emits SizeOf(NPCDATA), so **do not trim four bytes or assume the extra bytes belong to the next script label** without verifying the executable, assembler and label boundaries.

Qedit also uses v2_flags bit 1 to choose its special-model preview, while the server's corresponding field is named validation_flags. These names and uses must remain separately documented; a preview selection alone does not establish the correct BB quest configuration.

## Existing-byte checks

The accompanying tool reads the 48 previously recognized visual blocks directly from decompressed quest BINs. It resolves the script-relative data address using the BIN code offset, decodes the numeric fields and compares available integer annotations with the saved disassembly. Raw 112-byte blocks and exact source addresses are retained for review. This verifies byte/annotation consistency, not Qedit writing or runtime appearance.

## Save/reopen fixture checklist

1. Preserve a baseline quest and record its hashes, Qedit executable hash and client build.
2. Select a known working visual block and record its label, boundaries and NPC application instructions.
3. Change one selector or channel; save, reopen and compare the decompressed bytes and neighboring labels.
4. Test hair black/white, mixed endpoint channels, name colour, slider endpoints, and class/special-model transitions separately.
5. Test empty, 13-character, 15-character and non-ASCII names; inspect both name regions and terminators.
6. Verify Qedit's emitted record size and byte continuity, then client appearance and multiplayer behavior.

**Pending:** native Qedit save/reopen and client tests. The current automation surface cannot operate the native Windows editor; none of those tests have been simulated or marked passed.
