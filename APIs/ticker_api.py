import requests
import json

url = "https://tools.morningstar.es/api/rest.svc/timeseries_ohlcv/2nhcdckzon"

querystring = {"currencyId":"EUR","idtype":"Morningstar","frequency":"daily","startDate":"1970-01-01","performanceType":"","outputType":"COMPACTJSON","id":"0P000000GY]3]0]E0WWE$$ALL","applyTrackRecordExtension":"true"}

payload = ""
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://tools.morningstar.es/2nhcdckzon/interactivechart/htmlv2/default.aspx?ModuleId=59&embedded=true&overview=false&width=913&chartType=ITGrowthChart&plotType=growth&showLastPriceTickLabel=false&LanguageId=es-ES&SecurityTokenList=0P000000GY%5D3%5D0%5DE0WWE%24%24ALL",
    "__RequestVerificationToken": "ZwrjVIm6nG_X9eVw7nXcGyBF53iLmATaRpU_F0zzalqvOlxp2L_lcpjPUUJLW8vBITAS8q5N7CnzW-HPE5Ju1xjKg8SEyQgu8QBq4BW0OZw1:LFM5j_0DgQxWxGyhHDmippCUTJKf-N3MdGuP1SzuDCnD8L_l8mXGMbsPZi_NgnbzfJDgiFtzfbfFKZdj9srlytHAel-6YeSVZLguxz27xyY1",
    "X-Requested-With": "XMLHttpRequest",
    "DNT": "1",
    "Connection": "keep-alive",
    "Cookie": "RT_es_LANG=es-ES; ASP.NET_SessionId=darxqqb4hi2c45iovu2hi0ll; __RequestVerificationToken=ZwrjVIm6nG_X9eVw7nXcGyBF53iLmATaRpU_F0zzalqvOlxp2L_lcpjPUUJLW8vBITAS8q5N7CnzW-HPE5Ju1xjKg8SEyQgu8QBq4BW0OZw1; BackBtn1_997484697=goBackCount=1&backButtonLabel=esstockreport&backButtonLabelKey=esstockreport&backButtonUrl=https://tools.morningstar.es/es/stockreport/default.aspx?Site=es&id=0P000000GY&LanguageId=es-ES&SecurityToken=0P000000GY]3]0]E0WWE$$ALL&backButtonLabelLangId=es-ES; BackBtn1_=goBackCount=1&backButtonLabel=esstockreport&backButtonLabelKey=esstockreport&backButtonUrl=https://tools.morningstar.es/es/stockreport/default.aspx?tab=7&SecurityToken=0P000000GY]3]0]E0WWE$$ALL&Id=0P000000GY&ClientFund=0&CurrencyId=EUR&backButtonLabelLangId=es-ES",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "TE": "trailers"
}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

data_content = json.loads(response.text)

with open('AAPL_prices.json', 'w') as json_file:
    json.dump(data_content, json_file)

print(response.text)

#The chunk below creates a candlestick chart using the json data:

if response.status_code == 200:
 data = json.loads(response.text)

 ohlc = []

 for item in data:
     timestamp, open_price, high_price, low_price, close_price, volume = item
     ohlc.append([timestamp, open_price, high_price, low_price, close_price])


 fig, ax = plt.subplots()
 fig.subplots_adjust(bottom=0.2)  

 candlestick_ochl(ax, ohlc, width=0.6, colorup='g', colordown='r')

 ax.xaxis.set_major_locator(MaxNLocator(nbins=6))
 plt.xticks(rotation=45)
 ax.xaxis_date() 
 plt.title('Candlestick Chart')
 plt.xlabel('Date')
 plt.ylabel('Price')

 plt.show()
else:
print("Request failed with status code:", response.status_code)

