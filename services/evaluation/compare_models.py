# import json

# from services.evaluation.evaluator import (
#     Evaluator
# )

# from models.tfidf.tfidf_model import (
#     TFIDFRetriever
# )

# from models.bm25.bm25_model import (
#     BM25Retriever
# )

# from models.embedding.semantic_search import (
#     SemanticRetriever
# )

# from models.hybrid.sequential_hybrid import (
#     SequentialHybridRetriever
# )

# from models.hybrid.parallel_hybrid import (
#     ParallelHybridRetriever
# )


# with open(
#     "datasets/processed/trec_covid/documents_processed.json",
#     "r",
#     encoding="utf-8"
# ) as f:

#     documents = json.load(f)

# print("Loading retrievers...")

# tfidf = TFIDFRetriever()
# tfidf.fit(documents)

# bm25 = BM25Retriever()
# bm25.fit(documents)

# embedding = SemanticRetriever()

# hybrid_seq = SequentialHybridRetriever(
#     bm25
# )

# hybrid_parallel = ParallelHybridRetriever(
#     bm25,
#     embedding
# )

# evaluator = Evaluator(
#     "datasets/processed/trec_covid/queries_processed.json",
#     "datasets/raw/trec_covid/qrels.json"
# )

# results = []

# models = [

#     ("TF-IDF", tfidf, "tfidf"),

#     ("BM25", bm25, "bm25"),

#     ("Embedding", embedding, "embedding"),

#     ("Hybrid Sequential",
#      hybrid_seq,
#      "hybrid_sequential"),

#     ("Hybrid Parallel",
#      hybrid_parallel,
#      "hybrid_parallel")
# ]

# for name, retriever, mode in models:

#     print(f"\nEvaluating {name}")

#     metrics = evaluator.evaluate_model(
#         retriever,
#         mode,
#         max_queries=50
#     )

#     metrics["Model"] = name

#     results.append(metrics)

#     print(metrics)

# with open(
#     "reports/evaluation_results.json",
#     "w",
#     encoding="utf-8"
# ) as f:

#     json.dump(
#         results,
#         f,
#         indent=4
#     )

# print(
#     "\nSaved reports/evaluation_results.json"
# )



import json
import numpy as np

from services.evaluation.evaluator import (
    Evaluator
)

from models.tfidf.tfidf_model import (
    TFIDFRetriever
)

from models.bm25.bm25_model import (
    BM25Retriever
)

from models.embedding.semantic_search import (
    SemanticRetriever
)

from models.hybrid.sequential_hybrid import (
    SequentialHybridRetriever
)

from models.hybrid.parallel_hybrid import (
    ParallelHybridRetriever
)

from services.clustering.clustered_bm25 import (
    ClusteredBM25
)

from services.clustering.clustered_embedding import (
    ClusteredEmbeddingRetriever
)

from services.clustering.clustered_hybrid import (
    ClusteredHybridRetriever
)

with open(
    "datasets/processed/trec_covid/documents_processed.json",
    "r",
    encoding="utf-8"
) as f:

    documents = json.load(f)

print(
    "Loading retrievers..."
)

tfidf = TFIDFRetriever()
tfidf.fit(documents)

bm25 = BM25Retriever()
bm25.fit(documents)

embedding = SemanticRetriever()

hybrid_seq = (
    SequentialHybridRetriever(
        bm25
    )
)

hybrid_parallel = (
    ParallelHybridRetriever(
        bm25,
        embedding
    )
)

print(
    "Loading embeddings..."
)

embeddings = np.load(
    "models/embedding/document_embeddings.npy"
)

clustered_bm25 = (
    ClusteredBM25(
        bm25,
        documents
    )
)

clustered_embedding = (
    ClusteredEmbeddingRetriever(
        documents,
        embeddings
    )
)

clustered_hybrid = (
    ClusteredHybridRetriever(
        bm25,
        documents,
        embeddings
    )
)

evaluator = Evaluator(
    "datasets/processed/trec_covid/queries_processed.json",
    "datasets/raw/trec_covid/qrels.json"
)

results = []

models = [

    (
        "TF-IDF",
        tfidf,
        "tfidf"
    ),

    (
        "BM25",
        bm25,
        "bm25"
    ),

    (
        "Embedding",
        embedding,
        "embedding"
    ),

    (
        "Hybrid Sequential",
        hybrid_seq,
        "hybrid_sequential"
    ),

    (
        "Hybrid Parallel",
        hybrid_parallel,
        "hybrid_parallel"
    ),

    (
        "Clustered BM25",
        clustered_bm25,
        "clustered_bm25"
    ),

    (
        "Clustered Embedding",
        clustered_embedding,
        "clustered_embedding"
    ),

    (
        "Clustered Hybrid",
        clustered_hybrid,
        "clustered_hybrid"
    )
]

for name, retriever, mode in models:

    print(
        f"\nEvaluating {name}"
    )

    metrics = (
        evaluator.evaluate_model(
            retriever,
            mode,
            max_queries=50
        )
    )

    metrics["Model"] = name

    results.append(
        metrics
    )

    print(metrics)

with open(
    "reports/evaluation_results.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        results,
        f,
        indent=4
    )

print(
    "\nSaved reports/evaluation_results.json"
)