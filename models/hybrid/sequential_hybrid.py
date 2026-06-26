import numpy as np

from models.embedding.embedding_model import (
    EmbeddingModel
)


class SequentialHybridRetriever:

    def __init__(self, bm25_retriever):

        self.bm25 = bm25_retriever

        self.embedding_model = EmbeddingModel()

    # =========================
    # Normalize Scores
    # =========================

    def normalize_scores(self, scores):

        scores = np.array(scores)

        if len(scores) == 0:

            return np.array([])

        if scores.max() == scores.min():

            return np.ones(len(scores))

        return (

            scores - scores.min()

        ) / (

            scores.max() - scores.min()

        )

    # =========================
    # Sequential Hybrid Search
    # =========================

    def search(
        self,
        processed_query,
        original_query,
        top_k=5,
        bm25_top_n=100,
        alpha=0.4
    ):

        # =========================
        # Step 1: BM25 Retrieval
        # =========================

        bm25_results = self.bm25.search(
            processed_query,
            top_k=bm25_top_n
        )

        # =========================
        # Remove Zero BM25 Scores
        # =========================

        bm25_results = [

            doc

            for doc in bm25_results

            if doc["score"] > 0
        ]

        if len(bm25_results) == 0:

            return []

        # =========================
        # Step 2: Encode Documents
        # =========================

        texts = [

            doc["processed_text"]

            for doc in bm25_results
        ]

        doc_embeddings = self.embedding_model.encode(
            texts
        )

        # =========================
        # Step 3: Encode Query
        # =========================

        query_embedding = self.embedding_model.encode(
            [original_query]
        )

        # =========================
        # Step 4: Cosine Similarity
        # =========================

        similarities = np.dot(
            doc_embeddings,
            query_embedding.T
        ).flatten()

        # =========================
        # Step 5: Normalize BM25
        # =========================

        bm25_scores = [

            doc["score"]

            for doc in bm25_results
        ]

        normalized_bm25 = self.normalize_scores(
            bm25_scores
        )

        # =========================
        # Step 6: Fusion
        # =========================

        results = []

        for i, doc in enumerate(bm25_results):

            bm25_score = float(
                normalized_bm25[i]
            )

            embedding_score = float(
                similarities[i]
            )

            final_score = (

                alpha * bm25_score

                +

                (1 - alpha) * embedding_score
            )

            results.append({

                "doc_id":
                    doc["doc_id"],

                "original_text":
                    doc["original_text"],

                "processed_text":
                    doc["processed_text"],

                "bm25_score":
                    float(doc["score"]),

                "embedding_score":
                    embedding_score,

                "final_score":
                    final_score
            })

        # =========================
        # Step 7: Sort by Final Score
        # =========================

        results.sort(
            key=lambda x: x["final_score"],
            reverse=True
        )

        # =========================
        # Step 8: Return Top K
        # =========================

        return results[:top_k]