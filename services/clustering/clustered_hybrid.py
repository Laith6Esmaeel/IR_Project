# import numpy as np

# from services.clustering.cluster_service import (
#     ClusterService
# )

# from models.embedding.embedding_model import (
#     EmbeddingModel
# )


# class ClusteredHybridRetriever:

#     def __init__(
#         self,
#         bm25_retriever,
#         documents,
#         embeddings
#     ):

#         self.bm25 = bm25_retriever

#         self.documents = documents

#         self.embeddings = embeddings

#         self.cluster_service = (
#             ClusterService()
#         )

#         self.embedding_model = (
#             EmbeddingModel()
#         )

#         self.doc_map = {

#             str(doc["id"]): i

#             for i, doc in enumerate(
#                 documents
#             )
#         }

#     def normalize(
#         self,
#         scores
#     ):

#         scores = np.array(scores)

#         if len(scores) == 0:

#             return scores

#         if scores.max() == scores.min():

#             return np.ones(
#                 len(scores)
#             )

#         return (

#             scores - scores.min()

#         ) / (

#             scores.max() - scores.min()
#         )

#     def search(
#         self,
#         query,
#         top_k=10,
#         alpha=0.5
#     ):

#         cluster_id = (

#             self.cluster_service.get_top_clusters(
#                 query
#             )
#         )

#         cluster_docs = set(

#             self.cluster_service.clusters[
#                 cluster_id
#             ]
#         )

#         bm25_results = self.bm25.search(
#             query,
#             top_k=10000
#         )

#         bm25_results = [

#             r

#             for r in bm25_results

#             if str(
#                 r["doc_id"]
#             ) in cluster_docs
#         ]

#         if len(
#             bm25_results
#         ) == 0:

#             return []

#         query_embedding = (

#             self.embedding_model.encode(
#                 [query]
#             )[0]
#         )

#         bm25_scores = [

#             r["score"]

#             for r in bm25_results
#         ]

#         bm25_scores = self.normalize(
#             bm25_scores
#         )

#         results = []

#         for i, r in enumerate(
#             bm25_results
#         ):

#             idx = self.doc_map[
#                 str(
#                     r["doc_id"]
#                 )
#             ]

#             emb_score = float(
#                 np.dot(
#                     self.embeddings[idx],
#                     query_embedding
#                 )
#             )

#             final_score = (

#                 alpha *
#                 bm25_scores[i]

#                 +

#                 (1 - alpha)
#                 * emb_score
#             )

#             doc = self.documents[idx]

#             results.append({

#                 "doc_id":
#                     doc["id"],

#                 "bm25_score":
#                     float(
#                         r["score"]
#                     ),

#                 "embedding_score":
#                     emb_score,

#                 "final_score":
#                     float(
#                         final_score
#                     ),

#                 "original_text":
#                     doc["original_text"],

#                 "processed_text":
#                     doc["processed_text"]
#             })

#         results.sort(

#             key=lambda x:
#             x["final_score"],

#             reverse=True
#         )

#         return results[:top_k]



import numpy as np

from services.clustering.cluster_service import (
    ClusterService
)

from models.embedding.embedding_model import (
    EmbeddingModel
)


class ClusteredHybridRetriever:

    def __init__(
        self,
        bm25_retriever,
        documents,
        embeddings
    ):

        self.bm25 = bm25_retriever

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

    def normalize(
        self,
        scores
    ):

        scores = np.array(scores)

        if len(scores) == 0:
            return scores

        if scores.max() == scores.min():
            return np.ones(
                len(scores)
            )

        return (
            scores - scores.min()
        ) / (
            scores.max() - scores.min()
        )

    def search(
        self,
        query,
        top_k=10,
        alpha=0.5
    ):

        # الحصول على أفضل Clusters
        # cluster_ids = (
        #     self.cluster_service.get_top_clusters(
        #         query
        #     )
        # )
        cluster_ids = (
    self.cluster_service.get_top_clusters(
        query
    )
)

        # إذا رجع Cluster واحد فقط
        if not isinstance(
            cluster_ids,
            (list, tuple, set)
        ):
            cluster_ids = [cluster_ids]

        # جمع جميع الوثائق من الـ Clusters المختارة
        cluster_docs = set()

        for cid in cluster_ids:

                if cid in self.cluster_service.clusters:

                    cluster_docs.update(
            map(
                str,
                self.cluster_service.clusters[cid]
            )
        )

        if len(cluster_docs) == 0:
            return []

        bm25_results = self.bm25.search(
            query,
            top_k=10000
        )

        bm25_results = [
            r
            for r in bm25_results
            if str(
                r["doc_id"]
            ) in cluster_docs
        ]

        if len(
            bm25_results
        ) == 0:
            return []

        query_embedding = (
            self.embedding_model.encode(
                [query]
            )[0]
        )

        bm25_scores = [
            r["score"]
            for r in bm25_results
        ]

        bm25_scores = self.normalize(
            bm25_scores
        )

        results = []

        for i, r in enumerate(
            bm25_results
        ):

            doc_id = str(
                r["doc_id"]
            )

            if doc_id not in self.doc_map:
                continue

            idx = self.doc_map[
                doc_id
            ]

            emb_score = float(
                np.dot(
                    self.embeddings[idx],
                    query_embedding
                )
            )

            final_score = (
                alpha *
                bm25_scores[i]
                +
                (1 - alpha)
                * emb_score
            )

            doc = self.documents[idx]

            results.append({

                "doc_id":
                    doc["id"],

                "bm25_score":
                    float(
                        r["score"]
                    ),

                "embedding_score":
                    emb_score,

                "final_score":
                    float(
                        final_score
                    ),

                "original_text":
                    doc["original_text"],

                "processed_text":
                    doc["processed_text"]

            })

        results.sort(
            key=lambda x:
            x["final_score"],
            reverse=True
        )

        return results[:top_k]