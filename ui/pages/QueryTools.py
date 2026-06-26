import streamlit as st
import requests

SUGGEST_API = "http://localhost:8000/suggest"

REFINE_API = "http://localhost:8000/refine"

st.title(
    "Query Assistance Tools"
)

tab1, tab2 = st.tabs(
    [
        "Query Suggestions",
        "Query Refinement"
    ]
)

# =====================================
# Suggestions
# =====================================

with tab1:

    st.subheader(
        "Query Suggestions"
    )

    prefix = st.text_input(
        "Enter Prefix",
        key="suggest"
    )

    limit = st.slider(
        "Number of Suggestions",
        1,
        20,
        10
    )

    if st.button(
        "Get Suggestions"
    ):

        response = requests.post(

            SUGGEST_API,

            json={
                "query": prefix,
                "limit": limit
            }
        )

        data = response.json()

        st.success(
            "Suggestions Generated"
        )

        for item in data[
            "suggestions"
        ]:

            st.write(
                f"• {item}"
            )

# =====================================
# Refinement
# =====================================

with tab2:

    st.subheader(
        "Query Refinement"
    )

    query = st.text_input(
        "Enter Query",
        key="refine"
    )

    if st.button(
        "Refine Query"
    ):

        response = requests.post(

            REFINE_API,

            json={
                "query": query
            }
        )

        data = response.json()

        st.success(
            "Refinement Completed"
        )

        st.write(
            "Original Query:",
            data["original_query"]
        )

        st.write(
            "Corrected Query:",
            data["corrected_query"]
        )

        st.write(
            "Expanded Query:",
            data["expanded_query"]
        )

        st.write(
            "Processed Query:",
            data["processed_query"]
        )