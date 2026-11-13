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

st.write("Lignes :", len(df))   # provisoire, a supprimer a l'etape 3