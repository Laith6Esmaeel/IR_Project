# import faiss
# import numpy as np

# embeddings = np.load(
#     "models/embedding/document_embeddings.npy"
# )

# dimension = embeddings.shape[1]

# index = faiss.IndexFlatIP(
#     dimension
# )

# index.add(
#     embeddings.astype("float32")
# )

# faiss.write_index(
#     index,
#     "models/embedding/faiss.index"
# )

# print("FAISS Index Saved")

import faiss
import numpy as np

# 📥 تحميل embeddings
embeddings = np.load("models/embedding/document_embeddings.npy").astype("float32")

dimension = embeddings.shape[1]

# 🔥 Index سريع للـ cosine similarity
index = faiss.IndexFlatIP(dimension)

# ➕ إضافة البيانات
index.add(embeddings)

# 💾 حفظ الفهرس
faiss.write_index(index, "models/embedding/faiss.index")

print("FAISS Index Saved")
print("Total vectors:", index.ntotal)