from models.tfidf.tfidf_model import TFIDFRetriever
from services.preprocessing.preprocessing_service import PreprocessingService
import json
# load processed documents
with open(
    "datasets/processed/scifact/documents_processed.json",
    "r",
    encoding="utf-8"
) as f:
    documents = json.load(f)

# create preprocessor
preprocessor = PreprocessingService()

# create model
retriever = TFIDFRetriever()

# fit model
retriever.fit(documents)

# raw query
query = "cancer treatment"

# 🔥 IMPORTANT: preprocess query
processed_query = preprocessor.preprocess(query)

# search using processed query
results = retriever.search(processed_query, top_k=5)

# print results
for rank, result in enumerate(results, start=1):

    print(f"\nRank #{rank}")
    print("Doc ID:", result["doc_id"])
    print("Score:", result["score"])
    print("Text:", result["original_text"][:300])