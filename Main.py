import pandas as pd
import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.subheader("Pedro Barreto - 2220318")
    st.title("Consumo de energia elétrica no Brasil! 💹")

    # st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        Dados mensais do consumo de energia elétrica na rede (MWh) em nível nacional e separado por classes.
        Organização
        Ministério de Minas e Energia (MME)
        Cobertura temporal:
        2004─2021
    """
    )

    st.markdown(
        """
        https://basedosdados.org/dataset/3e31e540-81ba-4665-9e72-3f81c176adad?table=b955feef-1649-428b-ba46-bc891d2facc2
    """
    )

    st.markdown(""" Introdução:""")
    st.markdown("""
    O dados estão divididos por ano e estado, cada estado possui diversos tipo de consumo no mesmo ano e separado por mês:
    """)
    tipos = ['Total', 'Cativo', 'Residencial', 'Industrial', 'Comercial', 'Outros']
    st.dataframe(tipos)

    df = pd.read_csv('./data/uf.csv')

    st.dataframe(df)


if __name__ == "__main__":
    run()
