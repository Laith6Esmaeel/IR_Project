from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class TFIDFRetriever:
    def __init__(self):
        # نستخدم الكلمات المفتاحية للمشروع، وبما أننا قمنا بالتنظيف مسبقاً فلا داعي لـ stop_words هنا
        self.vectorizer = TfidfVectorizer()
        self.document_vectors = None
        self.documents = []

    def fit(self, processed_documents):
        """
        تجهيز الموديل وحساب الأوزان للوثائق.
        processed_documents: قائمة من القواميس تحتوي على id, processed_text, original_text
        """
        self.documents = processed_documents
        
        # استخراج النصوص المعالجة فقط لبناء الـ Vocabulary
        corpus = [doc["processed_text"] for doc in processed_documents]
        
        # تحويل النصوص إلى مصفوفة TF-IDF (Sparse Matrix)
        self.document_vectors = self.vectorizer.fit_transform(corpus)
        print(f" Successfully indexed {len(corpus)} documents.")

    def search(self, processed_query, top_k=5):
        """
        البحث باستخدام الاستعلام المعالج وحساب التشابه.
        """
        if self.document_vectors is None:
            raise ValueError("الموديل لم يتم تدريبه بعد! قم باستدعاء fit() أولاً أو تحميل موديل جاهز.")

        # 1. تحويل الـ Query إلى Vector بناءً على الـ Vocabulary الخاص بالموديل
        query_vector = self.vectorizer.transform([processed_query])

        # 2. حساب الـ Cosine Similarity بين الـ Query وجميع الوثائق
        # النتيجة تكون مصفوفة ثنائية الأبعاد، نستخدم flatten() لتحويلها لـ 1D Array
        similarities = cosine_similarity(query_vector, self.document_vectors).flatten()

        # 3. ترتيب الأندكسات تنازلياً بناءً على السكور (من الأعلى تشابهاً للأقل)
        # argsort تعطي الترتيب تصاعدياً، لذلك نستخدم [::-1] لقلبها، ثم نأخذ أول top_k نتائج
        ranked_indices = similarities.argsort()[::-1][:top_k]

        results = []
        for idx in ranked_indices:
            # لتجنب إرجاع وثائق ليس لها أي علاقة بالبحث (Score = 0)
            if similarities[idx] == 0:
                continue
                
            results.append({
                "doc_id": self.documents[idx]["id"],
                "score": float(similarities[idx]),
                "original_text": self.documents[idx].get("original_text", "No original text available"),
                "processed_text": self.documents[idx]["processed_text"]
            })

        return results