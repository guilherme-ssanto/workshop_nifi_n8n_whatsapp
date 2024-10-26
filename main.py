import requests
from tinydb import TinyDB, Query
from datetime import datetime

db = TinyDB("bando_de_dados.json")

def get_price():
    url = ""
    response  = requests.get(url)
    return response.json()

def calculate_kpis(price_data):
    price_usd = price_data['data']['amount']
    price_real = float(price_usd) * 5.5
    price_data['price_real'] = price_real
    return price_data

def save_data(data):
    db.insert({**data, "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})

if __name__ == "__main__":
    price_usd = get_price()
    price_real = calculate_kpis(price_usd)
    save_data(price_usd)
    save_data(price_real)