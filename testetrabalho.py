import streamlit as st
import pandas as pd
import plotly.express as px

# Função para carregar dados
def carregar_dados():
    # Simulação de dados fictícios
    data = {
        'Estado': ['SP', 'RJ', 'MG', 'BA', 'RS'],
        'Crimes Violentos': [80000, 65000, 50000, 60000, 40000],
        'Taxa de Encarceramento': [400, 450, 350, 300, 500],
        'Homicídios': [5000, 3500, 3000, 4000, 2000],
        'Latrocínios': [150, 100, 90, 120, 80],
        'Furto': [30000, 25000, 22000, 28000, 23000]
    }
    return pd.DataFrame(data)

# Carregar dados de criminalidade
df = carregar_dados()

# Título do painel
st.title("Painel de Estatísticas de Crimes e Prisões")

st.write("""
    Este painel interativo permite visualizar dados sobre crimes e prisões no Brasil, 
    com informações sobre taxas de criminalidade, encarceramento, tipos de crimes mais comuns, 
    e comparações entre estados.
""")

# Mostrar os dados em uma tabela
st.subheader('Tabela de Crimes e Taxas de Encarceramento por Estado')
st.write(df)

# Gráfico de Crimes Violentos por Estado
st.subheader('Gráfico de Crimes Violentos por Estado')
fig1 = px.bar(df, x='Estado', y='Crimes Violentos', title='Crimes Violentos por Estado')
st.plotly_chart(fig1)

# Gráfico de Taxa de Encarceramento
st.subheader('Gráfico de Taxa de Encarceramento por Estado')
fig2 = px.bar(df, x='Estado', y='Taxa de Encarceramento', title='Taxa de Encarceramento por Estado')
st.plotly_chart(fig2)

# Gráfico de Homicídios por Estado
st.subheader('Gráfico de Homicídios por Estado')
fig3 = px.bar(df, x='Estado', y='Homicídios', title='Número de Homicídios por Estado')
st.plotly_chart(fig3)

# Análise por Tipo de Crime (simulação com gráfico de pizza)
st.subheader('Distribuição dos Tipos de Crimes em SP')
dados_sp = df[df['Estado'] == 'SP'][['Homicídios', 'Latrocínios', 'Furto']].transpose()
dados_sp.columns = ['Quantidade']
dados_sp['Tipo de Crime'] = dados_sp.index
fig4 = px.pie(dados_sp, values='Quantidade', names='Tipo de Crime', title="Distribuição dos Crimes em SP")
st.plotly_chart(fig4)

# Comparação com outro Estado
estado_comparar = st.selectbox('Escolha um Estado para comparar com SP:', df['Estado'].tolist())
if estado_comparar != 'SP':
    dados_comparacao = df[df['Estado'] == estado_comparar][['Homicídios', 'Latrocínios', 'Furto']].transpose()
    dados_comparacao.columns = ['Quantidade']
    dados_comparacao['Tipo de Crime'] = dados_comparacao.index
    fig5 = px.bar(dados_comparacao, x='Tipo de Crime', y='Quantidade', title=f'Comparação entre SP e {estado_comparar}')
    st.plotly_chart(fig5)

