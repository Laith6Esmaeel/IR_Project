from services.indexing.index_loader import (
    IndexLoader
)

loader = IndexLoader()

term = "covid"

print(
    "\nPOSTINGS\n"
)

print(
    loader.get_postings(term)
)

print(
    "\nDOCUMENT FREQUENCY\n"
)

print(
    loader.get_document_frequency(term)
)