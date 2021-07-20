import requests
import json
from bs4 import BeautifulSoup
from pymongo import MongoClient

def get_points(calories, sugar, satFat, protein):
    url = 'https://www.calculator.net/weight-watchers-points-calculator.html?w5energy=%s&w5energyunit=1&w5sugar=%s&w5sugarunit=1&w5sfat=%s&w5sfatunit=1&w5protein=%s&w5proteinunit=1&caltype=5&x=53&y=29#lastestpoint' % (calories, sugar, satFat, protein)

    r = requests.get(url)

    soup = BeautifulSoup(r.text, "html.parser")

    options = soup.find_all('b')

    return int(options[0].string.replace(' Points', ''))

def get_points_from_list(items:[], collection_name: MongoClient)->int:
    total_points = 0

    # loop through food items for that restautant collection
    for item in items:
        # if that item has points stored, get value
        points = item.get('points')

        # else query website for point total and store result in db
        if not points:
            points = get_points(item['calories'], item['sugar'], item['saturatedFat'], item['protein'])
            collection_name.update_one({"_id": item["_id"]}, {"$set": {"points": points}})

        total_points += points

    return total_points

