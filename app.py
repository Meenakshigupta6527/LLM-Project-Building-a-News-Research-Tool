import streamlit as st
import pandas as pd
from langchain_config import llm_chain, get_summary

# Page Config
st.set_page_config(page_title="AI News Research Tool", page_icon="📰", layout="wide")

# Storage for queries
if "query_history" not in st.session_state:
    st.session_state.query_history = []

# Custom Styling
st.markdown(
    """
    <style>
        .stButton>button {
            font-size: 16px;
            padding: 10px 20px;
            border-radius: 10px;
            background-color: #4CAF50;
            color: white;
        }
        .stDownloadButton>button {
            font-size: 14px;
            padding: 8px 15px;
            border-radius: 8px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.title("🔎 AI News Research Tool")
st.markdown("#### Get AI-powered news summaries instantly!")

# Input Section
query = st.text_input("🔍 Enter your query:", placeholder="E.g., AI in Healthcare")

col1, col2 = st.columns([1, 4])
with col1:
    submit = st.button("Get News 📰", use_container_width=True)

if submit:
    if query.strip():
        with st.spinner("Fetching latest news... ⏳"):
            summaries = get_summary(query)
            response = llm_chain.run({"query": query, "summaries": summaries})

            # Save Query & Response
            st.session_state.query_history.append({"Query": query, "Summary": response})

            st.success("✅ Summary Generated!")
            st.subheader("🔹 AI Summary:")
            st.write(response)
    else:
        st.warning("⚠️ Please enter a query before searching.")

# Download History Section
if st.session_state.query_history:
    with st.expander("📜 View Query History", expanded=False):
        df = pd.DataFrame(st.session_state.query_history)
        st.dataframe(df, use_container_width=True)

        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Download History", csv, "summary_history.csv", "text/csv")
