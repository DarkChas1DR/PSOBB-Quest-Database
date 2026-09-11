"""Restore the packaged search files, verifying hashes before installation."""
import gzip
import hashlib
import json
import pathlib
import shutil

ROOT = pathlib.Path(__file__).resolve().parent

def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        while data := f.read(1024 * 1024):
            h.update(data)
    return h.hexdigest()

def inside(relative):
    path = (ROOT / relative).resolve()
    if not path.is_relative_to(ROOT):
        raise ValueError('Archive path must remain inside the repository')
    return path

def main():
    for item in json.loads((ROOT / 'archives.json').read_text(encoding='utf-8')):
        archive, dest = inside(item['archive']), inside(item['destination'])
        if dest.exists():
            if digest(dest) == item['sha256']:
                print('Already verified:', item['destination'])
                continue
            raise FileExistsError(f'{dest} differs from the packaged file; move it aside before restoring')
        temp = dest.with_name(dest.name + '.restoring')
        try:
            with gzip.open(archive, 'rb') as src, temp.open('xb') as out:
                shutil.copyfileobj(src, out, 1024 * 1024)
            if temp.stat().st_size != item['size'] or digest(temp) != item['sha256']:
                raise ValueError(f'Archive integrity check failed: {archive}')
            temp.replace(dest)
        except Exception:
            # Retain partial output for inspection; never replace an existing database.
            raise
        print('Restored and verified:', item['destination'])

if __name__ == '__main__':
    main()
