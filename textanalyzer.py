import streamlit as st
import openai

st.title("Ticket Classifier")
st.info("Group tickets based on their description")

st.header("Upload Ticket Data")
uploaded_file = st.fileuploader("Upload a .csv file")
