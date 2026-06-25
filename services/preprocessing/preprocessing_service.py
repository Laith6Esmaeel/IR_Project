# import re
# import spacy
# import json
# # تحميل model مرة واحدة فقط
# nlp = spacy.load("en_core_web_sm")


# class PreprocessingService:

#     def __init__(self):

#         pass

#     def clean_text(self, text):

#         # lowercase
#         text = text.lower()

#         # remove special characters
#         text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)

#         # remove extra spaces
#         text = re.sub(r'\s+', ' ', text).strip()

#         return text

#     def tokenize_and_lemmatize(self, text):

#         doc = nlp(text)

#         tokens = []

#         for token in doc:

#             # skip stopwords
#             if token.is_stop:
#                 continue

#             # skip punctuation
#             if token.is_punct:
#                 continue

#             lemma = token.lemma_.strip()

#             if lemma:
#                 tokens.append(lemma)

#         return tokens

#     def preprocess(self, text):

#         cleaned_text = self.clean_text(text)

#         tokens = self.tokenize_and_lemmatize(cleaned_text)

#         processed_text = " ".join(tokens)

#         return processed_text
    





import json
import re
import spacy
import os
nlp = spacy.load(
    "en_core_web_sm",
    disable=["parser", "ner"]
)


class PreprocessingService:

    def __init__(self):
        pass

    def clean_text(self, text):

        if text is None:
            return ""

        text = text.lower()

        text = re.sub(
            r"[^a-zA-Z0-9\s]",
            " ",
            text
        )

        text = re.sub(
            r"\s+",
            " ",
            text
        ).strip()

        return text

    def tokenize_and_lemmatize(
        self,
        text
    ):

        doc = nlp(text)

        tokens = []

        for token in doc:

            if token.is_stop:
                continue

            if token.is_punct:
                continue

            if token.is_space:
                continue

            lemma = token.lemma_.strip()

            if lemma:
                tokens.append(lemma)

        return tokens

    def preprocess(
        self,
        text
    ):

        cleaned_text = self.clean_text(
            text
        )

        tokens = self.tokenize_and_lemmatize(
            cleaned_text
        )

        return " ".join(tokens)




