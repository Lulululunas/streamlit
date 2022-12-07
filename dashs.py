#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go


# In[ ]:


df = pd.read_csv('crimedata.csv', sep=',')


# In[ ]:
st.title("Crimes in US Communities Dashboard")
st.write("""This dashboard will present how crimes correlate with variables""")

# Настройка боковой панели
st.sidebar.title("About")
st.sidebar.info(" The github link can be found "
                "[here](https://github.com/Lulululunas/streamlit/blob/main/dashs.py)")

colors = ['LightSalmon', 'DarkSalmon', 'IndianRed', 'Brown',  'DarkSalmon',  'FireBrick', 'Maroon', 'DarkRed']
crime = ['murders', 'rapes', 'robberies', 'assaults', 'arsons', 'autoTheft', 'larcenies', 'burglaries']

fig = go.Figure()
fig.add_trace(go.Pie(values=df[crime].sum(axis=0).values, labels=df[crime].sum(axis=0).index))
fig.update_traces(marker=dict(colors=colors))
fig.update_traces(textposition='inside')
fig.update_coloraxes(showscale=False)

st.plotly_chart(fig, use_container_width=True)  
