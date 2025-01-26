import streamlit as st
import pandas as pd
import plotly.express as px
from get_data import load_data
from functions import interactive_plot_dev, columns_one_graph, interactive_plot_bar, columns_graph, plot_dev, plot_dev_bar, plot_dev_line, interactive_plot_dev_line, plot_dev_bar_2, plot_dev_line_2, plot_heatmap
import plotly.graph_objects as go

st.set_page_config(page_title = "Data Literacy Dashboard",layout = "wide")
st.sidebar.image("./assets/logo-TH-Köln1.png",caption = "Data Literacy")
scope = pd.read_excel("./assets/scope.xlsx", index_col=False)
st.sidebar.subheader("Scope:")
st.sidebar.write(scope)

tabs_title = [
"Kosten",
"Medizinische Einrichtungen",
"Patienten",
"Personal",
"COVID-19",

]

tab1, tab2, tab3 , tab4, tab5 = st.tabs(tabs_title)

d_kh, d_pn, d_kosten,d_ausgaben, d_dg2018, d_dg2019, d_dg2020, d_dg2021, d_dg2022, d_dg2023, d_t2010, d_t2011, d_t2012, d_t2013, d_t2014, d_t2015, d_t2016, d_t2017, d_t2018, d_t2019, d_t2020,d_t2021,d_t2022,d_t2023, d_tode_insg, tode_i_alles, bettenauslastung, verweildauer  = load_data()

with tab1:
    
    st.subheader("Kosten von deutschen Krankenhäusern 1996 - 2023")
    plot_dev_bar(d_kosten,0, 1 )

    st.subheader("Ausgaben Gesundheitswesen 1992 - 2022")

    y_axis = d_ausgaben["Jahr"]
    x_axis = d_ausgaben["Ausgaben (in Millionen Euro)"]

    plot = px.bar(d_ausgaben, x = x_axis, y=y_axis,orientation="h", color_discrete_sequence=["#FF5733"] )
    st.plotly_chart(plot)

with tab2:

    st.write(" ")
    st.subheader("Entwicklung: Krankenhäuser / Betten / Patienten")

    col1, col2 = st.columns(2)
    with col1:
        interactive_plot_dev_line(d_kh, 0, 1, 3)
    with col2:
        st.write("Anzahl Patienten:")
        plot_dev_line_2(d_kh, 0, 3)

    
    st.subheader("Bettenauslastung 2010 - 2023")
    plot_dev_bar_2(bettenauslastung,0, 1)

    st.subheader("Verweildauer 1990 - 2024")
    plot_dev_line(verweildauer, 0, 3)

    st.write("Verweildauer 1990: 14 Tage")
    st.write("Verweildauer 2024: 7 Tage")



with tab4:

    st.subheader("Entwicklung Gesamtpersonal 2010 - 2023")
    plot_dev_line(d_pn, 0, 1)

    df_personal = d_pn
    df_patients = d_kh
    df_combined= pd.concat([df_patients, df_personal], axis=1)  

    df_combined['Patienten pro Arzt (in Tausend)'] = df_combined['Patienten Anzahl'] / df_combined ['Hauptamtliche Ärzte']  
    #df_combined['Patienten pro Pflegekraft'] = df_combined['Patienten Anzahl'] / d_personal ["Nichtärztliches Personal"]  


    # Visualisierung der Daten

    st.subheader("Anzahl der Ärzte")
    plot_dev_bar_2(d_pn,0, 2)

    st.subheader("Anzahl der Patienten die ein Arzt betreuen muss")
    plot_dev_line(df_combined, 0, 14)   

    data = pd.DataFrame({
    "Jahr": d_pn["Datum"],
    "Nichtärztliches Personal": d_pn["Nichtärztliches Personal"],
    "Ärztliches Personal": d_pn["Hauptamtliche Ärzte"]
    })
    fig_balken = px.bar(
    data,
    x="Jahr",
    y=["Nichtärztliches Personal", "Ärztliches Personal"],
    title="Vergleich: Nichtärztliches vs Ärztliches Personal",
    labels={"value": "Personalanzahl", "variable": "Personalart"},
    barmode="stack",
    text_auto=True
    )
    fig_linie = px.line(
    data,
    x="Jahr",
    y=["Nichtärztliches Personal", "Ärztliches Personal"],
    title="Entwicklung: Nichtärztliches- und ärztliches Personal",
    labels={"value": "Personalanzahl", "variable": "Personalart"},
    markers=True
    )

    st.plotly_chart(fig_balken)
    st.plotly_chart(fig_linie)

    tode = d_tode_insg["Todesanzahl insgesamt"]
    personal_anzahl = d_pn[[ "Hauptamtliche Ärzte", "Nichtärztliches Personal"]]


    data = pd.concat([tode, personal_anzahl], axis=1)


    correlation_matrix = data.corr()

    fig = px.imshow(
    correlation_matrix,
    text_auto=True,  
    color_continuous_scale="darkmint", 
    title="Korrelationsmatrix: Todesanzahl vs Anzahl Krankenhauspersonal"
    )

    st.plotly_chart(fig)







with tab3:

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





    st.subheader("Entwicklung der Patienten Anzahl 2010 - 2023")
    plot_dev_line(d_kh, 0, 3)
  

    st.subheader("Entwicklung der Tode in deutschen Krankenhäusern 2010 - 2023")
    plot_dev_line(d_tode_insg, 0, 1)


    col1, col2 = st.columns(2)
    with col1:
        st.write(" ") 
        st.write(f"Durchschnittliche Todesrate 2010-2020: {sterberate_2010_2020}%")
        st.write(" ")
        st.write(f"Durchschnittliche Todesrate 2020-2022: {sterberate_2020_2022}%")
        st.write(" ")
    with col2:
        st.write(" ")
        st.write(f"Durchschnittliche Tote pro Jahr 2010-2020: {sterberate_pro_jahr_2010_2020} Millionen")
        st.write(" ")
        st.write(f"Durchschnittliche Tote pro Jahr 2020-2022: {sterberate_pro_jahr_2020_2022} Millionen")
        st.write(" ")

    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    

    st.subheader("Analyse der häufigsten Todesursachen")

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

    st.write(" ")
    st.write(" ")
    st.write(" ")


    correlation_columns = [
    'Kind Männlich', 'Jugendlich Männlich', 'Erwachsener Männlich', 'Senior Männlich',
    'Kind Weiblich', 'Jugendlich Weiblich', 'Erwachsener Weiblich', 'Senior Weiblich',
   
    ]
        
    filtered_df = todesursachen_df[correlation_columns]



    st.subheader("Korrelation zwischen verschiedenen Altersgruppen und Geschlechtern in Bezug auf Todesfälle.")

    plot_heatmap(filtered_df)

    col1, col2 = st.columns(2)
    with col1:
        st.write(" ") 
        st.write("Weibliche Senioren & Männliche Erwachsene > Erwachsene Frauen & Männliche Senioren")
        st.write(" ")
        st.write("Jugendlich Männlich & Senior Weiblich < Jugendlich Weiblich & Senior Männlich")
    with col2:
        st.write(" ")
        st.write("Erwachsene Weiblich & Erwachsene Männlich < Senioren Männlich & Erwachsen Männlich")
        st.write(" ")
        















with tab5:
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

    # Berechnung des Anteils der COVID-19-Todesfälle an den Gesamt-Todesfällen
    covid_percentage = covid_data[['Erwachsener Männlich', 'Senior Männlich', 
                                'Erwachsener Weiblich', 'Senior Weiblich']].sum() / \
                        d_tode_insg[d_tode_insg['Jahr'] == int(year)]['Todesanzahl insgesamt'].sum() * 100

    # Pie Chart für den Anteil der COVID-19-Todesfälle an den Gesamt-Todesfällen
    fig_covid_percentage_pie = px.pie(
        names=covid_percentage.index,
        values=covid_percentage.values,
        labels={'names': 'Altersgruppen und Geschlecht', 'values': 'COVID-19 Anteil (%)'},
        title=f"Anteil der COVID-19-Todesfälle an den Gesamt-Todesfällen {year}",
        hole=0.3  # Ein Loch in der Mitte, wie bei einem Donut-Diagramm (optional)
    )

    # Anzeige des Kreisdiagramms

    st.plotly_chart(fig_covid_percentage_pie)   





















   



