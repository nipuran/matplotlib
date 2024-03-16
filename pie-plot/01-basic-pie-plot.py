import matplotlib.pyplot as plt

# add style
plt.style.use('ggplot')

# data
slices = [22, 24, 29, 60]

labels = ['one', 'two', 'three', 'four']
explode = [0, 0, 0.1, 0]

# creating pie plot
plt.pie(slices, labels=labels, explode=explode, startangle=0, shadow=True, autopct='%1.1f%%', wedgeprops={'edgecolor':'black'})

# argument that are used above -
# labels
# explode
# startangle
# shadow
# autopct
# wedgeprops

plt.title('Pie Chart')

plt.tight_layout()

plt.show()
