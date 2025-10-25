# 🚀 TAXONOMÍA DE LA CARPETA `kb-soporte-tecnico`Estructura 



# 📚 Base de Conocimiento – Soporte Técnico FTTH

Repositorio oficial de procedimientos, guías y documentación técnica utilizada por el agente de soporte en n8n.
Aquí se almacena el conocimiento que los técnicos y el agente consultan para resolver incidencias, ejecutar configuraciones o responder solicitudes operativas.

## 🎯 Propósito

Organizar y centralizar la información técnica de soporte para:

- Garantizar respuestas consistentes entre humanos y el agente.
- Mantener control de versiones sobre cada procedimiento.
- Permitir indexación automática en el agente (RAG / LLM).
- Facilitar la actualización colaborativa sin conocimientos de programación.

## 🗂️ Estructura del repositorio


kb-soporte-tecnico/
├── SOP/           → Procedimientos operativos estándar
├── Playbooks/     → Árboles de diagnóstico y resolución de fallas
├── Catalogos/     → Comandos, parámetros y equivalencias por equipo
├── FAQs/          → Preguntas rápidas y glosarios técnicos
├── CHANGELOG.md   → Historial de cambios de la base
└── README.md      → Este archivo (guía general)

<pre class="overflow-visible!" data-start="1394" data-end="1653"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"></div></div></pre>


## 1️⃣ **📁 SOP/** — *Procedimientos operativos estándar*

### 📌 Propósito:

Documentar **cómo ejecutar tareas repetitivas o críticas** del día a día técnico: configuración, diagnóstico, aprovisionamiento, validaciones, etc.
Son las “recetas” de operación que el agente usará para dar pasos claros y seguros.

### 📋 Contenido típico:

* Encabezado YAML con metadatos (`id`, `version`, `producto`, etc.)
* Secciones:
  * `# Objetivo`
  * `# Pasos`
  * `# Comandos de referencia`
  * `# Umbrales`
  * `# Errores comunes`
  * `# Referencias`

### 🧠 Ejemplos:

* `sop-huawei-ma5800-provisioning-v2.3.md`
* `sop-zte-reset-ont-v1.1.md`
* `sop-consulta-portafolio-cliente-v1.0.md`

### 🧩 Uso por el agente:

Cuando el técnico pregunte *“¿Cómo provisiono una ONT Huawei?”*, el agente buscará un SOP con las etiquetas `[provisionamiento, huawei, ont]` y devolverá los pasos desde ese documento.


## 2️⃣ **📁 Playbooks/** — *Guías de diagnóstico o resolución de fallas*

### 📌 Propósito:

### 📌 Propósito:

Instrucciones **condicionales o tipo árbol de decisión** para resolver fallas o incidencias.
Mientras el SOP te dice “cómo hacerlo”, el playbook te dice **“qué hacer si algo sale mal”**.

### 📋 Contenido típico:

* YAML + Markdown con:
  * `# Falla`
  * `# Árbol de decisión` (usando diagramas o listas)
  * `# Checks` (comandos de diagnóstico)
  * `# Acciones`
  * `# Validaciones finales`

### 🧠 Ejemplos:

* `playbook-ont-los-v1.2.md` → diagnóstico si la ONT tiene LED LOS encendido.
* `playbook-pppoe-autenticacion-v2.0.md` → guiar al técnico en fallas PPPoE.
* `playbook-fibra-baja-potencia-v1.0.md` → manejo de potencias ópticas anormales.

### 🧩 Uso por el agente:

Cuando la consulta es “ONT con LOS, potencia -28 dBm, O5 no levanta”, el agente recupera el playbook de esa falla y responde con las ramas de decisión y pasos recomendados.

## 3️⃣ **📁 Catalogos/** — *Comandos, parámetros y equivalencias por equipo*

### 📌 Propósito:

Almacenar los **comandos técnicos** por fabricante, modelo o entorno (OLT, router, CPE).
Ayuda al agente a traducir intenciones humanas en comandos concretos.

### 📋 Contenido típico:

* YAML/Markdown con:
  * `# Equipo`
  * `# Comandos`
  * `# Descripción`
  * `# Ejemplo`
  * `# Salida esperada`
  * `# Notas`

### 🧠 Ejemplos:

* `cli-huawei-ma5800-v6.3.md`
* `cli-zte-c320-v5.1.md`
* `cli-mikrotik-basico-v1.0.md`

### 🧩 Uso por el agente:

Cuando un SOP dice “verificar potencia óptica”, el agente consulta el catálogo correspondiente y devuelve el comando exacto para ese modelo (`display optical-module 0/1/2` o `show pon power onu ...`).

## 4️⃣ **📁 FAQs/** — *Preguntas rápidas y conceptos básicos*

### 📌 Propósito:

Respuestas cortas a preguntas recurrentes que **no requieren pasos técnicos largos**.
Es el “mini-glosario” de la operación.

### 📋 Contenido típico:

* `# Preguntas frecuentes`
* Listas tipo:
  <pre class="overflow-visible!" data-start="3425" data-end="3581"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>**¿Qué potencia óptica es normal en ONT?**</span><span>  
  Entre -15 y -27 dBm.

  </span><span>**¿Qué significa estado O5?**</span><span>  
  ONT sincronizada correctamente con OLT.
  </span></span></code></div></div></pre>

### 🧠 Ejemplos:

* `faq-soporte-ftth.md`
* `faq-conceptos-pppoe.md`
* `faq-cpe-configuracion.md`

### 🧩 Uso por el agente:

Cuando el técnico lanza algo vago como “qué es O5” o “cuánto es potencia normal”, el agente no consulta un SOP, sino las FAQs, para responder de inmediato.

## 5️⃣ **📄 CHANGELOG.md** — *Historial de cambios de la base de conocimiento*

### 📌 Propósito:

Registrar qué se ha modificado en los documentos (quién, cuándo y por qué).
Evita caos con versiones múltiples o contradicciones.

### 📋 Formato sugerido:

<pre class="overflow-visible!" data-start="4129" data-end="4321"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-md"><span><span>## [2025-10-25]</span><span>
</span><span>-</span><span> Se agrega SOP de consulta de portafolio del cliente (v1.0)
</span><span>-</span><span> Actualización de umbrales en SOP MA5800 provisioning (v2.3 → v2.4)
</span><span>-</span><span> Corrección ortográfica en FAQ FTTH
</span></span></code></div></div></pre>

### 🧩 Uso por el equipo:

Permite saber qué versión está vigente y qué cambios se deben re-indexar en el agente.

## 6️⃣ **📄 README.md** — *Guía general y normas de la base*

### 📌 Propósito:

Explicar al equipo **cómo contribuir**, **cómo nombrar archivos** y **qué formato seguir**.

### 📋 Contenido típico:

* Propósito de la base de conocimiento
* Estructura de carpetas
* Formato estándar YAML + Markdown
* Guía de versiones
* Buenas prácticas (sin pantallazos, sin datos sensibles, etc.)

### 🧩 Uso por nuevos usuarios:

Cuando alguien entra por primera vez al repo, el README es el mapa de navegación para no romper nada.
