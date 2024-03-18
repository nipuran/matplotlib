import matplotlib.pyplot as plt
import numpy as np

n=20

# array of n elements with random values from 1 to 9
x = np.random.randint(1, 9, size=n)
y = np.random.randint(1, 9, size=n)

colors = np.random.randint(1, 9, size=n)
sizes = np.random.randint(200, 600, size=n)

plt.scatter(x, y, s=sizes, c=colors, cmap='plasma', edgecolor='black', linewidth=1, alpha=0.7)
# arguments ----
# s for size
# c for color
# marker for marker
# both c and s has array of numbers which correspond each data points and
# change the color shade and size of the data points
# cmap change the color of the shades

# color bar
plt.colorbar().set_label('Satisfactions')

plt.show()
