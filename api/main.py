# from fastapi import FastAPI
# from pydantic import BaseModel

# import json

# from services.preprocessing.preprocessing_service import PreprocessingService
# from models.tfidf.tfidf_model import TFIDFRetriever

# app = FastAPI()

# # =========================
# # Load Documents
# # =========================

# with open(
#     "datasets/processed/scifact/documents_processed.json",
#     "r",
#     encoding="utf-8"
# ) as f:

#     documents = json.load(f)

# # =========================
# # Init Services
# # =========================

# preprocessor = PreprocessingService()

# retriever = TFIDFRetriever()

# retriever.fit(documents)

# # =========================
# # Request Model
# # =========================

# class SearchRequest(BaseModel):

#     query: str

#     top_k: int = 5

# # =========================
# # Search API
# # =========================

# @app.post("/search")

# def search(request: SearchRequest):

#     processed_query = preprocessor.preprocess(request.query)

#     results = retriever.search(
#         processed_query,
#         top_k=request.top_k
#     )

#     return {
#         "query": request.query,
#         "results": results
#     }


# ظ
# from fastapi import FastAPI
# from pydantic import BaseModel

# import json

# from services.preprocessing.preprocessing_service import PreprocessingService

# from models.tfidf.tfidf_model import TFIDFRetriever
# from models.bm25.bm25_model import BM25Retriever

# app = FastAPI()

# # =========================
# # Load Documents
# # =========================

# with open(
#     "datasets/processed/scifact/documents_processed.json",
#     "r",
#     encoding="utf-8"
# ) as f:

#     documents = json.load(f)

# # =========================
# # Init Services
# # =========================

# preprocessor = PreprocessingService()

# # TF-IDF Retriever
# tfidf_retriever = TFIDFRetriever()

# tfidf_retriever.fit(documents)

# # =========================
# # Request Model
# # =========================

# class SearchRequest(BaseModel):

#     query: str

#     top_k: int = 5

#     model: str = "tfidf"

#     # BM25 Parameters
#     k1: float = 1.5

#     b: float = 0.75

# # =========================
# # Search API
# # =========================

# @app.post("/search")

# def search(request: SearchRequest):

#     # preprocess query
#     processed_query = preprocessor.preprocess(
#         request.query
#     )

#     # =========================
#     # TF-IDF
#     # =========================

#     if request.model == "tfidf":

#         results = tfidf_retriever.search(
#             processed_query,
#             top_k=request.top_k
#         )

#     # =========================
#     # BM25
#     # =========================

#     elif request.model == "bm25":

#         bm25_retriever = BM25Retriever(
#             k1=request.k1,
#             b=request.b
#         )

#         bm25_retriever.fit(documents)

#         results = bm25_retriever.search(
#             processed_query,
#             top_k=request.top_k
#         )

#     # =========================
#     # Invalid Model
#     # =========================

#     else:

#         return {
#             "error": "Invalid model"
#         }

#     # =========================
#     # Response
#     # =========================

#     return {

#         "query": request.query,

#         "processed_query": processed_query,

#         "model": request.model,

#         "top_k": request.top_k,

#         "results": results
#     }




# tfidf,bm25,embedding
# from fastapi import FastAPI
# from pydantic import BaseModel

# import json

# from services.preprocessing.preprocessing_service import PreprocessingService

# from models.tfidf.tfidf_model import TFIDFRetriever
# from models.bm25.bm25_model import BM25Retriever
# from models.embedding.semantic_search import SemanticRetriever

# app = FastAPI()

# # =========================
# # Load Documents
# # =========================

# with open(
#     "datasets/processed/scifact/documents_processed.json",
#     "r",
#     encoding="utf-8"
# ) as f:

#     documents = json.load(f)

# # =========================
# # Init Services
# # =========================

# preprocessor = PreprocessingService()

# # =========================
# # TF-IDF Retriever
# # =========================

# tfidf_retriever = TFIDFRetriever()

# tfidf_retriever.fit(documents)

# # =========================
# # Semantic Retriever
# # =========================

# semantic_retriever = SemanticRetriever()



# # =========================
# # Request Model
# # =========================

# class SearchRequest(BaseModel):

#     query: str

#     top_k: int = 5

#     model: str = "tfidf"

#     # BM25 Parameters
#     k1: float = 1.5

#     b: float = 0.75

# # =========================
# # Search API
# # =========================

# @app.post("/search")
# def search(request: SearchRequest):

#     # preprocessing
#     processed_query = preprocessor.preprocess(
#         request.query
#     )

#     # =========================
#     # TF-IDF
#     # =========================

#     if request.model == "tfidf":

#         results = tfidf_retriever.search(
#             processed_query,
#             top_k=request.top_k
#         )

#     # =========================
#     # BM25
#     # =========================

#     elif request.model == "bm25":

#         bm25_retriever = BM25Retriever(
#             k1=request.k1,
#             b=request.b
#         )

#         bm25_retriever.fit(documents)

#         results = bm25_retriever.search(
#             processed_query,
#             top_k=request.top_k
#         )

#     # =========================
#     # Semantic Search
#     # =========================

#     elif request.model == "embedding":

#         results = semantic_retriever.search(
#             request.query,
#             top_k=request.top_k
#         )

#     # =========================
#     # Invalid Model
#     # =========================

#     else:

#         return {
#             "error": "Invalid model",
#             "available_models": [
#                 "tfidf",
#                 "bm25",
#                 "embedding"
#             ]
#         }

#     # =========================
#     # Response
#     # =========================

#     return {

#         "query": request.query,

#         "processed_query": processed_query,

#         "model": request.model,

#         "top_k": request.top_k,

#         "results": results
#     }






























































# بدون اضافات









# from fastapi import FastAPI
# from pydantic import BaseModel

# import json

# from services.preprocessing.preprocessing_service import PreprocessingService

# from models.tfidf.tfidf_model import TFIDFRetriever
# from models.bm25.bm25_model import BM25Retriever
# from models.embedding.semantic_search import SemanticRetriever

# from models.hybrid.sequential_hybrid import SequentialHybridRetriever
# from models.hybrid.parallel_hybrid import ParallelHybridRetriever

# app = FastAPI()

# # =========================
# # Load Documents
# # =========================

# with open(
#     "datasets/processed/trec_covid/documents_processed.json",
#     "r",
#     encoding="utf-8"
# ) as f:

#     documents = json.load(f)

# # =========================
# # Init Services
# # =========================

# preprocessor = PreprocessingService()

# # =========================
# # TF-IDF Retriever
# # =========================

# tfidf_retriever = TFIDFRetriever()
# tfidf_retriever.fit(documents)

# # =========================
# # BM25 Retriever
# # =========================

# bm25_retriever = BM25Retriever(
#     k1=1.5,
#     b=0.75
# )

# bm25_retriever.fit(documents)

# # =========================
# # Embedding Retriever
# # =========================

# semantic_retriever = SemanticRetriever()

# # =========================
# # Hybrid Retrievers
# # =========================

# sequential_hybrid = SequentialHybridRetriever(
#     bm25_retriever
# )

# parallel_hybrid = ParallelHybridRetriever(
#     bm25_retriever,
#     semantic_retriever
# )

# # =========================
# # Request Model
# # =========================

# class SearchRequest(BaseModel):

#     query: str

#     top_k: int = 5

#     model: str = "tfidf"

#     k1: float = 1.5

#     b: float = 0.75

#     alpha: float = 0.5

# # =========================
# # Search API
# # =========================

# @app.post("/search")
# def search(request: SearchRequest):

#     processed_query = preprocessor.preprocess(
#         request.query
#     )

#     # =========================
#     # TF-IDF
#     # =========================

#     if request.model == "tfidf":

#         results = tfidf_retriever.search(
#             processed_query,
#             top_k=request.top_k
#         )

#     # =========================
#     # BM25
#     # =========================

#     elif request.model == "bm25":

#         bm25_retriever.k1 = request.k1
#         bm25_retriever.b = request.b

#         results = bm25_retriever.search(
#             processed_query,
#             top_k=request.top_k
#         )

#     # =========================
#     # Embedding
#     # =========================

#     elif request.model == "embedding":

#         results = semantic_retriever.search(
#             request.query,
#             top_k=request.top_k
#         )

#     # =========================
#     # Hybrid Serial
#     # =========================

#     elif request.model == "hybrid_serial":

#        results = sequential_hybrid.search(
#     processed_query=processed_query,
#     original_query=request.query,
#     top_k=request.top_k
# )

#     # =========================
#     # Hybrid Parallel
#     # =========================

#     elif request.model == "hybrid_parallel":

#         results = parallel_hybrid.search(
#             request.query,
#             top_k=request.top_k,
#             alpha=request.alpha
#         )

#     # =========================
#     # Invalid Model
#     # =========================

#     else:

#         return {

#             "error": "Invalid model",

#             "available_models": [

#                 "tfidf",

#                 "bm25",

#                 "embedding",

#                 "hybrid_serial",

#                 "hybrid_parallel"
#             ]
#         }

#     # =========================
#     # Response
#     # =========================

#     return {

#         "query": request.query,

#         "processed_query": processed_query,

#         "model": request.model,

#         "top_k": request.top_k,

#         "results": results
#     }



























# مع اضافات


# from fastapi import FastAPI
# from pydantic import BaseModel

# import json

# # =========================
# # Services
# # =========================
# from services.preprocessing.preprocessing_service import PreprocessingService
# from services.query_processing.spell_corrector import SpellCorrector
# from services.query_processing.query_suggester import QuerySuggester

# # =========================
# # Models
# # =========================
# from models.tfidf.tfidf_model import TFIDFRetriever
# from models.bm25.bm25_model import BM25Retriever
# from models.embedding.semantic_search import SemanticRetriever

# from models.hybrid.sequential_hybrid import SequentialHybridRetriever
# from models.hybrid.parallel_hybrid import ParallelHybridRetriever


# app = FastAPI()

# # =========================
# # Load Documents
# # =========================
# with open(
#     "datasets/processed/trec_covid/documents_processed.json",
#     "r",
#     encoding="utf-8"
# ) as f:
#     documents = json.load(f)

# # =========================
# # Core Services
# # =========================
# preprocessor = PreprocessingService()
# spell_corrector = SpellCorrector()
# query_suggester = QuerySuggester()

# # =========================
# # Query Pipeline (NO EXPANSION)
# # =========================
# def process_query(query: str):

#     corrected = spell_corrector.correct_query(query)

#     processed = preprocessor.preprocess(corrected)

#     return corrected, processed


# # =========================
# # TF-IDF
# # =========================
# tfidf_retriever = TFIDFRetriever()
# tfidf_retriever.fit(documents)

# # =========================
# # BM25
# # =========================
# bm25_retriever = BM25Retriever(k1=1.5, b=0.75)
# bm25_retriever.fit(documents)

# # =========================
# # Embedding
# # =========================
# semantic_retriever = SemanticRetriever()

# # =========================
# # Hybrid
# # =========================
# sequential_hybrid = SequentialHybridRetriever(bm25_retriever)

# parallel_hybrid = ParallelHybridRetriever(
#     bm25_retriever,
#     semantic_retriever
# )

# # =========================
# # Request Model
# # =========================
# class SearchRequest(BaseModel):

#     query: str
#     top_k: int = 5
#     model: str = "tfidf"

#     k1: float = 1.5
#     b: float = 0.75
#     alpha: float = 0.5


# # =========================
# # SEARCH ENDPOINT
# # =========================
# @app.post("/search")
# def search(request: SearchRequest):

#     # 🔥 Query Processing (NO EXPANSION)
#     corrected_query, processed_query = process_query(request.query)

#     # =========================
#     # TF-IDF
#     # =========================
#     if request.model == "tfidf":

#         results = tfidf_retriever.search(
#             processed_query,
#             top_k=request.top_k
#         )

#     # =========================
#     # BM25
#     # =========================
#     elif request.model == "bm25":

#         bm25_retriever.k1 = request.k1
#         bm25_retriever.b = request.b

#         results = bm25_retriever.search(
#             processed_query,
#             top_k=request.top_k
#         )

#     # =========================
#     # EMBEDDING
#     # =========================
#     elif request.model == "embedding":

#         results = semantic_retriever.search(
#             corrected_query,
#             top_k=request.top_k
#         )

#     # =========================
#     # HYBRID SERIAL
#     # =========================
#     elif request.model == "hybrid_serial":

#         results = sequential_hybrid.search(
#             processed_query=processed_query,
#             original_query=request.query,
#             top_k=request.top_k
#         )

#     # =========================
#     # HYBRID PARALLEL (RRF / Fusion)
#     # =========================
#     elif request.model == "hybrid_parallel":

#         results = parallel_hybrid.search(
#             processed_query,
#             top_k=request.top_k,
#             alpha=request.alpha
#         )

#     # =========================
#     # INVALID MODEL
#     # =========================
#     else:

#         return {
#             "error": "Invalid model",
#             "available_models": [
#                 "tfidf",
#                 "bm25",
#                 "embedding",
#                 "hybrid_serial",
#                 "hybrid_parallel"
#             ]
#         }

#     # =========================
#     # RESPONSE
#     # =========================
#     return {
#         "query": request.query,
#         "corrected_query": corrected_query,
#         "processed_query": processed_query,
#         "model": request.model,
#         "top_k": request.top_k,
#         "results": results
#     }


# # =========================
# # SUGGEST API
# # =========================
# @app.get("/suggest")
# def suggest(prefix: str):

#     return {
#         "prefix": prefix,
#         "suggestions": query_suggester.suggest(prefix)
#     }


# # =========================
# # REFINE DEBUG API
# # =========================
# @app.get("/refine")
# def refine(query: str):

#     corrected, processed = process_query(query)

#     return {
#         "original_query": query,
#         "corrected_query": corrected,
#         "processed_query": processed
#     }












# from fastapi import FastAPI
# from pydantic import BaseModel

# import json

# # =========================
# # Services
# # =========================
# from services.preprocessing.preprocessing_service import PreprocessingService
# from services.query_processing.spell_corrector import SpellCorrector

# # =========================
# # Models
# # =========================
# from models.tfidf.tfidf_model import TFIDFRetriever
# from models.bm25.bm25_model import BM25Retriever
# from models.embedding.semantic_search import SemanticRetriever

# from models.hybrid.sequential_hybrid import SequentialHybridRetriever
# from models.hybrid.parallel_hybrid import ParallelHybridRetriever


# app = FastAPI()

# # =========================
# # Load Documents
# # =========================
# with open(
#     "datasets/processed/trec_covid/documents_processed.json",
#     "r",
#     encoding="utf-8"
# ) as f:
#     documents = json.load(f)

# # =========================
# # Services Init
# # =========================
# preprocessor = PreprocessingService()
# spell_corrector = SpellCorrector()

# # =========================
# # TF-IDF
# # =========================
# tfidf_retriever = TFIDFRetriever()
# tfidf_retriever.fit(documents)

# # =========================
# # BM25
# # =========================
# bm25_retriever = BM25Retriever(k1=1.5, b=0.75)
# bm25_retriever.fit(documents)

# # =========================
# # Embedding
# # =========================
# semantic_retriever = SemanticRetriever()

# # =========================
# # Hybrid
# # =========================
# sequential_hybrid = SequentialHybridRetriever(bm25_retriever)

# parallel_hybrid = ParallelHybridRetriever(
#     bm25_retriever,
#     semantic_retriever
# )

# # =========================
# # Request Model
# # =========================
# class SearchRequest(BaseModel):

#     query: str
#     top_k: int = 5
#     model: str = "tfidf"

#     k1: float = 1.5
#     b: float = 0.75
#     alpha: float = 0.5


# # =========================
# # SEARCH ENDPOINT
# # =========================
# @app.post("/search")
# def search(request: SearchRequest):

#     # =========================
#     # 1. SPELL CORRECTION
#     # =========================
#     corrected_query = spell_corrector.correct_query(request.query)

#     # =========================
#     # 2. PREPROCESSING
#     # =========================
#     processed_query = preprocessor.preprocess(corrected_query)

#     # =========================
#     # TF-IDF
#     # =========================
#     if request.model == "tfidf":

#         results = tfidf_retriever.search(
#             processed_query,
#             top_k=request.top_k
#         )

#     # =========================
#     # BM25
#     # =========================
#     elif request.model == "bm25":

#         bm25_retriever.k1 = request.k1
#         bm25_retriever.b = request.b

#         results = bm25_retriever.search(
#             processed_query,
#             top_k=request.top_k
#         )

#     # =========================
#     # EMBEDDING
#     # =========================
#     elif request.model == "embedding":

#         results = semantic_retriever.search(
#             corrected_query,
#             top_k=request.top_k
#         )

#     # =========================
#     # HYBRID SERIAL
#     # =========================
#     elif request.model == "hybrid_serial":

#         results = sequential_hybrid.search(
#             processed_query=processed_query,
#             original_query=request.query,
#             top_k=request.top_k
#         )

#     # =========================
#     # HYBRID PARALLEL
#     # =========================
#     elif request.model == "hybrid_parallel":

#         results = parallel_hybrid.search(
#             processed_query,
#             top_k=request.top_k,
#             alpha=request.alpha
#         )

#     # =========================
#     # INVALID MODEL
#     # =========================
#     else:

#         return {
#             "error": "Invalid model",
#             "available_models": [
#                 "tfidf",
#                 "bm25",
#                 "embedding",
#                 "hybrid_serial",
#                 "hybrid_parallel"
#             ]
#         }

#     # =========================
#     # RESPONSE
#     # =========================
#     return {
#         "query": request.query,
#         "corrected_query": corrected_query,
#         "processed_query": processed_query,
#         "model": request.model,
#         "top_k": request.top_k,
#         "results": results
#     }








# قبل النهائي شغال 100

# from fastapi import FastAPI
# from pydantic import BaseModel

# import json

# # =========================
# # Services
# # =========================
# from services.preprocessing.preprocessing_service import PreprocessingService
# from services.query_processing.spell_corrector import SpellCorrector
# from services.query_processing.query_suggester import QuerySuggester
# from services.query_processing.query_expander import QueryExpander
# # =========================
# # Models
# # =========================
# from models.tfidf.tfidf_model import TFIDFRetriever
# from models.bm25.bm25_model import BM25Retriever
# from models.embedding.semantic_search import SemanticRetriever

# from models.hybrid.sequential_hybrid import SequentialHybridRetriever
# from models.hybrid.parallel_hybrid import ParallelHybridRetriever


# app = FastAPI()

# # =========================
# # Load Documents
# # =========================
# with open(
#     "datasets/processed/trec_covid/documents_processed.json",
#     "r",
#     encoding="utf-8"
# ) as f:
#     documents = json.load(f)

# # =========================
# # Services Init
# # =========================
# preprocessor = PreprocessingService()
# spell_corrector = SpellCorrector()
# query_suggester = QuerySuggester()
# query_expander = QueryExpander()
# # =========================
# # TF-IDF
# # =========================
# tfidf_retriever = TFIDFRetriever()
# tfidf_retriever.fit(documents)

# # =========================
# # BM25
# # =========================
# bm25_retriever = BM25Retriever(k1=1.5, b=0.75)
# bm25_retriever.fit(documents)

# # =========================
# # Embedding
# # =========================
# semantic_retriever = SemanticRetriever()

# # =========================
# # Hybrid
# # =========================
# sequential_hybrid = SequentialHybridRetriever(bm25_retriever)

# parallel_hybrid = ParallelHybridRetriever(
#     bm25_retriever,
#     semantic_retriever
# )

# # =========================
# # Request Model
# # =========================
# class SearchRequest(BaseModel):

#     query: str
#     top_k: int = 5
#     model: str = "tfidf"

#     k1: float = 1.5
#     b: float = 0.75
#     alpha: float = 0.5


# # =========================
# # SEARCH PIPELINE
# # =========================
# @app.post("/search")
# def search(request: SearchRequest):

#     # 1. Spell Correction
#     corrected_query = spell_corrector.correct_query(request.query)

#     # 2. Preprocessing
#     processed_query = preprocessor.preprocess(corrected_query)

#     # =========================
#     # TF-IDF
#     # =========================
#     if request.model == "tfidf":

#         results = tfidf_retriever.search(
#             processed_query,
#             top_k=request.top_k
#         )

#     # =========================
#     # BM25
#     # =========================
#     elif request.model == "bm25":

#         bm25_retriever.k1 = request.k1
#         bm25_retriever.b = request.b

#         results = bm25_retriever.search(
#             processed_query,
#             top_k=request.top_k
#         )

#     # =========================
#     # EMBEDDING
#     # =========================
#     elif request.model == "embedding":

#         results = semantic_retriever.search(
#             corrected_query,
#             top_k=request.top_k
#         )

#     # =========================
#     # HYBRID SERIAL
#     # =========================
#     elif request.model == "hybrid_serial":

#         results = sequential_hybrid.search(
#             processed_query=processed_query,
#             original_query=request.query,
#             top_k=request.top_k
#         )

#     # =========================
#     # HYBRID PARALLEL
#     # =========================
#     elif request.model == "hybrid_parallel":

#         results = parallel_hybrid.search(
#             processed_query,
#             top_k=request.top_k,
#             alpha=request.alpha
#         )

#     else:

#         return {
#             "error": "Invalid model",
#             "available_models": [
#                 "tfidf",
#                 "bm25",
#                 "embedding",
#                 "hybrid_serial",
#                 "hybrid_parallel"
#             ]
#         }

#     return {
#         "query": request.query,
#         "corrected_query": corrected_query,
#         "processed_query": processed_query,
#         "model": request.model,
#         "top_k": request.top_k,
#         "results": results
#     }


# # =========================
# # 🔥 SUGGEST API
# # =========================
# @app.get("/suggest")
# def suggest(prefix: str):

#     suggestions = query_suggester.suggest(prefix)

#     return {
#         "prefix": prefix,
#         "suggestions": suggestions
#     }


# # =========================
# # 🔥 REFINE DEBUG API
# # =========================
# @app.get("/refine")
# def refine(query: str):

#     corrected_query = spell_corrector.correct_query(query)
#     processed_query = preprocessor.preprocess(corrected_query)

#     return {
#         "original_query": query,
#         "corrected_query": corrected_query,
#         "processed_query": processed_query
#     }



# @app.get("/expand")
# def expand(query: str):

#     expanded_terms = query_expander.expand(query)

#     return {
#         "original_query": query,
#         "expanded_terms": expanded_terms,
#         "expanded_query": " ".join(expanded_terms)
#     }



















from fastapi import FastAPI
from pydantic import BaseModel

import json
import numpy as np

from services.clustering.clustered_bm25 import (
    ClusteredBM25
)

from services.clustering.clustered_embedding import (
    ClusteredEmbeddingRetriever
)

from services.clustering.clustered_hybrid import (
    ClusteredHybridRetriever
)
from services.preprocessing.preprocessing_service import (
    PreprocessingService
)

from services.query_processing.spell_corrector import (
    SpellCorrector
)

from services.query_processing.query_expander import (
    QueryExpander
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
from services.query_processing.query_suggester import (
    QuerySuggester
)


# =====================================
# FastAPI
# =====================================

app = FastAPI(
    title="Hybrid IR System"
)

# =====================================
# Load Documents
# =====================================

with open(
    "datasets/processed/trec_covid/documents_processed.json",
    "r",
    encoding="utf-8"
) as f:

    documents = json.load(f)

# =====================================
# Services
# =====================================

preprocessor = PreprocessingService()

spell_corrector = SpellCorrector()

query_expander = QueryExpander()

query_suggester = QuerySuggester()

# =====================================
# TF-IDF
# =====================================

tfidf_retriever = TFIDFRetriever()

tfidf_retriever.fit(
    documents
)

# =====================================
# BM25
# =====================================

bm25_retriever = BM25Retriever(
    k1=1.5,
    b=0.75
)

bm25_retriever.fit(
    documents
)

# =====================================
# Embedding
# =====================================

semantic_retriever = SemanticRetriever()

# =====================================
# Load Embeddings
# =====================================

embeddings = np.load(
    "models/embedding/document_embeddings.npy"
)

# =====================================
# Hybrid Sequential
# =====================================

sequential_hybrid = SequentialHybridRetriever(
    bm25_retriever
)

# =====================================
# Hybrid Parallel
# =====================================

parallel_hybrid = ParallelHybridRetriever(
    bm25_retriever,
    semantic_retriever
)

# =====================================
# Clustered BM25
# =====================================

clustered_bm25 = ClusteredBM25(
    bm25_retriever,
    documents
)

# =====================================
# Clustered Embedding
# =====================================

clustered_embedding = (
    ClusteredEmbeddingRetriever(
        documents,
        embeddings
    )
)

# =====================================
# Clustered Hybrid
# =====================================

clustered_hybrid = (
    ClusteredHybridRetriever(
        bm25_retriever,
        documents,
        embeddings
    )
)

# =====================================
# Request Model
# =====================================
class SuggestRequest(
    BaseModel
):

    query: str

    limit: int = 10 

class QueryRequest(BaseModel):

    query: str

class SearchRequest(BaseModel):

    query: str

    model: str = "tfidf"

    top_k: int = 10

    # BM25

    k1: float = 1.5

    b: float = 0.75

    # Hybrid Parallel

    alpha: float = 0.5

    # Features

    use_spell_correction: bool = True

    use_query_expansion: bool = False

# =====================================
# Search Endpoint
# =====================================

@app.post("/search")
def search(request: SearchRequest):

    original_query = request.query

    corrected_query = original_query

    # =====================================
    # Spell Correction
    # =====================================

    if request.use_spell_correction:

        corrected_query = (
            spell_corrector.correct_query(
                original_query
            )
        )

    expanded_query = corrected_query

    # =====================================
    # Query Expansion
    # =====================================

    if request.use_query_expansion:

        expanded_query = (
            query_expander.expand(
                corrected_query
            )
        )

    processed_query = (
        preprocessor.preprocess(
            expanded_query
        )
    )

    # =====================================
    # TF-IDF
    # =====================================

    if request.model == "tfidf":

        results = tfidf_retriever.search(
            processed_query,
            top_k=request.top_k
        )

    # =====================================
    # BM25
    # =====================================

    elif request.model == "bm25":

        bm25_retriever.k1 = request.k1

        bm25_retriever.b = request.b

        results = bm25_retriever.search(
            processed_query,
            top_k=request.top_k
        )

    # =====================================
    # Embedding
    # =====================================

    elif request.model == "embedding":

        results = semantic_retriever.search(
            expanded_query,
            top_k=request.top_k
        )

    # =====================================
    # Hybrid Sequential
    # =====================================

    elif request.model == "hybrid_serial":

        bm25_retriever.k1 = request.k1

        bm25_retriever.b = request.b

        results = sequential_hybrid.search(
            processed_query=processed_query,
            original_query=expanded_query,
            top_k=request.top_k
        )

    # =====================================
    # Hybrid Parallel
    # =====================================

    elif request.model == "hybrid_parallel":

        bm25_retriever.k1 = request.k1

        bm25_retriever.b = request.b

        results = parallel_hybrid.search(
            expanded_query,
            top_k=request.top_k,
            alpha=request.alpha
        )

    # =====================================
    # Clustered BM25
    # =====================================

    elif request.model == "clustered_bm25":

        bm25_retriever.k1 = request.k1

        bm25_retriever.b = request.b

        results = clustered_bm25.search(
            processed_query=processed_query,
            original_query=expanded_query,
            top_k=request.top_k
        )

    # =====================================
    # Clustered Embedding
    # =====================================

    elif request.model == "clustered_embedding":

        results = clustered_embedding.search(
            expanded_query,
            top_k=request.top_k
        )

    # =====================================
    # Clustered Hybrid
    # =====================================

    elif request.model == "clustered_hybrid":

        bm25_retriever.k1 = request.k1

        bm25_retriever.b = request.b

        results = clustered_hybrid.search(
            expanded_query,
            top_k=request.top_k,
            alpha=request.alpha
        )

    # =====================================
    # Invalid Model
    # =====================================

    else:

        return {

            "error": "Invalid model",

            "available_models": [

                "tfidf",

                "bm25",

                "embedding",

                "hybrid_serial",

                "hybrid_parallel",
                "clustered_bm25",

                "clustered_embedding",

                "clustered_hybrid"
            ]
        }

    return {

        "original_query": original_query,

        "corrected_query": corrected_query,

        "expanded_query": expanded_query,

        "processed_query": processed_query,

        "model": request.model,

        "top_k": request.top_k,

        "k1": request.k1,

        "b": request.b,

        "alpha": request.alpha,

        "results": results
    }

# =====================================
# Models Endpoint
# =====================================
@app.post("/suggest")
def suggest_query(
    request: SuggestRequest
):

    suggestions = (
        query_suggester.suggest(
            request.query,
            request.limit
        )
    )

    return {

        "prefix":
            request.query,

        "suggestions":
            suggestions
    }


@app.post("/refine")
def refine_query(
    request: QueryRequest
):

    corrected = (
        spell_corrector.correct_query(
            request.query
        )
    )

    expanded = (
        query_expander.expand(
            corrected
        )
    )

    processed = (
        preprocessor.preprocess(
            expanded
        )
    )

    return {

        "original_query":
            request.query,

        "corrected_query":
            corrected,

        "expanded_query":
            expanded,

        "processed_query":
            processed
    }






@app.get("/models")
def get_models():

    return [

        "tfidf",

        "bm25",

        "embedding",

        "hybrid_serial",

        "hybrid_parallel",
        
        "clustered_bm25",

        "clustered_embedding",

        "clustered_hybrid"
    ]

# =====================================
# Evaluation Endpoint
# =====================================

@app.post("/evaluate")
def evaluate():

    with open(
        "reports/evaluation_results.json",
        "r",
        encoding="utf-8"
    ) as f:

        results = json.load(f)

    return results


@app.post("/run-evaluation")
def run_evaluation():

    import subprocess

    subprocess.run(
        ["python",
         "services/evaluation/compare_models.py"]
    )

    with open(
        "reports/evaluation_results.json",
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)

# =====================================
# Health Check
# =====================================

@app.get("/")
def root():

    return {

        "message":
        "Hybrid Information Retrieval System",

        "models": [

            "tfidf",

            "bm25",

            "embedding",

            "hybrid_serial",

            "hybrid_parallel",
            "clustered_bm25",

            "clustered_embedding",

            "clustered_hybrid"
        ]
    }