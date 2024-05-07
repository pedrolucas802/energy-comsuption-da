import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Analise consumo", page_icon="💹", layout="wide")
st.title('Analise de crescimentos de consumo')

df = pd.read_csv('./data/uf.csv')

def load_data(selected_states, consumption_type):
    growth_data = []
    growth_mean = []
    for state in selected_states:
        state_data = df[df['sigla_uf'] == state]
        filtered_data = state_data[state_data['tipo_consumo'] == consumption_type]
        yearly_data = filtered_data.groupby('ano')['consumo'].sum().reset_index()
        yearly_data['crescimento'] = yearly_data['consumo'].diff(1).fillna(0)
        yearly_data['sigla_uf'] = state
        growth_data.extend(yearly_data.to_dict('records'))
        growth_mean.append({
            'sigla_uf': state,
            'crescimento_avg': f"{yearly_data.get('crescimento').mean():,.2f} MWh"
        })

    data = pd.DataFrame(growth_data)

    st.write("")
    st.write("Crescimento por ano")
    bar_fig = px.bar(data, x="ano", y="crescimento", color="sigla_uf")

    st.plotly_chart(bar_fig)
    line_fig = px.line(data, x="ano", y="crescimento", color="sigla_uf")

    st.plotly_chart(line_fig)

    ols_fig = px.scatter(data, x="ano", y="crescimento", trendline="ols")
    st.plotly_chart(ols_fig)

    lowess_fig = px.scatter(data, x="ano", y="crescimento",  trendline="lowess")
    st.plotly_chart(lowess_fig)

    st.markdown("Media de crescimento")
    mean_data = pd.DataFrame(growth_mean).sort_values(by='crescimento_avg', ascending=False)
    st.dataframe(mean_data)
    st.markdown("Dados escolhidos")
    st.write(data)


def load_screen():
    col1, col2 = st.columns(2)

    with col1:
        selected_states = st.multiselect('UF', options=list(df['sigla_uf'].unique()), default=["CE"])

    with col2:
        consumption_type = st.selectbox('Consumo', options=list(df['tipo_consumo'].unique()), index=0)

    load_data(selected_states, consumption_type)


load_screen()
