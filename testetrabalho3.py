import streamlit as st
import requests
import pandas as pd

# Título da aplicação
st.title("Consulta de Deputados - Câmara dos Deputados")

# --- Parte 1: Consulta pelo nome do deputado ---
nome_deputado = st.text_input("Digite o nome do deputado:")

if nome_deputado:
    url = f"https://basedosdados.org/dataset/3d388daa-2d20-49eb-8f55-6c561bef26b6?table=d37931b4-8b67-47c7-b910-014695dc8f36&nome={nome_deputado}"
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        
        deputados = data.get("dados", [])
        
        if deputados:
            st.success(f"{len(deputados)} deputado(s) encontrado(s):")
            
            # Mostra informações do deputado
            for deputado in deputados:
                st.subheader(deputado.get("nome"))
                st.write(f"**ID:** {deputado.get('id')}")
                st.write(f"**Sigla Partido:** {deputado.get('siglaPartido')}")
                st.write(f"**UF:** {deputado.get('siglaUf')}")
                st.write(f"**URL Perfil:** [Link]({deputado.get('uri')})")
            
            # --- Parte 2: Consulta de despesas pelo ID ---
            st.markdown("---")
            st.subheader("Consultar despesas do deputado")
            id_deputado = st.text_input("Digite o ID do deputado para ver suas despesas:")
            
            if id_deputado:
                url_despesas = f"https://basedosdados.org/dataset/3d388daa-2d20-49eb-8f55-6c561bef26b6?table=d37931b4-8b67-47c7-b910-014695dc8f36&id={id_deputado}"
                
                try:
                    resp_despesas = requests.get(url_despesas, timeout=10)
                    despesas_data = resp_despesas.json()
                    
                    despesas = despesas_data.get("dados", [])
                    
                    if despesas:
                        st.success(f"{len(despesas)} despesa(s) encontrada(s):")
                        
                        # Cria DataFrame
                        df = pd.DataFrame(despesas)

                        # Converte valorDocumento para número (corrige erro do gráfico)
                        df["valorDocumento"] = pd.to_numeric(df.get("valorDocumento", 0), errors="coerce").fillna(0)

                        # Lista de colunas desejadas
                        colunas_desejadas = ["ano", "mes", "tipoDespesa", "valorDocumento", "fornecedor"]

                        # Mantém apenas as colunas que realmente existem no DataFrame
                        colunas_existentes = [col for col in colunas_desejadas if col in df.columns]

                        # Exibe tabela apenas com colunas disponíveis
                        if colunas_existentes:
                            st.dataframe(df[colunas_existentes])
                        else:
                            st.warning("Não há colunas esperadas disponíveis para exibição.")

                        # --- Gráficos ---
                        st.markdown("### 📊 Gráfico de Despesas")

                        if not df.empty:
                            # Gráfico de barras por tipo de despesa
                            if "tipoDespesa" in df.columns:
                                grafico_tipo = (
                                    df.groupby("tipoDespesa")["valorDocumento"]
                                    .sum()
                                    .sort_values(ascending=False)
                                )
                                if not grafico_tipo.empty:
                                    st.bar_chart(grafico_tipo)
                                else:
                                    st.info("Sem dados para gerar o gráfico por tipo de despesa.")
                            else:
                                st.info("Coluna 'tipoDespesa' não disponível para gerar gráfico.")

                            # Gráfico de linha por mês (ordenado)
                            if "mes" in df.columns:
                                grafico_mes = (
                                    df.groupby("mes")["valorDocumento"]
                                    .sum()
                                    .sort_index()
                                )
                                if not grafico_mes.empty:
                                    st.line_chart(grafico_mes)
                                else:
                                    st.info("Sem dados para gerar o gráfico mensal.")
                            else:
                                st.info("Coluna 'mes' não disponível para gerar gráfico.")
                        else:
                            st.warning("Não foi possível gerar gráficos — dados vazios.")

                    else:
                        st.warning("Nenhuma despesa encontrada para este deputado.")
                        
                except requests.RequestException as e:
                    st.error(f"Erro ao consultar as despesas: {e}")
                    
        else:
            st.warning("Nenhum deputado encontrado com esse nome.")
            
    except requests.RequestException as e:
        st.error(f"Erro ao consultar a API: {e}")
