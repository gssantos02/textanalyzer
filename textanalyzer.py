import streamlit as st
import pandas as pd

st.title("Ticket Classifier")

st.header("Upload Ticket Data")

uploaded_file = st.file_uploader("Upload a .csv file")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  df = df.head(5)

