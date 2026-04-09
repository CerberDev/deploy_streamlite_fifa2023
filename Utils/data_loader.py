import pandas as pd
import streamlit as st
from datetime import datetime
from pathlib import Path
def clean_money(value):
    """Limpa a formatação do dinheiro na base Fifa."""
    if pd.isna(value):
        return None
    value = str(value).replace("€", "").replace(",", "").strip()

    if "M" in value:
        return float(value.replace("M","")) * 1_000_000
    elif "K" in value:
        return float(value.replace("K","")) * 1_000
    else:
        try:
            return float(value)
        except:
            return None
        
@st.cache_data
def carregar_dados():
    """Lê e trata o dataset. O cache evita que isso rode duas vezes."""
    #Descobre onde o script atual está rodando e monta o caminho dinamicamente
    pasta_raiz = Path(__file__).parent.parent
    caminho_csv = pasta_raiz /"datasets"/"FIFA23_official_data.csv"
    df_data = pd.read_csv(caminho_csv, index_col=0)

    df_data["Value"] = df_data["Value"].apply(clean_money)
    df_data["Wage"] = df_data["Wage"].apply(clean_money)
    df_data["Release Clause"] = df_data["Release Clause"].apply(clean_money)

    df_data["Contract Valid Until"] = pd.to_numeric(df_data["Contract Valid Until"], errors='coerce')
    df_data = df_data.dropna(subset=["Value", "Contract Valid Until"])

    current_year = datetime.now().year
    df_data = df_data[df_data["Contract Valid Until"] >= current_year]
    df_data = df_data[df_data["Value"] > 0 ]

    return df_data.sort_values(by="Overall", ascending=False)