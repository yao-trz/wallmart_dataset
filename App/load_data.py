import streamlit as st
import pandas as pd
import joblib

@st.cache_data
def load_data() -> pd.DataFrame:
    df: pd.DataFrame = joblib.load("../Walmart_Sales.pkl")

    return df