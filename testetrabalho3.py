import streamlit as st
import pandas as pd

st.title("Consulta de Deputados - Base dos Dados (Versão CSV Pública)")

# URLs públicas dos CSVs da Base dos Dados
URL_DEPUTADOS = "https://storage.googleapis.com/basedosdados-public/extra/br_camara_deputados/deputado.csv"
URL_DESPESAS = "https://storage.googleapis.com/basedosdados-public/extra/br_camara_deputados/despesa.csv"

# --- Parte 1: Consulta pelo nome do deputado ---
nome_deputado = st.text_input("Digite o nome do deputado:")

if nome_deputado:
    try:
        deputados = pd.read_csv(URL_DEPUTADOS, dtype=str)
        deputados_filtrados = deputados[deputados["nome"].str.contains(nome_deputado, case=False, na=False)]

        if not deputados_filtrados.empty:
            st.success(f"{len(deputados_filtrados)} deputado(s) encontrado(s):")
            for _, dep in deputados_filtrados.iterrows():
                st.subheader(dep["nome"])
                st.write(f"**ID:** {dep['id_deputado']}")
                st.write(f"**Sigla Partido:** {dep['sigla_partido']}")
                st.write(f"**UF:** {dep['sigla_uf']}")

            # --- Parte 2: Consulta de despesas pelo ID ---
            st.markdown("---")
            st.subheader("Consultar despesas do deputado")
            id_deputado = st.text_input("Digite o ID do deputado para ver suas despesas:")

            if id_deputado:
                despesas = pd.read_csv(URL_DESPESAS, dtype=str)
                despesas = despesas[despesas["id_deputado"] == id_deputado]

                if not despesas.empty:
                    st.success(f"{len(despesas)} despesa(s) encontrada(s):")

                    despesas["valor_documento"] = pd.to_numeric(
                        despesas["valor_documento"], errors="coerce"
                    ).fillna(0)

                    colunas = ["ano", "mes", "tipo_despesa", "valor_documento", "fornecedor"]
                    colunas_existentes = [c for c in colunas if c in despesas.columns]
                    st.dataframe(despesas[colunas_existentes])

                    # Gráficos
                    st.markdown("### 📊 Gráfico de Despesas")

                    if "tipo_despesa" in despesas.columns:
                        grafico_tipo = (
                            despesas.groupby("tipo_despesa")["valor_documento"]
                            .sum()
                            .sort_values(ascending=False)
                        )
                        st.bar_chart(grafico_tipo)

                    if "mes" in despesas.columns:
                        grafico_mes = (
                            despesas.groupby("mes")["valor_documento"]
                            .sum()
                            .sort_index()
                        )
                        st.line_chart(grafico_mes)
                else:
                    st.warning("Nenhuma despesa encontrada para este deputado.")
        else:
            st.warning("Nenhum deputado encontrado com esse nome.")
    except Exception as e:
        st.error(f"Erro ao carregar dados: {e}")


