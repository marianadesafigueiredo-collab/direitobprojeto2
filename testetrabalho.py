import streamlit as st

# Função para calcular a possibilidade de conversão de pena
def calcular_conversao(pena, crime, reincidencia, comportamento):
    # Critérios para a conversão da pena
    conversao_possivel = False
    alternativas = []

    # Se a pena for de até 4 anos, pode ser convertida
    if pena <= 4:
        conversao_possivel = True
        alternativas.append('Prestação de serviços à comunidade')
        alternativas.append('Pena de multa')

        # Se o condenado for primário, pode haver a possibilidade de mais alternativas
        if reincidencia == 'Não':
            alternativas.append('Pena restritiva de direitos (como interdição temporária de direitos)')
    
    # Progressão de regime
    if pena > 4:
        if comportamento == 'Bom':
            regime = 'Progressão para o regime semiaberto'
        else:
            regime = 'Permanência no regime fechado'
    else:
        regime = 'Não há progressão necessária'

    return conversao_possivel, alternativas, regime

# Interface Streamlit
st.title('Simulador de Conversão de Penas')

st.write("""
    **Bem-vindo ao Simulador de Conversão de Penas!**
    
    Este sistema permite simular a conversão de pena privativa de liberdade para penas alternativas,
    considerando as condições do condenado (pena, tipo de crime, reincidência, comportamento).
""")

# Entrada de dados
pena = st.number_input('Informe a pena aplicada (em anos):', min_value=1, max_value=30, value=1)
crime = st.selectbox('Selecione o tipo de crime:', ['Furto', 'Roubo', 'Homicídio', 'Lesão Corporal', 'Tráfico de Drogas'])
reincidencia = st.selectbox('O condenado é reincidente?', ['Sim', 'Não'])
comportamento = st.select


