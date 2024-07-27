def average_score(scores: list[int]) -> float:
    return sum(scores) / len(scores)


def max_score(scores: list[int]) -> int:
    return max(scores)


def min_score(scores: list[int]) -> int:
    return min(scores)


def num_scores_above(scores: list[int], threshold: int) -> int:
    count = 0
    for i in range(len(scores)):
        if scores[i] >= threshold:
            count += 1
    return count


def median_score(scores: list[int]) -> float:
    # sort the scores
    scores.sort()
    # check if len(scores) is even or odd
    # [0, 1, 2] len 3
    if len(scores) % 2 == 0:  # if even
        index1 = int(len(scores) / 2)
        index2 = index1 - 1
        return (scores[index1] + scores[index2]) / 2
    else:  # if odd
        index = int((len(scores) - 1) / 2)
        return float(scores[index])


def standard_deviation(scores: list[int]) -> float:
    raise NotImplementedError


if __name__ == "__main__":  # This block of code will be executed when you run the file

    student_scores: list[int] = [90, 85, 70, 75, 80, 59, 80, 75, 90, 87, 93, 78, 80, 85, 100]

    print(f"Average score: {average_score(student_scores)}")
    print(f"Max score: {max_score(student_scores)}")
    print(f"Min score: {min_score(student_scores)}")
    print(f"Number of scores above 60: {num_scores_above(student_scores, 60)}")
    print(f"Median score: {median_score(student_scores)}")
    # print(f"Standard deviation: {standard_deviation(scores)}")
