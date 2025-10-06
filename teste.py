import streamlit as st 

st.write("Alô mundo")

import streamlit as st

# Define o título da aplicação
st.title("Exibindo uma imagem no Streamlit")

# Adiciona uma imagem ao aplicativo
# Certifique-se de que o caminho 'caminho/para/sua/imagem.jpg' está correto
st.image("caminho/para/sua/imagem.jpg", caption="Uma imagem de exemplo", width=300)
