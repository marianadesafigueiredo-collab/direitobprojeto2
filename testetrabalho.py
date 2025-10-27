import streamlit as st
from datetime import datetime, timedelta

# Função para calcular a prescrição
def calcular_prescricao(data_crime, pena, tipo_prescricao, suspensao_interruptiva):
    # Definir os prazos de prescrição com base na pena
    if pena <= 1:
        prazo_prescricao = timedelta(days=3*365)  # 3 anos para penas de até 1 ano
    elif pena <= 2:
        prazo_prescricao = timedelta(days=4*365)  # 4 anos para penas de até 2 anos
    elif pena <= 4:
        prazo_prescricao = timedelta(days=8*365)  # 8 anos para penas de até 4 anos
    elif pena <= 8:
        prazo_prescricao = timedelta(days=12*365)  # 12 anos para penas de até 8 anos
    else:
        prazo_prescricao = timedelta(days=16*365)  # 16 anos para penas superiores a 8 anos

    # Tipo de prescrição (prescrição da ação penal ou prescrição da pena)
    if tipo_prescricao == "Ação Penal":
        prazo_prescricao = timedelta(days=prescricao_acao_pena(pena))

    # Ajuste para causas suspensivas ou interruptivas
    if suspensao_interruptiva:
        prazo_prescricao += timedelta(days=2*365)  # Supondo 2 anos adicionais por causa suspensiva

    # Calcular a data limite para prescrição
    data_limite = data_crime + prazo_prescricao

    # Verificar se o crime já prescreveu
    hoje = datetime.now()
    prescreveu = hoje > data_limite

    return data_limite, prescreveu

# Função para definir o prazo de prescrição da ação penal
def prescricao_acao_pena(pena):
    if pena <= 1:
        return 8 * 365  # Ação penal prescreve em 8 anos
    elif pena <= 2:
        return 10 * 365  # Ação penal prescreve em 10 anos
    elif pena <= 4:
        return 12 * 365  # Ação penal prescreve em 12 anos
    elif pena <= 8:
        return 16 * 365  # Ação penal prescreve em 16 anos
    else:
        return 20 * 365  # Ação penal prescreve em 20 anos

# Interface Streamlit
st.title('Calculadora de Prescrição Penal')

st.write("""
    **Bem-vindo à Calculadora de Prescrição Penal!**
    
    Aplique as informações do crime e da pena para calcular o prazo de prescrição e saber se o crime já prescreveu.
""")

# Inputs do usuário
data_crime = st.date_input('Data do crime:')
pena = st.number_input('Pena aplicada (em anos):', min_value=1, max_value=30, value=1)
tipo_prescricao = st.selectbox('Tipo de prescrição:', ('Ação Penal', 'Prescrição da Pena'))
suspensao_interruptiva = st.radio('Existem causas suspensivas ou interruptivas?', ('Sim', 'Não')) == 'Sim'

# Calcular o prazo de prescrição
data_limite, prescreveu = calcular_prescricao(data_crime, pena, tipo_prescricao, suspensao_interruptiva)

# Exibir resultado
if prescreveu:
    st.markdown(f"**O crime prescreveu.** O prazo de prescrição foi até **{data_limite.strftime('%d/%m/%Y')}**.")
else:
    st.markdown(f"**O crime não prescreveu.** O prazo de prescrição vai até **{data_limite.strftime('%d/%m/%Y')}**.")

# Exemplo prático
st.write("""
    **Exemplo prático**:
    
    Se um crime ocorrido em 01/01/2010 com uma pena de 4 anos for analisado, com a prescrição da ação penal, ele terá o seguinte cálculo:
    - Data limite de prescrição: 01/01/2022
    - Se hoje for após 01/01/2022, o crime já terá prescrito.
""")

