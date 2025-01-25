import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(page_title = "Data Literacy Dashboard",layout = "wide")
st.sidebar.image("./assets/logo-TH-Köln1.png",caption = "Data Literacy")

#tode_2019 = pd.read_excel("../../data/cleaned_data/data_tode_2019_final.xlsx")




st.header("Data Literacy Dashboard")
st.write(""" Das folgende Projekt im Wahlpflichtfach “Data Literacy” untersucht Unterschiede, Zusammenhänge und
Entwicklungen sowie Ursachen der variierenden Sterblichkeitsraten und Todesfälle in deutschen
Krankenhäusern. Dabei steht im Fokus, ob diese Faktoren durch spezifische Ursachen wie zum Beispiel
Krankheiten, Behandlungsmethoden oder Krankenhausbedingungen beeinflusst werden.
.""")

st.subheader("Datengrundlage:")
st.write("Als Rohdaten hatten wir eine Basis von 4 Tabellen zur VErfügung. Diese wurden aus Destatis herausgezogen:")
#st.write(tode_2019.head(10))