import streamlit as st
import pandas as pd
from transformers import pipeline

classifier = pipeline("zero-shot-classification")

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
  if submit is not None:
    res = classifier(
      prompt,
      candidate_labels=['access','hardware','software'],
    )
    res = res['labels'][0]
    st.write(res)


