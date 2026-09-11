# DAT spatial reference

This describes decompressed quest DAT data for the supplied BB corpus. Full raw sections and placement records are preserved in the database; unknown/runtime fields must not be silently discarded by future tooling.

## Section envelope

Each section begins with four little-endian uint32 values: type, section size including the 16-byte header, floor, and data size. Type 0 terminates the section sequence. Any remaining bytes are preserved as source evidence and are not automatically interpreted as live placements.

| Type | Payload |
|---:|---|
| 1 | Object set records, 0x44 bytes each |
| 2 | Enemy/NPC set records, 0x48 bytes each |
| 3 | Event header, EVT1 or EVT2 records, and completion-action stream |
| 4 | Random-enemy room/location tables |
| 5 | Random-enemy definitions and weighted choices |

Use the section's floor as the placement floor. Some imported records have stale embedded floor fields; keep both fields in evidence rather than quietly rewriting originals.

## Object fields

| Offset | Contents |
|---|---|
| 00–0E | Eight uint16 fields: base type, flags, runtime index, embedded floor, entity ID, group, room, unknown |
| 10 | XYZ position, three float32 values |
| 1C | XYZ angles, three 32-bit values |
| 28 | p1–p3, three float32 values |
| 34 | p4–p6, three int32 values |
| 40 | Unused/runtime pointer field |

Object parameter semantics come from the actual object type. Raw angles often represent 16-bit turn values carried in 32-bit fields. Preserve source values rather than converting arbitrary degrees without a verified rule.

## Enemy/NPC fields

| Offset | Contents |
|---|---|
| 00–12 | Ten uint16 fields: base type, flags, runtime index, child count, embedded floor, entity ID, room, wave, second wave field, unknown |
| 14 | XYZ position, three float32 values |
| 20 | XYZ angles, three 32-bit values |
| 2C | p1–p5, five float32 values |
| 40 | p6–p7, two int16 values |
| 44 | Unused/runtime pointer field |

The source header's angle-offset comment contains an inconsistency: the struct layout puts enemy angles at 0x20, after the three floats at 0x14, and parameters begin at 0x2C. The database parser uses the actual contiguous layout and preserves raw records.

An enemy's base type and parameters select a constructor/variant. A child-count value of zero can invoke a constructor default; it does not universally mean zero children. NPCs also occupy this section type.

## Events

The event payload header has action-stream offset, entry-table offset, count, and four format bytes. Format zero uses 0x14-byte EVT1 records. `evt2` uses 0x18-byte records. These offsets are relative to the event payload, not the outer DAT file.

EVT1 records identify event, flags/type, room, wave, delay in frames and action offset. Enemy matching uses floor/room/wave, while activation uses the event ID. Duplicate event IDs are possible and can trigger multiple records; database consumers must not assume `(floor,event_id)` identifies exactly one row.

EVT2 adds minimum/maximum delay, minimum/maximum enemies and a maximum wave count. Random sections supply eligible spawn positions, enemy definitions and weights. The RNG seed and runtime materialization are required to produce one concrete sequence.

| Action byte | Arguments | Meaning |
|---|---|---|
| 00 | none | nop |
| 01 | none | stop |
| 08 | room:uint16, group:uint16 | Construct object group |
| 09 | room:uint16, wave:uint16 | Construct enemy wave |
| 0A | switch:uint16 | Set switch |
| 0B | switch:uint16 | Clear switch |
| 0C | event:uint32 | Trigger event |
| 0D | room:uint16, wave:uint16 | Construct enemies, then stop |

Action offsets in each event record are relative to the action stream. DAT actions and BIN script opcodes are separate instruction sets.

## Random tables

Type 4 contains a room table and location entries. Each room supplies an ID, location count and byte offset into the location-entry table. Room IDs should be ordered as required by the loader. Locations carry position, angles and two unknown uint16 values. The library indexes these records without pretending that all positions will be used in one run.

Type 5 has offsets/counts for 0x20-byte definitions and four-byte weights. Definitions hold five float parameters, **p7 then p6**, entry index, an unknown field and child-count bounds. A weight row contains base-type index, definition index, weight and an unknown byte. Base-type index is not automatically the final enemy base-type ID.

## Coordinate evidence

The client and Qedit asset file inventories are in `asset-index.json`; they are path/size indexes, not copied complete geometry. The client SetDataTable files are preserved. Before new placements are generated, obtain the selected layout's room transforms or reuse positions from a verified matching layout. Knowing an area name and a Room ID alone is insufficient to invent safe positions.
