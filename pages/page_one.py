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
st.sidebar.title("About")
st.sidebar.info(" The github link can be found "
                "[here](https://github.com/Lulululunas/streamlit/blob/main/dashs.py)")


crime = ['murders', 'rapes', 'robberies', 'assaults', 'arsons', 'autoTheft', 'larcenies', 'burglaries']

def state_crimes(crimes = crime):
    df_states = df[crime + ['state']].groupby(['state']).sum().loc[:,[crimes]]
    return df_states

select_crime = st.sidebar.selectbox('Crimes amoung states. Select:', ('all', 'murders', 'rapes', 'robberies', 'assaults', 'arsons', 'autoTheft', 'larcenies', 'burglaries'))
if select_crime == 'all':
    st.bar_chart(df[crime + ['state']].groupby(['state']).sum())
else:
    st.bar_chart(state_crimes(select_crime))
 