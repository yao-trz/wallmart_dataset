import streamlit as st

pages = [
    st.Page(
        page="exploratory_analysis.py", 
        title="Analyse Exploratoire",
        icon=":material/data_exploration:"
    ),
    st.Page(
        page="statistical_analysis.py",
        title="Analyse Statistique",
        icon=":material/scatter_plot:"
    )
]

app = st.navigation(pages, position="top")

app.run()