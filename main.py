import streamlit as st

# Configuraçã globa das páginas
st.set_page_config(page_title="FIFA 23 Dashboard", layout="wide")

# Mapeamento das páginas
home = st.Page("paginas/1_Home.py", title="Home", icon="🏠", default=True)
players = st.Page("paginas/2_players.py", title="Players", icon="🏃🏽‍♀️‍➡️")
teams = st.Page("paginas/3_teams.py", title="Teams", icon="⚽")

# Criando a navegação
pg = st.navigation([home, players, teams])

#Executando as paginas selecionadas
pg.run()