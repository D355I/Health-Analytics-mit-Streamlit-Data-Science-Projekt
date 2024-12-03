import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
df=st.session_state['df']
x_axis_val = st.selectbox('Welchen X-Wert wollen Sie?', options=df.columns)
y_axis_val = st.selectbox('Welchen Y-Wert wollen Sie?', options=df.columns)
plot = px.scatter(df, x=x_axis_val, y=y_axis_val)
st.plotly_chart(plot)
st.sidebar.title('DATEI')

options = st.sidebar.radio('Pages', options=['No Name', 'sag an'])
