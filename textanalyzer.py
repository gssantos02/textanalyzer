import streamlit as st
import pandas as pd
from transformers import pipeline

##@st.cache(allow_output_mutation=True)
#def load_model(model_name):
  #classifier = pipeline(model_name)
  #return(classifier)
#classifier = load_model("zero-shot-classification")

st.title("Ticket Classifier")
st.header("Upload Ticket Data")

uploaded_file = st.file_uploader("Upload a .csv file")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  df = df["Title"]
  st.write(df)
  
with st.form("Sample Description"):
   prompt = st.text_area("Prompt", "Sample Ticket Description")
   submit = st.form_submit_button("Generate Category")
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


