
import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Previsões Futebol - Por Data", layout="wide")
st.title("📊 Previsões de Jogos por Data")

# Seletor de data
data_selecionada = st.date_input("📅 Escolha a data da análise", value=datetime.today())
data_formatada = data_selecionada.strftime('%Y-%m-%d')

# Simulação de dados por data (dados fictícios)
jogos = [
    {"data": data_formatada, "campeonato": "Libertadores", "jogo": "Talleres vs São Paulo", "gols_mandante": 0.73, "gols_visitante": 1.27, "sofre_mandante": 1.0, "sofre_visitante": 0.93, "empates_rec": 0.7, "vitorias_mandante": 0.2, "vitorias_visitante": 0.3},
    {"data": data_formatada, "campeonato": "Premier League", "jogo": "Arsenal vs Man City", "gols_mandante": 1.9, "gols_visitante": 2.1, "sofre_mandante": 1.2, "sofre_visitante": 0.8, "empates_rec": 0.2, "vitorias_mandante": 0.3, "vitorias_visitante": 0.5},
    {"data": data_formatada, "campeonato": "Brasileirão", "jogo": "Palmeiras vs Flamengo", "gols_mandante": 1.7, "gols_visitante": 1.5, "sofre_mandante": 1.1, "sofre_visitante": 1.3, "empates_rec": 0.2, "vitorias_mandante": 0.4, "vitorias_visitante": 0.4},
    {"data": data_formatada, "campeonato": "Eredivisie", "jogo": "Ajax vs PSV", "gols_mandante": 2.1, "gols_visitante": 2.0, "sofre_mandante": 1.4, "sofre_visitante": 1.1, "empates_rec": 0.25, "vitorias_mandante": 0.35, "vitorias_visitante": 0.4}
]

# Filtro por data
jogos_data = [j for j in jogos if j["data"] == data_formatada]

# Algoritmo preditivo avançado
def analisar(j):
    media_gols = j["gols_mandante"] + j["gols_visitante"]
    ambas_marcam = j["gols_mandante"] > 0.9 and j["gols_visitante"] > 0.9
    mais_25_gols = media_gols > 2.5

    ataque_forca = (j["gols_mandante"] + j["gols_visitante"]) / 2
    defesa_fraqueza = (j["sofre_mandante"] + j["sofre_visitante"]) / 2
    confianca = round((ataque_forca + defesa_fraqueza) * 10, 1)

    total = j["vitorias_mandante"] + j["vitorias_visitante"] + j["empates_rec"]
    prob_mandante = round((j["vitorias_mandante"] / total) * 100, 1)
    prob_empate = round((j["empates_rec"] / total) * 100, 1)
    prob_visitante = round((j["vitorias_visitante"] / total) * 100, 1)

    risco = "Baixo" if confianca >= 30 else "Médio" if confianca >= 20 else "Alto"

    return {
        "Jogo": j["jogo"],
        "Campeonato": j["campeonato"],
        "Média de Gols": round(media_gols, 2),
        "+2.5 Gols": "Sim" if mais_25_gols else "Não",
        "Ambas Marcam": "Sim" if ambas_marcam else "Não",
        "Vitória Mandante (%)": prob_mandante,
        "Empate (%)": prob_empate,
        "Vitória Visitante (%)": prob_visitante,
        "Confiabilidade": confianca,
        "Risco da Aposta": risco,
    }

df = pd.DataFrame([analisar(j) for j in jogos_data])
st.dataframe(df, use_container_width=True)
st.caption("⚠️ Previsões baseadas em dados simulados. Resultados não garantidos.")
