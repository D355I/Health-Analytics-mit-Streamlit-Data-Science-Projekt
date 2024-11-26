import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly as px



col1, col2, col3 = st.columns([1,2,1])

col1.markdown("DATA LITERACY ANALYTICAL PROJECT")

file = col2.file_uploader("Upload your file here")

