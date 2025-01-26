import streamlit as st
import pandas as pd
import plotly.express as px
from get_data import load_data
from functions import interactive_plot_dev, columns_one_graph, interactive_plot_bar, columns_graph, plot_dev, plot_dev_bar, plot_dev_line, interactive_plot_dev_line


st.set_page_config(page_title = "Data Literacy Dashboard",layout = "wide")
st.sidebar.image("./assets/logo-TH-Köln1.png",caption = "Data Literacy")
scope = pd.read_excel("./assets/scope.xlsx", index_col=False)
st.sidebar.subheader("Scope:")
st.sidebar.write(scope)


d_kh, d_pn, d_dg2018, d_dg2019, d_dg2020, d_dg2021, d_dg2022, d_dg2023, d_t2010, d_t2011, d_t2012, d_t2013, d_t2014, d_t2015, d_t2016, d_t2017, d_t2018, d_t2019, d_t2020,d_t2021,d_t2022,d_t2023, d_tode_insg, d_i_alles  = load_data()

st.header("Entwicklung")
st.write(" ")
st.write("Wieviele Menschen sterben von Jahr bis Jahr in Krankenhäusern?")

plot_dev_line(d_tode_insg, 0, 1)

st.write("Wieviele Krankenhäuser haben wir in Deutschland mit wievielen Mitarbeitern?")

col1, col2 = st.columns(2)
with col1:
    interactive_plot_dev_line(d_kh, 0, 1, 3)
with col2:
    st.write("Anzahl Patienten:")
    plot_dev(d_kh, 0, 3)

plot_dev_line(d_pn, 0, 1)



st.write("Ausgaben Gesundheitswesen:")
st.image("./assets/statistik_gesundheitsausgabe.jpeg")
st.write("https://de.statista.com/statistik/daten/studie/5463/umfrage/gesundheitssystem-in-deutschland-ausgaben-seit-1992")



