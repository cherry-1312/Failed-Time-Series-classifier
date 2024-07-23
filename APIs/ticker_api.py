import requests
import json

url = "https://api.example.com/endpoint"  # Replace with placeholder

querystring = {
    "currencyId": "EUR",
    "idtype": "Morningstar",
    "frequency": "daily",
    "startDate": "1970-01-01",
    "performanceType": "",
    "outputType": "COMPACTJSON",
    "id": "PLACEHOLDER_ID",  # Replace with placeholder
    "applyTrackRecordExtension": "true"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://www.example.com",  # Replace with placeholder
    "X-Requested-With": "XMLHttpRequest",
    "DNT": "1",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
}

response = requests.get(url, headers=headers, params=querystring)
data_content = response.json()

with open('stock_prices.json', 'w') as json_file:
    json.dump(data_content, json_file)

print(response.text)
