---
id: sop-consulta-portafolio-cliente
titulo: Consulta de portafolio del cliente desde Telegram
version: "1.0"
estado: vigente
producto: FTTH
vendor: Neutral
modelos: [CRM, OSS]
ambito: soporte-tecnico
idioma: es-CO
autor: operaciones-soporte EH
revision_por: supervisor EH
fecha_publicacion: 2025-10-24
fecha_vigencia_desde: 2025-10-24
criticidad: baja
tags: [consulta, portafolio, cliente, megas, contratada, contratado, cantidad, canales, premium, HBO]
precondiciones: [
  "Técnico autenticado en el bot de Telegram",
  "Cliente identificado por número de servicio o contrato",
  "Sistema CRM disponible"
]
riesgos: [
  "Divulgación de información sensible si no se valida identidad del técnico"
]
validaciones_salida: [
  "El portafolio mostrado corresponde al cliente consultado",
  "Los valores de velocidad y servicios coinciden con el CRM"
]
---
# Objetivo

Permitir que un técnico de campo consulte el portafolio completo del cliente desde Telegram, accediendo a la información de su servicio activo registrada en el sistema CRM.

# Pasos

1. El técnico ingresa el ID Visita .
2. El bot valida el ID Visita.
3. El flujo en n8n consulta el CRM y devuelve velocidad, decodificadores y paquetes activos.

# Ejemplo de salida

> Cliente 31544666:
>
> - 3 decodificadores activos
> - Banda ancha 500 Mb
> - Paquete premium HBO activo

---
