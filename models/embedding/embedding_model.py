# from sentence_transformers import SentenceTransformer

# class EmbeddingModel:

#     def __init__(self):

#         self.model = SentenceTransformer(
#             "BAAI/bge-small-en-v1.5"
#         )

#     def encode(self, texts):

#         return self.model.encode(
#             texts,
#             show_progress_bar=True,
#             normalize_embeddings=True
#         )
    

from sentence_transformers import SentenceTransformer
import os

class EmbeddingModel:

    def __init__(self):

        os.environ["TOKENIZERS_PARALLELISM"] = "false"

        self.device = "cpu"
        print("Using device:", self.device)

        # 🔥 أسرع موديل للـ CPU
        self.model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2",
            device=self.device
        )

    def encode(self, texts):

        return self.model.encode(
            texts,
            batch_size=128,              # 🔥 تسريع مهم جداً
            show_progress_bar=True,
            normalize_embeddings=True,
            convert_to_numpy=True
        )
    