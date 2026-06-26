from collections import defaultdict
from collections import Counter


class InvertedIndex:

    def __init__(self):

        self.index = defaultdict(dict)

    def build(
        self,
        documents
    ):

        total_docs = len(documents)

        for i, doc in enumerate(documents):

            if i % 1000 == 0:

                print(
                    f"Processing {i}/{total_docs}"
                )

            doc_id = str(
                doc["id"]
            )

            tokens = doc[
                "processed_text"
            ].split()

            frequencies = Counter(
                tokens
            )

            for term, tf in frequencies.items():

                self.index[
                    term
                ][doc_id] = tf

        return dict(
            self.index
        )