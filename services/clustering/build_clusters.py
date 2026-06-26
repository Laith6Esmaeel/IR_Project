import json
import numpy as np

from sklearn.cluster import MiniBatchKMeans
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))


from models.embedding.embedding_model import (
    EmbeddingModel
)

print("Loading documents...")

with open(
    "datasets/processed/trec_covid/documents_processed.json",
    "r",
    encoding="utf-8"
) as f:

    documents = json.load(f)

texts = [

    doc["processed_text"]

    for doc in documents
]

print("Loading existing embeddings...")

embeddings = np.load(
    "models/embedding/document_embeddings.npy"
)

print(
    f"Embeddings loaded: {embeddings.shape}"
)

print("Building clusters...")

NUM_CLUSTERS = 15

kmeans = MiniBatchKMeans(

    n_clusters=NUM_CLUSTERS,

    batch_size=1000,

    random_state=42
)

cluster_ids = kmeans.fit_predict(
    embeddings
)

clusters = {}

for doc, cluster_id in zip(
    documents,
    cluster_ids
):

    cluster_id = int(cluster_id)

    if cluster_id not in clusters:

        clusters[cluster_id] = []

    clusters[cluster_id].append(
        doc["id"]
    )

with open(
    "services/clustering/clusters.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        clusters,
        f,
        indent=4
    )

np.save(
    "services/clustering/cluster_centers.npy",
    kmeans.cluster_centers_
)

print("Clusters saved")