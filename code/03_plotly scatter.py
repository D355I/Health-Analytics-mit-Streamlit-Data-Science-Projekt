import streamlit as st
import duckdb as h
import plotly.express as px


def plot_bottom_left():
    # Beispielhafte SQL-Abfrage mit den Spalten "Krankenhäuser" und "Patienten"
    query = """
    SELECT 'Krankenhaus A' AS Krankenhaus, Patient AS Patienten
    UNION ALL SELECT 'Krankenhaus ', 
    UNION ALL SELECT 'Patienten', 

    """

    # Abfrage ausführen und Daten in ein DataFrame laden
    data = h.query(query).to_df()

    # Diagramm erstellen
    fig = px.bar(
        data,
        x="Krankenhaus",
        y="Patienten",
        text="Patienten",
        title="Patientenanzahl pro Krankenhaus"
    )

    fig.update_traces(textposition="outside")
    st.plotly_chart(fig, use_container_width=True)


# Funktion aufrufen
plot_bottom_left()
