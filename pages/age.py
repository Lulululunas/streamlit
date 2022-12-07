import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go


df = pd.read_csv('crimedata.csv', sep=',')
df.dropna(inplace = True)

# Настройка боковой панели
st.sidebar.title("Crimes and income")

age = ['12 to 21', '12 to 29', '16 to 24', 'above 60']

df_new = df[['ViolentCrimesPerPop', 'agePct12t21', 'agePct12t29', 'agePct16t24', 'agePct65up']].copy()

df_new = df_new.set_axis(['ViolentCrimes']+age, axis=1, copy=False)

def ages_crimes(ages):
    if ages == 'all':
        st.title("Violent crimes and age")
        st.write("""How violent crimes per capita correlate with age above 12""")
        fig = px.scatter(x=df_new['ViolentCrimes'].values, y=df_new[age].sum(axis=1).values, trendline="ols")
    else:
        st.title("Violent crimes and age "+ages)
        st.write("""How violent crimes per capita correlate with age groups""", ages)
        fig = px.scatter(x=df_new['ViolentCrimes'].values, y=df_new[ages].values, trendline="ols")
    fig.update_layout(xaxis_title="Violent crimes per capita",
                  yaxis_title="Percentage of the population")
    fig.update_traces(marker_size=8)
    return fig

select_crime = st.sidebar.selectbox('Select:', ('above 12', '12 to 21', '12 to 29', '16 to 24', 'above 60'))
st.plotly_chart(ages_crimes(select_crime), use_container_width=True)
