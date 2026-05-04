# SKILL: Generación de Propuestas Comerciales de Marketing

## Objetivo
Producir propuestas comerciales de marketing B2B en español que sean **persuasivas,
específicas y orientadas a resultados**, calibradas al perfil del decisor y al sector
del cliente.

---

## Criterios de Calidad (QA Checklist)

### 1. Personalización (Critical)
- [ ] El nombre y empresa del cliente aparecen al menos 3 veces en el cuerpo
- [ ] El sector/industria se refleja en el análisis, la estrategia y los entregables
- [ ] Los pain points mencionados vienen del brief del cliente, no son genéricos
- [ ] Los KPIs propuestos son relevantes para ese sector específico

### 2. Estructura Narrativa
- [ ] El Resumen Ejecutivo responde en 3 párrafos: problema → solución → resultado
- [ ] Cada sección prepara lógicamente la siguiente (flujo narrativo)
- [ ] La sección "Por Qué Esta Estrategia" conecta análisis → estrategia → propuesta
- [ ] "Próximos Pasos" tiene una acción concreta con verbo imperativo (Ej: "Agenda...")

### 3. Persuasión y Lenguaje
- [ ] Los beneficios son tangibles y cuantificables (evitar "mejoraremos su presencia")
- [ ] Se anticipan y responden al menos 2 objeciones implícitas
- [ ] El tono es consultivo, no vendedor (enfocado en el cliente, no en la agencia)
- [ ] Los verbos en la propuesta son de acción y resultado (lograr, aumentar, consolidar)

### 4. Formato y Legibilidad
- [ ] Encabezado formal con N° de propuesta, fecha, remitente y destinatario
- [ ] Uso consistente de Markdown: ## para secciones, **bold** para énfasis clave
- [ ] Listas de viñetas para entregables y fases (máx. 6 ítems por lista)
- [ ] Cronograma presentado en fases claras (no en fechas absolutas)
- [ ] Sección de inversión con condiciones y forma de pago explícitas

### 5. Completitud
- [ ] 11 secciones presentes en el orden definido (ver CLAUDE.md)
- [ ] Mínimo 800 palabras en el cuerpo de la propuesta
- [ ] Firma con nombre, cargo, empresa y contacto del remitente

---

## Anti-patrones a Evitar

| Anti-patrón                          | Corrección                                                      |
|--------------------------------------|-----------------------------------------------------------------|
| "Somos líderes en el mercado"        | "Hemos gestionado campañas en [sector] con resultados de [X]"  |
| KPIs genéricos (engagement, alcance) | KPIs de negocio (costo por lead, tasa de conversión, ROI)       |
| Cronograma en fechas absolutas       | Semanas/fases relativas al inicio del contrato                  |
| Precio sin contexto                  | Inversión + desglose de valor entregado                         |
| Cierre pasivo "esperamos su respuesta"| CTA activo: "Agenda una llamada de 30 min esta semana"         |

---

## Estructura de Prompt Óptima para Agentes

### Patrón de System Prompt
  Eres [ROL ESPECÍFICO] con [X] años de experiencia en [DOMINIO].
  Tu misión en esta propuesta es [OBJETIVO CONCRETO].
  Aplica [FRAMEWORK O METODOLOGÍA ESPECÍFICA].
  Output: [FORMATO ESPERADO], máximo [N] palabras.

### Patrón de Human Message
  [CONTEXTO DE INPUT PREVIO]
  ---
  [DATOS ESPECÍFICOS DEL CLIENTE]
  ---
  Genera [OUTPUT ESPECÍFICO] que cumpla:
  1. [CRITERIO 1]
  2. [CRITERIO 2]
  3. [CRITERIO 3]

---

## Frameworks de Referencia por Agente

### Agente Analista → Framework PEST + Pain-Gain-Fear
- **P**olítico/Legal del sector
- **E**conómico: presupuesto típico de marketing en ese sector
- **S**ocial: comportamiento del consumidor del cliente
- **T**ecnológico: madurez digital del sector
- **Pain:** qué problema urgente resuelve
- **Gain:** qué resultado positivo promete
- **Fear:** qué riesgo de NO contratar existe

### Agente Estratega → Messaging Hierarchy Canvas
  Core Message (1 frase)
    ├── Proof Point 1 (evidencia)
    ├── Proof Point 2 (caso/dato)
    └── Proof Point 3 (garantía/metodología)

### Agente Redactor → StoryBrand Framework Adaptado
  1. Personaje: el cliente y su situación
  2. Problema: el obstáculo específico de marketing
  3. Guía: la agencia con su expertise
  4. Plan: el servicio propuesto en fases
  5. Llamada a la acción: los próximos pasos
  6. Éxito: los resultados esperados con KPIs

### Agente Editor → Rubrica de Revisión PACT
- **P**ersonalización: ¿Parece escrita para ESTE cliente?
- **A**ccionabilidad: ¿El cliente sabe qué hacer al leerla?
- **C**laridad: ¿Cada sección puede leerse en 60 segundos?
- **T**ono: ¿Consultivo, no vendedor?
