import json

from semantic_search import SemanticRetriever

with open(
    "datasets/processed/trec_covid/documents_processed.json",
    "r",
    encoding="utf-8"
) as f:

    docs = json.load(f)

retriever = SemanticRetriever()

retriever.load_documents(docs)

results = retriever.search(
    "breast cancer",
    top_k=5
)

for result in results:

    print(
        result["id"],
        result["original_text"]
    )