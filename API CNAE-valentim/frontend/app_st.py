import streamlit as st
import requests
from style import aplicar_estilo

# URL base da sua API Flask local
FLASK_URL = "http://127.0.0.1:5000"

st.set_page_config(page_title="CNAE Explorer", page_icon="💻", layout="centered")

# Aplica o tema visual do ficheiro style.py
aplicar_estilo()

st.title("💻 CNAE API Explorer")
st.caption("Interface de consulta para a API Flask do IBGE.")

col1, col2 = st.columns([1, 2])

with col1:
    tipo_consulta = st.radio(
        "Selecione o endpoint:",
        ("Classes", "Subclasses", "Seções")
    )

with col2:
    endpoints = {
        "Classes": "classes",
        "Subclasses": "subclasses",
        "Seções": "secoes"
    }
    endpoint = endpoints[tipo_consulta]
    
    id_busca = st.text_input(
        f"Buscar por ID ({tipo_consulta})", 
        placeholder="Deixe em branco para listar todos"
    )
    
    buscar = st.button(f"Executar GET /{endpoint}{'/' + id_busca if id_busca else ''}")

st.divider()

if buscar:
    url_alvo = f"{FLASK_URL}/{endpoint}"
    if id_busca:
        url_alvo += f"/{id_busca.strip()}"
    
    with st.spinner("A aguardar resposta do servidor Flask..."):
        try:
            resposta = requests.get(url_alvo)
            
            if resposta.status_code == 200:
                st.success("Status 200: OK")
                st.json(resposta.json())
            elif resposta.status_code == 404:
                st.warning("Código 404: Registo não encontrado.")
            else:
                st.error(f"Erro {resposta.status_code}: {resposta.text}")
                
        except requests.exceptions.ConnectionError:
            st.error("Falha na ligação. Verifique se a sua API Flask está a correr no terminal.")