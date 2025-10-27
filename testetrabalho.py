import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Função para calcular o valor da indenização
def calcular_indenizacao(tipo_dano, valor_dano, agravante, dias_juros, taxa_juros_ano=0.1, correcao_monetaria=0.05):
    """
    Calcula o valor da indenização com base no tipo de dano, agravantes, juros e correção monetária.
    
    :param tipo_dano: Tipo de dano (material ou moral)
    :param valor_dano: Valor estimado do dano
    :param agravante: Agravantes (ex: sofrimento adicional)
    :param dias_juros: Número de dias passados desde o evento
    :param taxa_juros_ano: Taxa de juros anual (padrão: 10%)
    :param correcao_monetaria: Taxa de correção monetária anual (padrão: 5%)
    :return: Valor final da indenização
    """
    # Cálculo do valor corrigido
    correção = (1 + correcao_monetaria) ** (dias_juros / 365)
    valor_corrigido = valor_dano * correção
    
    # Cálculo dos juros
    juros = valor_corrigido * (1 + taxa_juros_ano) ** (dias_juros / 365) - valor_corrigido
    
    # Ajustando o valor com o agravante
    valor_final = valor_corrigido + juros + agravante
    return valor_final

# Função para gerar gráfico de comparação
def gerar_grafico(indenizacao):
    fig, ax = plt.subplots()
    ax.bar(["Indenização Final"], [indenizacao], color="#4CAF50")
    ax.set_ylabel('Valor da Indenização (R$)')
    ax.set_title('Cálculo da Indenização por Responsabilidade Civil')
    st.pyplot(fig)

# Interface Streamlit
st.title("Calculadora de Indenização por Responsabilidade Civil")

# Escolher o tipo de dano
tipo_dano = st.selectbox("Escolha o tipo de dano", ["Dano Material", "Dano Moral"])

# Entrar com o valor do dano
valor_dano = st.number_input("Informe o valor estimado do dano (R$):", min_value=0.0)

# Agravantes (como sofrimento, dor, etc.)
agravante = st.number_input("Informe valor adicional por agravantes (ex: sofrimento, dor) (R$):", min_value=0.0)

# Tempo em dias desde o evento que causou o dano
dias_juros = st.number_input("Informe o número de dias desde o evento que causou o dano:", min_value=0)

# Calcular a indenização
indenizacao_final = calcular_indenizacao(tipo_dano, valor_dano, agravante, dias_juros)

# Exibir resultados
st.write(f"Valor final da indenização: R${indenizacao_final:,.2f}")

# Gerar gráfico de comparação
gerar_grafico(indenizacao_final)

# Informações adicionais sobre o cálculo
st.markdown("""
### Como a Indenização foi Calculada:
- **Valor do Dano**: O valor informado pelo usuário para o dano material ou moral.
- **Agravantes**: Fatores adicionais como sofrimento, dor, perda de qualidade de vida, entre outros.
- **Correção Monetária**: Considerando a inflação acumulada desde o evento.
- **Juros**: Juros aplicados ao valor corrigido com base no tempo passado (dias) desde o evento.
""")
