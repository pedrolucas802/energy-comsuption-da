import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Analise consumo", page_icon="💹", layout="wide")
st.title('Analise dos tipos de consumo')

df = pd.read_csv('./data/uf.csv')


def load_data(selected_state, consumption_types):
    df_filtered = df[(df['sigla_uf'] == selected_state) & (df['tipo_consumo'].isin(consumption_types))]
    fig = px.line(df_filtered, x="ano", y="consumo", color='tipo_consumo')
    st.plotly_chart(fig)


def load_screen():
    col1, col2 = st.columns(2)

    with col1:
        selected_state = st.selectbox('UF', options=list(df['sigla_uf'].unique()), index=0)

    with col2:
        consumption_types = st.multiselect('Consumo', options=list(df['tipo_consumo'].unique()), default=["Total"])

    load_data(selected_state, consumption_types)


load_screen()