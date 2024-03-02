import json
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ochl

with open('dir', 'r', encoding='utf-8') as file:
    data = json.load(file)

ohlc = []


for item in data:
    timestamp, open_price, high_price, low_price, close_price, volume = item
    ohlc.append([timestamp, open_price, high_price, low_price, close_price])

fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2) 

candlestick_ochl(ax, ohlc, width=0.6, colorup='g', colordown='r')

plt.xticks(rotation=45)
plt.title('Candlestick Chart')
plt.xlabel('Date')
plt.ylabel('Price')

plt.show()
