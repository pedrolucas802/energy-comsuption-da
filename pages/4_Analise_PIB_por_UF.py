import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="Analise PIB", page_icon="💹", layout="wide")
st.title('Analise PIB - UF de 2002 a 2021')
st.write("Fonte IBGE:")
st.write(
    'https://www.ibge.gov.br/estatisticas/economicas/contas-nacionais/9088-produto-interno-bruto-dos-municipios.html?=&t=downloads')


def load_graphs(data):

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Produto Interno Bruto, a preços correntes(R$ 1.000)")

        bar_fig = px.bar(data, x="ano", y="soma_produto_interno_bruto", color="uf")
        st.plotly_chart(bar_fig)

        line_fig = px.line(data, x="ano", y="soma_produto_interno_bruto", color="uf")
        st.plotly_chart(line_fig)

        lowess_fig = px.scatter(data, x="ano", y="soma_produto_interno_bruto", trendline="lowess")
        st.plotly_chart(lowess_fig)

    with col2:
        st.subheader("Produto Interno Bruto per capita, a preços correntes(R$ 1,00)")

        bar_fig = px.bar(data, x="ano", y="soma_produto_interno_bruto_per_capita", color="uf")
        st.plotly_chart(bar_fig)

        line_fig = px.line(data, x="ano", y="soma_produto_interno_bruto_per_capita", color="uf")
        st.plotly_chart(line_fig)

        lowess_fig = px.scatter(data, x="ano", y="soma_produto_interno_bruto_per_capita", trendline="lowess")
        st.plotly_chart(lowess_fig)



    st.markdown("Dados escolhidos")
    st.write(data)

def load_data(df,selected_states):
    data = df[df['uf'].isin(selected_states)]
    load_graphs(data)

def load_screen():
    df = pd.read_csv('./data/uf_pib_ano.csv')

    selected_states = st.multiselect('UF', options=list(df['uf'].unique()), default=["CE"])

    load_data(df, selected_states)

load_screen()
