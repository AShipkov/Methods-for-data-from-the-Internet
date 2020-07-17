"""
Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа).
Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл.
Для работы выбра API Наса
Ввожу даты, получаю количество астероидов вблизи орбиты земли
+ Доп информация в response.jsoon
"""

import requests
import json
API_KEY='0bDSGclMNHH56nn6zdOUp98kybn5FSW7jfEoazEF'
START_DATE ='2020-07-23'
END_DATE = '2020-07-23'# Дата окончания должна быть не далее 7 дней
response = requests.get(f'https://api.nasa.gov/neo/rest/v1/feed?start_date={START_DATE}&end_date={END_DATE}&api_key={API_KEY}')
with open('response.json', 'w') as f:
    json.dump(response.json(), f)
data = response.json()
print(f'Количесво астероидов с {START_DATE} по {END_DATE} пролетающих вблизи орбиты Земли -- {data["element_count"]}')
