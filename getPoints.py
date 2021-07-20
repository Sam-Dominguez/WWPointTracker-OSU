import requests
import json
from bs4 import BeautifulSoup

def getPoints(calories, sugar, satFat, protein):
    url = 'https://www.calculator.net/weight-watchers-points-calculator.html?w5energy=%s&w5energyunit=1&w5sugar=%s&w5sugarunit=1&w5sfat=%s&w5sfatunit=1&w5protein=%s&w5proteinunit=1&caltype=5&x=53&y=29#lastestpoint' % (calories, sugar, satFat, protein)

    r = requests.get(url)

    soup = BeautifulSoup(r.text, "html.parser")

    options = soup.find_all('b')

    return int(options[0].string.replace(' Points', ''))