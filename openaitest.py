import streamlit as st
import pandas as pd
from transformers import pipeline
import os
os.environ['OPENAI_API_KEY'] = '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'


st.title("OpenAI Test")

  
with st.form("Sample Description"):
   prompt = st.text_area("Prompt", "Input Prompt")
   submit = st.form_submit_button("Submit")
if submit:
  
  st.write("Functioning correctly")
