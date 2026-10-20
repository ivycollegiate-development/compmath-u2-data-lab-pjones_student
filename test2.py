    import csv
    import matplotlib
    import matplotlib.pyplot as plt

    hours, scores = [], []
    with open(“data/u2_dataset1_study_habits.csv“) as f:
        for row in csv.DictReader(f):
            hours.append(float(row[“Study_Hours“]))
            scores.append(float(row[“Test_Score“]))

    plt.figure(figsize=(7,5))
    plt.scatter(hours, scores, s=15, color=“steelblue“, label=“Study vs Score“)
    plt.title(“Test Score vs. Study Hours (52 Students)“)
    plt.xlabel(“Weekly Study Hours (hrs)“)
    plt.ylabel(“Test Score (points)“)
    plt.grid(True, alpha=0.4)
    plt.legend()
    plt.tight_layout()
    plt.savefig(“review_scatter_p2_v1.png“, dpi=150)
    plt.show()
