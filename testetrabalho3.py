# --- Parte 2: Consulta de despesas pelo ID ---
st.markdown("---")
st.subheader("Consultar despesas do deputado")
id_deputado = st.text_input("Digite o ID do deputado para ver suas despesas:")

if id_deputado:
    base_url = f"https://dadosabertos.camara.leg.br/api/v2/deputados/{id_deputado}/despesas"
    despesas = []
    pagina = 1

    try:
        # Loop para percorrer todas as páginas
        while True:
            url_despesas = f"{base_url}?pagina={pagina}&itens=100"  # até 100 por página
            resp_despesas = requests.get(url_despesas, timeout=10)
            despesas_data = resp_despesas.json()
            dados_pagina = despesas_data.get("dados", [])

            if not dados_pagina:
                break  # sem mais páginas

            despesas.extend(dados_pagina)
            pagina += 1

        if despesas:
            st.success(f"{len(despesas)} despesa(s) encontrada(s):")

            df = pd.DataFrame(despesas)
            df["valorDocumento"] = pd.to_numeric(df.get("valorDocumento", 0), errors="coerce").fillna(0)

            colunas_desejadas = ["ano", "mes", "tipoDespesa", "valorDocumento", "fornecedor"]
            colunas_existentes = [col for col in colunas_desejadas if col in df.columns]

            if colunas_existentes:
                st.dataframe(df[colunas_existentes])
            else:
                st.warning("Não há colunas esperadas disponíveis para exibição.")

            # --- Gráficos ---
            st.markdown("### 📊 Gráfico de Despesas")

            if not df.empty:
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
                st.warning("Não foi possível gerar gráficos — dados vazios.")

        else:
            st.warning("Nenhuma despesa encontrada para este deputado.")

    except requests.RequestException as e:
        st.error(f"Erro ao consultar as despesas: {e}")
