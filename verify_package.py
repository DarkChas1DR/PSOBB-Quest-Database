"""Verify this checkout without requiring the original author's input folders."""
import hashlib
import json
import pathlib
import sqlite3

ROOT = pathlib.Path(__file__).resolve().parent
K = ROOT / 'analysis/quest-knowledge'

def main():
    manifest = json.loads((K / 'manifest.json').read_text(encoding='utf-8'))
    for item in manifest['files']:
        p = (K / item['snapshot']).resolve()
        assert p.is_relative_to(K), p
        assert hashlib.sha256(p.read_bytes()).hexdigest() == item['sha256'], p
    print('Preserved snapshot hashes verified:', len(manifest['files']))
    db = sqlite3.connect((K / 'quest-library.sqlite').as_uri() + '?mode=ro', uri=True)
    assert db.execute('PRAGMA integrity_check').fetchone()[0] == 'ok'
    n = db.execute('SELECT count(*) FROM quests').fetchone()[0]
    assert n == manifest['counts']['quest_variants'], n
    assert db.execute("SELECT count(*) FROM chunks_fts WHERE chunks_fts MATCH 'if_zone_clear'").fetchone()[0] > 0
    db.close()
    print('Database integrity, quest count and text search verified:', n)

if __name__ == '__main__':
    main()
