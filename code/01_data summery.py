import streamlit as st


df=st.session_state['df']
st.header('Data Statistics')
st.write(df.describe())
st.sidebar.title('DATEI')
options = st.sidebar.radio('Pages', options=['No Name', 'sag an'])