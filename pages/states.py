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


# Настройка боковой панели
st.sidebar.title("Crimes amoung states")


crime = ['murders', 'rapes', 'robberies', 'assaults', 'arsons', 'autoTheft', 'larcenies', 'burglaries']

df_new = df[['murdPerPop', 'rapesPerPop', 'robbbPerPop', 'assaultPerPop', 'arsonsPerPop', 'autoTheftPerPop', \
         'larcPerPop', 'burglPerPop', 'state']].copy()

df_new = df_new.set_axis(crime+['state'], axis=1, copy=False)

def state_crimes(crimes = crime):
    if crimes == 'all':
         st.title("Crimes in US states")
         st.write("""How crimes per capita correlate with states""")
         df_states = df_new[crime + ['state']].groupby(['state']).mean()
    else:
         st.title("Level of "+crimes+" in US states")
         st.write("""How """,crimes,""" per capita correlate with states""")
         df_states = df_new[crime + ['state']].groupby(['state']).mean().loc[:,[crimes]]
    return df_states

select_crime = st.sidebar.selectbox('Select:', ('all', 'murders', 'rapes', 'robberies', 'assaults', 'arsons', 'autoTheft', 'larcenies', 'burglaries'))
st.bar_chart(data = state_crimes(select_crime))
 
