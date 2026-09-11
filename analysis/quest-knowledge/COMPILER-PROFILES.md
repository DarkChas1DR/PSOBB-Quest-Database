# Compiler and opcode profiles

## Available evidence

The supplied main editor identifies itself as Quest Editor v2.0c Public. Its recovered configuration is saved under `reference/qedit-config/`; external floor/interface overrides are under `reference/qedit-external/`. The nested Qedit executable is a separate apparently packed build and has not been unpacked.

The analysis tool is newserv build `1f7faff9+`. Its source snapshots and the separately supplied `Tools/NewServSource/src` sources are retained separately. Source availability does not prove the running server was built from that exact checkout. No standalone `.pbs` compiler specification has been identified; do not claim `.pbs` compatibility without establishing its compiler and grammar.

## Important aliases

| Opcode | Newserv name | Recovered Qedit name | Note |
|---|---|---|---|
| 02 | sync | wait_vsync | Yield a frame |
| 04 | thread | unknown04 | Profile mismatch; do not invent a supported mnemonic |
| B1 | thread_stg | new_thread | A separately numbered thread opcode; do not replace 04 by B1 solely because names sound similar |
| F8BC | set_episode | set_epiII | 0/1/2 = Episodes 1/2/4; resets map configuration |
| F951 | bb_map_designate | BB_Map_Designate | Five BYTEs versus BYTE/WORD/BYTE/BYTE presentation |
| 88 | if_zone_clear | if_zone_clear | Result register plus base of floor/room register pair |
| EF | sync_register2 | sync_register | BB argument-stack form |
| D9 | sync_register | sync_leti | Bundled Qedit config tags this older entry DC; do not select it by name without target checking |
| 90 | switch_on | unlock_door1 | Local switch change; not multiplayer synchronization |
| F82B | set_switch_flag_sync | unlock_door2 | Floor, switch; synchronized operation |
| 5A | window_msg | window_msg | Window text |
| 5E | window_msg_end | winend | Matching window-message end |
| 5C | message_end | mesend | Different message end opcode |

The complete raw definitions are in `opcode-reference.json` and `qedit-opcode-dialect.json`. The opcode reference retains source/version flags. It is an extracted index, not a replacement for reading the source comments around a complex operation.

## Operand packing

For F951 the actual payload is five bytes:

```text
floor, area, type, layout_variation, entities_variation
```

The archived Qedit definition groups the area and type into a little-endian WORD:

```text
floor, area + (type << 8), layout_variation, entities_variation
```

`01, 0001, 00, 00` consequently means floor 1, area 1, type 0, layout 0, entities 0. All generated source should explicitly state its numeric base and compiler formatting; the same printed number can be read differently by different assemblers.

## Assembly evidence

All 527 server quest scripts decoded and assembled with newserv. 376 rebuilt files are byte-identical after decompression. Another 143 differ only by alignment padding and header size/offset fields. Eight have additional header changes; their code and label tables still survive, with alignment accounted for. Rebuilding those eight without checking BB floor assignments/item masks could change behavior even though their instruction streams are preserved.

None of these checks is a live Qedit text-import/compile test. `script.txt` files in the catalogue use newserv assembly with directives, explicit labels and argument annotations. They must not be relabelled `.pasm` and called verified Qedit source.

The native editor cannot currently be operated through this task's enabled native-app controls. A later Qedit validation can use an available supported control path or a user-run import/save check. This does not block bytecode analysis and newserv validation.
