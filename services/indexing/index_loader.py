import json


class IndexLoader:

    def __init__(self, path="services/indexing/index.json"):

        self.path = path

        with open(self.path, "r", encoding="utf8") as f:
            self.index = json.load(f)

    def get_postings(self, term):

        # postings: {doc_id: tf}
        return self.index.get(term, {})

    def get_document_frequency(self, term):

        postings = self.get_postings(term)
        return len(postings)

    def get_term_frequency(self, term, doc_id):

        postings = self.get_postings(term)
        return postings.get(str(doc_id), 0)