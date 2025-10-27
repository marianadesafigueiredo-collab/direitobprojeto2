import streamlit as st
import pandas as pd
import numpy as np

# Função para calcular penalidade por rescisão antecipada
def calcular_penalidade(valor_contrato, percentual_penalidade):
    """
    Função que calcula a penalidade por rescisão antecipada.
    
    :param valor_contrato: Valor total do contrato (R$).
    :param percentual_penalidade: Percentual da penalidade (em %).
    :return: Valor da penalidade.
    """
    penalidade = valor_contrato * (percentual_penalidade / 100)
    return penalidade

# Função para calcular o valor da remuneração (baseado no tempo do contrato)
def calcular_remuneracao(valor_contrato, duracao_meses):
    """
    Função que calcula a remuneração mensal baseada no valor do contrato e a duração.
    
    :param valor_contrato: Valor total do contrato (R$).
    :param duracao_meses: Duração do contrato em meses.
    :return: Remuneração mensal.
    """
    remuneracao_mensal = valor_contrato / duracao_meses
    return remuneracao_mensal

# Interface Streamlit
st.title("Simulador de Cláusulas Contratuais")

# Entrada do valor do contrato
valor_contrato = st.number_input("Informe o valor total do contrato (R$):", min_value=0.0, step=1000.0)

# Seção para a rescisão
st.header("Cláusula de Rescisão Antecipada")
percentual_penalidade = st.slider("Escolha o percentual de penalidade por rescisão antecipada (%)", 0, 20, 10)

# Cálculo da penalidade
penalidade = calcular_penalidade(valor_contrato, percentual_penalidade)

# Seção para a duração do contrato
st.header("Cláusula de Remuneração")
duracao_meses = st.number_input("Informe a duração do contrato em meses:", min_value=1, step=1)

# Cálculo da remuneração mensal
remuneracao_mensal = calcular_remuneracao(valor_contrato, duracao_meses)

# Exibir os resultados
st.write(f"**Valor do contrato**: R${valor_contrato:,.2f}")
st.write(f"**Penalidade por rescisão antecipada**: R${penalidade:,.2f}")
st.write(f"**Remuneração mensal**: R${remuneracao_mensal:,.2f}")

# Exibir um resumo do contrato
st.header("Resumo do Contrato")
st.write(f"Se o contrato for rescindido antecipadamente, a penalidade será de R${penalidade:,.2f}.")
st.write(f"A remuneração mensal acordada para a duração do contrato será de R${remuneracao_mensal:,.2f}.")

# Adicionando uma cláusula de pagamento antecipado (opcional)
st.header("Cláusula de Pagamento Antecipado")
pagamento_antecipado = st.checkbox("Simular pagamento antecipado")

if pagamento_antecipado:
    meses_antecipado = st.slider("Selecione a quantidade de meses a serem pagos antecipadamente", 1, duracao_meses)
    valor_pago_antecipado = remuneracao_mensal * meses_antecipado
    st.write(f"Se o pagamento for feito para {meses_antecipado} meses de forma antecipada, o valor pago será de R${valor_pago_antecipado:,.2f}.")

# Gráfico de distribuição do valor do contrato
st.header("Distribuição do Valor do Contrato")
import matplotlib.pyplot as plt
labels = ["Valor do Contrato", "Penalidade por Rescisão", "Remuneração Mensal"]
values = [valor_contrato, penalidade, remuneracao_mensal * duracao_meses]

fig, ax = plt.subplots()
ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=["#66b3ff", "#ff6666", "#99ff99"])
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig)

# Conclusão e observações
st.markdown("""
### Observações Importantes:
- **Penalidade por Rescisão Antecipada**: É calculada com base no percentual informado. Normalmente, contratos comerciais incluem uma cláusula que estipula uma penalidade por rescisão antecipada.
- **Remuneração Mensal**: A remuneração é dividida igualmente ao longo da duração do contrato. Esse valor pode ser ajustado para casos específicos.
- **Pagamento Antecipado**: Caso haja um pagamento antecipado de meses, o valor será descontado do total do contrato.
""")
