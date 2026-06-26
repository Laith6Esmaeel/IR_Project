
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
# from services.indexing.index_loader import IndexLoader

# loader = IndexLoader()

# print("Vocabulary size:", len(loader.index))

# # تجربة term
# term = "covid"

# print("Postings:", loader.get_postings(term))
# print("DF:", loader.get_document_frequency(term))



# from services.query_processing.spell_corrector import SpellCorrector

# corrector = SpellCorrector()

# queries = [
#     "what",
#     "Approac",
#     "Avarage",
#     "deathe covid"
# ]

# for q in queries:
#     print("Original:", q)
#     print("Corrected:", corrector.correct_query(q))
#     print("-" * 40)




# from services.query_processing.query_suggester import QuerySuggester

# suggester = QuerySuggester()

# prefixes = ["Demo", "Coro", "Dis", "Hea"]

# for p in prefixes:
#     print(f"Prefix: {p}")
#     print(suggester.suggest(p))
#     print("-" * 40)


from services.query_processing.query_expander import QueryExpander

expander = QueryExpander()

query = "covid treatment"

expanded = expander.expand(query)

print("Original:", query)
print("Expanded:")
print(expanded)


# from services.query_processing.query_refiner import QueryRefiner

# refiner = QueryRefiner()

# query = "covid treatment"

# refined = refiner.refine(query)

# print("Refined Query:")
# print(refined)