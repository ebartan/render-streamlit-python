import streamlit as st
import pandas as pd
from streamlit_extras.tags import tagger_component

st.caption('Hi 👋, I am ebartan - A LLM Resercher & No-code & Full Stack Developer From Yalikavak/Bodrum/Turkey')
st.write("""
# Eray Bartan
As an OpenAI GPT Implementer and Expert Full Stack Developer with 18 years of experience in the municipality sector, I specialize in no-code and low-code solutions to streamline workflows and enhance user experiences. *Thanks!*""")
st.write("""# Topics dealing with in recent days""")
tagger_component(
        "Here are colored tags",
        ["turtle", "rabbit", "lion"],
        color_name=["blue", "orange", "lightblue"],
    )