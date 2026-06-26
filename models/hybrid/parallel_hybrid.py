from models.hybrid.fusion_methods import (
    min_max_normalize,
    weighted_sum
)


class ParallelHybridRetriever:

    def __init__(
        self,
        bm25_retriever,
        embedding_retriever
    ):

        self.bm25 = bm25_retriever
        self.embedding = embedding_retriever

    def search(
        self,
        query,
        top_k=10,
        alpha=0.7,
        candidate_docs=1000
    ):

        bm25_results = self.bm25.search(
            query,
            top_k=candidate_docs
        )

        embedding_results = self.embedding.search(
            query,
            top_k=candidate_docs
        )

        bm25_scores = {}
        embedding_scores = {}
        combined_docs = {}

        for doc in bm25_results:

            doc_id = str(doc["doc_id"])

            bm25_scores[doc_id] = doc["score"]

            if doc_id not in combined_docs:
                combined_docs[doc_id] = doc

        for doc in embedding_results:

            doc_id = str(doc["doc_id"])

            embedding_scores[doc_id] = doc["score"]

            if doc_id not in combined_docs:
                combined_docs[doc_id] = doc

        bm25_scores = min_max_normalize(
            bm25_scores
        )

        embedding_scores = min_max_normalize(
            embedding_scores
        )

        fused_results = []

        for doc_id, doc in combined_docs.items():

            bm25_score = bm25_scores.get(
                doc_id,
                0.0
            )

            embedding_score = embedding_scores.get(
                doc_id,
                0.0
            )

            final_score = weighted_sum(
                bm25_score,
                embedding_score,
                alpha
            )

            item = doc.copy()

            item["bm25_score"] = bm25_score
            item["embedding_score"] = embedding_score
            item["score"] = final_score

            fused_results.append(item)

        fused_results.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return fused_results[:top_k]


