import streamlit as st 

st.title("Meu programa")
st.write("Alô mundo")

nome= st.text_input("Digite o seu nome:")
if nome:
  st.write (nome.upper())

idade= st.text_input("Digite sua idade:")
if idade:
  st.write (idade)

cargo= st.text_input("Digite o seu cargo:")
try:
    salario= float(st.text_input("Digite o seu salário:"))
    erro = False
except:
    st.write("O salário deve ser um número")
    erro = True

if not erro:
  if cargo.lower().startswith == 'gerente':
   novo_salario= salario * 1.05
  else:
   novo_salario= salario * 1.07
st.write("O novo salário é ", novo_salario)
