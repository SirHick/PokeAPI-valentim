import streamlit as st

def aplicar_estilo():
    estilo_css = """
    <style>
        /* Fundo principal da aplicação */
        .stApp {
            background-color: #1E1E2E;
            color: #E6E6FA;
            font-family: monospace, sans-serif;
        }
        
        /* Cor de lavanda para textos gerais e títulos */
        h1, h2, h3, p, span, label, div {
            color: #E6E6FA !important;
            font-family: monospace, sans-serif !important;
        }
        
        /* Estilização dos botões (Roxo) */
        .stButton > button {
            background-color: #9370DB !important;
            color: #FFFFFF !important;
            border: 1px solid #9370DB !important;
        }
        .stButton > button:hover {
            background-color: #7B68EE !important;
            border-color: #E6E6FA !important;
            color: #FFFFFF !important;
        }
        
        /* Caixas de texto e fundos secundários */
        .stTextInput input {
            background-color: #2D2B55 !important;
            color: #E6E6FA !important;
            border: 1px solid #9370DB !important;
        }
    </style>
    """
    st.markdown(estilo_css, unsafe_allow_html=True)