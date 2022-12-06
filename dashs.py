#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


# In[ ]:


df = pd.read_csv('crimedata.csv', sep=',')


# In[ ]:
st.title("Crimes in US Communities Dashboard")
st.write("""This dashboard will present how crimes correlate with variables""")

# Настройка боковой панели
st.sidebar.title("About")
st.sidebar.info(" The github link can be found "
                "[here](https://github.com/Lulululunas/streamlit/blob/main/dashs.py)")


crime = ['murders', 'rapes', 'robberies', 'assaults', 'arsons', 'autoTheft', 'larcenies', 'burglaries']

def state_crimes(crimes = crime):
    df_states = df[crime + ['state']].groupby(['state']).sum().reset_index()
    for state in states:
        x = df_states.loc[state][name_x]
        y = df_states.loc[state][name_y]
        data_states.append(go.Scatter(x=x, y=y, mode = 'markers'))
    
    layout = go.Layout(
        width=1000,
        height=600
    )

    plot = go.Figure(data = df_states, layout = layout)
    return plot
  
select_crime = st.sidebar.selectbox('Select crime', ('murders', 'rapes', 'robberies', 'assaults', 'arsons', 'autoTheft', 'larcenies', 'burglaries'))
st.plotly_chart(state_crimes(select_crime), use_container_width=True)  
