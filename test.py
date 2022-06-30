from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

EMAIL = 'blabla@grrr.com'
PASSWORD = 'hophop'

st.write(EMAIL)
st.write(PASSWORD)
st.text("Du texte pour tester des truuuuqueuh")
st.write(os.getenv("EMAIL"))
st.write(os.getenv("PASSWORD"))
