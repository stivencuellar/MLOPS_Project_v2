---
id: playbook-error-consulta-portafolio
titulo: Manejo de fallas en la consulta de portafolio del cliente
version: "1.0"
estado: vigente
producto: FTTH
vendor: Neutral
modelos: [CRM, OSS]
ambito: soporte-tecnico
idioma: es-CO
autor: operaciones-soporte EH
revision_por: supervisor EH
fecha_publicacion: 2025-10-26
fecha_vigencia_desde: 2025-10-26
criticidad: media
tags: [telegram, crm, error, portafolio, soporte]
precondiciones: [
  "El técnico intenta consultar portafolio vía bot Telegram",
  "El bot o el CRM devuelve error 404, 401 o 500"
]
riesgos: [
  "Demora en la atención del cliente final",
  "Duplicidad de solicitudes hacia el NOC",
  "Escalamiento innecesario si no se valida causa real"
]
validaciones_salida: [
  "La causa de error queda identificada y corregida",
  "El CRM responde correctamente a la siguiente consulta"
]
---
# Falla

El técnico no recibe respuesta del bot o el sistema devuelve error durante la consulta de portafolio del cliente.

---

# Objetivo

Guiar al técnico y al analista de soporte para identificar rápidamente si la falla proviene del bot, del flujo n8n o del CRM, y definir las acciones correctivas.

---

# Árbol de decisión

```mermaid
flowchart TD
A[Inicio: Técnico reporta falla en consulta] --> B{El bot responde con error visible?}
B -- Sí --> C[Revisar tipo de error devuelto]
B -- No --> D[Verificar conectividad o token de Telegram]
C --> E{Código 404?}
E -- Sí --> F[Cliente no existe: validar número de servicio]
E -- No --> G{Código 401?}
G -- Sí --> H[Validar ID del técnico en base autorizados]
G -- No --> I{Código 500?}
I -- Sí --> J[CRM fuera de línea: escalar a NOC aplicaciones]
I -- No --> K[Reintentar o capturar logs del flujo n8n]
D --> L[Si no hay respuesta, revisar logs del flujo n8n]
L --> M[Validar webhook activo y token Telegram vigente]
```
