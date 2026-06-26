import streamlit as st
import plotly.express as px
import joblib
import pandas as pd

@st.cache_data
def load_data() -> pd.DataFrame:
    df: pd.DataFrame = joblib.load("../Walmart_Sales.pkl")

    return df

@st.cache_data
def plot_sales_histogram(df: pd.DataFrame, store: list[int], nbins: int = 50):
    fig = px.histogram(
        df[df["Store"].isin(store)], 
        x="Weekly_Sales", 
        nbins=nbins,
    )

    return fig

@st.cache_data
def plot_sales_boxplot(df: pd.DataFrame, store: list[int]):
    fig = px.box(
        df[df["Store"].isin(store)], 
        x="Store", 
        y="Weekly_Sales", 
        color="Store"
    )

    return fig

@st.cache_data
def plot_histograms(df: pd.DataFrame, col: str, store: list[int], nbins: int = 50):
    fig = px.histogram(
        df[df["Store"].isin(store)], 
        x=col, 
        nbins=nbins,
    )

    return fig

df = load_data()

st.markdown("### :material/data_exploration: Analyse Exploratoire")
st.markdown("#### Aperçu général des données")


st.markdown("##### :red-badge[Aperçu des données]")
st.dataframe(df)
st.info(f"{df.shape[0]} lignes et {df.shape[1]} colonnes")

st.markdown("##### :red-badge[Nombre de valeurs manquantes par colonne]")
st.table(df.isnull().sum(), hide_header=True)

st.markdown("##### :red-badge[Nombre de valeurs uniques par colonne]")
st.table(df.nunique(), hide_header=True)

st.markdown("##### :red-badge[Statistiques descriptives]")
st.dataframe(df.describe())

st.markdown("##### :red-badge[Types de données par colonne]")
st.table(df.dtypes, hide_header=True)


st.markdown("#### Analyse par magasin")

st.multiselect(
    "Sélectionnez les magasins à analyser",
    options=df["Store"].unique(),
    default=df["Store"].unique(),
    key="store_selection"
)

st.markdown("##### :red-badge[Distribution des ventes hebdomadaires]")

nbins = (
    50 
    if "nbins_slider" not in st.session_state 
    else st.session_state.nbins_slider
)

st.plotly_chart(
    plot_sales_histogram(
        df, 
        st.session_state.store_selection, 
        nbins
    )
)

st.slider(
    "Sélectionnez le nombre de barres pour l'histogramme",
    min_value=10,
    max_value=1000,
    value=50,
    step=1,
    key="nbins_slider"
)

st.markdown("##### :red-badge[Boxplot des ventes hebdomadaires par magasin]")
st.plotly_chart(
    plot_sales_boxplot(
        df, 
        st.session_state.store_selection
    )
)

st.markdown(
    "##### :red-badge[Ventes hebdomadaires moyennes par magasin]"
    )

st.toggle(
    "Afficher les ventes hebdomadaires moyennes par magasin",
    key="show_stats"
)

if st.session_state.show_stats:

    st.info(
        "**Vente Moyenne par magasin :** \n" +
        "\n".join(
            [
                f"- Magasin {store} : "
                f"{df[df['Store'] == store]['Weekly_Sales'].mean():,.2f}" 
                for store in st.session_state.store_selection
            ]
        ) 
    )

st.selectbox(
    "Sélectionnez la colonne à analyser",
    options=["Temperature", "Fuel_Price", "CPI", "Unemployment"],
    key="col_selection"
)

st.markdown(
    f"##### :red-badge[Distribution de {st.session_state.col_selection}]"
)

nbins_2 = (
    50 
    if "nbins_slider_2" not in st.session_state 
    else st.session_state.nbins_slider_2
)

st.plotly_chart(
    plot_histograms(
        df, 
        st.session_state.col_selection, 
        st.session_state.store_selection,
        nbins_2
    )
)

st.slider(
    "Sélectionnez le nombre de barres pour l'histogramme",
    min_value=10,
    max_value=1000,
    value=50,
    step=1,
    key="nbins_slider_2"
)

st.markdown("#### Analyse selon les semaines fériées")