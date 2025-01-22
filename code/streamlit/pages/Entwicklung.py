import streamlit as st
import pandas as pd
import plotly.express as px
from get_data import load_data
from functions import interactive_plot_dev, columns_one_graph, interactive_plot_bar, columns_graph, plot_dev


st.set_page_config(page_title = "Data Literacy Dashboard",layout = "wide")
st.sidebar.image("./assets/logo-TH-Köln1.png",caption = "Data Literacy")
scope = pd.read_excel("./assets/scope.xlsx", index_col=False)
st.sidebar.subheader("Scope:")
st.sidebar.write(scope)

d_kh, d_pn, d_dg2018, d_dg2019, d_dg2020, d_dg2021, d_dg2022, d_dg2023 = load_data()

st.header("Entwicklung")
st.subheader("Entwicklung bei den Krankenhäusern")

#interactive_plot_bar(d_dg2018,0, 2, 7)

st.subheader("Entwicklung bei dem Personal")

# interactive_plot_dev(d_pn,0, 1, 5)

#columns(d_kh,0, 1, 5, "Hallo Welt")

# columns_graph(d_kh, 0, 1, 5, d_pn, 0, 1, 5)


plot1 = plot_dev(d_kh, 0, 1)
plot2 = plot_dev(d_pn, 0, 1)

col1 , col2 = st.columns(2)
col1.write(plot1)
col2.write(plot2)