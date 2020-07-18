"""
Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа).
Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл.
Для работы выбра API Наса
Ввожу даты, получаю количество астероидов вблизи орбиты земли
+ Доп информация в response.jsoon
"""
import requests
import json
import datetime
API_KEY='0bDSGclMNHH56nn6zdOUp98kybn5FSW7jfEoazEF'
START_DATE ='2020-07-17'
END_DATE = '2020-07-22'# Дата окончания должна быть не далее 7 дней
try:
    A=(int((datetime.datetime.strptime(END_DATE,'%Y-%m-%d')-datetime.datetime.strptime(START_DATE,'%Y-%m-%d')).days)+1)
except:
    print('Даты введены неправльно')
try:
    if A>0:
        response = requests.get(f'https://api.nasa.gov/neo/rest/v1/feed?start_date={START_DATE}&end_date={END_DATE}&api_key={API_KEY}')
        with open('response.json', 'w') as f:
            json.dump(response.json(), f)
        data = response.json()
        print(f'Количесво астероидов с {START_DATE} по {END_DATE} пролетающих вблизи орбиты Земли -- {((int(data["element_count"]))//A)}')
    else:
        print('Порверьте даты')
except:
    print('Проверьте даты. Разница между START_DATE и END_DATE должна быть не более 7 дней')