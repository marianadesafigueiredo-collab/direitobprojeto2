import streamlit as st

# Função para calcular os honorários
def calcular_honorarios(valor_causa, tipo_acao, percentual=0.1, valor_fixo=0):
    """
    Função que calcula o valor dos honorários advocatícios com base no valor da causa e tipo de ação.
    
    :param valor_causa: Valor monetário da causa (R$)
    :param tipo_acao: Tipo de ação (ex: "Cível", "Trabalhista", etc.)
    :param percentual: Percentual sobre o valor da causa (default: 10%)
    :param valor_fixo: Valor fixo, se aplicável (default: 0)
    :return: Valor final dos honorários
    """
    if valor_fixo > 0:
        # Caso seja um valor fixo
        honorarios = valor_fixo
    else:
        # Caso seja calculado por percentual
        honorarios = valor_causa * percentual
    
    return honorarios

# Interface do Streamlit
st.title("Calculadora de Honorários Advocatícios")

# Inputs do usuário
valor_causa = st.number_input("Informe o valor da causa (R$):", min_value=0.0, step=1000.0)
tipo_acao = st.selectbox("Escolha o tipo de ação", ["Cível", "Trabalhista", "Família", "Criminal", "Empresarial"])
percentual = st.slider("Escolha o percentual de honorários (%)", min_value=1, max_value=30, value=10, step=1)
valor_fixo = st.number_input("Ou informe o valor fixo para honorários (R$):", min_value=0.0, value=0.0)

# Cálculo de honorários
honorarios = calcular_honorarios(valor_causa, tipo_acao, percentual, valor_fixo)

# Exibir os resultados
st.write(f"O valor dos honorários advocatícios para uma causa de R${valor_causa:,.2f} é de R${honorarios:,.2f}")

# Exibição do tipo de ação e percentual utilizado
st.write(f"Tipo de Ação: {tipo_acao}")
st.write(f"Percentual de Honorários: {percentual}%")

# Informações sobre os tipos de ações e tabelas
st.markdown("""
### Tabela de Honorários (exemplo):
- **Ação Cível**: 10% sobre o valor da causa.
- **Ação Trabalhista**: 15% sobre o valor da causa.
- **Ação de Família**: 12% sobre o valor da causa.
- **Ação Criminal**: 8% sobre o valor da causa.
- **Ação Empresarial**: Valor fixo dependendo do tipo de serviço.

*Obs: Os valores de percentual e valores fixos são apenas exemplos. A tabela de honorários pode ser adaptada conforme a OAB ou a negociação entre o advogado e o cliente.*
""")

