# import streamlit as st
# import requests

# API_URL = "http://localhost:8000/search"

# st.title("Search Engine")

# query = st.text_input(
#     "Enter Query"
# )

# model = st.selectbox(
#     "Choose Model",
#     [
#         "tfidf",
#         "bm25",
#         "embedding",
#         "hybrid_serial",
#         "hybrid_parallel"
#     ]
# )

# top_k = st.slider(
#     "Top K",
#     1,
#     20,
#     10
# )

# st.markdown("---")

# st.subheader("BM25 Parameters")

# k1 = st.slider(
#     "k1",
#     0.5,
#     3.0,
#     1.5,
#     0.1
# )

# b = st.slider(
#     "b",
#     0.0,
#     1.0,
#     0.75,
#     0.05
# )

# st.markdown("---")

# st.subheader("Hybrid Parallel Parameter")

# alpha = st.slider(
#     "Alpha",
#     0.0,
#     1.0,
#     0.5,
#     0.05
# )

# st.markdown("---")

# spell_correction = st.checkbox(
#     "Enable Spell Correction",
#     value=True
# )

# query_expansion = st.checkbox(
#     "Enable Query Expansion",
#     value=False
# )

# if st.button("Search"):

#     payload = {

#         "query": query,

#         "model": model,

#         "top_k": top_k,

#         "k1": k1,

#         "b": b,

#         "alpha": alpha,

#         "use_spell_correction":
#             spell_correction,

#         "use_query_expansion":
#             query_expansion
#     }

#     response = requests.post(
#         API_URL,
#         json=payload
#     )

#     data = response.json()

#     st.success("Search Completed")

#     st.markdown("## Query Information")

#     st.write(
#         "Original Query:",
#         data["original_query"]
#     )

#     st.write(
#         "Corrected Query:",
#         data["corrected_query"]
#     )

#     st.write(
#         "Expanded Query:",
#         data["expanded_query"]
#     )

#     st.write(
#         "Processed Query:",
#         data["processed_query"]
#     )

#     st.markdown("---")

#     st.markdown(
#         f"## Results ({len(data['results'])})"
#     )

#     for rank, result in enumerate(
#         data["results"],
#         start=1
#     ):

#         with st.expander(
#             f"Rank {rank} | {result['doc_id']}"
#         ):

#             st.write(
#                 f"Document ID: {result['doc_id']}"
#             )

#             if "score" in result:

#                 st.write(
#                     f"Score: {result['score']:.4f}"
#                 )

#             if "final_score" in result:

#                 st.write(
#                     f"Final Score: {result['final_score']:.4f}"
#                 )

#             if "bm25_score" in result:

#                 st.write(
#                     f"BM25 Score: {result['bm25_score']:.4f}"
#                 )

#             if "embedding_score" in result:

#                 st.write(
#                     f"Embedding Score: {result['embedding_score']:.4f}"
#                 )

#             st.markdown("### Document")

#             st.write(
#                 result["original_text"]
#             )











import streamlit as st
import requests

API_URL = "http://localhost:8000/search"

st.title("Search Engine")

query = st.text_input(
    "Enter Query"
)

model = st.selectbox(
    "Choose Model",
    [
        "tfidf",
        "bm25",
        "embedding",
        "hybrid_serial",
        "hybrid_parallel",
        "clustered_bm25",
        "clustered_embedding",
        "clustered_hybrid"
    ]
)

top_k = st.slider(
    "Top K",
    1,
    20,
    10
)

st.markdown("---")

st.subheader("BM25 Parameters")

k1 = st.slider(
    "k1",
    0.5,
    3.0,
    1.5,
    0.1
)

b = st.slider(
    "b",
    0.0,
    1.0,
    0.75,
    0.05
)

st.markdown("---")

st.subheader("Hybrid Alpha")

alpha = st.slider(
    "Alpha",
    0.0,
    1.0,
    0.5,
    0.05
)

st.markdown("---")

spell_correction = st.checkbox(
    "Enable Spell Correction",
    value=True
)

query_expansion = st.checkbox(
    "Enable Query Expansion",
    value=False
)

if st.button("Search"):

    payload = {

        "query": query,

        "model": model,

        "top_k": top_k,

        "k1": k1,

        "b": b,

        "alpha": alpha,

        "use_spell_correction":
            spell_correction,

        "use_query_expansion":
            query_expansion
    }

    response = requests.post(
        API_URL,
        json=payload
    )

    if response.status_code != 200:

        st.error(
            f"API Error: {response.text}"
        )

        st.stop()

    data = response.json()

    st.success("Search Completed")

    st.markdown("## Query Information")

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

    st.markdown("---")

    st.markdown(
        f"## Results ({len(data['results'])})"
    )

    for rank, result in enumerate(
        data["results"],
        start=1
    ):

        title = f"Rank {rank} | Doc {result['doc_id']}"

        with st.expander(title):

            st.write(
                f"Document ID: {result['doc_id']}"
            )

            if "score" in result:

                st.write(
                    f"Score: {result['score']:.4f}"
                )

            if "final_score" in result:

                st.write(
                    f"Final Score: {result['final_score']:.4f}"
                )

            if "bm25_score" in result:

                st.write(
                    f"BM25 Score: {result['bm25_score']:.4f}"
                )

            if "embedding_score" in result:

                st.write(
                    f"Embedding Score: {result['embedding_score']:.4f}"
                )

            st.markdown("### Document")

            st.write(
                result["original_text"]
            )