import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

def interactive_plot_dev(df, spalte_von, spalte_bis):
    x_axis_val = df.columns[0]
    y_axis_val = st.selectbox("Optionen", options=df.columns[spalte_von:spalte_bis])

    plot = px.scatter(df, x = x_axis_val, y= y_axis_val)
    st.plotly_chart(plot)