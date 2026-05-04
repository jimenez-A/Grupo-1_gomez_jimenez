# Convenciones de Código

## Python

- **Formateo:** PEP 8, líneas máx. 100 caracteres
- **Nombres de funciones de agente:** `agent_<rol>` en snake_case
- **Nombres de nodos LangGraph:** snake_case corto (ej. `analyst`, `writer`)
- **TypedDict:** usar `MarketingProposalState` como único estado compartido del grafo
- **LLM helper:** centralizar en `_llm(api_key, max_tokens)` para evitar repetición

## Strings de Prompts

- Los system prompts van en `SystemMessage(content="""...""")`
- Los human messages estructuran el input con separadores `━━━ SECCIÓN ━━━`
- Nunca hardcodear la API key en el código; leer de `state["api_key"]`

## Streamlit

- Configuración de página en `st.set_page_config()` al inicio, antes de cualquier widget
- CSS custom vía `st.markdown("""<style>...</style>""", unsafe_allow_html=True)`
- Estado de sesión con `st.session_state["proposal"]` para la propuesta generada
- Botones de descarga con `st.download_button()`

## Gestión de Errores

- Capturar errores de autenticación, rate limit y genéricos por separado
- Mostrar mensajes de error en español y orientados a la acción del usuario

## Archivos del Proyecto

| Archivo          | Propósito                                           |
|------------------|-----------------------------------------------------|
| `app.py`         | App principal Streamlit (agentes + UI)              |
| `_check.py`      | Validaciones y utilidades                           |
| `_writer.py`     | Helpers de generación de texto/PDF                  |
| `requirements.txt` | Dependencias Python                               |
| `CLAUDE.md`      | Descripción del proyecto para Claude Code           |
| `.env`           | Variables de entorno locales (no commitear)         |
