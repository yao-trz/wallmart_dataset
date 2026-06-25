import streamlit as st

pages = [
    st.Page(
        page="exploratory_analysis.py", 
        title="Analyse Exploratoire",
        icon=":material/analytics:"
    ),
]

app = st.navigation(pages)

app.run()