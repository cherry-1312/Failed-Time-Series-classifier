import requests
import json
import pandas as pd
from tqdm import tqdm

data = pd.read_csv('your_data.csv')
data_dict = {}

with tqdm(total=len(data)) as pbar:
    for sec_id in data['SecId']:
        url = "https://api.example.com/endpoint"  
        querystring = {
            "currencyId": "EUR",
            "idtype": "Morningstar",
            "frequency": "daily",
            "startDate": "2013-10-01",
            "performanceType": "",
            "outputType": "COMPACTJSON",
            "id": sec_id + "]3]0]E0WWE$$ALL",
            "applyTrackRecordExtension": "true"
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://example.com",  
            "__RequestVerificationToken": "YOUR_TOKEN_HERE",  
            "X-Requested-With": "XMLHttpRequest",
            "DNT": "1",
            "Connection": "keep-alive",
            "Cookie": "YOUR_COOKIE_HERE",  
        }
        response = requests.get(url, headers=headers, params=querystring)
        data_content = json.loads(response.text)
        data_dict[sec_id] = data_content
        pbar.update(1)

with open('output_data.json', 'w') as json_file:
    json.dump(data_dict, json_file)
