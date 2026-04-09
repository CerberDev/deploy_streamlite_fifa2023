import streamlit as st
import requests
import base64
from Utils.data_loader import carregar_dados


# A interface avisa o usuário que está trabalhando para os casos em que demorar carregar a tela
with st.spinner("⏳ Carregando dados e buscando fotos dos servidores..."):

    @st.cache_data
    def get_image_base64(url):
        """
        Baixa a imagem da URL passando-se por um navegador real 
        e converte para Base64 para exibição segura no DataFrame.
        """
        if not isinstance(url, str) or url.strip() == "" or url.strip() == "0" or url == "nan":
            return None

        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0",
                "Accept": "image/avif,image/webp,*/*",
                "Accept-Language": "en-US,en;q=0.5",
                "Connection": "keep-alive",
            }
            response = requests.get(url, headers=headers, timeout=5)

            if response.status_code == 200:
                b64 = base64.b64encode(response.content).decode()
                return f"data:image/png;base64,{b64}"
        except Exception:
            return None

        return None



# 2. Carrega os dados e aplica os filtros iniciais (mesmo processo da aba principal, mas sem remover a coluna 'Photo')
# Recupera os dados salvos na memória pela aba principal
    df_data = carregar_dados()

# Filtros na barra lateral
clubes = df_data["Club"].value_counts().index
club = st.sidebar.selectbox("Clube", clubes) 

# Filtra a tabela para manter apenas os jogadores do clube selecionado
# Utilizamos o .copy() para modificar o dataframe com segurança depois
df_filtered = df_data[df_data["Club"] == club].copy()
df_filtered = df_filtered.set_index("Name")



# 3. Mostra o escudo do time e o nome do clube

st.markdown(f"## {club}")

# Captura apenas o texto do link da primeira linha (índice 0)
foto_clube = str(df_filtered.iloc[0]["Club Logo"])

# Verifica se a foto é um texto válido
if foto_clube.strip() != "" and foto_clube.strip() != "0" and foto_clube != "nan":
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0",
            "Accept": "image/avif,image/webp,*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
        }
        response = requests.get(foto_clube, headers=headers, timeout=5)
        
        if response.status_code == 200:
            st.image(response.content)
        else:
            st.warning("O servidor original bloqueou a exibição deste escudo específico.")
            
    except Exception:
        st.warning("Falha de conexão ao tentar baixar o escudo do time.")
else:
    st.warning("O escudo deste time não está disponível na base de dados.")

st.divider()



# 4. Jogadores
st.subheader("Elenco")

#Converte tanto a foto do jogador quanto a bandeira (Flag) para Base64
with st.spinner("Carregando fotos e nacionalidades..."):
    df_filtered["Photo_Display"] = df_filtered["Photo"].apply(get_image_base64)
    df_filtered["Flag_Display"] = df_filtered["Flag"].apply(get_image_base64) 

# Define as colunas que irão aparecer na tabela (usando Flag_Display no lugar de Flag)
columns = [
    "Photo_Display", "Age", "Flag_Display", "Overall", "Value", 
    "Wage", "Joined", "Height", "Weight", 
    "Contract Valid Until", "Release Clause"
]

# Trata o valor máximo do salário para evitar erros caso a coluna esteja vazia
max_wage = float(df_filtered["Wage"].max()) if not df_filtered["Wage"].isna().all() else 1000

# 1. Trata a Altura: 
# Remove "cm", converte a coluna para decimal (float), divide por 100 e formata adicionando o "m"
df_filtered["Height"] = (df_filtered["Height"].str.replace("cm", "").astype(float) / 100).apply(lambda x: f"{x:.2f} m")

# 2. Trata o Peso:
# Substitui o "kg" grudado por um " kg" com espaço (Ex: "82kg" vira "82 kg")
df_filtered["Weight"] = df_filtered["Weight"].str.replace("kg", " kg")

# Exibe a tabela com as colunas selecionadas e as configurações de formatação
st.dataframe(
    df_filtered[columns],
    column_config={
            "Overall": st.column_config.ProgressColumn(
            "Overall", min_value=0, max_value=100
        ),
        "Wage": st.column_config.ProgressColumn(
            "Weekly Wage", format="€ %d", min_value=0, max_value=max_wage
        ),
        "Photo_Display": st.column_config.ImageColumn("Foto"),
        "Flag_Display": st.column_config.ImageColumn("Country"),
        

    },
)