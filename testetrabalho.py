import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Função para simular a partilha de bens
def calcular_partilha(bens, regime, filhos, dividas):
    # Definindo os regimes de bens
    if regime == "Comunhão Parcial":
        # Regime de comunhão parcial - divide apenas os bens adquiridos durante o casamento
        bens_comum = sum(bens['comum'])
        bens_particular = sum(bens['particular'])
        total_comum = bens_comum / 2  # Cada cônjuge recebe metade dos bens comuns
        total_particular = bens_particular
    elif regime == "Comunhão Universal":
        # Regime de comunhão universal - todos os bens são comuns
        bens_comum = sum(bens['comum']) + sum(bens['particular'])
        bens_particular = 0
        total_comum = bens_comum / 2  # Cada cônjuge recebe metade dos bens comuns
        total_particular = 0
    elif regime == "Separação Total":
        # Regime de separação total - não há partilha de bens adquiridos individualmente
        bens_comum = 0
        bens_particular = sum(bens['comum']) + sum(bens['particular'])
        total_comum = 0
        total_particular = bens_particular
    else:
        total_comum = total_particular = 0

    # Simulação de cenários de acordo com a presença de filhos e dívidas
    if filhos > 0:
        # Se houver filhos, a partilha pode ser alterada
        total_comum += bens_comum * 0.1  # Aumento fictício para filhos (pode ser ajustado)
    
    if dividas > 0:
        # Se houver dívidas, pode-se diminuir a partilha
        total_comum -= dividas * 0.2  # Ajuste para dívidas (também fictício)
    
    return total_comum, total_particular

# Função para gerar gráficos
def gerar_grafico(partilha_comum, partilha_particular):
    labels = ['Bens Comuns', 'Bens Particulares']
    sizes = [partilha_comum, partilha_particular]
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)

# Interface Streamlit
st.title("Simulador de Divórcio e Partilha de Bens")

# Entrada de dados
regime = st.selectbox("Escolha o Regime de Bens", ["Comunhão Parcial", "Comunhão Universal", "Separação Total"])
bens_comum = st.number_input("Valor de bens comuns (imóveis, veículos, etc.):", min_value=0)
bens_particular = st.number_input("Valor de bens particulares (bens de cada cônjuge antes do casamento):", min_value=0)
filhos = st.number_input("Número de filhos:", min_value=0)
dividas = st.number_input("Valor das dívidas a serem consideradas:", min_value=0)

# Criação do dataframe de bens
bens = pd.DataFrame({
    'comum': [bens_comum],
    'particular': [bens_particular]
})

# Cálculo da partilha
partilha_comum, partilha_particular = calcular_partilha(bens, regime, filhos, dividas)

# Exibição dos resultados
st.write(f"Total de bens comuns: R${partilha_comum:,.2f}")
st.write(f"Total de bens particulares: R${partilha_particular:,.2f}")

# Gerar gráfico de partilha
gerar_grafico(partilha_comum, partilha_particular)

