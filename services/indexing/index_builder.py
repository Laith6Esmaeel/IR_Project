import json
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../../.."
        )
    )
)

from services.indexing.inverted_index import (
    InvertedIndex
)

with open(
    "datasets/processed/trec_covid/queries_processed.json",
    "r",
    encoding="utf8"
) as f:

    documents = json.load(f)

indexer = InvertedIndex()

index = indexer.build(
    documents
)

os.makedirs(
    "services/indexing",
    exist_ok=True
)

with open(
    "services/indexing/index.json",
    "w",
    encoding="utf8"
) as f:

    json.dump(
        index,
        f
    )

print(
    f"\nIndexed Terms: {len(index)}"
)