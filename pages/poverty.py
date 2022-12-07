import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go


df = pd.read_csv('crimedata.csv', sep=',')
df.dropna(inplace = True)

# Настройка боковой панели
st.sidebar.title("Crimes and poverty")

crime = ['murders', 'rapes', 'robberies', 'assaults', 'arsons', 'autoTheft', 'larcenies', 'burglaries']

df_new = df[['murdPerPop', 'rapesPerPop', 'robbbPerPop', 'assaultPerPop', 'arsonsPerPop', 'autoTheftPerPop', \
         'larcPerPop', 'burglPerPop']].copy()

df_new.set_axis(crime, axis=1, inplace=True)

def poverty_crimes(crimes):
    if crimes == 'all':
        st.title("Crimes and poverty")
        st.write("""How a level of crimes per capita correlate with percentage of population under poverty""")
        fig = px.scatter(x=df['PctPopUnderPov'].values, y=df_new[crime].mean(axis=1).values, trendline="ols", \
                         color_continuous_scale=px.colors.sequential.Viridis)
    else:
        st.title("Correlation between "+crimes+" and poverty")
        st.write("""How""", crimes, """ per capita correlate with percentage of population under poverty""")
        fig = px.scatter(x=df['PctPopUnderPov'].values, y=df_new[crimes].values, trendline="ols", \
                         color_continuous_scale=px.colors.sequential.Viridis)
    fig.update_layout(xaxis_title="Percentage of population under poverty",
                  yaxis_title="Crimes per capita")
    fig.update_traces(marker_size=8)
    fig.update_coloraxes(showscale=False)
    return fig

select_crime = st.sidebar.selectbox('Select:', ('all', 'murders', 'rapes', 'robberies', 'assaults', 'arsons', 'autoTheft', 'larcenies', 'burglaries'))
st.plotly_chart(poverty_crimes(select_crime), use_container_width=True)
