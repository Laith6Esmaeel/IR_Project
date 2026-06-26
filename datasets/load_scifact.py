# import ir_datasets

# dataset = ir_datasets.load("beir/scifact/test")

# documents = []

# for doc in dataset.docs_iter():

#     documents.append({
#         "id": doc.doc_id,
#         "text": doc.text
#     })

# print(documents[0])


# queries = []

# for query in dataset.queries_iter():

#     queries.append({
#         "id": query.query_id,
#         "text": query.text
#     })

# print(queries[0])


# qrels = []

# for qrel in dataset.qrels_iter():

#     qrels.append({
#         "query_id": qrel.query_id,
#         "doc_id": qrel.doc_id,
#         "relevance": qrel.relevance
#     })

# print(qrels[0])

import ir_datasets
import json
import os

# تحميل dataset
dataset = ir_datasets.load("beir/scifact/test")

documents = []
queries = []
qrels = []

# =========================
# Documents
# =========================

for doc in dataset.docs_iter():

    documents.append({
        "id": doc.doc_id,
        "text": doc.text
    })

# =========================
# Queries
# =========================

for query in dataset.queries_iter():

    queries.append({
        "id": query.query_id,
        "text": query.text
    })

# =========================
# Qrels
# =========================

for qrel in dataset.qrels_iter():

    qrels.append({
        "query_id": qrel.query_id,
        "doc_id": qrel.doc_id,
        "relevance": qrel.relevance
    })

# =========================
# Create Folder
# =========================

os.makedirs("datasets/raw/scifact", exist_ok=True)

# =========================
# Save Files
# =========================

with open("datasets/raw/scifact/documents.json", "w", encoding="utf-8") as f:

    json.dump(documents, f, indent=4)

with open("datasets/raw/scifact/queries.json", "w", encoding="utf-8") as f:

    json.dump(queries, f, indent=4)

with open("datasets/raw/scifact/qrels.json", "w", encoding="utf-8") as f:

    json.dump(qrels, f, indent=4)

print("SciFact dataset saved successfully.")


#تجربة اعادة القرائة بعد الحفظ
import json

with open("datasets/raw/scifact/documents.json", "r", encoding="utf-8") as f:

    documents = json.load(f)

print(documents[1])