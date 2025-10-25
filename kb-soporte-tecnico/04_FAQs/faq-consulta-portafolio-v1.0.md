---
id: faq-consulta-portafolio
titulo: Preguntas frecuentes – Consulta de portafolio por Telegram
version: "1.0"
estado: vigente
producto: FTTH
vendor: Neutral
modelos: [CRM-SIMULADO]
ambito: soporte-tecnico
idioma: es-CO
autor: operaciones-soporte
revision_por: supervisor-noc
fecha_publicacion: 2025-10-25
fecha_vigencia_desde: 2025-10-25
criticidad: baja
tags: [faq, telegram, portafolio, crm, json]
precondiciones: [
  "Técnico autenticado en el bot de Telegram",
  "Conectividad HTTPS hacia raw.githubusercontent.com",
  "Dataset JSON publicado en /data/"
]
riesgos: [
  "Confusión si el ID del cliente está mal digitado",
  "Uso de dataset desactualizado"
]
validaciones_salida: [
  "El bot devuelve velocidad, decodificadores y paquetes para el id solicitado",
  "Estructura de respuesta cumple formato del SOP"
]
---
# Preguntas frecuentes (FAQ)

### 1) ¿Cuál es el comando para consultar el portafolio?

Usa:
/portafolio <id_cliente>

makefile
Copy code
Ejemplo:
/portafolio 31544666

yaml
Copy code

---

### 2) ¿Qué responde el bot si todo sale bien?

Formato esperado:
Portafolio del cliente <id_cliente>
• Velocidad: <valor>
• Decodificadores: <número>
• Paquetes: <lista o "Ninguno">

yaml
Copy code

---

### 3) Me sale “Formato inválido”. ¿Por qué?

Porque no enviaste el ID correctamente.
Debe escribirse exactamente así:
/portafolio 31544666

yaml
Copy code
Sin comas, sin texto adicional, sin espacios extra.

---

### 4) Dice “No encontré ese cliente”. ¿Qué reviso?

- Que el **id_cliente** esté bien digitado.
- Que el **JSON** incluya ese registro.
- Si es un entorno nuevo, valida que se haya subido el archivo
  `data/clientes_portafolio_20.json`.

---

### 5) El bot no responde o tarda mucho. ¿Qué hago?

- Verifica que el flujo esté **activo en n8n**.
- Revisa el nodo **HTTP Request**: URL Raw correcta y con acceso.
- Si el repositorio es privado, valida el **token** de acceso y los headers (ver Catálogo).

---

### 6) ¿Dónde está la “fuente de datos” del CRM simulado?

El archivo se encuentra en el repositorio, en la carpeta:
/data/clientes_portafolio_20.json

yaml
Copy code
Para obtener la URL Raw:

1. Abre el archivo en GitHub.
2. Haz clic en el botón **Raw**.
3. Copia la URL del navegador.

---

### 7) ¿Puedo agregar o actualizar clientes?

Sí. Edita el archivo JSON y agrega un nuevo registro con el formato:

```json
{
  "id_cliente": "31544XXX",
  "nombre": "Nombre Apellido",
  "velocidad": "500Mb",
  "decodificadores": 2,
  "paquetes": ["HBO"]
}
Luego haz commit y registra el cambio en CHANGELOG.md.

8) ¿Qué valores de velocidad son válidos en el entorno simulado?
100Mb, 200Mb, 300Mb, 500Mb, 600Mb, 1Gb.

9) ¿Qué paquetes premium pueden aparecer?
HBO, Netflix, Disney+, Prime Video, Paramount+, Star+.
Si el cliente no tiene ninguno activo, el bot muestra “Ninguno”.

10) ¿Qué hago si el JSON se abre con la interfaz de GitHub y no como texto?
No copies la URL normal del archivo.
Haz clic en Raw y usa esa dirección, que muestra solo texto.
Esa es la que funciona con n8n.

Referencias
SOP: sop-consulta-portafolio-cliente-v1.0.md

Playbook: playbook-error-consulta-portafolio-v1.0.md

Catálogo: catalogo-crm-portafolio-simulado-v1.0.md
```
