import json
import csv
import pandas as pd
import requests

def load_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    return data

json_file = '.json'

data = load_json(json_file)

csv_file = 'financial_data.csv'

if 'CategoryId' in data:
    category_data = data['CategoryId']

    res = []

    for category in category_data:
        CATEGORY = category['id']
        COMPANY = ''
        
        for x in range(1, 5):
            url = "https://tools.morningstar.co.uk/api/rest.svc/klr5zyak8x/security/screener"

            querystring = {
                "page": f"{x}",
                "pageSize": "100",
                "sortOrder": "LegalName asc",
                "outputType": "json",
                "version": "1",
                "languageId": "es-ES",
                "currencyId": "EUR",
                "universeIds": "FOESP$$ALL",
                "securityDataPoints": "Name|TenforeId|ReturnM0|ReturnM12|ReturnM36|ReturnM60|ReturnM120|AlphaM36|BetaM36|StandardDeviationM36|SharpeM36|TrackRecordExtension",
                "filters": f"CategoryId:IN:{CATEGORY}"
            }

            payload = ""
            headers = {
                "cookie": "ASP.NET_SessionId=itqe4quqswvwi5weuuntd3re",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:102.0) Gecko/20100101 Firefox/102.0",
                "Accept": "application json, text/plain, */*",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate, br",
                "Origin": "https://www.morningstar.es",
                "DNT": "1",
                "Connection": "keep-alive",
                "Referer": "https://www.morningstar.es",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site"
            }

            r = requests.get(url, headers=headers, params=querystring)
            data = r.json()
            for p in data['rows']:
                res.append(p)

    funds_data = pd.json_normalize(res)
    funds_data.to_csv(csv_file)

    print(f"CSV file '{csv_file}' has been created.")
else:
    print("'CategoryId' key not found in the JSON data.")
