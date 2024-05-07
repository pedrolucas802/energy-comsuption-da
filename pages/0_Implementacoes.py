import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Analise consumo", page_icon="💹", layout="wide")
st.title('Graficos utilizados')

df = pd.read_csv('./data/uf.csv')

def load_screen():
    st.subheader("Os graficos implementados utilizando Plotly e Streamlit:")
    st.write("Barra - utilizado para visualizar os totais de consumo por ano")
    st.write("Linha - utilizado para visualizar os totais de consumo por ano")
    st.write("OLS - Ordinary least squares")
    st.markdown(
        "método utilizado em regressão linear para encontrar a reta que melhor se ajusta a um conjunto de dados. Ele faz isso minimizando as distâncias entre os pontos de dados e a reta.")
    st.write("LOWESS (Locally Weighted Scatterplot Smoothing)")
    st.markdown(
        "Ao invés de uma reta única, ele cria uma série de retas locais, ponderando os pontos próximos a cada um dos pontos analisados. Isso permite capturar tendências não-lineares que a regressão linear comum poderia perder.")
    st.subheader("Docs:")
    st.write("https://docs.streamlit.io")
    st.write("https://plotly.com/python/linear-fits/")
    st.write("https://plotly.com/python/")

load_screen()