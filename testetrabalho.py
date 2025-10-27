import streamlit as st

import random
# Função para gerar um caso fictício
def gerar_caso():
    casos = [
        {'caso': 'Homicídio Qualificado', 'detalhes': 'Réu acusado de matar a vítima com requintes de crueldade.', 'penalidade': '25 a 30 anos de prisão'},
        {'caso': 'Furto Qualificado', 'detalhes': 'Réu acusado de furtar um objeto em uma residência com arrombamento.', 'penalidade': '2 a 6 anos de prisão'},
        {'caso': 'Tráfico de Drogas', 'detalhes': 'Réu acusado de tráfico de entorpecentes com grande quantidade de droga.', 'penalidade': '5 a 15 anos de prisão'},
        {'caso': 'Lesão Corporal', 'detalhes': 'Réu acusado de agredir fisicamente a vítima, resultando em lesões.', 'penalidade': '1 a 3 anos de prisão'}
    ]
    return random.choice(casos)

# Função para gerar perguntas para o advogado
def gerar_perguntas(caso):
    perguntas = {
        'Homicídio Qualificado': [
            "Qual a motivação do crime?",
            "O réu agiu com premeditação?",
            "Quais elementos caracterizam a qualificadora do homicídio?"
        ],
        'Furto Qualificado': [
            "O réu tinha intenção de furtar?",
            "Havia alguma circunstância que justifique o arrombamento?",
            "Há alguma possibilidade de erro na acusação?"
        ],
        'Tráfico de Drogas': [
            "Como foi a apreensão das drogas?",
            "Há provas que liguem o réu diretamente ao tráfico?",
            "O réu tem antecedentes criminais?"
        ],
        'Lesão Corporal': [
            "Como as lesões foram causadas?",
            "A vítima provocou o réu de alguma forma?",
            "Existem testemunhas que confirmem a agressão?"
        ]
    }
    return perguntas.get(caso, [])

# Função para avaliação do desempenho do advogado (simples)
def avaliar_resposta(pergunta, resposta_usuario):
    respostas_esperadas = {
        'Homicídio Qualificado': {
            "Qual a motivação do crime?": "Discussão entre o réu e a vítima",
            "O réu agiu com premeditação?": "Sim",
            "Quais elementos caracterizam a qualificadora do homicídio?": "Requintes de crueldade"
        },
        'Furto Qualificado': {
            "O réu tinha intenção de furtar?": "Sim, a intenção estava clara",
            "Havia alguma circunstância que justifique o arrombamento?": "Não"
        },
        'Tráfico de Drogas': {
            "Como foi a apreensão das drogas?": "Foi realizada uma abordagem policial com mandado",
            "Há provas que liguem o réu diretamente ao tráfico?": "Sim, havia drogas no carro do réu"
        },
        'Lesão Corporal': {
            "Como as lesões foram causadas?": "O réu agrediu a vítima com socos",
            "A vítima provocou o réu de alguma forma?": "Sim, a vítima agrediu verbalmente o réu"
        }
    }
    resposta_esperada = respostas_esperadas[caso].get(pergunta, "")
    if resposta_usuario.lower() in resposta_esperada.lower():
        return "Resposta correta!"
    else:
        return f"Resposta incorreta. A resposta esperada era: {resposta_esperada}"

# Interface do Streamlit
st.title("Simulador de Audiência Penal")
st.write("Simulador de Audiências de Instrução e Julgamento para advogados e estudantes de direito.")

# Gerar um caso fictício
caso = gerar_caso()
st.subheader(f"Caso: {caso['caso']}")
st.write(f"Detalhes do caso: {caso['detalhes']}")
st.write(f"Pena sugerida: {caso['penalidade']}")

# Perguntar ao advogado (usuário) sobre o caso
perguntas = gerar_perguntas(caso['caso'])
pergunta_atual = st.selectbox("Escolha uma pergunta para responder:", perguntas)

# Entrada de resposta do usuário
resposta_usuario = st.text_input("Sua resposta:")

# Avaliar a resposta
if st.button("Avaliar Resposta"):
    avaliacao = avaliar_resposta(caso['caso'], pergunta_atual, resposta_usuario)
    st.write(avaliacao)

# Dicas durante a audiência
st.subheader("Dicas para a Defesa")
st.write("""
    1. Fique atento aos detalhes do caso, e sempre reforce a tese da defesa.
    2. Faça perguntas claras e objetivas às testemunhas.
    3. Lembre-se de que a motivação do réu é uma defesa importante em casos de homicídio.
    4. Para crimes de furto, explore a ausência de dolo ou a falta de intenção de prejudicar a vítima.
""")

# Exemplo de como conduzir a audiência
st.subheader("Exemplo Prático")
st.write("""
    Imagine que você está defendendo um réu acusado de **homicídio qualificado**. Durante o interrogatório, 
    o juiz pode questionar sobre a motivação do crime, e você pode argumentar que houve uma discussão que 
    levou ao crime. Lembre-se de que é importante demonstrar que o réu não agiu com premeditação.
""")

