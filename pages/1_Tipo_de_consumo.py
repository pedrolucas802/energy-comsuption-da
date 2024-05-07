import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Analise consumo", page_icon="💹", layout="wide")
st.title('Analise do total de tipos de consumo')

df = pd.read_csv('./data/uf.csv')


def load_data_alt(selected_state, consumption_types):
    df_filtered = df[(df['sigla_uf'] == selected_state) & (df['tipo_consumo'].isin(consumption_types))]
    fig = px.line(df_filtered, x="ano", y="consumo", color='tipo_consumo')
    st.plotly_chart(fig)
    st.write(df_filtered)


def load_data(selected_state, consumption_types):
    years_sum_array = []

    for consumption_type in consumption_types:
        current_year = 2004
        for j in range(18):
            current_year_sum = 0
            for i in range(13):
                month_filter = df[(df['sigla_uf'] == selected_state) & (df['mes'] == i) & (df['ano'] == current_year) & (df['tipo_consumo'] == consumption_type)]
                current_year_sum += month_filter['consumo'].sum()
            years_sum_array.append({"sigla_uf":selected_state,"ano":current_year ,"tipo_consumo": consumption_type,"consumo": current_year_sum})
            current_year += 1

    data = pd.DataFrame(years_sum_array)
    col1, col2 = st.columns(2)

    if (len(consumption_types) > 0):
        with col1:
            fig = px.line(data, x="ano", y="consumo", color='tipo_consumo', markers=True)  # text="consumo"
            st.plotly_chart(fig)
            st.write(data)

        with col2:
            ols_fig = px.scatter(data, x="ano", y="consumo", trendline="ols")
            st.plotly_chart(ols_fig)
            lowess_fig = px.scatter(data, x="ano", y="consumo", trendline="lowess")
            st.plotly_chart(lowess_fig)
    else:
        st.write("Selecionum tipo de consumo")


def load_screen():
    col1, col2 = st.columns(2)

    with col1:
        selected_state = st.selectbox('UF', options=list(df['sigla_uf'].unique()), index=0)

    with col2:
        consumption_types = st.multiselect('Consumo', options=list(df['tipo_consumo'].unique()), default=["Total"])

    load_data(selected_state, consumption_types)


load_screen()