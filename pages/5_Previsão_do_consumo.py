import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="Analise consumo", page_icon="💹", layout="wide")
st.title('Previsão de crescimentos de consumo')

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
            'crescimento_avg': f"{yearly_data['crescimento'].mean():,.2f} MWh"
        })

        # Predict consumption growth for the next 10 years
        if len(yearly_data) >= 2:  # Check if there's enough data for prediction
            X = yearly_data['ano'].values.reshape(-1, 1)
            y = yearly_data['crescimento'].values
            model = LinearRegression()
            model.fit(X, y)
            future_years = np.arange(yearly_data['ano'].max() + 1, yearly_data['ano'].max() + 11).reshape(-1, 1)
            future_growth = model.predict(future_years)

            future_data = pd.DataFrame({'ano': future_years.flatten(), 'crescimento': future_growth, 'sigla_uf': state})
            growth_data.extend(future_data.to_dict('records'))
        else:
            st.warning(f"Not enough data available for state {state} and consumption type {consumption_type}.")

    data = pd.DataFrame(growth_data)

    st.write("")
    st.write("Crescimento por ano")
    bar_fig = px.bar(data, x="ano", y="crescimento", color="sigla_uf")
    st.plotly_chart(bar_fig)

    line_fig = px.line(data, x="ano", y="crescimento", color="sigla_uf")
    st.plotly_chart(line_fig)

    ols_fig = px.scatter(data, x="ano", y="crescimento", trendline="ols")
    st.plotly_chart(ols_fig)

    lowess_fig = px.scatter(data, x="ano", y="crescimento", trendline="lowess")
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