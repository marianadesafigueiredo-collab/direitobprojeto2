import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Função para calcular o valor da pensão alimentícia
def calcular_pensao(renda, necessidades, percentual=0.3):
    """
    Calcula o valor da pensão alimentícia baseado na renda do alimentante e nas necessidades do alimentado.
    O percentual é uma estimativa do valor a ser destinado, baseado na jurisprudência.
    """
    valor_pensao = renda * percentual  # Percentual baseado na renda
    valor_necessidade = necessidades  # Valor necessário para cobrir as necessidades básicas
    valor_pensao_final = max(valor_pensao, valor_necessidade)  # A pensão será o maior valor entre o cálculo e as necessidades

    return valor_pensao_final

# Função para gerar gráfico da comparação entre percentual e necessidade
def gerar_grafico(valor_pensao, valor_necessidade):
    fig, ax = plt.subplots()
    categories = ['Pensão Calculada', 'Necessidades']
    values = [valor_pensao, valor_necessidade]
    ax.bar(categories, values, color=['#4CAF50', '#FF5733'])
    ax.set_ylabel('Valor (R$)')
    ax.set_title('Comparação entre Pensão Calculada e Necessidades')
    st.pyplot(fig)

# Interface Streamlit
st.title("Simulador de Pensão Alimentícia")

# Entrada de dados
renda = st.number_input("Informe a renda mensal do alimentante (R$):", min_value=0.0)
necessidades = st.number_input("Informe o valor das necessidades do alimentado (R$):", min_value=0.0)
percentual = st.slider("Escolha o percentual de pensão (com base na jurisprudência)", 0.05, 0.5, 0.3, 0.01)

# Calcular o valor da pensão
va

