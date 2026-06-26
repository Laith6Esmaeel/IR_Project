# import json

# from services.evaluation.metrics import (
#     precision_at_k,
#     recall_at_k,
#     average_precision,
#     reciprocal_rank,
#     ndcg_at_k
# )


# class Evaluator:

#     def __init__(
#         self,
#         queries_path,
#         qrels_path
#     ):

#         with open(
#             queries_path,
#             "r",
#             encoding="utf-8"
#         ) as f:

#             self.queries = json.load(f)

#         with open(
#             qrels_path,
#             "r",
#             encoding="utf-8"
#         ) as f:

#             qrels = json.load(f)

#         self.qrels = {}

#         for item in qrels:

#             qid = str(item["query_id"])

#             if qid not in self.qrels:
#                 self.qrels[qid] = set()

#             if item["relevance"] > 0:

#                 self.qrels[qid].add(
#                     str(item["doc_id"])
#                 )

#     def evaluate_model(
#         self,
#         retriever,
#         model_name,
#         max_queries=50
#     ):

#         precision_scores = []
#         recall_scores = []
#         ap_scores = []
#         mrr_scores = []
#         ndcg_scores = []

#         evaluated = 0

#         for query in self.queries:

#             if evaluated >= max_queries:
#                 break

#             qid = str(query["id"])

#             if qid not in self.qrels:
#                 continue

#             relevant = self.qrels[qid]

#             if len(relevant) == 0:
#                 continue

#             try:

#                 if model_name == "embedding":

#                     results = retriever.search(
#                         query["original_text"],
#                         top_k=10
#                     )

#                 elif model_name == "hybrid_sequential":

#                     results = retriever.search(
#                         processed_query=query["processed_text"],
#                         original_query=query["original_text"],
#                         top_k=10
#                     )

#                 elif model_name == "hybrid_parallel":

#                     results = retriever.search(
#                         query["original_text"],
#                         top_k=10
#                     )

#                 else:

#                     results = retriever.search(
#                         query["processed_text"],
#                         top_k=10
#                     )

#             except Exception as e:

#                 print(
#                     f"ERROR {model_name} QID={qid}"
#                 )

#                 print(e)

#                 continue

#             retrieved = [

#                 str(r["doc_id"])

#                 for r in results
#             ]

#             precision_scores.append(
#                 precision_at_k(
#                     retrieved,
#                     relevant,
#                     10
#                 )
#             )

#             recall_scores.append(
#                 recall_at_k(
#                     retrieved,
#                     relevant,
#                     10
#                 )
#             )

#             ap_scores.append(
#                 average_precision(
#                     retrieved,
#                     relevant
#                 )
#             )

#             mrr_scores.append(
#                 reciprocal_rank(
#                     retrieved,
#                     relevant
#                 )
#             )

#             ndcg_scores.append(
#                 ndcg_at_k(
#                     retrieved,
#                     relevant,
#                     10
#                 )
#             )

#             evaluated += 1

#         if evaluated == 0:

#             return {

#                 "Queries Evaluated": 0,

#                 "MAP": 0,

#                 "Precision@10": 0,

#                 "Recall@10": 0,

#                 "MRR": 0,

#                 "nDCG@10": 0
#             }

#         return {

#             "Queries Evaluated": evaluated,

#             "MAP":
#                 sum(ap_scores)
#                 / len(ap_scores),

#             "Precision@10":
#                 sum(precision_scores)
#                 / len(precision_scores),

#             "Recall@10":
#                 sum(recall_scores)
#                 / len(recall_scores),

#             "MRR":
#                 sum(mrr_scores)
#                 / len(mrr_scores),

#             "nDCG@10":
#                 sum(ndcg_scores)
#                 / len(ndcg_scores)
#         }





import json

from services.evaluation.metrics import (
    precision_at_k,
    recall_at_k,
    average_precision,
    reciprocal_rank,
    ndcg_at_k
)


class Evaluator:

    def __init__(
        self,
        queries_path,
        qrels_path
    ):

        with open(
            queries_path,
            "r",
            encoding="utf-8"
        ) as f:

            self.queries = json.load(f)

        with open(
            qrels_path,
            "r",
            encoding="utf-8"
        ) as f:

            qrels = json.load(f)

        self.qrels = {}

        for item in qrels:

            qid = str(
                item["query_id"]
            )

            if qid not in self.qrels:

                self.qrels[qid] = set()

            if item["relevance"] > 0:

                self.qrels[qid].add(
                    str(item["doc_id"])
                )

    def evaluate_model(
        self,
        retriever,
        model_name,
        max_queries=50
    ):

        precision_scores = []
        recall_scores = []
        ap_scores = []
        mrr_scores = []
        ndcg_scores = []

        evaluated = 0

        for query in self.queries:

            if evaluated >= max_queries:
                break

            qid = str(
                query["id"]
            )

            if qid not in self.qrels:
                continue

            relevant = self.qrels[qid]

            if len(relevant) == 0:
                continue

            try:

                if model_name == "embedding":

                    results = retriever.search(
                        query["original_text"],
                        top_k=10
                    )

                elif model_name == "hybrid_sequential":

                    results = retriever.search(
                        processed_query=query[
                            "processed_text"
                        ],
                        original_query=query[
                            "original_text"
                        ],
                        top_k=10
                    )

                elif model_name == "hybrid_parallel":

                    results = retriever.search(
                        query["original_text"],
                        top_k=10
                    )

                elif model_name == "clustered_bm25":

                    results = retriever.search(
                        processed_query=query[
                            "processed_text"
                        ],
                        original_query=query[
                            "original_text"
                        ],
                        top_k=10
                    )

                elif model_name == "clustered_embedding":

                    results = retriever.search(
                        query["original_text"],
                        top_k=10
                    )

                elif model_name == "clustered_hybrid":

                    results = retriever.search(
                        query["original_text"],
                        top_k=10
                    )

                else:

                    results = retriever.search(
                        query["processed_text"],
                        top_k=10
                    )

            except Exception as e:

                print(
                    f"ERROR {model_name} QID={qid}"
                )

                print(e)

                continue

            retrieved = [

                str(
                    r["doc_id"]
                )

                for r in results
            ]

            precision_scores.append(

                precision_at_k(
                    retrieved,
                    relevant,
                    10
                )
            )

            recall_scores.append(

                recall_at_k(
                    retrieved,
                    relevant,
                    10
                )
            )

            ap_scores.append(

                average_precision(
                    retrieved,
                    relevant
                )
            )

            mrr_scores.append(

                reciprocal_rank(
                    retrieved,
                    relevant
                )
            )

            ndcg_scores.append(

                ndcg_at_k(
                    retrieved,
                    relevant,
                    10
                )
            )

            evaluated += 1

        if evaluated == 0:

            return {

                "Queries Evaluated": 0,

                "MAP": 0,

                "Precision@10": 0,

                "Recall@10": 0,

                "MRR": 0,

                "nDCG@10": 0
            }

        return {

            "Queries Evaluated":
                evaluated,

            "MAP":
                sum(ap_scores)
                / len(ap_scores),

            "Precision@10":
                sum(precision_scores)
                / len(precision_scores),

            "Recall@10":
                sum(recall_scores)
                / len(recall_scores),

            "MRR":
                sum(mrr_scores)
                / len(mrr_scores),

            "nDCG@10":
                sum(ndcg_scores)
                / len(ndcg_scores)
        }