import numpy as np
import plotly.express as px
import streamlit as st
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

st.set_page_config(page_title="Analise consumo", page_icon="💹", layout="wide")
st.title('Previsão de crescimentos de consumo')

def load_data():
    df = pd.read_csv("./data/uf_pib_energy_year.csv")

    data = df[['ano', 'uf', 'consumo_energia', 'soma_produto_interno_bruto']]

    predictions_energy = {}
    predictions_gdp = {}

    for uf in data['uf'].unique():
        uf_data = data[data['uf'] == uf]

        X = uf_data[['ano']]
        y_energy = uf_data['consumo_energia']
        y_gdp = uf_data['soma_produto_interno_bruto']

        X_train, X_test, y_energy_train, y_energy_test = train_test_split(X, y_energy, test_size=0.2, random_state=42)
        _, _, y_gdp_train, y_gdp_test = train_test_split(X, y_gdp, test_size=0.2, random_state=42)

        energy_reg = LinearRegression()
        energy_reg.fit(X_train, y_energy_train)

        gdp_reg = LinearRegression()
        gdp_reg.fit(X_train, y_gdp_train)

        future_years = range(uf_data['ano'].max() + 1, uf_data['ano'].max() + 11)
        future_years = pd.DataFrame(future_years, columns=['ano'])

        future_energy_pred = energy_reg.predict(future_years)
        future_gdp_pred = gdp_reg.predict(future_years)

        predictions_energy[uf] = future_energy_pred
        predictions_gdp[uf] = future_gdp_pred


    fig = px.line()
    for uf, pred_energy in predictions_energy.items():
        fig.add_scatter(x=list(range(data['ano'].min(), data['ano'].max() + 11)),
                        y=list(data[data['uf'] == uf]['consumo_energia']) + list(pred_energy),
                        mode='lines', name=uf)

    fig.update_layout(xaxis_title='Ano', yaxis_title='Consumo de Energia',
                      title='Previsão de Consumo de Energia para Cada UF',
                      legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
                      margin=dict(l=20, r=20, t=40, b=20),
                      height=600)

    fig_scatter = px.scatter(data, x='consumo_energia', y='soma_produto_interno_bruto', color='uf',
                             title='Consumo de Energia vs PIB por UF',
                             labels={'consumo_energia': 'Consumo de Energia', 'soma_produto_interno_bruto': 'PIB'},
                             hover_name='ano', hover_data=['uf'])

    # Add predicted values to the scatter plot
    for uf, pred_energy in predictions_energy.items():
        fig_scatter.add_scatter(x=predictions_energy[uf], y=predictions_gdp[uf],
                                mode='lines', name=f'Previsão {uf}')


    st.plotly_chart(fig)

    st.plotly_chart(fig_scatter)

    load_data2()

    energy_mae_train = mean_absolute_error(y_energy_train, energy_reg.predict(X_train))
    energy_mae_test = mean_absolute_error(y_energy_test, energy_reg.predict(X_test))
    energy_mse_train = mean_squared_error(y_energy_train, energy_reg.predict(X_train))
    energy_mse_test = mean_squared_error(y_energy_test, energy_reg.predict(X_test))
    energy_r2_train = r2_score(y_energy_train, energy_reg.predict(X_train))
    energy_r2_test = r2_score(y_energy_test, energy_reg.predict(X_test))

    gdp_mae_train = mean_absolute_error(y_gdp_train, gdp_reg.predict(X_train))
    gdp_mae_test = mean_absolute_error(y_gdp_test, gdp_reg.predict(X_test))
    gdp_mse_train = mean_squared_error(y_gdp_train, gdp_reg.predict(X_train))
    gdp_mse_test = mean_squared_error(y_gdp_test, gdp_reg.predict(X_test))
    gdp_r2_train = r2_score(y_gdp_train, gdp_reg.predict(X_train))
    gdp_r2_test = r2_score(y_gdp_test, gdp_reg.predict(X_test))

    st.write(f"Metrics Energia:")
    st.write("treino MAE:", energy_mae_train)
    st.write("Test MAE:", energy_mae_test)
    st.write("treino MSE:", energy_mse_train)
    st.write("Test MSE:", energy_mse_test)
    st.write("treino R-squared:", energy_r2_train)
    st.write("Test R-squared:", energy_r2_test)
    st.write()

    st.write(f"Metricas GDP:")
    st.write("treino MAE:", gdp_mae_train)
    st.write("Test MAE:", gdp_mae_test)
    st.write("treino MSE:", gdp_mse_train)
    st.write("Test MSE:", gdp_mse_test)
    st.write("treino R-squared:", gdp_r2_train)
    st.write("Test R-squared:", gdp_r2_test)
    st.write()


def load_data2():
    classified_df = pd.read_csv("./data/uf_pib_energy_year_classified.csv")

    fig_tipo_consumo = px.scatter(classified_df, x='consumo_energia', y='soma_produto_interno_bruto', color='highest_tipo_consumo',
                                  title='Consumo de Energia vs PIB por UF (Comercial vs Residencial)',
                                  labels={'consumo_energia': 'Consumo de Energia', 'soma_produto_interno_bruto': 'PIB'},
                                  hover_name='ano', hover_data=['uf', 'highest_tipo_consumo'])

    st.plotly_chart(fig_tipo_consumo)

def load_screen():
    load_data()


load_screen()