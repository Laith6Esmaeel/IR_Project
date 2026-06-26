# import json

# from services.preprocessing.preprocessing_service import PreprocessingService

# service = PreprocessingService()

# with open("datasets/raw/scifact/queries.json", "r", encoding="utf-8") as f:

#     queries = json.load(f)

# # # فقط أول 100 query للتجربة
# # queries = queries[:100]

# processed_queries = []

# for i, query in enumerate(queries):

#     processed_text = service.preprocess(query["text"])

#     processed_queries.append({

#         "id": query["id"],

#         "original_text": query["text"],

#         "processed_text": processed_text
#     })

#     print(f"Processed Query {i+1}")

# with open(
#     "datasets/processed/scifact/queries_processed.json",
#     "w",
#     encoding="utf-8"
# ) as f:

#     json.dump(processed_queries, f, indent=4)

# print("Queries preprocessing completed.")



import json
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
from services.preprocessing.preprocessing_service import (
    PreprocessingService
)

service = PreprocessingService()

INPUT_FILE = (
    "datasets/raw/trec_covid/queries.json"
)

OUTPUT_FILE = (
    "datasets/processed/trec_covid/queries_processed.json"
)

with open(
    INPUT_FILE,
    "r",
    encoding="utf-8"
) as f:

    queries = json.load(f)

processed_queries = []

for i, query in enumerate(queries):

    processed_text = service.preprocess(
        query["text"]
    )

    processed_queries.append({

        "id":
            query["id"],

        "original_text":
            query["text"],

        "processed_text":
            processed_text
    })

    print(
        f"Processed Query {i+1}"
    )

os.makedirs(
    "datasets/processed/trec_covid",
    exist_ok=True
)

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        processed_queries,
        f,
        indent=4
    )

print(
    "Queries preprocessing completed."
)