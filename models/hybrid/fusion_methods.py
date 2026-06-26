def min_max_normalize(scores):

    if not scores:
        return {}

    values = list(scores.values())

    min_score = min(values)
    max_score = max(values)

    if max_score == min_score:

        return {
            k: 1.0
            for k in scores
        }

    return {

        k: (
            v - min_score
        ) / (
            max_score - min_score
        )

        for k, v in scores.items()
    }


def weighted_sum(
    bm25_score,
    embedding_score,
    alpha=0.5
):

    return (

        alpha * bm25_score

        +

        (1 - alpha) * embedding_score

    )