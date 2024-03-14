# importing module
from matplotlib import pyplot as plt

# datas
ages = [24, 25, 26, 27, 28]
salaries = [50238, 82784, 48325, 49281, 20130]

# creating the plot
plt.plot(ages, salaries)

# labeling x and y axis
plt.xlabel('Ages')
plt.ylabel('Salaries')

# name of the plot
plt.title('Salaries by Ages')

# show the plot
plt.show()
