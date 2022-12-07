import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go


df = pd.read_csv('crimedata.csv', sep=',')
df.dropna(inplace = True)

# Настройка боковой панели
st.sidebar.title("Crimes and income")


def population_crimes(crimes):
    if crimes == 'all':
        st.title("Crimes and median income")
        st.write("""How crimes correlate with income""")
        crime = ['murders', 'rapes', 'robberies', 'assaults', 'arsons', 'autoTheft', 'larcenies', 'burglaries']
        fig = px.scatter(x=df['medIncome'].values, y=df[crime].sum(axis=1).values, trendline="ols")
    else:
        st.title("Correlation between "+crimes+" and median income")
        st.write("""How""", crimes, """correlate with income""")
        df_pop = df[[crimes] + ['medIncome']]
        fig = px.scatter(x=df_pop['medIncome'].values, y=df_pop[crimes].values, trendline="ols")
    fig.update_layout(xaxis_title="Median income",
                  yaxis_title="Number of crimes")
    fig.update_traces(marker_size=8)
    return fig

select_crime = st.sidebar.selectbox('Select:', ('all', 'murders', 'rapes', 'robberies', 'assaults', 'arsons', 'autoTheft', 'larcenies', 'burglaries'))
st.plotly_chart(population_crimes(select_crime), use_container_width=True)
