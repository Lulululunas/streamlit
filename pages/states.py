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
st.title("Crimes in US states")
st.write("""How crimes correlate with states""")

# Настройка боковой панели
st.sidebar.title("Crimes amoung states")


crime = ['murders', 'rapes', 'robberies', 'assaults', 'arsons', 'autoTheft', 'larcenies', 'burglaries']

df_new = df[['murdPerPop', 'rapesPerPop', 'robbbPerPop', 'assaultPerPop', 'arsonsPerPop', 'autoTheftPerPop', \
         'larcPerPop', 'burglPerPop', 'state']].copy()

df_new.set_axis(crime+['state'], axis=1, inplace=True)

def state_crimes(crimes = crime):
    if crimes == 'all':
        df_states = df_new[crime + ['state']].groupby(['state']).sum()
    else:
        df_states = df_new[crime + ['state']].groupby(['state']).sum().loc[:,[crimes]]
    return df_states

select_crime = st.sidebar.selectbox('Select:', ('all', 'murders', 'rapes', 'robberies', 'assaults', 'arsons', 'autoTheft', 'larcenies', 'burglaries'))
st.bar_chart(data = state_crimes(select_crime))
 
