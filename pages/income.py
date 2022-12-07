import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go


df = pd.read_csv('crimedata.csv', sep=',')
df.dropna(inplace = True)

st.title("Crimes and median income")
st.write("""How crimes correlate with income""")

# Настройка боковой панели
st.sidebar.title("Crimes and income")


crime = ['murders', 'rapes', 'robberies', 'assaults', 'arsons', 'autoTheft', 'larcenies', 'burglaries']

def population_crimes(crimes):
    df_pop = df[[crimes] + ['medIncome']]
    fig = px.scatter(x=df_pop['medIncome'].values, y=df_pop[crimes].values, trendline="ols")
    fig.update_layout(xaxis_title="Median income",
                  yaxis_title="Number of crimes")
    fig.update_traces(marker_size=8)
    return fig

select_crime = st.sidebar.selectbox('Select:', ('murders', 'rapes', 'robberies', 'assaults', 'arsons', 'autoTheft', 'larcenies', 'burglaries'))
st.plotly_chart(population_crimes(select_crime), use_container_width=True)
