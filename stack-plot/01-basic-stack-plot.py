import matplotlib.pyplot as plt

# datas
minutes = [1, 2, 3, 4, 5, 6]

# performance of player
player_1 = [1, 2, 3, 2, 4, 2]
player_2 = [2, 3, 2, 4, 2, 1]
player_3 = [1, 2, 3, 2, 1, 2]

# labels
labels = ['Player 1', 'Player 2', 'Player 3']

# creating stack plot
plt.stackplot(minutes, player_1, player_2, player_3, labels=labels)

plt.title('Stack Plot')

plt.legend()

plt.tight_layout()

plt.show()
