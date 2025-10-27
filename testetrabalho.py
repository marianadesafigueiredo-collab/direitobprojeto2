import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Função para calcular o valor da indenização
def calcular_indenizacao(valor_dano, tipo_dano, agravantes, juros, correcao_monetaria, dias):
    """
    Função que calcula a indenização com base no valor do dano, tipo de dano, agravantes, juros e correção monetária.
    
    :param valor_dano: Valor estimado do dano (R$).
    :param tipo_dano: Tipo de dano (material ou moral).
    :param agravantes: Fatores agravantes (R$ adicionais).
    :param juros: Taxa de juros aplicada (em percentual).
    :param correcao_monetaria: Taxa de correção monetária (em percentual).
    :param dias: Número de dias desde o evento.
    :return: Valor total da indenização.
    """
    
    # Cálculo da correção monetária (composta)
    correcao = (1 + correcao_monetaria/100) ** (dias / 365)
    valor_corrigido = valor_dano * correcao
    
    # Cálculo dos juros (compostos)
    juros_calculados = valor_corrigido * (1 + juros / 100) ** (dias / 365) - valor_corrigido
    
    # Calcular valor final com agravantes
    valor_final = valor_corrigido + juros_calculados + agravantes
    
    return valor_final, valor_corrigido, juros_calculados

# Interface Streamlit
st.title("Calculadora de Indenização Judicial por Danos Morais e Materiais")

# Inputs
valor_dano = st.number_input("Informe o valor estimado do dano (R$):", min_value=0.0, step=1000.0)
tipo_dano = st.selectbox("Escolha o tipo de dano", ["Dano Material", "Dano Moral"])
agravantes = st.number_input("Informe o valor de agravantes (ex: sofrimento psicológico, lesões permanentes) (R$):", min_value=0.0)
juros = st.number_input("Informe a taxa de juros (em %):", min_value=0.0)
correcao_monetaria = st.number_input("Informe a taxa de correção monetária (em %):", min_value=0.0)
dias = st.number_input("Informe o número de dias desde o evento:", min_value=0)

# Cálculo da indenização
indenizacao_total, valor_corrigido, juros_calculados = calcular_indenizacao(valor_dano, tipo_dano, agravantes, juros, correcao_monetaria, dias)

# Exibir resultados
st.write(f"### Resultados do Cálculo da Indenização:")
st.write(f"**Valor corrigido do dano** (com correção monetária): R${valor_corrigido:,.2f}")
st.write(f"**Valor de juros aplicados**: R${juros_calculados:,.2f}")
st.write(f"**Valor final da indenização**: R${indenizacao_total:,.2f}")

# Exibindo uma visualização dos valores
st.write("### Gráfico de Comparação dos Valores")
fig, ax = plt.subplots()
labels = ['Valor Inicial', 'Correção Monetária', 'Juros', 'Valor Final']
values = [valor_dano, valor_corrigido - valor_dano, juros_calculados, indenizacao_total - agravantes]
ax.bar(labels, values, color=['blue', 'orange', 'green', 'red'])
ax.set_ylabel('Valor (R$)')
ax.set_title(f"Distribuição dos Valores da Indenização para um Dano {tipo_dano}")
st.pyplot(fig)

# Detalhes adicionais sobre o cálculo
st.markdown("""
### Detalhes sobre o Cálculo:
- **Correção Monetária**: Considera a inflação ou o índice de correção monetária do período.
- **Juros**: Juros compostos aplicados ao valor corrigido com base no número de dias passados desde o evento.
- **Agravantes**: Fatores como sofrimento psicológico, dor, e perda de qualidade de vida podem aumentar o valor da indenização.
""")

# Exemplo de tabela de referência
st.markdown("""
### Exemplos de Tipos de Dano:
- **Dano Material**: Danos a bens patrimoniais ou materiais (ex: danos em veículos, propriedades, etc.).
- **Dano Moral**: Danos à integridade psicológica ou à dignidade da pessoa.
""")

