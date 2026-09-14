# NPC appearance writeback: first source trace

Status: source-traced editor path; not executable-matched, compiled or client-tested.

The NPC Builder edits a script data block. Its selected data label is not the DAT NPC type, player class ID or NPC instance ID.

| Step | Source evidence | Established behavior |
|---|---|---|
| Internal record | [NPCBuild.pas:10](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/NPCBuild.pas#L10) | TNPCDATA declares name, name colour, extra_model, section/class/flags, costume/skin/face/head/hair, RGB components, proportions and a trailing UNINAME buffer. |
| Start editor | [FScrypt.pas:1071](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/FScrypt.pas#L1071) | Button10Click clears the record, sets name_colour to 0xFFFFFFFF and proportions to 0.333 / 0.5 before reading existing data. |
| Read existing block | [FScrypt.pas:1086](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/FScrypt.pas#L1086) | Parses HEX lines into the record up to SizeOf(NPCDATA)-36. Reads a separate extended name and may interpret it as wide characters. |
| Accept changes | [FScrypt.pas:1145](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/FScrypt.pas#L1145) | After ShowModal returns 1, replaces the existing data lines, constructs a label from SpinEdit1.Value and registers it with AddDataRef. |
| Emit script data | [FScrypt.pas:1160](https://github.com/schthack/qedit/blob/2af5d144485b58ba28b57d98d2daa1a6b141ff4f/FScrypt.pas#L1160) | Writes record bytes as hexadecimal text lines. This is an intermediate script representation, not direct proof of final BIN layout. |

## Field groups to verify next

- `char_name`, `UNINAME`: ANSI versus extended-name encoding, prefixes, terminators, exact lengths and truncation.
- `name_color`, checksum and flags: editor updates, byte order and client interpretation.
- `extra_model`, `section_id`, `char_class`: independent namespaces and mode-dependent restrictions.
- `costume`, `skin`, `face`, `head`, `hair`: WORD declarations; valid selectors depend on class/mode.
- `hair_red`, `hair_green`, `hair_blue`: WORD storage does not establish accepted channel ranges.
- `proportion_x`, `proportion_y`: Single declarations; editor defaults do not establish valid client bounds.

## Required fixture checks

1. Establish the supplied executable's record size, alignment and matching save caller. The source comments use historical absolute-looking offsets; they are not automatically BIN offsets.
2. Verify byte continuity across the first 16-byte output line and the following loop. The source reuses the `for` loop variable `x`; do not assume its post-loop value without checking the compiler/executable behavior.
3. Save/reopen a new block and an existing block, including empty, ASCII and non-ASCII names.
4. Change one appearance field at a time and compare emitted HEX data and final assembled bytes.
5. Trace how the resulting label is referenced by quest instructions and applied to a placed NPC; then test the clean client.

The archived source record and controls are in [record declarations](record-declarations.json) and the [NPC Builder form inventory](forms/NPCBuild.md). No universal appearance layout or valid quest payload is certified by this trace alone.
