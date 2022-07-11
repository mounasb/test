import streamlit as st

st.text("Du texte pour tester des trucs")
EMAIL = st.secrets.EMAIL
PASSWORD = st.secrets.PASSWORD
st.write(EMAIL)
st.write(PASSWORD)
