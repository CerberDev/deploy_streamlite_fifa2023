import streamlit as st
import requests
from Utils.data_loader import carregar_dados
# Configurações de página


# A interface avisa o usuário que está trabalhando para os casos em que demorar carregar a tela
with st.spinner("⏳ Carregando dados e buscando fotos dos servidores..."):
# Recupera os dados salvos na memória pela aba principal
    df_data = carregar_dados()

# Filtros na barra lateral
clubes = df_data["Club"].value_counts().index
club = st.sidebar.selectbox("Clube", clubes) 

# Filtra a tabela para manter apenas os jogadores do clube selecionado
df_players = df_data[df_data["Club"] == club]

# Filtra o jogador
players = df_players["Name"].value_counts().index
player = st.sidebar.selectbox("Jogador", players) 

# Captura a única linha com todas as estatísticas do jogador escolhido
player_stats = df_players[df_players["Name"] == player].iloc[0]


# 1. EXIBE O CABEÇALHO PRIMEIRO
st.title(player_stats["Name"])
st.markdown(f"**Clube:** {player_stats['Club']}")

# Limpa o texto da posição para exibir apenas a última parte
posicao_limpa = str(player_stats['Position']).split(">")[-1]
st.markdown(f"**Posição:** {posicao_limpa}")


# 2. EXIBE A FOTO
foto = player_stats["Photo"]

# Verifica se a foto é um texto válido
if isinstance(foto, str) and foto.strip() != "" and foto.strip() != "0":
    try:
        # Cabeçalhos completos simulando um navegador real
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0",
            "Accept": "image/avif,image/webp,*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
        }
        
        response = requests.get(foto, headers=headers, timeout=5)
        
        if response.status_code == 200:
            st.image(response.content)
        else:
            st.warning("O servidor original bloqueou a exibição desta foto específica.")
            
    except Exception:
        st.warning("Falha de conexão ao tentar baixar a foto.")
else:
    st.warning("A foto deste jogador não está disponível na base de dados.")


# 3. Exibe informações organizadas em colunas Idade,Altura e Peso
col1, col2, col3, col4 = st.columns(4)

# Trata altura
altura_cm = player_stats['Height'].replace("cm", "")
altura_metros = float(altura_cm) / 100

# Trata peso (ajustado para 'kg' minúsculo conforme a base de dados)
peso_limpo = player_stats['Weight'].replace("kg", "")

# Exibe informações organizadas em colunas
col1.markdown(f"**Idade:** {player_stats['Age']} anos")
col2.markdown(f"**Altura:** {altura_metros:.2f} m")
col3.markdown(f"**Peso:** {peso_limpo} kg")

st.divider()


# 4. Exibe estatísticas em formato de progress e valores de mercado
# Overall exibe a nota geral do jogador e uma barra de progresso visual
st.subheader(f"Overall: {player_stats['Overall']}")
st.progress(int(player_stats['Overall']))

# Adicionando colunas para organizar as finanças
col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Valor de Mercado", value=f"€ {player_stats['Value']:,.0f}")
col2.metric(label="Remuneração Semanal", value=f"€ {player_stats['Wage']:,.0f}")
col3.metric(label="Cláusula de Rescisão", value=f"€ {player_stats['Release Clause']:,.0f}")