import streamlit as st
from transformers import pipeline

#Load the summarization model
@st.cache_resource
def load_summarizer():
  return pipeline("summarization",model="ARTeLab/mbart-summarization-fanpage")

summarizer=load_summarizer()
st.title("AI Text Summarize")
st.write("Enter a long text below, and get a concise summary!")
# Text Input
long_text = st.text_area("Enter text to Summarize:", height=200)

#Summary parameters
max_length = st.slider("Max Summary Length", min_value=50, max_value=300, value=130)
min_length = st.slider("Min Summary Length", min_value=20, max_value=100, value=30)
if st.button("Summarize"):
  if long_text.strip():
    with st.spinner("Generating summary... "):
        summary = summarizer(long_text, max_length=max_length, min_length=min_length, do_sample=false)
        st.subheader("Summary:")
        st.success(sumary[0]['summary_text'])
else:
  st.warning("Please enter some text to summarize.")
    
