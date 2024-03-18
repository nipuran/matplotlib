import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('2019-05-31-data.csv')
view_count = df['view_count']
likes = df['likes']
ratio = df['ratio']

# creating a scatter plot
plt.scatter(view_count, likes, c=ratio, cmap='viridis', edgecolor='black', linewidth=1, alpha=0.7)

# create a color bar
cbar = plt.colorbar()
# labeling the color bar
cbar.set_label('Like/Dislike Ratio')

# change the scale into log
plt.xscale('log')
plt.yscale('log')

plt.xlabel('View Count')
plt.ylabel('Likes')
plt.title('Trending Youtube Videos')

plt.tight_layout()
plt.show()


