from services.clustering.cluster_service import (
    ClusterService
)


class ClusteredBM25:

    def __init__(
        self,
        bm25,
        documents
    ):

        self.bm25 = bm25

        self.documents = documents

        self.cluster_service = (
            ClusterService()
        )

    def search(
        self,
        processed_query,
        original_query,
        top_k=10
    ):
    

#         cluster_id = (
#             self.cluster_service.get_cluster(
#                 original_query
#             )
#         )

        
#         cluster_docs = set(
#     str(doc_id)

#     for doc_id in

#     self.cluster_service.clusters[
#         cluster_id
#     ]
# )
        cluster_ids = (
            self.cluster_service.get_top_clusters(
                original_query,
                top_n=5
            )
        )

        cluster_docs = set()

        for cid in cluster_ids:

            cluster_docs.update(

                str(doc_id)

                for doc_id in

                self.cluster_service.clusters[cid]
            )

        results = self.bm25.search(
            processed_query,
            top_k=10000
        )

        results = [

            doc

            for doc in results

          if str(
    doc["doc_id"]
) in cluster_docs
        ]

        return results[:top_k]