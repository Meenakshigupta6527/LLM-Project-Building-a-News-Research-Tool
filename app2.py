import streamlit as st
from langchain_config import llm_chain, get_summary

# Streamlit UI Setup
st.set_page_config(page_title="AI News Research Tool",layout="centered")

st.markdown("# AI News Research Tool")
st.write("This tool help users efficiently gather, analyze, and summarize news articles from various sources.")
groq_api_key = st.text_input("Your Groq API Key:", type="password")
newsapi_key = st.text_input("Your NewsAPI Key:", type="password")

query = st.text_input("Type your query:")

# Search Button
if st.button("Search & Analyze"):
    if query and newsapi_key and groq_api_key:
        summaries = get_summary(query, newsapi_key, days)
        response = llm_chain.run({"query": query, "summaries": summaries})
        
        st.write("### Summary:")
        st.write(response)
    else:
        st.error("Please fill all the Details.")
