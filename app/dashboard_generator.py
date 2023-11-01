import pandas as pd
import plotly.express as px
import streamlit as st

file_csv = "kanyesteves/fatalities-in-the-israeli-palestinian/master/datasets/treated_fatalities_isr_pse_conflict_2000_to_2023.csv"
df = pd.read_csv(file_csv)

st.set_page_config(layout="wide")
city = st.sidebar.selectbox("Cidade", df["citizenship"].unique())

df['date_of_death'] = pd.to_datetime(df['date_of_death'])
df["year"] = df['date_of_death'].dt.year.copy()
df_filtered_citys = df[df["citizenship"] == city]
col1, col2 = st.columns(2)


# Filtros
total_deaths_by_citizenship = df_filtered_citys.groupby("year")["citizenship"].value_counts()
dataframe1 = pd.DataFrame(total_deaths_by_citizenship).reset_index()

total_deaths = df_filtered_citys.groupby("citizenship")["gender"].value_counts()
dataframe2 = pd.DataFrame(total_deaths).reset_index()


# Gráficos
fig_total_deaths = px.pie(dataframe2,
                          values="count",
                          names="gender",
                          title='Análise Comparativa de Mortes Entre Homens vs Mulheres')
col1.plotly_chart(fig_total_deaths, use_container_with=True)

fig_total_deaths_per_year = px.bar(dataframe1,
                          x='year',
                          y="count",
                          color='citizenship',
                          title='Análise Comparativa de Mortes por Ano')
col2.plotly_chart(fig_total_deaths_per_year, use_container_with=True)