import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

def interactive_plot_dev(df,x, spalte_von, spalte_bis):
    x_axis_val = df.columns[x]
    y_axis_val = st.selectbox("Optionen", options=df.columns[spalte_von:spalte_bis])

    plot = px.scatter(df, x = x_axis_val, y= y_axis_val)
    st.plotly_chart(plot)

def columns(df, zeile_von, zeile_bis, text):
    col1, col2 = st.columns(2)

    with col1: 
        interactive_plot_dev(df, zeile_von, zeile_bis)
    with col2: 
        st.write(text)