import os
import json
import pickle
import sys
from models.tfidf.tfidf_model import TFIDFRetriever
from services.preprocessing.preprocessing_service import PreprocessingService
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

def main():
    # المسارات (تعديلها حسب هيكلية مشروعك)
    DATASET_PATH = "datasets/processed/trec_covid/documents_processed.json"
    MODEL_SAVE_PATH = "models/tfidf/tfidf_model.pkl"
    
    # 1. تحميل الوثائق المعالجة مسبقاً
    print("⏳ Loading processed documents...")
    if not os.path.exists(DATASET_PATH):
        print(f"❌ Error: Raw data not found at {DATASET_PATH}. Please run preprocessing first.")
        return
        
    with open(DATASET_PATH, "r", encoding="utf-8") as f:
        documents = json.load(f)
    
    # 2. بناء وتدريب الـ TF-IDF Retriever
    retriever = TFIDFRetriever()
    print("⏳ Training TF-IDF Model...")
    retriever.fit(documents)
    
    # 3. حفظ الموديل لاستخدامه لاحقاً دون إعادة تدريب
    print("⏳ Saving model to disk...")
    os.makedirs(os.path.dirname(MODEL_SAVE_PATH), exist_ok=True)
    with open(MODEL_SAVE_PATH, "wb") as f:
        pickle.dump(retriever, f)
    print(f"🎉 Model saved successfully at {MODEL_SAVE_PATH}")
    
    # --- تجربة النظام (Simulation) ---
    print("\n" + "="*40)
    print("🚀 Testing Search Engine")
    print("="*40)
    
    # تهيئة خدمة معالجة النصوص للاستعلام
    preprocessor = PreprocessingService() 
    
    # raw_query = "What are the latest cancer treatments?"
    raw_query = "what is the origin of COVID-19"
    print(f"👤 User Query: '{raw_query}'")
    
    # خطوة جوهرية: معالجة الـ Query بنفس طريقة الوثائق
    processed_query = preprocessor.preprocess(raw_query)
    print(f"⚙️ Processed Query: '{processed_query}'")
    
    # تنفيذ البحث
    top_k = 3
    results = retriever.search(processed_query, top_k=top_k)
    
    # عرض النتائج
    print(f"\n🎯 Top {top_k} Results Found:")
    if not results:
        print("⚠️ No matching documents found.")
    else:
        for rank, res in enumerate(results, start=1):
            print(f"\n[Rank #{rank}] | Doc ID: {res['doc_id']} | Similarity Score: {res['score']:.4f}")
            print(f"📄 Text: {res['original_text'][:200]}...") 


if __name__ == "__main__":
    main()