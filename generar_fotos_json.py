#!/usr/bin/env python3
"""
Ejecuta este script desde la raiz de tu repo para generar fotos.json:
  python3 generar_fotos_json.py

Requiere: pip install requests
"""
import requests, json, os, sys

GITHUB_USER   = 'normarsv'
GITHUB_REPO   = 'lachabalada'
GITHUB_BRANCH = 'main'
PHOTOS_FOLDER = 'fotos'
RAW_BASE      = f'https://raw.githubusercontent.com/{GITHUB_USER}/{GITHUB_REPO}/{GITHUB_BRANCH}/{PHOTOS_FOLDER}/'
API_BASE      = f'https://api.github.com/repos/{GITHUB_USER}/{GITHUB_REPO}/contents'
HEADERS       = {'Accept': 'application/vnd.github.v3+json'}
IMAGE_EXT     = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp'}

def fetch(path):
    r = requests.get(f'{API_BASE}/{path}?ref={GITHUB_BRANCH}', headers=HEADERS)
    r.raise_for_status()
    return r.json()

files = []

print(f'Leyendo carpeta /{PHOTOS_FOLDER}...')
root = fetch(PHOTOS_FOLDER)

for item in root:
    ext = os.path.splitext(item['name'])[1].lower()
    if item['type'] == 'file' and ext in IMAGE_EXT:
        files.append({
            'name':  item['name'],
            'album': 'Todos',
            'src':   RAW_BASE + requests.utils.quote(item['name'])
        })
    elif item['type'] == 'dir':
        print(f'  Leyendo subcarpeta: {item["name"]}...')
        try:
            sub = fetch(item['path'])
            for f in sub:
                ext2 = os.path.splitext(f['name'])[1].lower()
                if f['type'] == 'file' and ext2 in IMAGE_EXT:
                    files.append({
                        'name':  f['name'],
                        'album': item['name'],
                        'src':   f'https://raw.githubusercontent.com/{GITHUB_USER}/{GITHUB_REPO}/{GITHUB_BRANCH}/{item["path"]}/{requests.utils.quote(f["name"])}'
                    })
        except Exception as e:
            print(f'    Error: {e}')

output = 'fotos.json'
with open(output, 'w', encoding='utf-8') as fh:
    json.dump(files, fh, ensure_ascii=False, indent=2)

print(f'\n✓ {len(files)} fotos guardadas en {output}')
print('  Sube fotos.json a la raiz de tu repo en GitHub.')
