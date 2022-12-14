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

def income_crimes(crimes):
    if crimes == 'all':
        st.title("Crimes and median income")
        st.write("""How a level of crimes per capita correlate with income""")
        fig = px.scatter(x=df['medIncome'].values, y=df_new[crime].mean(axis=1).values, trendline="ols", \
                         color_discrete_sequence=px.colors.qualitative.Antique)
    else:
        st.title("Correlation between "+crimes+" and median income")
        st.write("""How""", crimes, """ per capita correlate with income""")
        fig = px.scatter(x=df['medIncome'].values, y=df_new[crimes].values, trendline="ols", \
                         color_discrete_sequence=px.colors.qualitative.Antique)
    fig.update_layout(xaxis_title="Median income",
                  yaxis_title="Crimes per capita")
    fig.update_traces(marker_size=8)
    fig.update_coloraxes(showscale=False)
    return fig

select_crime = st.sidebar.selectbox('Select:', ('all', 'murders', 'rapes', 'robberies', 'assaults', 'arsons', 'autoTheft', 'larcenies', 'burglaries'))
st.plotly_chart(income_crimes(select_crime), use_container_width=True)
