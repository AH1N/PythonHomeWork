import requests
import json

def change(value):
    res = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
    data = res.json()
    info = ""
    value = value.upper()
    if value in data['Valute']:
        info = f"Курс {data['Valute'][value]['Name']} - {data['Valute'][value]['Value']}"
    else:
        info = "ВЫ ВВЕЛИ КАКУЮ-ТО ЕРУНДУ"
    return info

def wht_valutes():
    res = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
    data = res.json()
    res_valutes = ""
    for key in data['Valute']:
        v =  data['Valute'][key]['Value']
        res_valutes += f"{key} - {v}\n"
    return res_valutes
