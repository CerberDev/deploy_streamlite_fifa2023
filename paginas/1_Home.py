from datetime import datetime
import streamlit as st
import webbrowser
import pandas as pd
from Utils.data_loader import carregar_dados

# A interface avisa o usuário que está trabalhando para os casos em que demorar carregar a tela
with st.spinner("Carregando os dados da página..."):
# Carrega os dados (roda a regra de negócio sem sujar a tela)
    df_data = carregar_dados()

# Interface da aba principal
st.markdown("# FIFA23 OFFICIAL DATASET! ⚽")
st.sidebar.markdown("Desenvolvido por [Alessandro França](https://www.linkedin.com/in/alessandro-franca-rpa-developer/)")

# Comentado para adicionar uma feature que funciona após clicar quando hospedado, da forma atual so abre no meu navegador
#btn = st.button("Acesse os dados do Kaggle")
#if btn:
 #   webbrowser.open_new_tab("https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database")

#Foram após deploy
btn = st.link_button("Acesse os dados do Kaggle","https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database")
st.markdown(
    """
O conjunto de dados de jogadores de futebol de 2023 fornece informações abrangentes sobre jogadores de futebol profissionais.
O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos do jogador, características físicas, estatísticas de jogo, detalhes do contrato e afiliações de clubes. 

Com **mais de 17.000 registros**, este conjunto de dados oferece um recurso valioso para analistas de futebol, pesquisadores e entusiastas interessados em explorar vários aspectos do mundo do futebol, pois permite estudar atributos de jogadores, métricas de desempenho, avaliação de mercado, análise de clubes, posicionamento de jogadores e desenvolvimento do jogador ao longo do tempo.
"""
)