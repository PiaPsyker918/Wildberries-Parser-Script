# Wildberries-Parser-Script
Скрипт, который парсит товары из Wildberries.

<img width="1291" height="324" alt="WBParserLogo" src="https://github.com/user-attachments/assets/3166033a-97fd-49f1-a038-047c59634ba1" />

Видео пример:

https://github.com/user-attachments/assets/2d612ec2-73cb-4c16-92c3-936088ef030c

```(Скрипт в раннем доступе, и в будущем будет дорабатываться. Если вы увидите баг напишите мне.)```

# Переводы

English: [English](https://github.com/PiaPsyker918/Wildberries-Parser-Script/tree/main)

# Требования 
```
requests
```

# Загрузка

1. Скачайте zip-файл.
2. Откройте CMD и впишите.
```pip install requests```
3. Следующий шаг в "Как использовать".

# Как использовать

В CMD впишите

Windows

```
.\parser.py
```

Linux

```
$ ./parser.py
```

# Опции

```Query``` - Какая категория должна быть запарсена.

```Currensy``` - Валюта для отображения.

```Language``` - Язык.

# Как это работает

Заголовки: User-Agent и Accept отправляются на сервер, и мы получаем веб-страницу и HTML-код в ответ от сервера

<img width="1482" height="583" alt="wbparser" src="https://github.com/user-attachments/assets/e95e2cc4-d6da-4bcb-90b8-92f991931ca7" />

У нас есть WB URL и PARAMS,

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
wildberries использует API для получения интересующей нас информации на странице. Давайте зайдем на сайт и откроем любую категорию. Давайте выберем Электронику -> Гарнитуры и наушники-вкладыши.
Теперь откройте инструмент разработчика, перейдите на вкладку сеть, чтобы просмотреть запросы, отправленные веб-сайтом, и выберите фильтр Fetch/XHR. Перезагрузите страницу.
```

Мы получили URL-адрес, и теперь проанализируем наиболее важные параметры

```"curr"``` - Currency, отвечающий за валюту, в которой будет отправлен ответ.

```"lang"``` - Язык, это важно для WB.

```"query"``` - Запрос, ЭТО ОЧЕНЬ ВАЖНО, запрос может быть как  ```"%D1%82%D0%B5%D0%BB%D0%B5%D1%84%D0%BE%D0%BD"``` или ```"Smartphone"```.


<img width="727" height="387" alt="image" src="https://github.com/user-attachments/assets/5004887c-aefa-4149-9805-04cd17fa5b2a" />

После получения HTML-кода мы берем JSON и извлекаем из него определенные блоки

```
product['name'] - Product Name.

product['sizes'][0]['price']['basic'] / 100 - Мы получаем цену, и поскольку она указана в центах, мы делим ее на 100, чтобы получить доллары или рубли.
```

# Contact

[<img width="100" height="100" alt="telegram-circle-icon-for-web-design-free-png" src="https://github.com/user-attachments/assets/1e4c0cb3-a856-417b-86d1-29354b2d92a8" />](https://t.me/Girlanda228)
