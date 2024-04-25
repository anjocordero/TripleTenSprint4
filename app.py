_ = """
Import libraries
"""
import pandas as pd
import streamlit as st
import plotly_express as px

_ = """
Read in and enrich DataFrame, as explained in EDA.ipynb
"""

df = pd.read_csv("vehicles_us.csv")
df['is_4wd'] = df['is_4wd'] == 1.0
df['manufacturer'] = df['model'].apply(lambda x: x.split()[0])

_ = """
Display graphs
"""

st.header("An Analysis of Cars on Sale in the US")

manualSelected = st.checkbox("Manual transmission?")
numBins = 700

df_filtered = df.copy()

if manualSelected:
    df_filtered = df_filtered[ df_filtered['transmission'] == 'manual' ]
    numBins = 200
else:
    df_filtered = df_filtered[ df_filtered['transmission'] == 'automatic' ]

fig = px.histogram(
    df_filtered['price'],
    range_x=[0, 75000],
    nbins=numBins
    )

st.write(fig)