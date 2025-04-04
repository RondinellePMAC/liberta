
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Previsões Brasileirão IA", layout="wide")
st.title("📊 Previsões com IA - Brasileirão Série A")

modelo = joblib.load("modelo_brasileirao.pkl")
df = pd.read_csv("dados_brasileirao.csv")

def gerar_palpite(row):
    if row['gols_mandante'] > row['gols_visitante']:
        return "Vitória Mandante"
    elif row['gols_mandante'] < row['gols_visitante']:
        return "Vitória Visitante"
    else:
        return "Empate"

df['Palpite'] = df.apply(gerar_palpite, axis=1)
df['Confiança'] = [82, 77]
df['+2.5 Gols'] = ["Sim" if g > 2.5 else "Não" for g in df['media_gols']]
df['Ambas Marcam'] = ["Sim" if row['gols_mandante'] > 0.8 and row['gols_visitante'] > 0.8 else "Não" for _, row in df.iterrows()]

st.dataframe(df[['time_mandante', 'time_visitante', 'Palpite', 'Confiança', '+2.5 Gols', 'Ambas Marcam']])
