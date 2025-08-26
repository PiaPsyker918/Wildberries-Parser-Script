# Wildberries-Parser-Script
A script that parses products from Wildberries.

<img width="1291" height="324" alt="WBParserLogo" src="https://github.com/user-attachments/assets/3166033a-97fd-49f1-a038-047c59634ba1" />

Video preview:

https://github.com/user-attachments/assets/2d612ec2-73cb-4c16-92c3-936088ef030c

```(The script is currently in early access, and it will be integrated into the Telegram bot and other applications in the future. If you see a bug please text me.)```

# Translations

Russian: [Russian](https://github.com/PiaPsyker918/Wildberries-Parser-Script/russian)

# Requirements 
```
requests
```

# Installation

1. Install the zip-file.
2. Open CMD and write.
```pip install requests```
3. Next step in "How to use".

# How to use

In CMD write 

Windows

```
.\parser.py
```

Linux

```
$ ./parser.py
```

# Options

```Query``` - What needs to be parsed.

```Currensy``` - The currency for displaying prices.

```Language``` - Language.

# How it works

Headers: User-Agent and Accept are sent to the server, and we receive Web-Page and HTML in response from the server

<img width="1482" height="583" alt="wbparser" src="https://github.com/user-attachments/assets/e95e2cc4-d6da-4bcb-90b8-92f991931ca7" />

We have our WB URL and PARAMS,

```
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
```
```
wildberries uses an API to get the information we're interested in on the page. Let's go to the website and open any category. Let's choose Electronics -> Headsets and Earbuds.
Now, open the developer tool, switch to the network tab to view the requests sent by the website, and select the Fetch/XHR filter. Reload the page.
```

We have received the URL, and now we will analyze the most important parameters

```"curr"``` - Currensy, responsible for the currency in which the response will be sent.

```"lang"``` - Language, this is important for WB.

```"query"``` - Query, THIS IS VERY IMPORTANT, the request can be like ```"%D1%82%D0%B5%D0%BB%D0%B5%D1%84%D0%BE%D0%BD"``` and like ```"Smartphone"```.


<img width="727" height="387" alt="image" src="https://github.com/user-attachments/assets/5004887c-aefa-4149-9805-04cd17fa5b2a" />

After receiving the HTML, we take the JSON and extract specific blocks from it

```
product['name'] - Product Name.

product['sizes'][0]['price']['basic'] / 100 - We get the price, and since it's displayed in cents, we divide it by 100 to get dollars or ruble.
```

# Contact

[<img width="100" height="100" alt="telegram-circle-icon-for-web-design-free-png" src="https://github.com/user-attachments/assets/1e4c0cb3-a856-417b-86d1-29354b2d92a8" />](https://t.me/Girlanda228)
