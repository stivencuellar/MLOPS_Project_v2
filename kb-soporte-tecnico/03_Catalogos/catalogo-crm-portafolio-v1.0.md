titulo: Catálogo de consulta de portafolio (fuente JSON en GitHub)
version: "1.0"
estado: vigente
producto: FTTH
vendor: Neutral
modelos: [CRM-SIMULADO]
ambito: soporte-aplicativo
idioma: es-CO
autor: operaciones-soporte EH
revision_por: equipo-ti
fecha_publicacion: 2025-10-25
fecha_vigencia_desde: 2025-10-25
criticidad: baja
tags: [crm, api, json, portafolio, simulacion, github]
precondiciones: [
"Conectividad HTTPS hacia raw.githubusercontent.com",
"Archivo JSON publicado en el repo bajo /data/",
"El id_cliente que consulta el técnico existe en el JSON"
]
riesgos: [
"Datos estáticos; requieren actualización manual",
"Posible retraso por caché del CDN de GitHub"
]
validaciones_salida: [
"Respuesta JSON válida",
"Estructura con campos esperados",
"Coincidencia exacta por id_cliente"
]
---
# Objetivo

Definir el uso del archivo JSON alojado en GitHub que actúa como base simulada del CRM para que el flujo n8n o el agente IA pueda consultar el portafolio del cliente de forma controlada y repetible.

# Endpoint simulado (lectura)

**Método:** `GET`
**URL base (ejemplo):**
[https://raw.githubusercontent.com/stivencuellar/MLOPS_Project_v2/main/data/clientes_portafolio.json](https://raw.githubusercontent.com/stivencuellar/MLOPS_Project_v2/main/data/clientes_portafolio.json)
