import requests
import csv
import pandas as pd

csv_file = 'NYSE_Stocks.csv'
res = []

url = "https://tools.morningstar.co.uk/api/rest.svc/2nhcdckzon/security/screener"
total_iterations = 2

for x in range(0, total_iterations + 1):
    querystring = {
        "page":"1",
        "pageSize":"1000",
        "sortOrder":"Name asc",
        "outputType":"json",
        "version":"1",
        "languageId":"en-ENG",
        "currencyId":"USD",
        "universeIds":"E0EXG$XNYS",  #E0WWE$$ALL, E0EXG$XNYS, E0EXG$XNAS
        "securityDataPoints":"SecId|LegalName|Name|IndustryName|SectorName|Ticker|ClosePrice|MarketCap|TenforeId|Universe|ExchangeId",
        #|StarRatingM255|QuantitativeStarRating|DividendYield|PERatio|PEGRatio|MarketCountryName|EquityStyleBox|ReturnD1|ReturnW1|ReturnM1|ReturnM3|ReturnM6|ReturnM0|ReturnM12|ReturnM36|ReturnM60|ReturnM120|EBTMarginYear1|ROEYear1|ROICYear1|EPSGrowth3YYear1|RevenueGrowth3Y|DebtEquityRatio|NetMargin|ROATTM|ROETTM",
        "filters":"",
        "term":"",
        "subUniverseId":""
        }

    payload = ""
    headers = {
        "cookie": "ASP.NET_SessionId=qyhxas2pyyqlk5ppahjkydvu",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/119.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-GB,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Origin": "https://www.morningstar.es",
        "DNT": "1",
        "Connection": "keep-alive",
        "Referer": "https://www.morningstar.es/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site"
    }

    r = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    data = r.json()
    for p in data['rows']:
        res.append(p)
    progress = (x / total_iterations) * 100
    print(f"Progress: {progress:.2f}%")
    
funds_data = pd.json_normalize(res)
funds_data.to_csv(csv_file)
