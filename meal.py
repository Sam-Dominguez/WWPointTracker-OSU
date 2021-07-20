from getPoints import get_points_from_list
from pymongo import MongoClient

class Meal:

    def __init__(self, Restaurant: MongoClient):
        self.Restaurant: MongoClient = Restaurant
        self.items:[] = []
        self.points = 0

    def get_points(self):
        self.points = get_points_from_list(self.items, self.Restaurant)
        return self.points

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_items(self):
        for item in self.items:
            print(item['name'])