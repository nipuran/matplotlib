# importing modules
from matplotlib import pyplot as plt
import numpy as np

# add style
plt.style.use('ggplot')

# datas
ages = [24, 25, 26, 27, 28]

# salaries of python developer
py_dev = np.array([23532, 40239, 45923, 40234, 23985])
plt.plot(ages, py_dev, marker='*', label='Python Developer')

# salaries of java developer 
java_dev = np.array([20334, 43723, 32085, 39275, 47307])
plt.plot(ages, java_dev, marker='*', label='Java Developer')

# salaries of rust developer
# rust_dev = [48273, 21424, 24324, 32750, 52833]
# plt.plot(ages, rust_dev, marker='*', label='Rust Developer')

plt.fill_between(ages, py_dev, java_dev, where=(py_dev>java_dev), interpolate=True, alpha=0.25)
plt.fill_between(ages, py_dev, java_dev, where=(py_dev<=java_dev), interpolate=True, alpha=0.25)

# labeling x and y axis
plt.xlabel('Ages')
plt.ylabel('Salaries')

# name of the plot
plt.title('Salaries by Ages')

# show the label of the line plots
plt.legend()

# add padding
plt.tight_layout()

# show the plot
plt.show()
