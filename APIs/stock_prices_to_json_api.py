import requests
import json
import pandas as pd
from tqdm import tqdm

data = pd.read_csv('/Users/seb/Desktop/stock ids.csv')

data_dict = {}

with tqdm(total=len(data)) as pbar:
    for sec_id in data['SecId']:

        url = "https://tools.morningstar.es/api/rest.svc/timeseries_ohlcv/2nhcdckzon"

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
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/119.0",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "en-GB,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://tools.morningstar.es/2nhcdckzon/interactivechart/htmlv2/default.aspx?ModuleId=59&embedded=true&overview=false&width=913&chartType=ITGrowthChart&plotType=growth&showLastPriceTickLabel=false&LanguageId=es-ES&SecurityTokenList=" + sec_id + "%5D3%5D0%5DE0WWE$$ALL",
            "__RequestVerificationToken": "i7UpE3pr2DXNgLJIyCSE9ChsY73s7jzOTHBPtWNM8rSNJLJo-mHAJhGzMHKiwmOg8juuMOSMdKVOmg8FHy8DRgeKSMrnUOY-Vpzl7yxOgZ01:IeJTgCJjpUmLoyD9DtVXWwGdbEm7V2YMhXSx4ngxBQ0lth9wkkNhvR39wHugLojAiDJO4h2PJJUfiML3j1vy3r2NymFc1748wlweakBL-IU1",
            "X-Requested-With": "XMLHttpRequest",
            "DNT": "1",
            "Connection": "keep-alive",
            "Cookie": "RT_es_LANG=es-ES; _ga_8R1W3TJHY4=GS1.1.1698412989.5.1.1698413016.0.0.0; _ga=GA1.1.1400416096.1698162032; ad-profile=%7B%22NeedRefresh%22%3Afalse%2C%22UserType%22%3A0%2C%22AudienceType%22%3A-1%2C%22PortofolioCreated%22%3A0%2C%22IsForObsr%22%3Afalse%2C%22NeedPopupAudienceBackfill%22%3Afalse%2C%22EnableInvestmentInUK%22%3A-1%7D; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Oct+27+2023+14%3A23%3A22+GMT%2B0100+(British+Summer+Time)&version=6.23.0&isIABGlobal=false&hosts=&consentId=40550431-9d10-47fa-ace7-7359dc45901e&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2C+C0003%3A0%2C+C0002%3A0%2C+C0004%3A0&geolocation=%3B&AwaitingReconsent=false; OptanonAlertBoxClosed=2023-10-24T15:40:35.391Z; ASP.NET_SessionId=zajmk5yc1hkp3ei5tat0jpla; __RequestVerificationToken=i7UpE3pr2DXNgLJIyCSE9ChsY73s7jzOTHBPtWNM8rSNJLJo-mHAJhGzMHKiwmOg8juuMOSMdKVOmg8FHy8DRgeKSMrnUOY-Vpzl7yxOgZ01; BackBtn1_997484697=goBackCount=1&backButtonLabel=esstockreport&backButtonLabelKey=esstockreport&backButtonUrl=https://tools.morningstar.es/es/stockreport/default.aspx?Site=es&id=" + sec_id + "&LanguageId=es-ES&SecurityToken=" + sec_id + "]3]0]E0WWE$$ALL&backButtonLabelLangId=es-ES; BackBtn1_=goBackCount=1&backButtonLabel=esstockreport&backButtonLabelKey=esstockreport&backButtonUrl=https://tools.morningstar.es/es/stockreport/default.aspx?tab=7&SecurityToken=" + sec_id + "]3]0]E0WWE$$ALL&Id=" + sec_id + "&ClientFund=0&CurrencyId=EUR&backButtonLabelLangId=es-ES",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "TE": "trailers"
        }

        response = requests.get(url, headers=headers, params=querystring)

        data_content = json.loads(response.text)

        data_dict[sec_id] = data_content

        pbar.update(1)

with open('NASDAQ_prices.json', 'w') as json_file:
    json.dump(data_dict, json_file)

