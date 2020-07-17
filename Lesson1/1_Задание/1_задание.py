"""
Посмотреть документацию к API GitHub, разобраться как
вывести список репозиториев для конкретного пользователя,
сохранить JSON-вывод в файле *.json.
"""

import requests
import json
main_link = 'https://api.github.com'
user='Ashipkov'
response = requests.get(f'{main_link}/users/{user}/repos')
with open('data.json', 'w') as f:
    json.dump(response.json(), f)
for i in response.json():
    print(i['name'])

"""
Пользовтель AShipkov - это я
Для проверки взел данные нескольких пользователей и проверил 
Скрины в PDF
"""