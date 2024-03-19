import matplotlib.pyplot as plt
import pandas as pd
from itertools import count
from matplotlib.animation import FuncAnimation

def animate(i):
    data = pd.read_csv('data.csv')

    x_values = data['x_values']
    total_1 = data['total_1']
    total_2 = data['total_2']

    plt.cla()
    plt.plot(x_values, total_1, label='channel 1')
    plt.plot(x_values, total_2, label='channel 2')
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval=1000, cache_frame_data=False)
plt.show()


