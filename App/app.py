import streamlit as st

pages = [
    st.Page(
        page="exploratory_analysis", 
        title="Exploratory Analysis",
        icon=":material/analytics"
    ),
]

app = st.navigation(pages)

app.run()