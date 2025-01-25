import streamlit as st
import pandas as pd
import plotly.express as px
from get_data import load_data

# Daten laden
d_kh, d_pn, d_dg2018, d_dg2019, d_dg2020, d_dg2021, d_dg2022, d_dg2023, d_t2010, d_t2011, d_t2012, d_t2013, d_t2014, d_t2015, d_t2016, d_t2017, d_t2018, d_t2019, d_t2020,d_t2021,d_t2022,d_t2023, d_tode_insg  = load_data()
st.set_page_config(page_title="Data Literacy Dashboard", layout="wide")
st.sidebar.image("./assets/logo-TH-Köln1.png", caption="Data Literacy")
scope = pd.read_excel("./assets/scope.xlsx", index_col=False)

st.sidebar.subheader("Scope:")
st.sidebar.write(scope)


tode = d_tode_insg["Todesanzahl insgesamt"]
personal_anzahl = d_pn[["Personal", "Hauptamtliche Ärzte", "Nichtärztliches Personal"]]


data = pd.concat([tode, personal_anzahl], axis=1)


correlation_matrix = data.corr()

fig = px.imshow(
    correlation_matrix,
    text_auto=True,  
    color_continuous_scale="darkmint", 
    title="Korrelationsmatrix: Todesanzahl vs Anzahl Krankenhauspersonal"
)


fig.update_layout(
    xaxis=dict(tickangle=45),  
    coloraxis_colorbar=dict(title="Korrelation")  
)

st.title("Zusammenhänge Personal")


data = pd.DataFrame({
    "Jahr": d_pn["Datum"],
    "Nichtärztliches Personal": d_pn["Nichtärztliches Personal"],
    "Ärztliches Personal": d_pn["Hauptamtliche Ärzte"]
})

# Gestapeltes Balkendiagramm
fig_balken = px.bar(
    data,
    x="Jahr",
    y=["Nichtärztliches Personal", "Ärztliches Personal"],
    title="Vergleich: Nichtärztliches vs Ärztliches Personal",
    labels={"value": "Personalanzahl", "variable": "Personalart"},
    barmode="stack",
    text_auto=True
)

# Liniendiagramm
fig_linie = px.line(
    data,
    x="Jahr",
    y=["Nichtärztliches Personal", "Ärztliches Personal"],
    title="Entwicklung: Nichtärztliches- und ärztliches Personal",
    labels={"value": "Personalanzahl", "variable": "Personalart"},
    markers=True
)

# Streamlit-Anzeige


st.plotly_chart(fig_balken)


st.plotly_chart(fig_linie)

st.plotly_chart(fig)

st.title("Zusammenhänge COVID-19")

year = st.sidebar.selectbox(
    "Wählen Sie das Jahr:",
    options=[str(year) for year in range(2020, 2023)],
    index=0  # Standardmäßig 2010 auswählen
)

# Daten je nach ausgewähltem Jahr auswählen
selected_data = globals()[f'd_t{year}']

# Filter für COVID-19-Todesfälle im jeweiligen Jahr
covid_data = selected_data[selected_data['Todesursache'] == "COVID019, Virus nachgewiesen"]

# Visualisierung der Gesamtzahl der COVID-19-Todesfälle
covid_total_deaths = covid_data[['Kind Männlich', 'Jugendlich Männlich', 'Erwachsener Männlich', 'Senior Männlich', 
                                 'Kind Weiblich', 'Jugendlich Weiblich', 'Erwachsener Weiblich', 'Senior Weiblich']].sum()

fig_covid_total_deaths = px.bar(
    x=covid_total_deaths.index,
    y=covid_total_deaths.values,
    labels={'x': 'Altersgruppen und Geschlecht', 'y': 'Anzahl Todesfälle'},
    title=f"COVID-19 Todesfälle {year} nach Altersgruppen und Geschlecht",
    text=covid_total_deaths.values
)

st.plotly_chart(fig_covid_total_deaths)

# Visualisierung der Verteilung der COVID-19-Todesfälle nach Altersgruppen und Geschlecht
covid_age_gender_deaths = covid_data[['Kind Männlich', 'Jugendlich Männlich', 'Erwachsener Männlich', 'Senior Männlich', 
                                     'Kind Weiblich', 'Jugendlich Weiblich', 'Erwachsener Weiblich', 'Senior Weiblich']].sum()

fig_covid_age_gender = px.bar(
    x=covid_age_gender_deaths.index,
    y=covid_age_gender_deaths.values,
    labels={'x': 'Altersgruppen und Geschlecht', 'y': 'Anzahl Todesfälle'},
    title=f"Verteilung der COVID-19-Todesfälle {year} nach Altersgruppen und Geschlecht",
    text=covid_age_gender_deaths.values
)

st.plotly_chart(fig_covid_age_gender)

# Berechnung des Anteils der COVID-19-Todesfälle an den Gesamt-Todesfällen
covid_percentage = covid_data[['Kind Männlich', 'Jugendlich Männlich', 'Erwachsener Männlich', 'Senior Männlich', 
                               'Kind Weiblich', 'Jugendlich Weiblich', 'Erwachsener Weiblich', 'Senior Weiblich']].sum() / \
                      d_tode_insg[d_tode_insg['Jahr'] == int(year)]['Todesanzahl insgesamt'].sum() * 100

fig_covid_percentage = px.bar(
    x=covid_percentage.index,
    y=covid_percentage.values,
    labels={'x': 'Altersgruppen und Geschlecht', 'y': 'COVID-19 Anteil (%)'},
    title=f"Anteil der COVID-19-Todesfälle an den Gesamt-Todesfällen {year}",
    text=covid_percentage.values
)

st.plotly_chart(fig_covid_percentage)