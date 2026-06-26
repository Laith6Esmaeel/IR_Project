import json
import pandas as pd
import matplotlib.pyplot as plt


with open(
    "reports/evaluation_results.json",
    "r",
    encoding="utf-8"
) as f:

    results = json.load(f)

df = pd.DataFrame(results)

df.to_csv(
    "reports/evaluation.csv",
    index=False
)

metrics = [

    "MAP",

    "Precision@10",

    "Recall@10",

    "MRR",

    "nDCG@10"
]

for metric in metrics:

    plt.figure(figsize=(8, 5))

    plt.bar(
        df["Model"],
        df[metric]
    )

    plt.title(metric)

    plt.ylabel(metric)

    plt.xticks(rotation=20)

    plt.tight_layout()

    plt.savefig(
        f"reports/{metric}.png"
    )

    plt.close()

print("Reports generated successfully.")