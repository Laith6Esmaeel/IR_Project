import json
import numpy as np

from models.embedding.embedding_model import (
    EmbeddingModel
)
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))


class ClusterService:

    def __init__(self):

        with open(
            "services/clustering/clusters.json",
            "r",
            encoding="utf-8"
        ) as f:

            self.clusters = json.load(f)

        self.centers = np.load(
            "services/clustering/cluster_centers.npy"
        )

        self.embedding_model = (
            EmbeddingModel()
        )
    def get_top_clusters(
        self,
        query,
        top_n=5
    ):

        query_embedding = (
            self.embedding_model.encode(
                [query]
            )[0]
        )

        similarities = np.dot(
            self.centers,
            query_embedding
        )

        top_clusters = np.argsort(
            similarities
        )[::-1][:top_n]

        return [
            str(c)
            for c in top_clusters
        ]

    # def get_cluster(
    #     self,
    #     query
    # ):

    #     query_embedding = (
    #         self.embedding_model.encode(
    #             [query]
    #         )[0]
    #     )

    #     similarities = np.dot(
    #         self.centers,
    #         query_embedding
    #     )

    #     cluster_id = np.argmax(
    #         similarities
    #     )

    #     return str(cluster_id)

    