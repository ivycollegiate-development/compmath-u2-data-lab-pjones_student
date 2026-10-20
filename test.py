import csv
import matplotlib.pyplot as plt

hours, scores = [], []
with open("data/u2_dataset1_study_habits.csv") as f:
    for rows in csv.DictReader(f):
        hours.append(float(rows["Study_Hours"]))
        scores.append(float(rows["Test_Score"]))

plt.figure(figsize=(7,5))
plt.scatter(hours, scores, s=15, color="steelblue", label="Study vs Score")
plt.title("Test Score vs. Study Hours (52 Students)")
plt.xlabel("Weekly Study Hours (hrs)")
plt.ylabel("Test Score (points)")
plt.grid(True)
plt.tight_layout()
plt.savefig("review_scatter_v01.png", dpi=150)
plt.show()
