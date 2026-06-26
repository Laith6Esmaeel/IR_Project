import os
import sys
import pickle
from services.preprocessing.preprocessing_service import PreprocessingService
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
def load_system():
    """تحميل الموديل وخدمة معالجة النصوص"""
    MODEL_PATH = "models/tfidf/tfidf_model.pkl"
    
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError("❌ ملف الموديل غير موجود! تأكد من تشغيل ملف التدريب (search_engine.py) أولاً لإنشاء ملف .pkl")
        
    print("⏳ Loading Preprocessor and Saved TF-IDF Model...")
    preprocessor = PreprocessingService()
    
    with open(MODEL_PATH, "rb") as f:
        retriever = pickle.load(f)
        
    return preprocessor, retriever

def run_automated_tests():
    try:
        preprocessor, retriever = load_system()
    except Exception as e:
        print(e)
        return

    print("\n" + "="*50)
    print("🧪 STARTING AUTOMATED RETRIEVAL TESTS")
    print("="*50)

    # -----------------------------------------------------------------
    # Test 1 & 2: فحص معالجة الاستعلام (Query Preprocessing) ومنطقية النتائج
    # -----------------------------------------------------------------
    print("\n▶️ [Test 1 & 2] Checking Preprocessing & Result Relevancy...")
    # استعلام يحتوي كلمات توقف وصيغ جمع/تصريف
    raw_query = "The blocking of cancer treatments and cells" 
    processed_query = preprocessor.preprocess(raw_query)
    
    print(f"   Raw Query: '{raw_query}'")
    print(f"   Processed Query: '{processed_query}'") # المتوقع رؤية كلمات مثل (cancer, treatment, cell) بدون the, of, and
    
    results = retriever.search(processed_query, top_k=3)
    
    if results:
        print(f"   ✅ Success! Found {len(results)} relevant documents.")
        print(f"   Top Result ID: {results[0]['doc_id']} with Score: {results[0]['score']:.4f}")
    else:
        print("   ❌ Fail: No results returned. Check if corpus matches query terms.")

    # -----------------------------------------------------------------
    # Test 3: فحص تحجيم النتائج (top_k Control)
    # -----------------------------------------------------------------
    print("\n▶️ [Test 3] Checking top_k constraints...")
    for k in [1, 3, 5]:
        res = retriever.search(processed_query, top_k=k)
        print(f"   Requested top_k={k} -> Returned results count: {len(res)}")
        if len(res) != k and len(retriever.documents) >= k:
            print(f"   ❌ Fail: Expected exactly {k} results.")
        else:
            print(f"   ✅ Success: top_k parameter obeyed.")

    # -----------------------------------------------------------------
    # Test 4: فحص الترتيب التنازلي للـ Scores (Sorting Check)
    # -----------------------------------------------------------------
    print("\n▶️ [Test 4] Checking if scores are sorted descending...")
    many_results = retriever.search(processed_query, top_k=5)
    scores = [r['score'] for r in many_results]
    
    # التأكد من أن كل سكور أكبر أو يساوي السكور الذي يليه
    is_sorted = all(scores[i] >= scores[i+1] for i in range(len(scores)-1))
    if is_sorted:
        print(f"   ✅ Success! Scores are strictly sorted: {scores}")
    else:
        print(f"   ❌ Fail: Scores are not sorted properly: {scores}")

    # -----------------------------------------------------------------
    # Test 5: فحص تأثير الكلمات النادرة (TF-IDF Weighting)
    # -----------------------------------------------------------------
    print("\n▶️ [Test 5] Checking Rare Words Impact (IDF)...")
    # كلمة شائعة جداً في المجال الطبي (مثل effect أو study) + كلمة دقيقة جداً ونادرة (مثل اسم جين أو مرض نادر)
    # لنفرض أن "cancer" شائعة و "mutations" أقل شيوعاً
    rare_query = preprocessor.preprocess("cancer mutations")
    rare_results = retriever.search(rare_query, top_k=3)
    
    print("   Top matched snippets for rare query:")
    for i, r in enumerate(rare_results):
        print(f"   #{i+1} [Score: {r['score']:.4f}]: {r['original_text'][:120]}...")

    print("\n" + "="*50)
    print("🎉 ALL TESTS COMPLETED")
    print("="*50)

if __name__ == "__main__":
    run_automated_tests()