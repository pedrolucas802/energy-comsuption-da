
import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.write("# Consumo de energia elétrica no Brasil! 👋")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        Dados mensais do consumo de energia elétrica na rede (MWh) em nível nacional e separado por classes.
        Organização
        Ministério de Minas e Energia (MME)
        Cobertura temporal:
        2004─2021
    """
    )


if __name__ == "__main__":
    run()
