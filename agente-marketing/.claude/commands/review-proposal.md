# /review-proposal

Revisa la propuesta generada contra el checklist de calidad del SKILL.md.

## Uso
/review-proposal

## Qué Hace
1. Lee `.claude/skills/proposal-generation/SKILL.md`
2. Aplica el checklist de calidad a st.session_state["proposal"]
3. Lista los ítems que fallan y sugiere correcciones específicas

## Criterios Revisados
- Personalización (nombre del cliente, sector, pain points)
- Estructura narrativa (11 secciones en orden)
- Persuasión (beneficios tangibles, objeciones respondidas)
- Formato Markdown (consistencia, legibilidad)
- Completitud (mínimo 800 palabras, firma, CTA activo)