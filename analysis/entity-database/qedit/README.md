# Qedit authoring reference

Qedit's supplied definitions are the primary reference here for editor labels, placement types, presets and area menus. Client behavior still needs separate verification. The supplied client is clean according to the owner; its folder name does not override that information.

## Browse the data

- [Native NPC Builder controls and per-class appearance IDs](native-builder/README.md), traced directly from Qedit's executable.

- [Quest entity IDs and ordered field labels](entity-fields.md), also [JSON](entity-fields.json).
- [Add-monster/NPC placement presets](placement-presets.json), retaining repeated fields in order.
- [Bundled and external area lists](area-lists.json) and [their differences](area-differences.json).
- [Appearance examples from existing quest visual blocks](appearance-examples.json).
- [Client appearance input hashes](client-appearance-inputs.json).
- [Validation results](validation.json).

## Keep the appearance systems separate

| Namespace | HUmar example | RAmar example |
|---|---:|---:|
| Player class selector | 0 | 3 |
| Default quest NPC DAT type | 33 / 0x21 (Ash) | 36 / 0x24 (Bernie) |

Qedit's DAT **Skin** field selects the placement type. It must not be equated to the skin-color field in a custom visual configuration. A quest character ID identifies the instance, while the interaction function identifies code to run. The stage NPC type 51 (0x33) is another mechanism with special fields; it is not a synonym for player class 51.

The supplied Qedit language file includes **NPC Builder**, **Skin**, **Head**, **Face**, **Hair**, **Costume**, and **Section id** controls. The subsequent [native code trace](native-builder/README.md) establishes the control-to-form-memory mappings and per-class selector limits. Those form offsets must not be confused with serialized quest offsets.

## Evidence and limitations

The [supplied configuration guide](../../quest-knowledge/reference/qedit-notes/Config_files.txt) describes npcname.ini as field/name definitions, monsters.txt as placement defaults, and FloorSet.ini as area menus. Bundled and external lists differ. Both exclude Hildebear type 64 from Forest 1 and include it in Forest 2. Do not merge the lists silently or equate menu availability with a tested client constructor.

Appearance examples are decoded by the supporting newserv disassembler and remain labelled accordingly. They are not native Qedit roundtrip tests. The NPC Builder's control-to-memory mapping is now traced; serialization, complete client appearance decoding, and the hair/face/costume gallery remain unfinished. Native application controls are unavailable in this session, so no interaction with Qedit's actual dialog is claimed.

The next verification work is to trace those mappings in Qedit, check the client lookup tables, and compare controlled appearance configurations against the resulting visuals. This reference does not claim 100% appearance coverage.
