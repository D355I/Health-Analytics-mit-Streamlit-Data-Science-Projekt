import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
df=st.session_state['df']
st.header('Data Header')
st.write(df.head())
st.sidebar.title('DATEI')

options = st.sidebar.radio('Pages', options=['No Name', 'sag an'])
