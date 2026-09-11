# Qedit NPC Builder: native appearance selectors

Extracted from the supplied Qedit1.exe, using its TFORM20 resource, Delphi method metadata and x86 handlers. This independently establishes the editor's selector tables; it does not establish what every model looks like.

[Qedit reference](../README.md) · [Exact IDs as JSON](appearance-ids.json) · [Executable provenance](provenance.json)

## Per-class table counts

These are visual class selectors inside NPC Builder, **not quest DAT NPC type IDs**. For positive count N the button wraps through IDs 0–N−1. Zero marks an absent option in this table, not a selectable ID range. The refresh code also resets/disables fields for some classes or special models.

| Visual class ID | Name | Skin | Face | Costume | Hair | Head |
|---|---|---:|---:|---:|---:|---:|
| 0 | HUmar | 4 | 5 | 18 | 10 | 1 |
| 1 | HUnewearl | 4 | 5 | 18 | 10 | 1 |
| 2 | HUcast | 25 | 0 | 0 | 0 | 5 |
| 3 | RAmar | 4 | 5 | 18 | 10 | 1 |
| 4 | RAcast | 25 | 0 | 0 | 0 | 5 |
| 5 | RAcaseal | 25 | 0 | 0 | 0 | 5 |
| 6 | FOmarl | 4 | 5 | 18 | 10 | 1 |
| 7 | FOnewm | 4 | 5 | 18 | 10 | 1 |
| 8 | FOnewearl | 4 | 5 | 18 | 10 | 1 |
| 9 | HUcaseal | 25 | 0 | 0 | 0 | 5 |
| 10 | FOmar | 4 | 5 | 18 | 10 | 1 |
| 11 | RAmarl | 4 | 5 | 18 | 10 | 1 |

## Control-to-field trace

Offsets below are relative to the Qedit form instance in memory. They are **not BIN/DAT file offsets**. The layout resembles the known shared visual structure, but its load/save connection remains to be traced.

| Control handlers | Field | Form offset | Evidence |
|---|---|---|---|
| Button9 / Button10 | Visual class | 0x505, byte | [Increment wraps after 11](Button9Click.asm.txt) |
| Button3 / Button4 | Skin | 0x50E, word | [Handler](Button3Click.asm.txt) |
| Button5 / Button6 | Face | 0x510, word | [Handler](Button5Click.asm.txt) |
| Button7 / Button8 | Costume | 0x50C, word | [Handler](Button7Click.asm.txt) |
| Button2 / Button1 | Hair | 0x514, word | [Handler](Button1Click.asm.txt) |
| Button13 / Button14 | Head | 0x512, word | [Handler](Button13Click.asm.txt) |
| Panel2 | Color split into three channels | 0x516, 0x518, 0x51A, words | [Handler](Panel2Click.asm.txt); consistent with hair RGB, save mapping pending |
| Panel3 | ARGB color | 0x4EC, dword | [Handler](Panel3Click.asm.txt); consistent with name color, not body color |
| TrackBar1 / TrackBar2 | Two float proportions | 0x51C, 0x520 | [First slider](TrackBar1Change.asm.txt) / [second](TrackBar2Change.asm.txt) |

## Findings that prevent wrong assumptions

- The face button uses the table at 0xA2B5D8 to wrap the face value, but uses 0xA2B5CC (the skin table) in the displayed denominator. The refresh routine also uses the skin table in that caption. This is a static inconsistency; runtime display has not been tested.
- The saved form contains design-time captions such as Hair 1/9, while the actual hair limit table contains 10 for human/newman classes. Design-time captions are not reliable limits.
- The extracted special-model selector contains seven names: GM, Rico, Sonic, Knux, Tails, Flowen, Elly. This is the editor's list, not proof that these are all BB NPC models. It differs from the broader newserv list.
- The confirmed hair/face/costume counts agree with the earlier supporting limits for the ordinary classes. Head uses a count of 1 for human/newman classes here, whereas the supporting normalization table forces their head value to zero; both lead to head 0, but the evidence remains distinct.

## What is not yet verified

Exact serialization offsets and the quest label receiving this form's data; every rendered face/hair/costume/skin appearance; class-specific special-model constraints in the client; complete resource-to-ID mapping. The OK handler sets a result flag and closes the modal dialog, so the actual writeback must be followed in its caller rather than assumed to occur in that button.

[Refresh routine](refresh.asm.txt) · [OK handler](Button15Click.asm.txt) · [Method addresses](npc-builder-methods.json) · [Raw limit tables](appearance-limit-tables.json)
