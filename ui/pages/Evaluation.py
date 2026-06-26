# import streamlit as st
# import requests
# import pandas as pd

# API_URL = "http://localhost:8000"

# st.title(
#     "📊 Evaluation Dashboard"
# )

# col1, col2 = st.columns(2)

# with col1:

#     if st.button(
#         "Load Evaluation"
#     ):

#         response = requests.post(
#             f"{API_URL}/evaluate"
#         )

#         results = response.json()

#         df = pd.DataFrame(
#             results
#         )

#         st.dataframe(
#             df,
#             use_container_width=True
#         )

#         st.subheader(
#             "MAP Comparison"
#         )

#         st.bar_chart(
#             df.set_index(
#                 "Model"
#             )["MAP"]
#         )

#         st.subheader(
#             "MRR Comparison"
#         )

#         st.bar_chart(
#             df.set_index(
#                 "Model"
#             )["MRR"]
#         )

#         st.subheader(
#             "nDCG@10 Comparison"
#         )

#         st.bar_chart(
#             df.set_index(
#                 "Model"
#             )["nDCG@10"]
#         )

#         st.subheader(
#             "Precision@10 Comparison"
#         )

#         st.bar_chart(
#             df.set_index(
#                 "Model"
#             )["Precision@10"]
#         )
        
#         st.subheader(
#             "Recall@10 Comparison"
#         )

#         st.bar_chart(
#             df.set_index(
#                 "Model"
#             )["Recall@10"]
#         )

# with col2:

#     if st.button(
#         "Run Evaluation Again"
#     ):

#         with st.spinner(
#             "Running Evaluation..."
#         ):

#             response = requests.post(
#                 f"{API_URL}/run-evaluation"
#             )

#             results = response.json()

#             st.success(
#                 "Evaluation Finished"
#             )

#             df = pd.DataFrame(
#                 results
#             )

#             st.dataframe(
#                 df,
#                 use_container_width=True
#             )






import streamlit as st
import requests
import pandas as pd

API_URL = "http://localhost:8000"

st.title(
    "Evaluation Dashboard"
)

# ====================================
# Load Existing Evaluation
# ====================================

if st.button(
    "Load Evaluation"
):

    response = requests.post(
        f"{API_URL}/evaluate"
    )

    results = response.json()

    df = pd.DataFrame(
        results
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    st.markdown("---")

    metrics = [

        "MAP",

        "MRR",

        "nDCG@10",

        "Precision@10",

        "Recall@10"
    ]

    for metric in metrics:

        st.subheader(
            metric
        )

        chart = df.set_index(
            "Model"
        )[[metric]]

        st.bar_chart(
            chart
        )

# ====================================
# Run Evaluation Again
# ====================================

if st.button(
    "Run Evaluation Again"
):

    with st.spinner(
        "Running Evaluation..."
    ):

        response = requests.post(
            f"{API_URL}/run-evaluation"
        )

        results = response.json()

        st.success(
            "Evaluation Finished"
        )

        df = pd.DataFrame(
            results
        )

        st.dataframe(
            df,
            use_container_width=True
        )

        st.markdown("---")

        metrics = [

            "MAP",

            "MRR",

            "nDCG@10",

            "Precision@10",

            "Recall@10"
        ]

        for metric in metrics:

            st.subheader(
                metric
            )

            chart = df.set_index(
                "Model"
            )[[metric]]

            st.bar_chart(
                chart
            )

# ====================================
# Best Model Section
# ====================================

st.markdown("---")

if st.button(
    "Show Best Models"
):

    response = requests.post(
        f"{API_URL}/evaluate"
    )

    results = response.json()

    df = pd.DataFrame(
        results
    )

    st.subheader(
        "Best Model Per Metric"
    )

    metrics = [

        "MAP",

        "MRR",

        "nDCG@10",

        "Precision@10",

        "Recall@10"
    ]

    for metric in metrics:

        best_row = df.loc[
            df[metric].idxmax()
        ]

        st.success(
            f"{metric}: "
            f"{best_row['Model']} "
            f"({best_row[metric]:.4f})"
        )