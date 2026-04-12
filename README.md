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

---

## Firebase

El chismógrafo, los likes del anuario y los boletos del admin se guardan en Firebase Realtime Database. El proyecto está en `lachabalada-6c3c3`.

Para limpiar datos de prueba: [console.firebase.google.com](https://console.firebase.google.com) → Realtime Database → selecciona el nodo → eliminar.

---

## Admin

Acceso en `lachabalada.com/admin.html`. La contraseña está en el archivo `admin.html` en la línea:

```js
const ADMIN_PASSWORD = 'chabalada2026';
```

Cámbiala antes de subir a producción.

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
