import streamlit as st 

st.title("Meu programa")
st.write("Alô mundo")

nome= st.text_input("Digite o seu nome:")
if nome:
  st.write (nome.upper())

idade= st.text_input("Digite sua idade:")
if idade:
  st.write (idade)

frase= nome +" é uma pessoa legal"
st.write(frase)

time= st.text_input("Qual é o melhor time do Rio")
if time:
   st.write(time)

