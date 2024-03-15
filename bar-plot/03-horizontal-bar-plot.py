import matplotlib.pyplot as plt
import numpy as np

# city names
city = ['Delhi', 'Mumbai', 'Kolkata', 'Bangalore']

city_indexes = np.arange(4)

width=0.2

# vageterian population
veg = np.random.randint(20000, 50000, size=4)
plt.barh(city_indexes, veg, width, color='g', label='Vegetarian')


# non vegeterian population
non_veg = np.random.randint(20000, 50000, size=4)
plt.barh(city_indexes+width, non_veg, width, color='r', label='Non Vegetarian')

plt.title('Vegetarian and Non-Vegetarian Demographic')
plt.ylabel('Cities')
plt.xlabel('Population')

plt.yticks(ticks=city_indexes, labels=city)

plt.legend()
plt.tight_layout()
plt.show()
