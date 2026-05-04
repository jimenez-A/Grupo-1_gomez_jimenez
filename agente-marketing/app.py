import re
import io
import os
from datetime import date, datetime
import streamlit as st
from typing import TypedDict

# Importaciones de LangChain y LangGraph
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.graph import StateGraph, END

# Importaciones de ReportLab para el PDF
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

# ══════════════════════════════════════════════
# 1. CONFIGURACIÓN DE PÁGINA Y ESTILOS CSS
# ══════════════════════════════════════════════
st.set_page_config(
    page_title="Equipo de Agentes de Marketing | LangGraph + Claude",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
    .main-title {
        background: linear-gradient(135deg, #0f3460 0%, #16213e 50%, #1a1a2e 100%);
        color: white; padding: 30px 40px; border-radius: 12px;
        text-align: center; margin-bottom: 30px;
    }
    .main-title h1 { color: white !important; margin: 0 0 10px 0; font-size: 2em; }
    .main-title p  { color: #a8d8ea !important; margin: 0; font-size: 1.05em; }
    .agent-card {
        background: #f8f9fa; border: 1px solid #e0e0e0;
        border-radius: 8px; padding: 12px 16px; margin: 8px 0;
    }
    .agent-card h4 { color: #0f3460; margin: 0 0 4px 0; font-size: 0.95em; }
    .agent-card p  { color: #666; margin: 0; font-size: 0.82em; }
    .proposal-box {
        background: #ffffff; border: 1px solid #d0d7de;
        border-radius: 10px; padding: 35px; line-height: 1.8; font-size: 1.05em;
        color: #24292f; box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }
    .info-card {
        background: #e8f4f8; border-left: 5px solid #0f3460;
        border-radius: 6px; padding: 14px 20px; margin-bottom: 20px;
        font-size: 0.92em; color: #1a2f4b;
    }
    .success-banner {
        background: #d4edda; border-left: 5px solid #27ae60;
        border-radius: 6px; padding: 14px 20px; color: #155724;
        font-weight: 500; margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════
# 2. CONSTANTES Y ESTADO
# ══════════════════════════════════════════════
AGENT_LABELS = {
    "analyst": "🔍 Agente 1: Analista de Mercado",
    "strategist": "📊 Agente 2: Estratega de Marca",
    "writer": "✍️ Agente 3: Redactor Comercial",
    "editor": "✅ Agente 4: Editor Senior",
}

AGENT_DESCRIPTIONS = {
    "analyst": "Analiza al cliente, su mercado, pain points y oportunidades.",
    "strategist": "Define mensajes clave, propuesta de valor y estrategia persuasiva.",
    "writer": "Redacta la propuesta completa con todas sus secciones formales.",
    "editor": "Revisa, mejora y pule la propuesta para máximo impacto.",
}

OUTPUT_KEYS = {
    "analyst": "market_analysis",
    "strategist": "brand_strategy",
    "writer": "proposal_draft",
    "editor": "final_proposal",
}

class MarketingProposalState(TypedDict):
    api_key: str
    client_name: str
    client_company: str
    client_industry: str
    client_need: str
    target_audience: str
    service_type: str
    service_details: str
    budget_range: str
    timeline: str
    sender_company: str
    sender_name: str
    sender_role: str
    sender_contact: str
    today: str
    market_analysis: str
    brand_strategy: str
    proposal_draft: str
    final_proposal: str

# ══════════════════════════════════════════════
# 3. HELPERS (LLM, PDF)
# ══════════════════════════════════════════════
def _llm(api_key: str, max_tokens: int = 1500) -> ChatAnthropic:
    return ChatAnthropic(
        model="claude-3-5-sonnet-20240620", 
        anthropic_api_key=api_key,
        max_tokens_to_sample=max_tokens,
        temperature=0.7
    )

def _inline_md(text: str) -> str:
    if not text: return ""
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"\*(.+?)\*", r"<i>\1</i>", text)
    return text

def generate_pdf(proposal_text: str, client_company: str) -> bytes:
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=25*mm, leftMargin=25*mm, topMargin=28*mm, bottomMargin=28*mm)
    base = getSampleStyleSheet()
    sH1 = ParagraphStyle("sH1", parent=base["Heading1"], fontSize=18, textColor=HexColor("#0f3460"), spaceAfter=12)
    sBody = ParagraphStyle("sBody", parent=base["Normal"], fontSize=10, leading=14, spaceAfter=8)
    
    story = []
    for line in proposal_text.splitlines():
        line = line.strip()
        if not line: continue
        if line.startswith("# "): story.append(Paragraph(_inline_md(line[2:]), sH1))
        else: story.append(Paragraph(_inline_md(line), sBody))
    
    doc.build(story)
    return buffer.getvalue()

# ══════════════════════════════════════════════
# 4. NODOS DE LOS AGENTES
# ══════════════════════════════════════════════
def agent_market_analyst(state: MarketingProposalState):
    llm = _llm(state["api_key"])
    res = llm.invoke([SystemMessage(content="Eres un analista B2B."), HumanMessage(content=f"Analiza a {state['client_company']}.")])
    return {"market_analysis": res.content}

def agent_brand_strategist(state: MarketingProposalState):
    llm = _llm(state["api_key"])
    res = llm.invoke([SystemMessage(content="Eres un estratega senior."), HumanMessage(content=f"Estrategia basada en: {state['market_analysis']}")])
    return {"brand_strategy": res.content}

def agent_proposal_writer(state: MarketingProposalState):
    llm = _llm(state["api_key"], max_tokens=3000)
    res = llm.invoke([SystemMessage(content="Eres un redactor comercial."), HumanMessage(content=f"Redacta propuesta para {state['client_company']}.")])
    return {"proposal_draft": res.content}

def agent_editor(state: MarketingProposalState):
    llm = _llm(state["api_key"], max_tokens=3500)
    res = llm.invoke([SystemMessage(content="Eres un editor senior aplicando rúbrica PACT."), HumanMessage(content=f"Pule esta propuesta: {state['proposal_draft']}")])
    return {"final_proposal": res.content}

# ══════════════════════════════════════════════
# 5. CONSTRUCCIÓN DEL GRAFO
# ══════════════════════════════════════════════
def build_graph():
    graph = StateGraph(MarketingProposalState)
    graph.add_node("analyst", agent_market_analyst)
    graph.add_node("strategist", agent_brand_strategist)
    graph.add_node("writer", agent_proposal_writer)
    graph.add_node("editor", agent_editor)
    graph.set_entry_point("analyst")
    graph.add_edge("analyst", "strategist")
    graph.add_edge("strategist", "writer")
    graph.add_edge("writer", "editor")
    graph.add_edge("editor", END)
    return graph.compile()

# ══════════════════════════════════════════════
# 6. INTERFAZ PRINCIPAL (MAIN)
# ══════════════════════════════════════════════
def main():
    st.markdown("""
    <div class="main-title">
        <h1>🎯 Equipo de Agentes de Marketing</h1>
        <p>4 agentes especializados orquestados con <strong>LangGraph</strong> + <strong>Claude de Anthropic</strong></p>
    </div>
    """, unsafe_allow_html=True)

    with st.sidebar:
        st.header("⚙️ Configuración")
        api_key_input = st.text_input("API Key de Anthropic", type="password", placeholder="sk-ant-...")
        st.markdown("---")
        st.markdown("**🤖 Equipo de Agentes:**")
        for key, label in AGENT_LABELS.items():
            st.markdown(f'<div class="agent-card"><h4>{label}</h4><p>{AGENT_DESCRIPTIONS[key]}</p></div>', unsafe_allow_html=True)
        st.markdown("---")
        st.caption("2026 - Ing. Julian Andres Quimbayo Castro")

    with st.form("input_form"):
        st.markdown('<div class="info-card">Ingresa los datos para activar el ciclo de producción.</div>', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        client_name = c1.text_input("👤 Nombre del Contacto")
        client_company = c1.text_input("🏢 Empresa del Cliente")
        service_type = c2.selectbox("🛠️ Tipo de Servicio", ["Selecciona un servicio...", "Marketing Digital", "Estrategia B2B", "SEO & Contenidos", "Publicidad Pauta"])
        budget_range = c2.text_input("💰 Inversión Estimada")
        client_need = st.text_area("🎯 Problema a Resolver")
        
        generate_btn = st.form_submit_button("🚀 Activar Equipo de Agentes")

    if generate_btn:
        if not client_name or not client_company or service_type == "Selecciona un servicio...":
            st.error("⚠️ Completa los campos obligatorios.")
        else:
            api_key = api_key_input.strip() or os.getenv("ANTHROPIC_API_KEY", "")
            if not api_key:
                st.error("⚠️ Falta API Key.")
            else:
                initial_state = {
                    "api_key": api_key, "client_name": client_name, "client_company": client_company, "client_industry": "",
                    "client_need": client_need, "target_audience": "", "service_type": service_type, "service_details": "",
                    "budget_range": budget_range, "timeline": "", "sender_company": "Mi Agencia", "sender_name": "Julian",
                    "sender_role": "Director", "sender_contact": "", "today": date.today().strftime("%d de %B de %Y"),
                    "market_analysis": "", "brand_strategy": "", "proposal_draft": "", "final_proposal": ""
                }

                try:
                    graph = build_graph()
                    with st.status("🤖 Equipo trabajando...", expanded=True) as status:
                        for step in graph.stream(initial_state):
                            for node_name, output in step.items():
                                if node_name in AGENT_LABELS:
                                    st.write(f"**{AGENT_LABELS[node_name]}** ✅")
                                    if node_name == "editor": final_proposal = output["final_proposal"]
                        status.update(label="✅ Propuesta Generada", state="complete")
                    
                    st.session_state["proposal"] = final_proposal
                    st.session_state["proposal_client"] = client_company
                except Exception as e:
                    st.error(f"Error: {e}")

    if "proposal" in st.session_state:
        st.markdown("---")
        tab1, tab2 = st.tabs(["📄 Vista Formateada", "📝 Texto Plano"])
        with tab1:
            st.markdown(f'<div class="proposal-box">{st.session_state["proposal"]}</div>', unsafe_allow_html=True)
        with tab2:
            st.text_area("Copia el texto:", value=st.session_state["proposal"], height=400)
        
        pdf_bytes = generate_pdf(st.session_state["proposal"], st.session_state["proposal_client"])
        st.download_button("⬇️ Descargar PDF", data=pdf_bytes, file_name="propuesta.pdf", mime="application/pdf")

if __name__ == "__main__":
    main()
    