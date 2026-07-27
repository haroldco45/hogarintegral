# 📤 Cómo Subir Hogar Integral a GitHub Pages

Sigue estos pasos para publicar la app como PWA instalable en tu GitHub personal.

---

## ✅ Checklist Pre-Subida

- [ ] Renombra `hogar-integral.html` a `index.html`
- [ ] Tienes los archivos: `index.html`, `manifest.json`, `README.md`
- [ ] Cuenta de GitHub activa (haroldco45)
- [ ] Git instalado en tu computadora

---

## 🚀 Paso 1: Crear el Repositorio en GitHub

1. Ve a https://github.com/new
2. **Repository name**: `hogar-integral`
3. **Description**: "Gestión integral del hogar: calendario, gastos, mantenimiento y documentos. PWA instalable."
4. **Public** ✓
5. **Initialize with README**: Sin marcar (lo vamos a reemplazar)
6. Haz clic en "Create repository"

---

## 💻 Paso 2: Clona el Repositorio Localmente

Abre PowerShell o Terminal en tu carpeta de proyectos:

```bash
# Navega a tu carpeta de proyectos
cd C:\Mis Documentos\Proyectos
# O en Mac/Linux: cd ~/Proyectos

# Clona el repositorio
git clone https://github.com/haroldco45/hogar-integral.git

# Entra a la carpeta
cd hogar-integral
```

---

## 📁 Paso 3: Copia los Archivos

Dentro de la carpeta `hogar-integral/`, coloca estos 3 archivos:

1. **index.html** (renombrado desde hogar-integral.html)
2. **manifest.json**
3. **README.md**

La carpeta debe verse así:
```
hogar-integral/
├── index.html
├── manifest.json
├── README.md
└── .git/
```

---

## 🖼️ Paso 4: Crear la Imagen OG (Crítico para Compartir)

Necesitamos una imagen de 1200x630px que se muestre al compartir.

### Opción A: Crear imagen simple con Python

1. Instala Pillow:
```bash
pip install Pillow
```

2. Crea un archivo `create-og-image.py`:
```python
from PIL import Image, ImageDraw, ImageFont
import os

# Crear imagen 1200x630
img = Image.new('RGB', (1200, 630), color='#2C5F2D')
draw = ImageDraw.Draw(img)

# Intentar usar fuente del sistema, sino usar por defecto
try:
    title_font = ImageFont.truetype("arial.ttf", 80)
    subtitle_font = ImageFont.truetype("arial.ttf", 40)
except:
    title_font = ImageFont.load_default()
    subtitle_font = ImageFont.load_default()

# Textos
title = "Hogar Integral"
subtitle = "Gestión completa del hogar: calendario, gastos, mantenimiento y documentos"

# Dibujar título
draw.text((600, 200), title, fill='#FFFFFF', font=title_font, anchor='mm')

# Dibujar subtítulo (dividir en 2 líneas)
draw.text((600, 380), "Calendario • Gastos • Mantenimiento • Documentos", 
          fill='#E8A35D', font=subtitle_font, anchor='mm')

# Dibujar emojis
draw.text((150, 150), "🏠", font=ImageFont.load_default())
draw.text((1050, 150), "💰", font=ImageFont.load_default())

# Guardar
img.save('og-image.png')
print("✅ og-image.png creada!")
```

3. Ejecuta el script:
```bash
python create-og-image.py
```

4. Mueve `og-image.png` a la carpeta `hogar-integral/`

### Opción B: Usar un editor online (más fácil)

1. Ve a https://www.canva.com
2. Crea un diseño nuevo: 1200x630px
3. Fondo verde oscuro (#2C5F2D)
4. Título grande: "Hogar Integral"
5. Subtítulo: "Gestión del hogar: 📅 📊 🔧 📄"
6. Descarga como PNG: `og-image.png`
7. Coloca en carpeta `hogar-integral/`

---

## 📝 Paso 5: Actualizar HTML con la URL OG

El archivo `index.html` ya tiene los meta tags, pero asegúrate de reemplazar las URLs:

Busca estas líneas en el `index.html` y cámbialas con tu URL:

```html
<meta property="og:url" content="https://haroldco45.github.io/hogar-integral/">
<meta property="og:image" content="https://haroldco45.github.io/hogar-integral/og-image.png">
```

**Estas ya están así en el archivo, solo verifica que sean correctas.**

---

## 📤 Paso 6: Sube a GitHub

En PowerShell/Terminal dentro de la carpeta `hogar-integral/`:

```bash
# Agrega todos los archivos
git add .

# Crea el commit
git commit -m "chore: app hogar integral v1.0 - PWA instalable"

# Sube a GitHub
git push origin main
```

Si pide credenciales, usa tu token de GitHub como contraseña (o autenticación SSH).

---

## ⚙️ Paso 7: Activar GitHub Pages

1. Ve a tu repositorio: https://github.com/haroldco45/hogar-integral
2. Abre **Settings** (Configuración)
3. En el lado izquierdo: **Pages**
4. **Source**: Selecciona `main` y `/root`
5. Presiona **Save**

Espera 30-60 segundos. GitHub construirá tu sitio.

---

## ✨ Paso 8: Verifica que Funcione

La app estará disponible en:
```
https://haroldco45.github.io/hogar-integral/
```

**Pruebas importantes:**
- [ ] La página carga sin errores
- [ ] Aparece el botón "Instalar" (en Chrome/Edge/Edge)
- [ ] Puedo agregar eventos al calendario
- [ ] Puedo registrar gastos
- [ ] Se guardan los datos localmente
- [ ] Funciona offline (desactiva internet y prueba)

---

## 🔗 Paso 9: Compartir la App

### En Redes Sociales
```
🏠 Hogar Integral | Gestión completa del hogar

Una PWA instalable para toda la familia:
✅ Calendario sincronizado
✅ Control de gastos
✅ Alertas de mantenimiento
✅ Documentos importantes

Funciona sin internet • Tus datos en tu dispositivo

🔗 https://haroldco45.github.io/hogar-integral/
```

### En WhatsApp
- La imagen OG (1200x630) se mostrar automáticamente
- Los meta tags harán que se vea profesional

### Crear QR
Usa https://qr-code-generator.com/ para crear un QR de:
```
https://haroldco45.github.io/hogar-integral/
```

---

## 🔄 Paso 10: Actualizaciones Futuras

Para actualizar la app después:

```bash
# Edita archivos en tu carpeta local

# Agrega cambios
git add .

# Crea commit
git commit -m "feat: agregar nueva funcionalidad"

# Sube
git push origin main
```

GitHub Pages actualiza automáticamente en 30-60 segundos.

---

## 🐛 Troubleshooting

### "La app no aparece en GitHub Pages"
- Verifica que GitHub Pages esté habilitado en Settings
- Espera 2-3 minutos después de hacer push
- Abre en incógnito (Ctrl+Shift+N) para evitar caché

### "El botón Instalar no aparece"
- Solo funciona en Chrome, Edge, Firefox moderno
- Debe ser HTTPS (GitHub Pages lo proporciona)
- Debe tener manifest.json válido

### "Pierdo datos entre sesiones"
- Revisa que localStorage esté habilitado en el navegador
- En modo incógnito, localStorage se borra al cerrar
- Abre en modo normal (no incógnito)

### "Imagen OG no se muestra al compartir"
- Verifica que og-image.png esté en la carpeta
- Revisa que la URL en og:image sea correcta
- Usa https://www.opengraphcheck.com/ para validar

---

## 📊 Estructura Final en GitHub

```
hogar-integral/
├── .github/
│   └── workflows/     (GitHub Actions opcional)
├── index.html         (App principal)
├── manifest.json      (Configuración PWA)
├── og-image.png       (Imagen para compartir)
├── README.md          (Documentación)
├── GITHUB-SETUP.md    (Este archivo)
└── .gitignore         (Opcional)
```

---

## 🎉 ¡Listo!

Tu app PWA está lista para:
- ✅ Compartir en redes
- ✅ Instalar en móviles y desktop
- ✅ Funcionar sin internet
- ✅ Guardar datos localmente

**URL Final:**
```
https://haroldco45.github.io/hogar-integral/
```

---

## 💡 Tips Avanzados

### Añadir un favicon personalizado
Crea un favicon.ico y colócalo en la carpeta.

### Mejorar el Service Worker
Reemplaza el data URL del service worker con uno completo en `sw.js`.

### Analytics
Agrega Google Analytics en el index.html si quieres rastrear uso.

### Dominio personalizado
Si tienes un dominio propio, puedes configurarlo en GitHub Pages Settings.

---

**¿Preguntas?** Revisa la documentación oficial:
- PWA: https://web.dev/progressive-web-apps/
- GitHub Pages: https://docs.github.com/en/pages
- Open Graph: https://ogp.me/

¡Éxito! 🚀🏠
