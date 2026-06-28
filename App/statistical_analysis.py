import streamlit as st
import plotly.express as px
import pandas as pd

from load_data import load_data
df = load_data()

@st.cache_data
def plot_correlation_heatmap(df: pd.DataFrame):
    fig = px.imshow(
        df.corr(), 
        text_auto=True, 
        aspect="auto", 
        color_continuous_scale="peach", 
    )

    return fig

st.markdown("### :material/scatter_plot: Analyse Statistique")

st.markdown("##### :red-badge[Coorélations entre les variables]")
st.plotly_chart(plot_correlation_heatmap(df))