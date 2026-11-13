import pandas as pd
import streamlit as st

st.set_page_config(page_title="Catalogue", page_icon="📚", layout="wide")

FICHIER = "data/livres_poetry.csv"

@st.cache_data
def charger_donnees(chemin):
    return pd.read_csv(chemin)

st.title("Catalogue de livres")
st.caption("Donnees collectées sur books.toscrape.com")

df = charger_donnees(FICHIER)

with st.sidebar:
    st.header("Filtres")
    note_mini = st.slider("Note minimale", 1, 5, 1)
    prix_min, prix_max = st.slider("Fourchette de prix", 0.0, 60.0, (0.0, 60.0))
    recherche = st.text_input("Le titre contient")

selection = df.copy()
selection = selection[selection["note"] >= note_mini]
selection = selection[selection["prix_gbp"] >= prix_min]
selection = selection[selection["prix_gbp"] <= prix_max]
if recherche:
    selection = selection[selection["titre"].str.contains(recherche, case=False)]

col1, col2, col3, col4 = st.columns(4)
col1.metric("Livres retenus", len(selection))
col2.metric("Prix moyen", f"{selection['prix_gbp'].mean():.2f} GBP")
col3.metric("Note moyenne", f"{selection['note'].mean():.2f} / 5")
col4.metric("Stock total", selection["stock"].sum())