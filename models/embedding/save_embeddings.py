# import json
# import numpy as np

# from embedding_model import EmbeddingModel

# model = EmbeddingModel()

# with open(
#     "datasets/processed/trec_covid/documents_processed.json",
#     "r",
#     encoding="utf-8"
# ) as f:

#     documents = json.load(f)

# texts = [
#     doc["original_text"]
#     for doc in documents
# ]

# embeddings = model.encode(texts)

# np.save(
#     "models/embedding/document_embeddings.npy",
#     embeddings
# )

# print(embeddings.shape)



import json
import numpy as np
from embedding_model import EmbeddingModel

model = EmbeddingModel()

# 📂 تحميل البيانات
with open(
    "datasets/processed/trec_covid/documents_processed.json",
    "r",
    encoding="utf-8"
) as f:
    documents = json.load(f)

texts = [doc["original_text"] for doc in documents]

print(f"Loaded {len(texts)} documents")

# ⚡ تقسيم البيانات (مهم للسرعة والاستقرار)
batch_size = 500
embeddings_list = []

for i in range(0, len(texts), batch_size):

    batch = texts[i:i + batch_size]
    print(f"Processing batch {i} → {i + len(batch)}")

    emb = model.encode(batch)
    embeddings_list.append(emb)

# 🔥 دمج النتائج
embeddings = np.vstack(embeddings_list).astype("float32")

# 💾 حفظ
np.save("models/embedding/document_embeddings.npy", embeddings)

print("Done!")
print("Shape:", embeddings.shape)