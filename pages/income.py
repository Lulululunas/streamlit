import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go


df = pd.read_csv('crimedata.csv', sep=',')
df.dropna(inplace = True)

# Настройка боковой панели
st.sidebar.title("Crimes and income")

crime = ['murders', 'rapes', 'robberies', 'assaults', 'arsons', 'autoTheft', 'larcenies', 'burglaries']

df_new = df[['murdPerPop', 'rapesPerPop', 'robbbPerPop', 'assaultPerPop', 'arsonsPerPop', 'autoTheftPerPop', \
         'larcPerPop', 'burglPerPop']].copy()

df_new.set_axis(crime, axis=1, inplace=True)

def population_crimes(crimes):
    if crimes == 'all':
        st.title("Crimes and median income")
        st.write("""How crimes correlate with income""")
        fig = px.scatter(x=df['medIncome'].values, y=df_new[crime].sum(axis=1).values, trendline="ols")
    else:
        st.title("Correlation between "+crimes+" and median income")
        st.write("""How""", crimes, """ per population correlate with income""")
        fig = px.scatter(x=df['medIncome'].values, y=df_new[crimes].values, trendline="ols")
    fig.update_layout(xaxis_title="Median income",
                  yaxis_title="Number of crimes")
    fig.update_traces(marker_size=8)
    return fig

select_crime = st.sidebar.selectbox('Select:', ('all', 'murders', 'rapes', 'robberies', 'assaults', 'arsons', 'autoTheft', 'larcenies', 'burglaries'))
st.plotly_chart(population_crimes(select_crime), use_container_width=True)
