import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


# Streamlit App-Header
st.title("dAli Express")
st.text('Wilkommen im schlechtesten Aktien vergleich Web')


# Datei-Upload in der Sidebar
uploaded_file = st.sidebar.file_uploader("Choose a file")


# Überprüfen, ob eine Datei hochgeladen wurde
if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.session_state['df'] = df

df=st.session_state['df']
st.header('Data Statistics')
st.write(df.describe())
st.sidebar.title('DATEI')
options = st.sidebar.radio('Pages', options=['No Name', 'sag an'])




