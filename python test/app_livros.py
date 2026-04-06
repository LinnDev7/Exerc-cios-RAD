import streamlit as st
import pandas as pd

# 1. Título do seu Aplicativo
st.title("📚 Dashboard da Minha Livraria")
st.markdown("Analise o catálogo de 12 mil livros de forma interativa.")

# 2. Carregar e Limpar os Dados (Sua lógica da Aula 2)
# Usamos o cache para o app não ficar lento ao recarregar
@st.cache_data
def carregar_dados():
    df = pd.read_csv("livros.csv", sep=";", encoding='latin1')
    # Limpeza básica que fizemos antes
    df_limpo = df[df["paginas"] > 0].copy()
    df_limpo["decada"] = (df_limpo["ano"].fillna(0) // 10 * 10).astype(int)
    return df_limpo

df = carregar_dados()

# 3. Filtro na Barra Lateral
st.sidebar.header("Configurações")
ano_minimo = st.sidebar.slider("Filtrar por ano de início:", 
                               int(df["ano"].min()), 
                               int(df["ano"].max()), 
                               2000)

# Aplicando o filtro
df_filtrado = df[df["ano"] >= ano_minimo]

# 4. Exibindo os Resultados
col1, col2 = st.columns(2)
with col1:
    st.metric("Total de Livros", len(df_filtrado))
with col2:
    st.metric("Média de Páginas", f"{df_filtrado['paginas'].mean():.0f}")

st.subheader("Tabela de Livros Filtrados")
st.dataframe(df_filtrado.head(100)) # Mostra os primeiros 100 resultados

# 5. Gráfico Visual
st.subheader("Distribuição de Livros por Década")
contagem_decada = df_filtrado.groupby("decada").size()
st.bar_chart(contagem_decada)