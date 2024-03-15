# importing modules
import matplotlib.pyplot as plt
import numpy as np

# datas
ages = [24, 25, 26, 27, 28]

ages_indexes = np.arange(5)

width=0.25

# python developer salaries
py_dev = np.random.randint(20000, 50000, size=5)
plt.bar(ages_indexes-width, py_dev, width=width, label='Python developer')

# java developer salaries
java_dev = np.random.randint(20000, 50000, size=5)
plt.bar(ages_indexes, java_dev, width=width, label='Java developer')

# rust developer salaries
rust_dev = np.random.randint(20000, 50000, size=5)
plt.bar(ages_indexes+width, rust_dev, width=width, label='Rust developer')

# name of the plot
plt.title('Salaries by Ages')

# labeling x and y axis
plt.xlabel('Ages')
plt.ylabel('Salaries')

# show the bar labels
plt.legend()

# labeling x axis indexes
plt.xticks(ticks=ages_indexes, labels=ages)

# add padding
plt.tight_layout()

# show the plot
plt.show()
