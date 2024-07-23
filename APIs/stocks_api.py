import requests
import csv
import pandas as pd

csv_file = 'Stock_Data.csv'
res = []
url = "https://api.example.com/endpoint"  # Replace with placeholder

total_iterations = 2
for x in range(0, total_iterations + 1):
    querystring = {
        "page": "1",
        "pageSize": "1000",
        "sortOrder": "Name asc",
        "outputType": "json",
        "version": "1",
        "languageId": "en-ENG",
        "currencyId": "USD",
        "universeIds": "PLACEHOLDER",  # Replace with placeholder
        "securityDataPoints": "SecId|LegalName|Name|IndustryName|SectorName|Ticker|ClosePrice|MarketCap|TenforeId|Universe|ExchangeId",
        "filters": "",
        "term": "",
        "subUniverseId": ""
    }
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Origin": "https://www.example.com",  # Replace with placeholder
        "DNT": "1",
        "Connection": "keep-alive",
        "Referer": "https://www.example.com/",  # Replace with placeholder
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site"
    }
    
    r = requests.get(url, headers=headers, params=querystring)
    data = r.json()
    for p in data['rows']:
        res.append(p)
    
    progress = (x / total_iterations) * 100
    print(f"Progress: {progress:.2f}%")

funds_data = pd.json_normalize(res)
funds_data.to_csv(csv_file)
