import streamlit as st
import pandas as pd

st.title("Ticket Classifier")

st.header("Upload Ticket Data")
uploaded_file = st.file_uploader("Upload a .csv file")
