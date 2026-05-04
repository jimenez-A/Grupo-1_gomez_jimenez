# Reglas de Desarrollo de Agentes

## Principios Generales

1. **Rol específico:** Cada agente tiene un rol claro y único; no solapan responsabilidades
2. **Input explícito:** El human message siempre incluye el contexto completo necesario
3. **Output acotado:** El system prompt define el formato y el límite de palabras del output
4. **Sin estado externo:** Los agentes solo leen de `state` y solo escriben su clave de output

## Estructura de System Prompt (obligatoria)

  Eres [ROL ESPECÍFICO] con [X] años de experiencia en [DOMINIO].
  Tu misión es [OBJETIVO CONCRETO Y MEDIBLE].
  Aplica [FRAMEWORK O METODOLOGÍA].
  Formato: [Markdown/viñetas/tabla]. Máximo [N] palabras.

## Tokens y Modelos

| Agente     | max_tokens | Justificación                            |
|------------|-----------|------------------------------------------|
| analyst    | 1500      | Análisis estructurado, conciso           |
| strategist | 1500      | Estrategia y mensajes clave              |
| writer     | 3500      | Propuesta completa (11 secciones)        |
| editor     | 4096      | Propuesta completa + mejoras             |

## Flujo de Estado LangGraph

- El estado es un `TypedDict` inmutable desde la perspectiva de cada agente
- Cada agente retorna **solo** el dict con su clave de output: {"market_analysis": ...}
- LangGraph hace el merge automático al estado compartido

## Añadir un Nuevo Agente

1. Crear la función `agent_<nombre>(state: MarketingProposalState) -> dict`
2. Agregar la clave de output al `TypedDict` en `MarketingProposalState`
3. Registrar el nodo en `build_graph()`: `graph.add_node("nombre", agent_nombre)`
4. Agregar el edge correspondiente con `graph.add_edge()`
5. Actualizar `AGENT_LABELS`, `AGENT_DESCRIPTIONS` y `OUTPUT_KEYS`
6. Documentar el agente en `.claude/agents/<nombre>.md`

## Skills Aplicables

Los agentes de propuesta deben implementar los frameworks definidos en:
.claude/skills/proposal-generation/SKILL.md
