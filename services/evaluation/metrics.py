import math


def precision_at_k(retrieved, relevant, k=10):

    retrieved = retrieved[:k]

    if k == 0:
        return 0.0

    hits = sum(
        1
        for doc_id in retrieved
        if str(doc_id) in relevant
    )

    return hits / k


def recall_at_k(retrieved, relevant, k=10):

    retrieved = retrieved[:k]

    if len(relevant) == 0:
        return 0.0

    hits = sum(
        1
        for doc_id in retrieved
        if str(doc_id) in relevant
    )

    return hits / len(relevant)


def average_precision(retrieved, relevant):

    score = 0.0
    hits = 0

    for rank, doc_id in enumerate(
        retrieved,
        start=1
    ):

        if str(doc_id) in relevant:

            hits += 1

            score += hits / rank

    if hits == 0:
        return 0.0

    return score / hits


def reciprocal_rank(retrieved, relevant):

    for rank, doc_id in enumerate(
        retrieved,
        start=1
    ):

        if str(doc_id) in relevant:

            return 1 / rank

    return 0.0


def dcg(relevances):

    score = 0.0

    for rank, rel in enumerate(
        relevances,
        start=1
    ):

        score += rel / math.log2(rank + 1)

    return score


def ndcg_at_k(retrieved, relevant, k=10):

    retrieved = retrieved[:k]

    rels = []

    for doc_id in retrieved:

        if str(doc_id) in relevant:
            rels.append(1)
        else:
            rels.append(0)

    dcg_score = dcg(rels)

    ideal = sorted(
        rels,
        reverse=True
    )

    idcg = dcg(ideal)

    if idcg == 0:
        return 0.0

    return dcg_score / idcg