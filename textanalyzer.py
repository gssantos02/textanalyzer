import streamlit as st
import pandas as pd
from transformers import pipeline



st.title("Ticket Classifier")
st.header("Upload Ticket Data")

uploaded_file = st.file_uploader("Upload a .csv file")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  df = df["Title"]
  st.write(df)
  
with st.form("Sample Description"):
   prompt = st.text_area("Prompt", "Input sample ticket description")
   submit = st.form_submit_button("Submit")
if submit:
  st.write("Functioning correctly")
#if submit is not None:
  #classifier = pipeline("zero-shot-classification")
  #res = classifier(
    #prompt,
    #candidate_labels=['access','hardware','software'],
  #)
  #tag = res['labels'][0]
  #st.write(tag)


