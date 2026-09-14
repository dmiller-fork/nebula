import matplotlib.pyplot as plt
import numpy as np

methods = ["TF-IDF", "TF only", "IDF only"]

precision = [5.00, 5.00, 0.00]
recall = [100.00, 100.00, 0.00]

x = np.arange(2)
width = 0.25

fig, ax = plt.subplots()

ax.bar(x - width, [precision[0], recall[0]], width, label="TF-IDF")
ax.bar(x,         [precision[1], recall[1]], width, label="TF only")
ax.bar(x + width, [precision[2], recall[2]], width, label="IDF only")

ax.set_ylabel("Percentage (%)")
ax.set_title("Treasure Island Query: Precision and Recall")
ax.set_xticks(x)
ax.set_xticklabels(["Precision@20", "Recall@20"])
ax.set_ylim(0, 100)
ax.legend()

plt.tight_layout()
plt.show()
