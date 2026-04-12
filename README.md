# La Chabalada · Generación 2006

Sitio web para la reunión de 20 años de La Chabalada.
**25 de Julio 2026 · Casino Social de Navojoa, Sonora**

---

## Páginas

| Archivo | URL | Descripción |
|---|---|---|
| `index.html` | `lachabalada.com` | Home con countdown, info del evento y preview de fotos |
| `anuario.html` | `lachabalada.com/anuario.html` | Galería de fotos organizada por álbumes con likes |
| `chismografo.html` | `lachabalada.com/chismografo.html` | Chismógrafo digital compartido entre todos |
| `admin.html` | `lachabalada.com/admin.html` | Panel de administración (boletos y pagos) |

---

## Fotos

Las fotos van dentro de la carpeta `/fotos/`. Puedes organizarlas en subcarpetas por evento — el anuario las detecta automáticamente y crea un menú con cada subcarpeta.

```
fotos/
├── Las Bocas/
│   ├── foto1.jpg
│   └── foto2.jpg
├── Dias de Escuela/
│   └── foto3.jpg
└── foto_suelta.jpg
```

### Actualizar el anuario después de agregar fotos

El anuario lee las fotos desde `fotos.json` (más rápido y sin límites). Cada vez que agregues fotos nuevas al repo, regenera este archivo:

```bash
# Si tienes pip3 (Mac moderno)
pip3 install requests
python3 generar_fotos_json.py

# Si el anterior no funciona
python3 -m pip install requests
python3 generar_fotos_json.py

# Si no tienes Python, instálalo primero
brew install python3
```

Luego sube el `fotos.json` actualizado a GitHub y listo.

---

## Firebase

El chismógrafo, los likes del anuario y los boletos del admin se guardan en Firebase Realtime Database. El proyecto está en `lachabalada-6c3c3`.

Para limpiar datos de prueba: [console.firebase.google.com](https://console.firebase.google.com) → Realtime Database → selecciona el nodo → eliminar.

Para limpiar votos de prueba del navegador: F12 → Application → Local Storage → lachabalada.com → borrar claves que empiecen con `vote_` y `lachab_`.

---

## Admin

Acceso en `lachabalada.com/admin.html`. La contraseña está en el archivo `admin.html` en la línea:

```js
const ADMIN_PASSWORD = 'chabalada2026';
```

Cámbiala antes de subir a producción. Esta URL no está linkeada en ningún lado del sitio público — solo tú sabes que existe.

---

## Dominio

`lachabalada.com` apunta a GitHub Pages vía GoDaddy DNS.

| Tipo | Nombre | Valor |
|---|---|---|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | normarsv.github.io |

Si el certificado SSL da error, ve a GitHub → Settings → Pages → borra el custom domain → guarda → vuelve a escribir `lachabalada.com` → guarda. Espera 15-30 min.

---

## Archivos en el repo

```
lachabalada/
├── index.html              ← Home principal
├── anuario.html            ← Galería de fotos
├── chismografo.html        ← Chismógrafo digital
├── admin.html              ← Panel de admin (privado)
├── fotos.json              ← Lista de fotos (regenerar con el script)
├── generar_fotos_json.py   ← Script para actualizar fotos.json
├── CNAME                   ← Dominio personalizado (auto-generado por GitHub)
├── README.md               ← Este archivo
└── fotos/
    ├── Las Bocas/
    ├── Dias de Escuela/
    └── ...
```
