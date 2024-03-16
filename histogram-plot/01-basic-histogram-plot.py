import matplotlib.pyplot as plt

data = [1, 2, 3, 2, 3, 5, 5, 5, 6, 6, 7, 7, 7, 7, 8, 9, 9]
bins = [0, 3, 6, 9]

plt.hist(data, bins=bins, edgecolor='black')

plt.title('histogram plot')

plt.tight_layout()

plt.show()
