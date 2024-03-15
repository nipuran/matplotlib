# importing module
import matplotlib.pyplot as plt

# add style
plt.style.use('ggplot')

# datas based on 2011 census of India
city = ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Ahmedabad']
population = [12442373, 11034555, 8443675, 6993262, 5577940]

# creating bar plot
plt.bar(city, population)

# labeling x and y axis
plt.xlabel('City')
plt.ylabel('Population')

# name of the plot
plt.title('Population by City')

# add padding
plt.tight_layout()

# show the plot
plt.show()
