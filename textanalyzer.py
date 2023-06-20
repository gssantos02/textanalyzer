import streamlit as st
import pandas as pd

st.title("Ticket Classifier")

st.header("Upload Ticket Data")

with st.form("Uplod File"):
  uploaded_file = st.file_uploader("Upload a .csv file")
  upload = st.form_submit_button("Upload")
  if submit:
    df = pd.read_csv(uploaded_file)
    #st.write(df.head(5))
