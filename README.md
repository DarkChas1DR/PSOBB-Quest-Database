# PSOBB Quest Database & Interactive Developer Toolkit

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live%20Web%20Viewer-00f0ff?style=for-the-badge&logo=github)](https://darkchas1dr.github.io/PSOBB-Quest-Database/)
[![Database](https://img.shields.io/badge/SQLite%20Master-21%20Tables%20%7C%20121%2C176%20Rows-10b981?style=for-the-badge&logo=sqlite)](psobb_master_database.sqlite)
[![Documentation](https://img.shields.io/badge/Technical%20Spec-PSOBB__MASTER__DATABASE.md-f59e0b?style=for-the-badge&logo=markdown)](PSOBB_MASTER_DATABASE.md)

An exhaustive, verified relational data warehouse and interactive development suite for **Phantasy Star Online Blue Burst (PSOBB)** quest authoring, bytecode assembly, monster parameter tuning, item creation hex synthesis, and spatial wave event sequencing.

---

## 🌐 [Open Live Interactive Web Database](https://darkchas1dr.github.io/PSOBB-Quest-Database/)

Explore the complete dataset online with no installation required via GitHub Pages:
- **[⚡ Interactive Web Application](https://darkchas1dr.github.io/PSOBB-Quest-Database/)**
- 📜 **Opcode Explorer**: Search all 518 opcodes by hex (`0x002c`), name (`p_dead_v`), or category, with 1-click **Copy Assembly** buttons.
- ⚔️ **Item Creation Code Builder**: Dynamic calculator for `item_create1` / `item_create2` calculating exact `R200..R211` register presets for weapons (grinds, % attributes), Mags (DEF/POW/DEX/MIND), units, and disks.
- 🚩 **Quest Flag Safety Checker**: Test any flag ID (0–1023) to verify if it is **Safe for Custom Quests** or **Sega Reserved** (prevents breaking Pioneer 2 teleporters, client timers, and story state).
- 👾 **Enemies & Rare Spawns**: All 64 monster parameter schemas with rare spawn trigger rates (1/512 Hildeblue, Pouilly Slime division logic, Kondrieu, Saint-Milion), pack leader flags, and hive caps.
- 📦 **Object Parameter Schemas**: 359 interactive object schemas across 306 objects (`param1..param6`, angle masks, area applicability).
- 👤 **NPCs & Hero Models**: Special player models (Sonic, Knuckles, Tails, Rico, Flowen, Elly, Momoka, Irene), Stage NPCs (NiGHTS, Chao), and 62 standard NPC presets.
- 🎥 **Camera & Cutscenes**: Opcode schemas for `cam_data`, `cam_mode`, fleti camera modes, coordinate vectors, and cutscene starter recipes.
- ✨ **Particle Effects**: Particle IDs (`0x0000..0x0011` / `TObjParticle`), emission radii, and draw distance flags.
- 🌊 **Wave Event Actions**: Binary DAT wave trigger sequences, delay frames, and room clearing events.
- 💬 **Quest Dialogue Strings**: Multi-lingual dialogue strings with Sega colour format tags decoded.
- 🎲 **Minigame Mechanics**: Gallon's Shop roulette math, Pioneer 2 soccer ball physics, and Challenge Mode death counter clocks.
- 💻 **In-Browser WebAssembly SQL Console**: Execute arbitrary SQLite queries directly against the 121,176-row database in your browser using WebAssembly `sql.js` with instant CSV export!

---

## 📊 Master Database Summary (21 Tables, 121,176 Records)

All quest data is stored relationally in `psobb_master_database.sqlite` (19.3 MB) and exported in `psobb_master_database.json` (46.3 MB):

| Table Name | Row Count | Primary Contents |
|:---|---:|:---|
| `quests` | 527 | Official Sega quests & community classics across Episodes 1, 2, and 4 |
| `opcodes` | 518 | Bytecode opcodes, hex mappings, Qedit/newserv mnemonics, operand formats |
| `areas` | 47 | Area IDs, episode bindings, default floor IDs, and map asset relocations |
| `floor_compatibility` | 47 | Allowed monster & object masks, door connectivity, and floor transitions |
| `object_parameter_schemas` | 359 | Interactive world entities (switches, lasers, warps, doors, chests) |
| `standard_npcs` | 62 | Standard Hunter, Ranger, Force, Citizen, and Lab personnel presets |
| `special_player_models` | 11 | Cameo character models (Sonic, Knuckles, Tails, Rico, Flowen, Elly, GM) |
| `special_city_objects` | 4 | Pioneer 2 city monitors, decorative props, and furniture entities |
| `special_stage_npcs` | 3 | Unique stage NPCs (NiGHTS sitting, NiGHTS flying, Chao) |
| `story_npcs` | 64 | Story-critical NPC appearances and character visual configurations |
| `sound_effects` | 13 | Quest audio cues, jingles, and event sound triggers |
| `quest_script_templates` | 4 | Ready-to-use boilerplate assembly code templates for Qedit and newserv |
| `enemy_parameter_schemas` | 64 | Rare variant rates, slime splits, pack leaders, and hive spawn caps |
| `item_creation_codes` | 1,512 | Item hex prefixes, classes, grinds, attributes, and R200–R211 registers |
| `quest_flag_registry` | 250 | Sega reserved vs safe quest flags, collision avoidance, and usage rules |
| `particle_effects` | 18 | Particle effect types (`TObjParticle` / `0x0001`), radii, and draw distances |
| `camera_cutscene_schemas` | 11 | Camera pan schemas, coordinates, timings, and cutscene routines |
| `wave_event_actions` | 35,647 | Binary DAT wave trigger sequences, delay frames, and room clearing |
| `quest_dialogue_strings` | 80,782 | Multi-lingual quest dialogue lines with Sega colour tags decoded |
| `quest_minigame_mechanics` | 6 | Complex quest mechanics (Gallon Roulette, Soccer physics, CMode timers) |
| `qedit_tooling_assets` | 1,227 | Qedit 3D meshes, entity icons, Delphi forms, and UI layouts |
| **Total Verified Records** | **121,176** | **Complete Quest System Extraction** |

---

## 🛠️ Developer Quick-Start

### 1. Querying with Python & SQLite
```python
import sqlite3

conn = sqlite3.connect("psobb_master_database.sqlite")
cur = conn.cursor()

# Find all rare monster parameter rules
for row in cur.execute("SELECT name, rare_variant_behavior FROM enemy_parameter_schemas WHERE rare_variant_behavior IS NOT NULL"):
    print(f"[{row[0]}] {row[1]}")

# Verify if Flag 105 is safe for custom quests
flag_info = cur.execute("SELECT flag_id, is_reserved_official, purpose_description FROM quest_flag_registry WHERE flag_id = 105").fetchone()
print(f"Flag 105 Reserved: {bool(flag_info[1])} - {flag_info[2]}")
```

### 2. Item Creation Code Assembly Recipe (`item_create2`)
```text
// Give Red Ring (0x01, 0x02, 0x1B) with max stats:
set_register R200, 0x01    // Item Class: Armor & Shield
set_register R201, 0x02    // Category: Barrier / Shield
set_register R202, 0x1B    // Item ID: Red Ring
set_register R203, 0x00    // DFP bonus
set_register R204, 0x00    // EVP bonus
item_create2 R200          // Deliver directly to player
```

### 3. Safe Quest Flag Guidelines
- **Flags 0–31**: Core Sega Engine & Network State (**DO NOT OVERWRITE**).
- **Flags 32–127**: Quest Status, Story Branches, and Hunter's Guild Registration.
- **Flags 128–255**: Area Floor Cleared & Boss Portal Synchronization.
- **Flags 600–899**: **Universal Safe Custom Range** (guaranteed zero collision with Sega quests).

---

## 📁 Repository Structure

```
PSOBB-Quest-Database/
├── index.html                  # Interactive Single-Page Web Viewer (GitHub Pages)
├── psobb_master_database.sqlite # Master SQLite database (21 tables, 121,176 records)
├── psobb_master_database.json   # Full nested JSON export (46.3 MB)
├── PSOBB_MASTER_DATABASE.md    # Comprehensive technical manual & ASM recipes
├── web_data/                   # Lightweight modular JSON chunks for instant web loading
│   ├── manifest.json           # Database statistics and schema metadata
│   ├── opcodes.json            # 518 opcodes with operands and stack behavior
│   ├── items.json              # 1,512 item creation codes & register presets
│   ├── flags.json              # 250 quest flag registry entries
│   ├── enemies.json            # 64 enemy schemas with rare spawn rules
│   ├── objects.json            # 359 object parameter schemas
│   ├── npcs.json               # Special models, stage NPCs, and standard NPCs
│   ├── cameras.json            # 11 camera cutscene schemas
│   ├── particles.json          # 18 particle effect types
│   ├── minigames.json          # 6 minigame state machines
│   ├── quests.json             # 527 catalogued quest dossiers
│   ├── dialogues_sample.json   # Sample story dialogues
│   └── waves_sample.json       # Sample wave event sequences
├── analysis/                   # Detailed catalogues, floor maps, and wireframes
│   ├── entity-database/        # Monsters, NPCs, and appearance galleries
│   ├── floor-database/         # Floor layouts and room geometries
│   ├── object-database/        # Qedit interactive object definitions
│   └── quest-knowledge/       # DAT schema, compiler profiles, and review notes
└── .github/workflows/pages.yml # Automatic GitHub Pages deployment workflow
```

---

## ⚖️ Attribution & Provenance

Original quest assets, client bytecode specifications, and game entities are copyright **Sega / Sonic Team**. This project is an open-source reverse-engineering and preservation initiative intended for developers, researchers, and community quest creators. Upstream newserv definitions are referenced under the [newserv license](analysis/quest-knowledge/reference/NEWSERV-LICENSE).
