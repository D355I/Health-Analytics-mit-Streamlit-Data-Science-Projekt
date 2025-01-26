import streamlit as st
import pandas as pd
import plotly.express as px
from get_data import load_data
from functions import plot_dev_line, plot_dev_bar_2, interactive_plot_bar, interactive_plot_dev_line, plot_dev_line_2

# Daten laden
d_kh, d_pn, d_kosten,d_ausgaben, d_dg2018, d_dg2019, d_dg2020, d_dg2021, d_dg2022, d_dg2023, d_t2010, d_t2011, d_t2012, d_t2013, d_t2014, d_t2015, d_t2016, d_t2017, d_t2018, d_t2019, d_t2020,d_t2021,d_t2022,d_t2023, d_tode_insg, d_i_alles, bettenauslastung, verweildauer = load_data()
st.set_page_config(page_title="Data Literacy Dashboard", layout="wide")
st.sidebar.image("./assets/logo-TH-Köln1.png", caption="Data Literacy")
scope = pd.read_excel("./assets/scope.xlsx", index_col=False)

st.sidebar.subheader("Scope:")
st.sidebar.write(scope)

st.title("Handlungsempfehlung")
st.write(" ")



st.write("__________________________________________________________________")

st.header("Personal Probleme")
col1, col2 = st.columns(2)
with col1:
    df_personal = d_pn
    df_patients = d_kh
    df_combined= pd.concat([df_patients, df_personal], axis=1)  
    df_combined['Patienten pro Arzt (in Tausend)'] = df_combined['Patienten Anzahl'] / df_combined ['Hauptamtliche Ärzte']  


    st.write("Anzahl der Ärzte")
    plot_dev_bar_2(d_pn,0, 2)

with col2: 
    st.write("Anzahl der Patienten die ein Arzt betreuen muss")
    plot_dev_line(df_combined, 0, 14)   

st.subheader("Handlungsempfehlung:")
st.write("Reduktion des Numerus Clausus (NC) für Medizinstudienplätze: Einführung von Eignungstests zur Bekämpfung des Personalmangels im Gesundheitswesen, angelehnt an das Modell der Schweiz. ")

st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")

st.write("__________________________________________________________________")

st.header("Abbau von Krankenhäusern und Betten")

col1, col2 = st.columns(2)
with col1:
    interactive_plot_dev_line(d_kh, 0, 1, 3)
with col2:
    st.write("Anzahl Patienten:")
    plot_dev_line_2(d_kh, 0, 3)

st.subheader("Handlungsempfehlung:")
st.write("Investitionen in Krankenhäuser: Steuererhöhungen zur Finanzierung von Krankenhauskapazitäten, um den Bettenabbau zu verhindern und eine frühzeitige Entlassung potenziell kranker Patienten zu vermeiden.")
st.write("Effizientere Verteilung von Krankenhausbetten: Optimierung der Bettenplanung zur besseren Auslastung und Ressourcennutzung.")

st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")

st.write("__________________________________________________________________")

st.header("Zu lange Verweildauer")
st.write("Verweildauer 1990 - 2024")
plot_dev_line(verweildauer, 0, 3)

st.subheader("Handlungsempfehlung:")
st.write("Förderung präventiver Maßnahmen: Stärkere Fokussierung auf Prävention zur Vermeidung von Krankenhausaufenthalten und Reduktion der Verweildauer.")

st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")

st.write("__________________________________________________________________")

st.header("Betroffene Risikogruppen")

 # Daten je nach ausgewähltem Jahr auswählen
year = 2021
selected_data = globals()[f'd_t{year}']

# Filter für COVID-19-Todesfälle im jeweiligen Jahr
covid_data = selected_data[selected_data['Todesursache'] == "COVID019, Virus nachgewiesen"]

# Vsualisierung der Gesamtzahl der COVID-19-Todesfälle
covid_total_deaths = covid_data[['Jugendlich Männlich', 'Erwachsener Männlich', 'Senior Männlich', 
                                    'Jugendlich Weiblich', 'Erwachsener Weiblich', 'Senior Weiblich']].sum()


    # Visualisierung der Verteilung der COVID-19-Todesfälle nach Altersgruppen und Geschlecht
covid_age_gender_deaths = covid_data[['Erwachsener Männlich', 'Senior Männlich', 
                                        'Erwachsener Weiblich', 'Senior Weiblich']].sum()

fig_covid_age_gender = px.bar(
        x=covid_age_gender_deaths.index,
        y=covid_age_gender_deaths.values,
        labels={'x': 'Altersgruppen und Geschlecht', 'y': 'Anzahl Todesfälle'},
        title=f"Verteilung der COVID-19-Todesfälle {year} nach Altersgruppen und Geschlecht",
        text=covid_age_gender_deaths.values
    )

st.plotly_chart(fig_covid_age_gender)

st.subheader("Handlungsempfehlung:")
st.write("Gezielte Forschung zu Geschlechterunterschieden: Analyse der höheren Risikogruppen, insbesondere bei Männern, um maßgeschneiderte Präventionsstrategien zu entwickeln.")

st.write("__________________________________________________________________")