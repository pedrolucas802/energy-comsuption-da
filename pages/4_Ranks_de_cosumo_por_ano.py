import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Analise consumo", page_icon="💹", layout="wide")
st.title('Rnaks de consumo por ano')

df = pd.read_csv('./data/uf.csv')

## clusterizar mapa por estados e seus principais consumos

def load_data(selected_state, consumption_types):
    years_sum_array = []



def load_screen():
    col1, col2 = st.columns(2)

    with col1:
        selected_state = st.selectbox('UF', options=list(df['sigla_uf'].unique()), index=0)

    with col2:
        consumption_types = st.multiselect('Consumo', options=list(df['tipo_consumo'].unique()), default=["Total"])

    load_data(selected_state, consumption_types)


load_screen()