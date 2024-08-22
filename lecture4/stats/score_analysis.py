def highest(scores: dict[str, list]) -> str:
    """
    Return the highest scored student's name
    """
    max_score: int = max(scores["score"])
    max_score_index = 0
    for i in range(len(scores["score"])):
        if scores["score"][i] == max_score:
            max_score_index = i
    max_score_name = scores["name"][max_score_index]
    return max_score_name
