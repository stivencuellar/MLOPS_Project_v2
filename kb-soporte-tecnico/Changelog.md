# 🧾 CHANGELOG – Base de Conocimiento Soporte Técnico

Este documento registra los cambios, adiciones y actualizaciones realizados sobre los SOP, Playbooks, Catálogos y FAQs que conforman la base de conocimiento utilizada por el agente de soporte.

---

## [2025-10-25]

### 🆕 [Agregado]

- **SOP:** `sop-consulta-portafolio-cliente-v1.0.md`
  Creación del procedimiento base que describe la consulta de portafolio del cliente a través del bot de Telegram.
  Contiene metadatos YAML, pasos operativos, errores comunes y validaciones de salida.
  **Autor:** operaciones-soporte EH
  **Revisor:** supervisor-EH

### 🆕 [Agregado]

- **Playbook:** playbook-error-consulta-portafolio-v1.0nombre-del-archivo.md
  Guía de diagnóstico para errores en la consulta del portafolio (bot, CRM o flujo n8n).Breve descripción del nuevo documento creado.
  **Autor:** Eliana Henao<nombre>
  **Revisor:** Eliana Henao

### 🆕 [Agregado]

- **Catalogo:** catalogo-crm-portafolio-v1.0playbook-error-consulta-portafolio-v1.0nombre-del-archivo.md
  ocumentación del endpoint simulado (JSON en GitHub) usado como fuente de datos para el agente.Guía de diagnóstico para errores en la consulta del portafolio (bot, CRM o flujo n8n).
  **Autor:** Eliana Henao<nombre>
  **Revisor:** Eliana Henao
-

### 🆕 [Agregado]

- **Data:** cliente_portafolio.jason
  Simulacion de una base de datos de 20 clientes con informacion de su portafolio
  **Autor:** Eliana Henao<nombre>
  **Revisor:** Eliana Henao

### 🆕 [Agregado]

- **FAQs:** faq-consulta-portafolio-v1.0
  Preguntas frecuentes sobre el flujo de consulta de portafolio en Telegram.
  **Autor:** Eliana Henao<nombre>
  **Revisor:** Eliana Henao

### ✏️ [Modificado]

- **SOP:** nombre-del-archivo.md
  Qué se cambió (por ejemplo, actualización de versión, comandos, tags).
  **Versión anterior:** v1.0 → **Nueva:** v1.1
  **Autor:** <nombre>

### 🐞 [Corregido]

- **SOP:** nombre-del-archivo.md
  Corrección de formato o error menor (sin cambio de versión).

## [2025-10-25]

🆕 [Agregado]

- **Data:** clientes_equipos.json
  Simulacion de los equipos instalados en los clientes, los datos de lso clientes ID y nombre corrsponden a los clientes que se construyeron para  informacion de su portafolio
- URLRAW: [raw.githubusercontent.com/stivencuellar/MLOPS\_Project\_v2/refs/heads/main/kb-soporte-tecnico/Data/clientes\_equipos.json](https://raw.githubusercontent.com/stivencuellar/MLOPS_Project_v2/refs/heads/main/kb-soporte-tecnico/Data/clientes_equipos.json)
  **Autor:** Eliana Henao<nombre>
  **Revisor:** Eliana Henao

### 🆕 [Agregado]

- **Data:** clientex_Infraestructura.json
  Simulacion de infraestructura asignada a cada cliente, los datos de lso clientes ID y nombre corrsponden a los clientes que se construyeron para  informacion de su portafolio
- URLRAW:[raw.githubusercontent.com/stivencuellar/MLOPS\_Project\_v2/refs/heads/main/kb-soporte-tecnico/Data/clientes\_infraestructura.json](https://raw.githubusercontent.com/stivencuellar/MLOPS_Project_v2/refs/heads/main/kb-soporte-tecnico/Data/clientes_infraestructura.json)
- **Autor:** Eliana Henao<nombre>
  **Revisor:** Eliana Henao

🆕 [Agregado]

- **Data:** clientes_parametros.json
  Simulacion de los parametros de los servicios instalados en los clientes, los datos de lso clientes ID y nombre corrsponden a los clientes que se construyeron para  informacion de su portafolio.
- los resultados podran ser identificados con estos criterios:
- potencia_rx: nivel óptico recibido en el ONT (dBm).
- Normal: entre -15 y -25 dBm
- Crítico: menor a -27 dBm
- Fuera de rango alto: mayor a -13 dBm
- potencia_tx: potencia de transmisión del equipo hacia la red.
- estado_optico:  calculado con base en `potencia_rx`
- URLRAW: [raw.githubusercontent.com/stivencuellar/MLOPS\_Project\_v2/refs/heads/main/kb-soporte-tecnico/Data/clientes\_Parametros.json](https://raw.githubusercontent.com/stivencuellar/MLOPS_Project_v2/refs/heads/main/kb-soporte-tecnico/Data/clientes_Parametros.json)
  **Autor:** Eliana Henao<nombre>
  **Revisor:** Eliana Henao

🆕 [Agregado]

- **Data:** clientes_diagnostico.json
  Simulacion de diagnostico del router instalados en los clientes, los datos de lso clientes ID y nombre corrsponden a los clientes que se construyeron para  informacion de su portafolio.
- estado_router: "Online", "Offline" o "Intermitente"
- ping_promedio_ms: tiempo promedio de respuesta en milisegundos (5–100 ms)
- uptime_dias: días desde el último reinicio del equipo
- URLRAW: [raw.githubusercontent.com/stivencuellar/MLOPS\_Project\_v2/refs/heads/main/kb-soporte-tecnico/Data/clientes\_diagnostico.json](https://raw.githubusercontent.com/stivencuellar/MLOPS_Project_v2/refs/heads/main/kb-soporte-tecnico/Data/clientes_diagnostico.json)
  **Autor:** Eliana Henao<nombre>
  **Revisor:** Eliana Henao



- **Playbook:** playbook-error-consulta-portafolio-v1.0nombre-del-archivo.md
  Guía de diagnóstico para errores en la consulta del portafolio (bot, CRM o flujo n8n).Breve descripción del nuevo documento creado.
  **Autor:** Eliana Henao<nombre>
  **Revisor:** Eliana Henao
