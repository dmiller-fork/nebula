import matplotlib.pyplot as plt

sizes = [3, 30, 1000]

heap = [0.000014, 0.000020, 0.000085]
sort = [0.000008, 0.000010, 0.000124]

x = range(len(sizes))
width = 0.35

plt.bar([i - width/2 for i in x], heap, width, label="Heap")
plt.bar([i + width/2 for i in x], sort, width, label="Sort")

plt.xticks(x, sizes)
plt.xlabel("Data size")
plt.ylabel("Time (s)")
plt.title("Heap vs. Sort Performance")
plt.legend()
plt.tight_layout()
plt.show()
