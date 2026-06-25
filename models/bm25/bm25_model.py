import pickle

from rank_bm25 import BM25Okapi


class BM25Retriever:

    def __init__(self, k1=1.5, b=0.75):

        self.k1 = k1

        self.b = b

        self.bm25 = None

        self.documents = []

    # =========================
    # Fit Model
    # =========================

    def fit(self, processed_documents):

        self.documents = processed_documents

        tokenized_corpus = []

        for doc in processed_documents:

            tokens = doc["processed_text"].split()

            tokenized_corpus.append(tokens)

        self.bm25 = BM25Okapi(
            tokenized_corpus,
            k1=self.k1,
            b=self.b
        )

    # =========================
    # Search
    # =========================

    def search(self, processed_query, top_k=5):

        query_tokens = processed_query.split()

        scores = self.bm25.get_scores(query_tokens)

        ranked_indices = sorted(
            range(len(scores)),
            key=lambda i: scores[i],
            reverse=True
        )[:top_k]

        results = []

        for idx in ranked_indices:

            results.append({

                "doc_id": self.documents[idx]["id"],

                "score": float(scores[idx]),

                "original_text": self.documents[idx]["original_text"],

                "processed_text": self.documents[idx]["processed_text"]
            })

        return results

    # =========================
    # Save Model
    # =========================

    def save_model(self, path):

        with open(path, "wb") as f:

            pickle.dump({

                "k1": self.k1,

                "b": self.b,

                "bm25": self.bm25,

                "documents": self.documents

            }, f)

    # =========================
    # Load Model
    # =========================

    def load_model(self, path):

        with open(path, "rb") as f:

            data = pickle.load(f)

        self.k1 = data["k1"]

        self.b = data["b"]

        self.bm25 = data["bm25"]

        self.documents = data["documents"]

