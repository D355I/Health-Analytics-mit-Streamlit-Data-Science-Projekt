import streamlit as st
import pandas as pd
import plotly.express as px
from get_data import load_data

# Daten laden
d_kh, d_pn, d_dg2018, d_dg2019, d_dg2020, d_dg2021, d_dg2022, d_dg2023, d_t2010, d_t2011, d_t2012, d_t2013, d_t2014, d_t2015, d_t2016, d_t2017, d_t2018, d_t2019, d_t2020, d_tode_insg  = load_data()
st.set_page_config(page_title="Data Literacy Dashboard", layout="wide")
st.sidebar.image("./assets/logo-TH-Köln1.png", caption="Data Literacy")

# Todesanzahl und Personalanzahl-Daten vorbereiten
tode = d_tode_insg["Todesanzahl insgesamt"]
personal_anzahl = d_pn[["Personal", "Hauptamtliche Ärzte", "Nichtärztliches Personal"]]

# DataFrame erstellen
data = pd.concat([tode, personal_anzahl], axis=1)

# Korrelationsmatrix berechnen
correlation_matrix = data.corr()

# Plotly-Visualisierung der Korrelationsmatrix
fig = px.imshow(
    correlation_matrix,
    text_auto=True,  # Werte innerhalb der Matrix anzeigen
    color_continuous_scale="darkmint",  # Farbschema für die Matrix
    title="Korrelationsmatrix: Todesanzahl vs Personalanzahl"
)

# Achsen beschriften und Layout anpassen
fig.update_layout(
    xaxis=dict(tickangle=45),  # Achsentitel rotieren
    coloraxis_colorbar=dict(title="Korrelation")  # Farbbalken beschriften
)

# Streamlit-Frontend
st.title("Korrelationsmatrix: Todesanzahl vs Personalanzahl")
st.write("Unten sehen Sie die Korrelation zwischen Todesanzahl und Personalanzahl:")
st.plotly_chart(fig)