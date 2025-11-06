import streamlit as st
import pandas as pd
from basedosdados import read_sql

# Título da aplicação
st.title("Consulta de Deputados - Base dos Dados (Câmara dos Deputados)")

# --- Parte 1: Consulta pelo nome do deputado ---
nome_deputado = st.text_input("Digite o nome do deputado:")

if nome_deputado:
    try:
        query = f"""
        SELECT id_deputado, nome, sigla_partido, sigla_uf
        FROM `basedosdados.br_camara_deputados.deputado`
        WHERE LOWER(nome) LIKE LOWER('%{nome_deputado}%')
        """
        deputados = read_sql(query, billing_project_id="seu_projeto_no_bigquery")

        if not deputados.empty:
            st.success(f"{len(deputados)} deputado(s) encontrado(s):")
            for _, dep in deputados.iterrows():
                st.subheader(dep["nome"])
                st.write(f"**ID:** {dep['id_deputado']}")
                st.write(f"**Sigla Partido:** {dep['sigla_partido']}")
                st.write(f"**UF:** {dep['sigla_uf']}")
            
            # --- Parte 2: Consulta de despesas pelo ID ---
            st.markdown("---")
            st.subheader("Consultar despesas do deputado")
            id_deputado = st.text_input("Digite o ID do deputado para ver suas despesas:")

            if id_deputado:
                query_despesas = f"""
                SELECT ano, mes, tipo_despesa, valor_documento, fornecedor
                FROM `basedosdados.br_camara_deputados.despesa`
                WHERE id_deputado = {id_deputado}
                """
                despesas = read_sql(query_despesas, billing_project_id="seu_projeto_no_bigquery")

                if not despesas.empty:
                    st.success(f"{len(despesas)} despesa(s) encontrada(s):")

                    # Converte valores e exibe tabela
                    despesas["valor_documento"] = pd.to_numeric(
                        despesas["valor_documento"], errors="coerce"
                    ).fillna(0)

                    st.dataframe(despesas)

                    # --- Gráficos ---
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
        st.error(f"Erro ao consultar a Base dos Dados: {e}")

