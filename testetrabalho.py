import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Função para simular a partilha de bens
def calcular_partilha(bens, regime, filhos, dividas):
    # Definindo os regimes de bens
    if regime == "Comunhão Parcial":
        # Regime de comunhão parcial - divide apenas os bens adquiridos durante o casamento
        bens_comum = sum(bens['comum'])
        bens_particular = sum(bens['particular'])
        total_comum = bens_comum / 2  # Cada cônjuge recebe metade dos bens comuns
        total_particular = bens_particular
    elif regime == "Comunhão Universal":
        # Regime de comunhão universal - todos os bens são comuns
        bens_comum = sum(bens['comum']) + sum(bens['particular'])
        bens_particular = 0
        total_comum = bens_comum / 2  # Cada cônjuge recebe metade dos bens comuns
        total_particular = 0
    elif regime == "Separação Total":
        # Regime de separação total - não há partilha de bens adquiridos indivi

