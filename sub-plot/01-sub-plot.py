import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data.csv')

# Age,All_Devs,Python,JavaScript

age = df['Age']
all_devs = df['All_Devs']
python = df['Python']
javascript = df['JavaScript']

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)

ax1.plot(age, python, label='Python')
ax1.plot(age, javascript, label='JavaScript')
ax2.plot(age, all_devs, linestyle='--', label='All Devs')

ax1.legend()
ax1.set_title('Salaries by Ages')
ax1.set_ylabel('Salaries')

ax2.legend()
ax2.set_ylabel('Salaries')
ax2.set_xlabel('Ages')

plt.tight_layout()
plt.show()
