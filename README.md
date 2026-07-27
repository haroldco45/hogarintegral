# 🏠 Hogar Integral

**Solución completa para la gestión integral del hogar familiar**

Una aplicación web progresiva (PWA) instalable que centraliza el control del hogar en cuatro módulos: **Calendario Sincronizado**, **Control de Gastos**, **Alertas de Mantenimiento** y **Documentos Familiares Importantes**.

---

## 📋 Características Principales

### 📅 **Calendario Familiar Sincronizado**
- Vista mensual interactiva del calendario
- Agregar eventos, recordatorios y alertas
- Visualizar próximos compromisos (citas médicas, pagos, etc.)
- Indicadores visuales de días con eventos
- Gestión completa de eventos

### 💰 **Control de Gastos en la Nube**
- Registro de ingresos y egresos familiares
- Categorización automática de gastos
- Resumen mensual y análisis por categoría
- Visualización en gráficos de barras interactivos
- Historial completo de movimientos

### 🔧 **Alertas de Mantenimiento**
- Recordatorios recurrentes (semanal, mensual, trimestral, semestral, anual)
- Tareas como: limpieza de filtros A/C, revisión de tuberías, fumigación, pago de impuestos
- Estado de urgencia (tareas vencidas en rojo)
- Asignación de responsables
- Marcado como completado con actualización automática de próxima fecha

### 📄 **Documentos Familiares Importantes**
- Registro de ubicación de documentos en la nube
- Tipos: Escrituras, contratos, facturas de garantía, identidad, salud/vacunas, seguros
- Enlaces a Google Drive, OneDrive, Dropbox o similar
- Búsqueda rápida y notas adicionales
- Copia de rutas para acceso rápido

---

## 🚀 Cómo Instalar

### En el Navegador (Recomendado)
1. Accede a la aplicación web
2. Haz clic en el botón **"📥 Instalar"** en la esquina superior derecha
3. Confirma la instalación
4. ¡Listo! Abre la app desde tu escritorio o pantalla de inicio

### Manual (Si no ves el botón)
- **Chrome/Edge**: Abre el menú ⋮ > "Instalar Hogar Integral"
- **Safari (iOS)**: Toca Compartir > "Agregar a pantalla de inicio"
- **Firefox**: Abre el menú ≡ > "Instalar aplicación"

---

## 📱 Funciona Offline

- ✅ **Sin conexión a internet**: La app funciona completamente offline
- ✅ **Datos locales**: Toda la información se guarda en tu dispositivo (localStorage)
- ✅ **Sincronización**: Para sincronizar entre dispositivos, usa Google Drive, OneDrive o Dropbox (manualmente)
- ✅ **Privacidad**: Tus datos NO se envían a servidores externos

---

## 💡 Casos de Uso

### Familia
- Coordina citas médicas en el calendario compartido
- Registra gastos familiares para presupuestar juntos
- Organiza tareas de mantenimiento del hogar
- Centraliza documentos importantes (escrituras, seguros, vacunas)

### Pareja
- Planifica juntos en el calendario
- Controla ingresos y egresos mensuales
- Recibe alertas de pagos y mantenimiento
- Accede a documentos críticos desde cualquier lado

### Personas Mayores
- Interfaz simple y clara
- Recordatorios para tomar medicinas (módulo Mantenimiento)
- Control de medicamentos y documentos de salud
- Fácil de usar en tablets

---

## 📊 Estructura de Datos

Todos los datos se guardan **localmente** en tu navegador:

```
localStorage
├── hogar_events       → Eventos del calendario
├── hogar_gastos       → Movimientos financieros
├── hogar_mantenimiento → Tareas de mantenimiento
└── hogar_documentos   → Registros de documentos
```

### Cómo Exportar/Hacer Backup

1. Abre la consola del navegador (F12)
2. Copia estos comandos:
   ```javascript
   // Ver todos los datos
   console.log(JSON.stringify({
     events: JSON.parse(localStorage.getItem('hogar_events') || '[]'),
     gastos: JSON.parse(localStorage.getItem('hogar_gastos') || '[]'),
     mantenimiento: JSON.parse(localStorage.getItem('hogar_mantenimiento') || '[]'),
     documentos: JSON.parse(localStorage.getItem('hogar_documentos') || '[]')
   }, null, 2))
   ```
3. Copia el resultado a un archivo `.json` en Google Drive/OneDrive

---

## 🎯 Guía de Módulos

### 📅 Calendario
**Pasos:**
1. Selecciona una fecha o haz clic en un día
2. Escribe el título (ej: "Cita al dentista")
3. Elige tipo: Evento, Recordatorio, Alerta
4. Agrega descripción (opcional)
5. Presiona "Agregar Evento"

**Tipos:**
- **Evento** (azul): Compromisos regulares
- **Recordatorio** (naranja): Tareas pendientes
- **Alerta** (rojo): Urgencias

---

### 💰 Gastos
**Pasos:**
1. Selecciona fecha
2. Tipo: Ingreso o Egreso
3. Categoría (Servicios, Alimentos, Salud, etc.)
4. Concepto (ej: "Pago de teléfono")
5. Monto en pesos colombianos
6. Presiona "Registrar"

**Análisis:**
- El gráfico muestra el TOP 6 de categorías
- Total de ingresos y egresos del mes
- Historial ordenado cronológicamente

---

### 🔧 Mantenimiento
**Pasos:**
1. Nombre de la tarea (ej: "Limpiar filtro A/C")
2. Próxima fecha programada
3. Frecuencia (semanal, mensual, anual, etc.)
4. Responsable (opcional)
5. Presiona "Agregar Tarea"

**Estado:**
- ⚠️ **Vencida**: Mostrada en rojo si la fecha pasó
- Botón ✓: Marca como hecha y actualiza automáticamente la siguiente fecha

---

### 📄 Documentos
**Pasos:**
1. Nombre (ej: "Escritura Casa")
2. Tipo de documento
3. Ubicación en la nube (ej: "Google Drive > Mi Unidad > Casa")
4. Notas (opcional: número de folio, vencimiento, etc.)
5. Presiona "Guardar Documento"

**Ubicaciones Recomendadas:**
- **Google Drive**: `Google Drive > Carpeta Compartida > Hogar`
- **OneDrive**: `OneDrive > Documentos Importantes`
- **Dropbox**: `Dropbox > Hogar > Documentos`

---

## ⚙️ Configuración y Opciones

### Tema y Colores
- La app usa colores naturales (verde oscuro y naranjas)
- Diseñado para ser cómodo a la vista durante todo el día

### Notificaciones
- Las alertas de navegador se envían solo cuando están **vencidas**
- Para configurarlas: Abre el calendario o mantenimiento

### Idioma
- Toda la interfaz está en **español colombiano**
- Fechas en formato local (DD/MM/AAAA)

---

## 🔒 Privacidad y Seguridad

✅ **Tu privacidad está protegida:**
- Datos almacenados SOLO en tu dispositivo
- No se envía información a internet
- No hay rastreo ni publicidad
- No hay servidores externos

⚠️ **Importante:**
- Si borras el almacenamiento del navegador, perderás los datos
- Haz backups periódicamente a Google Drive
- No compartir credenciales de acceso a documentos en la nube

---

## 🐛 Solución de Problemas

### "No aparece el botón Instalar"
- Usa Chrome, Edge o un navegador moderno
- Abre desde https:// (no funciona en http)
- Intenta manual: Menú ⋮ > Instalar aplicación

### "Perdí mis datos"
- Los datos están en localStorage de tu navegador
- Si limpias el caché, se pierden
- **Siempre haz backup a Google Drive**

### "¿Funciona en mi teléfono?"
- ✅ iOS: Sí (Safari)
- ✅ Android: Sí (Chrome, Firefox)
- ✅ Desktop: Sí (todos los navegadores modernos)

### "¿Se sincroniza entre dispositivos?"
- ❌ NO automáticamente (datos locales)
- ✅ Manual: Exporta a Google Drive y re-importa en otro dispositivo

---

## 📲 Compartir la App

Usa estos links para compartir:
- **En redes**: Copia la URL y pega
- **Open Graph**: La app genera automáticamente una imagen bonita al compartir
- **QR**: Apunta con tu cámara

**Formato de compartición:**
```
Hogar Integral | Gestión del Hogar Familiar
"Una solución completa para organizar: calendario, gastos, mantenimiento y documentos"
🏠 Funciona sin internet • ☁️ Tus datos en tu dispositivo
```

---

## 🛠️ Desarrollo y Tecnología

- **HTML5 PWA** puro (sin dependencias externas)
- **localStorage** para persistencia
- **Service Worker** para funcionamiento offline
- **Responsive Design**: Mobile, tablet y desktop
- **Performance**: Carga instantánea

---

## 📞 Soporte y Contacto

**Desarrollada por:**
- **Vibras Positivas HM**
- Soluciones digitales para hogares y negocios en Colombia
- Derechos de Autor Reservados

---

## 📝 Changelog

### v1.0.0 (Inicial)
- ✅ Módulo Calendario completo
- ✅ Módulo Gastos con gráficos
- ✅ Módulo Mantenimiento con alertas
- ✅ Módulo Documentos
- ✅ PWA instalable
- ✅ Offline-first
- ✅ Responsive design

---

## 🎓 Tips de Uso

1. **Automatiza tareas**: Usa Mantenimiento para recordatorios recurrentes
2. **Categoriza gastos**: Ayuda a controlar presupuesto mensual
3. **Fecha de hoy**: El calendario resalta el día actual en verde
4. **Urgencias**: Las tareas vencidas en Mantenimiento se marcan en rojo
5. **Backup semanal**: Exporta datos a Google Drive cada viernes

---

¡Disfruta organizando tu hogar de forma inteligente! 🏡✨

**Última actualización:** 26 de julio, 2026
