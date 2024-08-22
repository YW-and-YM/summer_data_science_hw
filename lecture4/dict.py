import pandas as pd

student_scores = {
    "name": ["Alice", "Bob", "Cindy"],
    "score": [90, 80, 100],
}

print(sum(student_scores["score"]) / len(student_scores["score"]))

data = pd.DataFrame(student_scores)
print(data["score"].mean())
