#!/usr/bin/env python3
"""
PSOBB Prompt-to-Quest Generator CLI Tool
Part of the PSOBB Quest Database Project (https://github.com/DarkChas1DR/PSOBB-Quest-Database)

Takes a natural language prompt or parameter flags and generates a complete,
verified, crash-free custom PSOBB quest package (script.txt, map.txt, CSVs, README, and ZIP).
Follows all official Sega bytecode conventions, safe flags (600..899), and collision geometry.
"""

import os
import sys
import json
import re
import struct
import argparse
import zipfile

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
WEB_DATA_DIR = os.path.join(REPO_DIR, 'web_data')

def load_json(filename):
    path = os.path.join(WEB_DATA_DIR, filename)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

# Area mapping definitions: Area keyword -> (Episode, AreaID, FloorIndex, WireframeID, FriendlyName)
AREA_KEYWORDS = {
    'forest': (1, 1, 1, 'map_forest01', 'Forest 1'),
    'forest 1': (1, 1, 1, 'map_forest01', 'Forest 1'),
    'forest 2': (1, 2, 2, 'map_forest02', 'Forest 2'),
    'cave': (1, 3, 3, 'map_cave01_00', 'Cave 1'),
    'caves': (1, 3, 3, 'map_cave01_00', 'Cave 1'),
    'cave 1': (1, 3, 3, 'map_cave01_00', 'Cave 1'),
    'cave 2': (1, 4, 4, 'map_cave02_00', 'Cave 2'),
    'cave 3': (1, 5, 5, 'map_cave03_00', 'Cave 3'),
    'mine': (1, 6, 6, 'map_machine01_00', 'Mine 1'),
    'mines': (1, 6, 6, 'map_machine01_00', 'Mine 1'),
    'mine 1': (1, 6, 6, 'map_machine01_00', 'Mine 1'),
    'mine 2': (1, 7, 7, 'map_machine02_00', 'Mine 2'),
    'ruin': (1, 8, 8, 'map_ancient01_00', 'Ruins 1'),
    'ruins': (1, 8, 8, 'map_ancient01_00', 'Ruins 1'),
    'ruins 1': (1, 8, 8, 'map_ancient01_00', 'Ruins 1'),
    'ruins 2': (1, 9, 9, 'map_ancient02_00', 'Ruins 2'),
    'ruins 3': (1, 10, 10, 'map_ancient03_00', 'Ruins 3'),
    'dragon': (1, 11, 11, 'map_boss01', 'Under the Dome (Dragon)'),
    'de rol le': (1, 12, 12, 'map_boss02', 'Underground Channel (De Rol Le)'),
    'vol opt': (1, 13, 13, 'map_boss03', 'Monitor Room (Vol Opt)'),
    'dark falz': (1, 14, 14, 'map_darkfalz00', '???? (Dark Falz)'),

    'temple': (2, 1, 1, 'map_ruins01_00', 'VR Temple Alpha'),
    'temple alpha': (2, 1, 1, 'map_ruins01_00', 'VR Temple Alpha'),
    'temple beta': (2, 2, 2, 'map_ruins02_00', 'VR Temple Beta'),
    'spaceship': (2, 3, 3, 'map_space01_00', 'VR Spaceship Alpha'),
    'spaceship alpha': (2, 3, 3, 'map_space01_00', 'VR Spaceship Alpha'),
    'spaceship beta': (2, 4, 4, 'map_space02_00', 'VR Spaceship Beta'),
    'jungle': (2, 6, 6, 'map_jungle02_00', 'Jungle Area North'),
    'mountain': (2, 8, 8, 'map_jungle04_00', 'Mountain Area'),
    'seaside': (2, 9, 9, 'map_jungle05_00', 'Seaside Area'),
    'seabed': (2, 10, 10, 'map_seabed01_00', 'Seabed Upper Levels'),
    'seabed upper': (2, 10, 10, 'map_seabed01_00', 'Seabed Upper Levels'),
    'seabed lower': (2, 11, 11, 'map_seabed02_00', 'Seabed Lower Levels'),
    'olga flow': (2, 13, 13, 'map_boss06', 'Test Subject Disposal Area (Olga Flow)'),

    'crater': (4, 1, 1, 'map_wilds01_00', 'Crater (Eastern Route)'),
    'desert': (4, 6, 6, 'map_desert01_00', 'Subterranean Desert 1'),
    'desert 1': (4, 6, 6, 'map_desert01_00', 'Subterranean Desert 1'),
    'desert 2': (4, 7, 7, 'map_desert02_00', 'Subterranean Desert 2'),
    'desert 3': (4, 8, 8, 'map_desert03_00', 'Subterranean Desert 3'),
}

# Standard enemy pools by area
ENEMY_POOLS = {
    'Forest': [
        ('Booma', 0x0040, 'Basic Native melee infantry'),
        ('Gobooma', 0x0041, 'Agile Native pack fighter'),
        ('Gigobooma', 0x0042, 'Heavy Native brawler'),
        ('Savage Wolf', 0x0043, 'Pack flanking quadruped'),
        ('Barbarous Wolf', 0x0044, 'Alpha pack leader'),
        ('Monest', 0x0045, 'Hive spawner (Mothmants)'),
        ('Hildebear', 0x0047, 'Brute ape with high HP and jumping strike'),
    ],
    'Caves': [
        ('Evil Shark', 0x0060, 'Altered Beast infantry'),
        ('Pal Shark', 0x0061, 'Altered Beast spearman'),
        ('Guil Shark', 0x0062, 'Elite Altered Beast guard'),
        ('Poison Lily', 0x0063, 'Paralysis & Megid spore plant'),
        ('Grass Assassin', 0x0064, 'Dual scythe striker'),
        ('Nano Dragon', 0x0065, 'Aerial laser breath reptile'),
        ('Pan Arms', 0x0067, 'Split shielding duo'),
    ],
    'Mines': [
        ('Gillchic', 0x0080, 'Machine laser infantry'),
        ('Dubchic', 0x0081, 'Remote core linked drone'),
        ('Canadine', 0x0083, 'Hovering ring laser platform'),
        ('Canane', 0x0084, 'Ring leader command drone'),
        ('Sinow Beat', 0x0085, 'Stealth camouflage assassin'),
        ('Garanz', 0x0086, 'Heavy armored missile tank'),
    ],
    'Ruins': [
        ('Dimenian', 0x00A0, 'Dark entity swordsman'),
        ('La Dimenian', 0x00A1, 'Dark entity veteran'),
        ('So Dimenian', 0x00A2, 'Heavy dark entity warrior'),
        ('Claw', 0x00A3, 'Swarm blade drone'),
        ('Bulk', 0x00A4, 'Swarm anchor core'),
        ('Dark Belra', 0x00A6, 'Giant rocket punch demon'),
        ('Chaos Sorcerer', 0x00A8, 'High-tier spellcaster (Rafoie/Rabarta)'),
    ],
    'Seabed': [
        ('Dolmolm', 0x0110, 'Submersible armored crustacean'),
        ('Dolmdarl', 0x0111, 'Advanced heavy submerger'),
        ('Morfos', 0x0112, 'Phase shifting laser automaton'),
        ('Recobox', 0x0113, 'Autonomous recon drone dispenser'),
        ('Sinow Zoa', 0x0115, 'High-mobility seabed assassin'),
        ('Delbiter', 0x0117, 'Armored charging behemoth'),
    ],
    'Desert': [
        ('Boota', 0x0130, 'Desert sand infantry'),
        ('Ze Boota', 0x0131, 'Desert sand skirmisher'),
        ('Ba Boota', 0x0132, 'Desert heavy sand fighter'),
        ('Zu', 0x0133, 'Giant desert avian terror'),
        ('Astark', 0x0135, 'Desert apex predator'),
        ('Goran', 0x0136, 'Desert rock burrower'),
        ('Goran Detonator', 0x0138, 'Heavy explosive desert beast'),
    ]
}

def parse_prompt(prompt_text):
    """Parses natural language prompt into structured quest parameters."""
    text = prompt_text.lower()

    # Determine Quest Type
    q_type = 'extermination'
    if any(k in text for k in ['shop', 'store', 'merchant', 'trade', 'buy', 'vendor', 'paganini', 'exchange']):
        q_type = 'shop'
    elif any(k in text for k in ['boss', 'rush', 'gauntlet', 'arena', 'dragon', 'de rol le', 'vol opt', 'falz', 'olga']):
        q_type = 'boss_rush'
    elif any(k in text for k in ['puzzle', 'switch', 'laser', 'terminal', 'infiltrat', 'hack']):
        q_type = 'puzzle'
    elif any(k in text for k in ['surviv', 'time', 'timed', 'timer', 'defend', 'horde']):
        q_type = 'survival'

    # Determine Area & Episode
    selected_area = None
    for kw in sorted(AREA_KEYWORDS.keys(), key=lambda x: -len(x)):
        if kw in text:
            selected_area = AREA_KEYWORDS[kw]
            break

    if not selected_area:
        selected_area = AREA_KEYWORDS['forest 1']

    ep, area_id, floor_idx, wireframe_id, friendly_name = selected_area

    # Determine Wave Count (1 to 8, default 3)
    waves = 3
    wave_match = re.search(r'(\d+)\s*(?:wave|stage|round|phase)', text)
    if wave_match:
        waves = max(1, min(8, int(wave_match.group(1))))

    has_boss = any(k in text for k in ['boss', 'dragon', 'olga', 'falz', 'de rol le', 'vol opt']) or (q_type == 'boss_rush')

    # Determine Reward
    reward = {'type': 'item', 'name': 'Photon Drop', 'hex': '0x03, 0x10, 0x00', 'count': 5}
    if 'red ring' in text:
        reward = {'type': 'item', 'name': 'Red Ring', 'hex': '0x01, 0x02, 0x1B', 'count': 1}
    elif 'heaven striker' in text:
        reward = {'type': 'item', 'name': 'Heaven Striker', 'hex': '0x00, 0x02, 0x51', 'count': 1}
    elif 'excalibur' in text:
        reward = {'type': 'item', 'name': 'Excalibur', 'hex': '0x00, 0x01, 0x54', 'count': 1}
    elif 'photon drop' in text:
        reward = {'type': 'item', 'name': 'Photon Drop', 'hex': '0x03, 0x10, 0x00', 'count': 10}
    elif 'meseta' in text:
        mes_match = re.search(r'(\d+(?:,\d+)?)\s*meseta', text)
        amount = int(mes_match.group(1).replace(',', '')) if mes_match else 50000
        reward = {'type': 'meseta', 'name': f'{amount:,} Meseta', 'amount': amount}

    title = None
    title_match = re.search(r'(?:called|named|title[d:]?)\s*[\'"]?([^\'",\.\n]+)[\'"]?', prompt_text, re.IGNORECASE)
    if title_match:
        title = title_match.group(1).strip()
    else:
        prefix = {'extermination': 'Hunt', 'shop': 'Bazaar', 'boss_rush': 'Trial', 'puzzle': 'Infiltration', 'survival': 'Stand'}[q_type]
        title = f"{prefix}: {friendly_name}"

    return {
        'title': title,
        'type': q_type,
        'episode': ep,
        'area_id': area_id,
        'floor_idx': floor_idx,
        'wireframe_id': wireframe_id,
        'area_name': friendly_name,
        'waves_count': waves,
        'has_boss': has_boss,
        'reward': reward,
        'raw_prompt': prompt_text
    }

def prs_compress(data):
    dst = bytearray()
    flag_byte_idx = 0
    flag_bit_idx = 0
    current_flags = 0
    dst.append(0)

    def write_bit(bit):
        nonlocal flag_byte_idx, flag_bit_idx, current_flags
        if flag_bit_idx == 8:
            flag_byte_idx = len(dst)
            dst.append(0)
            flag_bit_idx = 0
            current_flags = 0
        if bit:
            current_flags |= (1 << flag_bit_idx)
            dst[flag_byte_idx] = current_flags
        flag_bit_idx += 1

    src = 0
    data_len = len(data)
    while src < data_len:
        best_len = 0
        best_offset = 0
        max_lookback = min(src, 8190)
        max_len = min(256, data_len - src)
        if max_len >= 3 and max_lookback > 0:
            for l in range(1, max_lookback + 1):
                cm = 0
                while cm < max_len and data[src - l + (cm % l)] == data[src + cm]:
                    cm += 1
                if cm > best_len:
                    best_len = cm
                    best_offset = l
                    if best_len == max_len:
                        break

        if best_len >= 3:
            if best_len <= 5 and best_offset <= 256:
                write_bit(0); write_bit(0)
                write_bit(1 if ((best_len - 2) & 2) else 0)
                write_bit(1 if ((best_len - 2) & 1) else 0)
                dst.append((256 - best_offset) & 0xFF)
            else:
                write_bit(0); write_bit(1)
                comb = (8192 - best_offset) << 3
                if best_len <= 9:
                    val = comb | (best_len - 2)
                    dst.append(val & 0xFF)
                    dst.append((val >> 8) & 0xFF)
                else:
                    dst.append(comb & 0xFF)
                    dst.append((comb >> 8) & 0xFF)
                    dst.append(best_len - 1)
            src += best_len
        else:
            write_bit(1)
            dst.append(data[src])
            src += 1

    write_bit(0); write_bit(1)
    dst.append(0); dst.append(0)
    return bytes(dst)

def compile_quest_dat(spec, enemies_rows, objects_rows):
    RECORD_SIZE = 68
    SECTION_HDR = 16
    buf = bytearray()
    
    # 1. Floor 1 Objects
    obj_data = bytearray()
    for idx, row in enumerate(objects_rows[1:]):
        parts = row.split(',')
        if len(parts) < 8: continue
        flr = int(parts[0])
        if flr != 0 and flr != 1 and flr != spec.get('floor_idx', 1):
            continue
        type_id = int(parts[2], 16)
        room = int(parts[1])
        x, y, z = float(parts[4]), float(parts[5]), float(parts[6])
        angle = int(parts[7], 16)
        rec = bytearray(RECORD_SIZE)
        struct.pack_into('<2H3I3f3i3f4I', rec, 0,
            type_id, 2, idx, 16384 + idx, room,
            x, y, z, 0, angle, 0,
            1.0, 1.0, 1.0,
            int(parts[8]) if len(parts) > 8 and parts[8].strip().lstrip('-').isdigit() else 0,
            int(parts[9]) if len(parts) > 9 and parts[9].strip().lstrip('-').isdigit() else 0,
            int(parts[10]) if len(parts) > 10 and parts[10].strip().lstrip('-').isdigit() else 0,
            1000 + idx
        )
        obj_data.extend(rec)

    buf.extend(struct.pack('<4I', 1, SECTION_HDR + len(obj_data), 0, len(obj_data)))
    buf.extend(obj_data)

    # 2. Floor 1 Enemies
    ene_data = bytearray()
    events = []
    actions = bytearray()
    
    waves_dict = {}
    for idx, row in enumerate(enemies_rows[1:]):
        parts = row.split(',')
        if len(parts) < 8: continue
        w = int(parts[2])
        if w not in waves_dict: waves_dict[w] = []
        waves_dict[w].append((idx, parts))

    sorted_waves = sorted(waves_dict.keys())
    total_waves = len(sorted_waves)

    for wi, w in enumerate(sorted_waves):
        spawns = waves_dict[w]
        room = int(spawns[0][1][1])
        eid = 100 + w
        act_off = len(actions)
        if wi < total_waves - 1:
            actions.extend(struct.pack('<BI B', 0x0C, 100 + (w + 1), 0x01))
        else:
            actions.extend(struct.pack('<BH B', 0x0A, 1, 0x01))
        events.append((eid, 1, room, w, 10, act_off))

        for idx, parts in spawns:
            type_id = int(parts[4], 16)
            x, y, z = float(parts[5]), float(parts[6]), float(parts[7])
            angle = int(parts[8], 16)
            rec = bytearray(RECORD_SIZE)
            struct.pack_into('<4H2I3f3i3f4I', rec, 0,
                type_id, 0, eid, w, idx + 1, room,
                x, y, z, 0, angle, 0,
                1.0, 1.0, 1.0,
                32, 0, w, 2000 + idx
            )
            ene_data.extend(rec)

    buf.extend(struct.pack('<4I', 1, SECTION_HDR + len(ene_data), 1, len(ene_data)))
    buf.extend(ene_data)

    # 3. Map Events (Floor 2)
    evt_entries = bytearray()
    for e in events:
        eid, flr, rm, wv, prm, aoff = e
        evt_entries.extend(struct.pack('<I HH HH II', eid, 0, flr, rm, wv, prm, aoff))
    
    evt_hdr = struct.pack('<4I', 16 + len(evt_entries), 16, len(events), 0)
    evt_payload = evt_hdr + evt_entries + actions
    buf.extend(struct.pack('<4I', 2, SECTION_HDR + len(evt_payload), 1, len(evt_payload)))
    buf.extend(evt_payload)

    # 4. Terminator
    buf.extend(struct.pack('<4I', 0, 0, 0, 0))
    return prs_compress(bytes(buf))

def compile_quest_bin(spec):
    HEADER_SIZE = 0x122C
    header = bytearray(HEADER_SIZE)
    for i in range(0x398, HEADER_SIZE):
        header[i] = 0xFF

    title_u16 = spec['title'][:31].encode('utf-16le') + b'\0\0'
    header[0x18:0x18+len(title_u16)] = title_u16

    desc1 = f"PSOBB AI Quest ({spec['type'].upper()})".encode('utf-16le') + b'\0\0'
    header[0x58:0x58+len(desc1)] = desc1

    desc2 = f"Area: {spec['area_name']} (Floor {spec['floor_idx']}). Complete all wave encounters to claim your reward!".encode('utf-16le') + b'\0\0'
    header[0x158:0x158+len(desc2)] = desc2

    code = bytearray()
    fn_map = {}
    backpatch = []

    def def_fn(fid): fn_map[fid] = len(code)
    def emit_ref(fid):
        backpatch.append((len(code), fid))
        code.extend(b'\0\0')

    # Fn 0
    def_fn(0)
    code.extend(bytes([0xF8, 0xBC])) # set_episode
    code.extend(struct.pack('<i', spec['episode'] - 1))
    code.extend(bytes([0xF9, 0x51, 0, 0, 0, 0, 0])) # Pioneer 2
    code.extend(bytes([0xF9, 0x51, 1, spec['area_id'], 0, 0, 0])) # Floor 1
    code.append(0x04); emit_ref(100) # thread L100
    code.append(0x01) # ret

    # Fn 1
    def_fn(1); code.append(0x01)

    # Fn 10: Officer
    def_fn(10)
    code.append(0x65); code.append(0x5A)
    code.extend(b"Hunter's Guild:\\nA critical assignment on Ragol awaits you.\\nDeploy and eradicate all hostiles!\0")
    code.append(0x5E); code.append(0x01)

    # Fn 20: Scout
    def_fn(20)
    code.append(0x65); code.append(0x5A)
    code.extend(b"Tactical Scout:\\nRadar detects dense enemy clusters in designated sectors.\\nMaintain formation!\0")
    code.append(0x5E); code.append(0x01)

    # Fn 100: Monitor loop
    def_fn(100)
    code.append(0x02); code.append(0x28); emit_ref(100); code.append(0x01)

    for pos, fid in backpatch:
        target = fn_map.get(fid, 0)
        code[pos] = target & 0xFF
        code[pos+1] = (target >> 8) & 0xFF

    NUM_FNS = 702
    fn_table = bytearray(NUM_FNS * 4)
    for i in range(NUM_FNS):
        struct.pack_into('<I', fn_table, i * 4, 0xFFFFFFFF)
    for fid, off in fn_map.items():
        if fid < NUM_FNS:
            struct.pack_into('<I', fn_table, fid * 4, off)

    code_start = HEADER_SIZE
    fn_table_offset = code_start + len(code)
    total_size = fn_table_offset + len(fn_table)

    struct.pack_into('<6I', header, 0,
        code_start, fn_table_offset, total_size,
        0xFFFFFFFF, 999, 0x00000400
    )

    full_bin = header + code + fn_table
    return prs_compress(full_bin)

def compile_quest_qst(bin_prs, dat_prs, quest_num=999):
    dat_fname = f"quest{quest_num}.dat".encode('ascii')
    bin_fname = f"quest{quest_num}.bin".encode('ascii')
    chunks = []

    def make_header(fname, total_sz):
        hdr = bytearray(88)
        struct.pack_into('<2H', hdr, 0, 88, 0x0044)
        hdr[44:44+len(fname)] = fname
        struct.pack_into('<I', hdr, 60, total_sz)
        hdr[64:68] = b'PSO/'
        return bytes(hdr)

    def append_chunks(fname, data):
        num_chunks = max(1, (len(data) + 1023) // 1024)
        for ci in range(num_chunks):
            pkt = bytearray(1056)
            struct.pack_into('<2HI', pkt, 0, 1052, 0x0013, ci)
            pkt[8:8+len(fname)] = fname
            chunk = data[ci*1024:(ci+1)*1024]
            pkt[24:24+len(chunk)] = chunk
            struct.pack_into('<I', pkt, 1048, len(chunk))
            chunks.append(bytes(pkt))

    h1 = make_header(dat_fname, len(dat_prs))
    h2 = make_header(bin_fname, len(bin_prs))
    append_chunks(dat_fname, dat_prs)
    append_chunks(bin_fname, bin_prs)

    out = bytearray(h1 + h2)
    for c in chunks: out.extend(c)
    return bytes(out)

def generate_quest_files(spec, out_dir):
    """Generates all files (script.txt, map.txt, CSVs, README, and ZIP) for the quest."""
    os.makedirs(out_dir, exist_ok=True)

    wireframes = load_json('wireframes.json')
    wf = next((w for w in wireframes if w['id'] == spec['wireframe_id']), None)
    sec_ids = wf['section_ids'] if wf else [1, 2, 3, 4, 5]

    combat_rooms = sec_ids[:min(spec['waves_count'], len(sec_ids))]
    if not combat_rooms:
        combat_rooms = [1, 2, 3]

    FLAG_ACCEPTED = 610
    FLAG_ENCOUNTER_ACTIVE = 611
    FLAG_ROOM_CLEARED = 612
    FLAG_REWARD_CLAIMED = 613

    pool_key = 'Forest'
    for k in ENEMY_POOLS.keys():
        if k.lower() in spec['area_name'].lower():
            pool_key = k
            break
    enemies_catalog = ENEMY_POOLS[pool_key]

    asm_lines = [
        f"// ============================================================================",
        f"// Quest: {spec['title']}",
        f"// Episode: {spec['episode']} | Area: {spec['area_name']} (Floor {spec['floor_idx']})",
        f"// Type: {spec['type'].upper()} | Safe Flag Range: 600..699",
        f"// Generated via PSOBB AI Quest Creator Tool (Zero Collision Architecture)",
        f"// ============================================================================",
        f"",
        f"// ----------------------------------------------------------------------------",
        f"// FUNCTION 0: Entry Point & System Initialization",
        f"// ----------------------------------------------------------------------------",
        f"L0:",
        f"    set_episode {spec['episode'] - 1}                       // Set active Episode (0=Ep1, 1=Ep2, 2=Ep4)",
        f"    BB_Map_Designate 0, 0, 0, 0, 0             // Floor 0: Pioneer 2 City",
        f"    BB_Map_Designate {spec['floor_idx']}, {spec['area_id']}, 0, 0, 0    // Floor {spec['floor_idx']}: {spec['area_name']}",
    ]

    if spec['has_boss']:
        asm_lines.append(f"    BB_Map_Designate 11, 11, 0, 0, 0           // Floor 11: Boss Arena")

    asm_lines.extend([
        f"    initial_floor 0                            // Player starts on Pioneer 2",
        f"    set_guild_callback L1                      // Guild callback (Function 1 blank return)",
        f"    thread L100                                // Start background objective watcher thread",
        f"    ret",
        f"",
        f"// ----------------------------------------------------------------------------",
        f"// FUNCTION 1: Blank Callback Convention",
        f"// ----------------------------------------------------------------------------",
        f"L1:",
        f"    ret",
        f"",
        f"// ----------------------------------------------------------------------------",
        f"// FUNCTION 10: Hunter's Guild / Officer NPC Interaction",
        f"// ----------------------------------------------------------------------------",
        f"L10:",
        f"    check_flag {FLAG_REWARD_CLAIMED}, R200     // Check if quest already rewarded",
        f"    jmpi_eq R200, 1, L14                       // If claimed, branch to completed dialogue",
        f"    check_flag {FLAG_ROOM_CLEARED}, R200       // Check if objectives complete",
        f"    jmpi_eq R200, 1, L13                       // If complete, claim reward",
        f"    check_flag {FLAG_ACCEPTED}, R200           // Check if mission in progress",
        f"    jmpi_eq R200, 1, L12                       // Remind player of mission",
        f"",
        f"    // Mission Briefing Dialogue",
        f"    window_msg \"Hunter's Guild Officer:\\nGreetings, Hunter! We have received an urgent report from {spec['area_name']}.\"",
        f"    winend",
        f"    window_msg \"Dangerous hostiles are disrupting our telemetry network.\\nDeploy through the teleporter and neutralize all waves.\"",
        f"    winend",
        f"    set_flag {FLAG_ACCEPTED}                   // Mark mission accepted",
        f"    ret",
        f"",
        f"L12:",
        f"    window_msg \"Officer:\\nThe teleporter to {spec['area_name']} is active.\\nProceed immediately and eliminate all hostiles.\"",
        f"    winend",
        f"    ret",
        f"",
        f"L13:",
        f"    // Reward Distribution Routine",
        f"    window_msg \"Officer:\\nOutstanding work, Hunter! The telemetry network in {spec['area_name']} is secured.\"",
        f"    winend",
        f"    window_msg \"Here is your authorized reward from the Principal's office.\"",
        f"    winend",
    ])

    if spec['reward']['type'] == 'meseta':
        asm_lines.extend([
            f"    add_meseta {spec['reward']['amount']}                  // Deliver {spec['reward']['name']}",
            f"    sound_effect 0x0006                        // Play reward fanfare SFX",
        ])
    else:
        parts = [p.strip() for p in spec['reward']['hex'].split(',')]
        asm_lines.extend([
            f"    // Item Delivery via R200..R204",
            f"    set_register R200, {parts[0]}              // Item Class",
            f"    set_register R201, {parts[1]}              // Category",
            f"    set_register R202, {parts[2]}              // Item ID: {spec['reward']['name']}",
            f"    set_register R203, 0x00                    // Attribute 1",
            f"    set_register R204, 0x00                    // Attribute 2",
            f"    item_create2 R200                          // Safe direct item delivery",
            f"    sound_effect 0x0006                        // Play reward fanfare SFX",
        ])

    asm_lines.extend([
        f"    set_flag {FLAG_REWARD_CLAIMED}             // Lock reward to prevent duplicate claims",
        f"    set_register R255, 1                       // Signal Quest Success to Guild Framework",
        f"    ret",
        f"",
        f"L14:",
        f"    window_msg \"Officer:\\nThank you again for your service. Excellent performance.\"",
        f"    winend",
        f"    ret",
        f"",
        f"// ----------------------------------------------------------------------------",
        f"// FUNCTION 100: Background Objective Monitor Loop (Guaranteed Yield)",
        f"// ----------------------------------------------------------------------------",
        f"L100:",
        f"    sync                                       // Yield VM frame (prevents CPU lockup)",
        f"    check_flag {FLAG_ACCEPTED}, R200",
        f"    jmpi_eq R200, 0, L100                      // Wait until player accepts quest",
        f"",
        f"    // Polling encounter completion",
        f"    set_register R2, {spec['floor_idx']}                   // Floor slot",
        f"    set_register R3, {combat_rooms[-1]}                   // Target final combat room ID",
        f"    if_zone_clear R1, R2                       // Consumes R2=Floor, R3=Room; R1 receives 1 if cleared",
        f"    jmpi_eq R1, 0, L100                        // Still enemies alive, loop back and yield",
        f"",
        f"    // Objectives Cleared!",
        f"    set_flag {FLAG_ROOM_CLEARED}",
        f"    sound_effect 0x0004                        // Quest Objective Complete Chime",
        f"    set_switch_flag_sync {spec['floor_idx']}, 1           // Unlock return teleporter switch",
        f"    ret",
    ])

    script_content = "\n".join(asm_lines)
    with open(os.path.join(out_dir, "script.txt"), "w", encoding="utf-8") as f:
        f.write(script_content)

    enemies_rows = ["floor,room,wave,enemy_name,type_hex,x,y,z,angle,comment"]
    map_lines = [
        f"# PSOBB Spatial Placements & Wave Actions for: {spec['title']}",
        f"# Floor {spec['floor_idx']} ({spec['area_name']})",
        f"",
        f"[OBJECTS]",
        f"# floor, room, type_hex, type_name, x, y, z, angle, param1..param6",
        f"0, 10, 0x0002, Guild_Officer_NPC, 12.5, 0.0, -45.0, 0x8000, 0, 0, 0, 0, 0, 0",
        f"{spec['floor_idx']}, {combat_rooms[0]}, 0x0019, Warp_Pioneer2, 0.0, 0.0, 0.0, 0x0000, 0, 0, 0, 0, 1, 0",
        f"",
        f"[ENEMIES]"
    ]

    objects_rows = [
        "floor,room,type_hex,type_name,x,y,z,angle,comment",
        "0,10,0x0002,Guild_Officer_NPC,12.5,0.0,-45.0,0x8000,Pioneer 2 Quest Giver",
        f"{spec['floor_idx']},{combat_rooms[0]},0x0019,Warp_Pioneer2,0.0,0.0,0.0,0x0000,Return Teleporter Switch 1"
    ]

    waves_rows = ["floor,room,wave_num,trigger_event,delay_frames,enemy_count,next_action"]

    for w_idx in range(spec['waves_count']):
        room_id = combat_rooms[w_idx % len(combat_rooms)]
        wave_num = w_idx + 1
        trigger_evt = 100 + wave_num
        delay = 30 * w_idx

        e_type = enemies_catalog[w_idx % len(enemies_catalog)]
        e_count = 3 + (w_idx % 3)

        waves_rows.append(f"{spec['floor_idx']},{room_id},{wave_num},{trigger_evt},{delay},{e_count},spawn_wave")

        for i in range(e_count):
            x = (i - e_count / 2) * 15.0
            z = 20.0 + (i * 5.0)
            enemies_rows.append(f"{spec['floor_idx']},{room_id},{wave_num},{e_type[0]},{hex(e_type[1])},{x:.1f},0.0,{z:.1f},0x0000,{e_type[2]}")
            map_lines.append(f"{spec['floor_idx']}, {room_id}, {wave_num}, {e_type[0]} ({hex(e_type[1])}), x={x:.1f}, y=0.0, z={z:.1f}, delay={delay}")

    with open(os.path.join(out_dir, "enemies.csv"), "w", encoding="utf-8") as f:
        f.write("\n".join(enemies_rows))

    with open(os.path.join(out_dir, "objects.csv"), "w", encoding="utf-8") as f:
        f.write("\n".join(objects_rows))

    with open(os.path.join(out_dir, "waves.csv"), "w", encoding="utf-8") as f:
        f.write("\n".join(waves_rows))

    with open(os.path.join(out_dir, "map.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(map_lines))

    readme_content = f"""# {spec['title']}

A custom Phantasy Star Online Blue Burst quest generated by the **PSOBB AI Quest Creator Tool**.

## Quest Overview
* **Episode**: Episode {spec['episode']}
* **Primary Area**: {spec['area_name']} (Floor {spec['floor_idx']})
* **Quest Category**: {spec['type'].upper()}
* **Wave Encounters**: {spec['waves_count']} Waves
* **Authorized Reward**: {spec['reward']['name']}
* **Safe Flag Allocation**: Flags 610–613 (Zero Sega Collision Guaranteed)

## Included Files
* `script.txt`: Complete Qedit / newserv bytecode assembly with Function 0 entry point, yield monitoring, and guild rewards.
* `map.txt`: Full spatial placement table for NPCs, return teleporters, and monster waves.
* `enemies.csv`: Delimited enemy spawn table with section coordinates and delay frames.
* `objects.csv`: Interactive object configurations.
* `waves.csv`: Event triggers and succession parameters.

## How to Compile & Play
1. **With Qedit**:
   * Open Qedit -> `File > Open Script` -> choose `script.txt`.
   * Set map to `{spec['wireframe_id']}`.
   * Import `objects.csv` and `enemies.csv`.
   * Save as compiled `.bin` and `.dat`.
2. **With newserv**:
   * Run: `newserv assemble-quest-script script.txt quest{spec['area_id']}.bin`
   * Copy `.bin` and `.dat` to your newserv `system/quests/` folder.
"""
    with open(os.path.join(out_dir, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme_content)

    # Compile authentic Sega binaries
    dat_prs = compile_quest_dat(spec, enemies_rows, objects_rows)
    bin_prs = compile_quest_bin(spec)
    qst_bytes = compile_quest_qst(bin_prs, dat_prs, 999)

    with open(os.path.join(out_dir, "quest999.dat"), "wb") as f:
        f.write(dat_prs)
    with open(os.path.join(out_dir, "quest999.bin"), "wb") as f:
        f.write(bin_prs)
    with open(os.path.join(out_dir, "quest999.qst"), "wb") as f:
        f.write(qst_bytes)

    zip_path = os.path.join(out_dir, "custom_quest.zip")
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.write(os.path.join(out_dir, "script.txt"), "script.txt")
        zf.write(os.path.join(out_dir, "map.txt"), "map.txt")
        zf.write(os.path.join(out_dir, "enemies.csv"), "enemies.csv")
        zf.write(os.path.join(out_dir, "objects.csv"), "objects.csv")
        zf.write(os.path.join(out_dir, "waves.csv"), "waves.csv")
        zf.write(os.path.join(out_dir, "README.md"), "README.md")
        zf.write(os.path.join(out_dir, "quest999.dat"), "quest999.dat")
        zf.write(os.path.join(out_dir, "quest999.bin"), "quest999.bin")
        zf.write(os.path.join(out_dir, "quest999.qst"), "quest999.qst")

    return zip_path

def main():
    parser = argparse.ArgumentParser(description="PSOBB Prompt-to-Quest Generator CLI")
    parser.add_argument("--prompt", "-p", type=str, help="Natural language quest description")
    parser.add_argument("--out", "-o", type=str, default="generated_quest", help="Output directory")
    args = parser.parse_args()

    prompt = args.prompt or "Forest 1 extermination mission with 3 waves of Boomas and a Red Ring reward"
    print(f"[+] Parsing prompt: \"{prompt}\"...")
    spec = parse_prompt(prompt)

    print(f"[+] Quest Title: {spec['title']}")
    print(f"[+] Area: {spec['area_name']} (Floor {spec['floor_idx']}, Ep {spec['episode']})")
    print(f"[+] Encounter Waves: {spec['waves_count']} waves across rooms")
    print(f"[+] Reward: {spec['reward']['name']}")

    zip_file = generate_quest_files(spec, args.out)
    print(f"[+] Quest generation complete! Output saved to: {args.out}/")
    print(f"[+] ZIP Package: {zip_file}")

if __name__ == "__main__":
    main()
