import pandas as pd
import streamlit as st

dataset = pd.read_csv("https://www.irdx.com.br/media/uploads/paises.csv")

st.dataframe(dataset)


import plotly.express as px
fig= px.scatter_geo(dataset,
                    lat=dataset['latitude'],
                    lon=dataset['longitude'],
                    hover_name=dataset['nome'])
fig.update_layout(title='Coordenadas dos países no mapa',
                  geo_scope= 'world')
fig.show()
