import streamlit as st
import plotly.express as px
import joblib
import pandas as pd

@st.cache_data
def load_data():
    df: pd.DataFrame = joblib.load("../Walmart_Sales.pkl")
    return df

@st.cache_data
def plot_correlation_matrix(df: pd.DataFrame):
    corr_matrix = df.corr()
    fig = px.imshow(
        corr_matrix, 
        text_auto=True, 
        aspect="auto", 
        color_continuous_scale="RdBu_r"
    )

    return fig

df = load_data()

st.markdown("### :material/data_exploration: Analyse Exploratoire")

st.markdown("##### Aperçu des données")
st.dataframe(df)
st.info(f"{df.shape[0]} lignes et {df.shape[1]} colonnes")

st.markdown("##### Nombre de valeurs manquantes par colonne")
st.table(df.isnull().sum(), hide_header=True)

st.markdown("##### Nombre de valeurs uniques par colonne")
st.table(df.nunique(), hide_header=True)

st.markdown("##### Statistiques descriptives")
st.dataframe(df.describe())

st.markdown("##### Types de données par colonne")
st.table(df.dtypes, hide_header=True)

st.markdown("##### Matrice de corrélation")
st.plotly_chart(plot_correlation_matrix(df), width="stretch")
