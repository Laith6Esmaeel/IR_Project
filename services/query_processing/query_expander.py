# import nltk

# nltk.download("wordnet")


# from nltk.corpus import wordnet


# class QueryExpander:

#     def expand(self, query):

#         expanded = set()

#         words = query.split()

#         for word in words:

#             expanded.add(word)

#             for syn in wordnet.synsets(word):

#                 for lemma in syn.lemmas():

#                     expanded.add(
#                         lemma.name().replace("_", " ")
#                     )

#         return list(expanded)

from nltk.corpus import wordnet


class QueryExpander:

    def __init__(self):

        pass

    def expand(
        self,
        query,
        max_synonyms=2
    ):

        expanded = []

        words = query.split()

        for word in words:

            expanded.append(word)

            synonyms = set()

            for syn in wordnet.synsets(word):

                for lemma in syn.lemmas():

                    synonym = lemma.name().replace(
                        "_",
                        " "
                    )

                    if synonym.lower() != word:

                        synonyms.add(
                            synonym
                        )

            expanded.extend(
                list(synonyms)[
                    :max_synonyms
                ]
            )

        return " ".join(expanded)