# La Chabalada · Generación 2006

Sitio web para la reunión de 20 años de La Chabalada.
**25 de Julio 2026 · Casino Social de Navojoa, Sonora**

---

## Páginas

| Archivo | URL | Descripción |
|---|---|---|
| `index.html` | `lachabalada.com` | Home con countdown, info del evento y preview de fotos |
| `anuario.html` | `lachabalada.com/anuario.html` | Galería de fotos organizada por álbumes |
| `chismografo.html` | `lachabalada.com/chismografo.html` | Chismógrafo digital compartido entre todos |
| `admin.html` | `lachabalada.com/admin.html` | Panel de administración (boletos, gastos y to-do) |

---

## Fotos

Las fotos van dentro de la carpeta `/fotos/`. Organízalas en subcarpetas por evento — el anuario las detecta automáticamente y crea un menú con cada subcarpeta.

```
fotos/
├── Las Bocas/
│   ├── foto1.jpg
│   └── foto2.jpg
├── Dias de Escuela/
│   └── foto3.jpg
└── ...
```

### Agregar fotos nuevas

1. Sube las fotos a la subcarpeta correcta dentro de `/fotos/` en GitHub
2. ¡Listo! El anuario las detecta automáticamente via GitHub API

Las fotos recién agregadas muestran un badge **NEW** la primera vez que alguien las visita en su navegador.

> No se necesita correr ningún script ni generar ningún archivo extra.

---

## Firebase

El chismógrafo, los comentarios del anuario, los boletos y el to-do del admin se guardan en Firebase Realtime Database. El proyecto está en `lachabalada-6c3c3`.

Para limpiar datos de prueba: [console.firebase.google.com](https://console.firebase.google.com) → Realtime Database → selecciona el nodo → eliminar.

---

## Admin

Acceso en `lachabalada.com/admin.html`. La contraseña está en el archivo `admin.html`:

```js
const ADMIN_PASSWORD = 'chabalada2026';
```

Esta URL no está linkeada en ningún lado del sitio público — solo tú sabes que existe.

### Funciones del admin

- **Boletos** — genera boletos con o sin +1, calcula precio automático ($700 / $1,400)
- **Gastos** — registra gastos con monto total, abonos parciales y barra de progreso
- **To Do** — lista de tareas con prioridad y fecha límite, guardada en Firebase

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

Si el certificado SSL da error: GitHub → Settings → Pages → borra el custom domain → guarda → escribe `lachabalada.com` de nuevo → guarda. Espera 15–30 min.

---

## Archivos en el repo

```
lachabalada/
├── index.html              ← Home principal
├── anuario.html            ← Galería de fotos
├── chismografo.html        ← Chismógrafo digital
├── admin.html              ← Panel de admin (privado)
├── favicon.jpg             ← Ícono del sitio
├── og-image.jpg            ← Thumbnail para redes sociales
├── og-image-source.html    ← Fuente para generar og-image.jpg
├── CNAME                   ← Dominio personalizado (auto-generado por GitHub)
├── README.md               ← Este archivo
└── fotos/
    ├── Las Bocas/
    ├── Dias de Escuela/
    └── ...
```
