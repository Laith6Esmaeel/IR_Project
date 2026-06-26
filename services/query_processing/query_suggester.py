from collections import Counter
from services.indexing.index_loader import IndexLoader


class QuerySuggester:

    def __init__(self):

        self.loader = IndexLoader()

        self.index = self.loader.index

        # نحسب frequency لكل term
        self.term_frequency = self.build_term_frequency()

    # -----------------------------
    # حساب frequency من postings
    # -----------------------------
    def build_term_frequency(self):

        tf = Counter()

        for term, postings in self.index.items():

            tf[term] = sum(postings.values())

        return tf

    # -----------------------------
    # فلترة الكلمات السيئة
    # -----------------------------
    def is_valid_term(self, term):

        # لازم يكون حرفي أكثر من 2
        if len(term) < 3:
            return False

        # لازم يحتوي حرف (مش أرقام فقط)
        if not any(c.isalpha() for c in term):
            return False

        # استبعاد garbage مثل co1, cov2
        if sum(c.isdigit() for c in term) > len(term) / 2:
            return False

        return True

    # -----------------------------
    # suggestion
    # -----------------------------
    def suggest(self, prefix, top_k=10):

        prefix = prefix.lower()

        candidates = []

        for term in self.index.keys():

            if term.startswith(prefix) and self.is_valid_term(term):

                candidates.append(term)

        # ترتيب حسب frequency (الأهم!)
        candidates.sort(
            key=lambda x: self.term_frequency.get(x, 0),
            reverse=True
        )

        return candidates[:top_k]