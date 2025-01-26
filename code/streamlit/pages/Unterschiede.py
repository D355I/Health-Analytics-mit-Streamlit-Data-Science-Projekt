import streamlit as st
import pandas as pd
import plotly.express as px
from get_data import load_data
from functions import plot_dev_bar, plot_heatmap, plot_dev_line, plot_heatmap
# Streamlit-Konfiguration
st.set_page_config(page_title="Data Literacy Dashboard", layout="wide")
st.sidebar.image("./assets/logo-TH-Köln1.png", caption="Data Literacy")

# Scope-Daten laden (falls erforderlich)
scope = pd.read_excel("./assets/scope.xlsx", index_col=False)
st.sidebar.subheader("Scope:")
st.sidebar.write(scope)

# Header
st.header("Unterschiede")
st.write(" ")
st.write(" ")

# Daten laden
d_krankenhaus, d_personal, diagnose_2018, diagnose_2019, diagnose_2020, diagnose_2021, diagnose_2022, diagnose_2023, tode_2010, tode_2011, tode_2012, tode_2013, tode_2014, tode_2015, tode_2016, tode_2017, tode_2018, tode_2019, tode_2020, tode_2021, tode_2022, tode_2023, tode_insgesamt, tode_i_alles = load_data()

# Analyse der häufigsten Todesursachen
st.write("Analyse der häufigsten Todesursachen")

# Filterung und Datenvorbereitung
auszuschließen = ["Insgesamt 2014"]
todesursachen_df = tode_i_alles[~tode_i_alles["Todesursache"].isin(auszuschließen)]
todesursachen_grouped = todesursachen_df.groupby("Todesursache").sum(numeric_only=True)

# Top 5 Todesursachen berechnen
todesursachen_sum = todesursachen_grouped.sum(axis=1).sort_values(ascending=False).head(5)

# Umwandeln in ein geeignetes Format für das Plotting
todesursachen_top = pd.DataFrame({
    "Todesursache": todesursachen_sum.index,
    "Anzahl": todesursachen_sum.values
})

# Plotting mit der Funktion
plot_dev_bar(todesursachen_top, 0, 1)  # 0 = Spalte "Todesursache", 1 = Spalte "Anzahl"

correlation_columns = [
    'Kind Männlich', 'Jugendlich Männlich', 'Erwachsener Männlich', 'Senior Männlich',
    'Kind Weiblich', 'Jugendlich Weiblich', 'Erwachsener Weiblich', 'Senior Weiblich',
   
]

filtered_df = todesursachen_df[correlation_columns]


st.sidebar.subheader("Datenübersicht")
st.sidebar.write(f"Anzahl der Zeilen: {filtered_df.shape[0]}")
st.sidebar.write(f"Anzahl der Spalten: {filtered_df.shape[1]}")


st.write("Korrelation zwischen verschiedenen Altersgruppen und Geschlechtern in Bezug auf Todesfälle.")

plot_heatmap(filtered_df)



# Lade die Daten
df_personal = d_personal
df_patients = d_krankenhaus
df_combined= pd.concat([df_patients, df_personal], axis=1)

# Kombiniere die Daten anhand der Spalte "Datum" und "Jahre"

#df_combined = pd.merge(df_personal, df_patients, left_on='Datum', right_on='Jahre')


df_combined['Patienten pro Arzt'] = df_combined['Patienten Anzahl'] / df_combined['Hauptamtliche Ärzte']

st.write(df_combined.head(10))
# Visualisierung der Daten
plot_dev_line(df_combined, 0, 14)