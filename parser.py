import requests

uquery, currensy, language = input("Query: "), input("Currensy (for example rub, usd): "), input("Language (for example ru, eng): ")

url = "https://search.wb.ru/exactmatch/ru/common/v18/search" 
params = {
    "ab_testing": False,
    "appType": 1,
    "curr": currensy,
    "dest": 12358496,
    "inheritFilters": False,
    "lang": language,
    "page": 1,
    "query": uquery,
    "resultset": "catalog",
    "sort": "popular",
    "spp": 30,
    "suppressSpellcheck": False
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(url, params=params, headers=headers)
if response.status_code == 200:
        data = response.json()
        for product in data['products']:
            print(product['name'])
            print(product['sizes'][0]['price']['basic'] / 100)
            
else:
    print(f"Error: {response.status_code}")

input("Enter to exit.....")