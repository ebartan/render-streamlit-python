import streamlit as st
import pandas as pd
import requests
from streamlit_lottie import st_lottie
from typing_extensions import Literal

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

# Apply local CSS styles from the "style.css" file   
local_css("style/style.css")

# Load Lottie animations from various URLs
lottie_gif = load_lottieurl("https://lottie.host/4ce1cb87-98a3-4d76-98ae-60e13fa6e972/DpCBjgCfaZ.json")
st.caption('Hi 👋, I am ebartan - A LLM Resercher & No-code & Full Stack Developer From Yalikavak/Bodrum/Turkey')
st.write("""
# Eray Bartan
As an OpenAI GPT Implementer and Expert Full Stack Developer with 18 years of experience in the municipality sector, I specialize in no-code and low-code solutions to streamline workflows and enhance user experiences. *Thanks!*""")
st.write("""# Topics dealing with in recent days""")
with st.container():
    st.subheader('⚒️ Skills')
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        st_lottie(lottie_gif, height=70,width=70, key="python", speed=2.5)
