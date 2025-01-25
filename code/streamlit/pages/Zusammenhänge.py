import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from get_data import load_data

d_kh, d_pn, d_dg2018, d_dg2019, d_dg2020, d_dg2021, d_dg2022, d_dg2023, d_t2010, d_t2011, d_t2012, d_t2013, d_t2014, d_t2015, d_t2016, d_t2017, d_t2018, d_t2019, d_t2020, d_tode_insg  = load_data()
st.set_page_config(page_title = "Data Literacy Dashboard",layout = "wide")
st.sidebar.image("./assets/logo-TH-Köln1.png",caption = "Data Literacy")

tode = d_tode_insg["Todesanzahl insgesamt"]
personal_anzahl = d_pn[["Personal", "Hauptamtliche Ärzte", "Nichtärztliches Personal"]]

data = pd.concat([tode, personal_anzahl], axis=1)

# Korrelationsmatrix berechnen
correlation_matrix = data.corr()

# Korrelationsmatrix visualisieren
fig, ax = plt.subplots(figsize=(6, 4))
cax = ax.matshow(correlation_matrix, cmap="coolwarm")
fig.colorbar(cax)

# Achsen beschriften
ax.set_xticks(range(len(correlation_matrix.columns)))
ax.set_xticklabels(correlation_matrix.columns, rotation=45)
ax.set_yticks(range(len(correlation_matrix.columns)))
ax.set_yticklabels(correlation_matrix.columns)

# Titel setzen
ax.set_title("Korrelationsmatrix: Todesanzahl vs Personalanzahl", pad=20)

# Streamlit-Frontend
st.title("Korrelationsmatrix: Todesanzahl vs Personalanzahl")
st.write("Unten sehen Sie die Korrelation zwischen Todesanzahl und Personalanzahl:")
st.pyplot(fig)