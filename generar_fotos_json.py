#!/usr/bin/env python3
"""
Genera fotos.json con todas las imágenes del repo.
Preserva el campo added_at de fotos ya existentes para que el badge "NEW"
solo aparezca en fotos realmente nuevas (menos de 48h).

Ejecutar desde la raiz del repo:
  python3 generar_fotos_json.py
"""
import urllib.request
import urllib.parse
import json
import os
import time

GITHUB_USER   = 'normarsv'
GITHUB_REPO   = 'lachabalada'
GITHUB_BRANCH = 'main'
PHOTOS_FOLDER = 'fotos'
RAW_BASE      = f'https://raw.githubusercontent.com/{GITHUB_USER}/{GITHUB_REPO}/{GITHUB_BRANCH}/{PHOTOS_FOLDER}/'
API_BASE      = f'https://api.github.com/repos/{GITHUB_USER}/{GITHUB_REPO}/contents'
IMAGE_EXT     = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp'}

def fetch(path):
    url = f'{API_BASE}/{path}?ref={GITHUB_BRANCH}'
    req = urllib.request.Request(url, headers={'Accept': 'application/vnd.github.v3+json'})
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read().decode())

# Load existing fotos.json to preserve added_at timestamps
existing = {}
if os.path.exists('fotos.json'):
    try:
        with open('fotos.json', 'r', encoding='utf-8') as fh:
            for entry in json.load(fh):
                key = entry.get('album', '') + '/' + entry.get('name', '')
                if 'added_at' in entry:
                    existing[key] = entry['added_at']
        print(f'  Preservando timestamps de {len(existing)} fotos existentes.')
    except Exception as e:
        print(f'  No se pudo leer fotos.json existente: {e}')

now_ms = int(time.time() * 1000)
files  = []

print(f'Leyendo carpeta /{PHOTOS_FOLDER}...')
root = fetch(PHOTOS_FOLDER)

for item in root:
    ext = os.path.splitext(item['name'])[1].lower()
    if item['type'] == 'file' and ext in IMAGE_EXT:
        key      = 'Todos/' + item['name']
        added_at = existing.get(key, now_ms)
        files.append({
            'name':     item['name'],
            'album':    'Todos',
            'src':      RAW_BASE + urllib.parse.quote(item['name']),
            'added_at': added_at
        })
    elif item['type'] == 'dir':
        print(f'  Leyendo subcarpeta: {item["name"]}...')
        try:
            sub = fetch(item['path'])
            for f in sub:
                ext2 = os.path.splitext(f['name'])[1].lower()
                if f['type'] == 'file' and ext2 in IMAGE_EXT:
                    key      = item['name'] + '/' + f['name']
                    added_at = existing.get(key, now_ms)
                    files.append({
                        'name':     f['name'],
                        'album':    item['name'],
                        'src':      f'https://raw.githubusercontent.com/{GITHUB_USER}/{GITHUB_REPO}/{GITHUB_BRANCH}/{item["path"]}/{urllib.parse.quote(f["name"])}',
                        'added_at': added_at
                    })
        except Exception as e:
            print(f'    Error en {item["name"]}: {e}')

new_count = sum(1 for f in files if f['added_at'] == now_ms)

with open('fotos.json', 'w', encoding='utf-8') as fh:
    json.dump(files, fh, ensure_ascii=False, indent=2)

print(f'\n✓ {len(files)} fotos guardadas en fotos.json')
print(f'  {new_count} fotos nuevas con badge "NEW" (duran 48h)')
print('  Sube fotos.json a la raiz de tu repo en GitHub.')
