# import re
# from difflib import SequenceMatcher
# from services.indexing.index_loader import IndexLoader


# class SpellCorrector:

#     def __init__(self):

#         self.loader = IndexLoader()
#         self.vocabulary = set(self.loader.index.keys())

#     # -----------------------------
#     # similarity function
#     # -----------------------------
#     def similarity(self, a, b):

#         return SequenceMatcher(None, a, b).ratio()

#     # -----------------------------
#     # best match finder
#     # -----------------------------
#     def get_best_match(self, word):

#         best_word = word
#         best_score = 0.0

#         for vocab_word in self.vocabulary:

#             score = self.similarity(word, vocab_word)

#             if score > best_score:
#                 best_score = score
#                 best_word = vocab_word

#         # threshold dynamic
#         if best_score >= 0.75:
#             return best_word

#         return word

#     # -----------------------------
#     # correct single word
#     # -----------------------------
#     def correct_word(self, word):

#         word = word.lower().strip()

#         if word in self.vocabulary:
#             return word

#         return self.get_best_match(word)

#     # -----------------------------
#     # correct full query
#     # -----------------------------
#     def correct_query(self, query):

#         words = re.findall(r"\w+", query.lower())

#         corrected = [
#             self.correct_word(w)
#             for w in words
#         ]

#         return " ".join(corrected)

import re
from difflib import SequenceMatcher
from services.indexing.index_loader import IndexLoader


class SpellCorrector:

    def __init__(self):

        self.loader = IndexLoader()

        # تنظيف vocabulary بشكل صحيح
        self.vocabulary = self.clean_vocab(
            self.loader.index.keys()
        )

    # -------------------------
    # تنظيف الكلمات
    # -------------------------
    def clean_word(self, word):

        return re.sub(r"[^a-z0-9]", "", word.lower())

    def clean_vocab(self, vocab):

        return set(
            self.clean_word(w)
            for w in vocab
        )

    # -------------------------
    # similarity
    # -------------------------
    def similarity(self, a, b):

        return SequenceMatcher(None, a, b).ratio()

    # -------------------------
    # best match
    # -------------------------
    def correct_word(self, word):

        word = self.clean_word(word)

        if not word:
            return word

        if word in self.vocabulary:
            return word

        best_match = word
        best_score = 0.0

        for vocab_word in self.vocabulary:

            score = self.similarity(word, vocab_word)

            if score > best_score:
                best_score = score
                best_match = vocab_word

        # lower threshold (مهم جداً)
        if best_score >= 0.70:
            return best_match

        return word

    # -------------------------
    # full query
    # -------------------------
    def correct_query(self, query):

        words = query.split()

        corrected = [
            self.correct_word(w)
            for w in words
        ]

        return " ".join(corrected)