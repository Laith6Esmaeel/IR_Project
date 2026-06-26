from services.clustering.cluster_service import (
    ClusterService
)

from models.embedding.embedding_model import (
    EmbeddingModel
)

import numpy as np


class ClusteredEmbeddingRetriever:

    def __init__(
        self,
        documents,
        embeddings
    ):

        self.documents = documents

        self.embeddings = embeddings

        self.cluster_service = (
            ClusterService()
        )

        self.embedding_model = (
            EmbeddingModel()
        )

        self.doc_map = {

            str(doc["id"]): i

            for i, doc in enumerate(
                documents
            )
        }

    def search(
        self,
        query,
        top_k=10
    ):

        # cluster_id = (

        #     self.cluster_service.get_cluster(
        #         query
        #     )
        # )

        # cluster_docs = (

        #     self.cluster_service.clusters[
        #         cluster_id
        #     ]
        # )
        cluster_ids = (
            self.cluster_service.get_top_clusters(
                query,
                top_n=5
            )
        )

        cluster_docs = []

        for cid in cluster_ids:

            cluster_docs.extend(

                self.cluster_service.clusters[cid]
            )





        query_embedding = (

            self.embedding_model.encode(
                [query]
            )[0]
        )

        results = []

        for doc_id in cluster_docs:

            idx = self.doc_map[
                str(doc_id)
            ]

            similarity = np.dot(

                self.embeddings[idx],

                query_embedding
            )

            doc = self.documents[idx]

            results.append({

                "doc_id":
                    doc["id"],

                "score":
                    float(similarity),

                "original_text":
                    doc["original_text"],

                "processed_text":
                    doc["processed_text"]
            })

        results.sort(

            key=lambda x: x["score"],

            reverse=True
        )

        return results[:top_k]