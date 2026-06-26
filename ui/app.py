import streamlit as st

st.set_page_config(
    page_title="IR System",
    page_icon="🔎",
    layout="wide"
)

st.title(
    "Hybrid Information Retrieval System"
)

st.markdown("""
### Features

- TF-IDF
- BM25
- Embedding Search
- Hybrid Sequential
- Hybrid Parallel
- Query Suggestions
- Query Expansion
- Evaluation Dashboard

Use the pages menu on the left.
""")