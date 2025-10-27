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
valor_pensao = calcular_pensao(renda, necessidades, percentual)

# Exibir os resultados
st.write(f"Valor da pensão alimentícia calculado: R${valor_pensao:,.2f}")

# Gerar gráfico comparativo
gerar_grafico(valor_pensao, necessidades)

# Adicionalmente, podemos adicionar uma simulação de alteração no valor da renda ou nas necessidades
alteracao_renda = st.number_input("Simule uma alteração na renda (R$):", 0.0)
alteracao_necessidades = st.number_input("Simule uma alteração nas necessidades (R$):", 0.0)

# Calcular os novos valores de pensão com as alterações
nova_renda = renda + alteracao_renda
novas_necessidades = necessidades + alteracao_necessidades

# Recalcular a pensão com as novas informações
nova_pensao = calcular_pensao(nova_renda, novas_necessidades, percentual)

# Exibir os novos resultados
st.write(f"Novo valor da pensão alimentícia com alteração na renda: R${nova_pensao:,.2f}")
st.write(f"Nova renda do alimentante: R${nova_renda:,.2f}")
st.write(f"Novas necessidades do alimentado: R${novas_necessidades:,.2f}")

# Gerar gráfico comparativo após alterações
gerar_grafico(nova_pensao, novas_necessidades)

