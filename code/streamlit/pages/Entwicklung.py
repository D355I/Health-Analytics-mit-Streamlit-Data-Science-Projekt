import streamlit as st
import pandas as pd
import plotly.express as px
from get_data import load_data
from functions import interactive_plot_dev, columns_one_graph, interactive_plot_bar, columns_graph, plot_dev, plot_dev_bar, plot_dev_line, interactive_plot_dev_line
import plotly.graph_objects as go

st.set_page_config(page_title = "Data Literacy Dashboard",layout = "wide")
st.sidebar.image("./assets/logo-TH-Köln1.png",caption = "Data Literacy")
scope = pd.read_excel("./assets/scope.xlsx", index_col=False)
st.sidebar.subheader("Scope:")
st.sidebar.write(scope)

tabs_title = [
"Personal und Krankenhäuser",
"Kosten"


]

tab1, tab2 = st.tabs(tabs_title)

d_kh, d_pn, d_kosten,d_ausgaben, d_dg2018, d_dg2019, d_dg2020, d_dg2021, d_dg2022, d_dg2023, d_t2010, d_t2011, d_t2012, d_t2013, d_t2014, d_t2015, d_t2016, d_t2017, d_t2018, d_t2019, d_t2020,d_t2021,d_t2022,d_t2023, d_tode_insg, d_i_alles, bettenauslastung, verweildauer  = load_data()



with tab1:

    st.header("Entwicklung")
    st.write(" ")
    st.write("Wieviele Menschen sterben von Jahr bis Jahr in Krankenhäusern?")

    plot_dev_line(d_tode_insg, 0, 1)

    sterberate = round((d_tode_insg["Todesanzahl insgesamt"].sum() / d_kh["Patienten Anzahl"].sum()) * 100, 2)
    sterberate_pro_jahr = round((d_tode_insg["Todesanzahl insgesamt"].sum() / 13) / 1000000, 2)
    st.write(f"Durchschnittliche Tote pro Jahr (2010-2023): {sterberate_pro_jahr} Millionen")
    st.write(f"Prozentteil der gestorbenen Patienten in deutschen Krankenhäusern: {sterberate}%")

    ###

    d_kh_2010_2020 = d_kh[d_kh["Jahre"] <= 2020]
    d_tode_2010_2020 = d_tode_insg[d_tode_insg["Jahr"] <= 2020]

    # Zeitraum 2020-2022
    d_kh_2020_2022 = d_kh[(d_kh["Jahre"] >= 2020) & (d_kh["Jahre"] <= 2022)]
    d_tode_2020_2022 = d_tode_insg[(d_tode_insg["Jahr"] >= 2020) & (d_tode_insg["Jahr"] <= 2022)]

    # Sterberate für Zeitraum 2010-2020 berechnen
    sterberate_2010_2020 = round((d_tode_2010_2020["Todesanzahl insgesamt"].sum() / d_kh_2010_2020["Patienten Anzahl"].sum()) * 100, 2)
    sterberate_pro_jahr_2010_2020 = round((d_tode_2010_2020["Todesanzahl insgesamt"].sum() / 11) / 1000000, 2)

    # Sterberate für Zeitraum 2020-2022 berechnen
    sterberate_2020_2022 = round((d_tode_2020_2022["Todesanzahl insgesamt"].sum() / d_kh_2020_2022["Patienten Anzahl"].sum()) * 100, 2)
    sterberate_pro_jahr_2020_2022 = round((d_tode_2020_2022["Todesanzahl insgesamt"].sum() / 3) / 1000000, 2)

    # In den DataFrames d_kh und d_pn Spalten für Sterberaten hinzufügen
    d_kh["Sterberate_2010_2020"] = sterberate_2010_2020
    d_kh["Sterberate_2020_2022"] = sterberate_2020_2022

    # Wenn du auch in d_pn eine ähnliche Berechnung hast
    d_pn["Sterberate_2010_2020"] = sterberate_2010_2020
    d_pn["Sterberate_2020_2022"] = sterberate_2020_2022

    # Ausgabe in Streamlit
    st.write(f"Durchschnittliche Todesrate 2010-2020: {sterberate_2010_2020}%")
    st.write(f"Durchschnittliche Todesrate 2020-2022: {sterberate_2020_2022}%")
    st.write(f"Durchschnittliche Tote pro Jahr 2010-2020: {sterberate_pro_jahr_2010_2020} Millionen")
    st.write(f"Durchschnittliche Tote pro Jahr 2020-2022: {sterberate_pro_jahr_2020_2022} Millionen")

    ###

    st.write(" ")
    st.write("Wieviele Krankenhäuser haben wir in Deutschland mit wievielen Mitarbeitern?")

    col1, col2 = st.columns(2)
    with col1:
        interactive_plot_dev_line(d_kh, 0, 1, 3)
    with col2:
        st.write("Anzahl Patienten:")
        plot_dev_line(d_kh, 0, 3)
       

    plot_dev_bar(bettenauslastung,0, 1)
    plot_dev_line(d_pn, 0, 1)
    #plot_dev_line(d_kh, 0, 3)

    plot_dev_line(verweildauer, 0, 3)

   # d_pn = d_pn[d_pn.iloc[:, 0] <= 2018]
   #d_kh = d_kh[d_kh.iloc[:, 0] <= 2018]

    # Ärztliches Personal gesamt berechnen und in d_pn hinzufügen
    #personal_gesamt = d_pn["Hauptamtliche Ärzte"] #+ d_pn["Nichtärztliches Personal"] 
    #d_pn["Ärztliches Personal gesamt"] = personal_gesamt

    #col1, col2 = st.columns(2)

    #with col1:
    #    plot_dev_line(d_pn, 0, 5)
    #with col2:
    #    plot_dev_line(d_kh, 0, 3)

with tab2:

    st.title("Kosten von deutschen Krankenhäusern 1996 - 2023")
    plot_dev_bar(d_kosten,0, 1 )

 



    st.write("Ausgaben Gesundheitswesen:")



    y_axis = d_ausgaben["Jahr"]
    x_axis = d_ausgaben["Ausgaben (in Millionen Euro)"]

    plot = px.bar(d_ausgaben, x = x_axis, y=y_axis,orientation="h", color_discrete_sequence=["#FF5733"] )
    st.plotly_chart(plot)