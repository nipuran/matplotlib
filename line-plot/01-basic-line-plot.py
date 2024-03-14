# importing module
from matplotlib import pyplot as plt

# datas
ages = [24, 25, 26, 27, 28]
salaries = [28743, 53723, 40325, 43278, 50842]

# creating the plot
plt.plot(ages, salaries)

# labeling x and y axis
plt.xlabel('Ages')
plt.ylabel('Salaries')

# name of the plot
plt.title('Ages by Salaries')

# show the plot
plt.show()
