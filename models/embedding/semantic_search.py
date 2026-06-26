import json
import faiss

from models.embedding.embedding_model import (
    EmbeddingModel
)


class SemanticRetriever:

    def __init__(self):

        self.model = EmbeddingModel()

        self.index = faiss.read_index(
            "models/embedding/faiss.index"
        )

        self.documents = []

        with open(
            "datasets/processed/trec_covid/documents_processed.json",
            "r",
            encoding="utf-8"
        ) as f:

            self.documents = json.load(f)

    def search(
        self,
        query,
        top_k=5
    ):

        query_embedding = self.model.encode(
            [query]
        )

        scores, indices = self.index.search(
            query_embedding.astype("float32"),
            top_k
        )

        results = []

        for score, idx in zip(
            scores[0],
            indices[0]
        ):

            doc = self.documents[idx]

            results.append({

                "doc_id": doc["id"],

                "score": float(score),

                "original_text":
                    doc["original_text"],

                "processed_text":
                    doc["processed_text"]
            })

        return results