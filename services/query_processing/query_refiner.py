# from services.query_processing.query_expander import QueryExpander


# class QueryRefiner:

#     def __init__(self):

#         self.expander = QueryExpander()

#     def refine(self, query):

#         expanded = self.expander.expand(query)

#         return " ".join(expanded)


from services.query_processing.query_expander import (
    QueryExpander
)

from services.query_processing.spell_corrector import (
    SpellCorrector
)


class QueryRefiner:

    def __init__(self):

        self.corrector = SpellCorrector()

        self.expander = QueryExpander()

    def refine(
        self,
        query
    ):

        corrected = self.corrector.correct_query(
            query
        )

        expanded = self.expander.expand(
            corrected
        )

        return {

            "original_query":
                query,

            "corrected_query":
                corrected,

            "expanded_query":
                expanded
        }