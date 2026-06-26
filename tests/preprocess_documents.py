# import json

# from services.preprocessing.preprocessing_service import PreprocessingService

# service = PreprocessingService()

# with open("datasets/raw/scifact/documents.json", "r", encoding="utf-8") as f:

#     documents = json.load(f)

# # فقط أول 100 document للتجربة
# documents = documents[:100]

# processed_documents = []

# for i, doc in enumerate(documents):

#     processed_text = service.preprocess(doc["text"])

#     processed_documents.append({

#         "id": doc["id"],
#         "original_text": doc["text"],
#         "processed_text": processed_text
#     })

#     print(f"Processed {i+1}")

# with open(
#     "datasets/processed/scifact/documents_processed.json",
#     "w",
#     encoding="utf-8"
# ) as f:

#     json.dump(processed_documents, f, indent=4)

# print("Documents preprocessing completed.")

import json
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
from services.preprocessing.preprocessing_service import (
    PreprocessingService
)

service = PreprocessingService()

INPUT_FILE = (
    "datasets/raw/trec_covid/documents.json"
)

OUTPUT_FILE = (
    "datasets/processed/trec_covid/documents_processed.json"
)

with open(
    INPUT_FILE,
    "r",
    encoding="utf-8"
) as f:

    documents = json.load(f)

processed_documents = []

total_docs = len(documents)

for i, doc in enumerate(documents):

    title = doc.get(
        "title",
        ""
    )

    text = doc.get(
        "text",
        ""
    )

    original_text = (
        title +
        " " +
        text
    ).strip()

    processed_text = service.preprocess(
        original_text
    )

    processed_documents.append({

        "id":
            doc["id"],

        "title":
            title,

        "original_text":
            original_text,

        "processed_text":
            processed_text
    })

    if (i + 1) % 1000 == 0:

        print(
            f"Processed {i+1}/{total_docs}"
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
        processed_documents,
        f,
        indent=4
    )

print(
    "Documents preprocessing completed."
)