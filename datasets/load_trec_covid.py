import ir_datasets
import json
import os

# =========================
# Load Dataset
# =========================

dataset = ir_datasets.load(
    "beir/trec-covid"
)

documents = []
queries = []
qrels = []

# =========================
# Documents
# =========================

for doc in dataset.docs_iter():

    documents.append({

        "id": str(doc.doc_id),

        "title": doc.title if doc.title else "",

        "text": doc.text if doc.text else ""

    })

# =========================
# Queries
# =========================

for query in dataset.queries_iter():

    queries.append({

        "id": str(query.query_id),

        "text": query.text

    })

# =========================
# Qrels
# =========================

for qrel in dataset.qrels_iter():

    qrels.append({

        "query_id": str(qrel.query_id),

        "doc_id": str(qrel.doc_id),

        "relevance": int(qrel.relevance)

    })

# =========================
# Create Folder
# =========================

os.makedirs(
    "datasets/raw/trec_covid",
    exist_ok=True
)

# =========================
# Save Documents
# =========================

with open(
    "datasets/raw/trec_covid/documents.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        documents,
        f,
        ensure_ascii=False,
        indent=4
    )

# =========================
# Save Queries
# =========================

with open(
    "datasets/raw/trec_covid/queries.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        queries,
        f,
        ensure_ascii=False,
        indent=4
    )

# =========================
# Save Qrels
# =========================

with open(
    "datasets/raw/trec_covid/qrels.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        qrels,
        f,
        ensure_ascii=False,
        indent=4
    )

# =========================
# Statistics
# =========================

print(
    f"Documents: {len(documents)}"
)

print(
    f"Queries: {len(queries)}"
)

print(
    f"Qrels: {len(qrels)}"
)

print(
    "TREC-COVID dataset saved successfully."
)

# =========================
# Read Test
# =========================

with open(
    "datasets/raw/trec_covid/documents.json",
    "r",
    encoding="utf-8"
) as f:

    documents = json.load(f)

print("\nFirst Document:\n")

print(documents[0])