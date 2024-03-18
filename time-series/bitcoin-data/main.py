import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mpl_date

plt.style.use('ggplot')

df = pd.read_csv('data.csv')

date = pd.to_datetime(df['Date'])
close = df['Close']

plt.plot_date(date, close, linestyle='solid')

plt.gcf().autofmt_xdate()

date_format = mpl_date.DateFormatter('%d %b, %Y')

plt.gca().xaxis.set_major_formatter(date_format)

plt.title('Bitcoin prices')
plt.xlabel('Dates')
plt.ylabel('Closing Prices')

plt.tight_layout()
plt.show()
