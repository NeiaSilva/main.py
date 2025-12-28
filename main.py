import streamlit as st
import pandas as pd

st.set_page_config(page_title='CRIANDO SITE COM PYTHON-LIRA')

with st.container():
    st.subheader("Meu primeiro site com streamlit")
    st.title("Dashboard de Contratos")
    st.write("Informações sobre os contratos fechados pela Hash&Co ao longo de maio")
    st.write("Quer aprender Python? [Clique aqui](hhttps://www.hastagtreinamentos.com/curso-python)")

@st.cache_data #adiciona uma funcionalidade para a função que vem após ele. Ele armazema no cache do usuario os dados para tornar o acesso ao site mais eficiente.
def carregar_dados():
    tabela = pd.read_csv("resultados.csv")
    return tabela

with st.container():
    st.write("---")
    qtde_dias = st.selectbox("Selecione o período", ["7D", "15D", "21D", "30D"])
    num_dias = int(qtde_dias.replace("D", ""))
    dados = carregar_dados()
    dados = dados[-num_dias:] #retorna os últimos dias estipulados na consulta
    st.area_chart(dados, x="Data", y="Contratos")

