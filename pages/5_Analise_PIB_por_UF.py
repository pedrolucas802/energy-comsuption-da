import pandas as pd
import streamlit as st

st.set_page_config(page_title="Analise PIB", page_icon="💹", layout="wide")
st.title('Analise PIB - UF de 2002 a 2021')
st.write("Fonte IBGE:")
st.write(
    'https://www.ibge.gov.br/estatisticas/economicas/contas-nacionais/9088-produto-interno-bruto-dos-municipios.html?=&t=downloads')


def load_data():
    df_1 = pd.read_csv('./data/PIB_02-09.csv')
    df_2 = pd.read_csv('./data/PIB_10-21.csv')
    st.dataframe(df_1)
    st.dataframe(df_2)


def load_screen():
    load_data()


load_screen()
