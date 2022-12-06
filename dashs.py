#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


# In[ ]:


df = pd.read_csv('crimedata.csv', sep=',')
df.head(4)


# In[ ]:
st.title("Crimes in US Communities Dashboard")
st.write("""This dashboard will present how crimes correlate with variables""")

# Настройка боковой панели
st.sidebar.title("About")
st.sidebar.info(" The github link can be found "
                "[here](https://github.com/Lulululunas/streamlit/blob/main/dashs.py)")

