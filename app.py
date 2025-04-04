
import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Previsões Diárias de Futebol", layout="wide")
st.title("📅 Jogos de Hoje - Previsões de Futebol")

# Mostrar data
hoje = datetime.now().strftime('%d/%m/%Y')
st.markdown(f"🗓️ Jogos do dia: **{hoje}**")

# Dados simulados com datas
jogos = [
    # Libertadores
    {"data": "2025-04-04", "campeonato": "Libertadores", "jogo": "Talleres vs São Paulo", "gols_mandante": 0.73, "gols_visitante": 1.27, "empates_rec": 0.7, "vitorias_mandante": 0.2, "vitorias_visitante": 0.3},
    {"data": "2025-04-04", "campeonato": "Libertadores", "jogo": "Universidad de Chile vs Botafogo", "gols_mandante": 2.2, "gols_visitante": 0.93, "empates_rec": 0.25, "vitorias_mandante": 0.35, "vitorias_visitante": 0.4},
    # Brasileirão
    {"data": "2025-04-04", "campeonato": "Brasileirão", "jogo": "Palmeiras vs Flamengo", "gols_mandante": 1.7, "gols_visitante": 1.5, "empates_rec": 0.2, "vitorias_mandante": 0.4, "vitorias_visitante": 0.4},
    # Premier League
    {"data": "2025-04-04", "campeonato": "Premier League", "jogo": "Arsenal vs Manchester City", "gols_mandante": 1.9, "gols_visitante": 2.1, "empates_rec": 0.2, "vitorias_mandante": 0.3, "vitorias_visitante": 0.5},
    # Eredivisie
    {"data": "2025-04-04", "campeonato": "Eredivisie", "jogo": "Ajax vs PSV", "gols_mandante": 2.1, "gols_visitante": 2.0, "empates_rec": 0.25, "vitorias_mandante": 0.35, "vitorias_visitante": 0.4},
    # Argentina
    {"data": "2025-04-04", "campeonato": "Argentina", "jogo": "Boca Juniors vs River Plate", "gols_mandante": 1.6, "gols_visitante": 1.7, "empates_rec": 0.3, "vitorias_mandante": 0.3, "vitorias_visitante": 0.4},
]

# Filtrar apenas os jogos do dia
jogos_hoje = [j for j in jogos if j["data"] == datetime.now().strftime('%Y-%m-%d')]

# Função preditiva
def analisar_jogo(d):
    media_total_gols = d["gols_mandante"] + d["gols_visitante"]
    ambas_marcam = "Sim" if d["gols_mandante"] > 0.9 and d["gols_visitante"] > 0.9 else "Não"
    mais_25_gols = "Sim" if media_total_gols > 2.5 else "Não"

    total = d["vitorias_mandante"] + d["vitorias_visitante"] + d["empates_rec"]
    prob_mandante = round((d["vitorias_mandante"] / total) * 100, 1)
    prob_empate = round((d["empates_rec"] / total) * 100, 1)
    prob_visitante = round((d["vitorias_visitante"] / total) * 100, 1)

    return {
        "Jogo": d["jogo"],
        "Campeonato": d["campeonato"],
        "Média de Gols": round(media_total_gols, 2),
        "+2.5 Gols": mais_25_gols,
        "Ambas Marcam": ambas_marcam,
        "Vitória Mandante (%)": prob_mandante,
        "Empate (%)": prob_empate,
        "Vitória Visitante (%)": prob_visitante,
    }

# Gerar tabela
df = pd.DataFrame([analisar_jogo(j) for j in jogos_hoje])

# Mostrar
st.dataframe(df, use_container_width=True)
st.markdown("---")
st.caption("⚠️ Dados simulados. Use com responsabilidade.")
