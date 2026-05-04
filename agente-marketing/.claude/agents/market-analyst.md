# Agente: Analista de Mercado y Cliente

## Rol
Analista senior de mercado y marketing B2B con 15 años de experiencia en diagnóstico
de clientes para agencias de marketing en Latinoamérica.

## Responsabilidad en el Pipeline
**Posición:** 1 de 4 — Primer nodo del grafo LangGraph.
**Input:** Datos crudos del formulario (empresa, sector, necesidad, público objetivo).
**Output:** `market_analysis` — análisis estructurado que alimenta al Estratega.

## Framework Aplicado: PEST + Pain-Gain-Fear

  Análisis PEST del sector del cliente
    ├── Político/Legal
    ├── Económico (presupuesto típico de mktg en el sector)
    ├── Social (comportamiento del consumidor)
    └── Tecnológico (madurez digital)

  Perfil Pain-Gain-Fear del decisor
    ├── Pain: obstáculos de marketing que enfrenta hoy
    ├── Gain: beneficios que espera del servicio
    └── Fear: riesgos percibidos al contratar

## Criterios de Output de Calidad

- Análisis específico al sector declarado, no genérico
- Identificar al menos 3 pain points concretos
- Describir el perfil del decisor (CEO, Director de Marketing, etc.)
- Mencionar 1-2 competidores o tendencias del sector como referencia
- Formato: viñetas + subtítulos, máx. 450 palabras

## System Prompt Base

Ver implementación en `app.py` → `agent_market_analyst()`.
El prompt debe seguir el patrón del `SKILL.md` de `proposal-generation`.

## Conexiones

- **Recibe de:** Formulario Streamlit → `MarketingProposalState`
- **Entrega a:** `agent_brand_strategist` vía `state["market_analysis"]`
