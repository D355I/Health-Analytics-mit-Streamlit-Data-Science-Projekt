import streamlit as st
import pandas as pd
import plotly.express as px
from get_data import load_data
from functions import interactive_plot_dev


st.set_page_config(page_title = "Data Literacy Dashboard",layout = "wide")
st.sidebar.image("./assets/logo-TH-Köln1.png",caption = "Data Literacy")
scope = pd.read_excel("./assets/scope.xlsx", index_col=False)
st.sidebar.subheader("Scope:")
st.sidebar.write(scope)

d_kh, d_pn, d_dg2018, d_dg2019, d_dg2020, d_dg2021, d_dg2022, d_dg2023 = load_data()

st.header("Entwicklung")
st.subheader("Entwicklung bei den Krankenhäusern")

interactive_plot_dev(d_kh, 1, 5)

st.subheader("Entwicklung bei dem Personal")

interactive_plot_dev(d_pn, 1, 5)