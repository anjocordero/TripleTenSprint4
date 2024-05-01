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
df['is_4wd'] = df['is_4wd'] == 1.0 # Convert integer to boolean values
df['model_year'] = df['model_year'].fillna(df.groupby('model')['model_year'].transform('median')) # Replace missing values
df['cylinders'] = df['cylinders'].fillna(df.groupby('model')['cylinders'].transform('median')) # Replace missing values
df['odometer'] = df['odometer'].fillna(df.groupby(['model', 'model_year'])['odometer'].transform('median')) # Replace missing values
df['model'] = df['model'].apply(lambda x: x.title()) # Convert Model to Title Case
df['manufacturer'] = df['model'].apply(lambda x: x.split()[0]) # Isolate first word of model to find manufacturer
df_price_filtered = df[ df['price'] != 1 ].copy() # Remove prices which are set to 1

_ = """
Display graphs
"""
st.header("An Analysis of Cars on Sale in the US")


"""
Histogram showing price of cars on the market
"""

# Checkbox to filter by manual transmission cars
manualSelected = st.checkbox("Manual transmission?")
numBins = 700

# Filter out based on checkbox value
df_manual_filtered = df_price_filtered.copy()
if manualSelected:
    df_manual_filtered = df_manual_filtered[ df_manual_filtered['transmission'] == 'manual' ]
    numBins = 200
else:
    df_manual_filtered = df_manual_filtered[ df_manual_filtered['transmission'] == 'automatic' ]

# Display graph
fig = px.histogram(
    df_manual_filtered['price'],
    range_x=[0, 75000],
    nbins=numBins
    )
st.write(fig)

"""
Scatterplot showing Price vs. Model Year, organized by Manufacturer
"""

fig = px.scatter(
    df_price_filtered,
    x = 'price',
    y = 'model_year',
    labels = {
        'price':'Price (USD)',
        'model':'Model',
        'model_year':'Model Year',
        'manufacturer':'Manufacturer'
    },
    hover_data={
        'model':True,
        'model_year':True,
        'price':False,
        'manufacturer':False
    },
    color = 'manufacturer',
    title = 'Vehicle Price vs. Model Year by Manufacturer',
    opacity = 0.66
)
st.write(fig)

"""
Scatterplot showing Miles on Odometer vs. Model Year, organized by Manufacturer
"""

fig = px.scatter(
    df_price_filtered,
    x='model_year',
    y='odometer',
    labels={
        'model_year':'Model Year',
        'odometer':'Miles',
        'manufacturer':'Manufacturer'
    },
    color='manufacturer',
    title='Miles on Odometer vs. Model Year',
    opacity=0.66
)

st.write(fig)