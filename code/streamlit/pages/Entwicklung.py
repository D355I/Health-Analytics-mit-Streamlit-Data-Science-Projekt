import streamlit as st
import pandas as pd
import plotly.express as px



st.set_page_config(page_title = "Data Literacy Dashboard",layout = "wide")
st.sidebar.image("./assets/logo-TH-Köln1.png",caption = "Data Literacy")
scope = pd.read_excel("./assets/scope.xlsx", index_col=False)
st.sidebar.subheader("Scope:")
st.sidebar.write(scope)

def load_data():
    d_krankenhaus = pd.read_excel("../../data/cleaned_data/Krankenhäuser.xlsx")
    d_personal = pd.read_excel("../../data/cleaned_data/Personal.xlsx")

    return d_krankenhaus, d_personal

d_kh, d_pn = load_data()

st.write(d_kh)