import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
from get_data import load_data


def interactive_plot_dev(df,x, spalte_von, spalte_bis):
    x_axis_val = df.columns[x]
    y_axis_val = st.selectbox("Optionen", options=df.columns[spalte_von:spalte_bis])

    plot = px.scatter(df, x = x_axis_val, y= y_axis_val)
    st.plotly_chart(plot)

def columns_one_graph(df,x, zeile_von, zeile_bis, text):
    col1, col2 = st.columns(2)

    with col1: 
        interactive_plot_dev(df,x, zeile_von, zeile_bis)
    with col2: 
        st.write(text)

def interactive_plot_bar(df, y, spalte_von, spalte_bis):
    y_axis_val = df.columns[y]
    x_axis_val = st.selectbox("Optionen", options=df.columns[spalte_von:spalte_bis])

    plot = px.bar(df, x = x_axis_val, y= y_axis_val)
    st.plotly_chart(plot)

def columns_graph(df,x, zeile_von, zeile_bis, df2, x_2, zeile_von2, zeile_bis2):
    col1, col2 = st.columns(2)

    with col1: 
        interactive_plot_dev(df,x, zeile_von, zeile_bis)
    with col2: 
        interactive_plot_dev(df2,x_2, zeile_von2, zeile_bis2)

def plot_dev(df, x, y):
    x_axis = df.columns[x]
    y_axis = df.columns[y]
    plot = px.scatter(df, x=x_axis, y=y_axis)
    st.plotly_chart(plot)

def plot_dev_bar(df, x, y):
    x_axis = df.columns[x]
    y_axis = df.columns[y]
    plot = px.bar(df, x=x_axis, y=y_axis)
    st.plotly_chart(plot)

def plot_dev_line(df, x, y):
    x_axis = df.columns[x]
    y_axis = df.columns[y]
    plot = px.line(df, x=x_axis, y=y_axis, markers=True)
    st.plotly_chart(plot)

def interactive_plot_dev_line(df,x, spalte_von, spalte_bis):
    x_axis_val = df.columns[x]
    y_axis_val = st.selectbox("Optionen", options=df.columns[spalte_von:spalte_bis])

    plot = px.line(df, x = x_axis_val, y= y_axis_val, markers=True)
    st.plotly_chart(plot)

def pie_chart(df):
    px.pie(df)
