import streamlit as st
import pandas as pd
import plotly.express as px

data_patienten_diagnose = pd.read_excel("../../data/raw_data/excel/data_Patienten_diagnosen.xlsx")
krankenhäuser = pd.read_excel("../../data/raw_data/excel/Krankenhäuser.xlsx")
personal = pd.read_excel("../../data/raw_data/excel/Personal.xlsx")
tode = pd.read_excel("../../data/raw_data/excel/tode.xlsx")

st.set_page_config(page_title = "Data Literacy Dashboard",layout = "wide")
st.sidebar.image("./assets/logo-TH-Köln1.png",caption = "Data Literacy")

#tode_2019 = pd.read_excel("../../data/cleaned_data/data_tode_2019_final.xlsx")


tabs_names = [
"Einleitung",
"Datengrundlage"



]

tab1, tab2 = st.tabs(tabs_names)


with tab1:
    st.title("Data Literacy Projekt im Bereich Gesundheitswesen")
    st.write("Präsentiert von: Carlo Beck und Jonathan Bach")
    st.write(" ")

    st.write(" ")
    st.subheader("Analyse von Entwicklung, Ursachen und Zusammenhänge der variierenden Sterberate in deutschen Krankenhäusern")

    st.write(" ")
    st.write(" ")
    st.subheader("Ziel:")
    st.write("Ziel der Analyse der gegebenen Gesundheitswesens-Daten ist es, auf Basis der Ergebnisse gezielte Handlungsempfehlungen zur Optimierung des Systems abzuleiten.")
    st.image("./assets/Logo-TH-Köln1.png")

with tab2:

    st.title("Datengrundlage:")
    st.write("Die Rohdaten basieren auf vier Tabellen, die aus den Datensätzen des Statistischen Bundesamts (Destatis) extrahiert wurden.")

    st.subheader("Tabelle zur Diagnose von Patienten")
    st.write(data_patienten_diagnose.head(10))

    st.subheader("Tabelle zu deutschen Krankenhäusern")
    st.write(krankenhäuser.head(10))

    st.subheader("Tabelle zum Personal in deutschen Krankenhäusern")
    st.write(personal.head(10))

    st.subheader("Tabelle zu Toden in deutschen Krankenhäusern")
    st.write(tode.head(10))

    st.write("Die Tabellen wurden durch eine gründliche Datenbereinigung für die Analyse nutzbar gemacht.")


    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.subheader("Beispielhafter Ablauf der Datenverarbeitung: data_patienten_diagnose")
    st.image("./assets/flowchart.png")

    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.subheader("Scope:")
    scope = pd.read_excel("./assets/scope.xlsx", index_col=False)
    st.write(scope)

    