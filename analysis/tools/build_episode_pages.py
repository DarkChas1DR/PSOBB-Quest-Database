"""Build episode navigation from decoded headers, preserving category copies."""
import collections
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
CAT = ROOT / 'analysis/server-catalogue'

def escape(value):
    return str(value).replace('|', '&#124;').replace('[', '&#91;').replace(']', '&#93;').replace('\n', ' ')

def main():
    records = json.loads((CAT / 'catalogue.json').read_text(encoding='utf-8'))
    totals = {}
    for episode in (1, 2, 4):
        rows = [r for r in records if r['episode'] == f'Episode{episode}']
        groups = collections.defaultdict(list)
        for r in rows:
            groups[(r['category'], r['prefix'], r['filename_quest_id'])].append(r)
        totals[episode] = (len(groups), len(rows))
        text = [f'# Episode {episode} quest catalogue', '',
                '[All episodes](README.md) · [Episode 1](episode-1.md) · [Episode 2](episode-2.md) · [Episode 4](episode-4.md)', '',
                f'**{len(groups)} category/ID groups; {len(rows)} language variants** from the supplied server quest collection. Episode assignments come from decoded quest headers. Category copies and language variants are retained.', '',
                'Click a quest name for its dossier, then choose scripts, map placements, waves, enemies/NPCs, objects, or state/reward operations. Data is statically decoded; placement counts are not kill totals and full gameplay behavior is not yet verified.', '',
                'For enhanced random-event data and malformed-record cautions, see the [knowledge library](../quest-knowledge/README.md). The original dossier wave tables predate that enhanced parsing; use the searchable database for complete random-event records.', '']
        for category in sorted({k[0] for k in groups}):
            text += [f'## {category}', '', '| Quest | ID | Languages | Script | Map data | Download |', '|---|---|---|---|---|---|']
            for key, variants in sorted(groups.items(), key=lambda item: (item[0][0], item[1][0]['name'].casefold(), item[0][2])):
                if key[0] != category:
                    continue
                variants.sort(key=lambda r: (r['language'] != 'E', r['language']))
                first = variants[0]
                q = first['key']
                langs = ', '.join(f"[{r['language']}]({r['key']}/README.md)" for r in variants)
                text.append(f"| [{escape(first['name'])}]({q}/README.md) | {key[1]}{key[2]} | {langs} | [View]({q}/script-offsets.txt) | [View]({q}/map.txt) | [Files]({q}/README.md#download-quest-files) |")
            text.append('')
        page = CAT / f'episode-{episode}.md'
        page.write_text('\n'.join(text) + '\n', encoding='utf-8')
    for page in CAT.glob('episode-*.md'):
        for target in re.findall(r'\]\(([^)]+)\)', page.read_text(encoding='utf-8')):
            assert (page.parent / target.split('#')[0]).exists(), target
    assert sum(v[1] for v in totals.values()) == len(records), 'Unlisted episode'
    print(json.dumps(totals))

if __name__ == '__main__':
    main()
