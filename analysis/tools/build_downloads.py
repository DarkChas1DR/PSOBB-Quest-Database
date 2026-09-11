"""Expose preserved quest files and create per-variant ZIP downloads."""
import hashlib
import json
import pathlib
import re
import zipfile
from urllib.parse import quote

ROOT = pathlib.Path(__file__).resolve().parents[2]
CAT = ROOT / 'analysis/server-catalogue'
SOURCE = ROOT / 'analysis/quest-knowledge/source-quests'
BASE = 'https://github.com/DarkChas1DR/PSOBB-Quest-Database/raw/refs/heads/main/'

def url(path):
    return BASE + quote(path.relative_to(ROOT).as_posix()) + '?download=1'

def main():
    records = json.loads((CAT / 'catalogue.json').read_text(encoding='utf-8'))
    index = []
    for r in records:
        key = r['key']
        folder = CAT / key
        filename = pathlib.PureWindowsPath(r['source']).name
        original = SOURCE / r['category'] / filename
        assert original.exists(), original
        assert hashlib.sha256(original.read_bytes()).hexdigest() == r['source_sha256']
        files = [(original, original.name, 'Original ' + original.suffix[1:].upper())]
        if original.suffix.lower() == '.bin':
            dat = original.with_suffix('.dat')
            if not dat.exists():
                dat = original.with_name(re.sub(r'-[a-z]\.bin$', '.dat', original.name))
            assert dat.exists(), dat
            assert hashlib.sha256(dat.read_bytes()).hexdigest() == r['map_sha256'], dat
            files.append((dat, dat.name, 'Original DAT'))
            note = 'BIN and DAT are the preserved server files. Download both, or use the ZIP to keep the pair together.'
        else:
            assert original.suffix.lower() == '.qst', original
            for ext in ('bin', 'dat'):
                matches = list(folder.glob(original.name + '-quest*.' + ext))
                assert len(matches) == 1, (key, matches)
                extracted = matches[0]
                files.append((extracted, original.stem + '.' + ext, 'Extracted ' + ext.upper()))
            note = 'QST is the preserved original package. BIN and DAT are its decoded payload files, not reassembled scripts. The ZIP contains all three formats.'
        dest = ROOT / 'downloads' / (key + '.zip')
        dest.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(dest, 'w', compression=zipfile.ZIP_DEFLATED) as z:
            for p, name, _ in files:
                info = zipfile.ZipInfo(name, date_time=(2026, 9, 11, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                z.writestr(info, p.read_bytes())
        with zipfile.ZipFile(dest) as z:
            assert z.testzip() is None
            for p, name, _ in files:
                assert z.read(name) == p.read_bytes()
        section = '\n'.join(['<!-- quest-downloads:start -->', '## Download quest files', '',
            f'**[Download quest ZIP]({url(dest)})**', '',
            ' · '.join(f'[{label}]({url(p)})' for p, _, label in files), '', note, '',
            'These downloads preserve the analysed quest content, including any known issues. They have not been newly playtested. Language follows this page\'s variant.',
            '<!-- quest-downloads:end -->', ''])
        page = folder / 'README.md'
        text = page.read_text(encoding='utf-8')
        text = re.sub(r'<!-- quest-downloads:start -->.*?<!-- quest-downloads:end -->\n*', '', text, flags=re.S)
        head, body = text.split('\n', 1)
        page.write_text(head + '\n\n' + section + '\n' + body.lstrip(), encoding='utf-8')
        index.append(dict(key=key, episode=r['episode'], name=r['name'], zip=dest.relative_to(ROOT).as_posix(),
            sha256=hashlib.sha256(dest.read_bytes()).hexdigest(), files=[dict(path=p.relative_to(ROOT).as_posix(),archive_name=n,label=l,sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p,n,l in files]))
    (ROOT / 'downloads/index.json').write_text(json.dumps(index, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    print('Verified quest ZIPs and individual download links:', len(index))

if __name__ == '__main__':
    main()
