pip3 install streamlit
pip3 install openai
pip3 install pandas

import streamlit as st
import pandas as pd

st.title("Ticket Classifier")
st.info("Group tickets based on their description")

st.header("Upload Ticket Data")
uploaded_file = st.fileuploader("Upload a .csv file")
