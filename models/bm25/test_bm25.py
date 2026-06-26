import json

from services.preprocessing.preprocessing_service import PreprocessingService

from models.bm25.bm25_model import BM25Retriever

# =========================
# Load Documents
# =========================

with open(
    "datasets/processed/trec_covid/documents_processed.json",
    "r",
    encoding="utf-8"
) as f:

    documents = json.load(f)

# =========================
# Init Services
# =========================

preprocessor = PreprocessingService()

retriever = BM25Retriever()

# =========================
# Fit Model
# =========================

retriever.fit(documents)

# =========================
# Query
# =========================

query = "cancer treatment"

processed_query = preprocessor.preprocess(query)

# =========================
# Search
# =========================

results = retriever.search(
    processed_query,
    top_k=5
)

# =========================
# Results
# =========================

for rank, result in enumerate(results, start=1):

    print("\n====================")

    print(f"Rank #{rank}")

    print("Score:", result["score"])

    print("Text:", result["original_text"][:300])