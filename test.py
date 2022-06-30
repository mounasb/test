import streamlit as st
# from dotenv import load_dotenv
# import os
#
# load_dotenv()
#
# EMAIL = 'blabla@grrr.com'
# PASSWORD = 'hophop'

st.text("Du texte pour tester des truuuuqueuh")
EMAIL = st.secrets.EMAIL
PASSWORD = st.secrets.PASSWORD
st.write(EMAIL)
st.write(PASSWORD)
# st.write(os.getenv("EMAIL"))
# st.write(os.getenv("PASSWORD"))
