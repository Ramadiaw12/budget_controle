import streamlit as st

# Lire le fichier HTML
with open("dashboard.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Afficher le HTML
st.components.v1.html(html_content, height=800, scrolling=True)