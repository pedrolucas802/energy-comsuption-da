
import inspect
import textwrap

import streamlit as st


def show_code(demo):
    """Showing the code of the demo."""
    show_code = st.sidebar.checkbox("Show code", True)
    if show_code:
        # Showing the code of the demo.
        st.markdown("## Code")
        sourcelines, _ = inspect.getsourcelines(demo)
        st.code(textwrap.dedent("".join(sourcelines[1:])))


# def load_data_alt(selected_states, consumption_type):
#     growth_array = []
#     for selected_state in selected_states:
#         years_sum_array = []
#         current_year = 2004
#         for j in range(18):
#             current_year_sum = 0
#             for i in range(13):
#                 month_filter = df[
#                     (df['sigla_uf'] == selected_state) & (df['mes'] == i) & (df['ano'] == current_year) & (
#                                 df['tipo_consumo'] == consumption_type)]
#                 current_year_sum += month_filter['consumo'].sum()
#             years_sum_array.append({"sigla_uf": selected_state, "ano": current_year, "tipo_consumo": current_year_sum,
#                                     "consumo": current_year_sum})
#             current_year += 1
#
#         current_year = 2004
#         for year in range(18):
#             if current_year != 2004:
#                 growth = years_sum_array[year].get("consumo") - years_sum_array[year - 1].get("consumo")
#                 growth_array.append({"sigla_uf": selected_state, "ano": current_year, "tipo_consumo": consumption_type,
#                                      "crescimento": growth})
#             current_year += 1
#
#     data = pd.DataFrame(growth_array)
#     fig = px.bar(data, x="ano", y="crescimento", color='sigla_uf')
#     st.plotly_chart(fig)
#     st.write(data)

