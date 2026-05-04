# Generador de Propuestas Comerciales de Marketing

## Descripción del Proyecto

Aplicación Streamlit multi-agente que genera propuestas comerciales de marketing personalizadas
usando LangGraph + Claude (Anthropic). Cuatro agentes especializados trabajan en cadena y
entregan la propuesta en formato `.md` y `.pdf`.

## Stack Tecnológico

- **Frontend:** Streamlit
- **Orquestación de agentes:** LangGraph
- **LLM:** Claude (claude-haiku-4-5-20251001) via `langchain-anthropic`
- **PDF:** ReportLab
- **Entorno:** Python 3.10+, `python-dotenv`

## Arquitectura de Agentes

MarketingProposalState
        │
        ▼
  [analyst] ──► [strategist] ──► [writer] ──► [editor]
  Analista de    Estratega de     Redactor     Editor
  Mercado        Marca            Comercial    Senior

Cada agente consume el estado compartido `MarketingProposalState` y agrega su output
al mismo estado antes de pasarlo al siguiente.

## Comandos Clave

  # Instalar dependencias
  pip install -r requirements.txt

  # Ejecutar la app
  streamlit run app.py

  # Crear archivo .env con la API key
  echo "ANTHROPIC_API_KEY=sk-ant-..." > .env

## Convenciones de Código

Ver `.claude/rules/code-style.md` y `.claude/rules/agents.md`.

## Skills Disponibles

Ver `.claude/skills/proposal-generation/SKILL.md` para la guía de calidad de propuestas.

## Agentes Definidos

Ver `.claude/agents/` para la especificación de cada rol.

## Variables de Entorno

| Variable           | Descripción                                                    |
|--------------------|----------------------------------------------------------------|
| ANTHROPIC_API_KEY  | API Key de Anthropic (obligatoria si no se ingresa en UI)      |

## Exportación

La propuesta se puede descargar en:
- **Markdown (`.md`)** — texto plano con formato
- **PDF (`.pdf`)** — documento profesional con estilos corporativos