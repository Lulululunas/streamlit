#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go


df = pd.read_csv('crimedata.csv', sep=',')
df.dropna(inplace = True)

# Настройка боковой панели
st.sidebar.title("Crimes and population")


def population_crimes(crimes):
    if crimes == 'all':
        st.title("Crimes and population")
        st.write("""How crimes correlate with population""")
        crime = ['murders', 'rapes', 'robberies', 'assaults', 'arsons', 'autoTheft', 'larcenies', 'burglaries']
        fig = px.scatter(x=df['population'].values, y=df[crime].sum(axis=1).values, trendline="ols")
    else:
        st.title("Correlation between"+crimes+" and population")
        st.write("""How""", crimes, """correlate with population""")
        df_pop = df[[crimes] + ['population']]
        fig = px.scatter(x=df_pop['population'].values, y=df_pop[crimes].values, trendline="ols")
    fig.update_layout(xaxis_title="Number of population",
                  yaxis_title="Number of crimes")
    fig.update_traces(marker_size=8)
    return fig

select_crime = st.sidebar.selectbox('Crimes and population. Select:', ('all', 'murders', 'rapes', 'robberies', 'assaults', 'arsons', 'autoTheft', 'larcenies', 'burglaries'))
st.plotly_chart(population_crimes(select_crime), use_container_width=True)

