
import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Previsões Futebol", layout="wide")
st.title("📊 Previsões de Jogos - Futebol Internacional")

st.markdown(f"🗓️ Atualizado em: **{datetime.now().strftime('%d/%m/%Y')}**")

# Dados simulados para vários campeonatos
jogos = [
    # Libertadores
    {"campeonato": "Libertadores", "jogo": "Talleres vs São Paulo", "gols_mandante": 0.73, "gols_visitante": 1.27, "empates_rec": 0.7, "vitorias_mandante": 0.2, "vitorias_visitante": 0.3},
    {"campeonato": "Libertadores", "jogo": "Universidad de Chile vs Botafogo", "gols_mandante": 2.2, "gols_visitante": 0.93, "empates_rec": 0.25, "vitorias_mandante": 0.35, "vitorias_visitante": 0.4},
    # Brasileirão
    {"campeonato": "Brasileirão", "jogo": "Palmeiras vs Flamengo", "gols_mandante": 1.7, "gols_visitante": 1.5, "empates_rec": 0.2, "vitorias_mandante": 0.4, "vitorias_visitante": 0.4},
    {"campeonato": "Brasileirão", "jogo": "Grêmio vs Internacional", "gols_mandante": 1.3, "gols_visitante": 1.1, "empates_rec": 0.3, "vitorias_mandante": 0.3, "vitorias_visitante": 0.4},
    # Premier League
    {"campeonato": "Premier League", "jogo": "Arsenal vs Manchester City", "gols_mandante": 1.9, "gols_visitante": 2.1, "empates_rec": 0.2, "vitorias_mandante": 0.3, "vitorias_visitante": 0.5},
    # La Liga
    {"campeonato": "La Liga", "jogo": "Real Madrid vs Atlético Madrid", "gols_mandante": 2.0, "gols_visitante": 1.3, "empates_rec": 0.25, "vitorias_mandante": 0.45, "vitorias_visitante": 0.3},
    # Serie A
    {"campeonato": "Serie A (Itália)", "jogo": "Juventus vs Milan", "gols_mandante": 1.5, "gols_visitante": 1.4, "empates_rec": 0.3, "vitorias_mandante": 0.3, "vitorias_visitante": 0.4},
    # Bundesliga
    {"campeonato": "Bundesliga", "jogo": "Bayern vs Dortmund", "gols_mandante": 2.4, "gols_visitante": 1.8, "empates_rec": 0.2, "vitorias_mandante": 0.5, "vitorias_visitante": 0.3},
    # Eredivisie
    {"campeonato": "Eredivisie", "jogo": "Ajax vs PSV", "gols_mandante": 2.1, "gols_visitante": 2.0, "empates_rec": 0.25, "vitorias_mandante": 0.35, "vitorias_visitante": 0.4},
    # Argentina
    {"campeonato": "Argentina", "jogo": "Boca Juniors vs River Plate", "gols_mandante": 1.6, "gols_visitante": 1.7, "empates_rec": 0.3, "vitorias_mandante": 0.3, "vitorias_visitante": 0.4}
]

# Função de previsão
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
        "Média de Gols": round(media_total_gols, 2),
        "+2.5 Gols": mais_25_gols,
        "Ambas Marcam": ambas_marcam,
        "Vitória Mandante (%)": prob_mandante,
        "Empate (%)": prob_empate,
        "Vitória Visitante (%)": prob_visitante,
    }

# Selecionar campeonato
campeonatos = sorted(set(j["campeonato"] for j in jogos))
selecao = st.selectbox("Selecione o Campeonato", campeonatos)

# Filtrar e aplicar previsões
dados_filtrados = [j for j in jogos if j["campeonato"] == selecao]
df = pd.DataFrame([analisar_jogo(j) for j in dados_filtrados])

# Exibir
st.dataframe(df, use_container_width=True)
st.markdown("---")
st.caption("⚠️ As previsões são baseadas em médias simuladas. Use com responsabilidade.")
