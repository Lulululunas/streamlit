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
    df_states = df[crime + ['state']].groupby(['state']).sum()
    x = df_states.index
    y = df_states[crimes]
    
#     layout = go.Layout(
#         width=1000,
#         height=600
#     )

    fig = go.Figure()
    fig.add_trace(go.Bar(x=x, y=y,))
    return fig

select_crime = st.sidebar.selectbox('Crimes amoung states. Select:', ('all', 'murders', 'rapes', 'robberies', 'assaults', 'arsons', 'autoTheft', 'larcenies', 'burglaries'))
if select_crime == 'all':
    st.bar_chart(df[crime + ['state']].groupby(['state']).sum())
else:
    st.plotly_chart(state_crimes(select_crime), use_container_width=False)
 
